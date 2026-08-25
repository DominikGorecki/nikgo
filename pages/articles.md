---
title: Articles on Agentic Engineering, RAG, and AI
description: Original essays and research by Dominik Gorecki on agentic engineering, retrieval-augmented generation, AI strategy, cognition, and society.
permalink: articles.html
layout: default
collection_page: articles
---

{% assign published_articles = site.articles | where: "published", true | sort: "date" | reverse %}
{% assign featured_articles = published_articles | where: "featured", true | sort: "feature_order" %}

# Articles

Essays and research on building dependable AI systems, evaluating retrieval and model choices, and understanding AI's consequences for attention, work, and society. Explore the focused reading paths for [agentic engineering]({{ '/topics/agentic-engineering/' | relative_url }}), [RAG research]({{ '/topics/rag-research/' | relative_url }}), or [AI, cognition, and society]({{ '/topics/ai-cognition-society/' | relative_url }}).

[Jump to the complete archive](#all-articles)

{% if featured_articles.size > 0 %}
## Featured reading

<ul class="card-grid" role="list">
  {% for article in featured_articles %}
  {% assign category = site.data.taxonomy.categories[article.category] %}
  <li>
    <article>
      <a href="{{ article.url | relative_url }}" class="card-item">
        {% if article.image and article.image.path %}
        <img src="{{ article.image.path | relative_url }}" class="card-image" alt="{{ article.image.alt | escape }}" width="{{ article.image.width }}" height="{{ article.image.height }}">
        {% endif %}
        <p class="card-category">{{ category.label | default: article.category | escape }}</p>
        <h3 class="card-title">{{ article.title | escape }}</h3>
        <p class="card-description">{{ article.description | escape }}</p>
        <span class="card-footer">Read article <span class="card-arrow" aria-hidden="true">→</span></span>
      </a>
    </article>
  </li>
  {% endfor %}
</ul>
{% endif %}

<hr>

## Complete archive

<p id="all-articles">Every published canonical article, including the featured reading above, in reverse chronological order.</p>

<ol class="article-archive-list">
  {% for article in published_articles %}
  {% assign category = site.data.taxonomy.categories[article.category] %}
  <li>
    <article>
      <p>{{ category.label | default: article.category | escape }}</p>
      <h3><a href="{{ article.url | relative_url }}">{{ article.title | escape }}</a></h3>
      <p><time datetime="{{ article.date | date_to_xmlschema }}">{{ article.date | date: "%B %-d, %Y" }}</time></p>
      <p>{{ article.description | escape }}</p>
    </article>
  </li>
  {% endfor %}
</ol>
