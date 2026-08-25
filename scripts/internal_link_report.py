#!/usr/bin/env python3
"""Report and validate the canonical article relationship graph.

Run from the repository root:
  python3 scripts/internal_link_report.py --check

The JSON report is intentionally written to stdout so CI can retain it as an
artifact without committing generated data.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml


MARKDOWN_LINK = re.compile(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)")


def load_article(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing front matter")
    try:
        _, front_matter, body = text.split("---", 2)
    except ValueError as error:
        raise ValueError(f"{path}: malformed front matter") from error
    data = yaml.safe_load(front_matter) or {}
    return data, body


def article_links(body: str) -> list[str]:
    links = []
    for raw_link in MARKDOWN_LINK.findall(body):
        link = raw_link.split("#", 1)[0]
        if link.startswith("/pages/articles/"):
            links.append(link)
    return links


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="exit nonzero for invalid canonical relationships")
    args = parser.parse_args()
    root = args.root.resolve()

    records: list[dict[str, Any]] = []
    errors: list[str] = []
    for source in sorted((root / "_articles").glob("*.md")):
        data, body = load_article(source)
        if data.get("published") is not True:
            continue
        records.append({"source": source, "data": data, "body": body})

    ids = [record["data"].get("content_id") for record in records]
    duplicate_ids = sorted(content_id for content_id, count in Counter(ids).items() if content_id and count > 1)
    missing_ids = [str(record["source"].relative_to(root)) for record in records if not record["data"].get("content_id")]
    if missing_ids:
        errors.append(f"missing content_id: {', '.join(missing_ids)}")
    if duplicate_ids:
        errors.append(f"duplicate content_id: {', '.join(duplicate_ids)}")

    by_id = {record["data"].get("content_id"): record for record in records if record["data"].get("content_id")}
    by_url = {record["data"].get("permalink"): record for record in records if record["data"].get("permalink")}
    redirects = {
        path
        for record in records
        for path in record["data"].get("redirect_from", [])
    }
    inbound: dict[str, set[str]] = defaultdict(set)
    report_articles: list[dict[str, Any]] = []

    for record in records:
        data = record["data"]
        content_id = data["content_id"]
        related = data.get("related", [])
        related_errors = []
        if not isinstance(related, list):
            related_errors.append("related must be a list")
            related = []
        for target in related:
            if target == content_id:
                related_errors.append(f"self-referential related ID: {target}")
            elif target not in by_id:
                related_errors.append(f"unknown related ID: {target}")
            elif target in related[: related.index(target)]:
                related_errors.append(f"duplicate related ID: {target}")
            else:
                inbound[target].add(content_id)

        body_urls = article_links(record["body"])
        broken_urls = sorted(url for url in body_urls if url not in by_url)
        redirect_urls = sorted(url for url in body_urls if url in redirects)
        raw_markdown_urls = sorted(url for url in body_urls if url.endswith(".md"))
        if related_errors:
            errors.extend(f"{content_id}: {error}" for error in related_errors)
        if broken_urls:
            errors.append(f"{content_id}: broken internal article URLs: {', '.join(broken_urls)}")
        if redirect_urls:
            errors.append(f"{content_id}: redirect URLs used: {', '.join(redirect_urls)}")
        if raw_markdown_urls:
            errors.append(f"{content_id}: raw Markdown URLs used: {', '.join(raw_markdown_urls)}")

        report_articles.append(
            {
                "content_id": content_id,
                "canonical_url": data.get("permalink"),
                "primary_hub": f"/topics/{data.get('category', '')}/",
                "related_ids": related,
                "outbound_article_urls": body_urls,
                "broken_article_urls": broken_urls,
                "redirect_article_urls": redirect_urls,
            }
        )

    for article in report_articles:
        article["inbound_article_ids"] = sorted(inbound[article["content_id"]])
    orphans = sorted(article["content_id"] for article in report_articles if not article["inbound_article_ids"])
    report = {"articles": report_articles, "orphan_content_ids": orphans, "errors": errors}
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if args.check and errors else 0


if __name__ == "__main__":
    sys.exit(main())
