"""Nomes Markdown legíveis que ainda carregam o GUID do tópico.

Os arquivos ficam como ``funcao-floor--fdb6195d-9b4d-4b3f-a410-48df0f146fa3.md``.
O GUID continua sendo o id estável usado pelo HTML, pelo topics.jsonl e pelo índice RAG.

Alguns arquivos PT foram gravados com o UUID de *outro* tópico. O casamento
portanto prefere identidade de título/assinatura ao UUID do nome do arquivo,
e só cai no UUID quando isso não contradiz essa identidade.
"""

from __future__ import annotations

import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

TOPIC_ID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
    re.I,
)
HEADING_RE = re.compile(r"^#\s+(.+)$")
CODE_BLOCK_RE = re.compile(r"```foxpro\n(.*?)```", re.S)
ERROR_RE = re.compile(r"\((?:error|erro)\s+(\d+)\)", re.I)
SYS_RE = re.compile(r"\bSYS\(\s*(\d+)\s*\)", re.I)
EXT_RE = re.compile(r"\.[a-z]{2,4}\b", re.I)
PME_EN_RE = re.compile(
    r"^(.+?)\s+properties,\s*methods,\s*and\s*events\s*$", re.I
)
PME_PT_RE = re.compile(
    r"^propriedades,\s*m[eé]todos\s+e\s+eventos\s+d[oea]s?\s+(.+)$", re.I
)
KIND_PREFIX_RE = re.compile(
    r"^(?:"
    r"fun[cç][aã]o|comando|propriedades?|m[eé]todos?|eventos?|"
    r"vari[aá]vel(?: de| do)? sistema|"
    r"rotina(?: da| de)? biblioteca(?: da| de)? api|"
    r"classe(?: de funda[cç][aã]o| base| b[aá]sica| foundation)?|"
    r"controle|objeto|"
    r"how to|como"
    r")\s*[:.]?\s+",
    re.I,
)
KIND_SUFFIX_RE = re.compile(
    r"\s+(?:"
    r"functions?|commands?|properties|property|methods?|events?|"
    r"system variable|api library routine|foundation class|"
    r"class|object|control|"
    r"fun[cç][aã]o|comando|propriedade|m[eé]todo|evento"
    r")\s*$",
    re.I,
)
# Depois de um prefixo de tipo em PT ("Comando", "Classe base"), não remover
# class/object do nome restante ("DEFINE CLASS", "Resize Object").
KIND_SUFFIX_AFTER_PREFIX_RE = re.compile(
    r"\s+(?:"
    r"functions?|commands?|properties|property|methods?|events?|"
    r"fun[cç][aã]o|comando|propriedade|m[eé]todo|evento"
    r")\s*$",
    re.I,
)
SECTION_HEADINGS = {
    "valor de retorno",
    "return value",
    "return values",
    "parametros",
    "parâmetros",
    "parameters",
    "observacoes",
    "observações",
    "remarks",
    "exemplo",
    "exemplos",
    "example",
    "examples",
    "see also",
    "consulte tambem",
    "consulte também",
}
STOPWORDS = {
    "or",
    "ou",
    "and",
    "e",
    "de",
    "do",
    "da",
    "das",
    "dos",
    "of",
    "the",
    "a",
    "o",
    "um",
    "uma",
    "para",
    "com",
    "em",
    "no",
    "na",
}
STRONG_PREFIXES = ("erro:", "sys:", "exts:", "pme:", "name:")


