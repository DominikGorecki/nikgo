---
title: Articles
permalink: articles.html
---

# Articles 

## White Papers

### [Domain-Specific RAG with Gemini 3 Flash Beats PRO with Web Search Grounding](articles/small_RAG_beats_large_large_search.md)

*By Dominik Gorecki*

This white paper shows that **Gemini 3 Flash using a domain-specific academic RAG corpus** still **beats Gemini 3 Pro grounded with web search**, with statistically significant gains in **overall score** plus **4/5 judged dimensions** (factual correctness, completeness, hallucination risk, and academic response), while **coherence remains unchanged**. The advantage is smaller than in earlier experiments—expected because Pro+search is a stronger baseline—but the system still wins **86.7%** of pairwise evaluations (with one tie and one loss out of 15). Bottom line: **“RAG” isn’t one thing—corpus quality and domain alignment matter enough that specialized academic retrieval can outperform generic search grounding even on a smaller model.**


### [Retrieval-Augmented Generation as a Capability Multiplier for Research Tasks](articles/rag_as_a_capability_multiplier.md) (2026)

*By Dominik Gorecki*

Two controlled experiments show that using RAG significantly improves research outputs on **overall_score** plus **4 of 5** quality dimensions (factual correctness, completeness, hallucination risk, and academic response), with **coherence** the only metric that doesn’t reliably change. Crucially, **Gemini 3 Flash with RAG outperforms Gemini 3 Pro without RAG**, suggesting retrieval can substitute for model scale in research workflows, at the cost of longer, denser, less readable writing.


### [The Dose-Response Curve of RAG: More Context Yields Diminishing Returns](articles/dose_response_curve_for_RAG__wp.md) (2025)

*By Domink Gorecki*

An empirical investigation into the relationship between retrieval volume and response quality in RAG systems. The study demonstrates that while RAG significantly improves academic depth and completeness, it exhibits steep diminishing returns beyond 10-15 sources, with marginal gains dropping by 12x at higher volumes.
