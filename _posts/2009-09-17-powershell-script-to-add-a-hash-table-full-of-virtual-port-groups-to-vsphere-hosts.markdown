---
layout: post
title: Script to add a hash table full of virtual port groups to vSphere hosts
date: '2009-09-17 11:45:27'
---


As part of the migration I'm working on, we needed to add a whole bunch of Virtual Port Groups with associated VLANs to the servers. The following script could do this in a few minutes (although Host Profiles would accomplish much the same thing, we're not running Enterprise)

```powershell
# Sets up virtual port groups on all hosts connected to a specific vCenter Server

# Name of vCenter Server
$strVCenterServer = "your.vCenter.Server"

# VLANs and associated VPGs
$ArrVLANs = @{
	"123" = "vlanA";
	"456" = "vlanB";
	"789" = "vlanC";
}

# Connect to the vCenter Server
Connect-VIserver -Server $strVCenterServer

# Loop through the VLAN/VPG pairs
ForEach($objVLAN in ($ArrVLANs.Keys | Sort-Object)){
	# Loop through the hosts
	ForEach ($objHost in (Get-VMHost | Sort-Object)){
		# Create the VPG with the VLAN as specified in the array above, on the switch called "VMSwitch" on the current host
		# Remove the "-WhatIf" tag from the end of the following line to "arm" the script
		New-VirtualPortGroup -Name $strNewVPG -VirtualSwitch (Get-Virtualswitch -VMHost $objHost | Where-Object { $_.Name -match "VMswitch" }) -VLanId $strNewVlanTag
		# Write what we've just done to screen
		Write-Host ("Adding Virtual Port Group $($ArrVLANs[$objVLAN]) with VLAN Tag $objVLAN to $objHost")
	}
}
# Disconnect the session from the host
Disconnect-VIServer -Confirm:$False
```

Although this isn't a complicated script, it was the first time I've used hash tables (thanks to [PowerShell.Com's excellent page](http://powershell.com/cs/blogs/ebook/archive/2008/10/22/chapter-4-arrays-and-hashtables.aspx)), so I thought I'd share.


