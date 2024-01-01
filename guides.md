---
layout: page
title: guides
permalink: /guides/
---

These guides are more in depth articles about specific subjects.

{% for guide in site.guides %}

  <h1>
    <a href="{{ guide.url }}">
      {{ guide.title }}
      {% if guide.image %}
      <p>
        <img src="{{ guide.image }}" class="guide-hero-image">
      </p>
      {% endif %}
    </a>
  </h1>
  <p>
    {{ guide.summary }}
  </p>

{% endfor %}