#!/usr/bin/env python3
"""
Junta os quatro corpora VFP 9 nos arquivos finais de treino/val usados no fine-tuning.

Cada corpus ensina uma coisa diferente, então a proporção é a alavanca
principal sobre o modelo resultante:

    help    Q&A em prosa         explica conceitos
    sig     fichas de assinatura impede alucinar APIs
    code    pares de funções     escreve FoxPro idiomático
    agent   rastros multi-turno  usa ferramentas e edita arquivos

O corpus de ajuda é bem maior, então os pesos superamostram os menores. A
mesclagem recusa emitir um split que vaze: qualquer linha de validação cuja
pergunta ou resposta também apareça no treino é descartada.

Uso:
    python merge_datasets.py
    python merge_datasets.py --weight code=3 --weight agent=4 --suffix _final
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

# nome -> (arquivo treino, arquivo val, peso padrão)
CORPORA: dict[str, tuple[str, str, int]] = {
    "help": ("train_messages_pt.jsonl", "val_messages_pt.jsonl", 1),
    "sig": ("train_sig_pt.jsonl", "val_sig_pt.jsonl", 1),
    "code": ("train_messages_code_pt.jsonl", "val_messages_code_pt.jsonl", 1),
    "agent": ("train_agent_pt.jsonl", "val_agent_pt.jsonl", 1),
}


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.open(encoding="utf-8") if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def role_text(example: dict, role: str) -> str:
    """First message of a role; for assistant, the last one carries the answer."""
    texts = [m.get("content") or "" for m in example.get("messages", []) if m.get("role") == role]
    if not texts:
        return ""
    return texts[-1] if role == "assistant" else texts[0]


def tag(rows: list[dict], source: str) -> list[dict]:
    return [{"source": source, "example": row} for row in rows]


def drop_leaks(train: list[dict], val: list[dict]) -> tuple[list[dict], int]:
    questions = {role_text(r["example"], "user") for r in train}
    answers = {role_text(r["example"], "assistant") for r in train}
    kept = [
        r
        for r in val
        if role_text(r["example"], "user") not in questions
        and role_text(r["example"], "assistant") not in answers
    ]
    return kept, len(val) - len(kept)


def summarize(rows: list[dict]) -> dict:
    sizes = sorted(len(json.dumps(r["example"], ensure_ascii=False)) for r in rows)
    answers = [role_text(r["example"], "assistant") for r in rows]
    multiturn = sum(1 for r in rows if len(r["example"].get("messages", [])) > 3)
    return {
        "rows": len(rows),
        "by_source": dict(Counter(r["source"] for r in rows)),
        "multi_turn_rows": multiturn,
        "rows_with_tools": sum(1 for r in rows if r["example"].get("tools")),
        "answers_with_pt_accents": sum(1 for a in answers if re.search(r"[àáâãéêíóôõúç]", a, re.I)),
        "answers_with_code": sum(1 for a in answers if "```" in a),
        "chars_p50": sizes[len(sizes) // 2] if sizes else 0,
        "chars_p95": sizes[int(len(sizes) * 0.95)] if sizes else 0,
        "approx_tokens_total": round(sum(sizes) / 3.5),
    }


def parse_weights(pairs: list[str]) -> dict[str, int]:
    weights = {name: default for name, (_, _, default) in CORPORA.items()}
    for pair in pairs:
        if "=" not in pair:
            raise SystemExit(f"--weight espera nome=valor, recebido: {pair}")
        name, value = pair.split("=", 1)
        if name not in CORPORA:
            raise SystemExit(f"corpus desconhecido: {name}. Use um de {sorted(CORPORA)}")
        weights[name] = int(value)
    return weights


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Merge the VFP 9 corpora.")
    parser.add_argument("--dir", type=Path, default=root / "data/training")
    parser.add_argument(
        "--weight",
        action="append",
        default=[],
        metavar="NOME=N",
        help=f"Repete cada exemplo do corpus N vezes. Corpora: {', '.join(CORPORA)}",
    )
    parser.add_argument(
        "--exclude", action="append", default=[], help="Deixa um corpus de fora da mesclagem"
    )
    parser.add_argument("--suffix", default="_final")
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rng = random.Random(args.seed)
    weights = parse_weights(args.weight)

    train: list[dict] = []
    val: list[dict] = []
    inputs: dict[str, dict] = {}
    for name, (train_file, val_file, _) in CORPORA.items():
        if name in args.exclude:
            continue
        rows_train = tag(load_jsonl(args.dir / train_file), name)
        rows_val = tag(load_jsonl(args.dir / val_file), name)
        if not rows_train:
            print(f"aviso: corpus '{name}' não encontrado em {args.dir / train_file}")
            continue
        inputs[name] = {
            "train": len(rows_train),
            "val": len(rows_val),
            "weight": weights[name],
            "train_after_weight": len(rows_train) * weights[name],
        }
        train += rows_train * weights[name]
        val += rows_val

    if not train:
        print("nenhum corpus carregado", file=sys.stderr)
        return 1

    val, leaked = drop_leaks(train, val)
    rng.shuffle(train)
    rng.shuffle(val)

    train_path = args.dir / f"train{args.suffix}.jsonl"
    val_path = args.dir / f"val{args.suffix}.jsonl"
    write_jsonl(train_path, [r["example"] for r in train])
    write_jsonl(val_path, [r["example"] for r in val])

    stats = {
        "weights": weights,
        "excluded": args.exclude,
        "leaked_val_rows_dropped": leaked,
        "inputs": inputs,
        "train": summarize(train),
        "val": summarize(val),
    }
    stats_path = args.dir / f"stats{args.suffix}.json"
    stats_path.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"train -> {train_path} ({len(train)} linhas)")
    print(f"  composição: {stats['train']['by_source']}")
    print(f"  tokens aprox.: {stats['train']['approx_tokens_total']:,}")
    print(f"val   -> {val_path} ({len(val)} linhas)")
    print(f"  composição: {stats['val']['by_source']}")
    print(f"linhas de validação descartadas por vazamento: {leaked}")
    print(f"stats -> {stats_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
