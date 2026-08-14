# SEO-021 — Build demand-led companion resources after measurement

- **Priority:** P2
- **Effort:** XL per resource batch
- **Status:** Gated by 60–90 days of measurement
- **Dependencies:** SEO-008, SEO-009, SEO-010, SEO-011, SEO-012, SEO-018
- **Blocks:** None
- **Spec coverage:** P2-24 and phase-three companion pages

## Outcome

The site earns durable non-branded discovery with a small number of original tools, checklists, glossaries, and implementation guides selected from observed demand—not a scaled collection of thin keyword pages.

## Current-state evidence

- The source spec proposes companion resources such as RAG evaluation guidance, an OODA playbook, an agentic-engineering checklist, and definitions.
- Current query/citation demand is not yet measured; building all candidates now risks duplication and thin programmatic content.
- The existing corpus contains frameworks and research that can support genuinely useful resources once demand and gaps are known.

## GitHub Pages compatibility constraints

- Publish static Markdown/HTML resources using existing collection/layout/include patterns.
- A simple calculator may use progressive-enhancement JavaScript, but its explanation, formula, inputs, and fallback must be server-rendered.
- Do not add a backend, database, arbitrary Jekyll plugin, or unsupported build dependency.
- Every resource needs an explicit permalink, metadata, taxonomy, author, dates, image, and content ID under existing quality gates.

## Entry gate

Do not start a resource until SEO-018 provides at least 60 days of usable data, preferably 90, and the proposal shows:

- A repeated search/GEO question or demonstrated reader need.
- A distinct job not already satisfied by an article or topic hub.
- First-party expertise, research, or a defensible original synthesis.
- A maintenance owner and review cadence.
- A clear internal path to/from supporting articles.

Low volume alone is not disqualifying for a strategic research resource, but the rationale must be documented.

## Candidate backlog

Evaluate, do not automatically publish:

- RAG evaluation checklist and experiment worksheet.
- Small-RAG experiment replication guide.
- Agentic engineering readiness/checklist.
- OODA loop implementation playbook for software teams.
- Vibe coding risk/review checklist.
- AI tokenomics calculator or downloadable assumptions sheet.
- Canonical glossary of agentic engineering, portable minds, BYOAI, and related coined terms.
- Research methods/citation resource for the site's published experiments.

Create a separate implementation sub-ticket for each selected resource with its evidence and definition of done.

## Implementation scope

Apply the following scope independently to each selected resource:

### 1. Establish intent and differentiation

Document the user question, current best-performing site page, competing result types, evidence of demand, and what original utility this page adds. If the answer is just a shorter version of an existing article, improve that article instead.

### 2. Build a complete standalone resource

Include:

- A direct answer/definition and explicit scope.
- The actionable tool, checklist, template, formula, or process in accessible HTML.
- Worked example(s) and common failure modes.
- Assumptions, limitations, version/date, and evidence links.
- A printable/downloadable format only when it adds value.
- Links to the supporting canonical research/articles and back from those pages.

Avoid gated downloads for basic value. If collecting email, that requires a separate privacy/consent decision and service integration.

### 3. Apply metadata and trust standards

Use the existing layout/front-matter contract and only appropriate schema. A checklist does not automatically qualify for HowTo; a glossary does not need FAQ schema. Credit the author, cite sources, and label generated examples or images according to policy.

### 4. Measure and maintain

Define page-specific outcomes before launch: qualified impressions, use/download, assisted navigation, external citations/links, or accurate GEO citation. Review after 30/60/90 days and improve, consolidate, or retire pages that remain duplicative or stale.

## Acceptance criteria

- [ ] Every selected resource has documented query/GEO/user evidence and a distinct job.
- [ ] Each resource contains original practical value beyond an article summary.
- [ ] Content is fully useful without signup and fully discoverable without JavaScript, unless an approved product requirement says otherwise.
- [ ] Assumptions, limits, author, review date, sources, and supporting research are visible.
- [ ] Bidirectional contextual links connect the resource with relevant articles/hubs.
- [ ] The page passes all SEO-017 metadata, schema, link, image, accessibility, and performance gates.
- [ ] No cluster of near-duplicate pages is produced for keyword variations.
- [ ] A post-launch measurement and maintenance decision is recorded.

## Verification

Before implementation, approve the demand brief. Before publication, test the resource task with representative users or a documented walkthrough, verify calculations/examples independently, build/crawl the page, and run the complete CI suite. At review windows, compare actual outcomes to the predeclared goal.

## Out of scope

- Programmatic SEO page generation.
- An email funnel or paid product without a separate product/privacy spec.
- Publishing every candidate regardless of demand or maintenance cost.

## Rollback

If a resource duplicates another page, consolidate the stronger content into one canonical and apply the best available legacy-path disposition. Preserve useful downloadable assets only when their landing page remains accurate.
