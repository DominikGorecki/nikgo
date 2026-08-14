# SEO-006 — Normalize canonical metadata, article schema, and social previews

- **Priority:** P0
- **Effort:** L
- **Status:** Ready after SEO-004 and SEO-005
- **Dependencies:** SEO-004, SEO-005
- **Blocks:** SEO-007, SEO-010, SEO-011, SEO-012, SEO-013, SEO-017
- **Spec coverage:** P0-8, P0-9, P0-10, P0-15, P1-26

## Outcome

Each canonical page emits one coherent metadata set for search engines, social platforms, and generative systems, with article-specific values and no conflicting duplicate schema.

## Current-state evidence

- `_layouts/default.html` uses `{% seo %}` from `jekyll-seo-tag` 2.8.0.
- A custom `_includes/article-social-image.html` infers a social image by scraping source/body conventions rather than using explicit metadata.
- Current production output mixes HTTP and HTTPS in canonical, Open Graph, image, and JSON-LD URLs.
- Articles lack consistent descriptions, author URLs, modified dates, image dimensions, and schema types.
- `jekyll-seo-tag` 2.8.0 already supports page title, description, image objects, author, locale, canonical URL, `seo.type`, and `date_modified`.

## GitHub Pages compatibility constraints

- `jekyll-seo-tag` 2.8.0 is supported, but its combined `{% seo %}` output does not expose the complete stable reusable `@id` graph required by this spec or a supported way to suppress only its JSON-LD.
- Replace the single `{% seo %}` invocation with one project-owned Liquid include that emits metadata and the complete JSON-LD graph. Do not retain the plugin's JSON-LD beside it.
- Serialize values with Liquid's `jsonify` and validate generated JSON. No custom Ruby plugin may generate metadata.
- Use front matter for all page-specific values. Do not parse rendered Markdown to discover titles, descriptions, or images.

## Implementation scope

### 1. Define the page metadata contract

Require the following on every article:

```yaml
title: "Human-readable article title"
description: "Specific 140–170 character summary of the page's actual answer."
date: 2026-01-15
date_modified: 2026-01-15
last_modified_at: 2026-01-15
author: dominik-gorecki
seo:
  type: BlogPosting
image:
  path: /assets/articles/example/cover-16x9.webp
  width: 1280
  height: 720
  alt: "Meaningful description"
```

Research pieces may use `ScholarlyArticle`, which is a subtype of `Article`, after SEO-010 verifies that the content carries genuine scholarly provenance. Titles and descriptions must be unique; they are editorial fields, not filename transformations.

### 2. Build one project-owned head include

- Replace `{% seo %}` and `_includes/article-social-image.html` with one `_includes/seo-head.html` invoked once by the default layout.
- Resolve the canonical URL from an explicit `canonical_url` override or `site.url` plus `page.url`; resolve the author key through `_data/authors.yml` from SEO-007.
- Emit one title, meta description, canonical, robots, Open Graph set, and Twitter set from the same resolved values.
- Emit `twitter:card=summary_large_image` only after every indexable page has a valid article or site fallback image.
- Remove `_includes/article-social-image.html` once explicit `page.image` values cover every article.
- Escape HTML attributes correctly and use `jsonify` for JSON values; never interpolate unescaped title/description/body text into JSON.
- Do not retain a parallel `{% seo %}` invocation or any manually duplicated Open Graph/canonical block.

### 3. Emit one reusable entity graph

- Use `https://nikgo.com/#website` for the WebSite and `https://nikgo.com/about/#person` for the author on every page.
- On Home, emit `WebSite` with the approved name, description, URL, creator/publisher reference, and a reference to the canonical Person. Do not invent `SearchAction` unless a functioning site search exists.
- On About, emit `ProfilePage` as the page type with `mainEntity` pointing to the full Person defined by SEO-007.
- On articles, emit one `BlogPosting`, `Article`, or qualifying `ScholarlyArticle` with `@id` equal to `<canonical>#article`, `mainEntityOfPage`, headline, description, dates, ImageObject dimensions, author Person `@id`, WebSite `isPartOf`, keywords, and language.
- Add `BreadcrumbList` with `<canonical>#breadcrumb` to articles and hubs, exactly matching visible breadcrumbs.
- Add `CollectionPage`/`ItemList` only to the generated article index, project index, and substantive topic hubs from SEO-008.
- Add `SoftwareApplication` only for a visible project that truthfully meets the type and has accurate properties.
- For genuine research in SEO-010, add visible/accurate `abstract`, citations, `isBasedOn`, PDF `encoding`, and dataset references only when the corresponding artifacts exist.
- Render `<meta name="robots" content="max-image-preview:large">` on indexable pages. Merge this value with any page-specific robots policy instead of creating two robots tags.

### 4. Establish conflict rules

- Visible title, metadata title, Open Graph title, and JSON-LD headline must describe the same page.
- Visible and structured publication/modified dates must come from the same front-matter fields.
- All image URLs must resolve to the image declared in front matter or an explicit site fallback.
- A page marked `noindex` must be excluded from the sitemap and cannot be presented as a canonical content result.
- Never add FAQ, HowTo, Review, Dataset, or Person markup unless the corresponding content and entity are visibly present.

## Acceptance criteria

- [ ] Every indexable page has one title, one meta description, one canonical, one robots policy, and coherent Open Graph/Twitter metadata.
- [ ] Every article emits a valid Article-subtype JSON-LD object with headline, canonical URL, author, publication date, modified date, and image.
- [ ] Home, About, articles, collections, and projects use the same WebSite and Person `@id` values without conflicting duplicate entities.
- [ ] Every Article has stable `<canonical>#article` and breadcrumb `<canonical>#breadcrumb` identifiers and references the canonical Person and WebSite.
- [ ] No generated metadata URL uses `http://nikgo.com`, a repository hostname, or a raw Markdown URL.
- [ ] Each article's social image is explicit, absolute after rendering, and includes width, height, and alt metadata where supported.
- [ ] Breadcrumb JSON-LD exactly matches visible breadcrumb order and URLs.
- [ ] `{% seo %}` is absent after the project-owned include is active, and no page contains conflicting duplicate Article, canonical, robots, or Open Graph values.
- [ ] Schema validators report no syntax errors or missing required Article properties.

## Verification

```bash
bundle exec jekyll build --trace
rg -n 'http://nikgo\.com|github\.io|\.md(["?#]|$)' _site --glob '*.html'
```

Parse every generated HTML head and JSON-LD block in CI. Sample the homepage, article index, one topic hub, one standard article, one research article, About, and 404 in Schema.org Validator and the applicable Google Rich Results Test. Social-debug one article with LinkedIn and other owner-used preview tools after deployment.

## Out of scope

- Writing the About page and Person profile; SEO-007.
- Creating image variants; SEO-013.
- Adding unsupported rich-result types solely to attract search features.

## Rollback

Restore the prior `{% seo %}` baseline only as a complete rollback of the custom head include. Never run the old plugin graph and the new entity graph together.
