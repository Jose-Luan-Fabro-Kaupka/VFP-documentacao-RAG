#!/usr/bin/env python3
"""
Traduz as respostas do assistente de um dataset em formato chat para
português do Brasil, sem mexer no código Visual FoxPro.

Cercas de código, código inline e identificadores VFP são mascarados com
sentinelas antes do texto chegar ao backend de tradução e restaurados depois,
para nenhum backend reescrever `.T.`, `ThisForm.Caption` ou um bloco
`DEFINE CLASS`. Cada segmento é validado após a tradução; o que falhar
conserva o inglês original em vez de corromper em silêncio.

As traduções ficam em cache SQLite chaveado por (backend, model, segment),
então uma execução interrompida retoma de onde parou.

Uso:
    # confere a tubulação sem um backend
    python translate_dataset.py --backend echo --limit 20 --report

    # Ollama local
    python translate_dataset.py --backend ollama --model qwen3:8b

    # qualquer endpoint compatível com OpenAI
    OPENAI_API_KEY=... python translate_dataset.py --backend openai --model gpt-4.1-mini
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

FENCE_RE = re.compile(r"```(?:\w+)?\n.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
# Sentinelas ASCII sobrevivem tanto a LLMs que seguem instruções quanto a
# modelos NMT simples, que tendem a droppar ou reescrever marcadores Unicode.
SENTINEL_RE = re.compile(r"\[\[([A-Z])(\d+)\]\]")

SYSTEM_PROMPT = (
    "Você é um tradutor técnico especializado em documentação de programação. "
    "Traduza o texto do inglês para o português do Brasil.\n"
    "REGRAS OBRIGATÓRIAS:\n"
    "1. Preserve EXATAMENTE os marcadores no formato [[C0]], [[I1]], [[T2]]. "
    "Não os traduza, não os reordene, não altere seus números.\n"
    "2. Preserve a formatação Markdown: títulos (##), negrito (**), listas (-), "
    "tabelas (|) e quebras de linha.\n"
    "3. NÃO traduza nomes de comandos, funções, propriedades, métodos, eventos, "
    "classes, parâmetros nem palavras-chave do Visual FoxPro. Exemplos que ficam "
    "em inglês: USE, SELECT, CursorAdapter, Caption, Visible, nWorkArea, .T., .F.\n"
    "4. Traduza apenas o texto explicativo. Use terminologia técnica natural do "
    "Brasil (arquivo, tabela, campo, registro, cadeia de caracteres, valor lógico).\n"
    "5. Responda SOMENTE com a tradução, sem comentários, sem preâmbulo e sem "
    "repetir o texto original."
)

# Termos que devem sobreviver à tradução mesmo quando aparecem como prosa.
GLOSSARY_PATTERNS = [
    r"\.(?:T|F|NULL)\.",
    r"\b[A-Za-z_][A-Za-z0-9_]*\s*\(\s*\)",        # SYS( ), _StrCpy()
    r"\b[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+\b",  # This.Caption
    # Nomes de comando, inclusive os de várias palavras como MODIFY REPORT ou SET TALK.
    r"\b[A-Z][A-Z0-9_]+(?:\s+[A-Z][A-Z0-9_]+)*\b",
    r"\b(?:[a-z]{1,3}[A-Z][A-Za-z0-9]+)\b",       # cFileName, nWorkArea, lExpression
    r"\b(?:Visual FoxPro|FoxPro)\b",
]
GLOSSARY_RE = re.compile("|".join(GLOSSARY_PATTERNS))


# --------------------------------------------------------------------------- #
# Mascaramento
# --------------------------------------------------------------------------- #
class Masker:
    """Replace code and protected terms with sentinels that survive translation."""

    def __init__(self, protect_terms: bool = True) -> None:
        self.protect_terms = protect_terms

    def mask(self, text: str) -> tuple[str, dict[str, str]]:
        store: dict[str, str] = {}
        counter = {"C": 0, "I": 0, "T": 0}

        def take(kind: str, value: str) -> str:
            key = f"[[{kind}{counter[kind]}]]"
            counter[kind] += 1
            store[key] = value
            return key

        text = FENCE_RE.sub(lambda m: take("C", m.group(0)), text)
        text = INLINE_CODE_RE.sub(lambda m: take("I", m.group(0)), text)
        if self.protect_terms:
            # Pula sentinelas já colocadas: o corpo (C0, I1) parece nome de
            # comando para o glossário, e aninhá-las estraga o marcador que o
            # tradutor precisa reproduzir.
            parts = []
            cursor = 0
            for marker in SENTINEL_RE.finditer(text):
                parts.append(GLOSSARY_RE.sub(lambda m: take("T", m.group(0)), text[cursor : marker.start()]))
                parts.append(marker.group(0))
                cursor = marker.end()
            parts.append(GLOSSARY_RE.sub(lambda m: take("T", m.group(0)), text[cursor:]))
            text = "".join(parts)
        return text, store

    @staticmethod
    def unmask(text: str, store: dict[str, str]) -> str:
        for _ in range(3):
            if not SENTINEL_RE.search(text):
                break
            text = SENTINEL_RE.sub(lambda m: store.get(m.group(0), m.group(0)), text)
        return text


def sentinel_keys(text: str) -> list[str]:
    return sorted(m.group(0) for m in SENTINEL_RE.finditer(text))


def validate(source: str, translated: str, store: dict[str, str]) -> str | None:
    """Return a rejection reason, or None when the translation is usable."""
    if not translated.strip():
        return "empty"
    if sentinel_keys(source) != sentinel_keys(translated):
        return "sentinel_mismatch"
    if source.count("|") != translated.count("|"):
        return "table_shape_changed"
    if source.count("**") != translated.count("**"):
        return "bold_markers_changed"
    src_headings = re.findall(r"(?m)^#{1,4}\s", source)
    dst_headings = re.findall(r"(?m)^#{1,4}\s", translated)
    if len(src_headings) != len(dst_headings):
        return "heading_count_changed"
    # Um backend que ecoa instruções ou enrola produz deriva selvagem de comprimento.
    ratio = len(translated) / max(len(source), 1)
    if ratio > 2.5 or ratio < 0.4:
        return "length_drift"
    if "[[" in translated and not store:
        return "stray_sentinel"
    return None


# --------------------------------------------------------------------------- #
# Backends
# --------------------------------------------------------------------------- #
def _post_json(url: str, payload: dict, headers: dict, timeout: int) -> dict:
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


class OllamaBackend:
    def __init__(self, model: str, host: str, timeout: int) -> None:
        self.model, self.host, self.timeout = model, host.rstrip("/"), timeout

    def translate(self, text: str) -> str:
        payload = {
            "model": self.model,
            "stream": False,
            "options": {"temperature": 0.1, "num_ctx": 8192},
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
        }
        result = _post_json(
            f"{self.host}/api/chat", payload, {"Content-Type": "application/json"}, self.timeout
        )
        return _strip_thinking(result["message"]["content"])


class OpenAIBackend:
    def __init__(self, model: str, base_url: str, api_key: str, timeout: int) -> None:
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    def translate(self, text: str) -> str:
        payload = {
            "model": self.model,
            "temperature": 0.1,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
        }
        result = _post_json(
            f"{self.base_url}/chat/completions",
            payload,
            {"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"},
            self.timeout,
        )
        return _strip_thinking(result["choices"][0]["message"]["content"])


class ArgosBackend:
    def __init__(self) -> None:
        import argostranslate.package
        import argostranslate.translate

        self._translate = argostranslate.translate
        installed = argostranslate.translate.get_installed_languages()
        codes = {lang.code for lang in installed}
        if not {"en", "pt"} <= codes:
            argostranslate.package.update_package_index()
            available = argostranslate.package.get_available_packages()
            package = next(p for p in available if p.from_code == "en" and p.to_code == "pt")
            argostranslate.package.install_from_path(package.download())

    def translate(self, text: str) -> str:
        return self._translate.translate(text, "en", "pt")


class EchoBackend:
    """No-op backend used to exercise masking, caching and validation."""

    def translate(self, text: str) -> str:
        return text


def _strip_thinking(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    return text.strip()


def load_dotenv(path: Path) -> None:
    """Read KEY=value pairs from a .env file without overriding real env vars."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def build_backend(args: argparse.Namespace):
    if args.backend == "ollama":
        return OllamaBackend(args.model, args.ollama_host, args.timeout)
    if args.backend == "openai":
        key = args.api_key or os.environ.get("OPENAI_API_KEY", "")
        if not key:
            raise SystemExit(
                "Backend 'openai' requires an API key.\n"
                "Set it with:  export OPENAI_API_KEY=sk-...\n"
                "or create a .env file in the repo root containing:\n"
                "  OPENAI_API_KEY=sk-..."
            )
        return OpenAIBackend(args.model, args.base_url, key, args.timeout)
    if args.backend == "argos":
        return ArgosBackend()
    return EchoBackend()


