#!/usr/bin/env python3
"""
Gera dataset SFT/QLoRA a partir de exemplos positivos (exemplo.pr2)
e negativos (ExemplosNegativos.pr2), no mesmo formato messages de
data/training/train_messages_pt.jsonl.

Usage:
    python scripts/build_code_training_dataset.py
"""

from __future__ import annotations

import argparse
import json
import random
import re
from collections import defaultdict
from pathlib import Path

SYSTEM_PROMPT_PT = (
    "Você é um assistente especializado em Microsoft Visual FoxPro 9. "
    "Responda com precisão técnica sobre comandos, funções, classes, "
    "propriedades, métodos e mensagens de erro."
)

FUNC_RE = re.compile(r"^(\s*)(FUNCTION|PROCEDURE)\s+(\S+)", re.I)
END_RE = re.compile(r"^(\s*)(ENDFUNC|ENDPROC)\s*$", re.I)
# Comentários de erro: "**texto" — não confundir com cabeçalhos "****".
ERROR_RE = re.compile(r"^\*\*([^*].+)$")
STAR_RE = re.compile(r"^\*+$")


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Build VFP9 code correct/incorrect SFT dataset."
    )
    parser.add_argument(
        "--positive",
        type=Path,
        default=root / "ExemplosCodigo" / "exemplo.pr2",
    )
    parser.add_argument(
        "--negative",
        type=Path,
        default=root / "ExemplosCodigo" / "ExemplosNegativos.pr2",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=root / "data" / "training",
    )
    parser.add_argument("--val-ratio", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--max-variants",
        type=int,
        default=1,
        help="Quantas variantes de pergunta por tipo de exemplo (1=igual ao dataset principal).",
    )
    return parser.parse_args()


def find_star_header(lines: list[str], i: int) -> int:
    if i > 0 and STAR_RE.fullmatch(lines[i - 1].strip()):
        return i - 1
    return i


def extract_functions(text: str) -> list[dict]:
    lines = text.splitlines()
    blocks: list[dict] = []
    i = 0
    n = len(lines)
    while i < n:
        m = FUNC_RE.match(lines[i])
        if not m:
            i += 1
            continue
        indent, kind, name = m.group(1), m.group(2).upper(), m.group(3)
        start = find_star_header(lines, i)
        j = i + 1
        found = False
        while j < n:
            m2 = END_RE.match(lines[j])
            if m2 and len(m2.group(1)) == len(indent):
                code = "\n".join(lines[start : j + 1]).strip()
                blocks.append(
                    {
                        "kind": kind,
                        "name": name,
                        "code": code,
                    }
                )
                i = j + 1
                found = True
                break
            j += 1
        if not found:
            i += 1
    return blocks


def extract_negatives(text: str) -> list[dict]:
    """Parse ExemplosNegativos: **erro + bloco FUNCTION/PROCEDURE."""
    lines = text.splitlines()
    items: list[dict] = []
    i = 0
    n = len(lines)
    while i < n:
        m = ERROR_RE.match(lines[i])
        if not m:
            i += 1
            continue
        error = m.group(1).strip()
        if not error or error.startswith("Exemplos"):
            i += 1
            continue
        # pula linhas em branco e espera o bloco da função
        j = i + 1
        while j < n and not lines[j].strip():
            j += 1
        # pula cabeçalho de asteriscos / acha FUNCTION
        while j < n and (STAR_RE.fullmatch(lines[j].strip()) or not lines[j].strip()):
            j += 1
        if j >= n:
            break
        # aceita cabeçalhos FUNCTION/PROCEDURE grafados errado nos negativos
        header = re.match(
            r"^(\s*)(FUNCTION|PROCEDURE|FUNCION|PROCEDUERE)\s+(\S+)",
            lines[j],
            re.I,
        )
        if not header:
            i += 1
            continue
        indent = header.group(1)
        raw_kind = header.group(2).upper()
        name = header.group(3)
        kind = (
            "FUNCTION"
            if raw_kind.startswith("FUNC")
            else "PROCEDURE"
        )
        start = find_star_header(lines, j)
        k = j + 1
        end = None
        while k < n:
            # para no próximo comentário de erro
            if ERROR_RE.match(lines[k]):
                end = k - 1
                break
            m_end = re.match(
                r"^(\s*)(ENDFUNC|ENDPROC|END\s+FUN\s+C|END\s+PRO\s+C)\s*$",
                lines[k],
                re.I,
            )
            if m_end and len(m_end.group(1)) == len(indent):
                end = k
                k += 1
                break
            # casos sem ENDFUNC: para antes do próximo cabeçalho de asteriscos + função
            if (
                STAR_RE.fullmatch(lines[k].strip())
                and k + 1 < n
                and re.match(
                    r"^\s*(FUNCTION|PROCEDURE|FUNCION|PROCEDUERE)\s+",
                    lines[k + 1],
                    re.I,
                )
            ):
                end = k - 1
                break
            k += 1
        if end is None:
            end = n - 1
        while end > start and not lines[end].strip():
            end -= 1
        code = "\n".join(lines[start : end + 1]).strip()
        if code:
            items.append(
                {
                    "error": error,
                    "kind": kind,
                    "name": name,
                    "code": code,
                }
            )
        i = max(k, i + 1)
    return items


