---
layout: post
title: Get the last user to power down a VM
date: '2009-10-12 08:07:40'
tags: vmware-vsphere powershell
---

We can use PowerShell to search through the event logs of a machine object (`$virtualMachine` in the example below) for events which match a specific pattern  - in this case powering off a machine. Once we have the event object, we can access the properties of the first object in the array (the most recent event).

<!--more-->

```powershell
$event = @(
    Get-VIEvent -Entity $virtualMachine | Where-Object {
        $_.fullFormattedMessage -like "Task: Power off Virtual Machine"
    }
)
$event[0].userName $event[0].createdTime
```

I recall seeing an alternate way of getting events, which might be faster; if I have time, I'll look it up.