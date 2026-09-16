#!/usr/bin/env python3
"""
Monta rastros agentic de vários turnos para um agente de código Visual FoxPro 9.

Os corpora de ajuda e de código ensinam conhecimento; este ensina comportamento:
buscar antes de ler, ler um trecho em vez do arquivo inteiro, e editar de forma
cirúrgica. Esses hábitos importam mais quando o modelo servido tem janela de
contexto pequena, então cada rastro é feito para manter a saída das ferramentas
curta.

Os rastros saem no formato de tool-calling da OpenAI (assistant.tool_calls mais
respostas role="tool") e podem ser convertidos para o formato inline Hermes/Qwen.

Uso:
    python build_agentic_dataset.py
    python build_agentic_dataset.py --tool-format hermes --tools-in-system
"""

from __future__ import annotations

import argparse
import difflib
import json
import random
import re
from collections import Counter
from pathlib import Path

from agentic_project import Project, load_functions, signature_of
from build_code_training_dataset import extract_negatives

SYSTEM_PROMPT = (
    "Você é um agente de desenvolvimento em Microsoft Visual FoxPro 9 e atua no "
    "código-fonte do projeto.\n\n"
    "Padrões do projeto:\n"
    "- Cabeçalho de rotina delimitado por linhas de asteriscos.\n"
    "- `PARAMETERS` seguido de `PRIVATE` declarando os mesmos nomes.\n"
    "- Corpo indentado com 3 espaços; `RETURN(...)` com parênteses.\n"
    "- `FUNCTION` encerra com `ENDFUNC`; `PROCEDURE` encerra com `ENDPROC`.\n"
    "- Prefixo húngaro nos nomes: c=caractere, n=numérico, l=lógico, d=data, "
    "o=objeto, a=array.\n\n"
    "Regras de trabalho:\n"
    "- Localize com `search_text` antes de abrir um arquivo.\n"
    "- Leia apenas o intervalo necessário com `read_file`; não carregue arquivos inteiros.\n"
    "- Altere com `edit_file` usando o menor trecho que identifique a mudança.\n"
    "- Não modifique nada que a tarefa não peça."
)

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "Lista os arquivos de código do projeto.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_text",
            "description": "Procura um padrão no código e devolve arquivo, linha e conteúdo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {"type": "string", "description": "Texto ou expressão regular."}
                },
                "required": ["pattern"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Lê um intervalo de linhas de um arquivo, numeradas.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "start_line": {"type": "integer"},
                    "end_line": {"type": "integer"},
                },
                "required": ["path", "start_line", "end_line"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": (
                "Substitui um trecho exato de um arquivo. O trecho em old_text deve "
                "ocorrer uma única vez no arquivo."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "old_text": {"type": "string"},
                    "new_text": {"type": "string"},
                },
                "required": ["path", "old_text", "new_text"],
            },
        },
    },
]


# --------------------------------------------------------------------------- #
# Auxiliares de mensagem
# --------------------------------------------------------------------------- #
def call(index: int, name: str, arguments: dict) -> dict:
    return {
        "role": "assistant",
        "content": None,
        "tool_calls": [
            {
                "id": f"call_{index}",
                "type": "function",
                "function": {"name": name, "arguments": json.dumps(arguments, ensure_ascii=False)},
            }
        ],
    }


def result(index: int, payload: str) -> dict:
    return {"role": "tool", "tool_call_id": f"call_{index}", "content": payload}


def search_payload(hits: list[tuple[str, int, str]]) -> str:
    if not hits:
        return "Nenhuma ocorrência encontrada."
    return "\n".join(f"{path}:{line}: {text.strip()}" for path, line, text in hits)


# --------------------------------------------------------------------------- #
# Diff cirúrgico
# --------------------------------------------------------------------------- #
def minimal_edit(original: str, updated: str, haystack: str) -> tuple[str, str] | None:
    """
    Smallest old/new pair that turns `original` into `updated`.

    Context is grown line by line until `old_text` appears exactly once in the
    file, which is what makes a surgical edit safe to apply.
    """
    before = original.split("\n")
    after = updated.split("\n")
    matcher = difflib.SequenceMatcher(None, before, after)
    opcodes = [op for op in matcher.get_opcodes() if op[0] != "equal"]
    if not opcodes:
        return None

    lo_before = min(op[1] for op in opcodes)
    hi_before = max(op[2] for op in opcodes)
    lo_after = min(op[3] for op in opcodes)
    hi_after = max(op[4] for op in opcodes)

    for padding in range(0, 8):
        start_b = max(0, lo_before - padding)
        end_b = min(len(before), hi_before + padding)
        start_a = max(0, lo_after - padding)
        end_a = min(len(after), hi_after + padding)
        old_text = "\n".join(before[start_b:end_b])
        new_text = "\n".join(after[start_a:end_a])
        # Um new_text vazio deixaria a linha em branco em vez de removê-la, então
        # cresce a janela até aparecer uma linha âncora sobrevivente.
        if not new_text.strip():
            continue
        if old_text and haystack.count(old_text) == 1 and old_text != new_text:
            return old_text, new_text
    if haystack.count(original) == 1:
        return original, updated
    return None


