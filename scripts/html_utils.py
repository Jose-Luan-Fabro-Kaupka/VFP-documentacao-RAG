"""Auxiliares compartilhados para analisar tópicos do HTML Help do VFP 9."""

from __future__ import annotations

import html
import re
from collections import defaultdict
from pathlib import Path

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

COPY_CODE_RE = re.compile(r"^Copy Code$", re.I)
WHITESPACE_RE = re.compile(r"[ \t]+\n")
MULTI_NEWLINE_RE = re.compile(r"\n{3,}")
HTML_LINK_RE = re.compile(r"/html/([0-9a-f-]+)\.htm", re.I)
# Remove resto de HTML de chrome, mas preserva includes C como <pro_ext.h>
LEFTOVER_HTML_RE = re.compile(
    r"</?(?:span|a|div|p|br|b|i|em|strong|font|img|table|tr|td|th|ul|ol|li|dl|dt|dd)"
    r"(?:\s[^>]*)?>",
    re.I,
)
COPY_CODE_TABLE_ROW_RE = re.compile(
    r"^\|\s*(?:\|\s*)?Copy Code\s*\|\s*$",
    re.I,
)
COPY_CODE_SEPARATOR_RE = re.compile(r"^\|\s*(?:---\s*\|\s*)+$")
VFPX_NOTE_RE = re.compile(
    r"VFPX FPW2\.6 begin\s*"
    r"(?:This (?:command|function|property|event|method|class|topic)[^.]*\.\s*)?"
    r"(?:but the following documentation was found[^.]*\.\s*)?",
    re.I,
)
VFPX_END_RE = re.compile(r"\s*VFPX FPW2\.6 end\s*", re.I)
FOOTER_NOISE_RE = re.compile(
    r"(?:Microsoft Visual FoxPro 9 SP2 Help file,? VFPX Edition[^\n]*\n?)?"
    r"(?:Send feedback[^\n]*\n?)?"
    r"(?:2009-2017 Placed under Creative Commons[^\n]*\n?)?"
    r"(?:Not all help features are available[^\n]*)?",
    re.I,
)
NOTE_TABLE_RE = re.compile(
    r"\|[ \t]*(Note|Tip|Important|Caution|Warning)[ \t]*\|\s*\n"
    r"\|[ \t]*---[ \t]*\|(?:\s*\n\|[ \t]*---[ \t]*\|)*\s*\n"
    r"\|[ \t]*(.+?)[ \t]*\|",
    re.I | re.S,
)
SEE_ALSO_SECTION_RE = re.compile(r"(?ms)^# See Also\s*\n(.*)\Z")
HEADING_RE = re.compile(r"(?m)^(#{1,4})\s+(.+?)\s*$")
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)
# Uma regra genérica `\.([A-Z])` corromperia a sintaxe FoxPro: literais lógicos
# (.T., .F., .NULL.), acesso a membro (This.Caption) e extensões (MYAPP.APP).
# No corpus da ajuda só uns poucos pontos realmente carecem de espaço, então o
# conserto vale só para ponto seguido de um iniciador completo de frase em inglês.
SENTENCE_STARTER_WORDS = (
    "The|This|These|Those|You|Your|If|When|While|However|Otherwise|Because|"
    "Visual|There|They|Note"
)
MISSING_SPACE_AFTER_PERIOD_RE = re.compile(
    rf"(?<![.\s])(?<=[a-z][a-z])\.({SENTENCE_STARTER_WORDS})(?![A-Za-z0-9_])"
)
UI_NOISE_LINES = {
    "copy code",
    "see also",
    "collapse all",
    "expand all",
    "collapse",
    "expand",
}
CALLOUT_LABELS = {"note", "tip", "important", "caution", "warning"}
FOOTER_MARKERS = (
    "send feedback",
    "vfpx edition",
    "creative commons licensing",
    "not all help features are available",
    "vfpx help file project team",
)


def project_paths(script_file: str | Path) -> dict[str, Path]:
    root = Path(script_file).resolve().parent.parent
    return {
        "root": root,
        "html_dir": root / "sources/dv_foxhelp/html",
        "hhc": root / "sources/dv_foxhelp/dv_foxhelp91.hhc",
        "hhk": root / "sources/dv_foxhelp/dv_foxhelp91K-2.hhk",
        "data_dir": root / "data",
    }


