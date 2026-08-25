# SEO-002 baseline and content-disposition record

**Captured:** 2026-08-14  
**Production site:** `https://nikgo.com`  
**Repository branch:** `master`  
**Approval state:** Approved by the site owner on 2026-08-14. The dispositions, metadata, dates, redirect target, archive decisions, and URL policy in this record are authoritative inputs for SEO-003.

This file is the reviewable implementation artifact for SEO-002. It records the pre-change public baseline, the complete 27-file inventory, proposed dispositions, and proposed metadata. It does not move, delete, redirect, re-index, or edit article content.

## 1. Baseline access record

### Authenticated search and analytics sources

This workspace has no authenticated access to Google Search Console, Bing Webmaster Tools, or site analytics. Therefore no private performance exports were retrieved or committed.

The following requested baseline data remains unavailable:

- Google page indexing, sitemap, query/page performance, selected canonical, Core Web Vitals, and generative-AI performance exports.
- Bing indexed-page, crawl-error, search-performance, backlink, AI citation, cited-page, and grounding-query exports.
- Search/AI referral data from private analytics.

When access is available, the owner should export both the previous 90 days and the maximum comparison period to a private location outside this repository and outside every Jekyll source directory. Exports must not contain committed queries with personal data, verification tokens, account identifiers, or analytics identifiers.

### Public HTTP baseline

Fresh GET requests against production on 2026-08-14 produced the following baseline:

| Check | Result |
|---|---|
| Current Markdown article files inventoried | 27 |
| Existing article `.html` URLs returning HTTP 200 | 27/27 |
| Existing raw article `.md` URLs returning HTTP 200 | 27/27 |
| `GET /sitemap.xml` | HTTP 404 |
| `GET /b/test.html` | HTTP 200; default “Welcome to Jekyll!” post |
| `GET /robots.txt` | HTTP 200 from Cloudflare-managed content-signals response |
| `HEAD /robots.txt` | HTTP 404 from the origin path |

Cloudflare's generated `robots.txt` response explains `search`, `ai-input`, and `ai-train` content signals but, at capture time, does not state an explicit yes/no value for any of them. SEO-004 owns the durable repository policy and must account for Cloudflare's edge behavior.

The public article index contains the `Domink Gorecki` misspelling on the Dose-Response article. It also labels that article as 2025, while the article body says January 2026 and the earliest repository commit is 2026-01-08. Both are correction/approval items below.

## 2. Proposed disposition inventory

The row count is authoritative for the current worktree: 27 Markdown source files. `publish-after-edit` means the article remains distinct but must not enter the canonical collection until its proposed title, metadata, references, and presentation are approved. Archive and redirect actions are deferred to SEO-003.

