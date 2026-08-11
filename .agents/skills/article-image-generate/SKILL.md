---
name: article-image-generate
description: Read a complete article, plan and generate three or four context-specific editorial images with imagegen, normalize them into ordered article assets, and place their Markdown references at meaningful narrative points. Use when the user supplies an article Markdown path and wants new images generated and inserted.
---

# Article Image Generate

## Inputs

- A path to one article Markdown file.
- Optional visual direction from the user. When absent, derive a coherent editorial style from the article's tone and subject.

Default asset directory: `<article-folder>/images`.

## Required Skills

Use `$imagegen` for every generated image. Read its current `SKILL.md` before generation and follow its built-in-tool-first workflow. Do not switch to its CLI fallback unless the user explicitly requests or approves that fallback.

## Project Conventions

Follow the dominant convention in `pages/articles/`:

- Store editorial images in `pages/articles/images/` for articles in `pages/articles/`.
- Normalize generated assets to metadata-free WebP at a maximum width of 800 pixels.
- Name them in narrative order: `01__<article-stem>.webp`, `02__<article-stem>.webp`, and so on.
- Reference them with an article-relative Markdown path such as `./images/02__attention_is_fundamental.webp`.
- Put the hero image after YAML frontmatter, if any, and before the H1.
- Place later images at meaningful transitions, not at fixed line intervals.

Useful reference articles include:

- `pages/articles/ai_after_the_outrage_machine.md`
- `pages/articles/attention_is_fundamental.md`
- `pages/articles/medicines_dead_time.md`
- `pages/articles/90_percent_problem_of_agentic_SWE.md`

Inspect current project examples when conventions may have changed.

## Workflow

### 1. Read the whole article

Resolve the supplied path and read it from the first byte through EOF. Do not plan from an excerpt, headings alone, or a search-result fragment. If tool output truncates, continue with later line ranges until every paragraph, list, figure, code block, and reference section has been read.

Identify:

- the central thesis and intended reader;
- the article's narrative or argumentative movements;
- concrete scenes, mechanisms, tensions, and consequences that can be visualized;
- existing editorial images, charts, diagrams, and their Markdown anchors;
- YAML frontmatter, H1 location, reference definitions, tables, lists, and code blocks that must not be split.

If the article already contains intentional editorial images, do not silently replace or crowd them. Preserve charts and evidence figures. If adding or replacing images would materially change the requested scope, ask the user which treatment they want. Never overwrite existing image files without explicit replacement approval.

### 2. Make an image and placement plan

Choose three images by default. Choose four only when the article has four distinct visual beats and enough length for the images not to feel crowded. The set should usually cover:

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

The first image is always the hero. Later image order must match reading order. Prefer a natural section boundary or the end of a paragraph that introduces the visual idea. Do not insert an image inside a paragraph, list, table, code block, block quote, footnote/reference definition, or between a heading and content when that separation would harm readability.

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
  --article pages/articles/example.md \
  --input /path/to/selected-hero.png --alt "Concise description of the hero" \
  --input /path/to/selected-second.png --alt "Concise description of the second image" \
  --input /path/to/selected-third.png --alt "Concise description of the third image"
```

Add a fourth `--input` and `--alt` pair when the plan calls for four images. The helper:

- preserves the explicit input order;
- applies EXIF orientation;
- strips image metadata;
- resizes to a maximum width of 800 pixels while preserving aspect ratio;
- writes ordered WebP files beside the article under `images/`;
- prints JSON containing the final paths and Markdown snippets.

The helper refuses existing destination filenames by default. Use `--overwrite` only when the user explicitly authorized replacing those exact assets. Do not leave any article-referenced asset only under `$CODEX_HOME/generated_images/`.

### 5. Place the Markdown references

Edit only the target article unless the user requested other changes.

- Insert `01__` after frontmatter, if present, and before the H1.
- Insert `02__` through `04__` at their planned semantic anchors.
- Use the exact snippets emitted by the helper.
- Keep a blank line before and after each image line.
- Preserve all article prose, formatting, links, reference definitions, and existing figures.

Do not add captions unless the surrounding articles use them or the user requests them. Alt text should describe what the image shows, not repeat the filename or act as a second title.

### 6. Verify the finished article

Read the edited article around every insertion and confirm:

- exactly three or four new editorial images are referenced;
- image order in the Markdown is `01__`, `02__`, `03__`, then optional `04__`;
- every referenced path exists in the article's `images/` directory;
- the hero is before the H1 and after any frontmatter;
- no prose or structured block was accidentally split;
- each image supports the nearby text and the full set is reasonably distributed.

Report the final article path, every saved asset path, the placement anchors, the final prompt set, and that the built-in imagegen path was used (or name an explicitly approved fallback).

## Boundaries

- Generate and place three or four images, not an arbitrary larger gallery.
- Do not rewrite the article while adding images.
- Do not treat charts or screenshots as interchangeable with editorial illustrations.
- Do not delete discarded generations or existing assets unless the user explicitly asks.
- Do not overwrite same-named assets without explicit permission.
