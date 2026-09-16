#!/usr/bin/env python3
"""
Pipeline de tradução EN -> pt-BR no nível de campo para as fichas de assinatura.

Traduzir fichas inteiras desperdiça esforço: as mesmas frases ("Character.",
"Specifies the name of the table.") se repetem em centenas de tópicos, e
entradas longas convidam o tradutor a desviar. Isto parte as fichas em campos
de prosa, remove duplicatas e entrega shards pequenos que podem ser traduzidos
independentemente e reunidos com validação.

Subcomandos:
    export   grava shards de campos não traduzidos em data/translation/shards/
    apply    valida os shards prontos e mescla em fields_pt.json
    status   relata cobertura e o que ainda falta

Uso:
    python translate_fields.py export --shard-size 120
    python translate_fields.py apply
    python translate_fields.py status
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from build_signature_dataset import build_card, translatable_fields
from html_utils import project_paths
from translate_dataset import SENTINEL_RE, Masker

TRANSLATOR_BRIEF = (
    "Traduza cada valor do inglês para o português do Brasil. "
    "Preserve EXATAMENTE os marcadores [[C0]], [[I1]], [[T2]] (mesma quantidade, "
    "mesmos números). Não traduza nomes de comandos, funções, propriedades, "
    "classes ou parâmetros do Visual FoxPro. Mantenha a pontuação final. "
    "Responda apenas com o JSON traduzido, no mesmo formato e com as mesmas chaves."
)


def collect_fields(topics_path: Path) -> list[str]:
    topics = [json.loads(line) for line in topics_path.open(encoding="utf-8") if line.strip()]
    cards = [card for card in (build_card(topic) for topic in topics) if card]
    seen: dict[str, None] = {}
    for card in cards:
        for field in translatable_fields(card):
            seen.setdefault(field, None)
    return list(seen)


def validate_pair(source: str, translated: str) -> str | None:
    """Reject a translation that lost a marker, stayed English, or ran away."""
    if not translated or not translated.strip():
        return "vazio"
    if sorted(SENTINEL_RE.findall(source)) != sorted(SENTINEL_RE.findall(translated)):
        return "marcadores alterados"
    ratio = len(translated) / max(len(source), 1)
    if ratio > 2.5 or ratio < 0.4:
        return "comprimento fora da faixa"
    if translated.strip() == source.strip() and len(source) > 40:
        return "não traduzido"
    return None


# Fragmentos recorrentes que vários tradutores renderizam de jeitos diferentes.
# Consistência importa mais que a escolha: um corpus que diz as duas formas
# ensina as duas ao modelo.
CANONICAL_FRAGMENTS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bSetting Description\b"), "Configuração Descrição"),
    (re.compile(r"\bValue Description\b"), "Valor Descrição"),
    (re.compile(r"\bProperty Description\b"), "Propriedade Descrição"),
    (re.compile(r"\bParameter Description\b"), "Parâmetro Descrição"),
    (re.compile(r"\bConstant Description\b"), "Constante Descrição"),
]


def canonicalize(text: str) -> str:
    for pattern, replacement in CANONICAL_FRAGMENTS:
        text = pattern.sub(replacement, text)
    return text


def shard_paths(directory: Path) -> list[Path]:
    """Input shards only: the .map.json and .pt.json siblings share the prefix."""
    return sorted(
        path
        for path in directory.glob("shard_*.json")
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
    fields = collect_fields(args.topics)
    store = load_store(args.store)
    pending = [field for field in fields if field not in store]

    args.shard_dir.mkdir(parents=True, exist_ok=True)
    if args.clean:
        # Mapas e traduções só fazem sentido ao lado do shard de entrada.
        for old in args.shard_dir.glob("shard_*.json"):
            old.unlink()

    written = 0
    for index in range(0, len(pending), args.shard_size):
        chunk = pending[index : index + args.shard_size]
        items = {}
        masks = {}
        for offset, field in enumerate(chunk):
            key = f"{index + offset:05d}"
            masked, mapping = masker.mask(field)
            items[key] = masked
            masks[key] = {"source": field, "store": mapping}
        number = index // args.shard_size
        (args.shard_dir / f"shard_{number:03d}.json").write_text(
            json.dumps({"instrucoes": TRANSLATOR_BRIEF, "textos": items}, indent=1, ensure_ascii=False),
            encoding="utf-8",
        )
        (args.shard_dir / f"shard_{number:03d}.map.json").write_text(
            json.dumps(masks, ensure_ascii=False), encoding="utf-8"
        )
        written += 1

    chars = sum(len(SENTINEL_RE.sub("", masker.mask(f)[0])) for f in pending)
    print(f"campos totais: {len(fields):,} | já traduzidos: {len(store):,} | pendentes: {len(pending):,}")
    print(f"prosa pendente: {chars:,} chars (~{chars // 4:,} tokens)")
    print(f"{written} shards de até {args.shard_size} campos em {args.shard_dir}")
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    store = load_store(args.store)
    accepted = 0
    rejected: dict[str, int] = {}
    missing = 0

    for shard in shard_paths(args.shard_dir):
        done = sibling(shard, "pt")
        mapping_path = sibling(shard, "map")
        if not done.exists() or not mapping_path.exists():
            continue
        translations = json.loads(done.read_text(encoding="utf-8"))
        if isinstance(translations, dict) and "textos" in translations:
            translations = translations["textos"]
        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        masked_inputs = json.loads(shard.read_text(encoding="utf-8"))["textos"]

        # Uma tradução velha de uma exportação anterior reusa as mesmas chaves
        # para fontes diferentes, o que colaria o português errado num campo
        # sem erro visível. Recusa o arquivo inteiro.
        extra = translations.keys() - masked_inputs.keys()
        if extra:
            print(
                f"  IGNORADO {done.name}: {len(extra)} chaves não existem no shard atual "
                f"(tradução obsoleta de uma exportação anterior)",
                file=sys.stderr,
            )
            continue

        for key, masked_source in masked_inputs.items():
            value = translations.get(key)
            if value is None:
                missing += 1
                continue
            reason = validate_pair(masked_source, value)
            if reason:
                rejected[reason] = rejected.get(reason, 0) + 1
                continue
            store[mapping[key]["source"]] = canonicalize(
                Masker.unmask(value, mapping[key]["store"])
            )
            accepted += 1

    # Entradas antigas foram mescladas antes de um fragmento virar canônico.
    normalized = 0
    for source, translated in list(store.items()):
        fixed = canonicalize(translated)
        if fixed != translated:
            store[source] = fixed
            normalized += 1
    if normalized:
        print(f"normalizados para a forma canônica: {normalized}")

    args.store.parent.mkdir(parents=True, exist_ok=True)
    args.store.write_text(json.dumps(store, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"aceitos nesta rodada: {accepted:,}")
    if missing:
        print(f"ausentes nos shards traduzidos: {missing:,}")
    for reason, count in sorted(rejected.items(), key=lambda kv: -kv[1]):
        print(f"  rejeitados por {reason}: {count}")
    print(f"store -> {args.store} ({len(store):,} campos)")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    fields = collect_fields(args.topics)
    store = load_store(args.store)
    done = sum(1 for field in fields if field in store)
    print(f"cobertura: {done:,}/{len(fields):,} campos ({done / max(len(fields), 1):.1%})")

    pending_shards = []
    for shard in shard_paths(args.shard_dir):
        if not sibling(shard, "pt").exists():
            pending_shards.append(shard.name)
    if pending_shards:
        print(f"shards sem tradução ({len(pending_shards)}): {', '.join(pending_shards[:10])}")
        if len(pending_shards) > 10:
            print(f"  ... e mais {len(pending_shards) - 10}")
    else:
        print("todos os shards exportados têm tradução")

    print("rode `translate_fields.py audit` para conferir a terminologia")
    return 0


# Termos cuja forma em português deve ser idêntica em todo lugar, para a ficha
# nunca chamar a mesma coisa de dois jeitos.
GLOSSARY_EXPECTED = {
    "Character.": "Caractere.",
    "Numeric.": "Numérico.",
    "Logical.": "Lógico.",
    "Character data type.": "Tipo de dado caractere.",
    "Logical data type.": "Tipo de dado lógico.",
    "Included for backward compatibility.": "Incluído para compatibilidade retroativa.",
}
# Identificadores que nunca devem ser traduzidos, conferidos como palavras inteiras.
PROTECTED_WORDS = [
    "CursorAdapter", "Caption", "Visible", "RecordSource", "ControlSource",
    "Visual FoxPro", "SELECT", "REPLACE", "APPEND", "BROWSE",
]
ENGLISH_RE = re.compile(r"\b(the|and|that|with|which|specifies|returns|when|from)\b", re.I)
# Nomes de comando e identificadores ficam em inglês de propósito; remova-os
# antes de perguntar se a tradução ainda parece inglês.
KEEP_ENGLISH_RE = re.compile(
    r"\b[A-Z][A-Z0-9_]+(?:\s+[A-Z][A-Z0-9_]+)*\b"  # SET SKIP OF, MODIFY REPORT
    r"|\b[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+\b"  # This.Caption
    r"|\b[a-z]{1,3}[A-Z][A-Za-z0-9]+\b"  # cFileName, lExpression
    r"|\b[A-Z][a-z]+[A-Z][A-Za-z0-9]*\b"  # CursorAdapter, RecordSource
)


def cmd_audit(args: argparse.Namespace) -> int:
    """Check the merged store for terminology drift, not just mechanical validity."""
    store = load_store(args.store)
    if not store:
        print("nenhuma tradução no store", file=sys.stderr)
        return 1

    problems: dict[str, list[tuple[str, str]]] = {}

    def flag(kind: str, source: str, translated: str) -> None:
        problems.setdefault(kind, []).append((source, translated))

    for source, translated in store.items():
        prose = KEEP_ENGLISH_RE.sub("", translated)
        if len(ENGLISH_RE.findall(prose)) >= 2 and len(source) > 40:
            flag("ainda parece inglês", source, translated)
        expected = GLOSSARY_EXPECTED.get(source.strip())
        if expected and translated.strip() != expected:
            flag("termo do glossário divergente", source, translated)
        for word in PROTECTED_WORDS:
            if re.search(rf"\b{re.escape(word)}\b", source) and not re.search(
                rf"\b{re.escape(word)}\b", translated
            ):
                flag(f"perdeu o identificador {word}", source, translated)
        if source.rstrip().endswith(".") and not translated.rstrip().endswith((".", "…")):
            flag("pontuação final perdida", source, translated)
        if canonicalize(translated) != translated:
            flag("fragmento fora da forma canônica", source, translated)

    # O mesmo texto inglês nunca deveria mapear para dois portugueses diferentes;
    # o store é chaveado pela fonte, então isso é garantido, mas o inverso vale
    # saber: fontes muito diferentes compartilhando uma tradução significa colapso.
    reverse: dict[str, int] = {}
    for translated in store.values():
        reverse[translated] = reverse.get(translated, 0) + 1

    print(f"traduções no store: {len(store):,}")
    if not problems:
        print("nenhum problema de terminologia encontrado")
    for kind, entries in sorted(problems.items(), key=lambda kv: -len(kv[1])):
        print(f"\n  {kind}: {len(entries)}")
        for source, translated in entries[:3]:
            print(f"    EN: {source[:90]}")
            print(f"    PT: {translated[:90]}")
    return 1 if problems else 0


def parse_args() -> argparse.Namespace:
    paths = project_paths(__file__)
    root = paths["data_dir"] / "translation"
    parser = argparse.ArgumentParser(description="Field-level translation pipeline.")
    parser.add_argument("--topics", type=Path, default=paths["data_dir"] / "topics.jsonl")
    parser.add_argument("--shard-dir", type=Path, default=root / "shards")
    parser.add_argument("--store", type=Path, default=root / "fields_pt.json")
    sub = parser.add_subparsers(dest="command", required=True)

    export = sub.add_parser("export", help="write shards of pending fields")
    export.add_argument("--shard-size", type=int, default=120)
    export.add_argument("--clean", action="store_true", help="remove existing shards first")
    export.set_defaults(func=cmd_export)

    apply_cmd = sub.add_parser("apply", help="validate and merge finished shards")
    apply_cmd.set_defaults(func=cmd_apply)

    status = sub.add_parser("status", help="report coverage")
    status.set_defaults(func=cmd_status)

    audit = sub.add_parser("audit", help="check terminology consistency of the store")
    audit.set_defaults(func=cmd_audit)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