def parse_hhc_categories(hhc_path: Path) -> dict[str, str]:
    """Mapeia nome do arquivo do tópico -> categoria (breadcrumb) do sumário."""
    if not hhc_path.exists():
        return {}

    soup = BeautifulSoup(hhc_path.read_text(encoding="utf-8", errors="replace"), "html.parser")
    categories: dict[str, str] = {}

    def walk_ul(ul: Tag, path: list[str]) -> None:
        for li in ul.find_all("li", recursive=False):
            obj = li.find("object")
            name = None
            local = None
            if obj:
                name_param = obj.find("param", attrs={"name": "Name"})
                local_param = obj.find("param", attrs={"name": "Local"})
                if name_param and name_param.get("value"):
                    name = name_param["value"].strip()
                if local_param and local_param.get("value"):
                    local = local_param["value"].strip()

            current_path = [*path, name] if name else path
            if local:
                categories[Path(local).name.lower()] = " > ".join(current_path)

            for nested in li.find_all("ul", recursive=False):
                walk_ul(nested, current_path)

    top_ul = soup.find("ul")
    if top_ul:
        walk_ul(top_ul, [])
    return categories


def parse_hhk_keywords(hhk_path: Path) -> dict[str, list[str]]:
    """Mapeia nome do arquivo do tópico -> palavras-chave do índice."""
    if not hhk_path.exists():
        return {}

    soup = BeautifulSoup(hhk_path.read_text(encoding="utf-8", errors="replace"), "html.parser")
    keywords: dict[str, list[str]] = defaultdict(list)

    for obj in soup.find_all("object"):
        kw_param = obj.find("param", attrs={"name": "Keyword"})
        local_param = obj.find("param", attrs={"name": "Local"})
        if not kw_param or not local_param:
            continue
        keyword = (kw_param.get("value") or "").strip()
        local = (local_param.get("value") or "").strip()
        if keyword and local:
            keywords[Path(local).name.lower()].append(keyword)

    return dict(keywords)


def extract_alink_keywords(soup: BeautifulSoup) -> list[str]:
    keywords: list[str] = []
    for obj in soup.find_all("object", attrs={"type": "application/x-oleobject"}):
        for param in obj.find_all("param"):
            if param.get("name", "").lower() == "alink name":
                value = (param.get("value") or "").strip()
                if value and not value.startswith("vfp."):
                    keywords.append(value)
    return keywords


def extract_title(soup: BeautifulSoup) -> str:
    nsr = soup.find("span", id="nsrTitle")
    if nsr:
        text = nsr.get_text(" ", strip=True)
        if text:
            return text
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return ""


def _looks_like_footer_text(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in FOOTER_MARKERS)


def prepare_body(body: Tag) -> None:
    """Remove chrome de UI e envelopes editoriais antes da conversão para Markdown."""
    for tag in body.find_all(["script", "style", "img", "input", "label", "noscript"]):
        tag.decompose()

    for comment in body.find_all(string=lambda value: isinstance(value, Comment)):
        comment.extract()

    for tag in body.find_all(class_="copyCode"):
        tag.decompose()

    for tag in body.find_all(class_="copyCodeImage"):
        tag.decompose()

    # Notas editoriais VFPX; mantém a documentação restaurada do FoxPro 2.6.
    for tag in body.find_all("p", class_="vfpx"):
        tag.decompose()

    for tag in body.find_all(id="allHistory"):
        tag.decompose()

    # Rodapés residuais VFPX / Creative Commons às vezes vazam para o mainBody.
    for tag in list(body.find_all(["div", "p", "font"])):
        text = tag.get_text(" ", strip=True)
        if text and _looks_like_footer_text(text):
            tag.decompose()


