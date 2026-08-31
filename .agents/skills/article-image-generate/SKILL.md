---
name: article-image-generate
description: Read a complete article, plan and generate three or four context-specific editorial images with imagegen, normalize them into ordered article assets, set the hero in article frontmatter, and place later images at meaningful narrative points. Use when the user supplies an article Markdown path and wants new images generated and inserted.
---

# Article Image Generate

## Inputs

- A path to one article Markdown file.
- Optional visual direction from the user. When absent, derive a coherent editorial style from the article's tone and subject.

For canonical sources under `_articles/`, the published asset directory is `pages/articles/images/`.

## Required Skills

Use `$imagegen` for every generated image. Read its current `SKILL.md` before generation and follow its built-in-tool-first workflow. Do not switch to its CLI fallback unless the user explicitly requests or approves that fallback.

## Project Conventions

The current repository separates article sources from published assets:

- Canonical article Markdown lives directly under `_articles/`.
- Generated editorial assets live under `pages/articles/images/`, where Jekyll publishes them beside article HTML.
- The article layout renders the hero from the YAML `image` object. Do **not** insert the hero as body Markdown.
- A local hero uses a root-relative frontmatter path plus its actual dimensions and alt text:

  ```yaml
  image:
    path: /pages/articles/images/01__example.webp
    width: 800
    height: 450
    alt: "Concrete description of the hero image"
  ```

- Inline editorial images use article-relative Markdown such as `./images/02__example.webp` because the rendered page lives under `/pages/articles/`.
- Normalize generated assets to metadata-free WebP at a maximum width of 800 pixels.
- Name a newly generated set in narrative order: `01__<article-stem>.webp`, `02__<article-stem>.webp`, and so on. `01__` is the frontmatter hero; only `02__` onward appear in the body.
- Source articles normally omit an H1 because `_layouts/article.html` renders `page.title`. Do not add an H1 merely to place an image.
- Place inline images at semantic transitions, not fixed line intervals. Current articles often put an image after the paragraph that establishes a mechanism or consequence, sometimes immediately before the next H2, and sometimes directly after a heading when it opens that section visually.
- Research articles use evidence figures under `pages/articles/figures/`, often with captions. Preserve those figures and do not renumber or replace them with editorial art.

Useful current examples include:

- `_articles/Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md`
- `_articles/what_freedom_for__v2.md`
- `_articles/attention_is_fundamental.md`
- `_articles/medicines_dead_time.md`
- `_articles/90_percent_problem_of_agentic_SWE.md`
- `_articles/small_RAG_beats_large_large_search.md` for the separate research-figure convention

Inspect current `_articles/` examples again whenever placement or repository layout may have changed.

## Workflow

### 1. Read the whole article

Resolve the supplied path and read it from the first byte through EOF. Do not plan from an excerpt, headings alone, or a search-result fragment. If tool output truncates, continue with later line ranges until every paragraph, list, figure, code block, and reference section has been read.

Identify:

- the central thesis and intended reader;
- the article's narrative or argumentative movements;
- concrete scenes, mechanisms, tensions, and consequences that can be visualized;
- existing editorial images, charts, diagrams, and their Markdown anchors;
- YAML frontmatter, especially `article_type` and the `image` object;
- reference definitions, headings, tables, lists, and code blocks that must not be split.

Confirm that the supplied source is the intended canonical file under `_articles/`. If it is a research article, distinguish evidence figures from optional editorial art before planning anything. If a draft has no YAML frontmatter, do not invent the full publication metadata merely to place a hero; ask whether frontmatter should be added before generation.

If the article already contains intentional editorial images, do not silently replace or crowd them. Preserve charts and evidence figures. If adding or replacing images would materially change the requested scope, ask the user which treatment they want. Never overwrite existing image files without explicit replacement approval.

### 2. Make an image and placement plan

Choose three images by default, counting the frontmatter hero. Choose four only when the article has four distinct visual beats and enough length for the images not to feel crowded. The set should usually cover:

1. a hero that expresses the article's thesis;
2. a mechanism, contrast, or turning point;
3. a human, organizational, or practical consequence;
4. an optional synthesis, future state, or second major turn.

For each planned image, write down:

- ordered index;
- narrative purpose;
- exact placement anchor, using a unique heading or nearby paragraph;
- concise descriptive alt text;
- a self-contained generation prompt.

The first image is always the frontmatter hero. Later image order must match reading order. Prefer the end of a paragraph that introduces or completes the visual idea, a natural section boundary, or a section-opening position demonstrated by current articles. Do not insert an image inside a paragraph, list, table, code block, block quote, caption, footnote, or reference definition.

### 3. Generate a coherent set with imagegen

