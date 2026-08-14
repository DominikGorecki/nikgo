# SEO-011 — Refresh the agentic engineering and future-of-work cluster for GEO

- **Priority:** P1
- **Effort:** XL
- **Status:** Ready after SEO-007 through SEO-009
- **Dependencies:** SEO-007, SEO-008, SEO-009
- **Blocks:** SEO-017, SEO-018, SEO-021
- **Spec coverage:** P1-19, P1-20, P1-22, P1-23

## Outcome

The agentic engineering and AI-at-work essays answer well-defined questions with clear definitions, evidence boundaries, quotable original insights, and connected reading paths suitable for human readers and generative retrieval.

## Current-state evidence

- This is the site's largest thematic cluster, but individual essays vary in opening clarity, sourcing, terminology, and internal connectivity.
- Several titles and claims refer to fast-changing model, company, workforce, or 2026-era conditions.
- Core phrases such as agentic engineering, vibe coding, portable minds, and the 90% problem are not yet connected through a canonical definition/hub structure.

## GitHub Pages compatibility constraints

- This is an editorial/front-matter task on the collection created in SEO-003; it must not change existing public permalinks.
- Use Markdown structures Jekyll 3.10 and Kramdown render correctly.
- Footnotes, tables, definition lists, diagrams, and callouts must be tested in the current Cayman-derived CSS.
- Any content-level structured data continues to flow through SEO-006; do not hand-write a second Article graph inside Markdown.

## Article scope

Audit and refresh the applicable canonical articles, including:

- `90_percent_problem_of_agentic_SWE.md`.
- `vibe-v-agentic-swe.md`.
- `OODA_faster.md`.
- `Why_Office_Agents_Shouldnt_Live_in_a_Shell.md`.
- `SWE-own-your-own-ai.md`.
- `your_ai_career_plan.md`.
- `Market_for_Portable_Minds.md`.
- `wrong_kind_of_smart.md`.
- `2028_intelligence_explosion.md`, if retained and published.
- `Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md`, if retained and published.

Resolve exact filenames and canonical URLs from the SEO-002 disposition inventory; do not create a second page when an existing title differs slightly.

## Implementation scope

### 1. Give each page a precise answer target

For every article, document one primary question, the intended reader, the durable takeaway, and the search/generative query family it serves. Rewrite the opening 100–180 words so a reader can understand the answer, thesis, and scope without reading the whole essay.

### 2. Define original concepts canonically

- Add a concise, quotable definition near the first use of each coined or specialized concept.
- State what the concept includes, excludes, and how it differs from neighboring terms.
- Choose one canonical page for each major definition; other pages should summarize and link to it.
- Preserve distinctive phrasing and concrete examples rather than repeating a generic SEO paragraph across the cluster.

### 3. Create extractable evidence blocks

Add only where genuinely useful:

- Key takeaways grounded in the article.
- Decision tables, checklists, stage models, or failure-mode lists.
- Concrete examples with assumptions.
- `What this means in practice` sections.
- Brief counterarguments and limits.

Use descriptive headings phrased around reader questions. Keep important claims in prose, not only in an image.

### 4. Fact-check time-sensitive material

- Verify model names, capabilities, product availability, company statements, employment data, and market figures as of the visible modified date.
- Replace vague relative dates such as `recently` with exact dates when material.
- Prefer first-party documentation, original research, and official statistics.
- Mark forecasts and scenarios explicitly; do not present the 2028 scenario as an observed event.
- Separate the author's prediction from sourced fact.
- Remove stale claims that cannot be substantiated rather than laundering them through an unsourced summary.

### 5. Connect the cluster

- Assign the controlled taxonomy from SEO-008.
- Link each page to the agentic-engineering or future-of-work hub.
- Add contextual links and curated related IDs according to SEO-009.
- Link research evidence from SEO-010 when it directly supports a claim.
- Avoid repeating identical anchor text across every page.

## Acceptance criteria

- [ ] Every in-scope page has one primary question and an opening answer/thesis that is understandable out of context.
- [ ] Every coined/specialized term has one canonical definition page and explicit scope boundaries.
- [ ] Time-sensitive claims show an exact supporting date and source or are clearly labeled as analysis/forecast.
- [ ] Scenario and speculative content is visibly labeled in the title area and metadata, not only in a closing disclaimer.
- [ ] Each page contains at least one genuinely original, self-contained framework, example, or actionable synthesis.
- [ ] Each page links to its hub, at least two relevant articles, and supporting primary evidence where applicable.
- [ ] No article receives FAQ/HowTo schema merely because headings are phrased as questions or steps.
- [ ] Titles, descriptions, image metadata, dates, and article schema pass SEO-006 validation.

## Verification

Use a per-article editorial checklist recording the question, answer paragraph, primary sources, facts checked, definitions, scenario labels, hub, inbound/outbound links, and author approval. Re-read extracted passages without surrounding context to ensure they do not overstate the article. Run the site build and link/schema checks after each batch.

## Out of scope

- Publishing dozens of keyword variations or AI-generated summaries.
- New companion resources selected from post-launch demand; SEO-021.
- External distribution/profile updates; SEO-020.

## Rollback

Commit article refreshes in small thematic batches so factual or stylistic regressions can be reverted per article. Preserve the last verified source and never roll back a disclosed factual correction silently.
