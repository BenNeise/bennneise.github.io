---
layout: post
title: Creating new Virtual Port Groups in ESX with PowerShell
date: '2009-04-28 12:18:34'
tags:
- script
---


We frequently need to create new virtual port groups on our ESX hosts with VLAN tags which correspond to pre-assigned DHCP scopes. I wrote this PowerShell script to create the new VPG across all hosts.

<script src="https://gist.github.com/GuruAnt/7213844.js"></script>

This assumes that your virtual port group is on a switch called **VMSwitch**. You could easily modify this to accept parameters from the command-line, rather than being specified in the script.

When it comes to re-naming existing virtual port groups across hosts there doesnÔÇÖt seem to be an inbuilt cmdlet, instead I wrote a script to delete the old VPG, and create a new one with the same VLAN tag:-

<script src="https://gist.github.com/GuruAnt/7213887.js"></script>

Run it once to check itÔÇÖs doing what you want, then remove the `-WhatIf` tags to run it for real.


