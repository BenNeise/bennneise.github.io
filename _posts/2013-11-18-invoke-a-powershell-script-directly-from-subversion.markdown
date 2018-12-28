---
layout: post
title: Invoke a PowerShell script directly from Subversion
date: '2013-11-18 16:30:54'
---


I've been thinking about doing something like this for a while. By adding this to PowerShell profiles, I can ensure that other people who use my scripts/functions are using the latest versions by having them run directly from a Subversion URL. This negates the requirement for them to have a local SVN repo (and for them to keep it up to date).

Our Subversion is set up for basic, rather than AD integrated, authentication, but I imagine AD integrated authentication would be easier to implement (probably using **Invoke-WebRequest** with the **UseDefaultCredentials** parameter). Rather than prompt the user at each use, I set up a service account which has only Read permissions on the repository, and hardcoded the Base64String encoded username and password into the internal version of this script.

The terrifying looking regex was based on [SqlChow](http://sqlchow.wordpress.com/2013/09/07/using-verbal-expressions-to-make-regex-easy-in-powershell/)ÔÇÿs example, with **PS1** appended to the end.

<script src="https://gist.github.com/BenNeise/7559974.js"></script>