# --------------------------------------------------------------------------- #
# Cache
# --------------------------------------------------------------------------- #
class Cache:
    def __init__(self, path: Path) -> None:
        self.lock = threading.Lock()
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS tr (k TEXT PRIMARY KEY, v TEXT NOT NULL)"
        )
        self.conn.commit()

    def get(self, key: str) -> str | None:
        with self.lock:
            row = self.conn.execute("SELECT v FROM tr WHERE k = ?", (key,)).fetchone()
        return row[0] if row else None

    def put(self, key: str, value: str) -> None:
        with self.lock:
            self.conn.execute("INSERT OR REPLACE INTO tr VALUES (?, ?)", (key, value))
            self.conn.commit()


# --------------------------------------------------------------------------- #
# Pipeline
# --------------------------------------------------------------------------- #
def split_segments(text: str) -> list[str]:
    """Split on blank lines so each unit keeps its own markdown structure."""
    return re.split(r"(\n{2,})", text)


def answer_segments(answer: str, masker: Masker) -> tuple[list[str], list[dict[str, str]], list[bool]]:
    parts = split_segments(answer)
    masked_parts: list[str] = []
    stores: list[dict[str, str]] = []
    translatable: list[bool] = []
    for part in parts:
        if not part.strip() or re.fullmatch(r"\n{2,}", part):
            masked_parts.append(part)
            stores.append({})
            translatable.append(False)
            continue
        masked, store = masker.mask(part)
        # Só restaram sentinelas: código puro, sem prosa para traduzir.
        residue = SENTINEL_RE.sub("", masked).strip()
        masked_parts.append(masked)
        stores.append(store)
        translatable.append(bool(re.search(r"[A-Za-z]{3}", residue)))
    return masked_parts, stores, translatable


