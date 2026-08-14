# SEO-012 — Refresh the cognition, attention, society, and health cluster for GEO

- **Priority:** P1
- **Effort:** XL
- **Status:** Ready after SEO-007 through SEO-009
- **Dependencies:** SEO-007, SEO-008, SEO-009
- **Blocks:** SEO-017, SEO-018, SEO-021
- **Spec coverage:** P1-19, P1-20, P1-22, P1-23, P1-31

## Outcome

The cognition and society essays become clear, responsibly sourced answers that preserve their argumentative voice while separating evidence, analogy, speculation, and high-stakes health implications.

## Current-state evidence

- The cluster includes attention, outrage, freedom, medicine/health, Roko's basilisk, labor disruption, and public-learning themes.
- Philosophical claims, empirical claims, analogies, and forecasts are not always labeled distinctly.
- Medical and cognitive claims require a higher evidence and qualification standard than ordinary opinion content.
- At least one reference list has duplicate numbering and several concepts span articles without a canonical definition path.

## GitHub Pages compatibility constraints

- Preserve current article URLs and use collection front matter/layouts.
- Use accessible Markdown/HTML for warnings, definitions, citations, tables, and figures; do not hide necessary qualifications in hover interactions.
- Do not use schema types implying medical review, professional credentials, or factual status that the visible page does not support.
- Render any scenario label and health disclaimer server-side so it is available to crawlers and browser agents.

## Article scope

Audit and refresh the applicable canonical articles, including:

- `attention_is_fundamental.md`.
- `ai_after_the_outrage_machine.md`.
- `what_freedom_for__v2.md` plus any unique material approved for merging from `what_freedom_for.md`.
- `medicines_dead_time.md`.
- `Rokos_Symbiotic_Carrot.md`.
- `great-ai-pink-slip-panic.md`.
- `ai_public_opinion_cliff.md`, if approved for publication.
- Other cognition/society pages identified in SEO-002.

## Implementation scope

### 1. Establish answer and argument structure

For each article, define the primary question, thesis, evidence type, intended reader, and key limitation. Make the opening answerable and add descriptive headings that distinguish:

- What is empirically observed.
- What the author infers.
- What is philosophical argument or analogy.
- What is forecast/speculative scenario.
- What the reader can reasonably do.

### 2. Verify evidence at the appropriate standard

- Prefer systematic reviews, consensus statements, original studies, and official public data for health/cognitive claims.
- Describe study population, effect size, limitations, and publication date when a single result carries an important conclusion.
- Do not generalize from animal, lab, correlational, or narrow-population findings without qualification.
- Verify technical analogies, including any quantum/computing comparison, with an authoritative source and state where the analogy stops.
- Distinguish a thought experiment such as Roko's basilisk from a demonstrated AI risk.
- Correct duplicate citation labels and add sources close to the claims they support.

### 3. Apply high-stakes content safeguards

For medical/health material:

- State the author's actual expertise boundary.
- Add a concise informational-not-medical-advice notice near the first actionable section.
- Avoid diagnosis, treatment promises, individualized dosing, or instructions unsupported by a qualified review.
- Give readers an appropriate path to professional or emergency resources when the topic warrants it.
- Record author or qualified-review approval and visible review date.

These safeguards do not substitute for accurate sources and must not be used to preserve a misleading claim.

### 4. Improve extractability without flattening voice

- Add a concise definition for central concepts and link to a canonical definition page.
- Use self-contained key observations, comparison tables, or argument maps only where they clarify reasoning.
- State counterarguments and unresolved questions.
- Keep memorable original examples, but label invented examples as hypothetical.
- Ensure a quoted/extracted paragraph retains its qualifying language.

### 5. Connect and classify

Apply the SEO-008 taxonomy, link to the cognition/society hub, and add contextual/related links per SEO-009. Connect to agentic-work articles only when there is a substantive conceptual bridge.

## Acceptance criteria

- [ ] Each in-scope article exposes a clear primary question, thesis, evidence type, and limitation.
- [ ] Empirical fact, author inference, analogy, forecast, and fiction/scenario are visibly distinguishable.
- [ ] Medical/health claims have current authoritative support, scope qualification, author-boundary disclosure, and review date.
- [ ] No page implies medical, scientific, or professional authority the author does not hold.
- [ ] Thought experiments and future scenarios are labeled before the reader encounters their claims.
- [ ] Citation markers are unique and every important factual claim has an appropriate nearby source.
- [ ] Each page has one canonical topic path plus useful contextual and related links.
- [ ] Extractable summaries preserve uncertainty and do not turn nuanced claims into absolutes.

## Verification

Maintain a claim ledger with columns for claim, claim type, source, source date, qualification, and reviewer. Independently review all medical/health passages and technical analogies. Test the built pages with citations, warning blocks, headings, images, and schema. Re-check high-stakes pages at the cadence defined in SEO-022.

## Out of scope

- Personalized medical advice.
- Unverified publication of the AI public-learning cliff draft.
- Schema that asserts medical review or scholarly status without evidence.

## Rollback

If a high-stakes claim cannot be verified, remove or clearly suspend it; do not restore the older unsupported version. Revert stylistic edits independently from factual corrections.
