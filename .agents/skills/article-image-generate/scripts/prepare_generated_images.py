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
import os
import re
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path

from PIL import Image, ImageOps, UnidentifiedImageError


DEFAULT_MAX_WIDTH = 800
DEFAULT_QUALITY = 88
MIN_IMAGES = 3
MAX_IMAGES = 4
ARTICLE_SOURCE_DIR = "_articles"
PUBLISHED_ARTICLE_DIR = Path("pages/articles")
EDITORIAL_IMAGE_DIR = "images"


@dataclass(frozen=True)
class PlannedImage:
    index: int
    role: str
    source: Path
    output: Path
    alt: str
    site_path: str
    markdown: str | None


@dataclass(frozen=True)
class ProcessedImage:
    index: int
    role: str
    source: str
    output: str
    alt: str
    site_path: str
    markdown: str | None
    original_size: tuple[int, int]
    output_size: tuple[int, int]


def normalize_alt_text(value: str) -> str:
    text = re.sub(r"\s+", " ", value).strip()
    if not text:
        raise ValueError("Alt text must not be empty")
    return text.replace("[", r"\[").replace("]", r"\]")


def is_collection_article(article: Path) -> bool:
    return article.parent.name == ARTICLE_SOURCE_DIR


def repository_root(article: Path) -> Path:
    if not is_collection_article(article):
        raise ValueError(
            f"Expected a Markdown source directly under {ARTICLE_SOURCE_DIR}/: {article}"
        )
    return article.parent.parent


def published_article_dir(article: Path) -> Path:
    return repository_root(article) / PUBLISHED_ARTICLE_DIR


def default_output_dir(article: Path) -> Path:
    if is_collection_article(article):
        return published_article_dir(article) / EDITORIAL_IMAGE_DIR
    return article.parent / EDITORIAL_IMAGE_DIR


def published_relative_path(article: Path, output: Path) -> Path | None:
    if not is_collection_article(article):
        return None
    try:
        return output.relative_to(published_article_dir(article))
    except ValueError as exc:
        raise ValueError(
            "Assets for _articles sources must be written under pages/articles "
            f"so Jekyll publishes them beside the article: {output}"
        ) from exc


def markdown_path(article: Path, output: Path) -> str:
    published_relative = published_relative_path(article, output)
    if published_relative is not None:
        return f"./{published_relative.as_posix()}"
    relative = Path(os.path.relpath(output, start=article.parent)).as_posix()
    if not relative.startswith("."):
        relative = f"./{relative}"
    return relative


def site_path(article: Path, output: Path) -> str:
    if is_collection_article(article):
        relative = published_relative_path(article, output)
        assert relative is not None
        return f"/{(PUBLISHED_ARTICLE_DIR / relative).as_posix()}"
    return markdown_path(article, output)


def resized_dimensions(size: tuple[int, int], max_width: int) -> tuple[int, int]:
    width, height = size
    if width <= 0 or height <= 0:
        raise ValueError(f"Invalid image size: {size}")
    if width <= max_width:
        return size
    ratio = max_width / width
    return (max_width, max(1, math.floor(height * ratio)))


def validate_count(inputs: list[Path], alts: list[str]) -> None:
    if not MIN_IMAGES <= len(inputs) <= MAX_IMAGES:
        raise ValueError(
            f"Expected {MIN_IMAGES} or {MAX_IMAGES} --input values; got {len(inputs)}"
        )
    if len(alts) != len(inputs):
        raise ValueError(
            "Provide exactly one --alt value for every --input value "
            f"({len(inputs)} inputs, {len(alts)} alt values)"
        )


def build_plan(
    article: Path,
    inputs: list[Path],
    alts: list[str],
    output_dir: Path,
) -> list[PlannedImage]:
    validate_count(inputs, alts)
    plan: list[PlannedImage] = []
    for index, (source, raw_alt) in enumerate(zip(inputs, alts, strict=True), start=1):
        alt = normalize_alt_text(raw_alt)
        output = output_dir / f"{index:02d}__{article.stem}.webp"
        role = "hero" if index == 1 else "inline"
        plan.append(
            PlannedImage(
                index=index,
                role=role,
                source=source,
                output=output,
                alt=alt,
                site_path=site_path(article, output),
                markdown=(
                    None
                    if role == "hero"
                    else f"![{alt}]({markdown_path(article, output)})"
                ),
            )
        )
    return plan