def _clean_inline_text(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = LEFTOVER_HTML_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()


def _pre_to_fenced(pre: Tag) -> str:
    # Separador vazio para que <span class="parameter"> inline não insira quebras de linha.
    code = pre.get_text("", strip=False)
    code = html.unescape(code)
    code = code.replace("\xa0", " ")
    code = code.replace("\r\n", "\n").replace("\r", "\n")
    code = "\n".join(line.rstrip() for line in code.split("\n")).strip("\n")
    code = LEFTOVER_HTML_RE.sub("", code)
    # A ajuda escreve referências chamáveis como "EOF( )"; emite "EOF()" idiomático no código.
    code = re.sub(r"\(\s+\)", "()", code)
    return f"\n```foxpro\n{code}\n```\n"


def _is_code_table(table: Tag) -> bool:
    if table.find("span", class_="copyCode"):
        return True
    if table.find("pre") and table.find_parent("div", class_="code"):
        return True
    return False


def _is_callout_table(rows: list[list[str]]) -> bool:
    if not rows:
        return False
    header = [cell.strip().lower() for cell in rows[0] if cell.strip()]
    return len(header) == 1 and header[0] in CALLOUT_LABELS


def _callout_to_markdown(rows: list[list[str]]) -> str:
    label = rows[0][0].strip().title()
    body_cells: list[str] = []
    for row in rows[1:]:
        for cell in row:
            cell = cell.strip()
            if cell:
                body_cells.append(cell)
    body = " ".join(body_cells).strip()
    if not body:
        return f"> **{label}**"
    return f"> **{label}:** {body}"


def _code_table_to_markdown(table: Tag) -> str:
    pre = table.find("pre")
    if pre:
        return _pre_to_fenced(pre)
    text = _clean_inline_text(table.get_text("\n", strip=True))
    text = COPY_CODE_RE.sub("", text).strip()
    if not text:
        return ""
    return f"\n```foxpro\n{text}\n```\n"


def _table_to_markdown(table: Tag) -> str:
    if _is_code_table(table):
        return _code_table_to_markdown(table)

    rows: list[list[str]] = []
    for tr in table.find_all("tr", recursive=False):
        cells = tr.find_all(["th", "td"], recursive=False)
        if not cells:
            cells = tr.find_all(["th", "td"], recursive=True)
            if not cells:
                continue
        row = [_clean_inline_text(cell.get_text(" ", strip=True)) for cell in cells]
        row = [cell for cell in row if cell and not COPY_CODE_RE.match(cell)]
        if any(row):
            rows.append(row)
    if not rows:
        return ""

    if _is_callout_table(rows):
        return _callout_to_markdown(rows)

    width = max(len(r) for r in rows)
    normalized = [r + [""] * (width - len(r)) for r in rows]
    header = normalized[0]
    body = normalized[1:] if len(normalized) > 1 else []

    if all(not cell for cell in header):
        return ""

    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in body:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def _render_children(node: Tag, link_titles: dict[str, str]) -> str:
    parts: list[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            text = str(child)
            if text.strip():
                parts.append(text)
            elif text:
                # Espaço em volta de tags inline é o separador de palavras; removê-lo
                # cola os vizinhos. A ajuda escreve tanto "<b>Page</b>
                # <b>Themes</b>" quanto "<b>Memo</b><b> </b>or", então o espaço pode
                # ser um irmão ou o conteúdo inteiro de uma tag. Chamadores de bloco
                # limpam depois.
                parts.append(" ")
        elif isinstance(child, Tag):
            parts.append(element_to_markdown(child, link_titles))
    return "".join(parts)


def element_to_markdown(node: Tag | NavigableString, link_titles: dict[str, str]) -> str:
    if isinstance(node, NavigableString):
        return str(node)

    name = node.name.lower()

    if name in {"script", "style", "img", "input", "label", "noscript"}:
        return ""

    if name == "pre":
        return _pre_to_fenced(node)

    if name == "code":
        text = _clean_inline_text(node.get_text(" ", strip=True))
        return f"`{text}`" if text else ""

    if name == "a":
        href = node.get("href", "")
        text = _clean_inline_text(node.get_text(" ", strip=True))
        match = HTML_LINK_RE.search(href)
        if match:
            linked_title = link_titles.get(f"{match.group(1).lower()}.htm")
            if linked_title:
                return linked_title
        return text

    if name in {"h1", "h2", "h3", "h4"}:
        level = int(name[1])
        text = _clean_inline_text(node.get_text(" ", strip=True))
        text = re.sub(r"^(Expand|Collapse)\s+", "", text, flags=re.I)
        return f"\n{'#' * level} {text}\n" if text else ""

    if name == "table":
        rendered = _table_to_markdown(node)
        return f"\n{rendered}\n" if rendered else ""

    if name == "dl":
        blocks: list[str] = []
        for dt in node.find_all("dt", recursive=False):
            term = _clean_inline_text(dt.get_text(" ", strip=True))
            dd = dt.find_next_sibling("dd")
            desc = _clean_inline_text(dd.get_text("\n", strip=True)) if dd else ""
            if term:
                blocks.append(f"**{term}**\n{desc}".strip())
        return "\n\n".join(blocks) + ("\n" if blocks else "")

    if name == "p":
        text = _render_children(node, link_titles).strip()
        return f"\n{text}\n" if text else ""

    if name in {"div", "span", "font", "dd", "dt", "li", "td", "th", "tr", "description"}:
        return _render_children(node, link_titles)

    if name in {"ul", "ol"}:
        items: list[str] = []
        for li in node.find_all("li", recursive=False):
            item = _clean_inline_text(li.get_text("\n", strip=True))
            if item:
                items.append(f"- {item}")
        return "\n".join(items) + ("\n" if items else "")

    if name == "br":
        return "\n"

    return _render_children(node, link_titles)


def _compact_see_also(section_body: str, max_links: int = 5) -> str:
    links: list[str] = []
    for line in section_body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("####") or stripped.startswith("###"):
            continue
        # Prefere linhas de lista/link a títulos vazios.
        candidate = stripped.lstrip("- ").strip()
        if not candidate or candidate.lower() in {"reference", "other resources"}:
            continue
        if candidate not in links:
            links.append(candidate)
        if len(links) >= max_links:
            break
    if not links:
        return ""
    return "# See Also\n" + "\n".join(f"- {item}" for item in links)


def _apply_outside_code(text: str, transform) -> str:
    """Aplica uma transformação só na prosa, deixando blocos de código intactos."""
    out: list[str] = []
    last = 0
    for match in CODE_FENCE_RE.finditer(text):
        out.append(transform(text[last : match.start()]))
        out.append(match.group(0))
        last = match.end()
    out.append(transform(text[last:]))
    return "".join(out)


BOLD_LABEL_RE = re.compile(r"(?m)^\*\*([A-Za-z_][A-Za-z0-9_]*(?: [A-Za-z0-9_]+)+)\*\*[ \t]*$")
# Parâmetros com prefixo húngaro partidos no meio do token, ex.: "l Value".
SPLIT_PARAM_RE = re.compile(r"\b([nclotefax]) ([A-Z][A-Za-z0-9]+)\b")
# Parâmetros vizinhos colados, ex.: "MenuBarName1lExpression1".
GLUED_PARAM_RE = re.compile(r"([A-Za-z][A-Za-z0-9]*[0-9a-z])([nclotefax][A-Z][A-Za-z0-9]*)")


def _rejoin_split_identifiers(text: str) -> str:
    """
    Repara identificadores partidos por marcação inline, ex.: `**nSort Order**` ou "l Value".

    Termos de definição são lidos com espaço no meio, o que é certo para rótulos
    reais ("Field Name") mas quebra identificadores envelopados em vários spans.
    Só rejunta quando a forma sem espaço ocorre em outro lugar no mesmo tópico,
    o que preserva rótulos genuínos de várias palavras.
    """

    def rejoin(candidate: str, rebuild) -> str:
        joined = candidate.replace(" ", "")
        if re.search(rf"\b{re.escape(joined)}\b", text):
            return rebuild(joined)
        return rebuild(candidate)

    def fix_label(match: re.Match[str]) -> str:
        label = match.group(1)
        joined = label.replace(" ", "")
        if re.search(rf"\b{re.escape(joined)}\b", text):
            return f"**{joined}**"
        # Dano inverso: parâmetros vizinhos colados num único token.
        split = GLUED_PARAM_RE.sub(r"\1 \2", label)
        if split != label and re.search(rf"\b{re.escape(split)}\b", text):
            return f"**{split}**"
        return match.group(0)

    text = BOLD_LABEL_RE.sub(fix_label, text)
    return _apply_outside_code(
        text,
        lambda part: SPLIT_PARAM_RE.sub(
            lambda m: rejoin(f"{m.group(1)} {m.group(2)}", lambda v: v), part
        ),
    )


def _rewrite_note_tables(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1).strip().title()
        body = re.sub(r"\s+", " ", match.group(2)).strip()
        return f"> **{label}:** {body}"

    return NOTE_TABLE_RE.sub(repl, text)


def body_to_markdown(body: Tag, link_titles: dict[str, str]) -> str:
    prepare_body(body)
    raw = element_to_markdown(body, link_titles)
    raw = WHITESPACE_RE.sub("\n", raw)
    raw = MULTI_NEWLINE_RE.sub("\n\n", raw)

    cleaned_lines: list[str] = []
    previous_blank = False
    for line in raw.splitlines():
        stripped = line.strip()
        if stripped.lower() in UI_NOISE_LINES or COPY_CODE_RE.match(stripped):
            continue
        if COPY_CODE_TABLE_ROW_RE.match(stripped):
            continue
        if COPY_CODE_SEPARATOR_RE.match(stripped) and (
            not cleaned_lines or not cleaned_lines[-1].startswith("| ")
        ):
            continue
        if _looks_like_footer_text(stripped):
            continue
        if not stripped:
            if previous_blank:
                continue
            cleaned_lines.append("")
            previous_blank = True
            continue
        cleaned_lines.append(line.rstrip())
        previous_blank = False

    return "\n".join(cleaned_lines).strip()


def build_title_index(html_dir: Path) -> dict[str, str]:
    """Mapeia 'uuid.htm' -> título do tópico para resolver links internos."""
    titles: dict[str, str] = {}
    for path in html_dir.glob("*.htm"):
        soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="replace"), "html.parser")
        title = extract_title(soup)
        if title:
            titles[path.name.lower()] = title
    return titles


