# SEO-005 — Build a semantic article layout with visible provenance

- **Priority:** P0
- **Effort:** L
- **Status:** Ready after SEO-003 and SEO-004
- **Dependencies:** SEO-003, SEO-004
- **Blocks:** SEO-006, SEO-007, SEO-009, SEO-010, SEO-011, SEO-012, SEO-013, SEO-015
- **Spec coverage:** P0-11, P0-12, P1-13

## Outcome

Every article has one semantic title, a scannable provenance block, valid document landmarks, and reusable presentation hooks without duplicating title or cover content from the Markdown body.

## Current-state evidence

- All pages use the overridden `_layouts/default.html`; there is no article-specific layout.
- The global hero renders `nikGo` as an `h1`, while article Markdown also starts with an `h1`, producing two top-level headings.
- Article bodies generally repeat their cover image and title as the first Markdown elements.
- The default layout wraps page content in an `article` element even for indexes and utility pages.
- Publication dates, modified dates, author identity, breadcrumbs, and related-reading regions are not consistently visible.

## GitHub Pages compatibility constraints

- Implement with layouts, includes, Liquid 4.0, HTML, and CSS only.
- Do not introduce a custom Ruby plugin or a Liquid filter absent from Jekyll 3.10.0.
- Use collection/front-matter values established by SEO-003; do not derive important metadata from Git history at build time.
- Keep each article's explicit legacy permalink so relative image and figure references continue to resolve.

## Implementation scope

### 1. Correct the shared document outline

- Change the global brand heading in `_layouts/default.html` from `h1` to a non-heading brand element or an anchor with equivalent styling.
- Keep one `main` landmark with a stable `id` for the skip link.
- Let page-specific layouts decide whether the primary content is an `article`; do not wrap every page type in `article`.
- Preserve the current theme and navigation behavior while eliminating invalid landmark nesting.

### 2. Add `_layouts/article.html`

The layout must render, in this order:

1. A visible breadcrumb: Home → Articles → current article.
2. Article category/topic label.
3. Exactly one `h1` from `page.title`.
4. Optional deck/summary from `page.description` or a dedicated `deck` field.
5. Byline linked to the canonical author page.
6. Machine-readable `<time datetime="...">` publication date and, when different, modified date.
7. Optional reading-time text only if supplied or calculated by tested Liquid without a plugin.
8. Cover `<figure>` using `page.image`, with meaningful alt text and optional caption/credit.
9. Article body in a stable content container.
10. Author/trust block and related-article include hooks.

Use semantic elements such as `header`, `nav`, `article`, `section`, `footer`, `figure`, and `figcaption` according to their actual purpose. A breadcrumb list must be a real ordered list, not CSS-generated text.

### 3. Normalize article bodies

- Remove only the leading Markdown cover image and duplicate `# Title` that the new layout replaces.
- Retain all substantive body copy, headings, figures, quotations, citations, links, and footnotes.
- Ensure the first body section begins at `h2`; do not mechanically shift headings inside embedded diagrams or code.
- Do not remove an opening image if it is materially different from the front-matter cover.

### 4. Provide explicit extension points

Create or reserve includes for:

- `article-author.html` — populated in SEO-007.
- `related-articles.html` — populated in SEO-009.
- `article-provenance.html` — optional research methods/citation details from SEO-010.

Includes must render nothing when required data is absent and must not leave empty headings or sections.

## Acceptance criteria

- [ ] Every canonical article uses `layout: article`.
- [ ] Each generated article has exactly one `h1`, matching its front-matter title.
- [ ] The visible author, publication date, and modified date agree with structured metadata.
- [ ] Every displayed date uses a valid machine-readable `datetime` value.
- [ ] Breadcrumbs are keyboard accessible and contain canonical internal links.
- [ ] The source body no longer repeats a layout-rendered title or cover.
- [ ] Index, About, topic hub, 404, and utility pages are not incorrectly wrapped as articles.
- [ ] Existing article permalinks and relative images remain functional.
- [ ] Empty optional metadata produces no empty DOM regions.

## Verification

```bash
bundle exec jekyll build --trace
```

Run an HTML parser against every canonical article and assert:

- one `main`, one `article`, and one `h1`;
- non-empty author link and publication `<time>`;
- breadcrumb links resolve;
- heading order does not skip from `h1` directly to `h3`;
- no duplicate leading cover image.

Manually inspect one short essay, one long research article, and one article with multiple figures at mobile and desktop widths.

## Out of scope

- JSON-LD and social metadata; SEO-006.
- Author biography content; SEO-007.
- Related-article selection; SEO-009.
- Accessibility behavior beyond the structural foundation; SEO-015.

## Rollback

Revert the layout assignment and body normalization in the same change. Restoring only the old layout would leave articles without their source title and cover.
