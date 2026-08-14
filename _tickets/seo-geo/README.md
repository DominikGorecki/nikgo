# SEO/GEO implementation ticket bundle

This directory decomposes [`SEO-GEO-IMPROVEMENT-SPEC.md`](../../SEO-GEO-IMPROVEMENT-SPEC.md) into independently executable implementation tickets for the current nikGo website.

The directory begins with `_`, so Jekyll ignores it. The ticket files must not be copied into `_site` or become public pages.

## Verified platform constraints

- Hosting: GitHub Pages behind the `nikgo.com` custom domain and Cloudflare edge.
- Publishing model: repository source on `master`; no custom deployment workflow is present. Ticket SEO-001 must confirm the GitHub Pages setting is `master` / repository root before implementation begins.
- Dependency bundle: `github-pages` 232.
- Jekyll: 3.10.0.
- Liquid: 4.0.4.
- Theme: `jekyll-theme-cayman` 0.2.0 with a repository-owned `_layouts/default.html` override.
- Supported relevant plugins already contained in the locked `github-pages` bundle:
  - `jekyll-seo-tag` 2.8.0
  - `jekyll-sitemap` 1.4.0
  - `jekyll-redirect-from` 0.16.0
  - `jekyll-feed` 0.17.0
  - `jekyll-optional-front-matter` 0.3.2
  - `jekyll-relative-links` 0.6.1
  - `jekyll-titles-from-headings` 0.5.3
- `_site` is generated output and is ignored by Git. It must not be committed.
- GitHub Pages branch builds run in safe mode. Tickets must not add `_plugins/`, arbitrary Ruby plugins, `.htaccess`, server middleware, or assumptions about configurable response headers.
- The existing public article `.html` URLs are preserved during the foundational migration. Clean URL migration is intentionally deferred because branch-hosted GitHub Pages cannot provide guaranteed HTTP 301 redirects. `jekyll-redirect-from` produces static redirect documents, not server-side 301 responses.
- `CNAME` must remain `nikgo.com`.
- The source spec audited 26 published Markdown article files. The current worktree also contains the untracked `pages/articles/Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md`; SEO-002 treats it as a 27th candidate requiring an explicit publish/archive decision and does not assume it is live.

## Global implementation rules

Every ticket must leave the site buildable and deployable on the current GitHub Pages setup. Implementers must:

1. Read this index, the target ticket, and its dependencies.
2. Build with the locked `github-pages` bundle, not a globally installed or latest Jekyll version.
3. Preserve unrelated user content and current public URLs unless the ticket contains an approved URL disposition.
4. Use only GitHub Pages-supported plugins listed in the lockfile.
5. Generate metadata from front matter rather than duplicating it by hand across layouts and indexes.
6. Treat `_site` as disposable build output.
7. Validate generated HTML, not only source Liquid/Markdown.
8. Use absolute `https://nikgo.com` URLs for canonicals, Open Graph, structured data, robots, and sitemap output.
9. Never claim a server-side status code that GitHub Pages cannot emit.
10. Keep content and structured data facts identical and evidence-based.
11. Do not add `llms.txt`, special AI markup, or machine-only text as a substitute for crawlability, evidence, and human-readable content.

## Recommended implementation order

