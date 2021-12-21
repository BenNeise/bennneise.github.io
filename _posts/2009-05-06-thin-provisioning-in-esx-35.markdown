---
layout: post
title: Thin Provisioning in ESX 3.5
date: '2009-05-06 11:45:57'
tags:
- script
- vcenter
- virtualisation
- vsphere
---


One of the nice new features of vSphere 4 is thin provisioning of virtual disks. Thin provisioned (TP) disks will be familiar if you've ever used VMware Workstation where they are used by default, (you need to select *Allocate all disk space now* to create thick disks). Essentially, rather than allocate all disk space at creation, disk space is allocated on the fly, meaning that a 50 GB virtual disk with only 5 GB being used by the guest, would only consume 5 GB of space. This can obviously result in real savings, but it does have an impact on machine performance due to the increased disk provisioning overhead as the machine grows.

VirtualGeek had an interesting article on [thin-provisioning in vSphere 4, and whether this should be done at the VM level, or at the array level](http://virtualgeek.typepad.com/virtual_geek/2009/04/thin-on-thin-where-should-you-do-thin-provisioning-vsphere-40-or-array-level.html). As well as containing a good description of the different disk types (*Thick*, *Thin *& *EagerZeroedThick*), there was a brief mention of using TP disks in VI 3.5. This was the first time I'd heard of this, and despite it's unsupported nature, it deserved some consideration. We're still using VI 3.5, and disk space is probably our number one capacity constraint; the potential opportunity to reduce our disk-footprint without investing in any new hardware or software was too good to pass-up.

I soon discovered that we already used TP disks in a very limited way. One of the options in vCenter's *Clone to Template* operation allows the creation of a *compact* template, and we had been using this to reduce the amount of space used by templates. Templates created in this manner use TP disks, and if you convert that template to a machine, the machine inherits the TP disk. However VMs deployed from the template are created with normal (thick) disks. If you're curious to see if you've got any existing TP machines, Eric Gray wrote a [PowerShell script to find existing thin provisioned disks](http://www.vcritical.com/2009/01/finding-thin-provisioned-virtual-disks-with-powershell/#more-514).

After only a little more digging, my dream of being lauded for increasing our free space overnight came to an end. In an article on [Virtual Future](http://virtualfuture.info/2008/12/vmware-esx-35-and-thinprovisioning/), Sven Huisman wrote:

> Apparently, when you move a VM with a thinprovisioned disk from vCenter server, it converts to a thick-disk. This is because thinprovisioned disks is not integrated with vCenter server yet.
> 
> Also, when you deploy from a template with a thinprovisioned disk, the new VM will get a thick-disk.

I imagine this is what they mean by "unsupported", and this is why the TP functionality in VI 3.5 is largely undocumented.

This changes the conversion process from a one-off time-consuming action to something that would need to be done on an ongoing basis. I think we'll just have to wait until we get the chance to upgrade to vSphere 4.


