# SEO-022 — Establish the ongoing SEO, GEO, and editorial maintenance runbook

- **Priority:** P1
- **Effort:** L initial, recurring thereafter
- **Status:** Ready after SEO-017 and SEO-018
- **Dependencies:** SEO-017, SEO-018
- **Blocks:** None
- **Spec coverage:** P1-31, P1-32, measurement cadence, maintenance, and governance

## Outcome

Technical health, source quality, entity consistency, content freshness, and generative-answer accuracy remain owned and reviewable after the implementation project ends.

## Current-state evidence

- The site has no documented publication checklist, content review cadence, correction log, redirect register, or deprecation process.
- Dates and metadata are currently inconsistent and can become stale without a deliberate workflow.
- Several topics—models, AI products, work forecasts, health/cognition research, and external profiles—change materially over time.
- SEO/GEO outcomes require repeated measurement rather than a one-time launch audit.

## GitHub Pages compatibility constraints

- Store safe runbooks/templates in repository Markdown outside published collections, preferably under `_docs/` or another ignored underscore directory.
- Keep private account details, personal contacts, raw query exports, and user-level analytics outside the public repository.
- Use the CI checks from SEO-017 for every content change; do not bypass the locked build for editorial-only updates.
- Update front-matter dates explicitly from substantive review evidence; never use build time or Git commit time to make content appear fresh.

## Implementation scope

### 1. Add a publication checklist

Require before every new/updated canonical page:

- Approved intent, audience, canonical content ID/permalink, taxonomy, and relationships.
- Unique title/description and accurate answer-first opening.
- Verified author, publish/modified dates, sources, claims, quotations, and links.
- Explicit evidence/interpretation/scenario boundaries.
- Required method, limitation, health, conflict, citation, and AI-use disclosures.
- Image provenance, dimensions, alt, caption/credit, and performance budget.
- Schema/visible-content agreement.
- Local locked build, full CI, mobile/keyboard/accessibility review, and preview approval.
- Sitemap/index/hub inclusion and post-publish verification.

### 2. Establish review tiers and cadence

Suggested maximum cadence:

- Quarterly: medical/health, model/product capabilities, labor/market numbers, forecasts, active research landing pages.
- Twice yearly: agentic engineering guidance, tool comparisons, profiles, policy pages, major topic hubs.
- Annually: durable philosophy/essay content, glossary definitions, image rights/provenance.
- Monthly technical: Search Console/Bing errors, sitemap, robots, security/manual actions, 404s, redirect chains, broken links, Core Web Vitals, CI dependencies.

Assign an owner and next-review date. High-stakes events can trigger earlier review.

### 3. Define update, correction, and retirement rules

- Change `date_modified` and `last_modified_at` only for a substantive reviewed change; keep them equal.
- Add a visible correction note when a material conclusion, number, citation, or safety statement changes.
- Keep a concise correction log with date, page, issue, and resolution.
- If content is superseded, merge into the stronger canonical and update internal/external distribution references.
- If content is invalid with no replacement, return an honest 404/410 where hosting permits; do not redirect unrelated content to Home.
- Retain scenario labels and historical context rather than rewriting past forecasts as if they were always current.

### 4. Run recurring technical and entity audits

- Execute the full CI suite and a live crawl.
- Compare sitemap, indexable canonicals, and Search Console indexed URLs.
- Review new 404s, redirect stubs, scheme/host drift, raw/source leakage, duplicate metadata, malformed schema, and image errors.
- Recheck owned profile URLs, biographies, `sameAs`, author image, and outbound resources.
- Review dependency/security advisories while retaining GitHub Pages compatibility.
- Test representative pages with JavaScript disabled and keyboard/screen-reader smoke tests.

### 5. Run recurring GEO/editorial review

- Repeat the fixed benchmark from SEO-018 and record engine/date/method.
- Audit whether answers cite the canonical page and preserve key qualifications.
- Identify passages that are frequently misquoted or omitted and clarify the visible content when justified.
- Review emerging queries and competitor/result formats for real content gaps.
- Feed validated demand into SEO-021 rather than creating pages ad hoc.
- Track third-party changes without attempting to manipulate or guarantee citations.

### 6. Maintain a decision register

Record major decisions about canonical URLs, archived variants, redirects, robots/AI crawler policy, analytics/privacy, schema types, image licenses, content withdrawals, and external syndication. Each entry needs date, owner, rationale, affected URLs, and rollback/next review.

## Acceptance criteria

- [ ] A repository-safe publication checklist, correction template, review inventory, and decision-register template exist.
- [ ] Every canonical page has an owner, risk tier, and next review date.
- [ ] Monthly/quarterly review responsibilities and escalation paths are assigned.
- [ ] Modified dates change only with substantive review and remain consistent across visible text, schema, and sitemap.
- [ ] Material corrections are visible and logged rather than silently overwritten.
- [ ] Technical audits use the locked build/CI and include live production checks.
- [ ] GEO reviews measure citation accuracy and qualification preservation, not only mentions.
- [ ] Stale/duplicate pages have an explicit update, consolidate, archive, or remove decision.

## Verification

Run one complete simulated publication and one quarterly audit using the new templates. Confirm another maintainer can execute the steps using repository documentation plus owner-held account access. Sample modified dates against Git history/correction notes and confirm no automatic freshness bump.

## Out of scope

- Guaranteed rankings, traffic, backlinks, or AI citations.
- Storing private provider credentials or raw personal data in the repository.
- Automated editorial changes without human review.

## Rollback

The runbook is versioned and should be amended, not discarded, when a step proves impractical. Preserve past decision/correction records when changing future process.
