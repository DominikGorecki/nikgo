# SEO-003 — Migrate canonical articles into a private Jekyll collection

- **Priority:** P0
- **Effort:** XL
- **Status:** Implemented and verified on 2026-08-14
- **Dependencies:** SEO-001, SEO-002
- **Blocks:** SEO-004 through SEO-013
- **Spec coverage:** P0-3, P0-4, P0-5, P0-8, part of P0-9

## Outcome

Each published article has one rendered HTML URL and no public raw Markdown twin. Article source lives in `_articles/`, carries explicit front matter, and is queryable as `site.articles`. Current public canonical HTML paths remain unchanged. Drafts, alternate source copies, test posts, and design/OS artifacts no longer ship.

## Current-state evidence

- The audited production/Jekyll output contains rendered `.html` and copied raw `.md` files for the 26 article sources present when the source spec was written.
- The current worktree now contains a 27th, untracked candidate, `Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md`; SEO-002 must disposition it before migration rather than assuming it is published.
- All 26 raw `.md` URLs in the production audit were verified as HTTP 200.
- Half the rendered articles receive generic titles because inference fails when an image precedes the first heading.
- `_site` shows the raw and rendered pairs plus `/b/test.html` and public `.af`, lock, and `Zone.Identifier` files.
- Jekyll 3.10 supports custom collections and per-document permalinks on GitHub Pages.

## GitHub Pages compatibility constraints

Use a standard Jekyll collection; do not add a custom plugin:

```yaml
collections:
  articles:
    output: true

defaults:
  - scope:
      path: ""
      type: articles
    values:
      layout: article
      author: dominik-gorecki
      sitemap: true
      published: true
```

Every document must declare its exact legacy permalink in front matter. Do **not** use `/:collection/:name`, because Jekyll's `:name` slugifies filenames and would change current case/underscores.

Example:

```yaml
---
layout: article
title: "The Market for Portable Minds"
description: "Approved description."
permalink: /pages/articles/Market_for_Portable_Minds.html
date: 2026-05-01
date_modified: 2026-08-11
last_modified_at: 2026-08-11
author: dominik-gorecki
category: agentic-engineering
tags:
  - portable context
  - AI labor markets
image:
  path: /pages/articles/images/02__Market_for_Portable_Minds.webp
  width: 800
  height: 450
  alt: "A controlled interface between portable worker context and company systems"
featured: true
feature_order: 5
published: true
redirect_from: []
---
```

`date_modified` is consumed by `jekyll-seo-tag` 2.8.0. `last_modified_at` is consumed by `jekyll-sitemap` 1.4.0. Keep the two values equal and update them only for material changes.

## Implementation scope

### 1. Add `_articles/` and collection configuration

- Move only approved published articles into `_articles/`.
- Add complete front matter from SEO-002.
- Keep article body content unchanged except for path corrections required by the move.
- Preserve existing article/figure asset directories initially so browser-relative image URLs keep resolving from the unchanged public article URL.
- Confirm `./images/...` and `./figures/...` links still resolve in generated HTML.

### 2. Preserve public HTML URLs

- Add an explicit `permalink` to every article.
- Compare generated paths before and after.
- Update templates to refer to `article.url | relative_url`; stop constructing URLs from filenames.
- Keep current absolute internal links valid.

### 3. Handle alternates according to SEO-002

- Move non-published source into an ignored archival directory such as `_archive/articles/` if retention is required.
- Do not configure `_archive` as a collection.
- Add approved alternate HTML paths to the canonical document's `redirect_from` array only after enabling the supported plugin in `_config.yml`.
- Verify redirect stubs contain a destination canonical/meta refresh and do not appear in the sitemap.
- Do not call these static pages “301 redirects.”
- Do not generate redirect stubs for raw `.md` URLs; those should return 404.

### 4. Remove build contaminants

- Remove `_posts/2018-01-01-test.md` and its companion test content from the production source, archiving outside the publish tree only if needed.
- Remove or relocate all public `.af`, `*.af~lock~*`, and `*:Zone.Identifier` files.
- Add patterns to `.gitignore` to prevent recurrence.
- Ensure no useful web image/PDF is removed.

### 5. Update content consumers

- Change article loops to use `site.articles` where introduced in the same change.
- Update `_layouts/default.html` logic that currently checks `page.path contains 'pages/articles/'`; collection paths begin `_articles/`. Prefer `page.collection == 'articles'` or `page.layout == 'article'`.
- Do not complete the full article-index refactor here; SEO-008 owns that work.

## Acceptance criteria

