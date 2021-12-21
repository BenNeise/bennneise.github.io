---
layout: post
title: Get the last user to power down a VM
date: '2009-10-12 08:07:40'
---


We can use PowerShell to search through the event logs of a machine object ($objVM in the example below) for events which match a specific pattern  - in this case powering off a machine. Once we have the event object, we can access the properties of the first object in the array (the most recent event).


```
$objEvent = @(
    Get-VIEvent -Entity $objVM | Where-Object{$_.fullFormattedMessage -like"Task: Power off Virtual Machine"}
)
$objEvent[0].userName $objEvent[0].createdTime
```

I recall seeing an alternate way of getting events, which might be faster; if I have time, I'll look it up.


