# SEO-010 — Strengthen research provenance, citations, and the PDF landing path

- **Priority:** P0
- **Effort:** XL
- **Status:** Ready after SEO-006, SEO-007, and SEO-009
- **Dependencies:** SEO-006, SEO-007, SEO-009
- **Blocks:** SEO-017, SEO-018, SEO-020, SEO-021
- **Spec coverage:** P0-15, P1-19, P1-20, P1-21, P1-23, P2-25

## Outcome

The site's original research becomes independently interpretable and citable: claims are tied to methods and sources, uncertainty is explicit, and the AI tokenomics PDF has an indexable HTML discovery page without duplicating the paper.

## Current-state evidence

- The corpus includes RAG experimentation, small-RAG analysis, a dose-response article, and an AI tokenomics PDF.
- Research pages often lead with narrative before stating a compact research question, method, sample, result, and limitation.
- Dataset/code availability, model/version dates, conflicts, and citation instructions are inconsistent.
- The PDF is linked directly from the article index and has no dedicated HTML landing page with descriptive metadata.
- GitHub Pages cannot set a canonical HTTP header on a static PDF.

## GitHub Pages compatibility constraints

- Keep research pages in the canonical article collection with explicit legacy permalinks.
- Use visible HTML sections and front matter; do not depend on a scholarly publishing plugin.
- GitHub Pages cannot add `Link: rel="canonical"` or `X-Robots-Tag` headers to one PDF. Treat the HTML landing page as the discovery/citation hub and make an explicit indexing decision for the PDF.
- `ScholarlyArticle` is permitted only when the visible page actually includes scholarly authorship, method, results, and citation details.

## Implementation scope

### 1. Inventory and verify research artifacts

Cover at least:

- `rag_as_a_capability_multiplier.md`.
- `small_RAG_beats_large_large_search.md`.
- `dose_response_curve_for_RAG__wp.md`.
- `SWE_LLM_Tokenomecs_V2.pdf` and any source/companion files.

For each, create a claim/source worksheet listing the research question, population/corpus, sample size, collection period, tools/models and versions, metrics, analysis method, primary findings, uncertainty, limitations, available data/code, and all external sources. Record `unknown` rather than inferring missing methodology.

### 2. Apply a visible research structure

Where the content supports it, add:

1. Abstract or executive summary.
2. Research question and scope.
3. Key findings with numbers and uncertainty in context.
4. Methods, sample, model/version, and evaluation details.
5. Results with accessible tables/figures.
6. Limitations and plausible alternative explanations.
7. Practical implications that do not overstate causality.
8. Data/code/materials availability.
9. Conflicts, funding, and AI-assistance disclosure.
10. How to cite and complete references.

Use stable section IDs for answer extraction. Keep the author's voice; do not flatten every paper into the same generic template.

### 3. Audit claims and references

- Prefer primary papers, official specifications, source repositories, and first-party datasets.
- Attach a citation close to each non-obvious factual claim.
- Preserve the distinction between measured result, author interpretation, and proposed hypothesis.
- State exact dates and model versions for time-sensitive results.
- Verify mathematical notation, sample counts, percentages, table totals, and figure labels.
- Do not invent a DOI, institutional affiliation, peer-review status, dataset URL, benchmark, confidence interval, or source.
- If data/code cannot be released, say so plainly and explain the boundary without implying reproducibility.

### 4. Add citation metadata

Add approved fields such as:

```yaml
citation_title: "Full research title"
citation_author: "Dominik Gorecki"
citation_publication_date: 2026-01-15
citation_pdf_url: /assets/papers/example.pdf
```

Render a copyable plain-text citation and, when accurate, BibTeX. Use `seo.type: ScholarlyArticle` only for qualifying pages and ensure visible values match JSON-LD. Add `Dataset` markup only for a real, accessible dataset described on the page.

### 5. Create the AI tokenomics HTML landing page

Create a canonical article landing page, for example `/pages/articles/ai-tokenomics-for-software-engineering.html`, containing:

- Unique title and description.
- Abstract, named author, publication and modified dates.
- Key findings and a table of contents or section overview.
- Clear PDF download link with file type and size.
- Citation text, methodology summary, limitations, and related research.
- `ScholarlyArticle` metadata only if the paper qualifies.

Do not paste the entire PDF into the page. Keep the PDF URL stable, link back to the HTML landing page within the PDF on its next revision if source is available, and decide/document whether the PDF remains in the sitemap.

## Acceptance criteria

- [ ] Every covered research page states its question, method, sample/corpus, dates/versions, key results, and limitations or explicitly identifies unavailable information.
- [ ] Numeric key findings match the body, tables, figures, and cited source data.
- [ ] Every citation resolves and no reference is duplicated, orphaned, or represented as primary when it is secondary.
- [ ] Data/code/materials availability and conflicts/AI assistance are stated accurately.
- [ ] Qualifying pages expose valid ScholarlyArticle metadata that agrees with visible content.
- [ ] The PDF has one canonical HTML landing page with an explicit download link, citation, abstract, and related links.
- [ ] Search/index pages link to the HTML landing page as the primary entry, while the PDF remains directly accessible.
- [ ] No unsupported credential, affiliation, DOI, peer-review claim, or reproducibility claim is introduced.

## Verification

- Independently recalculate a sample of reported percentages, counts, and table totals.
- Open every citation and record access failures for editorial resolution.
- Validate schema and compare its values field-by-field with the visible page.
- Request both the HTML landing page and PDF locally and after deployment.
- Have the author approve the methods, limitations, availability statement, citation, and AI-use disclosure.

## Out of scope

- Re-running an experiment whose data/code is unavailable; create a follow-up research ticket if needed.
- Claiming formal peer review.
- Server-level PDF headers unavailable on GitHub Pages.

## Rollback

Content corrections should be forward-fixed with a visible modified date. If a central result is invalid, add a clear correction/retraction note rather than silently restoring the old claim.