def preflight(
    article: Path,
    plan: list[PlannedImage],
    max_width: int,
    quality: int,
    overwrite: bool,
) -> None:
    if not article.exists() or not article.is_file():
        raise FileNotFoundError(f"Article file does not exist: {article}")
    if article.suffix.lower() not in {".md", ".markdown"}:
        raise ValueError(f"Article must be a Markdown file: {article}")
    if is_collection_article(article):
        for item in plan:
            published_relative_path(article, item.output)
    if max_width < 1:
        raise ValueError("--max-width must be greater than 0")
    if not 1 <= quality <= 100:
        raise ValueError("--quality must be between 1 and 100")

    missing = [item.source for item in plan if not item.source.is_file()]
    if missing:
        raise FileNotFoundError(
            "Generated input file(s) do not exist: " + ", ".join(map(str, missing))
        )

    collisions = [item.output for item in plan if item.output.exists()]
    if collisions and not overwrite:
        raise FileExistsError(
            "Destination file(s) already exist; explicit --overwrite is required: "
            + ", ".join(map(str, collisions))
        )


def normalize_image(source: Path, destination: Path, max_width: int, quality: int) -> tuple[tuple[int, int], tuple[int, int]]:
    try:
        with Image.open(source) as image:
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

            normalized.save(destination, "WEBP", quality=quality, method=6)
            return original_size, normalized.size
    except UnidentifiedImageError as exc:
        raise ValueError(f"Unsupported or corrupt image: {source}") from exc


def process_images(
    article: Path,
    inputs: list[Path],
    alts: list[str],
    output_dir: Path | None = None,
    max_width: int = DEFAULT_MAX_WIDTH,
    quality: int = DEFAULT_QUALITY,
    overwrite: bool = False,
    dry_run: bool = False,
) -> list[PlannedImage] | list[ProcessedImage]:
    output_dir = output_dir or default_output_dir(article)
    plan = build_plan(article, inputs, alts, output_dir)
    preflight(article, plan, max_width, quality, overwrite)
    if dry_run:
        return plan

    output_dir.mkdir(parents=True, exist_ok=True)
    processed: list[ProcessedImage] = []
    with tempfile.TemporaryDirectory(
        prefix=".article-image-generate-", dir=output_dir
    ) as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        staged: list[tuple[Path, PlannedImage, tuple[int, int], tuple[int, int]]] = []
        for item in plan:
            temporary_output = temp_dir / item.output.name
            original_size, output_size = normalize_image(
                item.source, temporary_output, max_width, quality
            )
            staged.append((temporary_output, item, original_size, output_size))

        for temporary_output, item, original_size, output_size in staged:
            temporary_output.replace(item.output)
            processed.append(
                ProcessedImage(
                    index=item.index,
                    role=item.role,
                    source=str(item.source),
                    output=str(item.output),
                    alt=item.alt,
                    site_path=item.site_path,
                    markdown=item.markdown,
                    original_size=original_size,
                    output_size=output_size,
                )
            )
    return processed


def serialize(items: list[PlannedImage] | list[ProcessedImage]) -> list[dict[str, object]]:
    serialized: list[dict[str, object]] = []
    for item in items:
        record = asdict(item)
        record["source"] = str(record["source"])
        record["output"] = str(record["output"])
        serialized.append(record)
    return serialized


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Normalize three or four explicitly ordered generated images into "
            "metadata-free article WebP assets. For _articles sources, write to "
            "pages/articles/images and print hero metadata plus inline Markdown as JSON."
        )
    )
    parser.add_argument("--article", help="Path to the target article Markdown file.")
    parser.add_argument(
        "--input",
        action="append",
        dest="inputs",
        help="Generated image path. Repeat three or four times in narrative order.",
    )
    parser.add_argument(
        "--alt",
        action="append",
        dest="alts",
        help="Descriptive alt text paired by order with each --input.",
    )
    parser.add_argument(
        "--output-dir",
        help=(
            "Asset directory. For _articles sources, defaults to "
            "pages/articles/images and must remain under pages/articles."
        ),
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=DEFAULT_MAX_WIDTH,
        help=f"Resize wider images to this width. Default: {DEFAULT_MAX_WIDTH}.",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=DEFAULT_QUALITY,
        help=f"WebP quality from 1 to 100. Default: {DEFAULT_QUALITY}.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace existing ordered destination assets.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs and print the planned JSON without writing files.",
    )
    parser.add_argument(
        "--run-tests",
        action="store_true",
        help="Run embedded unit tests and exit.",
    )
    return parser