- [x] Every approved published article exists in `_articles/` with explicit front matter.
- [x] Every published article retains its exact pre-migration `.html` URL and returns generated HTML.
- [x] Every published article has a unique title, description, date, author, category, explicit image state, and permalink.
- [x] `date_modified` and `last_modified_at` are equal for each article.
- [x] No `pages/articles/*.md` source file remains publicly copied.
- [x] No raw article `.md` exists anywhere in `_site`.
- [x] Approved alternate HTML URLs produce the expected static redirect document or a true 404 according to the disposition sheet.
- [x] `/b/test.html` is no longer generated.
- [x] No `.af`, lock, or `Zone.Identifier` file exists in `_site`.
- [x] All article images and figures resolve.
- [x] No current canonical article HTML URL changes.
- [x] The GitHub Pages-compatible build succeeds without custom plugins.

## Verification

```bash
bundle exec jekyll build --trace
find _site -type f | rg '\.md$|\.af$|Zone\.Identifier|~lock~|/b/test\.html$'
find _site/pages/articles -maxdepth 1 -name '*.html' -print | sort
rg -n '<title>|<h1|<img' _site/pages/articles/Market_for_Portable_Minds.html
git status --short
```

Expected: the contaminant search returns no results. Compare a saved pre-migration canonical URL list with generated output and fail on any missing path.

## Out of scope

- New article layout design beyond the minimum required to build; SEO-005 owns it.
- Final structured-data graph; SEO-006.
- Clean `/articles/slug/` URL migration.
- Server-side HTTP 301/410 headers, which branch-hosted GitHub Pages cannot configure.
- Rewriting article prose.

## Rollback

Revert the collection configuration and file moves together. Do not leave duplicate source in both `pages/articles/` and `_articles/` in a deployed commit.

## Implementation record — 2026-08-14

### Collection and URL migration

- Added the `articles` output collection, collection defaults, and the GitHub Pages-supported `jekyll-redirect-from` plugin to `_config.yml`.
- Added a minimal `_layouts/article.html` wrapper over the existing default layout. The article presentation remains unchanged; SEO-005 owns the semantic redesign.
- Moved the 19 SEO-002 `publish` documents into `_articles/` and added explicit approved front matter.
- Preserved all 19 canonical paths listed in [SEO-003-canonical-url-baseline.txt](SEO-003-canonical-url-baseline.txt). Every listed file exists in `_site`, and every generated canonical tag uses the same `https://nikgo.com` URL.
- Added `url: "https://nikgo.com"` and an empty `baseurl` so the supported redirect plugin emits the production custom-domain destination instead of a repository-derived GitHub URL.
- Updated the article index's Markdown links to explicit canonical HTML paths and applied the approved author/date corrections.
- Updated article detection in the default layout from a source-path substring check to the `articles` collection/article layout.

### Private dispositions

- Relocated five approved archive candidates, the source of the approved redirect, and two `publish-after-edit` candidates under `_archive/articles/`.
- Added the single approved static redirect from `/pages/articles/what_freedom_for.html` to `/pages/articles/what_freedom_for__v2.html`.
- Verified the redirect document contains the custom-domain canonical, JavaScript destination, meta refresh, and `noindex` directive.
- Verified the five archive candidates and two `publish-after-edit` candidates generate neither HTML nor raw Markdown output.

### Build-contaminant cleanup

- Relocated the default Jekyll test post and its companion include under `_archive/test-content/`.
- Relocated `.af`, lock, and `Zone.Identifier` files under `_archive/build-contaminants/`, preserving them in version control but excluding them from Jekyll output.
- Added recurrence guards to `.gitignore`, with narrow exceptions for the intentional private archive.
- Excluded `_archive/`, `README.md`, and `SEO-GEO-IMPROVEMENT-SPEC.md` explicitly so the generated site contains no Markdown source files.

### Metadata and content integrity

- All 19 public documents have unique titles and descriptions, an approved date/modified date, author key, category, tags, related candidates, explicit permalink, feature state, article type, and image state.
- Eighteen articles map to an existing representative image with verified dimensions and alt text. `great-ai-pink-slip-panic.md` retains the SEO-002-approved explicit `image: null` state; SEO-013 owns creation of its representative image.
- `date_modified` and `last_modified_at` match for all 19 documents.
- A source-body comparison found no prose changes. `Rokos_Symbiotic_Carrot.md` gained only a final newline.
- All local images, figures, scripts, and article-index targets referenced by generated article HTML resolve to generated files.

### Build verification

`make site-build` completed successfully with `github-pages` 232 and Jekyll 3.10.0. The expected unauthenticated local GitHub Metadata warning remains. Verification confirmed:

- 19 canonical article documents and one approved static redirect document are generated.
- Every URL in the saved canonical baseline exists and has the expected canonical tag.
- No `.md`, `.af`, lock, `Zone.Identifier`, or `/b/test.html` file exists in `_site`.
- No custom plugin directory or unsupported dependency was added.