| # | Source file | Proposed disposition | Redirect target | Indexability after SEO-003 | Evidence and reason |
|---:|---|---|---|---|---|
| 1 | `2028_intelligence_explosion.md` | publish | — | index | Listed article; distinct BYOAI macro memo. |
| 2 | `90_percent_problem_of_agentic_SWE.md` | publish | — | index | Listed article; distinct software-delivery thesis. |
| 3 | `Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md` | publish | — | index | Listed in the current index and present on production; preserve the existing URL. The article and four images remain unrelated untracked work and are not modified by SEO-002. |
| 4 | `Market_for_Portable_Minds.md` | publish | — | index | Listed article; distinct portable-context and labor-market thesis. |
| 5 | `OODA_faster.md` | publish | — | index | Listed, edited 814-word article focused on OODA velocity and the Company Context Bank. |
| 6 | `Rokos_Symbiotic_Carrot.md` | publish | — | index | Listed referenced/image-complete version. |
| 7 | `Rokos_Symbiotic_Carrot__no_ref.md` | archive | — | noindex/404 | Explicit no-reference derivative; 16 additions and 27 deletions relative to the listed version, with no distinct search intent. |
| 8 | `SWE-own-your-own-ai.md` | publish | — | index | Listed article; distinct personal-AI ownership thesis. |
| 9 | `Why_Office_Agents_Shouldnt_Live_in_a_Shell.md` | publish | — | index | Listed referenced/image-complete version. |
| 10 | `Why_Office_Agents_Shouldnt_Live_in_a_Shell__no_ref.md` | archive | — | noindex/404 | Explicit no-reference derivative; materially shorter than the listed version and not a distinct article. |
| 11 | `ai_after_the_outrage_machine.md` | publish | — | index | Listed article; distinct social-technology thesis. |
| 12 | `ai_in_the_veins_v1.md` | archive | — | noindex/404 | Early 1,374-word draft. Harvest any unique citations before archiving; do not redirect it solely because it discusses OODA. |
| 13 | `ai_in_the_veins_v2.md` | publish-after-edit | — | index after edit | The strongest and longest version at 2,775 words. It contains a detailed orchestration, retrieval, reusable-agent, and memory-layer playbook that is not present in the 814-word OODA article. Publish under a distinct approved title. |
| 14 | `ai_in_the_veins_v3.md` | archive | — | noindex/404 | Compressed 1,439-word revision of the v2 argument. Harvest unique phrasing/citations into v2 before archiving; do not redirect to OODA. |
| 15 | `ai_public_opinion_cliff.md` | publish-after-edit | — | index after edit | A 3,483-word distinct public-legitimacy and medical-breakthrough thesis. Add references, cover image, and approved metadata before publication. |
| 16 | `attention_is_fundamental.md` | publish | — | index | Listed article; distinct attention-allocation thesis. |
| 17 | `dose_response_curve_for_RAG__wp.md` | publish | — | index | Listed research article; date conflict requires approval. |
| 18 | `great-ai-pink-slip-panic.md` | publish | — | index | Listed article; distinct labor-displacement thesis. |
| 19 | `medicines_dead_time.md` | publish | — | index | Listed article; distinct medical-latency thesis. |
| 20 | `rag_as_a_capability_multiplier.md` | publish | — | index | Listed research article with controlled experiments. |
| 21 | `small_RAG_beats_large_large_search.md` | publish | — | index | Listed follow-up research article comparing domain RAG with search grounding. |
| 22 | `vibe-v-agentic-swe.md` | publish | — | index | Listed article; distinct engineering-practice thesis. |
| 23 | `what_freedom_for.md` | redirect | `/pages/articles/what_freedom_for__v2.html` | redirect document | The index already selects v2. Both files have the same heading structure, but v1 is about 600 words longer and contains unique phrasing; review/merge unique value before redirecting. One target only. |
| 24 | `what_freedom_for__v2.md` | publish | — | index | Current listed and edited canonical candidate. |
| 25 | `wrong_kind_of_smart.md` | publish | — | index | Listed referenced/image-complete version. |
| 26 | `wrong_kind_of_smart__no_ref.md` | archive | — | noindex/404 | Explicit no-reference derivative with the same thesis and no distinct search intent. |
| 27 | `your_ai_career_plan.md` | publish | — | index | Listed article; distinct personal-practice thesis. |

### Non-article cleanup decision

| Source | Proposed disposition | Reason |
|---|---|---|
| `_posts/b/2015-11-17-test.markdown` | archive/remove from production in SEO-003 | Default Jekyll test post; no editorial value and currently returns HTTP 200 at `/b/test.html`. |

## 3. Alternate-version comparison

### Explicit `__no_ref` derivatives

The three `__no_ref` files share the same titles and core arguments as their listed counterparts. They remove or rewrite references/images rather than serving distinct search intent. The proposed action is archive, not redirect, because SEO-003 is intended to remove raw duplicate publication and these URLs have never been intentionally linked as canonical pages.

### “What Freedom Is For”

Both versions have the same complete heading structure and use the same four images. V2 is an extensive line edit rather than an unrelated article: the diff contains 91 additions and 283 deletions, and v2 is approximately 600 words shorter. V1 nevertheless contains unique passages. SEO-003 must preserve v2's current `.html` URL, perform a final unique-value review, and create exactly one static redirect document from the v1 HTML path to v2.

### “AI in the Veins” and “The Companies That OODA Faster”

The four files were compared by structure and content, not title alone:

| File | Approximate words | Distinguishing content |
|---|---:|---|
| `ai_in_the_veins_v1.md` | 1,374 | Early continuous-form draft with references. |
| `ai_in_the_veins_v2.md` | 2,775 | Full implementation playbook: orchestration, enterprise retrieval, reusable narrow use cases, and a layered Company Context Bank. |
| `ai_in_the_veins_v3.md` | 1,439 | Compressed revision of the v2 playbook. |
| `OODA_faster.md` | 814 | Short, image-backed, edited executive argument about OODA velocity and durable context. |

