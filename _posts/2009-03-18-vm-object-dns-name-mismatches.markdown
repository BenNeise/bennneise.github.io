---
layout: post
title: Resolving Virtual Machine object name and DNS name mismatches using PowerCLI
date: '2009-03-18 12:50:13'
tags:
    - script
---


We were working recently to align our guest VM object names (the ones shown in vSphere) with their DNS names. As we have over 800 guests, this would have taken us a while to compile by hand. In order to make the process a little easier, I wrote the following PowerShell script to flag machines where the hostname differs from the  object name.

<script src="https://gist.github.com/BenNeise/7213409.js"></script>

This worked perfectly.  While I could have had the script rename these machine objects to the hostname, it was safer to look at each one individually.  Even so, the script saved us a few hours of tedious work.

Remember that renaming the object doesn't fix the file and folder names on the datastore. If you do your datastore management via vSphere, this won't matter to you. If you manage files on the datastore directly, then I expect you'll already know how to resolve this.