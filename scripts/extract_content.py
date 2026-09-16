#!/usr/bin/env python3
"""
Extrai e limpa tópicos do HTML Help do Visual FoxPro 9 para um JSONL intermediário.

Uso:
    python extract_content.py
    python extract_content.py --min-chars 120 --output data/topics.jsonl
    python extract_content.py --md-dir data/markdown_pt --no-jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from hashlib import md5
from pathlib import Path

from bs4 import BeautifulSoup

from html_utils import (
    body_to_markdown,
    build_title_index,
    extract_alink_keywords,
    extract_title,
    is_low_value_topic,
    normalize_content,
    parse_hhc_categories,
    parse_hhk_keywords,
    project_paths,
    useful_body_text,
)
from md_paths import markdown_filename


def parse_args() -> argparse.Namespace:
    paths = project_paths(__file__)
    parser = argparse.ArgumentParser(description="Extrai e limpa tópicos HTML da ajuda VFP.")
    parser.add_argument(
        "--html-dir",
        type=Path,
        default=paths["html_dir"],
        help="Directory containing .htm topic files",
    )
    parser.add_argument(
        "--hhc",
        type=Path,
        default=paths["hhc"],
        help="HTML Help contents (.hhc) file for categories",
    )
    parser.add_argument(
        "--hhk",
        type=Path,
        default=paths["hhk"],
        help="HTML Help index (.hhk) file for keywords",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=paths["data_dir"] / "topics.jsonl",
        help="Output JSONL file with cleaned topics",
    )
    parser.add_argument(
        "--min-chars",
        type=int,
        default=80,
        help="Skip topics whose cleaned content is shorter than this",
    )
    parser.add_argument(
        "--min-useful-chars",
        type=int,
        default=80,
        help="Skip See Also-heavy / navigation-only topics below this useful length",
    )
    parser.add_argument(
        "--max-see-also",
        type=int,
        default=5,
        help="Maximum See Also links retained per topic",
    )
    parser.add_argument(
        "--md-dir",
        type=Path,
        default=None,
        help="Write one Markdown file per topic into this directory",
    )
    parser.add_argument(
        "--no-jsonl",
        action="store_true",
        help="Skip writing the JSONL file (use with --md-dir)",
    )
    return parser.parse_args()


def topic_to_markdown(topic: dict) -> str:
    title = (topic.get("title") or "").strip()
    content = (topic.get("content") or "").strip()
    if title:
        return f"# {title}\n\n{content}\n"
    return f"{content}\n"


def extract_topic(
    path: Path,
    link_titles: dict[str, str],
    categories: dict[str, str],
    index_keywords: dict[str, list[str]],
    max_see_also: int,
) -> dict | None:
    raw_html = path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw_html, "html.parser")

    title = extract_title(soup)
    body = soup.find("div", id="mainBody")
    if not body:
        return None

    content = normalize_content(
        body_to_markdown(body, link_titles),
        max_see_also_links=max_see_also,
    )
    if len(content) < 1:
        return None

    file_key = path.name.lower()
    alink_keywords = extract_alink_keywords(soup)
    keywords = sorted(set(index_keywords.get(file_key, []) + alink_keywords))
    useful = useful_body_text(content)

    return {
        "id": path.stem,
        "source_file": path.name,
        "title": title,
        "category": categories.get(file_key, ""),
        "keywords": keywords,
        "content": content,
        "char_count": len(content),
        "useful_char_count": len(useful),
        "content_hash": md5(content.encode("utf-8")).hexdigest(),
    }


def main() -> int:
    args = parse_args()

    if not args.html_dir.is_dir():
        print(f"HTML directory not found: {args.html_dir}", file=sys.stderr)
        return 1

    print("Building title index for internal links...")
    link_titles = build_title_index(args.html_dir)

    print("Parsing table of contents and index...")
    categories = parse_hhc_categories(args.hhc)
    index_keywords = parse_hhk_keywords(args.hhk)

    html_files = sorted(args.html_dir.glob("*.htm"))
    print(f"Processing {len(html_files)} HTML files...")

    if args.md_dir:
        args.md_dir.mkdir(parents=True, exist_ok=True)

    out = None
    if not args.no_jsonl:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        out = args.output.open("w", encoding="utf-8")

    written = 0
    md_written = 0
    skipped_short = 0
    skipped_low_value = 0
    skipped_duplicate = 0
    skipped_no_body = 0
    seen_hashes: set[str] = set()

    try:
        for path in html_files:
            topic = extract_topic(
                path,
                link_titles,
                categories,
                index_keywords,
                max_see_also=args.max_see_also,
            )
            if not topic:
                skipped_no_body += 1
                continue

            if args.md_dir:
                md_path = args.md_dir / markdown_filename(topic["id"], topic["title"])
                md_path.write_text(topic_to_markdown(topic), encoding="utf-8")
                md_written += 1

            if out is None:
                continue
            if topic["char_count"] < args.min_chars:
                skipped_short += 1
                continue
            if is_low_value_topic(topic["content"], min_useful_chars=args.min_useful_chars):
                skipped_low_value += 1
                continue
            if topic["content_hash"] in seen_hashes:
                skipped_duplicate += 1
                continue
            seen_hashes.add(topic["content_hash"])
            out.write(json.dumps(topic, ensure_ascii=False) + "\n")
            written += 1
    finally:
        if out is not None:
            out.close()

    if args.md_dir:
        print(f"Wrote {md_written} Markdown files to {args.md_dir}")
    if out is not None:
        print(f"Wrote {written} topics to {args.output}")
        print(f"Skipped short: {skipped_short}")
        print(f"Skipped low-value/nav: {skipped_low_value}")
        print(f"Skipped duplicates: {skipped_duplicate}")
    print(f"Skipped missing body: {skipped_no_body}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
