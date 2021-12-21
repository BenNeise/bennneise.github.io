---
layout: post
title: vCenter and host build numbers
date: '2009-10-02 09:53:07'
tags:
- script
- vcenter
---


This is based on [Carter Shanklin's PowerShell snippets to query VC and ESX build version numbers](http://communities.vmware.com/message/1013433#1013433).

This script loops through the list of vCenter servers, and gets their version and build info, as well as the version and build info for it's connected hosts.

<script src="https://gist.github.com/BenNeise/7216184.js"></script>


