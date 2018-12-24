---
layout: post
title: Auto-generating PowerShell documentation in MarkDown
date: '2014-10-07 18:43:34'
---


![Markdown](/content/images/2016/01/1664x1024-solid.png)
I donÔÇÖt mind writing documentation for my scripts, but I find that most documentation writing exercises tends to suffers from two problems:-

- **Duplicated effort** ÔÇô I tend to document my script inline, (so that `Get-Help` will work), why do I need to document the same details elsewhere?
- **Keeping it up-to-date**┬áÔÇô The only thing worse than *no* documentation, is clearly outdated documentation.

I had a folder full of PS1 scripts, each of which had the necessary headers. However, I needed to get this documentation into our repository of choice (a GitLab wiki).

So, in order to save me duplicating some effort, I wrote up a quick function thatÔÇÖll read the inline documentation from all the PowerShell scripts in a folder, and output a markdown formatted document per script, as well as an index document which links to the others. This imports nicely into a GitLab wiki. At first I thought IÔÇÖd be lucky, and someone would have created an `ConvertTo-Markdown` function, but of course a PowerShell object doesnÔÇÖt map to a document in the same way that it maps to a table, or a CSV.

<script src="https://gist.github.com/GuruAnt/0eb1767ec2b0b5b37d00.js"></script>

The documentation generated looks something like [this](https://stackedit.io/viewer#!provider=gist&gistId=9cc7c75d1937de12f6a2&filename=TestPingDocumentation.markdown).

Not sure how useful this will be to other people, as itÔÇÖs a pretty specific set of circumstances. IÔÇÖm also not 100% satisfied with it, as the help object returned by Get-Help is a bit of a chimera of object types, which has made the code a bit ugly.


