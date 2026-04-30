---
name: article-image-ingest
description: Convert raw article images into ordered metadata-free WebP assets, then place them into an article markdown file by reading the article and image content.
---

# Article Image Ingest

## Use When

Use this skill when the user gives an article markdown path, such as `pages/articles/medicines_dead_time.md`, and wants the images in `pages/articles/raw-images` processed into article-ready assets under `pages/articles/images` and inserted into the article.

## Inputs

- Article markdown file path.
- Raw image folder. Default: `<article-folder>/raw-images`.
- Output image folder. Default: `<article-folder>/images`.

## Workflow

1. Inspect the target article and an existing image-bearing article if needed.
   - Top image pattern: `![Alt text](./images/<image>.webp)` before the `# Title`.
   - Example: `pages/articles/Rokos_Symbiotic_Carrot.md`.

2. Run the deterministic image processor from the repo root:

   ```bash
   .agents/skills/article-image-ingest/scripts/process_article_images.py --article pages/articles/medicines_dead_time.md
   ```

   If direct execution is unavailable, use:

   ```bash
   uv run --script .agents/skills/article-image-ingest/scripts/process_article_images.py --article pages/articles/medicines_dead_time.md
   ```

3. The script sorts files in `<article-folder>/raw-images` by last modified time, oldest first, and writes metadata-free WebP files to `<article-folder>/images`.

   Output naming:

   ```text
   01__<article-stem>.webp
   02__<article-stem>.webp
   03__<article-stem>.webp
   ```

   Example:

   ```text
   pages/articles/images/01__medicines_dead_time.webp
   ```

4. Read the generated script output. It includes ordered filenames, dimensions, and markdown snippets.

5. Understand the images before placing them.
   - Use image viewing or model vision on each generated image when available.
   - `01__` does not need semantic placement analysis; place it above the article title as the hero image.
   - For `02__` and later, inspect the image, read the article, and place each image where it best supports the nearby section.

6. Preserve image order constraints.
   - `01__` goes at the very top before the H1.
   - `02__` must appear somewhere after `01__`.
   - `03__` must appear somewhere after `02__`.
   - Continue in numeric order even when semantic placement is imperfect.

7. Insert markdown using article-relative paths:

   ```markdown
   ![Concise descriptive alt text](./images/02__medicines_dead_time.webp)
   ```

8. Keep edits scoped to the target article and generated image assets unless the user asks for more.

## Script Options

- `--article PATH`: required for normal execution.
- `--raw-dir PATH`: override the default raw image directory.
- `--output-dir PATH`: override the default output image directory.
- `--max-width 800`: resize images wider than this while preserving aspect ratio.
- `--quality 88`: WebP quality.
- `--newest-first`: reverse the modified-time order.
- `--dry-run`: print the planned output without writing images.
- `--run-tests`: run embedded tests.

## Notes

- The script strips metadata by loading pixels, applying EXIF orientation, and writing a fresh WebP without EXIF or ICC data.
- The script overwrites same-named generated WebP files. Do not delete raw images unless the user explicitly asks.
- If an article already has image markdown, preserve existing intentional placements unless replacing them is clearly part of the request.
