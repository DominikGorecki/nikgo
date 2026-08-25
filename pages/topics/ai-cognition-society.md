---
title: AI, Cognition, Attention, and Society
description: Essays on AI's effects on attention, agency, health, labor, institutions, and the social choices that shape an AI-enabled future.
permalink: /topics/ai-cognition-society/
layout: default
collection_page: topic
topic: ai-cognition-society
reading_path:
  - url: /pages/articles/attention_is_fundamental.html
    title: Attention Is Fundamental
    why: Start with attention as the allocation system behind leadership, platforms, and AI.
  - url: /pages/articles/ai_after_the_outrage_machine.html
    title: AI After the Outrage Machine
    why: Consider what AI systems should optimize for when social context and relationships are at stake.
  - url: /pages/articles/2028_intelligence_explosion.html
    title: The 2028 Intelligence Explosion
    why: Extend the question from media and attention to ownership, agency, and economic institutions.
---

{% assign topic_articles = site.articles | where: "published", true | where: "category", "ai-cognition-society" | sort: "date" | reverse %}

<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="{{ '/' | relative_url }}">Home</a></li>
    <li><a href="{{ '/articles.html' | relative_url }}">Articles</a></li>
    <li aria-current="page">AI, cognition, and society</li>
  </ol>
</nav>

# AI, cognition, attention, and society

AI changes more than task speed. It reshapes attention, agency, health systems, labor markets, and the institutions that coordinate collective life. This hub examines those consequences and the choices around them; it is not a feed of product launches or a forecast of inevitable outcomes.

## A reading path

<ol>
  {% for item in page.reading_path %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a> — {{ item.why | escape }}</li>
  {% endfor %}
</ol>

## All AI, cognition, and society articles

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

<p>Explore <a href="{{ '/topics/agentic-engineering/' | relative_url }}">agentic engineering</a> for AI-enabled work systems, or <a href="{{ '/topics/rag-research/' | relative_url }}">RAG research</a> for retrieval evidence. Return to <a href="{{ '/articles.html' | relative_url }}">all articles</a>.</p>
