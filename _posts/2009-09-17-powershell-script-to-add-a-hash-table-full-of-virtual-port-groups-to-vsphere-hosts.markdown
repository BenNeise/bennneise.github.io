---
layout: post
title: Script to add a hash table full of virtual port groups to vSphere hosts
date: '2009-09-17 11:45:27'
---


As part of the migration I'm working on, we needed to add a whole bunch of Virtual Port Groups with associated VLANs to the servers. The following script could do this in a few minutes (although Host Profiles would accomplish much the same thing, we're not running Enterprise)

<script src="https://gist.github.com/BenNeise/7216135.js"></script>

Although this isn't a complicated script, it was the first time I've used hash tables (thanks to [PowerShell.Com's excellent page](http://powershell.com/cs/blogs/ebook/archive/2008/10/22/chapter-4-arrays-and-hashtables.aspx)), so I thought I'd share.


