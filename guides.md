---
layout: page
title: Guides
permalink: /guides/
---

These are more in depth articles about specific subjects.


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