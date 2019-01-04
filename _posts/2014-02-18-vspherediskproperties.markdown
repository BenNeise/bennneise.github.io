---
layout: post
title: Displaying vSphere disk properties (including provisioning & persistence)
date: '2014-02-18 13:29:33'
---


I was doing some tidying of old scripts and came across something I thought it might be useful, so I tidied it up and added some documentation.

![Screenshot showing results of script](/assets/DiskInformation.png)

This PowerShell script uses the [vSphere PowerCLI](https://www.vmware.com/support/developer/PowerCLI/index.html) to display a list of virtual machine disks, file-names, modes (persistent or non-persistent), sizes and whether or not the disk is [thinly provisioned](https://www.vmware.com/products/vsphere/features/storage-thin-provisioning.html). You'll need to connect to one or more vSphere servers first.

<script src="https://gist.github.com/BenNeise/9069627.js"></script>  

It's likely that I based the original version of this script on someone else's work as it contained a couple of techniques which I don't tend to use (like [using Select-Object to create object properties](http://blogs.msdn.com/b/mediaandmicrocode/archive/2008/11/26/microcode-powershell-scripting-tricks-select-object-note-properties-vs-add-member-script-properties.aspx)), but I'm afraid I can't remember where, and searching for a couple of keywords brings back no results.