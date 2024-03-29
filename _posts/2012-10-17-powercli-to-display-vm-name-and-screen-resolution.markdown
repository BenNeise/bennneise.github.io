---
layout: post
title: PowerCLI to display VM name and screen resolution
date: '2012-10-17 11:14:28'
tags: vmware-vsphere powershell
---


One-liner PowerCLI to output a list of machine names and screen resolutions.

<!--more-->

`Get-VM | Where-Object {$_.Folder.Name -ne "VMwareViewComposerReplicaFolder"} | Select-Object Name,@{Name="Resolution";Expression={($_.Guest.ExtensionData.Screen.Width.ToString() + "x" + $_.Guest.ExtensionData.Screen.Height.ToString())}}`

Handy for checking that VDI desktops are not set to less than 1024x768 which can cause issues with PCOIP, hence the exclusion of View replicas via the `Folder.Name` property (which would otherwise pollute the results when running against a View vCenter).

I concatenated the _Height_ and _Width_ values into a single column via a calculated value, which wasn't strictly necessary but makes it more readable (for people).