# --------------------------------------------------------------------------- #
# Construtores de rastro
# --------------------------------------------------------------------------- #
def trace_locate(project: Project, function, rng: random.Random) -> dict | None:
    question = rng.choice(
        [
            f"Em qual arquivo está definida a rotina {function.name}?",
            f"Onde fica {function.name} no projeto?",
            f"Preciso ver o código de {function.name}. Onde ele está?",
        ]
    )
    hits = project.search(rf"(FUNCTION|PROCEDURE)\s+{re.escape(function.name)}\b", limit=3)
    if not hits:
        return None
    path, line, _ = hits[0]

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
        call(1, "search_text", {"pattern": f"FUNCTION {function.name}"}),
        result(1, search_payload(hits)),
        call(
            2,
            "read_file",
            {"path": path, "start_line": function.start_line, "end_line": function.end_line},
        ),
        result(2, project.read_range(path, function.start_line, function.end_line)),
        {
            "role": "assistant",
            "content": (
                f"`{function.name}` está em `{path}`, linhas "
                f"{function.start_line}–{function.end_line}.\n\n"
                f"```foxpro\n{function.code}\n```"
            ),
        },
    ]
    return {"kind": "localizar", "key": function.name, "messages": messages}


def trace_fix(project: Project, function, negative: dict, rng: random.Random) -> dict | None:
    """Repair a broken routine: locate, read the range, then patch minimally."""
    broken = negative["code"].strip()
    correct = function.code
    if broken == correct:
        return None

    module = project.modules[function.module]
    broken_file = module.text.replace(correct, broken)
    if broken_file == module.text:
        return None

    edit = minimal_edit(broken, correct, broken_file)
    if not edit:
        return None
    old_text, new_text = edit

    broken_lines = broken.split("\n")
    end_line = function.start_line + len(broken_lines) - 1
    numbered = "\n".join(
        f"{function.start_line + offset:5d}| {text}" for offset, text in enumerate(broken_lines)
    )

    error = negative["error"].rstrip(".")
    symptom = rng.choice(
        [
            f"A rotina {function.name} não está se comportando como deveria. Corrija.",
            f"Encontrei um problema em {function.name}. Ajuste o código.",
            f"{function.name} precisa de correção. Resolva no arquivo do projeto.",
        ]
    )
    hits = [(function.module, function.start_line, f"FUNCTION {function.name}")]

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": symptom},
        call(1, "search_text", {"pattern": f"FUNCTION {function.name}"}),
        result(1, search_payload(hits)),
        call(
            2,
            "read_file",
            {"path": function.module, "start_line": function.start_line, "end_line": end_line},
        ),
        result(2, numbered),
        call(3, "edit_file", {"path": function.module, "old_text": old_text, "new_text": new_text}),
        result(3, f"ok: 1 substituição em {function.module}"),
        {
            "role": "assistant",
            "content": (
                f"Corrigido em `{function.module}`.\n\n"
                f"**Problema:** {error}.\n\n"
                f"Ajustei apenas o trecho afetado; o restante de `{function.name}` "
                f"permanece igual."
            ),
        },
    ]
    return {"kind": "corrigir", "key": f"{function.name}:{negative['error'][:40]}", "messages": messages}