V2 has enough unique implementation value to remain a separate candidate. It should not redirect to `OODA_faster.html`. To prevent competing same-topic pages, v2 needs a differentiated title and framing before publication; v1 and v3 should be mined for unique evidence and then archived.

### “AI’s Public-Opinion Cliff”

This file is a substantial standalone essay, not an alternate of another article. It is proposed as `publish-after-edit`, with missing references and representative artwork completed before indexing.

## 4. Proposed canonical metadata

The following 21 rows cover every `publish` and `publish-after-edit` item. Dates are proposed from the earliest and latest relevant repository commits unless the source article contains a more specific date. They are evidence, not author approval.

All rows use:

- Author key: `dominik-gorecki`
- Canonical scheme/host: `https://nikgo.com`
- Existing case-sensitive `.html` path shown below
- Raw `.md` URL: must become a true 404 after SEO-003

### Identity, description, dates, and canonical URL

| Source | Display title | Unique description | Canonical path | Proposed published / modified | Date evidence or conflict |
|---|---|---|---|---|---|
| `2028_intelligence_explosion.md` | The 2028 Intelligence Explosion: BYOAI and the Return of the Human Production Unit | A macro memo on an alternative to centralized machine ownership: people retain compounding cognitive assets through Bring Your Own AI, preserving demand, mobility, and human productive agency. | `/pages/articles/2028_intelligence_explosion.html` | 2026-02-26 / 2026-02-26 | Earliest/latest Git commit. |
| `90_percent_problem_of_agentic_SWE.md` | The 90 Percent Problem of Agentic Software Delivery | Faster code generation does not transform delivery by itself. Agentic software engineering creates leverage when context, risk, evidence, and trust move continuously from intent through release. | `/pages/articles/90_percent_problem_of_agentic_SWE.html` | 2026-06-03 / 2026-07-17 | Git dates; index says June 2026. |
| `Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md` | Amdahl’s Law: The Intelligence Explosion Will Branch | Recursive self-improvement does not guarantee a permanent AI monopoly. Intelligence gains expose new bottlenecks and branch into domain-specific loops governed by evaluators, infrastructure, institutions, and power. | `/pages/articles/Amdahls_Law__The_Intelligence_Explosion_Will_Branch.html` | 2026-08-14 / 2026-08-14 | Article commit date; index says August 2026. |
| `Market_for_Portable_Minds.md` | The Market for Portable Minds | Productive intelligence should remain portable as AI enters work: workers carry generalized context, companies protect specialized context, and mobility is negotiated rather than absorbed into one central brain. | `/pages/articles/Market_for_Portable_Minds.html` | 2026-05-14 / 2026-07-17 | Git dates; index says May 2026. |
| `OODA_faster.md` | The Companies That OODA Faster | Competitive advantage comes from OODA velocity: continuously observing, orienting, deciding, and acting through governed agents and durable organizational context rather than isolated copilots. | `/pages/articles/OODA_faster.html` | 2026-03-27 / 2026-07-17 | Earliest Git commit is March 27; index says April 2026. Owner must resolve. |
| `Rokos_Symbiotic_Carrot.md` | Roko’s Symbiotic Carrot | A co-evolutionary alternative to Roko’s Basilisk in which humans and AI strengthen the civilizational competence that supports both, replacing coercive doom with reciprocal investment. | `/pages/articles/Rokos_Symbiotic_Carrot.html` | 2026-03-11 / 2026-03-11 | Git dates; index says 2026. |
| `SWE-own-your-own-ai.md` | Bring Your Own AI, Bring Your Own Leverage | Engineers can build portable AI judgment and workflows without crossing the boundary between transferable personal capability and company-owned data, systems, or intellectual property. | `/pages/articles/SWE-own-your-own-ai.html` | 2026-03-04 / 2026-03-06 | Git dates; index says 2026. |
| `Why_Office_Agents_Shouldnt_Live_in_a_Shell.md` | Why Office Agents Shouldn’t Live in a Shell | Shells, files, and folders are poor primitives for knowledge work. Enterprise agents need governed semantic layers that represent people, conversations, commitments, permissions, and institutional memory directly. | `/pages/articles/Why_Office_Agents_Shouldnt_Live_in_a_Shell.html` | 2026-03-09 / 2026-03-11 | Git dates; index says 2026. |
| `ai_after_the_outrage_machine.md` | AI After the Outrage Machine | AI can become a social technology of proportion rather than capture by restoring context, mediating disagreement, and returning people to real relationships instead of optimizing outrage and synthetic company. | `/pages/articles/ai_after_the_outrage_machine.html` | 2026-06-12 / 2026-07-17 | Git dates; index says June 2026. |
| `ai_in_the_veins_v2.md` | AI in the Veins: Building the Agentic Company’s Circulatory System | A practical playbook for connecting orchestration, enterprise retrieval, reusable agents, and a versioned Company Context Bank so organizations can compress the OODA loop without losing governance. | `/pages/articles/ai_in_the_veins_v2.html` | 2026-03-27 / 2026-03-27 | Git dates. Title is a proposed differentiation and requires approval. |
| `ai_public_opinion_cliff.md` | AI’s Public-Opinion Cliff: Why It Needs a Lifesaving Win | AI faces a legitimacy problem that incremental productivity gains may not reverse. A visible, broadly shared breakthrough—especially in medicine—could rebuild trust, while fear-driven deceleration may entrench incumbents. | `/pages/articles/ai_public_opinion_cliff.html` | 2026-03-27 / 2026-03-27 | Git dates; publication is deferred until edit requirements pass. |
| `attention_is_fundamental.md` | Attention Is Fundamental | Attention is the first allocation system behind leadership, markets, platforms, and AI: what people and institutions repeatedly make impossible to ignore becomes the world they inhabit. | `/pages/articles/attention_is_fundamental.html` | 2026-05-21 / 2026-07-17 | Git dates; index says May 2026. |
| `dose_response_curve_for_RAG__wp.md` | The Dose-Response Curve of RAG: More Context Yields Diminishing Returns | An empirical study of retrieval volume and response quality showing that balanced context improves RAG results while additional context eventually produces diminishing returns. | `/pages/articles/dose_response_curve_for_RAG__wp.html` | 2026-01-08 / 2026-01-08 | Body says January 2026 and Git begins January 8; index incorrectly says 2025. Owner must approve exact day. |
| `great-ai-pink-slip-panic.md` | The Great AI Pink-Slip Panic (and Why the Commute Still Wins) | AI will disrupt particular roles, but labor, spending, and institutions can reallocate in ways that make economy-wide collapse less inevitable than the “Jobpocalypse” narrative suggests. | `/pages/articles/great-ai-pink-slip-panic.html` | 2026-03-01 / 2026-03-01 | Git dates; index says 2026. |
| `medicines_dead_time.md` | Medicine’s Dead Time | Delay is itself a form of harm in lethal disease. Real-time trials, continuous monitoring, and human-relevant evidence systems expose how much medical caution is science and how much is avoidable latency. | `/pages/articles/medicines_dead_time.html` | 2026-04-30 / 2026-07-17 | Git dates; index says April 2026. |
| `rag_as_a_capability_multiplier.md` | Retrieval-Augmented Generation as a Capability Multiplier for Research Tasks | Two controlled experiments show that domain retrieval improves research outputs on four of five quality dimensions and can let a smaller model outperform a larger model without retrieval. | `/pages/articles/rag_as_a_capability_multiplier.html` | 2026-01-26 / 2026-01-28 | Exact body date is January 26, 2026; modified date from Git. |
| `small_RAG_beats_large_large_search.md` | Domain-Specific RAG with Gemini 3 Flash Beats Pro with Web Search Grounding | A controlled comparison finds that Gemini 3 Flash with a domain academic corpus outperforms Gemini 3 Pro with web search grounding on overall score and four of five judged dimensions. | `/pages/articles/small_RAG_beats_large_large_search.html` | 2026-01-28 / 2026-01-28 | Body says January 2026; exact day proposed from first Git commit. |
| `vibe-v-agentic-swe.md` | The Vibe Trap: From Vibe Coding to Agentic Engineering | Vibe coding accelerates prototypes but becomes a scaling trap when software matters. Agentic engineering replaces casual prompting with disciplined delegation, context, verification, and operational ownership. | `/pages/articles/vibe-v-agentic-swe.html` | 2026-03-03 / 2026-03-03 | Git dates; index says 2026. |
| `what_freedom_for__v2.md` | What Freedom Is For | AI may make leisure abundant, but it cannot make leisure good. The central challenge is developing the agency, habits, and leisure literacy needed to turn spare time into a life well lived. | `/pages/articles/what_freedom_for__v2.html` | 2026-08-11 / 2026-08-11 | Git dates; index says August 2026. |
| `wrong_kind_of_smart.md` | The Wrong Kind of Smart and the Most Expensive Model in the Room | Software teams should route model intelligence by the total expected cost of completing work, rather than treating either the strongest model or the cheapest token as the universal default. | `/pages/articles/wrong_kind_of_smart.html` | 2026-03-15 / 2026-07-17 | Earliest Git commit is March 15; index says April 2026. Owner must resolve. |
| `your_ai_career_plan.md` | Your Company’s AI Rollout Is Not Your Career Plan | A company-approved AI seat provides access, not mastery. Engineers build durable advantage through a private practice of comparative tools, real repetitions, and portable judgment. | `/pages/articles/your_ai_career_plan.html` | 2026-04-10 / 2026-07-17 | Git dates; index says April 2026. |

