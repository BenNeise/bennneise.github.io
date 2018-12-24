---
layout: post
title: Resolving Virtual Machine object name and DNS name mismatches
date: '2009-03-18 12:50:13'
---


We were working recently to align our guest VM object names (the ones shown in vSphere) with their DNS names. As we have over 800 guests, this would have taken us a while to compile by hand. In order to make the process a little easier, I wrote the following PowerShell script to flag machines where the hostname differs from the┬á object name.

<script src="https://gist.github.com/GuruAnt/7213409.js"></script>

This worked perfectly.┬á While I could have had the script rename these machine objects to the hostname, it was safer to look at each one individually.┬á Even so, the script saved us a few hours of tedious work.

Remember that renaming the object doesnÔÇÖt fix the file and folder names on the datastore. If you do your datastore management via vSphere, this wonÔÇÖt matter to you. If you manage files on the datastore directly, then I expect youÔÇÖll already know how to resolve this.


