#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "Pillow>=10.4.0",
# ]
# ///

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageOps, UnidentifiedImageError


DEFAULT_MAX_WIDTH = 800
DEFAULT_QUALITY = 88
SUPPORTED_EXTENSIONS = {
    ".avif",
    ".bmp",
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
    ".tif",
    ".tiff",
    ".webp",
}


@dataclass(frozen=True)
class PlannedImage:
    source: Path
    output: Path
    index: int
    markdown: str


@dataclass(frozen=True)
class ProcessedImage:
    source: str
    output: str
    index: int
    original_size: tuple[int, int]
    output_size: tuple[int, int]
    markdown: str


def article_stem(article: Path) -> str:
    return article.stem


def default_raw_dir(article: Path) -> Path:
    return article.parent / "raw-images"


def default_output_dir(article: Path) -> Path:
    return article.parent / "images"


def image_sort_key(path: Path) -> tuple[float, str]:
    return (path.stat().st_mtime, path.name.lower())


def discover_images(raw_dir: Path, newest_first: bool = False) -> list[Path]:
    if not raw_dir.exists():
        raise FileNotFoundError(f"Raw image directory does not exist: {raw_dir}")
    if not raw_dir.is_dir():
        raise NotADirectoryError(f"Raw image path is not a directory: {raw_dir}")

    files = [
        path
        for path in raw_dir.iterdir()
        if path.is_file()
        and not path.name.startswith(".")
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
    return sorted(files, key=image_sort_key, reverse=newest_first)


def alt_text_from_article_stem(stem: str) -> str:
    text = re.sub(r"[_-]+", " ", stem).strip()
    text = re.sub(r"\s+", " ", text)
    return text.title() if text else "Article image"


def markdown_for(output: Path, output_dir: Path, stem: str) -> str:
    return f"![{alt_text_from_article_stem(stem)}](./{output_dir.name}/{output.name})"


def build_plan(
    article: Path,
    raw_dir: Path,
    output_dir: Path,
    newest_first: bool = False,
) -> list[PlannedImage]:
    stem = article_stem(article)
    images = discover_images(raw_dir, newest_first=newest_first)
    width = max(2, len(str(len(images))))
    plan: list[PlannedImage] = []
    for index, source in enumerate(images, start=1):
        filename = f"{index:0{width}d}__{stem}.webp"
        output = output_dir / filename
        plan.append(
            PlannedImage(
                source=source,
                output=output,
                index=index,
                markdown=markdown_for(output, output_dir, stem),
            )
        )
    return plan


def resized_dimensions(size: tuple[int, int], max_width: int) -> tuple[int, int]:
    width, height = size
    if width <= 0 or height <= 0:
        raise ValueError(f"Invalid image size: {size}")
    if width <= max_width:
        return size
    ratio = max_width / width
    return (max_width, max(1, math.floor(height * ratio)))


def normalize_image(image: Image.Image, max_width: int) -> tuple[Image.Image, tuple[int, int]]:
    oriented = ImageOps.exif_transpose(image)
    original_size = oriented.size
    output_size = resized_dimensions(original_size, max_width)
    if output_size != original_size:
        oriented = oriented.resize(output_size, Image.Resampling.LANCZOS)

    if oriented.mode in {"RGBA", "LA"} or (
        oriented.mode == "P" and "transparency" in oriented.info
    ):
        normalized = oriented.convert("RGBA")
    else:
        normalized = oriented.convert("RGB")
    return normalized, original_size


def process_one(
    planned: PlannedImage,
    max_width: int,
    quality: int,
) -> ProcessedImage:
    try:
        with Image.open(planned.source) as image:
            normalized, original_size = normalize_image(image, max_width)
            planned.output.parent.mkdir(parents=True, exist_ok=True)
            normalized.save(
                planned.output,
                "WEBP",
                quality=quality,
                method=6,
            )
            output_size = normalized.size
    except UnidentifiedImageError as exc:
        raise ValueError(f"Unsupported or corrupt image: {planned.source}") from exc

    return ProcessedImage(
        source=str(planned.source),
        output=str(planned.output),
        index=planned.index,
        original_size=original_size,
        output_size=output_size,
        markdown=planned.markdown,
    )


def process_images(
    article: Path,
    raw_dir: Path | None = None,
    output_dir: Path | None = None,
    max_width: int = DEFAULT_MAX_WIDTH,
    quality: int = DEFAULT_QUALITY,
    newest_first: bool = False,
    dry_run: bool = False,
) -> list[ProcessedImage] | list[PlannedImage]:
    if max_width < 1:
        raise ValueError("--max-width must be greater than 0")
    if not 1 <= quality <= 100:
        raise ValueError("--quality must be between 1 and 100")
    if not article.exists():
        raise FileNotFoundError(f"Article does not exist: {article}")
    if not article.is_file():
        raise ValueError(f"Article path is not a file: {article}")

    raw_dir = raw_dir or default_raw_dir(article)
    output_dir = output_dir or default_output_dir(article)
    plan = build_plan(article, raw_dir, output_dir, newest_first=newest_first)
    if dry_run:
        return plan
    return [process_one(item, max_width=max_width, quality=quality) for item in plan]


def serialize_items(items: Iterable[ProcessedImage | PlannedImage]) -> list[dict[str, object]]:
    serialized: list[dict[str, object]] = []
    for item in items:
        data = {
            "index": item.index,
            "source": str(item.source),
            "output": str(item.output),
            "markdown": item.markdown,
        }
        if isinstance(item, ProcessedImage):
            data["original_size"] = list(item.original_size)
            data["output_size"] = list(item.output_size)
        serialized.append(data)
    return serialized


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Convert raw article images into ordered metadata-free WebP files. "
            "Input: --article PATH. Output: JSON listing generated files and markdown snippets."
        )
    )
    parser.add_argument("--article", help="Path to the target article markdown file.")
    parser.add_argument(
        "--raw-dir",
        help="Directory containing raw images. Defaults to <article-folder>/raw-images.",
    )
    parser.add_argument(
        "--output-dir",
        help="Directory for generated WebP files. Defaults to <article-folder>/images.",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=DEFAULT_MAX_WIDTH,
        help=f"Resize images wider than this value. Default: {DEFAULT_MAX_WIDTH}.",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=DEFAULT_QUALITY,
        help=f"WebP quality from 1 to 100. Default: {DEFAULT_QUALITY}.",
    )
    parser.add_argument(
        "--newest-first",
        action="store_true",
        help="Sort raw images newest first instead of oldest first.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned output without writing files.",
    )
    parser.add_argument(
        "--run-tests",
        action="store_true",
        help="Run embedded unit tests and exit.",
    )
    return parser


