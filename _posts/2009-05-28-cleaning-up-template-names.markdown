---
layout: post
title: Cleaning up VM template names
date: '2009-05-28 13:45:02'
tags:
- script
---


I wrote this today to remove occurrences of the string "Tmpl" anywhere in the name of the template, and then to re-name the template with "Tmpl" as a prefix. It had a higher purpose than keeping everything nice and neat, but it's rather specific to our environment so I won't bother going into the details.

<script src="https://gist.github.com/BenNeise/7215567.js"></script>

Despite being quite specific in it's current form, this could easily be modified to rename virtual machines (or indeed any other PowerShell object).

While I suspect there's a more elegant way to do this in fewer steps, it's not *particularly* hacky.


