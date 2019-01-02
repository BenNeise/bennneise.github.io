---
layout: page
title: Guides
permalink: /guides/
---

{% for guide in site.guides %}
  <h2>
    <a href="{{ guide.url }}">
      {{ guide.title }}
    </a>
  </h2>
  <p>
    {{ guide.summary }}
  </p>
{% endfor %}