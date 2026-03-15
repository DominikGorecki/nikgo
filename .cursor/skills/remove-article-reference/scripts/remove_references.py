#!/usr/bin/env python3
"""Strip references and links from article markdown."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

REFERENCE_DEFINITION_RE = re.compile(r"^\s*\[[^\]]+\]:\s*\S+.*$")
IMAGE_LINK_RE = re.compile(r"!\[([^\]]*)\]\(([^\)]*)\)")
INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\([^\)]*\)")
REFERENCE_LINK_RE = re.compile(r"\[([^\]]+)\]\[[^\]]*\]")
ANGLE_LINK_RE = re.compile(r"<(https?://[^>\s]+)>")
PLAIN_URL_RE = re.compile(r"\bhttps?://\S+\b")


def strip_markdown_links(content: str) -> str:
    """Return markdown with link/ reference syntax removed."""

    lines = [line for line in content.splitlines() if not REFERENCE_DEFINITION_RE.match(line)]
    content = "\n".join(lines)

    content = IMAGE_LINK_RE.sub(r"IMAGE: [\1] - \2", content)
    content = INLINE_LINK_RE.sub(r"\1", content)
    content = REFERENCE_LINK_RE.sub(r"\1", content)
    content = ANGLE_LINK_RE.sub("", content)
    content = PLAIN_URL_RE.sub("", content)

    # Clean up whitespace introduced by link removal.
    content = re.sub(r" {2,}", " ", content)
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content.strip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Create a link-free copy of an article markdown file. "
            "Output file is written to <stem>__no_ref.md in the same folder."
        )
    )
    parser.add_argument("input_markdown", help="Path to a markdown article file")
    parser.add_argument(
        "output_markdown",
        nargs="?",
        help="Optional output path (defaults to <input-dir>/<stem>__no_ref.md)",
    )
    args = parser.parse_args(argv)

    source_path = Path(args.input_markdown)
    if not source_path.exists():
        print(f"[ERROR] Input file not found: {source_path}", file=sys.stderr)
        return 1
    if not source_path.is_file():
        print(f"[ERROR] Input path is not a file: {source_path}", file=sys.stderr)
        return 1

    output_path = (
        Path(args.output_markdown)
        if args.output_markdown
        else source_path.with_name(f"{source_path.stem}__no_ref.md")
    )

    raw_text = source_path.read_text(encoding="utf-8")
    cleaned = strip_markdown_links(raw_text)
    output_path.write_text(cleaned, encoding="utf-8")

    print(f"[OK] Wrote sanitized file: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
