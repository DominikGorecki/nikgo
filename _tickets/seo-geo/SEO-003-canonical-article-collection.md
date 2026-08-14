# SEO-003 — Migrate canonical articles into a private Jekyll collection

- **Priority:** P0
- **Effort:** XL
- **Status:** Blocked on approved disposition inventory
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

- [ ] Every approved published article exists in `_articles/` with explicit front matter.
- [ ] Every published article retains its exact pre-migration `.html` URL and returns generated HTML.
- [ ] Every published article has a unique title, description, date, author, category, image, and permalink.
- [ ] `date_modified` and `last_modified_at` are equal for each article.
- [ ] No `pages/articles/*.md` source file remains publicly copied.
- [ ] No raw article `.md` exists anywhere in `_site`.
- [ ] Approved alternate HTML URLs produce the expected static redirect document or a true 404 according to the disposition sheet.
- [ ] `/b/test.html` is no longer generated.
- [ ] No `.af`, lock, or `Zone.Identifier` file exists in `_site`.
- [ ] All article images and figures resolve.
- [ ] No current canonical article HTML URL changes.
- [ ] The GitHub Pages-compatible build succeeds without custom plugins.

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