class Translator:
    def __init__(self, backend, cache: Cache, cache_key_prefix: str, retries: int) -> None:
        self.backend = backend
        self.cache = cache
        self.prefix = cache_key_prefix
        self.retries = retries
        self.stats = {"cached": 0, "translated": 0, "failed": 0}
        self.reasons: dict[str, int] = {}
        self.lock = threading.Lock()

    def _key(self, text: str) -> str:
        digest = hashlib.sha1(f"{self.prefix}\u0000{text}".encode("utf-8")).hexdigest()
        return digest

    def translate_segment(self, masked: str, store: dict[str, str]) -> str:
        key = self._key(masked)
        hit = self.cache.get(key)
        if hit is not None:
            with self.lock:
                self.stats["cached"] += 1
            return hit

        best = masked
        reason = "no_attempt"
        for attempt in range(self.retries + 1):
            try:
                candidate = self.backend.translate(masked)
            except (urllib.error.URLError, urllib.error.HTTPError, KeyError, TimeoutError) as exc:
                reason = f"backend_error:{type(exc).__name__}"
                time.sleep(1.5 * (attempt + 1))
                continue
            reason_now = validate(masked, candidate, store)
            if reason_now is None:
                best = candidate
                reason = None
                break
            reason = reason_now

        with self.lock:
            if reason is None:
                self.stats["translated"] += 1
            else:
                self.stats["failed"] += 1
                self.reasons[reason] = self.reasons.get(reason, 0) + 1
        self.cache.put(key, best)
        return best


def translate_answer(answer: str, masker: Masker, translator: Translator) -> str:
    parts, stores, translatable = answer_segments(answer, masker)
    out: list[str] = []
    for part, store, should in zip(parts, stores, translatable):
        text = translator.translate_segment(part, store) if should else part
        out.append(Masker.unmask(text, store))
    return "".join(out)