def trace_add(project: Project, function, rng: random.Random) -> dict | None:
    """Add a routine to the right module, after checking the local conventions."""
    module = project.modules[function.module]
    siblings = [f for f in module.functions if f.name != function.name]
    if not siblings:
        return None
    reference = siblings[len(siblings) // 2]

    signature = signature_of(function.code)
    if not signature:
        return None

    anchor = reference.code.split("\n")[-1]
    haystack = module.text
    old_text = anchor
    if haystack.count(old_text) != 1:
        tail = reference.code.split("\n")[-3:]
        old_text = "\n".join(tail)
        if haystack.count(old_text) != 1:
            return None
    new_text = f"{old_text}\n\n{function.code}"

    question = rng.choice(
        [
            f"Adicione ao projeto a rotina `{signature}`, seguindo o padrão do módulo.",
            f"Crie `{signature}` no arquivo apropriado, mantendo o estilo do projeto.",
        ]
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
        call(1, "search_text", {"pattern": function.name}),
        result(1, "Nenhuma ocorrência encontrada."),
        call(2, "list_files", {}),
        result(2, project.list_files()),
        call(
            3,
            "read_file",
            {
                "path": function.module,
                "start_line": reference.start_line,
                "end_line": reference.end_line,
            },
        ),
        result(3, project.read_range(function.module, reference.start_line, reference.end_line)),
        call(4, "edit_file", {"path": function.module, "old_text": old_text, "new_text": new_text}),
        result(4, f"ok: 1 substituição em {function.module}"),
        {
            "role": "assistant",
            "content": (
                f"`{function.name}` adicionada em `{function.module}`, seguindo o padrão "
                f"de `{reference.name}`.\n\n"
                f"```foxpro\n{function.code}\n```"
            ),
        },
    ]
    return {"kind": "adicionar", "key": f"add:{function.name}", "messages": messages}


def trace_inspect(project: Project, function, rng: random.Random) -> dict | None:
    """Answer a question about the code without editing anything."""
    question = rng.choice(
        [
            f"O projeto já tem alguma rotina para {human_topic(function.name)}?",
            f"Existe algo pronto relacionado a {human_topic(function.name)}?",
        ]
    )
    token = re.match(r"^[FP]_([A-Za-z]+)", function.name)
    if not token:
        return None
    prefix = token.group(1)[:6]
    hits = project.search(rf"(FUNCTION|PROCEDURE)\s+[FP]_{prefix}", limit=6)
    if len(hits) < 2:
        return None

    names = []
    for path, line, text in hits:
        found = re.search(r"(?:FUNCTION|PROCEDURE)\s+(\S+)", text)
        if found:
            names.append((found.group(1), path, line))

    listing = "\n".join(f"- `{name}` em `{path}`, linha {line}" for name, path, line in names)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
        call(1, "search_text", {"pattern": f"FUNCTION [FP]_{prefix}"}),
        result(1, search_payload(hits)),
        {
            "role": "assistant",
            "content": f"Sim. O projeto já tem estas rotinas:\n\n{listing}\n\nNada foi alterado.",
        },
    ]
    # Chaveado pelo prefixo da busca, não pela rotina: toda rotina que
    # compartilha o prefixo gera a mesma busca e a mesma resposta, então
    # só um rastro é útil.
    return {"kind": "inspecionar", "key": f"inspect:{prefix}", "messages": messages}


def human_topic(name: str) -> str:
    stripped = re.sub(r"^[FP]_", "", name)
    words = re.findall(r"[A-Z][a-z]+|\d+", stripped)
    return " ".join(word.lower() for word in words[:2]) or stripped.lower()


# --------------------------------------------------------------------------- #
# Formatos de saída
# --------------------------------------------------------------------------- #
def to_hermes(messages: list[dict]) -> list[dict]:
    """Inline <tool_call>/<tool_response> blocks for Qwen-style templates."""
    converted: list[dict] = []
    for message in messages:
        if message["role"] == "assistant" and message.get("tool_calls"):
            blocks = []
            for tool_call in message["tool_calls"]:
                payload = {
                    "name": tool_call["function"]["name"],
                    "arguments": json.loads(tool_call["function"]["arguments"]),
                }
                blocks.append(
                    "<tool_call>\n" + json.dumps(payload, ensure_ascii=False) + "\n</tool_call>"
                )
            converted.append({"role": "assistant", "content": "\n".join(blocks)})
        elif message["role"] == "tool":
            converted.append(
                {
                    "role": "user",
                    "content": "<tool_response>\n" + message["content"] + "\n</tool_response>",
                }
            )
        else:
            converted.append({k: v for k, v in message.items() if k != "tool_calls"})
    return converted


def tools_as_text() -> str:
    lines = ["", "Ferramentas disponíveis (responda com uma chamada por vez):"]
    for tool in TOOLS:
        function = tool["function"]
        params = ", ".join(function["parameters"]["properties"]) or "sem argumentos"
        lines.append(f"- {function['name']}({params}): {function['description']}")
    return "\n".join(lines)


def estimate_tokens(messages: list[dict]) -> int:
    text = json.dumps(messages, ensure_ascii=False)
    return round(len(text) / 3.5)