def useful_body_text(content: str) -> str:
    """Conteúdo sem a seção final See Also."""
    return SEE_ALSO_SECTION_RE.sub("", content).strip()


def is_low_value_topic(content: str, min_useful_chars: int = 80) -> bool:
    """Verdadeiro para tópicos só de navegação / pesados de See Also."""
    useful = useful_body_text(content)
    if len(useful) < min_useful_chars:
        return True
    # Quase só uma lista de links, com quase nenhuma prosa.
    linkish = sum(1 for line in useful.splitlines() if line.strip().startswith("- "))
    prose_chars = len(re.sub(r"(?m)^-\s+.*$", "", useful))
    return linkish >= 8 and prose_chars < min_useful_chars


def split_into_sections(content: str) -> list[tuple[str, str]]:
    """
    Parte o Markdown em pedaços (título, corpo).
    A introdução (antes do primeiro título) usa heading ''.
    """
    matches = list(HEADING_RE.finditer(content))
    if not matches:
        text = content.strip()
        return [("", text)] if text else []

    sections: list[tuple[str, str]] = []
    intro = content[: matches[0].start()].strip()
    if intro:
        sections.append(("", intro))

    for index, match in enumerate(matches):
        heading = match.group(2).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)
        body = content[start:end].strip()
        if heading.lower() == "see also":
            # Mantém um See Also compacto só no exemplo do tópico inteiro, não como pedaço.
            continue
        if body:
            sections.append((heading, body))
    return sections


