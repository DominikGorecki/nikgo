---
title: Agentic Engineering and AI-Enabled Organizations
description: Research and practical essays on dependable AI agents, agentic software delivery, organizational context, and the future of AI-enabled work.
permalink: /topics/agentic-engineering/
layout: default
collection_page: topic
topic: agentic-engineering
reading_path:
  - url: /pages/articles/90_percent_problem_of_agentic_SWE.html
    title: The 90 Percent Problem of Agentic Software Delivery
    why: Start with the operating model that turns code generation into trustworthy delivery.
  - url: /pages/articles/OODA_faster.html
    title: The Companies That OODA Faster
    why: Continue with how governed agents and durable context change organizational speed.
  - url: /pages/articles/your_ai_career_plan.html
    title: Your Company’s AI Rollout Is Not Your Career Plan
    why: Finish with the individual practice needed to build portable judgment inside a changing organization.
---

{% assign topic_articles = site.articles | where: "published", true | where: "category", "agentic-engineering" | sort: "date" | reverse %}

<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="{{ '/' | relative_url }}">Home</a></li>
    <li><a href="{{ '/articles.html' | relative_url }}">Articles</a></li>
    <li aria-current="page">Agentic engineering</li>
  </ol>
</nav>

# Agentic engineering and AI-enabled organizations

Agentic engineering is the practice of designing AI-assisted work so that context, authority, evidence, and accountability survive from intent through release. This hub focuses on software delivery and organizational operating models—not generic prompt tips, autonomous-agent hype, or vendor announcements.

## A reading path

<ol>
  {% for item in page.reading_path %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a> — {{ item.why | escape }}</li>
  {% endfor %}
</ol>

## All agentic engineering articles

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

<p>Explore <a href="{{ '/topics/rag-research/' | relative_url }}">RAG research</a> for evidence and retrieval systems, or <a href="{{ '/topics/ai-cognition-society/' | relative_url }}">AI, cognition, and society</a> for the human and institutional consequences. Return to <a href="{{ '/articles.html' | relative_url }}">all articles</a>.</p>