Issue one built-in image generation call per planned asset. These are distinct assets, so do not ask one call to return a collage or contact sheet.

Make every prompt self-contained because the images are generated separately. Include:

- use case: `illustration-story`, `stylized-concept`, `photorealistic-natural`, or another imagegen taxonomy slug appropriate to the article;
- asset type: editorial article illustration;
- the image's narrative purpose and concrete scene;
- wide landscape composition suitable for an article, preferably 16:9;
- a shared style, palette, lighting, and level of abstraction repeated across all prompts;
- no text, captions, labels, logos, borders, or watermarks unless the article truly requires exact text;
- enough subject and compositional variation that the set does not repeat the same laptop, robot, dashboard, or generic office scene.

Use the article's ideas as source material, but avoid inventing claims or depicting a metaphor that contradicts the prose. For sensitive historical, medical, or scientific subjects, prefer accurate and respectful visual framing.

Inspect each result before accepting it. Check subject accuracy, composition, stylistic consistency, unwanted text, visual artifacts, and fit with the planned placement. Regenerate only the failed asset with a targeted prompt change. Retain the selected local output path reported by imagegen for each accepted image.

### 4. Normalize, rename, and move the assets

From the repository root, pass the selected generated files to the helper in final narrative order. Pair each input with its matching alt text:

```bash
uv run --script .agents/skills/article-image-generate/scripts/prepare_generated_images.py \
  --article _articles/example.md \
  --input /path/to/selected-hero.png --alt "Concise description of the hero" \
  --input /path/to/selected-second.png --alt "Concise description of the second image" \
  --input /path/to/selected-third.png --alt "Concise description of the third image"
```

Add a fourth `--input` and `--alt` pair when the plan calls for four images. The helper:

- preserves the explicit input order;
- applies EXIF orientation;
- strips image metadata;
- resizes to a maximum width of 800 pixels while preserving aspect ratio;
- writes ordered WebP files to `pages/articles/images/` for an `_articles/` source;
- marks `01__` as `role: "hero"`, emitting its root-relative `site_path`, actual `output_size`, and `markdown: null`;
- emits article-relative Markdown only for inline images `02__` through `04__`;
- prints JSON containing the final filesystem paths, roles, site paths, dimensions, alt text, and inline Markdown snippets.

For `_articles/`, any explicit `--output-dir` must remain under `pages/articles/`; the helper rejects `_articles/images/` because Jekyll would not publish it beside the rendered article.

The helper refuses existing destination filenames by default. Use `--overwrite` only when the user explicitly authorized replacing those exact assets. Do not leave any article-referenced asset only under `$CODEX_HOME/generated_images/`.

### 5. Set the hero and place inline references

Edit only the target article unless the user requested other changes.

- Update the YAML `image` object for `01__` using the helper's `site_path`, actual output width and height, and planned alt text. Preserve any existing `caption` or `credit` unless the replacement changes their truth.
- Do not add a hero Markdown line to the article body.
- Insert the exact helper-emitted Markdown for `02__` through `04__` at their planned semantic anchors.
- Keep a blank line before and after each image line.
- Preserve all article prose, formatting, links, reference definitions, and existing figures.

Do not add captions unless the surrounding articles use them or the user requests them. Alt text should describe what the image shows, not repeat the filename or act as a second title.

### 6. Verify the finished article

Read the edited article around every insertion and confirm:

- exactly three or four new editorial assets exist: one frontmatter hero plus two or three inline images;
- frontmatter points to `01__`, and inline Markdown order is `02__`, `03__`, then optional `04__`;
- the root-relative hero path maps to an existing file under `pages/articles/images/`;
- every inline `./images/...` path maps to an existing file under `pages/articles/images/`;
- frontmatter width and height match the normalized hero's actual dimensions;
- no duplicate hero Markdown was inserted into the article body;
- no prose or structured block was accidentally split;
- each image supports the nearby text and the full set is reasonably distributed.

Run `make site-check` when the repository's Docker toolchain is available so Jekyll, image paths, frontmatter, and generated HTML are validated together.

Report the final article path, every saved asset path, the placement anchors, the final prompt set, and that the built-in imagegen path was used (or name an explicitly approved fallback).

## Boundaries

- Generate and place three or four images, not an arbitrary larger gallery.
- Do not rewrite the article while adding images.
- Do not treat charts or screenshots as interchangeable with editorial illustrations.
- Do not put generated assets under `_articles/images/`.
- Do not add a body H1 or duplicate the frontmatter hero in Markdown.
- Do not delete discarded generations or existing assets unless the user explicitly asks.
- Do not overwrite same-named assets without explicit permission.