def normalize_content(text: str, max_see_also_links: int = 5) -> str:
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = LEFTOVER_HTML_RE.sub("", text)
    text = VFPX_NOTE_RE.sub("", text)
    text = VFPX_END_RE.sub("\n", text)
    text = FOOTER_NOISE_RE.sub("", text)
    text = re.sub(r"(?im)^\s*Copy Code\s*$", "", text)
    text = re.sub(r"(?im)^\|\s*(?:\|\s*)?Copy Code\s*\|\s*$", "", text)
    text = _rewrite_note_tables(text)

    see_also_match = SEE_ALSO_SECTION_RE.search(text)
    if see_also_match:
        compact = _compact_see_also(see_also_match.group(1), max_links=max_see_also_links)
        text = text[: see_also_match.start()].rstrip()
        if compact:
            text = f"{text}\n\n{compact}"

    # Alguns tópicos de origem trazem literais malformados como "Default:. F." — rejunta.
    text = re.sub(r"\.\s+(T|F|NULL)\s*\.", r".\1.", text)
    text = _apply_outside_code(text, lambda part: MISSING_SPACE_AFTER_PERIOD_RE.sub(r". \1", part))
    text = _apply_outside_code(text, lambda part: re.sub(r"[ \t]{2,}", " ", part))
    text = MULTI_NEWLINE_RE.sub("\n\n", text.strip())
    return _rejoin_split_identifiers(text)
