---
layout: post
title: Cleaning up VM template names
date: '2009-05-28 13:45:02'
tags:
- script
---


I wrote this today to remove occurrences of the string ÔÇ£TmplÔÇØ anywhere in the name of the template, and then to re-name the template with ÔÇ£TmplÔÇØ as a prefix. It had a higher purpose than keeping everything nice and neat, but itÔÇÖs rather specific to our environment so I wonÔÇÖt bother going into the details.

<script src="https://gist.github.com/GuruAnt/7215567.js"></script>

Despite being quite specific in itÔÇÖs current form, this could easily be modified to rename virtual machines (or indeed any other PowerShell object).

While I suspect thereÔÇÖs a more elegant way to do this in fewer steps, itÔÇÖs not *particularly* hacky.


