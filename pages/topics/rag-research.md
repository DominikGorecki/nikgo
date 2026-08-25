---
title: RAG Research, Evaluation, and AI Tokenomics
description: Evidence-led research on retrieval-augmented generation, evaluation design, context selection, search grounding, and the economics of AI systems.
permalink: /topics/rag-research/
layout: default
collection_page: topic
topic: rag-research
reading_path:
  - url: /pages/articles/rag_as_a_capability_multiplier.html
    title: Retrieval-Augmented Generation as a Capability Multiplier for Research Tasks
    why: Begin with controlled evidence for when retrieval improves research quality.
  - url: /pages/articles/dose_response_curve_for_RAG__wp.html
    title: The Dose-Response Curve of RAG
    why: Learn why more retrieved context is not always better context.
  - url: /pages/articles/small_RAG_beats_large_large_search.html
    title: Domain-Specific RAG with Gemini 3 Flash Beats PRO with Web Search Grounding
    why: See how a targeted corpus can outperform a larger model with web-search grounding.
---

{% assign topic_articles = site.articles | where: "published", true | where: "category", "rag-research" | sort: "date" | reverse %}

<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="{{ '/' | relative_url }}">Home</a></li>
    <li><a href="{{ '/articles.html' | relative_url }}">Articles</a></li>
    <li aria-current="page">RAG research</li>
  </ol>
</nav>

# RAG research, evaluation, and AI tokenomics

Retrieval-augmented generation (RAG) pairs a model with a selected evidence corpus. This hub covers how to test that pairing, choose the right amount of context, and reason about model cost and error—not generic claims that every knowledge problem needs a vector database.

## A reading path

<ol>
  {% for item in page.reading_path %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a> — {{ item.why | escape }}</li>
  {% endfor %}
</ol>

## All RAG research articles

<ol class="article-archive-list">
  {% for article in topic_articles %}
  <li>
    <article>
      <h3><a href="{{ article.url | relative_url }}">{{ article.title | escape }}</a></h3>
      <p>{{ article.description | escape }}</p>
    </article>
  </li>
  {% endfor %}
</ol>

<p>Explore <a href="{{ '/topics/agentic-engineering/' | relative_url }}">agentic engineering</a> for delivery systems, or <a href="{{ '/topics/ai-cognition-society/' | relative_url }}">AI, cognition, and society</a> for broader consequences. Return to <a href="{{ '/articles.html' | relative_url }}">all articles</a>.</p>
