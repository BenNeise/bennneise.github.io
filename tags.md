---
layout: page
title: Tags
permalink: /tags/
---

{% for tag in site.tags %}
<ul>
<li>
    <a href="#{{ tag[0] }}">{{ tag[0] }}</a>
</li>
</ul>
{% endfor %}

{% for tag in site.tags %}
<h1 id="{{ tag[0] }}">{{ tag[0] }}</h1>
<ul>
    {% for post in tag[1] %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
{% endfor %}