def run_tests() -> int:
    import unittest

    class PrepareGeneratedImagesTests(unittest.TestCase):
        def test_run_tests_requires_no_other_arguments(self) -> None:
            args = build_parser().parse_args(["--run-tests"])
            self.assertTrue(args.run_tests)

        def test_plan_preserves_input_order_and_builds_markdown(self) -> None:
            root = Path("/project")
            article = root / "_articles" / "sample_article.md"
            inputs = [Path("hero.png"), Path("middle.png"), Path("ending.png")]
            alts = ["Hero scene", "Middle [contrast]", "Ending scene"]

            plan = build_plan(
                article,
                inputs,
                alts,
                root / "pages" / "articles" / "images",
            )

            self.assertEqual([item.source for item in plan], inputs)
            self.assertEqual(plan[0].output.name, "01__sample_article.webp")
            self.assertEqual(plan[0].role, "hero")
            self.assertIsNone(plan[0].markdown)
            self.assertEqual(
                plan[0].site_path,
                "/pages/articles/images/01__sample_article.webp",
            )
            self.assertEqual(
                plan[1].markdown,
                r"![Middle \[contrast\]](./images/02__sample_article.webp)",
            )

        def test_collection_output_must_be_published_beside_articles(self) -> None:
            root = Path("/project")
            article = root / "_articles" / "sample_article.md"

            with self.assertRaisesRegex(ValueError, "under pages/articles"):
                build_plan(
                    article,
                    [Path("one.png"), Path("two.png"), Path("three.png")],
                    ["One", "Two", "Three"],
                    root / "_articles" / "images",
                )

        def test_requires_three_or_four_images_and_matching_alts(self) -> None:
            with self.assertRaisesRegex(ValueError, "Expected 3 or 4"):
                validate_count([Path("one.png"), Path("two.png")], ["One", "Two"])
            with self.assertRaisesRegex(ValueError, "one --alt"):
                validate_count(
                    [Path("one.png"), Path("two.png"), Path("three.png")],
                    ["One", "Two"],
                )

        def test_processing_resizes_strips_metadata_and_refuses_collision(self) -> None:
            with tempfile.TemporaryDirectory() as temp_dir_name:
                root = Path(temp_dir_name)
                article_dir = root / "_articles"
                article_dir.mkdir()
                article = article_dir / "article.md"
                article.write_text("# Article\n", encoding="utf-8")
                inputs: list[Path] = []
                for index, color in enumerate(("red", "green", "blue"), start=1):
                    source = root / f"source-{index}.jpg"
                    image = Image.new("RGB", (1600, 900), color)
                    exif = Image.Exif()
                    exif[271] = "Test Camera"
                    image.save(source, exif=exif)
                    inputs.append(source)

                results = process_images(
                    article=article,
                    inputs=inputs,
                    alts=["Red scene", "Green scene", "Blue scene"],
                )

                self.assertEqual(len(results), 3)
                first_output = (
                    root / "pages" / "articles" / "images" / "01__article.webp"
                )
                self.assertTrue(first_output.exists())
                self.assertEqual(results[0].role, "hero")
                self.assertEqual(
                    results[0].site_path,
                    "/pages/articles/images/01__article.webp",
                )
                self.assertIsNone(results[0].markdown)
                self.assertEqual(
                    results[1].markdown,
                    "![Green scene](./images/02__article.webp)",
                )
                with Image.open(first_output) as generated:
                    self.assertEqual(generated.size, (800, 450))
                    self.assertFalse(generated.getexif())
                    self.assertNotIn("icc_profile", generated.info)

                with self.assertRaises(FileExistsError):
                    process_images(
                        article=article,
                        inputs=inputs,
                        alts=["Red scene", "Green scene", "Blue scene"],
                    )

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            PrepareGeneratedImagesTests
        )
    )
    return 0 if result.wasSuccessful() else 1


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.run_tests:
        return run_tests()
    if not args.article:
        parser.error("--article is required unless --help or --run-tests is used")
    if not args.inputs:
        parser.error("repeat --input three or four times")
    if not args.alts:
        parser.error("repeat --alt once for every --input")

    try:
        items = process_images(
            article=Path(args.article),
            inputs=[Path(value) for value in args.inputs],
            alts=args.alts,
            output_dir=Path(args.output_dir) if args.output_dir else None,
            max_width=args.max_width,
            quality=args.quality,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
        )
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(serialize(items), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
