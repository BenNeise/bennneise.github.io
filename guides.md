---
layout: page
title: Guides
permalink: /guides/
---


{% for guide in site.guides %}
  <h3>
    <a href="{{ guide.url }}">
      {{ guide.title }}
    </a>
  </h3>
  <p>
    {{ guide.summary }}
  </p>
{% endfor %}