def estimate_pending(answers: list[dict], masker: Masker, translator: Translator) -> dict:
    """Count the work still to be sent to the backend, ignoring cached segments."""
    segments = chars = cached = 0
    seen: set[str] = set()
    for message in answers:
        parts, _, translatable = answer_segments(message["content"], masker)
        for part, should in zip(parts, translatable):
            if not should or part in seen:
                continue
            seen.add(part)
            if translator.cache.get(translator._key(part)) is not None:
                cached += 1
                continue
            segments += 1
            chars += len(part)
    return {"segments": segments, "chars": chars, "cached": cached}


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.open(encoding="utf-8") if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Translate dataset answers to PT-BR.")
    parser.add_argument("--input-dir", type=Path, default=root / "data/training")
    parser.add_argument("--files", nargs="+", default=["train_messages_pt.jsonl", "val_messages_pt.jsonl"])
    parser.add_argument("--suffix", default="_ptbr", help="Suffix for the translated output files")
    parser.add_argument("--backend", choices=["ollama", "openai", "argos", "echo"], default="echo")
    parser.add_argument("--model", default="qwen3:8b")
    parser.add_argument("--ollama-host", default="http://localhost:11434")
    parser.add_argument("--base-url", default="https://api.openai.com/v1")
    parser.add_argument("--api-key", default="")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--limit", type=int, default=0, help="Only process the first N rows")
    parser.add_argument("--no-protect-terms", action="store_true")
    parser.add_argument("--cache", type=Path, default=root / "data/training/.translation_cache.sqlite")
    parser.add_argument("--report", action="store_true", help="Print before/after samples")
    parser.add_argument(
        "--estimate-only",
        action="store_true",
        help="Report how much text would be sent to the backend, then stop",
    )
    return parser.parse_args()


def preflight(backend, args: argparse.Namespace) -> None:
    """
    Fail loudly before spending time or money.

    Segment failures fall back to the original English text, so a misconfigured
    backend would otherwise finish "successfully" with an untranslated dataset.
    """
    if args.backend == "echo":
        return
    probe = "The [[T0]] property specifies the caption of the control."
    try:
        result = backend.translate(probe)
    except Exception as exc:  # noqa: BLE001 - surface any backend failure verbatim
        raise SystemExit(f"Backend preflight failed: {type(exc).__name__}: {exc}")
    if not result.strip():
        raise SystemExit("Backend preflight returned an empty translation.")
    if "[[T0]]" not in result:
        print(
            "warning: backend dropped the [[T0]] placeholder in the preflight probe; "
            "expect a higher fallback rate",
            file=sys.stderr,
        )
    print(f"preflight ok -> {result.strip()[:120]}")


def main() -> int:
    args = parse_args()
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    backend = build_backend(args)
    preflight(backend, args)
    cache = Cache(args.cache)
    prefix = f"{args.backend}:{args.model}:v2"
    translator = Translator(backend, cache, prefix, args.retries)
    masker = Masker(protect_terms=not args.no_protect_terms)

    started = time.time()
    for filename in args.files:
        source = args.input_dir / filename
        if not source.exists():
            print(f"skip (missing): {source}", file=sys.stderr)
            continue
        rows = load_jsonl(source)
        if args.limit:
            rows = rows[: args.limit]

        answers = []
        for row in rows:
            for message in row["messages"]:
                if message["role"] == "assistant":
                    answers.append(message)

        pending = estimate_pending(answers, masker, translator)
        print(
            f"{filename}: {len(answers)} answers, "
            f"{pending['segments']} segments to send "
            f"({pending['chars']:,} chars, ~{pending['chars'] / 3.5:,.0f} input tokens); "
            f"{pending['cached']} already cached"
        )
        if args.estimate_only:
            continue
        print(f"  translating with {args.workers} workers...")
        done = {"n": 0}
        lock = threading.Lock()

        def work(message: dict) -> None:
            original = message["content"]
            message["content"] = translate_answer(original, masker, translator)
            with lock:
                done["n"] += 1
                if done["n"] % 200 == 0:
                    elapsed = time.time() - started
                    rate = done["n"] / max(elapsed, 1)
                    print(
                        f"  {done['n']}/{len(answers)} answers "
                        f"({rate:.1f}/s, segments ok={translator.stats['translated']} "
                        f"cached={translator.stats['cached']} failed={translator.stats['failed']})"
                    )

        if args.workers > 1:
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                list(pool.map(work, answers))
        else:
            for message in answers:
                work(message)

        target = args.input_dir / filename.replace(".jsonl", f"{args.suffix}.jsonl")
        write_jsonl(target, rows)
        print(f"  wrote {target} ({len(rows)} rows)")

        if args.report:
            print("\n--- sample ---")
            for row in rows[:3]:
                answer = next(m["content"] for m in row["messages"] if m["role"] == "assistant")
                print(answer[:400])
                print("  ...")

    print(
        f"\nsegments: translated={translator.stats['translated']} "
        f"cached={translator.stats['cached']} failed={translator.stats['failed']}"
    )
    if translator.reasons:
        print(f"failure reasons: {translator.reasons}")
    print(f"elapsed: {time.time() - started:.0f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
