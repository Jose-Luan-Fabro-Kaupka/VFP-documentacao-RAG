#!/usr/bin/env python3
"""
Pipeline EN -> pt-BR para passagens de 'ajuda' do RAG que ainda não têm ficha PT.

As fichas de assinatura já são traduzidas via translate_fields.py. Isto cobre
as seções longas (Observações, exemplos, how-tos) que ainda vêm em inglês.

Subcomandos:
    export   grava shards de tradução em data/translation/rag_shards/
    apply    valida os shards prontos e mescla em rag_pt.json
    status   relata cobertura
    audit    marca inconsistências de terminologia

Uso:
    python translate_rag.py export --shard-size 60
    python translate_rag.py apply
    python translate_rag.py status
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from html_utils import project_paths
from translate_dataset import Masker, SENTINEL_RE

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "data" / "rag" / "index.jsonl"
STORE_PATH = ROOT / "data" / "translation" / "rag_pt.json"
SHARD_DIR = ROOT / "data" / "translation" / "rag_shards"

TRANSLATOR_BRIEF = (
    "Traduza cada valor do inglês para o português do Brasil.\n"
    "Preserve EXATAMENTE os marcadores [[C0]], [[I1]], [[T2]] (mesma quantidade, mesmos números).\n"
    "Não traduza nomes de comandos, funções, propriedades, classes ou parâmetros do Visual FoxPro.\n"
    "Preserve blocos ```foxpro```, formatação Markdown (##, **, listas, tabelas) e quebras de linha.\n"
    "Traduza apenas o texto explicativo.\n"
    "Responda SOMENTE com o JSON traduzido, no mesmo formato e com as mesmas chaves."
)

ENGLISH_HINT = re.compile(
    r"\b(the|and|with|for|that|this|returns|specifies|contains|following|using)\b",
    re.I,
)


def load_index() -> list[dict]:
    return [json.loads(line) for line in INDEX_PATH.open(encoding="utf-8")]


def ficha_topic_ids(entries: list[dict]) -> set[str]:
    return {entry["topic_id"] for entry in entries if entry["kind"] == "ficha"}


def pending_passages(
    entries: list[dict],
    store: dict[str, str],
    *,
    only_without_ficha: bool = True,
) -> list[dict]:
    fichas = ficha_topic_ids(entries)
    pending = []
    for entry in entries:
        if entry["kind"] != "ajuda":
            continue
        if only_without_ficha and entry["topic_id"] in fichas:
            continue
        if entry["id"] in store:
            continue
        pending.append(entry)
    return pending


def validate_pair(source: str, translated: str) -> str | None:
    if not translated or not translated.strip():
        return "vazio"
    if sorted(SENTINEL_RE.findall(source)) != sorted(SENTINEL_RE.findall(translated)):
        return "marcadores alterados"
    ratio = len(translated) / max(len(source), 1)
    if ratio > 2.8 or ratio < 0.35:
        return "comprimento fora da faixa"
    if translated.strip() == source.strip() and len(source) > 60:
        return "não traduzido"
    return None


def shard_paths(directory: Path) -> list[Path]:
    return sorted(
        path
        for path in directory.glob("rag_shard_*.json")
        if not path.name.endswith((".map.json", ".pt.json"))
    )


def sibling(shard: Path, kind: str) -> Path:
    return shard.with_name(f"{shard.stem}.{kind}.json")


def load_store(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_export(args: argparse.Namespace) -> int:
    masker = Masker()
    entries = load_index()
    store = load_store(args.store)
    pending = pending_passages(entries, store, only_without_ficha=not args.all_ajuda)

    args.shard_dir.mkdir(parents=True, exist_ok=True)
    if args.clean:
        for old in args.shard_dir.glob("rag_shard_*"):
            old.unlink()

    written = 0
    for index in range(0, len(pending), args.shard_size):
        chunk = pending[index : index + args.shard_size]
        items: dict[str, str] = {}
        masks: dict[str, dict] = {}
        for entry in chunk:
            masked, mapping = masker.mask(entry["text"])
            items[entry["id"]] = masked
            masks[entry["id"]] = {"source": entry["text"], "store": mapping}
        number = index // args.shard_size
        shard = args.shard_dir / f"rag_shard_{number:04d}.json"
        shard.write_text(
            json.dumps({"instrucoes": TRANSLATOR_BRIEF, "textos": items}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        sibling(shard, "map").write_text(json.dumps(masks, ensure_ascii=False), encoding="utf-8")
        written += 1

    chars = sum(len(entry["text"]) for entry in pending)
    print(f"passagens pendentes ... {len(pending):,}")
    print(f"caracteres ........... {chars:,}")
    print(f"shards gravados ....... {written}")
    print(f"pasta ................. {args.shard_dir.relative_to(ROOT)}")
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    masker = Masker()
    store = load_store(args.store)
    applied = rejected = 0

    for shard in shard_paths(args.shard_dir):
        translated_path = sibling(shard, "pt")
        mapping_path = sibling(shard, "map")
        if not translated_path.exists() or not mapping_path.exists():
            continue
        payload = json.loads(shard.read_text(encoding="utf-8"))
        masked_inputs = payload["textos"] if isinstance(payload, dict) and "textos" in payload else payload
        translations = json.loads(translated_path.read_text(encoding="utf-8"))
        if isinstance(translations, dict) and "textos" in translations:
            translations = translations["textos"]
        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        if set(translations) != set(masked_inputs):
            print(f"ignorado {shard.name}: chaves não batem", file=sys.stderr)
            rejected += len(masked_inputs)
            continue
        for key, masked_source in masked_inputs.items():
            if key not in translations or key not in mapping:
                rejected += 1
                continue
            restored = masker.unmask(translations[key], mapping[key]["store"])
            problem = validate_pair(masked_source, translations[key])
            if problem:
                print(f"  rejeitado {key}: {problem}", file=sys.stderr)
                rejected += 1
                continue
            store[key] = restored
            applied += 1

    args.store.parent.mkdir(parents=True, exist_ok=True)
    args.store.write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")
    entries = load_index()
    total = len(pending_passages(entries, {}, only_without_ficha=not args.all_ajuda))
    print(f"aplicadas ............ {applied}")
    print(f"rejeitadas ........... {rejected}")
    print(f"cobertura ............ {len(store):,}/{total + len(store):,}")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    entries = load_index()
    store = load_store(args.store)
    pending = pending_passages(entries, store, only_without_ficha=not args.all_ajuda)
    shards = shard_paths(args.shard_dir)
    done = sum(1 for shard in shards if sibling(shard, "pt").exists())
    chars_pending = sum(len(entry["text"]) for entry in pending)
    print(f"passagens traduzidas . {len(store):,}")
    print(f"passagens pendentes .. {len(pending):,} ({chars_pending:,} chars)")
    print(f"shards exportados .... {len(shards)}")
    print(f"shards traduzidos .... {done}")
    if shards:
        print(f"shards faltando ...... {len(shards) - done}")
    return 0


def cmd_audit(args: argparse.Namespace) -> int:
    store = load_store(args.store)
    english = 0
    for key, text in store.items():
        if len(text) > 80 and ENGLISH_HINT.search(text):
            english += 1
            if english <= 5:
                print(f"  {key}: {text[:100]}...")
    print(f"suspeitas de inglês .. {english}/{len(store)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    paths = project_paths(__file__)
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--store", type=Path, default=STORE_PATH)
    parser.add_argument("--shard-dir", type=Path, default=SHARD_DIR)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("export")
    p.add_argument("--shard-size", type=int, default=60)
    p.add_argument("--clean", action="store_true")
    p.add_argument("--all-ajuda", action="store_true", help="inclui tópicos que já têm ficha")
    p.set_defaults(func=cmd_export)

    p = sub.add_parser("apply")
    p.add_argument("--all-ajuda", action="store_true")
    p.set_defaults(func=cmd_apply)

    p = sub.add_parser("status")
    p.add_argument("--all-ajuda", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("audit")
    p.set_defaults(func=cmd_audit)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