### Category, type, imagery, and featured state

`none` is an explicit current asset state, not an invented path. SEO-013 owns creation of missing representative images.

| Source | Category | Type | Representative image and alt text | Featured state |
|---|---|---|---|---|
| `2028_intelligence_explosion.md` | `ai-cognition-society` | essay | `pages/articles/images/2028_intelligence_explosion__current.png` — “Diagram of the human-centric production model before centralized AI ownership” | false |
| `90_percent_problem_of_agentic_SWE.md` | `agentic-engineering` | essay | `pages/articles/images/01__90_percent_problem_of_agentic_SWE.webp` — “Coding shown as one slice of the broader software delivery task” | general / 4 |
| `Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md` | `ai-cognition-society` | essay | `pages/articles/images/01__Amdahls_Law__The_Intelligence_Explosion_Will_Branch.webp` — “A luminous intelligence core branching into laboratories, factories, power grids, and civic institutions” | general / 1 |
| `Market_for_Portable_Minds.md` | `agentic-engineering` | essay | `pages/articles/images/02__Market_for_Portable_Minds.webp` — “A controlled interface between portable worker context and company systems” | general / 6 |
| `OODA_faster.md` | `agentic-engineering` | blog-post | `pages/articles/images/OODA_faster_01.webp` — “Companies competing by completing the OODA loop faster” | general / 8 |
| `Rokos_Symbiotic_Carrot.md` | `ai-cognition-society` | essay | `pages/articles/images/Rokos_Symbiotic_Carrot.webp` — “Human and artificial intelligence linked by a reciprocal symbiotic loop” | false |
| `SWE-own-your-own-ai.md` | `agentic-engineering` | blog-post | `pages/articles/images/SWE-own-your-own-ai_01.png` — “An engineer carrying a personal AI capability between work environments” | false |
| `Why_Office_Agents_Shouldnt_Live_in_a_Shell.md` | `agentic-engineering` | blog-post | `pages/articles/images/Why_Office_Agents_Shouldnt_Live_in_a_Shell_01.png` — “Office knowledge represented through governed semantic objects instead of a raw shell” | false |
| `ai_after_the_outrage_machine.md` | `ai-cognition-society` | essay | `pages/articles/images/01__ai_after_the_outrage_machine.webp` — “A person standing between an exploding outrage feed and a calm AI interface” | general / 3 |
| `ai_in_the_veins_v2.md` | `agentic-engineering` | blog-post | none — create a differentiated cover before publication | false |
| `ai_public_opinion_cliff.md` | `ai-cognition-society` | essay | none — create a representative cover before publication | false |
| `attention_is_fundamental.md` | `ai-cognition-society` | essay | `pages/articles/images/01__attention_is_fundamental.webp` — “A leader lit by a phone while symbolic worlds spill into the room” | general / 5 |
| `dose_response_curve_for_RAG__wp.md` | `rag-research` | research-article | `pages/articles/figures/exp_3--RAG_v_non-RAG__overall.png` — “Evaluation scores comparing balanced RAG with a no-RAG baseline” | white-papers / 4 |
| `great-ai-pink-slip-panic.md` | `ai-cognition-society` | essay | none — create a representative cover in SEO-013 | false |
| `medicines_dead_time.md` | `ai-cognition-society` | essay | `pages/articles/images/01__medicines_dead_time.webp` — “A patient waiting outside a clinical research laboratory” | false |
| `rag_as_a_capability_multiplier.md` | `rag-research` | research-article | `pages/articles/figures/Gemini-3-flash__RAG_v_no-RAG__overall.png` — “Experiment results comparing Gemini 3 Flash with and without RAG” | white-papers / 3 |
| `small_RAG_beats_large_large_search.md` | `rag-research` | research-article | `pages/articles/figures/rag_v_proSearch__overall.png` — “Results comparing Gemini 3 Flash with domain RAG against Gemini 3 Pro with web search” | white-papers / 2 |
| `vibe-v-agentic-swe.md` | `agentic-engineering` | blog-post | `pages/articles/images/vibe_v_agentic-swe_01.png` — “A developer caught in the scaling trap of vibe coding” | general / 9 |
| `what_freedom_for__v2.md` | `ai-cognition-society` | essay | `pages/articles/images/01__what_freedom_for.webp` — “A person choosing between an open human world and a glowing loop of digital attention” | general / 2 |
| `wrong_kind_of_smart.md` | `agentic-engineering` | blog-post | `pages/articles/images/wrong_kind_of_smart_01.webp` — “A costly AI model assigned to a trivial interface adjustment” | false |
| `your_ai_career_plan.md` | `agentic-engineering` | blog-post | `pages/articles/images/your_ai_career_plan.webp` — “An engineer developing a personal AI practice beyond a company rollout” | general / 7 |

