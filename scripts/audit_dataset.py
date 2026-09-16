#!/usr/bin/env python3
"""
Audita um dataset SFT em formato chat pelos problemas que importam no fine-tuning:
esquema, dano à sintaxe FoxPro, idioma da resposta, truncamento e vazamento treino/val.

Uso:
    python audit_dataset.py ../data/training/train_messages_pt.jsonl \
                            ../data/training/val_messages_pt.jsonl
"""

from __future__ import annotations

import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

FENCE_RE = re.compile(r"```(?:\w+)?\n(.*?)```", re.S)
BROKEN_LOGICAL_RE = re.compile(r"\.\s+(?:T|F|NULL)\s*\.")
BROKEN_MEMBER_RE = re.compile(r"\b(?:This|ThisForm|ThisFormSet|_SCREEN|_VFP)\.\s+[A-Za-z]")
PT_MARKER_RE = re.compile(
    r"[àáâãéêíóôõúçÀÁÂÃÉÊÍÓÔÕÚÇ]|\b(?:que|não|uma|para|com|você|então|também|"
    r"função|comando|propriedade|retorna|especifica|seguinte|exemplo)\b",
    re.I,
)
EN_MARKER_RE = re.compile(
    r"\b(?:the|and|for|with|this|that|returns|specifies|creates|following|"
    r"value|when|which|from|you can)\b",
    re.I,
)


def load(path: Path) -> list[dict]:
    rows = []
    for line in path.open(encoding="utf-8"):
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def role_text(example: dict, role: str) -> str:
    for message in example.get("messages", []):
        if message.get("role") == role:
            return message.get("content") or ""
    return ""


def code_of(text: str) -> str:
    return "\n".join(m.group(1) for m in FENCE_RE.finditer(text))


def percentiles(values: list[int]) -> str:
    if not values:
        return "n/a"
    s = sorted(values)
    return (
        f"min={s[0]} p50={s[len(s)//2]} p95={s[int(len(s)*0.95)]} "
        f"max={s[-1]} mean={statistics.mean(s):.0f}"
    )


def audit(name: str, rows: list[dict]) -> dict:
    print(f"\n===== {name}  ({len(rows)} rows) =====")

    schema_bad = 0
    users, answers = [], []
    asst_lens = []
    pt_answers = en_answers = 0
    broken_logical = broken_member = 0
    open_fence = 0
    truncated = 0
    code_chars = 0

    for example in rows:
        messages = example.get("messages")
        if not isinstance(messages, list) or [m.get("role") for m in messages] != [
            "system",
            "user",
            "assistant",
        ]:
            schema_bad += 1
            continue
        user = role_text(example, "user")
        answer = role_text(example, "assistant")
        users.append(user)
        answers.append(answer)
        asst_lens.append(len(answer))

        if PT_MARKER_RE.search(answer):
            pt_answers += 1
        elif EN_MARKER_RE.search(answer):
            en_answers += 1

        if BROKEN_LOGICAL_RE.search(answer):
            broken_logical += 1
        if BROKEN_MEMBER_RE.search(answer):
            broken_member += 1
        if answer.count("```") % 2:
            open_fence += 1
        tail = answer.rstrip()
        if tail and not tail.endswith(("```", "|", ".", "!", "?", '"', "'", ")")):
            truncated += 1
        code_chars += len(code_of(answer))

    total = max(len(answers), 1)

    def line(label: str, count: int) -> None:
        print(f"  {label:36s} {count:6d}  ({100 * count / total:5.1f}%)")

    print(f"  schema violations: {schema_bad}")
    print(f"  unique questions: {len(set(users))} / {len(users)}")
    print(f"  unique answers:   {len(set(answers))} / {len(answers)}")
    print(f"  answer chars: {percentiles(asst_lens)}")
    print(f"  code chars total: {code_chars:,}")
    line("answers in PT", pt_answers)
    line("answers in EN", en_answers)
    line("broken logical (. T.)", broken_logical)
    line("broken member (This. Prop)", broken_member)
    line("unbalanced code fences", open_fence)
    line("answers with truncated tail", truncated)

    return {"users": set(users), "answers": set(answers)}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    train = audit("TRAIN", load(Path(sys.argv[1])))
    if len(sys.argv) > 2:
        val = audit("VAL", load(Path(sys.argv[2])))
        print("\n===== LEAKAGE =====")
        print(f"  identical questions in both: {len(train['users'] & val['users'])}")
        print(f"  identical answers in both:   {len(train['answers'] & val['answers'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
