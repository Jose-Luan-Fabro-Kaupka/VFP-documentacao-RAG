#!/usr/bin/env python3
"""
Transforma tópicos limpos da ajuda VFP em exemplos de treino QLoRA / SFT.

Uso:
    python build_training_dataset.py
    python build_training_dataset.py --format alpaca --locale pt --val-ratio 0.1
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

from html_utils import project_paths, split_into_sections, useful_body_text

SYSTEM_PROMPT_EN = (
    "You are an expert assistant for Microsoft Visual FoxPro 9. "
    "Answer with accurate technical details about commands, functions, classes, "
    "properties, methods, and error messages."
)

SYSTEM_PROMPT_PT = (
    "Você é um assistente especializado em Microsoft Visual FoxPro 9. "
    "Responda com precisão técnica sobre comandos, funções, classes, "
    "propriedades, métodos e mensagens de erro."
)

ERROR_TITLE_RE = re.compile(r"\(Error\s+(\d+)\)", re.I)
CODE_BLOCK_RE = re.compile(r"```foxpro\n(.*?)```", re.S | re.I)

QUESTION_TEMPLATES = {
    "en": {
        "explain": [
            "Explain: {title}",
            "What is {title} in Visual FoxPro 9?",
            "Provide documentation for {title}.",
        ],
        "section": [
            "In Visual FoxPro 9, explain the {section} section of {title}.",
            "What does the {section} section say about {title}?",
        ],
        "keyword": [
            "In Visual FoxPro 9, what does HELP {keyword} refer to?",
            "Tell me about {keyword} in VFP 9.",
        ],
        "error": [
            "What does Visual FoxPro error {error_code} mean?",
            "Explain error {error_code} in VFP 9: {title}",
        ],
        "syntax": [
            "What is the syntax for {title}?",
            "Show the syntax of {title} in Visual FoxPro 9.",
        ],
        "code": [
            "How do I use {title} in Visual FoxPro 9? Include an example.",
            "Show a Visual FoxPro example related to {title}.",
        ],
    },
    "pt": {
        "explain": [
            "Explique: {title}",
            "O que é {title} no Visual FoxPro 9?",
            "Forneça a documentação de {title}.",
        ],
        "section": [
            "No Visual FoxPro 9, explique a seção {section} de {title}.",
            "O que a seção {section} diz sobre {title}?",
        ],
        "keyword": [
            "No Visual FoxPro 9, a keyword HELP {keyword} se refere a quê?",
            "Fale sobre {keyword} no VFP 9.",
        ],
        "error": [
            "O que significa o erro {error_code} no Visual FoxPro?",
            "Explique o erro {error_code} no VFP 9: {title}",
        ],
        "syntax": [
            "Qual é a sintaxe de {title}?",
            "Mostre a sintaxe de {title} no Visual FoxPro 9.",
        ],
        "code": [
            "Como usar {title} no Visual FoxPro 9? Inclua um exemplo.",
            "Mostre um exemplo em Visual FoxPro relacionado a {title}.",
        ],
    },
}

SECTION_PRIORITY = (
    "remarks",
    "parameters",
    "return value",
    "example",
    "examples",
    "usage",
)


def parse_args() -> argparse.Namespace:
    paths = project_paths(__file__)
    parser = argparse.ArgumentParser(description="Build SFT/QLoRA training dataset from cleaned topics.")
    parser.add_argument(
        "--input",
        type=Path,
        default=paths["data_dir"] / "topics.jsonl",
        help="Cleaned topics JSONL produced by extract_content.py",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=paths["data_dir"] / "training",
        help="Directory for train/val JSONL outputs",
    )
    parser.add_argument(
        "--format",
        choices=["messages", "alpaca"],
        default="messages",
        help="Output format: OpenAI-style messages or Alpaca instruction/input/output",
    )
    parser.add_argument(
        "--locale",
        choices=["en", "pt"],
        default="en",
        help="Language for generated user questions (answers stay in source language)",
    )
    parser.add_argument(
        "--val-ratio",
        type=float,
        default=0.05,
        help="Fraction of examples reserved for validation",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for train/val split and template sampling",
    )
    parser.add_argument(
        "--max-keywords",
        type=int,
        default=1,
        help="Max keyword-based examples per topic when chosen as specialty (0 disables)",
    )
    parser.add_argument(
        "--max-variants",
        type=int,
        default=1,
        help="Max question variants per example kind",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=4000,
        help="Max chars per answer chunk (longer topics are split by section)",
    )
    parser.add_argument(
        "--min-answer-chars",
        type=int,
        default=100,
        help="Drop prose answers shorter than this (syntax/code answers are exempt)",
    )
    parser.add_argument(
        "--max-answer-repeats",
        type=int,
        default=2,
        help="How often the same answer text may be reused with different questions",
    )
    parser.add_argument(
        "--max-section-chunks",
        type=int,
        default=3,
        help="Max extra section-based examples for long topics",
    )
    parser.add_argument(
        "--include-system",
        action="store_true",
        default=True,
        help="Include a system prompt in each example",
    )
    parser.add_argument(
        "--no-system",
        action="store_true",
        help="Omit system prompt from examples",
    )
    return parser.parse_args()


def load_topics(path: Path) -> list[dict]:
    topics: list[dict] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                topics.append(json.loads(line))
    return topics


def pick_templates(locale: str, kind: str, max_variants: int, rng: random.Random) -> list[str]:
    templates = QUESTION_TEMPLATES[locale][kind]
    if max_variants <= 0:
        return []
    if max_variants >= len(templates):
        return templates
    return rng.sample(templates, max_variants)


def format_example(
    user: str,
    assistant: str,
    output_format: str,
    include_system: bool,
    system_prompt: str,
) -> dict:
    if output_format == "messages":
        messages = []
        if include_system:
            messages.append({"role": "system", "content": system_prompt})
        messages.extend(
            [
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant},
            ]
        )
        return {"messages": messages}

    return {
        "instruction": user,
        "input": "",
        "output": assistant,
    }


STATEMENT_RE = re.compile(
    r"(?mi)^\s*(?:\?{1,2}|\*|&&|USE|SELECT|DO|IF|ELSE|ENDIF|FOR|ENDFOR|DEFINE|PROCEDURE|"
    r"FUNCTION|ENDPROC|ENDDEFINE|STORE|SET|CREATE|LOCAL|PUBLIC|PRIVATE|LPARAMETERS|"
    r"PARAMETERS|WITH|ENDWITH|CLOSE|GO|GOTO|SCAN|ENDSCAN|WAIT|CLEAR|RETURN|THIS|THISFORM|"
    r"INSERT|UPDATE|DELETE|APPEND|REPLACE|INDEX|BROWSE|REPORT|MODIFY|COPY|SCATTER|GATHER|"
    r"TRY|CATCH|ENDTRY|TEXT|ENDTEXT|DIMENSION|RELEASE|ON|OPEN|ZAP|PACK|SKIP|LOCATE)\b"
)
MARKUP_START_RE = re.compile(r"^\s*<(?:\?xml|!DOCTYPE|[A-Za-z][\w:-]*[\s>/])")


def all_code_blocks(content: str) -> list[str]:
    return [m.group(1).strip() for m in CODE_BLOCK_RE.finditer(content) if m.group(1).strip()]


def looks_like_markup(code: str) -> bool:
    return bool(MARKUP_START_RE.match(code))


def looks_like_syntax_template(code: str) -> bool:
    """True for signature/grammar blocks such as `USE [TableName] [IN nWorkArea]`."""
    optional_markers = code.count("[") + code.count("]") + code.count("|")
    if optional_markers == 0:
        return False
    has_assignment = bool(re.search(r"(?m)^[^\n=]*[A-Za-z0-9_\)]\s*=\s*\S", code))
    has_comment = "&&" in code or bool(re.search(r"(?m)^\s*\*", code))
    if has_assignment or has_comment:
        return False
    # Blocos de gramática são densos em marcadores opcionais e não trazem valores concretos.
    return optional_markers >= 3 or code.count("\n") <= 1


def is_real_example_code(code: str) -> bool:
    if len(code) < 20 or looks_like_markup(code) or looks_like_syntax_template(code):
        return False
    lines = [ln for ln in code.split("\n") if ln.strip()]
    if not lines:
        return False
    if not STATEMENT_RE.search(code) and "=" not in code:
        return False
    # Blocos fragmentários como um `SYS(` nu ou `oMyForm.` não servem de exemplo.
    if len(lines) == 1 and (lines[0].rstrip().endswith((".", "(", ",", ";")) or len(lines[0]) < 24):
        return False
    return True


def example_code_block(content: str) -> str | None:
    """Pick a runnable example, preferring code under an Example heading."""
    candidates: list[str] = []
    for heading, body in split_into_sections(content):
        if heading.lower().startswith("example"):
            candidates.extend(all_code_blocks(body))
    if not candidates:
        # Pula o bloco inicial: em tópicos de referência ele é a assinatura.
        candidates = all_code_blocks(content)[1:]
    usable = [code for code in candidates if is_real_example_code(code)]
    if not usable:
        return None
    return max(usable, key=len)


def first_syntax(content: str) -> str | None:
    # Prefere o primeiro bloco cercado quando parece uma assinatura de uma linha.
    blocks = all_code_blocks(content)
    if not blocks:
        return None
    code = blocks[0]
    if len(code) >= 8 and code.count("\n") <= 2 and len(code) < 220:
        return code.replace("\n", " ").strip()
    return None


def _close_open_fences(text: str) -> str:
    """Ensure Markdown code fences are balanced."""
    fence_count = len(re.findall(r"(?m)^```", text))
    if fence_count % 2 == 1:
        text = text.rstrip() + "\n```"
    return text


def clip_answer(content: str, max_chars: int) -> str:
    """
    Clip text safely for training:
    - prefer section / paragraph boundaries
    - never cut mid-word
    - close any open code fence
    """
    answer = content.strip()
    if max_chars <= 0 or len(answer) <= max_chars:
        return _close_open_fences(answer)

    window = answer[:max_chars]

    # Prefere cortar antes de um título Markdown perto do fim da janela.
    heading_cut = None
    for match in re.finditer(r"(?m)^#{1,4}\s+", window):
        if match.start() >= max_chars // 3:
            heading_cut = match.start()
    if heading_cut is not None:
        candidate = window[:heading_cut].rstrip()
        if candidate:
            return _close_open_fences(candidate)

    # Em seguida: fronteira de parágrafo.
    para_cut = window.rfind("\n\n")
    if para_cut >= max_chars // 3:
        candidate = window[:para_cut].rstrip()
        if candidate:
            return _close_open_fences(candidate)

    # Em seguida: uma quebra de linha.
    line_cut = window.rfind("\n")
    if line_cut >= max_chars // 3:
        candidate = window[:line_cut].rstrip()
        if candidate:
            return _close_open_fences(candidate)

    # Em seguida: fim de frase.
    sentence_cut = max(window.rfind(". "), window.rfind("? "), window.rfind("! "))
    if sentence_cut >= max_chars // 3:
        candidate = window[: sentence_cut + 1].rstrip()
        if candidate:
            return _close_open_fences(candidate)

    # Último recurso: quebra em espaço em branco (nunca no meio da palavra).
    space_cut = window.rfind(" ")
    if space_cut >= max_chars // 4:
        candidate = window[:space_cut].rstrip()
    else:
        candidate = window.rstrip()

    # Se ainda terminar no meio do token, recua até o espaço anterior.
    if candidate and re.search(r"[A-Za-z0-9]$", candidate):
        ws = candidate.rfind(" ")
        if ws >= max_chars // 5:
            candidate = candidate[:ws].rstrip()

    return _close_open_fences(candidate)


def pack_blocks(blocks: list[str], max_chars: int) -> str:
    """Join whole blocks until max_chars; clip only the overflowing block safely."""
    if not blocks:
        return ""
    if max_chars <= 0:
        return _close_open_fences("\n\n".join(blocks).strip())

    packed: list[str] = []
    used = 0
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        extra = len(block) + (2 if packed else 0)
        if used + extra <= max_chars:
            packed.append(block)
            used += extra
            continue
        if not packed:
            # Só o primeiro bloco já é grande demais: recorta com segurança.
            return clip_answer(block, max_chars)
        break
    return _close_open_fences("\n\n".join(packed).strip())


def useful_keywords(title: str, keywords: list[str]) -> list[str]:
    title_l = title.lower()
    out: list[str] = []
    for kw in keywords:
        kw_l = kw.lower().strip()
        if len(kw_l) < 2 or kw_l.startswith("vfp."):
            continue
        if kw_l == title_l:
            continue
        if kw_l in title_l or title_l in kw_l:
            continue
        out.append(kw)
    return out


def build_overview_answer(topic: dict, max_chars: int) -> str:
    """Compact overview for the main explain example."""
    content = useful_body_text(topic["content"])
    sections = split_into_sections(content)
    if not sections:
        return clip_answer(content, max_chars)

    intro = ""
    selected: list[str] = []
    for heading, body in sections:
        if not heading:
            intro = body
            continue
        key = heading.lower()
        if key in SECTION_PRIORITY[:4] or key.startswith("parameter"):
            selected.append(f"## {heading}\n{body}")

    blocks: list[str] = []
    if intro:
        blocks.append(intro)
    blocks.extend(selected[:4])
    if not blocks:
        blocks = [f"## {h}\n{b}" if h else b for h, b in sections[:2]]
    return pack_blocks(blocks, max_chars)


def choose_specialty(
    topic: dict,
    max_keywords: int,
    rng: random.Random,
) -> tuple[str, dict] | None:
    """Pick at most one specialty example kind to reduce redundancy."""
    title = topic["title"]
    content = topic["content"]
    candidates: list[tuple[str, dict]] = []

    error_match = ERROR_TITLE_RE.search(title)
    if error_match:
        candidates.append(
            (
                "error",
                {
                    "error_code": error_match.group(1),
                    "answer": useful_body_text(content),
                },
            )
        )

    syntax = first_syntax(content)
    if syntax:
        candidates.append(("syntax", {"syntax": syntax}))

    code = example_code_block(content)
    if code:
        candidates.append(("code", {"code": code}))

    kws = useful_keywords(title, topic.get("keywords") or [])[:max_keywords]
    if kws:
        candidates.append(("keyword", {"keyword": kws[0]}))

    if not candidates:
        return None

    # Prefere erro/sintaxe/código a palavra-chave quando houver.
    ranked = sorted(
        candidates,
        key=lambda item: {"error": 0, "syntax": 1, "code": 2, "keyword": 3}.get(item[0], 9),
    )
    top_rank = {"error": 0, "syntax": 1, "code": 2, "keyword": 3}.get(ranked[0][0], 9)
    top = [item for item in ranked if {"error": 0, "syntax": 1, "code": 2, "keyword": 3}.get(item[0], 9) == top_rank]
    return rng.choice(top)


def build_section_chunks(
    topic: dict,
    max_chars: int,
    max_section_chunks: int,
) -> list[tuple[str, str]]:
    """Return (section_name, answer) chunks for long topics."""
    content = useful_body_text(topic["content"])
    if len(content) <= max_chars:
        return []

    sections = split_into_sections(content)
    chunks: list[tuple[str, str]] = []
    for heading, body in sections:
        if not heading:
            continue
        key = heading.lower()
        if key not in SECTION_PRIORITY and not key.startswith("parameter"):
            # Ainda permite seções nomeadas substanciais.
            if len(body) < 200:
                continue
        answer = clip_answer(f"{topic['title']} — {heading}\n\n{body}", max_chars)
        if len(answer) < 80:
            continue
        chunks.append((heading, answer))

    # Prefere primeiro as seções priorizadas.
    def rank(item: tuple[str, str]) -> tuple[int, int]:
        key = item[0].lower()
        try:
            return (SECTION_PRIORITY.index(key), -len(item[1]))
        except ValueError:
            if key.startswith("parameter"):
                return (1, -len(item[1]))
            return (50, -len(item[1]))

    chunks.sort(key=rank)
    return chunks[:max_section_chunks]


BARE_TOKEN_RE = re.compile(r"^[A-Za-z_][\w().\-]*$")
CODE_KINDS = {"syntax", "code"}


def answer_reject_reason(answer: str, kind: str, min_chars: int) -> str | None:
    """Return why an answer is unusable for training, or None when it is fine."""
    text = answer.strip()
    if not text:
        return "empty"

    if kind in CODE_KINDS:
        blocks = all_code_blocks(text)
        if not blocks or len(blocks[0]) < 12:
            return "code_too_small"
        return None

    # Tópicos de erro são legitimamente curtos ("Valid types are: CONNECTION, VIEW, ...").
    floor = 40 if kind == "error" else min_chars
    if len(text) < floor:
        return "too_short"

    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    last = lines[-1]

    # Recortado logo após o termo de uma lista de definição, deixando a descrição para trás.
    if re.fullmatch(r"\*\*.+?\*\*", last):
        return "dangling_term"
    if last.startswith("#"):
        return "heading_tail"
    # Dois-pontos no fim significam que a frase que ele introduziu foi cortada.
    if last.endswith(":") and not last.startswith("|"):
        return "trailing_colon"

    # Dump de navegação: listas nuas de identificadores (palavras reservadas, índices de comando).
    tail = lines[-8:]
    bare = sum(1 for ln in tail if BARE_TOKEN_RE.match(ln))
    if len(tail) >= 5 and bare >= len(tail) - 1:
        return "identifier_list"

    bullets = sum(1 for ln in lines if ln.startswith("- "))
    prose_chars = len(re.sub(r"(?m)^\s*-\s+.*$", "", text).strip())
    if bullets >= 5 and prose_chars < 200:
        return "link_dump"

    if not last.endswith(("```", "|", ".", "!", "?", '"', "'", ")")):
        return "truncated_tail"

    return None


def build_examples_for_topic(
    topic: dict,
    locale: str,
    output_format: str,
    include_system: bool,
    system_prompt: str,
    max_keywords: int,
    max_variants: int,
    max_chars: int,
    max_section_chunks: int,
    rng: random.Random,
    min_answer_chars: int = 0,
    rejects: Counter | None = None,
) -> list[dict]:
    title = topic["title"]
    overview = build_overview_answer(topic, max_chars)
    if not overview:
        return []

    examples: list[dict] = []
    seen_questions: set[str] = set()

    def add(question: str, answer: str, kind: str) -> None:
        q = question.strip()
        a = answer.strip()
        if not q or not a or q in seen_questions:
            return
        reason = answer_reject_reason(a, kind, min_answer_chars)
        if reason:
            if rejects is not None:
                rejects[reason] += 1
            return
        seen_questions.add(q)
        examples.append(
            {
                "topic_id": topic["id"],
                "title": title,
                "kind": kind,
                "example": format_example(
                    user=q,
                    assistant=a,
                    output_format=output_format,
                    include_system=include_system,
                    system_prompt=system_prompt,
                ),
            }
        )

    # 1) Um exemplo de visão geral / explicação.
    for template in pick_templates(locale, "explain", max_variants, rng):
        add(template.format(title=title), overview, "explain")

    # 2) No máximo um exemplo especial (erro OU sintaxe OU código OU palavra-chave).
    specialty = choose_specialty(topic, max_keywords=max_keywords, rng=rng)
    if specialty:
        kind, payload = specialty
        if kind == "error":
            for template in pick_templates(locale, "error", max_variants, rng):
                add(
                    template.format(error_code=payload["error_code"], title=title),
                    clip_answer(payload["answer"], max_chars),
                    "error",
                )
        elif kind == "syntax":
            for template in pick_templates(locale, "syntax", 1, rng):
                add(
                    template.format(title=title),
                    f"The syntax for {title} is:\n\n```foxpro\n{payload['syntax']}\n```",
                    "syntax",
                )
        elif kind == "code":
            for template in pick_templates(locale, "code", 1, rng):
                add(
                    template.format(title=title),
                    (
                        f"Here is a Visual FoxPro example for {title}:\n\n"
                        f"```foxpro\n{payload['code']}\n```"
                    ),
                    "code",
                )
        elif kind == "keyword":
            for template in pick_templates(locale, "keyword", 1, rng):
                add(
                    template.format(keyword=payload["keyword"], title=title),
                    overview,
                    "keyword",
                )

    # 3) Em tópicos longos, acrescenta pedaços de seção em vez de truncar às cegas.
    for section_name, answer in build_section_chunks(
        topic, max_chars=max_chars, max_section_chunks=max_section_chunks
    ):
        for template in pick_templates(locale, "section", 1, rng):
            add(template.format(title=title, section=section_name), answer, "section")

    return examples


def split_train_val_by_topic(
    records: list[dict], val_ratio: float, seed: int
) -> tuple[list[dict], list[dict]]:
    """Hold out whole topics so no validation answer was seen during training."""
    by_topic: dict[str, list[dict]] = {}
    for record in records:
        by_topic.setdefault(record["topic_id"], []).append(record)

    topic_ids = sorted(by_topic)
    rng = random.Random(seed)
    rng.shuffle(topic_ids)

    target = int(len(records) * val_ratio)
    val: list[dict] = []
    val_topics: set[str] = set()
    for topic_id in topic_ids:
        if len(val) >= target:
            break
        val.extend(by_topic[topic_id])
        val_topics.add(topic_id)

    train = [r for r in records if r["topic_id"] not in val_topics]
    rng.shuffle(train)
    rng.shuffle(val)
    return train, val


def drop_cross_split_duplicates(train: list[dict], val: list[dict]) -> tuple[list[dict], int]:
    """Remove validation rows whose question or answer also appears in training."""
    train_answers = {assistant_text(r["example"]) for r in train}
    train_questions = {user_text(r["example"]) for r in train}
    kept = [
        r
        for r in val
        if assistant_text(r["example"]) not in train_answers
        and user_text(r["example"]) not in train_questions
    ]
    return kept, len(val) - len(kept)


def dedupe_questions(records: list[dict]) -> tuple[list[dict], int]:
    """
    Keep one record per question text.

    Unrelated topics can share a keyword and produce the same question; training
    on the same prompt with conflicting answers only teaches ambiguity.
    """
    seen: set[str] = set()
    kept: list[dict] = []
    for record in records:
        question = user_text(record["example"])
        if question in seen:
            continue
        seen.add(question)
        kept.append(record)
    return kept, len(records) - len(kept)


def user_text(example: dict) -> str:
    if "messages" in example:
        for message in example["messages"]:
            if message.get("role") == "user":
                return message.get("content", "")
        return ""
    return example.get("instruction", "")


def assistant_text(example: dict) -> str:
    if "messages" in example:
        for message in example["messages"]:
            if message.get("role") == "assistant":
                return message.get("content", "")
        return ""
    return example.get("output", "")


def dedupe_answers(records: list[dict], max_repeats: int) -> tuple[list[dict], int]:
    """
    Limit how often an identical answer may appear.

    Reusing one answer for a couple of differently phrased questions is useful
    augmentation; repeating it many times mostly teaches memorisation.
    """
    counts: Counter[str] = Counter()
    kept: list[dict] = []
    for record in records:
        answer = assistant_text(record["example"])
        if counts[answer] >= max_repeats:
            continue
        counts[answer] += 1
        kept.append(record)
    return kept, len(records) - len(kept)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    args = parse_args()

    if not args.input.exists():
        print(
            f"Input not found: {args.input}\n"
            "Run extract_content.py first.",
            file=sys.stderr,
        )
        return 1

    include_system = args.include_system and not args.no_system
    system_prompt = SYSTEM_PROMPT_PT if args.locale == "pt" else SYSTEM_PROMPT_EN
    rng = random.Random(args.seed)

    topics = load_topics(args.input)
    print(f"Loaded {len(topics)} topics from {args.input}")

    rejects: Counter[str] = Counter()
    all_records: list[dict] = []
    for topic in topics:
        all_records.extend(
            build_examples_for_topic(
                topic=topic,
                locale=args.locale,
                output_format=args.format,
                include_system=include_system,
                system_prompt=system_prompt,
                max_keywords=args.max_keywords,
                max_variants=args.max_variants,
                max_chars=args.max_chars,
                max_section_chunks=args.max_section_chunks,
                rng=rng,
                min_answer_chars=args.min_answer_chars,
                rejects=rejects,
            )
        )

    all_records, duplicate_questions = dedupe_questions(all_records)
    all_records, duplicate_answers = dedupe_answers(all_records, args.max_answer_repeats)
    train, val = split_train_val_by_topic(all_records, args.val_ratio, args.seed)
    val, cross_split_dupes = drop_cross_split_duplicates(train, val)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    train_path = args.output_dir / f"train_{args.format}_{args.locale}.jsonl"
    val_path = args.output_dir / f"val_{args.format}_{args.locale}.jsonl"

    write_jsonl(train_path, [r["example"] for r in train])
    write_jsonl(val_path, [r["example"] for r in val])

    # Mantém o mapeamento de tópicos para os passos seguintes redividirem sem vazar.
    meta_path = args.output_dir / f"meta_{args.format}_{args.locale}.json"
    meta_path.write_text(
        json.dumps(
            {
                "train_topics": sorted({r["topic_id"] for r in train}),
                "val_topics": sorted({r["topic_id"] for r in val}),
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    stats = {
        "topics": len(topics),
        "examples_total": len(all_records),
        "examples_train": len(train),
        "examples_val": len(val),
        "train_topics": len({r["topic_id"] for r in train}),
        "val_topics": len({r["topic_id"] for r in val}),
        "kinds_train": dict(Counter(r["kind"] for r in train)),
        "kinds_val": dict(Counter(r["kind"] for r in val)),
        "rejected": dict(rejects),
        "rejected_total": sum(rejects.values()),
        "duplicate_questions_dropped": duplicate_questions,
        "duplicate_answers_dropped": duplicate_answers,
        "cross_split_duplicates_dropped": cross_split_dupes,
        "format": args.format,
        "locale": args.locale,
        "val_ratio": args.val_ratio,
        "max_keywords": args.max_keywords,
        "max_variants": args.max_variants,
        "max_chars": args.max_chars,
        "min_answer_chars": args.min_answer_chars,
        "max_answer_repeats": args.max_answer_repeats,
        "max_section_chunks": args.max_section_chunks,
    }
    stats_path = args.output_dir / f"stats_{args.format}_{args.locale}.json"
    stats_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")

    print(f"Generated {len(all_records)} training examples")
    print(f"  rejected by quality filters: {sum(rejects.values())} {dict(rejects)}")
    print(f"  duplicate questions dropped: {duplicate_questions}")
    print(f"  duplicate answers dropped:   {duplicate_answers}")
    print(f"  val rows dropped as dupes:   {cross_split_dupes}")
    print(f"  train -> {train_path} ({len(train)} rows, {len({r['topic_id'] for r in train})} topics)")
    print(f"  val   -> {val_path} ({len(val)} rows, {len({r['topic_id'] for r in val})} topics)")
    print(f"  stats -> {stats_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