The PDF `pages/articles/SWE_LLM_Tokenomecs_V2.pdf` remains the current `white-papers / 1` feature. Its landing-page treatment is owned by SEO-010 and is not one of the 27 Markdown disposition rows.

### Tags and related-article candidates

| Source | Proposed tags | Related candidates |
|---|---|---|
| `2028_intelligence_explosion.md` | `byoai`, `future-of-work`, `ai-ownership`, `political-economy` | `Market_for_Portable_Minds`, `SWE-own-your-own-ai`, `Amdahls_Law__The_Intelligence_Explosion_Will_Branch` |
| `90_percent_problem_of_agentic_SWE.md` | `agentic-engineering`, `software-delivery`, `developer-productivity`, `governance` | `vibe-v-agentic-swe`, `wrong_kind_of_smart`, `OODA_faster` |
| `Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md` | `intelligence-explosion`, `amdahls-law`, `ai-governance`, `decentralization` | `2028_intelligence_explosion`, `Rokos_Symbiotic_Carrot`, `Market_for_Portable_Minds` |
| `Market_for_Portable_Minds.md` | `portable-context`, `future-of-work`, `labor-markets`, `ai-ownership` | `2028_intelligence_explosion`, `SWE-own-your-own-ai`, `your_ai_career_plan` |
| `OODA_faster.md` | `ooda-loop`, `agentic-enterprise`, `context-engineering`, `organizational-memory` | `ai_in_the_veins_v2`, `90_percent_problem_of_agentic_SWE`, `Why_Office_Agents_Shouldnt_Live_in_a_Shell` |
| `Rokos_Symbiotic_Carrot.md` | `ai-symbiosis`, `rokos-basilisk`, `co-evolution`, `ai-futures` | `Amdahls_Law__The_Intelligence_Explosion_Will_Branch`, `2028_intelligence_explosion`, `attention_is_fundamental` |
| `SWE-own-your-own-ai.md` | `byoai`, `software-engineering`, `portable-skills`, `ai-workflows` | `your_ai_career_plan`, `Market_for_Portable_Minds`, `2028_intelligence_explosion` |
| `Why_Office_Agents_Shouldnt_Live_in_a_Shell.md` | `office-agents`, `semantic-layer`, `enterprise-ai`, `knowledge-management` | `OODA_faster`, `ai_in_the_veins_v2`, `90_percent_problem_of_agentic_SWE` |
| `ai_after_the_outrage_machine.md` | `social-media`, `attention`, `ai-mediation`, `online-discourse` | `attention_is_fundamental`, `ai_public_opinion_cliff`, `what_freedom_for__v2` |
| `ai_in_the_veins_v2.md` | `ooda-loop`, `agentic-enterprise`, `orchestration`, `organizational-memory` | `OODA_faster`, `Why_Office_Agents_Shouldnt_Live_in_a_Shell`, `90_percent_problem_of_agentic_SWE` |
| `ai_public_opinion_cliff.md` | `public-opinion`, `ai-legitimacy`, `medical-ai`, `ai-policy` | `medicines_dead_time`, `ai_after_the_outrage_machine`, `attention_is_fundamental` |
| `attention_is_fundamental.md` | `attention`, `leadership`, `platforms`, `cognition` | `ai_after_the_outrage_machine`, `what_freedom_for__v2`, `ai_public_opinion_cliff` |
| `dose_response_curve_for_RAG__wp.md` | `rag`, `retrieval-volume`, `diminishing-returns`, `llm-evaluation` | `rag_as_a_capability_multiplier`, `small_RAG_beats_large_large_search` |
| `great-ai-pink-slip-panic.md` | `automation`, `labor-markets`, `future-of-work`, `ai-economics` | `2028_intelligence_explosion`, `Market_for_Portable_Minds`, `your_ai_career_plan` |
| `medicines_dead_time.md` | `medical-ai`, `clinical-trials`, `fda`, `research-latency` | `ai_public_opinion_cliff`, `Amdahls_Law__The_Intelligence_Explosion_Will_Branch` |
| `rag_as_a_capability_multiplier.md` | `rag`, `research`, `llm-evaluation`, `small-models` | `dose_response_curve_for_RAG__wp`, `small_RAG_beats_large_large_search` |
| `small_RAG_beats_large_large_search.md` | `rag`, `search-grounding`, `gemini`, `llm-evaluation` | `rag_as_a_capability_multiplier`, `dose_response_curve_for_RAG__wp` |
| `vibe-v-agentic-swe.md` | `vibe-coding`, `agentic-engineering`, `software-quality`, `ai-agents` | `90_percent_problem_of_agentic_SWE`, `wrong_kind_of_smart`, `your_ai_career_plan` |
| `what_freedom_for__v2.md` | `leisure`, `automation`, `well-being`, `human-flourishing` | `attention_is_fundamental`, `ai_after_the_outrage_machine`, `great-ai-pink-slip-panic` |
| `wrong_kind_of_smart.md` | `model-routing`, `llm-cost`, `software-engineering`, `ai-economics` | `90_percent_problem_of_agentic_SWE`, `vibe-v-agentic-swe`, `SWE-own-your-own-ai` |
| `your_ai_career_plan.md` | `ai-careers`, `software-engineering`, `deliberate-practice`, `portable-skills` | `SWE-own-your-own-ai`, `Market_for_Portable_Minds`, `vibe-v-agentic-swe` |