def run_tests() -> int:
    import os
    import time
    import unittest

    class ProcessArticleImagesTests(unittest.TestCase):
        def test_run_tests_requires_no_input(self) -> None:
            args = build_parser().parse_args(["--run-tests"])
            self.assertTrue(args.run_tests)

        def test_resized_dimensions_preserves_ratio(self) -> None:
            self.assertEqual(resized_dimensions((1600, 900), 800), (800, 450))
            self.assertEqual(resized_dimensions((700, 500), 800), (700, 500))

        def test_plan_uses_mtime_order_and_article_stem(self) -> None:
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                article = root / "my_article.md"
                article.write_text("# My Article\n", encoding="utf-8")
                raw_dir = root / "raw-images"
                output_dir = root / "images"
                raw_dir.mkdir()
                newer = raw_dir / "newer.png"
                older = raw_dir / "older.png"
                Image.new("RGB", (10, 10), "red").save(newer)
                Image.new("RGB", (10, 10), "blue").save(older)
                now = time.time()
                os.utime(older, (now - 20, now - 20))
                os.utime(newer, (now - 10, now - 10))

                plan = build_plan(article, raw_dir, output_dir)

                self.assertEqual([p.source.name for p in plan], ["older.png", "newer.png"])
                self.assertEqual(plan[0].output.name, "01__my_article.webp")
                self.assertEqual(plan[1].output.name, "02__my_article.webp")
                self.assertEqual(
                    plan[0].markdown,
                    "![My Article](./images/01__my_article.webp)",
                )

        def test_process_strips_metadata_and_resizes(self) -> None:
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                article = root / "sample.md"
                article.write_text("# Sample\n", encoding="utf-8")
                raw_dir = root / "raw-images"
                output_dir = root / "images"
                raw_dir.mkdir()
                source = raw_dir / "source.jpg"
                image = Image.new("RGB", (1200, 600), "green")
                exif = Image.Exif()
                exif[271] = "Camera Brand"
                image.save(source, exif=exif)

                result = process_images(
                    article=article,
                    raw_dir=raw_dir,
                    output_dir=output_dir,
                    max_width=800,
                )

                self.assertEqual(len(result), 1)
                processed = result[0]
                self.assertIsInstance(processed, ProcessedImage)
                self.assertEqual(processed.output_size, (800, 400))
                with Image.open(output_dir / "01__sample.webp") as generated:
                    self.assertEqual(generated.size, (800, 400))
                    self.assertFalse(generated.getexif())
                    self.assertNotIn("icc_profile", generated.info)

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(ProcessArticleImagesTests)
    )
    return 0 if result.wasSuccessful() else 1


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.run_tests:
        return run_tests()
    if not args.article:
        parser.error("--article is required unless --help or --run-tests is used")

    try:
        items = process_images(
            article=Path(args.article),
            raw_dir=Path(args.raw_dir) if args.raw_dir else None,
            output_dir=Path(args.output_dir) if args.output_dir else None,
            max_width=args.max_width,
            quality=args.quality,
            newest_first=args.newest_first,
            dry_run=args.dry_run,
        )
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(serialize_items(items), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
