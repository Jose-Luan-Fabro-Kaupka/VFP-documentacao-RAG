#!/usr/bin/env python3
"""
Busca na ajuda do VFP 9 para que os fatos venham da documentação,
e não dos pesos do modelo.

O índice mistura dois tipos de passagem:

  ficha  cartão de referência em português montado a partir da página
         Markdown (assinatura completa, parâmetros e valor de retorno);
  ajuda  o tópico Markdown em português inteiro (sem fatiar por título
         nem por orçamento de caracteres), usado quando a ficha não basta.

A recuperação combina três sinais, fundidos por rank recíproco:

  nome exato  a pergunta cita um identificador ("STRTRAN", "SYS(2015)");
              é a evidência mais forte e ganha um bônus fixo;
  BM25        sobreposição lexical, o peso principal nas buscas por nome;
  embeddings  vetores densos opcionais, que fazem paráfrases funcionarem
              ("como removo espaços à direita" -> RTRIM).

A metade lexical não precisa de modelo: o índice já serve antes dos
embeddings.

Subcomandos:
  build    monta data/rag/index.jsonl a partir de markdown_pt, topics.jsonl e fichas PT
  embed    codifica as passagens em data/rag/embeddings.npy
  search   mostra o que seria recuperado para uma pergunta
  serve    API HTTP para a equipe (um processo, encoder carregado uma vez)
  answer   recupera e pede a um modelo local (Ollama) para responder com os trechos
  eval     mede o recall da recuperação em perguntas geradas e escritas à mão
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import threading
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Sequence
from urllib.parse import parse_qs, urlparse

from build_signature_dataset import build_complete_card, render_card
from md_paths import topic_markdown_index

ROOT = Path(__file__).resolve().parent.parent
TOPICS_PATH = ROOT / "data" / "topics.jsonl"
CARD_PATHS = [
    ROOT / "data" / "training" / "train_sig_pt.jsonl",
    ROOT / "data" / "training" / "val_sig_pt.jsonl",
]
INDEX_PATH = ROOT / "data" / "rag" / "index.jsonl"
EMBEDDINGS_PATH = ROOT / "data" / "rag" / "embeddings.npy"
MD_PT_DIR = ROOT / "data" / "markdown_pt"
EMBEDDING_MODEL = "intfloat/multilingual-e5-small"

MIN_TOPIC_CHARS = 80
MAX_RETURN_CHARS = 900

TITLE_SUFFIXES = (
    " Command",
    " Function",
    " Functions",
    " Property",
    " Method",
    " Event",
    " Object",
    " Class",
    " Keyword",
    " Overview",
)


# --------------------------------------------------------------------------
# tratamento de texto
# --------------------------------------------------------------------------

TOKEN_RE = re.compile(r"[a-z0-9_]+")
SYS_CALL_RE = re.compile(r"\b([a-z]{2,})\s*\(\s*(\d+)\s*\)")


def strip_accents(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def tokenize(text: str) -> list[str]:
    """Tokens alfanuméricos em minúsculas, mais um token colado para chamadas tipo SYS(2015)."""
    lowered = strip_accents(text).lower()
    tokens = TOKEN_RE.findall(lowered)
    tokens.extend(f"{name}{number}" for name, number in SYS_CALL_RE.findall(lowered))
    return tokens


ERROR_RE = re.compile(r"\(Error (\d+)\)\s*$")
# Um desambiguador é um parêntese precedido de espaço, o que separa
# 'REPLACE Command (Visual FoxPro)' de 'SYS(2015)'.
DISAMBIGUATOR_RE = re.compile(r"\s+\([^()]*\)$")


def canonical_name(title: str) -> str:
    """'STRTRAN( ) Function' -> 'STRTRAN'; 'SYS(2015) - Unique ...' -> 'SYS(2015)'."""
    name = title.split(" - ")[0].strip()
    name = DISAMBIGUATOR_RE.sub("", name).strip()
    for suffix in TITLE_SUFFIXES:
        if name.endswith(suffix):
            name = name[: -len(suffix)].strip()
            break
    name = re.sub(r"\(\s*\)$", "", name).strip()
    return name


def name_key(name: str) -> str:
    """Forma tokenizada usada para achar um nome dentro da pergunta.

    Colapsar em tokens unidos por espaço faz toda grafia do mesmo
    identificador convergir: 'SYS(2015)', 'SYS( 2015 )' e 'SYS 2015'
    viram 'sys 2015'.
    """
    return " ".join(TOKEN_RE.findall(strip_accents(name).lower()))


def name_variants(title: str) -> list[str]:
    """Todas as grafias do identificador do tópico que uma pergunta pode usar."""
    error = ERROR_RE.search(title)
    if error:
        return [f"Error {error.group(1)}", f"Erro {error.group(1)}"]
    name = canonical_name(title)
    if not name or len(name) > 40 or len(name) < 3:
        return []
    variants = [name]
    if "..." in name:
        for part in name.split("..."):
            part = part.strip(" .")
            if 3 <= len(part) <= 40:
                variants.append(part)
    unique: list[str] = []
    seen: set[str] = set()
    for variant in variants:
        key = name_key(variant)
        if key and key not in seen:
            seen.add(key)
            unique.append(variant)
    return unique


QUERY_EXPANSIONS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"percorr|loop (?:n|d)os regist|todos os regist", re.I), "SCAN"),
    (re.compile(r"área de trabalho|work ?area", re.I), "USE"),
    (re.compile(r"num[eé]rico em caractere|n[uú]mero em (?:string|caractere)", re.I), "TRANSFORM STR"),
    (re.compile(r"capturo erros|tratamento de erro|erros em tempo de execu", re.I), "ON ERROR TRY"),
    (re.compile(r"índice composto|index composto", re.I), "INDEX"),
    (re.compile(r"transa[cç][aã]o", re.I), "BEGIN TRANSACTION"),
]


def expand_query(query: str) -> str:
    extra = [terms for pattern, terms in QUERY_EXPANSIONS if pattern.search(query)]
    return f"{query} {' '.join(extra)}".strip() if extra else query


QUERY_KIND_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bcomand[oa]s?\b", re.I), "Command"),
    (re.compile(r"\bfun[cç][aã]o(?:es)?\b", re.I), "Function"),
    (re.compile(r"\bpropriedades?\b", re.I), "Property"),
    (re.compile(r"\bm[eé]todos?\b", re.I), "Method"),
    (re.compile(r"\beventos?\b", re.I), "Event"),
]
BARE_PARENS_RE = re.compile(r"\b[a-z_][\w]*\s*\(\s*\)", re.I)
EXAMPLE_QUERY_RE = re.compile(r"\bexempl[oa]s?\b|\bexamples?\b", re.I)
EXAMPLE_SECTIONS = frozenset({"exemplo", "exemplos", "example", "examples"})
# Prosa que a ficha compacta não traz (observações, how-to, erros).
FULL_PAGE_QUERY_RE = re.compile(
    r"\bexempl[oa]s?\b|\bexamples?\b|"
    r"observa[cç]|\bremarks?\b|"
    r"\berros?\b|\berror\b|"
    r"\bcomo\b|\bpor ?que\b|\bporque\b|"
    r"\bcomportamento\b",
    re.I,
)


def title_kind(title: str) -> str | None:
    """'SEEK Command' -> 'Command'; 'SYS(2015) - Unique …' -> None."""
    head = DISAMBIGUATOR_RE.sub("", title.split(" - ")[0].strip())
    for suffix in TITLE_SUFFIXES:
        if head.endswith(suffix):
            return suffix.strip()
    return None


def query_kind(query: str) -> str | None:
    """Command vs Function (etc.) conforme a própria pergunta nomeia."""
    for pattern, kind in QUERY_KIND_PATTERNS:
        if pattern.search(query):
            return kind
    if BARE_PARENS_RE.search(query):
        return "Function"
    return None


def kind_compatible(title: str, wanted: str | None) -> bool:
    if not wanted:
        return True
    got = title_kind(title)
    return got is None or got == wanted


def disambiguator_tokens(title: str) -> set[str]:
    """Tokens depois do primeiro ' - ', menos o próprio identificador (o SELECT permanece)."""
    parts = title.split(" - ", 1)
    if len(parts) < 2:
        return set()
    return set(tokenize(parts[1])) - set(tokenize(parts[0]))


def is_example_section(section: str) -> bool:
    return strip_accents(section).lower() in EXAMPLE_SECTIONS


def section_priority(entry: dict) -> tuple[int, int]:
    """Ficha primeiro, depois o tópico Markdown inteiro."""
    if entry["kind"] == "ficha":
        return (0, 0)
    return (1, 0)


# --------------------------------------------------------------------------
# construção do índice
# --------------------------------------------------------------------------

HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")

CARD_QUESTION_RE = re.compile(r"^Ficha de refer[eê]ncia de (.+?) no Visual FoxPro 9\.?$")


def load_cards() -> dict[str, str]:
    """Mapeia o assunto da ficha (como escrito na pergunta) para a resposta."""
    cards: dict[str, str] = {}
    for path in CARD_PATHS:
        if not path.exists():
            continue
        for line in path.open(encoding="utf-8"):
            messages = json.loads(line)["messages"]
            question = next(m["content"] for m in messages if m["role"] == "user")
            answer = next(m["content"] for m in messages if m["role"] == "assistant")
            match = CARD_QUESTION_RE.match(question.strip())
            if match:
                cards[match.group(1).strip()] = answer.strip()
    return cards


def card_key(title: str) -> str:
    """As fichas são tituladas com o tópico sem o sufixo ' Command'/' Function'."""
    subject = title.split(" - ")[0].strip()
    for suffix in TITLE_SUFFIXES:
        if subject.endswith(suffix):
            return subject[: -len(suffix)].strip()
    return subject


def markdown_body(text: str) -> str:
    """Remove o H1 inicial para o corpo da página não repetir o título do tópico."""
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and HEADING_RE.match(lines[0]):
        lines = lines[1:]
    return "\n".join(lines).strip()


def topic_help_text(topic: dict, md_index: dict[str, Path]) -> tuple[str, str]:
    """Devolve (corpo Markdown, idioma). Prefere o arquivo PT; senão, topics.jsonl."""
    path = md_index.get(topic["id"].lower())
    if path is not None and path.exists():
        return markdown_body(path.read_text(encoding="utf-8")), "pt"
    return topic.get("content") or "", "en"


def build_index(verbose: bool = True, md_dir: Path = MD_PT_DIR) -> list[dict]:
    topics = [json.loads(line) for line in TOPICS_PATH.open(encoding="utf-8")]
    cards = load_cards()
    md_index = topic_markdown_index(md_dir, topics)

    entries: list[dict] = []
    matched = 0
    from_markdown = 0
    missing_pt = 0
    for topic in topics:
        title = topic["title"]
        names = name_variants(title)
        base = {
            "topic_id": topic["id"],
            "title": title,
            "path": topic.get("category", ""),
            "names": names,
        }

        content, lang = topic_help_text(topic, md_index)
        if lang == "en":
            missing_pt += 1

        complete = build_complete_card(title, content) if content else None
        if complete:
            complete["topic_id"] = topic["id"]
            card = render_card(complete)
            from_markdown += 1
        else:
            card = cards.get(title) or cards.get(card_key(title))
        if card:
            matched += 1
            entries.append(
                {**base, "id": f"{topic['id']}#ficha", "kind": "ficha",
                 "section": "Ficha de referência", "text": card, "lang": "pt"}
            )

        if len(content) >= MIN_TOPIC_CHARS:
            entries.append(
                {**base, "id": f"{topic['id']}#topico", "kind": "ajuda",
                 "section": "Tópico", "text": content, "lang": lang}
            )

    if verbose:
        fichas = sum(1 for e in entries if e["kind"] == "ficha")
        ajuda_pt = sum(1 for e in entries if e["kind"] == "ajuda" and e.get("lang") == "pt")
        ajuda_en = sum(1 for e in entries if e["kind"] == "ajuda" and e.get("lang") != "pt")
        print(f"tópicos ...... {len(topics)}")
        print(f"fichas PT .... {from_markdown} do markdown, "
              f"{matched - from_markdown} da ficha curta, {matched} no total")
        print(f"markdown PT .. {len(topics) - missing_pt} tópicos, {missing_pt} sem arquivo PT")
        print(f"passagens .... {len(entries)} ({fichas} fichas, {ajuda_pt} ajuda PT, {ajuda_en} ajuda EN)")
    return entries


def save_index(entries: Sequence[dict], path: Path = INDEX_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
    size = path.stat().st_size / 1e6
    print(f"gravado em {path.relative_to(ROOT)} ({size:.1f} MB)")


# --------------------------------------------------------------------------
# recuperação
# --------------------------------------------------------------------------

K1 = 1.5
B = 0.75
RRF_K = 60.0
RRF_DEPTH = 150
WEIGHT_LEXICAL = 1.0
WEIGHT_DENSE = 1.0
NAME_BONUS = 1.0
FICHA_BONUS = 0.15


@dataclass
class Hit:
    entry: dict
    score: float
    exact: bool


def embedding_text(entry: dict) -> str:
    """Texto que entra no encoder. O E5 exige o prefixo 'passage: '."""
    return f"passage: {entry['title']} — {entry['section']}\n{entry['text'][:1000]}"


@dataclass
class Retriever:
    entries: list[dict]
    postings: dict[str, list[tuple[int, int]]] = field(default_factory=dict)
    lengths: list[int] = field(default_factory=list)
    average_length: float = 0.0
    names: dict[str, set[int]] = field(default_factory=dict)
    max_name_tokens: int = 1
    embeddings: "object | None" = None
    _encoder: "object | None" = None
    _encode_lock: threading.Lock = field(default_factory=threading.Lock)

    @classmethod
    def load(cls, path: Path = INDEX_PATH, with_embeddings: bool = True) -> "Retriever":
        if not path.exists():
            raise SystemExit(
                f"índice ausente em {path}. Rode primeiro: python scripts/rag.py build"
            )
        entries = [json.loads(line) for line in path.open(encoding="utf-8")]
        retriever = cls.from_entries(entries)
        if with_embeddings and EMBEDDINGS_PATH.exists():
            import numpy as np

            matrix = np.load(EMBEDDINGS_PATH)
            if len(matrix) != len(entries):
                print(
                    f"aviso: embeddings ({len(matrix)}) não batem com o índice "
                    f"({len(entries)}); rode 'embed' de novo. Seguindo só com BM25.",
                    file=sys.stderr,
                )
            else:
                retriever.embeddings = matrix.astype("float32")
        return retriever

    @classmethod
    def from_entries(cls, entries: list[dict]) -> "Retriever":
        postings: dict[str, list[tuple[int, int]]] = defaultdict(list)
        lengths: list[int] = []
        names: dict[str, set[int]] = defaultdict(set)
        max_name_tokens = 1

        for position, entry in enumerate(entries):
            searchable = f"{entry['title']}\n{entry['section']}\n{entry['text']}"
            counts = Counter(tokenize(searchable))
            for token, count in counts.items():
                postings[token].append((position, count))
            lengths.append(sum(counts.values()) or 1)
            for name in entry["names"]:
                key = name_key(name)
                if not key:
                    continue
                names[key].add(position)
                max_name_tokens = max(max_name_tokens, key.count(" ") + 1)

        return cls(
            entries=entries,
            postings=dict(postings),
            lengths=lengths,
            average_length=sum(lengths) / max(len(lengths), 1),
            names=dict(names),
            max_name_tokens=max_name_tokens,
        )

    # -- ranqueadores individuais -------------------------------------------

    def matching_names(self, query: str) -> set[int]:
        """Posições cujo identificador aparece literalmente na pergunta.

        Percorre os n-gramas de tokens da pergunta contra a tabela de nomes,
        bem mais barato do que testar uma regex por identificador conhecido.
        """
        tokens = TOKEN_RE.findall(strip_accents(query).lower())
        hits: set[int] = set()
        for start in range(len(tokens)):
            for size in range(1, min(self.max_name_tokens, len(tokens) - start) + 1):
                positions = self.names.get(" ".join(tokens[start : start + size]))
                if positions:
                    hits |= positions
        return hits

    def rank_lexical(self, query: str, depth: int = RRF_DEPTH) -> list[int]:
        total = len(self.entries)
        scores: dict[int, float] = defaultdict(float)
        for token in set(tokenize(query)):
            posting = self.postings.get(token)
            if not posting:
                continue
            idf = math.log(1 + (total - len(posting) + 0.5) / (len(posting) + 0.5))
            for position, count in posting:
                norm = 1 - B + B * self.lengths[position] / self.average_length
                scores[position] += idf * count * (K1 + 1) / (count + K1 * norm)
        ordered = sorted(scores, key=lambda position: -scores[position])
        return ordered[:depth]

    def encoder(self):
        if self._encoder is None:
            from sentence_transformers import SentenceTransformer

            self._encoder = SentenceTransformer(EMBEDDING_MODEL, device=pick_device())
        return self._encoder

    def rank_dense(self, query: str, depth: int = RRF_DEPTH) -> list[int]:
        if self.embeddings is None:
            return []
        import numpy as np

        vector = self.encoder().encode(
            [f"query: {query}"], normalize_embeddings=True, show_progress_bar=False
        )[0].astype("float32")
        similarity = self.embeddings @ vector
        depth = min(depth, len(similarity))
        top = np.argpartition(-similarity, depth - 1)[:depth]
        return [int(position) for position in top[np.argsort(-similarity[top])]]

    # -- fusão --------------------------------------------------------------

    def search(self, query: str, k: int = 5, per_topic: int = 1) -> list[Hit]:
        fused: dict[int, float] = defaultdict(float)
        query = expand_query(query)
        wanted_kind = query_kind(query)
        want_example = bool(EXAMPLE_QUERY_RE.search(query))
        want_full_page = bool(FULL_PAGE_QUERY_RE.search(query))
        exact = self.matching_names(query)
        named = {
            position for position in exact
            if kind_compatible(self.entries[position]["title"], wanted_kind)
        }
        if not named:
            named = exact
        query_tokens = set(tokenize(query))
        tight: set[int] = set()
        for position in named:
            extra = disambiguator_tokens(self.entries[position]["title"])
            if not extra or extra & query_tokens:
                tight.add(position)
        if tight:
            tight_stems = {
                name_key(canonical_name(self.entries[position]["title"]))
                for position in tight
            }
            named = {
                position for position in named
                if position in tight
                or name_key(canonical_name(self.entries[position]["title"]))
                not in tight_stems
            }

        for rank, position in enumerate(self.rank_lexical(query)):
            fused[position] += WEIGHT_LEXICAL / (RRF_K + rank)
        if self.embeddings is not None and not exact:
            with self._encode_lock:
                dense_ranks = self.rank_dense(query)
            for rank, position in enumerate(dense_ranks):
                fused[position] += WEIGHT_DENSE / (RRF_K + rank)

        for position in named:
            fused[position] += NAME_BONUS / (RRF_K)
        for position, score in list(fused.items()):
            if self.entries[position]["kind"] == "ficha":
                fused[position] = score * (1 + FICHA_BONUS)

        ordered = sorted(fused.items(), key=lambda item: -item[1])

        def usable(entry: dict) -> bool:
            return want_example or not is_example_section(entry["section"])

        hits: list[Hit] = []
        if named:
            by_topic: dict[str, list[int]] = defaultdict(list)
            topic_score: dict[str, float] = {}
            for position, score in ordered:
                if position not in named:
                    continue
                entry = self.entries[position]
                if not usable(entry):
                    continue
                by_topic[entry["topic_id"]].append(position)
                topic_score[entry["topic_id"]] = max(
                    topic_score.get(entry["topic_id"], score), score
                )
            ranked_topics = sorted(topic_score, key=lambda tid: -topic_score[tid])
            picked: dict[str, list[int]] = {}
            def choose(positions: list[int]) -> int:
                """Uma passagem por tópico: ficha para sintaxe, página quando a pergunta pede prosa."""
                ranked = sorted(
                    positions,
                    key=lambda pos: (section_priority(self.entries[pos]), pos),
                )
                fichas = [p for p in ranked if self.entries[p]["kind"] == "ficha"]
                pages = [p for p in ranked if self.entries[p]["kind"] != "ficha"]
                if want_full_page:
                    return (pages or fichas)[0]
                return (fichas or pages)[0]

            for topic_id in ranked_topics:
                picked[topic_id] = [choose(by_topic[topic_id])]

            def add(position: int) -> bool:
                hits.append(Hit(
                    entry=self.entries[position],
                    score=fused[position],
                    exact=position in exact,
                ))
                return len(hits) >= k

            # Nunca empilhar ficha + página do mesmo tópico. Vários identificadores:
            # um hit cada, para SEEK vs LOCATE ainda ver os dois.
            order = [picked[tid][0] for tid in ranked_topics]
            for position in order:
                if add(position):
                    return hits
            return hits

        seen: Counter[str] = Counter()
        for position, score in ordered:
            entry = self.entries[position]
            if not usable(entry) or seen[entry["topic_id"]] >= per_topic:
                continue
            seen[entry["topic_id"]] += 1
            hits.append(Hit(entry=entry, score=score, exact=False))
            if len(hits) >= k:
                break
        return hits


def pick_device() -> str:
    try:
        import torch

        if torch.backends.mps.is_available():
            return "mps"
        if torch.cuda.is_available():
            return "cuda"
    except Exception:
        pass
    return "cpu"


def embed_index(batch_size: int = 64) -> None:
    import numpy as np
    from sentence_transformers import SentenceTransformer

    entries = [json.loads(line) for line in INDEX_PATH.open(encoding="utf-8")]
    device = pick_device()
    print(f"codificando {len(entries)} passagens com {EMBEDDING_MODEL} em {device}...")
    model = SentenceTransformer(EMBEDDING_MODEL, device=device)
    matrix = model.encode(
        [embedding_text(entry) for entry in entries],
        batch_size=batch_size,
        normalize_embeddings=True,
        show_progress_bar=True,
    ).astype("float16")
    EMBEDDINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    np.save(EMBEDDINGS_PATH, matrix)
    print(
        f"gravado em {EMBEDDINGS_PATH.relative_to(ROOT)} "
        f"({matrix.nbytes / 1e6:.1f} MB, {matrix.shape[1]} dimensões)"
    )


# --------------------------------------------------------------------------
# montagem do prompt
# --------------------------------------------------------------------------

SYSTEM_PROMPT = (
    "Você é um assistente especializado em Microsoft Visual FoxPro 9.\n"
    "Responda SOMENTE com base nos trechos da documentação fornecidos abaixo.\n"
    "Se os trechos não contiverem a resposta, diga exatamente: "
    '"Não encontrei isso na documentação."\n'
    "Nunca invente nomes de parâmetros, valores de retorno ou comportamento.\n"
    "Cite o título do tópico que sustenta a resposta. Responda em português."
)


def clip_text(text: str, limit: int = MAX_RETURN_CHARS) -> str:
    if len(text) <= limit:
        return text
    clipped = text[:limit].rsplit("\n", 1)[0].rstrip()
    if len(clipped) < limit // 2:
        clipped = text[:limit].rstrip()
    return clipped + "\n…"


def passage_text(entry: dict, *, exact: bool = False) -> str:
    """Devolve a página armazenada. As páginas não são recortadas; `exact` não é usado."""
    return entry["text"]


def format_passages(hits: Sequence[Hit]) -> str:
    blocks = []
    for number, hit in enumerate(hits, start=1):
        entry = hit.entry
        blocks.append(
            f"[{number}] {entry['title']} — {entry['section']}\n"
            f"{passage_text(entry, exact=hit.exact)}"
        )
    return "\n\n".join(blocks)


def hits_as_json(query: str, hits: Sequence[Hit]) -> dict:
    return {
        "query": query,
        "hits": [
            {
                "title": hit.entry["title"],
                "section": hit.entry["section"],
                "kind": hit.entry["kind"],
                "score": round(hit.score, 4),
                "exact": hit.exact,
                "text": passage_text(hit.entry, exact=hit.exact),
            }
            for hit in hits
        ],
    }


def build_messages(question: str, hits: Sequence[Hit]) -> list[dict]:
    context = format_passages(hits)
    return [
        {"role": "system", "content": f"{SYSTEM_PROMPT}\n\n=== DOCUMENTAÇÃO ===\n{context}"},
        {"role": "user", "content": question},
    ]


# --------------------------------------------------------------------------
# resposta via servidor Ollama local
# --------------------------------------------------------------------------


def ask_ollama(messages: list[dict], model: str, host: str) -> str:
    import urllib.error
    import urllib.request

    payload = json.dumps(
        {
            "model": model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": 0.2, "num_ctx": 8192},
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        f"{host.rstrip('/')}/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            return json.load(response)["message"]["content"]
    except urllib.error.URLError as error:
        raise SystemExit(
            f"não consegui falar com o Ollama em {host} ({error}).\n"
            "Suba o servidor com 'ollama serve' e confira o nome do modelo."
        )


# --------------------------------------------------------------------------
# avaliação
# --------------------------------------------------------------------------

# Perguntas que um desenvolvedor faria, com todo tópico que as responde.
# As quatro primeiras são as que o modelo afinado errou de memória.
HAND_WRITTEN_QUERIES: list[tuple[str, tuple[str, ...]]] = [
    ("O que a função SYS(2015) retorna?", ("SYS(2015)",)),
    ("Para que serve SET DELETED ON?", ("SET DELETED",)),
    ("Qual a diferença entre SEEK e LOCATE?", ("SEEK", "LOCATE")),
    ("Quais são os parâmetros de STRTRAN?", ("STRTRAN",)),
    ("Como declaro um array de duas dimensões?", ("DIMENSION", "DECLARE")),
    ("Como abro uma tabela em uma área de trabalho específica?", ("USE",)),
    ("Como faço para percorrer todos os registros de uma tabela?", ("SCAN ... ENDSCAN",)),
    ("Qual função converte um valor numérico em caractere?", ("TRANSFORM", "STR")),
    ("Como removo espaços em branco à direita de uma string?", ("RTRIM", "TRIM", "ALLTRIM")),
    ("O que faz o comando REPLACE?", ("REPLACE",)),
    ("Como capturo erros em tempo de execução?", ("ON ERROR", "TRY ... CATCH ... FINALLY")),
    ("Qual a diferença entre COPY TO e EXPORT?", ("COPY TO", "EXPORT")),
    ("Como crio um índice composto?", ("INDEX",)),
    ("Como abro uma transação?", ("BEGIN TRANSACTION",)),
    ("O que a função EMPTY( ) considera vazio?", ("EMPTY",)),
    ("O que significa o erro 1429?", ("(Error 1429)",)),
    ("Como resolvo o erro 1830?", ("(Error 1830)",)),
    ("Explique o comando SEEK", ("SEEK Command",)),
    ("O que a função SEEK() retorna?", ("SEEK( ) Function",)),
]


def matches_expected(title: str, expected: str) -> bool:
    if expected.startswith("(Error"):
        return expected.upper() in title.upper()
    if expected.endswith(" Command") or expected.endswith(" Function"):
        return title.lower() == expected.lower()
    return canonical_name(title).upper() == expected.upper()


def evaluate(retriever: Retriever, k: int, sample: int, seed: int) -> None:
    import random

    print(f"=== perguntas escritas à mão (top-{k}) ===")
    acertos = 0
    for question, expected in HAND_WRITTEN_QUERIES:
        hits = retriever.search(question, k=k)
        titles = [hit.entry["title"] for hit in hits]
        ok = any(matches_expected(title, alvo) for title in titles for alvo in expected)
        acertos += ok
        marca = "ok  " if ok else "FALHA"
        print(f"  {marca} {question}")
        if not ok:
            print(f"        esperado {list(expected)}, veio {[canonical_name(t) for t in titles]}")
    print(f"  recall: {acertos}/{len(HAND_WRITTEN_QUERIES)}")

    # Perguntas sintéticas: pedir um tópico pelo nome e conferir se ele volta.
    random.seed(seed)
    candidates = sorted(
        {
            entry["title"]
            for entry in retriever.entries
            if entry["names"] and entry["kind"] == "ficha"
        }
    )
    chosen = random.sample(candidates, min(sample, len(candidates)))
    padroes = [
        "Qual a sintaxe de {}?",
        "Quais os parâmetros de {} no VFP9?",
        "Para que serve {}?",
        "O que {} retorna?",
    ]
    print(f"\n=== perguntas geradas: {len(chosen)} tópicos x {len(padroes)} formas (top-{k}) ===")
    total = 0
    encontrados = 0
    primeiro = 0
    for title in chosen:
        name = canonical_name(title)
        for padrao in padroes:
            hits = retriever.search(padrao.format(name), k=k)
            titles = [hit.entry["title"] for hit in hits]
            total += 1
            if title in titles:
                encontrados += 1
                primeiro += titles[0] == title
    print(f"  recall@{k}: {encontrados}/{total} ({100 * encontrados / total:.1f}%)")
    print(f"  acerto na 1a posição: {primeiro}/{total} ({100 * primeiro / total:.1f}%)")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def cmd_build(args: argparse.Namespace) -> None:
    entries = build_index(md_dir=args.md_dir)
    save_index(entries)


def cmd_embed(args: argparse.Namespace) -> None:
    embed_index(batch_size=args.lote)


def cmd_search(args: argparse.Namespace) -> None:
    retriever = Retriever.load()
    hits = retriever.search(args.pergunta, k=args.k)
    if not hits:
        print("nada encontrado.")
        return
    for number, hit in enumerate(hits, start=1):
        entry = hit.entry
        marca = " [nome exato]" if hit.exact else ""
        print(f"\n[{number}] {entry['title']} — {entry['section']} "
              f"({entry['kind']}, score {hit.score:.4f}){marca}")
        texto = entry["text"] if args.completo else clip_text(entry["text"])
        print(texto)


def cmd_serve(args: argparse.Namespace) -> None:
    """Um processo duradouro para 7–8 Cursors compartilharem um único encoder e5."""
    retriever = Retriever.load()
    if retriever.embeddings is not None:
        retriever.encoder()
        retriever.search("como removo espaços à direita", k=1)
    print(
        f"RAG em http://{args.host}:{args.port}/search "
        f"({len(retriever.entries)} passagens). GET /search?q=...&k=4",
        flush=True,
    )

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *log_args: object) -> None:
            sys.stderr.write("%s - %s\n" % (self.address_string(), format % log_args))

        def _send_json(self, payload: dict, status: int = 200) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            if parsed.path in {"/", "/health"}:
                self._send_json({"ok": True, "passages": len(retriever.entries)})
                return
            if parsed.path != "/search":
                self._send_json({"error": "not found"}, 404)
                return
            params = parse_qs(parsed.query)
            query = (params.get("q") or params.get("query") or [""])[0].strip()
            if not query:
                self._send_json({"error": "missing q"}, 400)
                return
            try:
                k = int((params.get("k") or ["4"])[0])
            except ValueError:
                k = 4
            k = max(1, min(k, 8))
            hits = retriever.search(query, k=k)
            self._send_json(hits_as_json(query, hits))

        def do_POST(self) -> None:
            if urlparse(self.path).path != "/search":
                self._send_json({"error": "not found"}, 404)
                return
            length = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(length) if length else b"{}"
            try:
                payload = json.loads(raw.decode("utf-8"))
            except json.JSONDecodeError:
                self._send_json({"error": "invalid json"}, 400)
                return
            query = str(payload.get("q") or payload.get("query") or "").strip()
            if not query:
                self._send_json({"error": "missing q"}, 400)
                return
            k = payload.get("k", 4)
            try:
                k = max(1, min(int(k), 8))
            except (TypeError, ValueError):
                k = 4
            hits = retriever.search(query, k=k)
            self._send_json(hits_as_json(query, hits))

    try:
        ThreadingHTTPServer((args.host, args.port), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nencerrado.")


def cmd_answer(args: argparse.Namespace) -> None:
    retriever = Retriever.load()
    hits = retriever.search(args.pergunta, k=args.k)
    messages = build_messages(args.pergunta, hits)
    if args.mostrar_contexto:
        print(messages[0]["content"])
        print("\n" + "=" * 60 + "\n")
    print(ask_ollama(messages, model=args.modelo, host=args.host))
    print("\nfontes:")
    for number, hit in enumerate(hits, start=1):
        print(f"  [{number}] {hit.entry['title']} — {hit.entry['section']}")


def cmd_chat(args: argparse.Namespace) -> None:
    """Loop interativo, para o encoder ser carregado uma vez em vez de a cada pergunta."""
    retriever = Retriever.load()
    retriever.search("aquecimento")
    print(f"pronto ({len(retriever.entries)} passagens). Ctrl-D ou 'sair' para encerrar.\n")
    while True:
        try:
            pergunta = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if pergunta.lower() in {"sair", "exit", "quit"}:
            return
        if not pergunta:
            continue
        hits = retriever.search(pergunta, k=args.k)
        print(ask_ollama(build_messages(pergunta, hits), model=args.modelo, host=args.host))
        print("\nfontes: " + "; ".join(hit.entry["title"] for hit in hits) + "\n")


def cmd_eval(args: argparse.Namespace) -> None:
    retriever = Retriever.load(with_embeddings=not args.somente_lexico)
    modo = "BM25 + nome exato" if retriever.embeddings is None else "híbrido"
    print(f"modo: {modo}\n")
    evaluate(retriever, k=args.k, sample=args.amostra, seed=args.semente)


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("build", help="constrói o índice")
    p.add_argument(
        "--md-dir",
        type=Path,
        default=MD_PT_DIR,
        help="Diretório dos tópicos Markdown em pt-BR",
    )
    p.set_defaults(func=cmd_build)

    p = sub.add_parser("embed", help="codifica as passagens em vetores")
    p.add_argument("--lote", type=int, default=64)
    p.set_defaults(func=cmd_embed)

    p = sub.add_parser("search", help="mostra as passagens recuperadas")
    p.add_argument("pergunta")
    p.add_argument("-k", type=int, default=5)
    p.add_argument("--completo", action="store_true", help="não trunca o texto")
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("serve", help="API HTTP para o Cursor dos devs (um processo)")
    p.add_argument("--host", default="0.0.0.0")
    p.add_argument("--port", type=int, default=8765)
    p.set_defaults(func=cmd_serve)

    p = sub.add_parser("answer", help="recupera e responde via Ollama")
    p.add_argument("pergunta")
    p.add_argument("-k", type=int, default=4)
    p.add_argument("--modelo", default="vfp9")
    p.add_argument("--host", default="http://localhost:11434")
    p.add_argument("--mostrar-contexto", action="store_true")
    p.set_defaults(func=cmd_answer)

    p = sub.add_parser("chat", help="loop interativo de perguntas")
    p.add_argument("-k", type=int, default=4)
    p.add_argument("--modelo", default="vfp9")
    p.add_argument("--host", default="http://localhost:11434")
    p.set_defaults(func=cmd_chat)

    p = sub.add_parser("eval", help="mede o recall da recuperação")
    p.add_argument("-k", type=int, default=5)
    p.add_argument("--amostra", type=int, default=200)
    p.add_argument("--semente", type=int, default=7)
    p.add_argument("--somente-lexico", action="store_true", help="ignora os embeddings")
    p.set_defaults(func=cmd_eval)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