## 5. Proposed URL policy

SEO-003 should apply the following policy only after owner approval:

1. Preserve every approved article's existing case-sensitive `.html` path exactly.
2. Do not migrate to extensionless or `/articles/slug/` URLs while GitHub Pages uses branch deployment.
3. Use a static `jekyll-redirect-from` document only for the approved `what_freedom_for.html` alternate, targeting `/pages/articles/what_freedom_for__v2.html`. Do not describe it as an HTTP 301.
4. Archive the five proposed derivative/draft sources without redirects after unique citations/value are harvested.
5. Allow old raw `.md` paths to become true 404s after canonical collection migration.
6. Preserve `CNAME` as `nikgo.com`; Cloudflare continues to own public HTTPS and edge behavior.

## 6. Correction list for SEO-003

- Correct `Domink Gorecki` to `Dominik Gorecki`.
- Resolve the Dose-Response year conflict: the article body says January 2026, Git begins 2026-01-08, and the index says 2025.
- Resolve the OODA date conflict: Git begins 2026-03-27 and the index says April 2026.
- Resolve the Wrong Kind of Smart date conflict: Git begins 2026-03-15 and the index says April 2026.
- Give `great-ai-pink-slip-panic.md` explicit metadata because its source begins with an H2 rather than an H1.
- Differentiate the proposed `ai_in_the_veins_v2.md` title from `OODA_faster.md` before publication.
- Add representative images to `ai_in_the_veins_v2.md`, `ai_public_opinion_cliff.md`, and `great-ai-pink-slip-panic.md` through SEO-013.

## 7. Owner approval record

On 2026-08-14, the site owner explicitly approved:

- All 27 dispositions in section 2.
- The 21 metadata rows, especially title/description and category.
- Every publication and modification date, including the three conflicts above.
- The single redirect target and the archive-without-redirect decisions.
- The URL policy in section 5.

This approval closes SEO-002 and authorizes SEO-003 to use this record as its editorial source of truth. SEO-003 must still perform its own implementation and verification steps; this approval does not itself move, delete, or redirect content.
