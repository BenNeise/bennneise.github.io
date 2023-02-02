---
layout: post
title: Get VDI Capacity Information from the Horizon View ADAM Database
date: '2014-05-09 08:08:41'
---


Quick script to assist with capacity planning.

```powershell
Connect-QADService -Service "YourConnectionServer"

$ObjVDICapacityData = Get-QADObject -IncludeAllProperties -SizeLimit 0 -SearchRoot "OU=Server Groups,DC=vdi,DC=vmware,DC=int" -Type "pae-ServerPool" | Select-Object Name,@{Name="DisplayName";Expression={$_."pae-DisplayName"}},@{Name="MinProvisioned";Expression={$_."pae-SVIRollingRefitMinReadyVM"}},@{Name="Spare";Expression={$_."pae-VmHeadroomCount"}},@{Name="MaxDesktops";Expression={$_."pae-VmMaximumCount"}},@{Name="MinDesktops";Expression={$_."pae-VmMinimumCount"}}

Disconnect-QADService

$ObjVDICapacityData | Format-Table -Auto
```

The version I'm using here (which is a little too specific to our environment to be posted here), also counts the number of people in the entitlement groups and appends that as a column.