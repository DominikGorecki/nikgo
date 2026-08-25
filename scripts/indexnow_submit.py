#!/usr/bin/env python3
"""Submit an explicit, reviewed list of nikgo.com canonical pages to IndexNow.

The public verification key is intentionally stored in the root text file named
after the key.  This script deliberately has no automatic deployment trigger:
call it only after GitHub Pages confirms the submitted revision is live.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

HOST = "nikgo.com"
ENDPOINT = "https://api.indexnow.org/indexnow"
MAX_BATCH_SIZE = 10_000
KEY_FILE = "eba952432abeb6494173cc79e3e39b6b0fb24968d3395e9808b3d7b6245c7c9a.txt"
KEY_LOCATION = f"https://{HOST}/{KEY_FILE}"
BLOCKED_SUFFIXES = (".md", ".markdown", ".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".css", ".js", ".xml", ".txt", ".json")
BLOCKED_PATHS = {"/404.html", "/sitemap.xml", "/robots.txt", f"/{KEY_FILE}"}


def canonical_url(value: str) -> str | None:
    """Return a valid content URL, otherwise None.

    IndexNow notifications are for canonical HTML documents, not source files,
    generated utility endpoints, assets, or a repository/preview host.
    """
    parsed = urlparse(value.strip())
    if parsed.scheme != "https" or parsed.netloc != HOST or parsed.params or parsed.query or parsed.fragment:
        return None
    if not parsed.path or parsed.path in BLOCKED_PATHS or parsed.path.endswith(BLOCKED_SUFFIXES):
        return None
    return f"https://{HOST}{parsed.path}"


def read_urls(path: Path) -> tuple[list[str], list[str]]:
    accepted: list[str] = []
    rejected: list[str] = []
    seen: set[str] = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        value = raw.strip()
        if not value or value.startswith("#"):
            continue
        normalised = canonical_url(value)
        if normalised is None:
            rejected.append(value)
        elif normalised not in seen:
            seen.add(normalised)
            accepted.append(normalised)
    return accepted, rejected


def submit_batch(urls: list[str], key: str) -> tuple[int, str]:
    payload = json.dumps({"host": HOST, "key": key, "keyLocation": KEY_LOCATION, "urlList": urls}).encode("utf-8")
    request = urllib.request.Request(ENDPOINT, data=payload, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, response.read(500).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as error:
        return error.code, error.read(500).decode("utf-8", errors="replace")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url_file", type=Path, help="UTF-8 file with one explicit changed canonical URL per line")
    parser.add_argument("--dry-run", action="store_true", help="validate and print the batch without making a network request")
    args = parser.parse_args(argv)
    urls, rejected = read_urls(args.url_file)
    for value in rejected:
        print(f"Rejected non-canonical/non-content URL: {value}", file=sys.stderr)
    if rejected:
        return 2
    if not urls:
        print("No canonical content URLs to submit.")
        return 0
    if args.dry_run:
        print("Dry run: would submit these canonical URLs:")
        print("\n".join(urls))
        return 0
    key = os.environ.get("INDEXNOW_KEY", "")
    if key != KEY_FILE.removesuffix(".txt"):
        print("INDEXNOW_KEY must match the committed public verification-key filename.", file=sys.stderr)
        return 2
    result = 0
    for start in range(0, len(urls), MAX_BATCH_SIZE):
        batch = urls[start : start + MAX_BATCH_SIZE]
        status, body = submit_batch(batch, key)
        safe_body = body.replace("\n", " ").strip() or "(empty response)"
        print(f"IndexNow batch {start // MAX_BATCH_SIZE + 1}: {len(batch)} URLs, HTTP {status}, {safe_body}")
        if status not in (200, 202):
            result = 1
    return result


if __name__ == "__main__":
    raise SystemExit(main())
