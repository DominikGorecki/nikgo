---
title: Engineering and AI Projects
description: Products, open-source packages, and experiments created by Dominik Gorecki across AI research, knowledge work, and developer tools.
permalink: projects.html
layout: default
collection_page: projects
---

# Projects

Products, packages, and experiments by Dominik Gorecki. Descriptions below identify the relationship to each project so readers can distinguish independent editorial analysis from product work.

<ul class="card-grid project-grid" role="list">
  {% for project in site.data.projects.projects %}
  <li class="project-grid-item">
    <article class="project-card">
      <a href="{{ project.url }}" class="card-item project-card-link">
        {% if project.image %}
        <img src="{{ project.image | relative_url }}" alt="{{ project.image_alt | escape }}" class="card-logo">
        {% endif %}
        <h2 class="card-title">{{ project.name | escape }}</h2>
        <p class="card-description">{{ project.description | escape }}</p>
        <span class="card-footer">{{ project.link_label | escape }} <span class="card-arrow" aria-hidden="true">→</span></span>
        <p class="project-meta"><strong>Relationship:</strong> {{ project.relationship | escape }}. <strong>Status:</strong> {{ project.status | escape }}.</p>
        <p class="project-disclosure">{{ project.disclosure | escape }}</p>
      </a>
    </article>
  </li>
  {% endfor %}
</ul>
