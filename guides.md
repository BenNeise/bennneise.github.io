---
layout: page
title: guides
permalink: /guides/
---

Guides are more in depth articles about specific subjects than the blog posts, and tend to be a bit more detailed.

{% for guide in site.guides %}

  <div class="guide-panel">
  <a href="{{ guide.url }}"><img src="{{ guide.image }}" class="guide-hero-image"></a>
  <h1><a href="{{ guide.url }}">{{ guide.title }}</a></h1>
  <p>{{ guide.summary }}</p>
  </div>


{% endfor %}