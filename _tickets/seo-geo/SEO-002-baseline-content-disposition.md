# SEO-002 — Record search baselines and approve article dispositions

- **Priority:** P0
- **Effort:** M
- **Status:** Requires site-owner/editor input
- **Dependencies:** None
- **Blocks:** SEO-003 and any content ticket
- **Spec coverage:** P0-4, publication dates, measurement baseline

## Outcome

Every current article/version has an approved disposition, canonical URL, publication date, modification date, title, description, category, and indexability state before files are moved. Search and AI visibility are exported before technical changes so impact can be measured.

## Why this is a separate ticket

Code cannot reliably infer whether a draft is unpublished, superseded, or a distinct article. Git history also does not necessarily equal original publication history. These are editorial decisions. SEO-003 must not delete, redirect, or canonicalize content based only on filename similarity.

## Current-state evidence

- There are 27 article Markdown files but only 18 Markdown articles in “All Articles,” plus one PDF.
- Three files are explicitly `__no_ref` derivatives.
- Three `ai_in_the_veins_v*` versions are live and unlisted.
- Both `what_freedom_for.md` and `what_freedom_for__v2.md` are live; v2 is linked.
- `ai_public_opinion_cliff.md` is live but unlisted.
- `/b/test.html` is a live default Jekyll test page.
- Dates are hard-coded in `pages/articles.md`, usually without a day, and do not appear on article pages.
- The article index misspells `Dominik` as `Domink` once.

## GitHub Pages compatibility constraints

- This ticket records decisions and read-only external baselines; it must not change Pages settings, source paths, permalinks, or dependencies.
- Use the current production URL behavior as evidence, including the raw Markdown copies emitted by the GitHub Pages plugin set.
- Git history is evidence only. Jekyll/GitHub Pages does not supply reliable original-publication metadata, so dates require editorial approval.
- Keep private webmaster exports outside the public repository and outside any directory Jekyll could publish.
- Preserve `CNAME` and the current article `.html` paths until SEO-003 applies the approved disposition map.

## Implementation scope

### 1. Export the pre-change baseline

From Google Search Console, export the previous 90 days and maximum available comparison period:

- Pages/indexing report.
- Submitted/discovered sitemap state.
- Search results by page and query: impressions, clicks, CTR, and average position.
- Google-selected canonical for every existing article HTML and Markdown URL that has data.
- Core Web Vitals by template if available.
- Generative AI performance report if available.

From Bing Webmaster Tools, export:

- Indexed pages and crawl errors.
- Search performance and backlinks.
- AI Performance citations, cited pages, and grounding-query samples if available.

Record current observable referrals from search/AI sources if analytics already exists. Do not install analytics in this ticket.

Store private exports outside the public Jekyll source. Do not commit account data, search queries containing personal data, verification tokens, or analytics identifiers.

### 2. Approve the disposition inventory

For every file below, record `publish`, `redirect`, `archive`, or `publish-after-edit`:

#### Listed canonical candidates

- `2028_intelligence_explosion.md`
- `90_percent_problem_of_agentic_SWE.md`
- `Market_for_Portable_Minds.md`
- `OODA_faster.md`
- `Rokos_Symbiotic_Carrot.md`
- `SWE-own-your-own-ai.md`
- `Why_Office_Agents_Shouldnt_Live_in_a_Shell.md`
- `ai_after_the_outrage_machine.md`
- `attention_is_fundamental.md`
- `dose_response_curve_for_RAG__wp.md`
- `great-ai-pink-slip-panic.md`
- `medicines_dead_time.md`
- `rag_as_a_capability_multiplier.md`
- `small_RAG_beats_large_large_search.md`
- `vibe-v-agentic-swe.md`
- `what_freedom_for__v2.md`
- `wrong_kind_of_smart.md`
- `your_ai_career_plan.md`

#### Unlisted/alternate candidates requiring explicit decisions

- `Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md`
- `Rokos_Symbiotic_Carrot__no_ref.md`
- `Why_Office_Agents_Shouldnt_Live_in_a_Shell__no_ref.md`
- `wrong_kind_of_smart__no_ref.md`
- `ai_in_the_veins_v1.md`
- `ai_in_the_veins_v2.md`
- `ai_in_the_veins_v3.md`
- `what_freedom_for.md`
- `ai_public_opinion_cliff.md`

Expected default, subject to owner confirmation:

- Archive/remove the three `__no_ref` copies from production.
- Keep `what_freedom_for__v2` as canonical and redirect/archive v1 after merging any unique value.
- Compare all three “AI in the Veins” versions with `OODA_faster`; do not assume they are duplicates solely from topic/title.
- Either intentionally publish `ai_public_opinion_cliff` with complete metadata or archive it.
- Remove the test post from production.

### 3. Create an authoritative metadata sheet

For every item marked `publish`, approve:

- Display title.
- Unique one- or two-sentence description.
- Exact current public HTML permalink to preserve.
- Publication date in `YYYY-MM-DD`.
- Material modification date in `YYYY-MM-DD`.
- Author key (`dominik-gorecki`).
- Category: `agentic-engineering`, `rag-research`, or `ai-cognition-society`.
- Tags.
- Representative image path and accurate alt text.
- `featured` state and feature order, if any.
- Related-article candidates.
- Whether the page is an essay, blog post, research article, or PDF landing page.

Use Git history as evidence, not as an automatic publication date. Resolve date conflicts with the author.

### 4. Approve URL policy

For the foundational implementation:

- Preserve every approved article's existing `.html` URL exactly, including case and underscores.
- Do not migrate to clean `/articles/slug/` URLs on branch-based GitHub Pages.
- Use `jekyll-redirect-from` only for approved alternate HTML paths, with the documented limitation that it emits static redirect documents rather than HTTP 301 responses.
- Raw `.md` URLs will be allowed to become true 404s after collection migration.

## Acceptance criteria

- [ ] Search/Bing baselines are exported or the absence of account access is explicitly recorded.
- [ ] All 27 Markdown files have one approved disposition.
- [ ] Every published page has complete approved metadata.
- [ ] Every redirect has exactly one target and a reason.
- [ ] No meaningfully distinct page is redirected only because its title/topic is similar.
- [ ] Publication and modification dates are author-approved.
- [ ] The URL-preservation policy is approved.
- [ ] The `Domink` typo is included in the correction list.
- [ ] Private exports and verification tokens are not committed.

## Verification

Review the disposition and metadata sheet against:

```bash
find pages/articles -maxdepth 1 -name '*.md' -print | sort
rg -n '^### \[' pages/articles.md
git log --follow --format='%cs %h %s' -- pages/articles/<file>.md
```

The count of disposition rows must equal the count of article Markdown files.

## Out of scope

- Moving or deleting files.
- Implementing redirects.
- Rewriting article copy.
- Installing analytics.

## Rollback

This is a decision/data ticket. If a decision changes before SEO-003 merges, update the approved inventory. After migration, disposition changes require a new redirect/canonical review.
