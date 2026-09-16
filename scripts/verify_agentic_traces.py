#!/usr/bin/env python3
"""
Reproduz rastros agentic para provar que de fato funcionariam.

Um rastro que parece plausível mas cuja edição não aplica ensina ao modelo um
movimento que falha em tempo de execução, pior do que nenhum rastro. Isto
confere validade do protocolo, que cada edição mira texto que o agente realmente
viu, e que as edições de reparo reconstroem a rotina conhecida byte a byte.

Uso:
    python verify_agentic_traces.py ../data/training/train_agent_pt.jsonl
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

from agentic_project import Project, load_functions

LINE_RE = re.compile(r"(?m)^\s*(\d+)\|\s?(.*)$")
VALID_ROLES = {"system", "user", "assistant", "tool"}


def strip_numbers(payload: str) -> tuple[str, list[int]]:
    matches = LINE_RE.findall(payload)
    if not matches:
        return payload, []
    return "\n".join(text for _, text in matches), [int(n) for n, _ in matches]


def check_protocol(messages: list[dict], report: Counter) -> None:
    if messages[0]["role"] != "system":
        report["não começa com system"] += 1
    if messages[1]["role"] != "user":
        report["segunda mensagem não é user"] += 1
    last = messages[-1]
    if last["role"] != "assistant" or not last.get("content"):
        report["não termina com resposta do assistant"] += 1

    pending: str | None = None
    for message in messages:
        if message["role"] not in VALID_ROLES:
            report["papel inválido"] += 1
        if message["role"] == "assistant" and message.get("tool_calls"):
            if pending:
                report["chamada sem resposta antes da próxima"] += 1
            if len(message["tool_calls"]) != 1:
                report["mais de uma chamada por turno"] += 1
            tool_call = message["tool_calls"][0]
            pending = tool_call["id"]
            try:
                json.loads(tool_call["function"]["arguments"])
            except json.JSONDecodeError:
                report["arguments não é JSON válido"] += 1
        elif message["role"] == "tool":
            if message.get("tool_call_id") != pending:
                report["tool_call_id não corresponde"] += 1
            pending = None
    if pending:
        report["chamada final sem resposta"] += 1


def check_trace(messages: list[dict], functions: dict[str, str], report: Counter) -> None:
    check_protocol(messages, report)

    seen_text: list[str] = []
    reads: list[tuple[dict, str]] = []
    for index, message in enumerate(messages):
        if message["role"] != "assistant" or not message.get("tool_calls"):
            continue
        tool_call = message["tool_calls"][0]
        name = tool_call["function"]["name"]
        try:
            args = json.loads(tool_call["function"]["arguments"])
        except json.JSONDecodeError:
            continue
        payload = messages[index + 1]["content"] if index + 1 < len(messages) else ""

        if name == "read_file":
            body, numbers = strip_numbers(payload)
            if not numbers:
                report["read_file sem linhas numeradas"] += 1
            else:
                if numbers[0] != args["start_line"] or numbers[-1] != args["end_line"]:
                    report["intervalo lido difere do solicitado"] += 1
                if numbers != list(range(numbers[0], numbers[-1] + 1)):
                    report["numeração de linhas não é contínua"] += 1
            seen_text.append(body)
            reads.append((args, body))

        elif name == "edit_file":
            old_text = args["old_text"]
            new_text = args["new_text"]
            if old_text == new_text:
                report["edição sem efeito"] += 1
            context = "\n".join(seen_text)
            if old_text not in context:
                report["edita trecho que não foi lido"] += 1
            if not payload.startswith("ok"):
                report["edição sem confirmação"] += 1

            # Ponta a ponta: o texto corrigido deve bater exatamente com o código conhecido.
            for _, body in reads:
                found = re.search(r"(?:FUNCTION|PROCEDURE)\s+(\S+)", body)
                if not found:
                    continue
                expected = functions.get(found.group(1))
                if not expected or old_text not in body:
                    continue
                patched = body.replace(old_text, new_text, 1).strip()
                if patched == expected.strip():
                    report["OK patch reconstrói a rotina"] += 1
                elif new_text.startswith(old_text):
                    check_append(patched, expected, functions, report)
                else:
                    report["patch não reconstrói a rotina correta"] += 1
                break


def check_append(patched: str, reference: str, functions: dict[str, str], report: Counter) -> None:
    """An append must leave the reference intact and add one known routine verbatim."""
    if not patched.startswith(reference.strip()):
        report["append alterou a rotina de referência"] += 1
        return
    added = patched[len(reference.strip()) :].strip()
    found = re.search(r"(?:FUNCTION|PROCEDURE)\s+(\S+)", added)
    if not found:
        report["append não contém rotina completa"] += 1
        return
    expected = functions.get(found.group(1))
    if expected is None or added != expected.strip():
        report["rotina anexada difere do código correto"] += 1
    else:
        report["OK append insere rotina íntegra"] += 1


def main() -> int:
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        print("uso: verify_agentic_traces.py <arquivo.jsonl> [...]", file=sys.stderr)
        return 1

    root = Path(__file__).resolve().parent.parent
    project = Project(load_functions([root / "ExemplosCodigo/vfp9.pr2", root / "ExemplosCodigo/exemplo.pr2"]))
    functions = {name: f.code for name, f in project.functions.items()}

    exit_code = 0
    for path in paths:
        rows = [json.loads(line) for line in path.open(encoding="utf-8") if line.strip()]
        report: Counter[str] = Counter()
        for row in rows:
            check_trace(row["messages"], functions, report)

        problems = {k: v for k, v in report.items() if not k.startswith("OK")}
        print(f"\n===== {path.name} ({len(rows)} traces) =====")
        print(f"  correções que reconstroem a rotina correta: {report['OK patch reconstrói a rotina']}")
        print(f"  inserções que anexam rotina íntegra:        {report['OK append insere rotina íntegra']}")
        if problems:
            exit_code = 1
            for key, value in sorted(problems.items(), key=lambda kv: -kv[1]):
                print(f"  FALHA  {key}: {value}")
        else:
            print("  nenhum problema encontrado")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
