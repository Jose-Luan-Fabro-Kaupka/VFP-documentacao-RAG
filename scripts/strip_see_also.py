#!/usr/bin/env python3
"""
Remove a seção "# Consulte também" (o título e tudo depois dele)
dos tópicos Markdown traduzidos.

Uso:
    python strip_see_also.py
    python strip_see_also.py --dry-run
    python strip_see_also.py --md-dir data/markdown_pt --heading "Consulte também"
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from html_utils import project_paths

HEADING_RE_TEMPLATE = r"^#+\s*{heading}\s*$"


def parse_args() -> argparse.Namespace:
    paths = project_paths(__file__)
    parser = argparse.ArgumentParser(
        description='Remove "# Consulte também" (e tudo depois) de arquivos Markdown.'
    )
    parser.add_argument(
        "--md-dir",
        type=Path,
        default=paths["data_dir"] / "markdown_pt",
        help="Pasta de arquivos .md (padrão: data/markdown_pt)",
    )
    parser.add_argument(
        "--heading",
        default="Consulte também",
        help='Texto do título a cortar, sem o prefixo "# "',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Lista os arquivos que mudariam, sem gravar",
    )
    return parser.parse_args()


def heading_pattern(heading: str) -> re.Pattern[str]:
    return re.compile(HEADING_RE_TEMPLATE.format(heading=re.escape(heading)))


def strip_from_heading(text: str, pattern: re.Pattern[str]) -> str | None:
    """Devolve o texto sem a linha do título e tudo depois dela, ou None."""
    lines = text.splitlines(keepends=True)
    cut_at = None
    for index, line in enumerate(lines):
        if pattern.match(line.rstrip("\r\n")):
            cut_at = index
            break
    if cut_at is None:
        return None
    kept = "".join(lines[:cut_at]).rstrip()
    return kept + "\n" if kept else ""


def main() -> int:
    args = parse_args()
    md_dir: Path = args.md_dir
    if not md_dir.is_dir():
        print(f"Pasta não encontrada: {md_dir}", file=sys.stderr)
        return 1

    pattern = heading_pattern(args.heading)
    files = sorted(md_dir.glob("*.md"))
    changed = 0
    emptied = 0
    skipped = 0

    for path in files:
        original = path.read_text(encoding="utf-8")
        stripped = strip_from_heading(original, pattern)
        if stripped is None:
            skipped += 1
            continue
        if stripped == original:
            skipped += 1
            continue
        if not stripped.strip():
            emptied += 1
        changed += 1
        if not args.dry_run:
            path.write_text(stripped, encoding="utf-8")

    action = "reescreveria" if args.dry_run else "reescreveu"
    print(
        f"{action} {changed} arquivo(s); "
        f"{skipped} sem '# {args.heading}'; "
        f"{emptied} ficaram vazios"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