# --------------------------------------------------------------------------- #
# Principal
# --------------------------------------------------------------------------- #
def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="Build agentic traces for VFP 9.")
    parser.add_argument("--sources", nargs="+", default=["vfp9.pr2", "exemplo.pr2"])
    parser.add_argument("--code-dir", type=Path, default=root / "ExemplosCodigo")
    parser.add_argument("--negative", type=Path, default=root / "ExemplosCodigo/ExemplosNegativos.pr2")
    parser.add_argument("--output-dir", type=Path, default=root / "data/training")
    parser.add_argument("--tool-format", choices=["openai", "hermes"], default="openai")
    parser.add_argument(
        "--tools-in-system",
        action="store_true",
        help="Append the tool list to the system prompt for trainers that ignore `tools`",
    )
    parser.add_argument("--max-tokens", type=int, default=3000, help="Drop traces longer than this")
    parser.add_argument("--max-fix-per-function", type=int, default=2)
    parser.add_argument("--val-ratio", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--suffix", default="_agent_pt")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rng = random.Random(args.seed)

    functions = load_functions([args.code_dir / name for name in args.sources])
    project = Project(functions)
    negatives = extract_negatives(args.negative.read_text(encoding="utf-8"))
    print(f"{len(functions)} rotinas em {len(project.modules)} módulos; {len(negatives)} negativos")

    traces: list[dict] = []
    per_function: Counter[str] = Counter()

    for negative in negatives:
        function = project.functions.get(negative["name"])
        if not function or per_function[function.name] >= args.max_fix_per_function:
            continue
        trace = trace_fix(project, function, negative, rng)
        if trace:
            per_function[function.name] += 1
            traces.append(trace)

    for function in project.functions.values():
        for builder in (trace_locate, trace_add, trace_inspect):
            trace = builder(project, function, rng)
            if trace:
                traces.append(trace)

    # Deduplica e aplica o orçamento de contexto.
    seen: set[str] = set()
    kept: list[dict] = []
    dropped_long = 0
    for trace in traces:
        if trace["key"] in seen:
            continue
        if estimate_tokens(trace["messages"]) > args.max_tokens:
            dropped_long += 1
            continue
        seen.add(trace["key"])
        kept.append(trace)

    # Parte por rotina para uma tarefa de validação nunca ser um treino disfarçado.
    def routine_of(trace: dict) -> str:
        return re.sub(r"^(add|inspect):", "", trace["key"]).split(":")[0]

    groups: dict[str, list[dict]] = {}
    for trace in kept:
        groups.setdefault(routine_of(trace), []).append(trace)

    names = sorted(groups)
    rng.shuffle(names)
    target = int(len(kept) * args.val_ratio)
    val: list[dict] = []
    val_names: set[str] = set()
    for name in names:
        if len(val) >= target:
            break
        val.extend(groups[name])
        val_names.add(name)
    train = [t for t in kept if routine_of(t) not in val_names]
    rng.shuffle(train)
    rng.shuffle(val)

    def render(trace: dict) -> dict:
        messages = [dict(m) for m in trace["messages"]]
        if args.tools_in_system:
            messages[0] = {"role": "system", "content": messages[0]["content"] + tools_as_text()}
        if args.tool_format == "hermes":
            return {"messages": to_hermes(messages)}
        return {"messages": messages, "tools": TOOLS}

    args.output_dir.mkdir(parents=True, exist_ok=True)
    train_path = args.output_dir / f"train{args.suffix}.jsonl"
    val_path = args.output_dir / f"val{args.suffix}.jsonl"
    for path, rows in ((train_path, train), (val_path, val)):
        with path.open("w", encoding="utf-8") as handle:
            for trace in rows:
                handle.write(json.dumps(render(trace), ensure_ascii=False) + "\n")

    tokens = sorted(estimate_tokens(t["messages"]) for t in kept)
    stats = {
        "routines": len(project.functions),
        "modules": {path: project.modules[path].line_count for path in sorted(project.modules)},
        "traces_total": len(kept),
        "traces_train": len(train),
        "traces_val": len(val),
        "kinds": dict(Counter(t["kind"] for t in kept)),
        "kinds_val": dict(Counter(t["kind"] for t in val)),
        "dropped_over_budget": dropped_long,
        "tokens_p50": tokens[len(tokens) // 2] if tokens else 0,
        "tokens_p95": tokens[int(len(tokens) * 0.95)] if tokens else 0,
        "tokens_max": tokens[-1] if tokens else 0,
        "tool_format": args.tool_format,
        "tools_in_system": args.tools_in_system,
        "max_tokens": args.max_tokens,
    }
    stats_path = args.output_dir / f"stats{args.suffix}.json"
    stats_path.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"traces: {len(kept)} {stats['kinds']}")
    print(f"  tokens p50={stats['tokens_p50']} p95={stats['tokens_p95']} max={stats['tokens_max']}")
    print(f"  descartados por exceder {args.max_tokens} tokens: {dropped_long}")
    print(f"  train -> {train_path} ({len(train)})")
    print(f"  val   -> {val_path} ({len(val)})")
    print(f"  stats -> {stats_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