def fox_block(code: str) -> str:
    return f"```foxpro\n{code.strip()}\n```"


def format_example(user: str, assistant: str, system_prompt: str) -> dict:
    return {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ]
    }


def pick(templates: list[str], max_variants: int, rng: random.Random) -> list[str]:
    if max_variants <= 0:
        return []
    if max_variants >= len(templates):
        return templates
    return rng.sample(templates, max_variants)


def classify_error(error: str) -> str:
    e = error.lower()
    if "estilo" in e:
        return "estilo"
    if "lógica" in e or "logica" in e:
        return "lógica"
    return "sintaxe"


def build_examples(
    positives: list[dict],
    negatives: list[dict],
    system_prompt: str,
    max_variants: int,
    rng: random.Random,
) -> list[dict]:
    by_name: dict[str, list[dict]] = defaultdict(list)
    for p in positives:
        by_name[p["name"]].append(p)

    # Prefere a primeira definição positiva quando os nomes se repetem.
    positive_map = {name: items[0] for name, items in by_name.items()}

    examples: list[dict] = []
    seen: set[str] = set()

    def add(user: str, assistant: str) -> None:
        u = user.strip()
        a = assistant.strip()
        if not u or not a or u in seen:
            return
        seen.add(u)
        examples.append(format_example(u, a, system_prompt))

    # --- Positivos ---
    q_positive_ok = [
        "Este código Visual FoxPro 9 está correto?\n\n{code}",
        "Avalie se o trecho abaixo segue boas práticas de VFP 9:\n\n{code}",
        "O código a seguir é um exemplo válido em Visual FoxPro 9?\n\n{code}",
    ]
    q_positive_explain = [
        "Explique o que faz este código Visual FoxPro 9:\n\n{code}",
        "Descreva a função/procedimento abaixo (VFP 9):\n\n{code}",
    ]
    q_positive_show = [
        "Mostre um exemplo correto em Visual FoxPro 9 da {kind} {name}.",
        "Escreva a {kind} {name} em Visual FoxPro 9 com estilo idiomático correto.",
        "Como implementar {name} corretamente no VFP 9?",
    ]

    for pos in positives:
        code = fox_block(pos["code"])
        kind_pt = "função" if pos["kind"] == "FUNCTION" else "procedimento"

        for tmpl in pick(q_positive_ok, max_variants, rng):
            add(
                tmpl.format(code=code),
                (
                    f"Sim. Este é um exemplo correto de {kind_pt} `{pos['name']}` "
                    f"em Microsoft Visual FoxPro 9.\n\n"
                    f"Pontos corretos:\n"
                    f"- Cabeçalho `{pos['kind']}` / "
                    f"{'ENDFUNC' if pos['kind'] == 'FUNCTION' else 'ENDPROC'} consistente\n"
                    f"- Uso adequado de `PARAMETERS` e `PRIVATE` quando necessário\n"
                    f"- Indentação e, quando houver SQL/comandos longos, continuação com `;`\n"
                    f"- Lógica e funções nativas aplicadas de forma idiomática\n\n"
                    f"Código de referência:\n{code}"
                ),
            )

        for tmpl in pick(q_positive_explain, max_variants, rng):
            add(
                tmpl.format(code=code),
                (
                    f"A {kind_pt} `{pos['name']}` é um exemplo correto em Visual FoxPro 9.\n\n"
                    f"Ela declara parâmetros/variáveis privadas conforme o padrão do projeto e "
                    f"executa a lógica principal com comandos e funções nativas do VFP 9, "
                    f"encerrando com "
                    f"{'ENDFUNC' if pos['kind'] == 'FUNCTION' else 'ENDPROC'}.\n\n"
                    f"{code}"
                ),
            )

        art = "da" if kind_pt == "função" else "do"
        for tmpl in pick(q_positive_show, max_variants, rng):
            add(
                tmpl.format(kind=kind_pt, name=pos["name"]),
                (
                    f"Exemplo correto {art} {kind_pt} `{pos['name']}` em Visual FoxPro 9:\n\n"
                    f"{code}"
                ),
            )

    # --- Negativos e correção ---
    q_negative_find = [
        "O que há de errado neste código Visual FoxPro 9?\n\n{code}",
        "Identifique o problema neste trecho de VFP 9:\n\n{code}",
        "Analise o código abaixo e explique o erro:\n\n{code}",
    ]
    q_negative_ok = [
        "Este código Visual FoxPro 9 está correto?\n\n{code}",
        "O trecho a seguir é válido em VFP 9?\n\n{code}",
    ]
    q_negative_fix = [
        "Corrija este código Visual FoxPro 9:\n\n{code}",
        "Reescreva o trecho abaixo de forma correta em VFP 9:\n\n{code}",
        "Há um erro neste código. Forneça a versão correta:\n\n{code}",
    ]
    q_contrast = [
        (
            "Qual das versões abaixo está correta em Visual FoxPro 9?\n\n"
            "Versão A:\n{bad}\n\nVersão B:\n{good}"
        ),
        (
            "Compare os trechos e diga qual segue o padrão correto de VFP 9.\n\n"
            "Trecho 1:\n{bad}\n\nTrecho 2:\n{good}"
        ),
    ]

    for neg in negatives:
        bad = fox_block(neg["code"])
        err = neg["error"]
        err_type = classify_error(err)
        pos = positive_map.get(neg["name"])
        kind_pt = "função" if neg["kind"] == "FUNCTION" else "procedimento"

        for tmpl in pick(q_negative_find, max_variants, rng):
            # Inclui nome+erro na unicidade da pergunta com variação só no assistente;
            # torna o user único acrescentando um marcador curto quando duplicar.
            user = tmpl.format(code=bad)
            if user in seen:
                user = (
                    f"{tmpl.format(code=bad)}\n\n"
                    f"(Foque em: {neg['name']})"
                )
            add(
                user,
                (
                    f"Há um erro de {err_type} neste código "
                    f"{'da' if kind_pt == 'função' else 'do'} {kind_pt} `{neg['name']}`.\n\n"
                    f"**Problema:** {err}.\n\n"
                    f"Em Visual FoxPro 9, esse padrão deve ser evitado porque compromete "
                    f"{'a compilação/sintaxe' if err_type == 'sintaxe' else 'o resultado esperado' if err_type == 'lógica' else 'a legibilidade e o padrão do projeto'}."
                    + (
                        f"\n\nVersão correta:\n{fox_block(pos['code'])}"
                        if pos
                        else ""
                    )
                ),
            )

        for tmpl in pick(q_negative_ok, max_variants, rng):
            user = tmpl.format(code=bad)
            if user in seen:
                user = f"{user}\n\nConsidere especialmente a {kind_pt} `{neg['name']}`."
            add(
                user,
                (
                    f"Não. O código está incorreto.\n\n"
                    f"**Tipo de erro:** {err_type}.\n"
                    f"**Detalhe:** {err}.\n\n"
                    f"{'A' if kind_pt == 'função' else 'O'} {kind_pt} `{neg['name']}` "
                    f"precisa seguir o padrão idiomático do VFP 9"
                    + (
                        f". Versão correta:\n\n{fox_block(pos['code'])}"
                        if pos
                        else "."
                    )
                ),
            )

        if pos:
            good = fox_block(pos["code"])
            art = "da" if kind_pt == "função" else "do"
            for tmpl in pick(q_negative_fix, max_variants, rng):
                user = tmpl.format(code=bad)
                if user in seen:
                    user = f"{user}\n\nNome esperado: `{neg['name']}`."
                add(
                    user,
                    (
                        f"O trecho apresentado contém erro de {err_type}: {err}.\n\n"
                        f"Versão corrigida {art} {kind_pt} `{neg['name']}`:\n\n{good}"
                    ),
                )

            for tmpl in pick(q_contrast, max_variants, rng):
                # Randomiza a ordem A/B para o modelo não escolher sempre B.
                if rng.random() < 0.5:
                    user = tmpl.format(bad=bad, good=good)
                    assistant = (
                        f"A versão correta é a **Versão B** / **Trecho 2**.\n\n"
                        f"A outra versão tem erro de {err_type}: {err}.\n\n"
                        f"Código correto:\n{good}"
                    )
                else:
                    # troca os rótulos no template à mão
                    user = tmpl.format(bad=good, good=bad)
                    # Depois da troca, "Versão A" é a boa e "Versão B" é a ruim
                    assistant = (
                        f"A versão correta é a **Versão A** / **Trecho 1**.\n\n"
                        f"A outra versão tem erro de {err_type}: {err}.\n\n"
                        f"Código correto:\n{good}"
                    )
                if user in seen:
                    user = f"{user}\n\nFunção analisada: `{neg['name']}`."
                add(user, assistant)

    return examples


