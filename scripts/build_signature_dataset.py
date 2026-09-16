#!/usr/bin/env python3
"""
Monta um dataset compacto de "fichas IntelliSense" a partir dos tópicos
limpos da ajuda do VFP 9.

Diferente do corpus em prosa, isto ensina o tipo de fato que um agente de
código não pode inventar no meio da linha: assinaturas exatas, nomes de
parâmetros e tipos de retorno. APIs alucinadas são o principal motivo de
FoxPro gerado não compilar; esse conhecimento cabe nos pesos, enquanto a
prosa explicativa cabe na recuperação.

As fichas são deliberadamente curtas. Um estilo verboso reintroduziria o
hábito de "responder com uma página de documentação", ruim para uso agentic.

Uso:
    python build_signature_dataset.py
    python build_signature_dataset.py --max-variants 2 --val-ratio 0.05
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

from build_training_dataset import split_train_val_by_topic, write_jsonl
from html_utils import project_paths, split_into_sections, useful_body_text

SYSTEM_PROMPT = (
    "Você é um assistente especializado em Microsoft Visual FoxPro 9. "
    "Responda com precisão técnica sobre comandos, funções, classes, "
    "propriedades, métodos e mensagens de erro."
)

CODE_BLOCK_RE = re.compile(r"```foxpro\n(.*?)```", re.S)
TERM_RE = re.compile(r"(?m)^\*\*(.+?)\*\*[ \t]*\n(.+?)(?=\n\*\*|\n#|\Z)", re.S)
# O Markdown PT costuma pôr um espaço antes de **Nome**; continua até o próximo termo ou título.
COMPLETE_TERM_RE = re.compile(
    r"(?m)^[ \t]*\*\*(.+?)\*\*[ \t]*\n(.*?)(?=^[ \t]*\*\*|\n#{1,6}\s|\Z)",
    re.S,
)
APPLIES_TO_RE = re.compile(r"Applies To:\s*(.+)")
APPLIES_TO_PT_RE = re.compile(r"Aplica-se a:\s*(.+)")
TABLE_LINE_RE = re.compile(r"(?m)^\|.*\|$")
SEE_ALSO_PT_RE = re.compile(
    r"(?ms)^#{1,6}\s+(?:See Also|Consulte tamb[eé]m)\s*\n.*\Z"
)

PARAM_HEADING_KEYS = (
    "parâmetro",
    "parametro",
    "parameter",
    "argument",
    "argumento",
)
RETURN_HEADING_KEYS = (
    "valor de retorno",
    "return value",
    "return values",
    "retorno",
    "returns",
)

ELEMENT_KINDS = (
    ("Function", "função"),
    ("Command", "comando"),
    ("Property", "propriedade"),
    ("Method", "método"),
    ("Event", "evento"),
    ("Class", "classe"),
    ("Object", "objeto"),
    ("System Variable", "variável de sistema"),
    ("API Library Routine", "rotina de API"),
)

# Títulos de seção que guardam os campos que queremos.
PARAM_KEYS = ("parameter", "argument", "parâmetro")
RETURN_KEYS = ("return value", "return values", "return")


def clean_sentence(text: str, limit: int = 220) -> str:
    """Primeira frase de um bloco, sem tabelas nem marcação."""
    text = TABLE_LINE_RE.sub("", text)
    text = re.sub(r"[*`>]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    match = re.search(r"^(.+?[.!?])(?:\s|$)", text)
    sentence = match.group(1) if match else text
    if len(sentence) > limit:
        sentence = sentence[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return sentence.strip()


def clean_applies_to(text: str, max_items: int = 12) -> str:
    """
    Mantém a lista Aplica-se a como lista.

    Truncá-la como prosa corta nomes de classe no meio, o que é pior do que
    não dizer nada: o agente aprenderia uma classe que não existe.
    """
    text = TABLE_LINE_RE.sub("", text)
    text = re.sub(r"[*`>]+", "", text)
    text = re.sub(r"\s+", " ", text).strip().rstrip(".")
    items = [item.strip() for item in text.split("|") if item.strip()]
    if not items:
        return ""
    # Crases mantêm os nomes de classe literais na tradução, do mesmo jeito
    # que os nomes de parâmetro são protegidos.
    shown = [f"`{item}`" for item in items[:max_items]]
    if len(items) <= max_items:
        return ", ".join(shown) + "."
    return ", ".join(shown) + f" (+{len(items) - max_items} outros)."


def ensure_period(text: str) -> str:
    return text if not text or text[-1] in ".!?…" else text + "."


def _norm_heading(heading: str) -> str:
    return heading.strip().lower()


def _heading_matches(heading: str, keys: tuple[str, ...]) -> bool:
    lowered = _norm_heading(heading)
    return any(lowered == key or lowered.startswith(key) for key in keys)


def clean_block(text: str, limit: int | None = None) -> str:
    """Mantém o corpo inteiro de parâmetro/retorno, inclusive tabelas e listas de flags."""
    text = re.sub(r"^>\s*", "", text, flags=re.M)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    text = re.sub(r"\s+", " ", text).strip() if "\n" not in text else text
    if not text:
        return ""
    if limit is not None and len(text) > limit:
        clipped = text[:limit].rsplit(" ", 1)[0].rstrip(",;:")
        return (clipped + "…").strip()
    return text


NONE_PARAM_RE = re.compile(r"^(?:nenhum|none|n/?a)\.?$", re.I)
TERM_TABLE_HEADER_RE = re.compile(
    r"termo|defini[cç][aã]o|term|definition|name|description|par[aâ]metro",
    re.I,
)
CODE_ROW_RE = re.compile(r"^.{1,3}\s+[A-ZÁÉÍÓÚÀÃÕ]")
PROSE_STARTERS = (
    "especifica",
    "incluir",
    "inclua",
    "para ",
    "quando ",
    "você ",
    "voce ",
    "the ",
    "this ",
    "you ",
    "row e ",
    "a primeira",
    "as coordenadas",
    "emita ",
    "use ",
    "using ",
)


def _looks_like_term_line(line: str) -> bool:
    text = line.strip()
    if not text or text.startswith(("#", "|", ">")):
        return False
    if text.startswith(("- ", "* ")) and not text.startswith("**"):
        return False
    if re.match(r"^\*\*.+\*\*\s*$", text):
        return True
    if NONE_PARAM_RE.match(text):
        return False
    if re.fullmatch(r"[-–—= ]+", text) or text.endswith(":"):
        return False
    if re.fullmatch(r"[A-Za-z]/[A-Za-z*+]+", text):
        return False
    if re.match(r"^RGB\s*\(", text, re.I):
        return False
    if text.startswith("@"):
        return False
    if re.search(r"['\"]", text):
        return False
    if re.match(
        r"^(STORE|READ|SKIP|CASE|IF|ELSE|ENDIF|FOR|ENDFOR|WHILE|ENDDO|RETURN|WAIT|CLEAR|CLOSE)\b",
        text,
        re.I,
    ) and "|" not in text and "[" not in text:
        return False
    if re.search(r",{2,}", text) or re.search(r"[A-Z]\+/[A-Z]", text):
        return False
    if (
        re.search(r"\b\d+\b", text)
        and not re.search(r"exp[CNL]\d", text, re.I)
        and not re.fullmatch(r"\d+", text)
    ):
        return False
    if len(text) > 90 or re.search(r"[.!]", text):
        return False
    if not re.search(r"[A-Za-z_0-9@]", text):
        return False
    words = text.split()
    if len(words) >= 8 and "|" not in text and "[" not in text:
        return False
    lowered = text.lower()
    if lowered.startswith(PROSE_STARTERS):
        return False
    if CODE_ROW_RE.match(text) and "|" not in text and "," not in text:
        return False
    # Prosa em Title Case ("Códigos de função"), não um nome de parâmetro.
    if (
        len(words) >= 2
        and re.match(r"^[A-ZÁÉÍÓÚÀÃÕ]", text)
        and not re.search(r"[,|\[\]()@\d]", text)
    ):
        return False
    return True


def _parse_term_table(body: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    lines = [line for line in (body or "").splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return rows
    header = lines[0].strip().strip("|")
    if not TERM_TABLE_HEADER_RE.search(header):
        return rows
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] and cells[1] and "---" not in cells[0]:
            rows.append((cells[0], ensure_period(clean_block(cells[1]))))
    return [(name, desc) for name, desc in rows if name and desc]


def _parse_plain_parameters(body: str) -> list[tuple[str, str]]:
    parameters: list[tuple[str, str]] = []
    lines = (body or "").splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if not _looks_like_term_line(line):
            index += 1
            continue
        name = re.sub(r"^\*\*(.+)\*\*$", r"\1", line.strip()).strip()
        index += 1
        desc_lines: list[str] = []
        while index < len(lines) and not _looks_like_term_line(lines[index]):
            desc_lines.append(lines[index])
            index += 1
        description = ensure_period(clean_block("\n".join(desc_lines)))
        if name and not NONE_PARAM_RE.match(name) and description:
            if description.lstrip().startswith(("@", "```")):
                continue
            parameters.append((name, description))
    return parameters


def parse_parameters(body: str, allow_plain: bool = True) -> list[tuple[str, str]]:
    parameters: list[tuple[str, str]] = []
    for name, description in COMPLETE_TERM_RE.findall(body or ""):
        name = name.strip()
        description = ensure_period(clean_block(description))
        if name and description:
            parameters.append((name, description))
    if parameters:
        return parameters
    table_rows = _parse_term_table(body or "")
    if table_rows:
        return table_rows
    if not allow_plain:
        return []
    return _parse_plain_parameters(body or "")


def build_complete_card(title: str, content: str) -> dict | None:
    """Ficha a partir de uma página Markdown PT (ou EN): parâmetros completos e valor de retorno."""
    content = SEE_ALSO_PT_RE.sub("", content).strip()
    content = useful_body_text(content)
    signature_match = CODE_BLOCK_RE.search(content)
    if not signature_match:
        return None
    signature = signature_match.group(1).strip()
    if not signature:
        return None

    sections = split_into_sections(content)
    intro = next((body for heading, body in sections if not heading), "")
    param_body = ""
    return_body = ""
    for heading, body in sections:
        if not heading:
            continue
        if _heading_matches(heading, PARAM_HEADING_KEYS):
            param_body = body
        elif _heading_matches(heading, RETURN_HEADING_KEYS):
            return_body = body

    parameters = parse_parameters(param_body, allow_plain=True)
    if not parameters and not param_body:
        parameters = parse_parameters(content, allow_plain=False)

    returns = ensure_period(clean_block(return_body))
    intro_prose = CODE_BLOCK_RE.sub("", intro)
    purpose = ensure_period(clean_sentence(intro_prose, limit=300))
    applies = APPLIES_TO_PT_RE.search(content) or APPLIES_TO_RE.search(content)
    applies_to = clean_applies_to(applies.group(1)) if applies else ""

    if not purpose and not parameters and not returns:
        return None

    english, portuguese = element_kind(title)
    return {
        "topic_id": "",
        "title": title,
        "name": display_name(title),
        "kind_en": english,
        "kind_pt": portuguese,
        "signature": signature,
        "purpose": purpose,
        "parameters": parameters,
        "returns": returns,
        "applies_to": applies_to,
    }


def element_kind(title: str) -> tuple[str, str]:
    for english, portuguese in ELEMENT_KINDS:
        if re.search(rf"\b{re.escape(english)}\b", title):
            return english, portuguese
    return "", "elemento"


def display_name(title: str) -> str:
    """`ASORT( ) Function` -> `ASORT( )`; preserva nomes no estilo SYS(2015)."""
    for english, _ in ELEMENT_KINDS:
        title = re.sub(rf"\s+{re.escape(english)}\s*$", "", title)
    return re.sub(r"\s*\(Visual FoxPro\)\s*$", "", title).strip()


def build_card(topic: dict) -> dict | None:
    content = useful_body_text(topic["content"])
    signature_match = CODE_BLOCK_RE.search(content)
    if not signature_match:
        return None
    signature = signature_match.group(1).strip()
    if not signature or len(signature) > 600:
        return None

    sections = split_into_sections(content)
    named = {heading.lower(): body for heading, body in sections if heading}
    intro = next((body for heading, body in sections if not heading), "")

    def section(keys: tuple[str, ...]) -> str:
        for key, body in named.items():
            if any(key.startswith(prefix) for prefix in keys):
                return body
        return ""

    parameters: list[tuple[str, str]] = []
    for name, description in TERM_RE.findall(section(PARAM_KEYS)):
        name = name.strip()
        description = ensure_period(clean_sentence(description, limit=200))
        if name and description:
            parameters.append((name, description))

    returns = ensure_period(clean_sentence(section(RETURN_KEYS), limit=400))
    purpose = ensure_period(clean_sentence(intro, limit=300))
    applies = APPLIES_TO_RE.search(content)
    applies_to = clean_applies_to(applies.group(1)) if applies else ""

    if not purpose and not parameters and not returns:
        return None

    english, portuguese = element_kind(topic["title"])
    return {
        "topic_id": topic["id"],
        "title": topic["title"],
        "name": display_name(topic["title"]),
        "kind_en": english,
        "kind_pt": portuguese,
        "signature": signature,
        "purpose": purpose,
        "parameters": parameters[:12],
        "returns": returns,
        "applies_to": applies_to,
    }


def translatable_fields(card: dict) -> list[str]:
    """
    Prosa de uma ficha, em unidades independentes.

    Assinaturas, nomes de parâmetro e a lista Aplica-se a são código e
    permanecem em inglês; só estas cadeias vão para o tradutor.
    """
    fields = [card["purpose"], card["returns"]]
    fields += [description for _, description in card["parameters"]]
    return [field for field in fields if field]


def apply_translations(card: dict, table: dict[str, str]) -> dict:
    """Devolve uma cópia da ficha com cada campo conhecido trocado pelo texto em pt-BR."""
    translated = dict(card)
    translated["purpose"] = table.get(card["purpose"], card["purpose"])
    translated["returns"] = table.get(card["returns"], card["returns"])
    translated["parameters"] = [
        (name, table.get(description, description)) for name, description in card["parameters"]
    ]
    return translated


def render_card(card: dict) -> str:
    lines = [f"```foxpro\n{card['signature']}\n```"]
    if card["purpose"]:
        lines.append(card["purpose"])
    if card["parameters"]:
        block = ["Parâmetros:"]
        block += [f"- `{name}` — {desc}" for name, desc in card["parameters"]]
        lines.append("\n".join(block))
    if card["returns"]:
        lines.append(f"Retorno: {card['returns']}")
    if card["applies_to"]:
        lines.append(f"Aplica-se a: {card['applies_to']}")
    return "\n\n".join(lines)


def render_parameters(card: dict) -> str:
    block = [f"Parâmetros de `{card['name']}`:"]
    block += [f"- `{name}` — {desc}" for name, desc in card["parameters"]]
    return "\n".join(block)


def question_bank(card: dict) -> list[tuple[str, str, str]]:
    """Candidatos (tipo, pergunta, resposta) para uma ficha, os mais úteis primeiro."""
    name = card["name"]
    kind = card["kind_pt"]
    out: list[tuple[str, str, str]] = []

    out.append(("ficha", f"Ficha de referência de {name} no Visual FoxPro 9.", render_card(card)))

    out.append(
        (
            "assinatura",
            f"Qual é a assinatura de {name} no VFP 9?",
            f"```foxpro\n{card['signature']}\n```",
        )
    )

    if card["parameters"]:
        out.append(
            ("parametros", f"Quais são os parâmetros de {name} no VFP 9?", render_parameters(card))
        )

    if card["returns"]:
        out.append(("retorno", f"O que {name} retorna no VFP 9?", f"Retorno: {card['returns']}"))

    if card["applies_to"] and card["kind_en"] in {"Property", "Method", "Event"}:
        out.append(
            (
                "aplica_se",
                f"A quais classes se aplica a {kind} {name} no VFP 9?",
                f"Aplica-se a: {card['applies_to']}",
            )
        )

    return out


def format_example(question: str, answer: str) -> dict:
    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }


def parse_args() -> argparse.Namespace:
    paths = project_paths(__file__)
    parser = argparse.ArgumentParser(description="Build VFP 9 signature-card dataset.")
    parser.add_argument("--input", type=Path, default=paths["data_dir"] / "topics.jsonl")
    parser.add_argument("--output-dir", type=Path, default=paths["data_dir"] / "training")
    parser.add_argument("--val-ratio", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--max-variants",
        type=int,
        default=1,
        help="Examples per topic (1 = full card only; higher adds targeted questions)",
    )
    parser.add_argument("--suffix", default="_sig_pt")
    parser.add_argument(
        "--translations",
        type=Path,
        help="JSON mapping of English field -> PT-BR field, applied while rendering",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.exists():
        print(f"Input not found: {args.input}\nRun extract_content.py first.", file=sys.stderr)
        return 1

    topics = [json.loads(line) for line in args.input.open(encoding="utf-8") if line.strip()]
    print(f"Loaded {len(topics)} topics from {args.input}")

    cards = [card for card in (build_card(topic) for topic in topics) if card]
    print(f"Built {len(cards)} signature cards")

    table: dict[str, str] = {}
    if args.translations and args.translations.exists():
        table = json.loads(args.translations.read_text(encoding="utf-8"))
        wanted = {field for card in cards for field in translatable_fields(card)}
        covered = len(wanted & table.keys())
        print(f"Translations: {covered}/{len(wanted)} fields ({covered / len(wanted):.0%})")
        cards = [apply_translations(card, table) for card in cards]

    rng = random.Random(args.seed)
    records: list[dict] = []
    kinds: Counter[str] = Counter()
    seen_questions: set[str] = set()

    for card in cards:
        candidates = question_bank(card)
        chosen = candidates[: max(1, args.max_variants)]
        for kind, question, answer in chosen:
            if question in seen_questions:
                continue
            seen_questions.add(question)
            kinds[kind] += 1
            records.append(
                {
                    "topic_id": card["topic_id"],
                    "kind": kind,
                    "example": format_example(question, answer),
                }
            )

    rng.shuffle(records)
    train, val = split_train_val_by_topic(records, args.val_ratio, args.seed)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    train_path = args.output_dir / f"train{args.suffix}.jsonl"
    val_path = args.output_dir / f"val{args.suffix}.jsonl"
    write_jsonl(train_path, [r["example"] for r in train])
    write_jsonl(val_path, [r["example"] for r in val])

    answers = [r["example"]["messages"][2]["content"] for r in records]
    prose = sum(len(CODE_BLOCK_RE.sub("", a)) for a in answers)
    stats = {
        "topics": len(topics),
        "cards": len(cards),
        "examples_total": len(records),
        "examples_train": len(train),
        "examples_val": len(val),
        "train_topics": len({r["topic_id"] for r in train}),
        "val_topics": len({r["topic_id"] for r in val}),
        "kinds": dict(kinds),
        "cards_with_parameters": sum(1 for c in cards if c["parameters"]),
        "cards_with_returns": sum(1 for c in cards if c["returns"]),
        "parameters_total": sum(len(c["parameters"]) for c in cards),
        "chars_total": sum(len(a) for a in answers),
        "chars_prose_to_translate": prose,
        "max_variants": args.max_variants,
        "val_ratio": args.val_ratio,
        "seed": args.seed,
    }
    stats_path = args.output_dir / f"stats{args.suffix}.json"
    stats_path.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"  examples: {len(records)} {dict(kinds)}")
    print(f"  parameters documented: {stats['parameters_total']}")
    print(f"  prose to translate: {prose:,} chars")
    print(f"  train -> {train_path} ({len(train)} rows, {stats['train_topics']} topics)")
    print(f"  val   -> {val_path} ({len(val)} rows, {stats['val_topics']} topics)")
    print(f"  stats -> {stats_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