def strip_accents(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def slugify_title(title: str, max_len: int = 80) -> str:
    text = strip_accents(title).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rstrip("-")
    return text or "topico"


def markdown_filename(topic_id: str, title: str) -> str:
    return f"{slugify_title(title)}--{topic_id}.md"


def topic_id_from_md_name(name: str) -> str | None:
    stem = Path(name).stem
    if "--" in stem:
        suffix = stem.rsplit("--", 1)[-1]
        if suffix:
            return suffix.lower()
    return stem.lower() or None


def first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines()[:20]:
        match = HEADING_RE.match(line.strip())
        if match:
            return match.group(1).strip()
    return path.stem


def first_signature(text: str) -> str | None:
    match = CODE_BLOCK_RE.search(text or "")
    if not match:
        return None
    signature = re.sub(r"\s+", " ", match.group(1)).strip().lower()
    return signature or None


def _norm_tokens(text: str) -> str:
    text = strip_accents(text).lower()
    tokens = re.findall(r"[_a-z0-9@]+", text)
    return "".join(token for token in tokens if token not in STOPWORDS)


def is_section_heading(heading: str) -> bool:
    return strip_accents(heading).strip().lower() in SECTION_HEADINGS


def identity_keys(title: str, signature: str | None = None) -> set[str]:
    """Chaves estáveis que sobrevivem à redação EN/PT do título quando o nome VFP é mantido."""
    keys: set[str] = set()
    if not title:
        return keys

    error = ERROR_RE.search(title)
    if error:
        keys.add(f"erro:{error.group(1)}")
    sys_fn = SYS_RE.search(title)
    if sys_fn:
        keys.add(f"sys:{sys_fn.group(1)}")

    extensions = tuple(sorted({item.lower() for item in EXT_RE.findall(title)}))
    if len(extensions) >= 4:
        keys.add("exts:" + "".join(extensions))

    heading = title.strip()
    if re.match(r"^(?:how to|como)\b", heading, re.I):
        if signature and len(signature) >= 4:
            keys.add(f"sig:{signature}")
        return keys

    pme = PME_EN_RE.match(heading) or PME_PT_RE.match(heading)
    if pme:
        core = re.sub(
            r"\b(control|object|controle|objeto)\b", "", pme.group(1), flags=re.I
        )
        token = _norm_tokens(core)
        if token:
            keys.add(f"pme:{token}")
    else:
        prefix_match = KIND_PREFIX_RE.match(heading)
        stripped = KIND_PREFIX_RE.sub("", heading, count=1)
        suffix_re = KIND_SUFFIX_AFTER_PREFIX_RE if prefix_match else KIND_SUFFIX_RE
        stripped = suffix_re.sub("", stripped, count=1)
        stripped = re.sub(r"\(\s*Visual FoxPro\s*\)", "", stripped, flags=re.I)
        stripped = re.sub(r"\(\s*\)", "", stripped).strip(" -")
        if stripped != heading:
            token = _norm_tokens(stripped)
            if token:
                keys.add(f"name:{token}")

    if signature and len(signature) >= 4:
        keys.add(f"sig:{signature}")
    return keys


def strong_keys(keys: Iterable[str]) -> set[str]:
    return {key for key in keys if key.startswith(STRONG_PREFIXES)}


@dataclass
class _MdPage:
    path: Path
    guid: str
    heading: str
    keys: set[str] = field(default_factory=set)


def _unique_map(items: Sequence[tuple[set[str], object]], prefix: str) -> dict[str, object]:
    buckets: dict[str, list[object]] = defaultdict(list)
    for keys, obj in items:
        for key in keys:
            if key.startswith(prefix):
                buckets[key].append(obj)
    return {key: objs[0] for key, objs in buckets.items() if len(objs) == 1}


def _guid_index(md_dir: Path) -> dict[str, Path]:
    index: dict[str, Path] = {}
    if not md_dir.is_dir():
        return index
    for path in md_dir.glob("*.md"):
        topic_id = topic_id_from_md_name(path.name)
        if topic_id:
            index[topic_id.lower()] = path
    return index


def _load_pages(md_dir: Path) -> list[_MdPage]:
    pages: list[_MdPage] = []
    if not md_dir.is_dir():
        return pages
    for path in md_dir.glob("*.md"):
        guid = (topic_id_from_md_name(path.name) or "").lower()
        text = path.read_text(encoding="utf-8", errors="replace")
        heading = ""
        for line in text.splitlines()[:20]:
            match = HEADING_RE.match(line.strip())
            if match:
                heading = match.group(1).strip()
                break
        if not heading:
            heading = path.stem
        if is_section_heading(heading):
            keys: set[str] = set()
        else:
            keys = identity_keys(heading, first_signature(text))
        pages.append(_MdPage(path=path, guid=guid, heading=heading, keys=keys))
    return pages


def topic_markdown_index(
    md_dir: Path,
    topics: Sequence[dict] | None = None,
) -> dict[str, Path]:
    """Mapeia GUID do tópico -> caminho Markdown.

    Sem *topics*, é um índice cru de UUID no nome do arquivo (nomes antigos e com slug).
    Com *topics*, o UUID só é usado quando concorda com a identidade da página, para
    arquivos PT trocados religarem ao tópico que o H1/assinatura realmente descrevem.
    """
    if topics is None:
        return _guid_index(md_dir)

    pages = _load_pages(md_dir)
    by_guid = {page.guid: page for page in pages if page.guid}
    page_items = [(page.keys, page) for page in pages]

    topic_rows: list[tuple[str, set[str]]] = []
    for topic in topics:
        title = topic.get("title") or ""
        content = topic.get("content") or ""
        keys = identity_keys(title, first_signature(content))
        topic_rows.append((topic["id"].lower(), keys))
    topic_items = [(keys, topic_id) for topic_id, keys in topic_rows]

    index: dict[str, Path] = {}
    assigned_paths: set[Path] = set()
    path_owner: dict[Path, str] = {}

    def assign(topic_id: str, page: _MdPage) -> None:
        if topic_id in index or page.path in assigned_paths:
            return
        index[topic_id] = page.path
        assigned_paths.add(page.path)
        path_owner[page.path] = topic_id

    unique_topic_by_key: dict[str, str] = {}
    for prefix in ("erro:", "sys:", "exts:", "pme:", "name:", "sig:"):
        files_for = _unique_map(page_items, prefix)
        topics_for = _unique_map(topic_items, prefix)
        unique_topic_by_key.update(topics_for)
        for key, topic_id in topics_for.items():
            page = files_for.get(key)
            if page is not None:
                assign(topic_id, page)

    for topic_id, keys in topic_rows:
        if topic_id in index:
            continue
        page = by_guid.get(topic_id)
        if page is None or page.path in assigned_paths:
            continue
        if is_section_heading(page.heading):
            continue
        owned_by_other = False
        for key in strong_keys(page.keys):
            owner = unique_topic_by_key.get(key)
            if owner and owner != topic_id:
                owned_by_other = True
                break
        if owned_by_other:
            continue
        assign(topic_id, page)

    for topic_id, keys in topic_rows:
        if topic_id in index:
            continue
        taken = by_guid.get(topic_id)
        if taken is None or taken.path not in assigned_paths:
            continue
        other_id = path_owner.get(taken.path)
        if not other_id:
            continue
        partner = by_guid.get(other_id)
        if partner is None or partner.path in assigned_paths:
            continue
        if is_section_heading(partner.heading):
            continue
        assign(topic_id, partner)

    return index
