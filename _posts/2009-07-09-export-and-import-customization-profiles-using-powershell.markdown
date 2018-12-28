---
layout: post
title: Export and import vSphere customization specifications using PowerShell
date: '2009-07-09 15:02:58'
---


I'm in the middle of preparing for a migration from VI3 to vSphere 4 just now (hence the lack of any substantial updates on this blog).

As part of this process, I was just about to start writing  a script to export our customisation specifications, when Arnim van Lieshout's post appeared in my [VMware Planet V12N](http://www.vmware.com/vmtn/planet/v12n/) RSS feed.

[Export and import customization profiles using Powershell | Arnim van Lieshout](http://www.van-lieshout.com/2009/07/export-and-import-customization-profiles-using-powershell/).

It failed on a couple of customisations, but by adding...

`Write-Host "Exporting $($CustomizationProfile.Name)"`

...after the ForEach loop started, it was easy to see that it was customisations with `/` and `*` characters that were causing the errors. I fixed those manually, and it worked perfectly.