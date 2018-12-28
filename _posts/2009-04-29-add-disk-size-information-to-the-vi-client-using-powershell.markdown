---
layout: post
title: Add disk size information to the VI Client using PowerShell
date: '2009-04-29 11:41:47'
tags:
- powercli
- script
- virtualisation
---


This is based on Hugo Peeters' script to [add snapshot information to the VI client using PowerShell](http://www.peetersonline.nl/index.php/vmware/add-snapshot-information-to-the-vi-client-using-powershell/).

Our users occasionally need larger machines created for packaging big applications.  After increasing the size, we used to append the VM Object name (e.g, "PACKVM01  - 10GB"), but this caused a mismatch between the virtual machine object name in VIC and the DNS host name. Also, it looked untidy!

We needed a new way for VIC users to easily see which were the larger machines, so I modified Hugo's script to add disk size as a custom attribute.

<script src="https://gist.github.com/BenNeise/7215113.js"></script>


