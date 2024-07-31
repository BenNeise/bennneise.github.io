---
layout: post
title: Creating new Virtual Port Groups in ESX with PowerShell
date: '2009-04-28 12:18:34'
tags: vmware-vsphere powershell
---


We frequently need to create new virtual port groups on our ESX hosts with VLAN tags which correspond to pre-assigned DHCP scopes. I wrote this PowerShell script to create the new VPG across all hosts.

<!--more-->

```powershell
$strNewVPG = "newVirtualPortGroup"
$strNewVlanTag = "123"

$ObjAllHosts = Get-VMHost | Sort-Object -Property Name

foreach ($objHost in $ObjAllHosts){
    $strVSwitch = Get-VirtualSwitch -VMHost (Get-VMHost $objHost) | Where-Object { $_.Name -like "VMswitch" }
    Write-Output -InputObject "Adding Virtual Port Group $strNewVPG with VLAN Tag $strNewVlanTag to $objHost"
    New-VirtualPortGroup -Name $strNewVPG -VirtualSwitch $strVSwitch -VLanId $strNewVlanTag
}
```

This assumes that your virtual port group is on a switch called **VMSwitch**. You could easily modify this to accept parameters from the command-line, rather than being specified in the script.

When it comes to re-naming existing virtual port groups across hosts there doesn't seem to be an inbuilt cmdlet, instead I wrote a script to delete the old VPG, and create a new one with the same VLAN tag:-

```powershell
$strOldVPG = "OldVPGName"
$strNewVPG = "NewVPGName"
$ObjAllHosts = (Get-VMHost | Sort-Object -Property Name)
foreach ($objHost in $ObjAllHosts){
    Write-Output -InputObject "Changing Virtual Port Group Settings on" $objHost
    $strVSwitch = Get-VirtualSwitch -VMHost (Get-VMHost -Name $objHost) | Where-Object { $_.Name -match "VMswitch" }
    $objOldVPG = Get-VirtualPortGroup (Get-VMHost -Name $objHost) | Where-Object { $_.Name -match $strOldVPG }
    Write-Output -InputObject "Removing Virtual Port Group" $objOldVPG
    Remove-VirtualPortGroup -VirtualPortGroup $objOldVPG -Confirm:$false -WhatIf
    Write-Output -InputObject "Adding Virtual Port Group" $strNewVPG "with VLAN Tag" $objOldVPG.VLanID
    New-VirtualPortGroup -Name $strNewVPG -VirtualSwitch $strVSwitch -VLanId $objOldVPG.VLanID -Confirm:$false -WhatIf
}
```

Run it once to check it's doing what you want, then remove the `-WhatIf` tags to run it for real.