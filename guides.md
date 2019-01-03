---
layout: page
title: Guides
permalink: /guides/
---

<p>Some guides I've written</p>

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