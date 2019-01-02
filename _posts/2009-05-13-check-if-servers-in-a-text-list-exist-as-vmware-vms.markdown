---
layout: post
title: Check if servers in a text list exist as VMware VMs
date: '2009-05-13 12:30:15'
tags:
- script
- virtualisation
---


I got handed a list of around 1,000 servers today, and asked if any of them were part of our VI environment.

Rather than work through it by hand, I wrote the following script:

<script src="https://gist.github.com/BenNeise/7215386.js"></script>

If your VM object names do not match the DNS names on the list, then this won't work, but I suppose you could combine this with some logic from the [script I wrote to find mismatches](http://ben.neise.co.uk/index.php/2009/03/vm-object-dns-name-mismatches/).