def split_train_val(
    examples: list[dict], val_ratio: float, seed: int
) -> tuple[list[dict], list[dict]]:
    rng = random.Random(seed)
    shuffled = examples[:]
    rng.shuffle(shuffled)
    val_count = max(1, int(len(shuffled) * val_ratio)) if shuffled else 0
    return shuffled[val_count:], shuffled[:val_count]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    args = parse_args()
    if not args.positive.exists():
        raise SystemExit(f"Arquivo positivo não encontrado: {args.positive}")
    if not args.negative.exists():
        raise SystemExit(f"Arquivo negativo não encontrado: {args.negative}")

    rng = random.Random(args.seed)
    positives = extract_functions(args.positive.read_text(encoding="utf-8"))
    negatives = extract_negatives(args.negative.read_text(encoding="utf-8"))

    examples = build_examples(
        positives=positives,
        negatives=negatives,
        system_prompt=SYSTEM_PROMPT_PT,
        max_variants=args.max_variants,
        rng=rng,
    )
    train, val = split_train_val(examples, args.val_ratio, args.seed)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    train_path = args.output_dir / "train_messages_code_pt.jsonl"
    val_path = args.output_dir / "val_messages_code_pt.jsonl"
    stats_path = args.output_dir / "stats_messages_code_pt.json"

    write_jsonl(train_path, train)
    write_jsonl(val_path, val)

    stats = {
        "source_positive": str(args.positive),
        "source_negative": str(args.negative),
        "functions_positive": len(positives),
        "examples_negative_source": len(negatives),
        "examples_total": len(examples),
        "examples_train": len(train),
        "examples_val": len(val),
        "format": "messages",
        "locale": "pt",
        "val_ratio": args.val_ratio,
        "max_variants": args.max_variants,
        "seed": args.seed,
        "kinds": [
            "codigo_correto",
            "explicacao_positiva",
            "gerar_codigo_correto",
            "detectar_erro",
            "avaliar_incorreto",
            "corrigir_codigo",
            "comparar_versoes",
        ],
    }
    stats_path.write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Positivos: {len(positives)} | Negativos fonte: {len(negatives)}")
    print(f"Exemplos gerados: {len(examples)}")
    print(f"  train -> {train_path} ({len(train)})")
    print(f"  val   -> {val_path} ({len(val)})")
    print(f"  stats -> {stats_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