| Order | Ticket | Priority | Effort | Depends on |
|---:|---|---|---|---|
| 1 | [SEO-001 — Reproducible GitHub Pages build](SEO-001-reproducible-github-pages-build.md) | P0 | M | None |
| 2 | [SEO-002 — Search baseline and content disposition](SEO-002-baseline-content-disposition.md) | P0 | M | None |
| 3 | [SEO-003 — Canonical article collection migration](SEO-003-canonical-article-collection.md) | P0 | XL | SEO-001, SEO-002 |
| 4 | [SEO-004 — Site identity, sitemap, and robots](SEO-004-site-identity-sitemap-robots.md) | P0 | M | SEO-001, SEO-003 |
| 5 | [SEO-005 — Semantic article layout](SEO-005-semantic-article-layout.md) | P0 | L | SEO-003, SEO-004 |
| 6 | [SEO-006 — SEO/social metadata and structured data](SEO-006-article-metadata-schema-social.md) | P0 | L | SEO-004, SEO-005 |
| 7 | [SEO-007 — Author entity and trust pages](SEO-007-author-trust-entity.md) | P0 | M | SEO-005, SEO-006 |
| 8 | [SEO-008 — Collection-driven index and topic hubs](SEO-008-article-index-topic-hubs.md) | P0 | L | SEO-003, SEO-005 |
| 9 | [SEO-009 — Internal linking and related content](SEO-009-internal-linking-related-content.md) | P1 | L | SEO-008 |
| 10 | [SEO-010 — Research provenance and PDF treatment](SEO-010-research-provenance-pdf.md) | P0 | XL | SEO-006, SEO-007, SEO-009 |
| 11 | [SEO-011 — Agentic engineering GEO upgrades](SEO-011-agentic-engineering-geo-refresh.md) | P1 | XL | SEO-007, SEO-008, SEO-009 |
| 12 | [SEO-012 — Cognition and society GEO upgrades](SEO-012-cognition-society-geo-refresh.md) | P1 | XL | SEO-007, SEO-008, SEO-009 |
| 13 | [SEO-013 — Article images, Discover, and social cards](SEO-013-image-discover-social-assets.md) | P1 | L | SEO-005, SEO-006 |
| 14 | [SEO-014 — Performance optimization](SEO-014-performance-core-web-vitals.md) | P1 | L | SEO-005, SEO-013 |
| 15 | [SEO-015 — Accessibility and browser-agent semantics](SEO-015-accessibility-agent-semantics.md) | P1 | L | SEO-005 |
| 16 | [SEO-016 — Custom 404 and domain redirects](SEO-016-custom-404-domain-redirects.md) | P1 | M | SEO-004 |
| 17 | [SEO-017 — CI SEO quality gates](SEO-017-ci-seo-quality-gates.md) | P0 | XL | SEO-001, SEO-003–SEO-006, SEO-008–SEO-009, SEO-013–SEO-016 |
| 18 | [SEO-018 — Webmaster tools, analytics, and GEO measurement](SEO-018-webmaster-analytics-geo-measurement.md) | P0 | L | SEO-002, SEO-004, SEO-007, SEO-014, SEO-016, SEO-017 |
| 19 | [SEO-019 — IndexNow publishing notifications](SEO-019-indexnow-post-publish.md) | P1 | M | SEO-004, SEO-017, SEO-018 |
| 20 | [SEO-020 — External entity consistency and distribution](SEO-020-external-entity-distribution.md) | P1 | L | SEO-007, SEO-010–SEO-012 |
| 21 | [SEO-021 — Demand-led companion resources](SEO-021-demand-led-companion-resources.md) | P2 | XL per batch | SEO-008–SEO-012, SEO-018 |
| 22 | [SEO-022 — Editorial freshness and maintenance](SEO-022-editorial-maintenance-runbook.md) | P1 | L + recurring | SEO-017, SEO-018 |

Tickets with no mutual dependency may be worked in parallel, but the order above is the safest one-by-one rollout.

## Specification coverage matrix

| Spec requirement | Primary ticket(s) |
|---|---|
| P0-1 robots policy | SEO-004 |
| P0-2 canonical XML sitemap | SEO-004 |
| P0-3 eliminate raw Markdown | SEO-003 |
| P0-4 resolve alternates/drafts/orphans | SEO-002, SEO-003 |
| P0-5 remove test and artifacts; branded 404 | SEO-003, SEO-016 |
| P1-6 one-hop domain redirects | SEO-016 |
| P0-7 explicit site identity | SEO-004 |
| P0-8 explicit article front matter | SEO-003 |
| P0-9 unique titles and descriptions | SEO-003, SEO-006 |
| P0-10 HTTPS metadata | SEO-004, SEO-006 |
| P0-11 article layout | SEO-005 |
| P0-12 one H1 | SEO-005 |
| P1-13 semantic navigation | SEO-015 |
| P1-14 generated article index | SEO-008 |
| P0-15 reusable entity graph | SEO-006, SEO-007 |
| P1-16 topic hubs | SEO-008 |
| P1-17 internal-link rules | SEO-009 |
| P1-18 author/about page | SEO-007 |
| P1-19 answerable openings | SEO-010, SEO-011, SEO-012 |
| P1-20 explicit attributable claims | SEO-010, SEO-011, SEO-012 |
| P1-21 research provenance | SEO-010 |
| P1-22 recurring term definitions | SEO-008, SEO-011, SEO-012 |
| P1-23 evidence-rich formats | SEO-010, SEO-011, SEO-012 |
| P2-24 companion pages | SEO-021 |
| P2-25 external corroboration | SEO-020 |
| P1-26 standard cover assets | SEO-013 |
| P1-27 image loading rules | SEO-013 |
| P2-28 image provenance | SEO-007, SEO-013 |
| P1-29 page-weight reduction | SEO-014 |
| P1-30 resilient animation | SEO-014, SEO-015 |
| P1-31 editorial/trust signals | SEO-007, SEO-022 |
| P1-32 publication QA | SEO-017, SEO-022 |
| Search/GEO measurement | SEO-018 |
| IndexNow | SEO-019 |

## Completion rule

The implementation program is complete only when all finite tickets are accepted, the recurring tickets have an owner and documented cadence, and the final generated/live-site checks in SEO-017 and SEO-018 pass. Completing only the template or metadata tickets is not full implementation.
