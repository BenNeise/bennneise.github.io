---
layout: post
title: vSphere bug with DRS, StandBy and non-persistent hard drives
date: '2009-12-09 10:36:55'
tags:
- onyx
- script
- virtualisation
- vsphere
---


WeÔÇÖve been in touch with VMware recently about an issue we were experiencing in vSphere 4, where machines in standby could not be powered on. VMware have now confirmed that this is a bug, and that there will be a fix in R2.

While itÔÇÖs fairly specific to our use-case, I thought IÔÇÖd share the details in case anyone else runs into this.

First of all, this bug will only affect you if the following conditions are met:

- You are using VMware vSphere 4.0 (or 4.0 Update 1)
- Guest OS power-saving settings cause the virtual machine to enter standby
- One or more of the guestÔÇÖs hard drives are set to ÔÇ£independent non-persistentÔÇØ
- DRS is enabled on the virtual machineÔÇÖs cluster

The machine enters standby as normal. The issue arises when you try to power the virtual machine back on: if DRS has allocated the machine to another host based on load the machine will not resume, and gives an error similar to the following:-

> ÔÇ£Virtual Machine is configured to use a device that prevents the operation: Device ÔÇÿHard disk 1ÔÇÖ is disk which is not in persistent mode. Device ÔÇÿHard disk 1ÔÇÖ which is not in persistent modeÔÇØ.

You cannot manually migrate the machine (even back to the original host). You cannot change the power-state on the machine, edit the virtual machine settings, or delete the machine.

If this has happened to you, the only way weÔÇÖve found to get the machine back up-and-running seems to be to remove the machine from inventory, then create a new virtual machine with the same specifications, and add the old machineÔÇÖs VMDK.

Fortunately, there are a couple of workarounds. You can either disable power-saving settings in the guest OS or change the guest power management settings from ÔÇ£Suspend the virtual machineÔÇØ to ÔÇ£Put the guest OS into standby mode and leave the virtual machine powered onÔÇØ (you can automate this as described [in my previous post](http://ben.neise.co.uk/index.php/2009/11/changing-standbyaction-using-powershell-script-generated-with-help-from-onyx/)).

Changing the guest power-management settings means that when the guest enters standby, although vSphere shows the machine as ÔÇ£powered-onÔÇØ, VMware Tools is not running, which can cause problems (i.e., when trying to gracefully shut down a batch of machines).

This was also my first time working with the VMware vSphere support and I was impressed. They quickly replicated the problem and confirmed that it was indeed a bug. As most people nowadays tend to use snapshots rather than non-persistent drives, and few users virtualise desktop operating systems (which are more likely to have power-saving settings on by default) I can understand why this particular set of circumstances went untested.


