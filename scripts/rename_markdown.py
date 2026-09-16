#!/usr/bin/env python3
"""
Renomeia arquivos Markdown que só têm GUID para slug--uuid.md, para
ficarem legíveis no editor, sem perder o id estável do tópico.

Uso:
    python rename_markdown.py --dry-run
    python rename_markdown.py
    python rename_markdown.py --md-dir data/markdown_pt
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from html_utils import project_paths
from md_paths import first_heading, markdown_filename, topic_id_from_md_name


def parse_args() -> argparse.Namespace:
    paths = project_paths(__file__)
    parser = argparse.ArgumentParser(
        description="Renomeia tópicos Markdown para slug--uuid.md"
    )
    parser.add_argument(
        "--md-dir",
        action="append",
        type=Path,
        dest="md_dirs",
        help="Pasta a renomear (repetível). Padrão: markdown_pt",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not args.md_dirs:
        args.md_dirs = [
            paths["data_dir"] / "markdown_pt",
        ]
    return args


def planned_name(path: Path) -> str | None:
    topic_id = topic_id_from_md_name(path.name)
    if not topic_id:
        return None
    title = first_heading(path)
    return markdown_filename(topic_id, title)


def rename_directory(md_dir: Path, dry_run: bool) -> tuple[int, int, int]:
    if not md_dir.is_dir():
        print(f"Pasta não encontrada: {md_dir}", file=sys.stderr)
        return 0, 0, 0

    renamed = 0
    skipped = 0
    missing = 0
    taken: set[str] = {p.name.lower() for p in md_dir.glob("*.md")}

    for path in sorted(md_dir.glob("*.md")):
        target_name = planned_name(path)
        if target_name is None:
            missing += 1
            continue
        if path.name == target_name:
            skipped += 1
            continue
        dest = path.with_name(target_name)
        if dest.exists() or target_name.lower() in taken:
            print(f"colisão, mantido {path.name}", file=sys.stderr)
            skipped += 1
            continue
        if not dry_run:
            path.rename(dest)
        taken.discard(path.name.lower())
        taken.add(target_name.lower())
        renamed += 1

    return renamed, skipped, missing


def main() -> int:
    args = parse_args()
    action = "renomearia" if args.dry_run else "renomeou"
    for md_dir in args.md_dirs:
        renamed, skipped, missing = rename_directory(md_dir, args.dry_run)
        print(
            f"{md_dir}: {action} {renamed}, "
            f"já ok {skipped}, sem id {missing}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
