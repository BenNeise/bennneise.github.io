---
layout: post
title: Manually creating linked clones in vSphere
date: '2010-01-13 16:18:57'
tags:
- script
- virtualisation
- vsphere
---


We've started our first "proper" implementation of Linked Clones in our vSphere 4 environment. While we've done some limited proof-of-concept work, this is the first project to be entirely deployed using Linked Clones. The objective is to reduce the space used by our training machines on our new environment.

Linked clones allow multiple machines to share a common read-only "base" VMDK file, with each machine generating their own delta (REDO). Under normal usage circumstances, the REDO would continue to grow throughout the life of the machine; however as our machines have non-persistent hard drives, they reset to a clean state when powered-down. This makes our environment ideally suited to taking advantage of the functionality offered by Linked Clones. They can either be created manually (by moving and renaming files on the datastore), or via the APIs, you can get more information on them in this [White Paper from VMware](http://www.vmware.com/support/developer/vc-sdk/linked_vms_note.pdf).

Our training machines are functionally identical to our production machines, and similarly consist of three types  - Capture, Packaging and Verification. These are 11, 8, and 8 GB respectively. The usage patterns are slightly different, as  - unlike "live" projects which have a steady stream of work, trainees tend to come in in large batches. This means that the training environment either needs to be continuously large, but mostly idle, or it needs to be regularly redeployed then stripped back.

The benefits achieved via the implementation of Linked Clones in this project resulted in roughly the same ratio of space saving as our proof-of-concepts, but as the number of machines involved was greater, the differences are more pronounced. Also this is the first time we have exceeded 8 machines sharing the same VMDK, which is a notable milestone as it is only possible if we limit the number of possible hosts that the machines can run on ([there is a VMFS limitation of 8 hosts accessing a VMDK concurrently](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1003319)). As we have DRS enabled, this meant reducing the number of hosts in each cluster to 8 or less.

We deployed twenty-five machines each, of  the three different builds used in a project. All were Windows XP virtual machines

The three machines being used as the parents had their [slack space on the drives was cleaned](http://ben.neise.co.uk/index.php/2009/10/using-sdelete-to-maximise-the-amount-of-disk-space-reclaimed-during-conversion-to-thin-provisioned-disks/) using [SDelete](http://technet.microsoft.com/en-us/sysinternals/bb897443.aspx), then the machine was converted to Thin Provisioned using Storage vMotion. It was switched off, and a snapshot was created. This snapshot will form the base for the parent's clones.

The machines were deployed using the a script similar to the one at the bottom of this post, and it took just over an hour to deploy and customize all 75 machines. This was considerably faster than the time it would have taken to deploy 75 machines using the normal "Deploy from template"  method.

Here are the data:-

- Estimated space used if deployed traditionally: **675 GB**- Capture: 11 GB per machine
- Packaging: 8 GB per machine
- Verification: 8 GB per machine

- Estimated Space if Deployed as Thin Provisioned, but not Linked Clones: **238.75 GB**- Capture: 3.34 GB per machine
- Packaging: 3.72 GB per machine
- Verification: 2.49 GB per machine

- Space used in current configuration: **19.3 GB**- Capture 3.34 GB for parent, plus 0.13 GB per Linked Clone
- Packaging 3.72 GB for parent, plus 0.13 GB per Linked Clone
- Verification 2.49 GB for parent, plus 0.13 GB per Linked Clone

And in graph-format, for extra impact:-

[![DiskSpaceUsed](http://ben.neise.co.uk/wp-content/uploads/2010/01/DiskSpaceUsed1-300x178.png)](http://ben.neise.co.uk/wp-content/uploads/2010/01/DiskSpaceUsed1.png)

All size estimates are based on the machines in a powered-down state. When powered on, a swap file (equal to the size of the assigned RAM) is created, and (assuming the machines are non-persistent) REDO files are created on all types of machines.

I've been on a few of the machines and they don't appear to suffer from any noticeable performance degradation, although the true test won't come until we get considerable concurrent use.

I'm tentatively declaring this a huge success. Rather than the training environment using 240 GB between training engagements, it's now down to a svelte 20 GB, with no reduction in functionality.

Below is a script similar to the one I used to deploy the linked clones. The actual "meat", which deploys the machines was based on Hal Rottenberg's [New-LinkedClone.ps1](http://poshcode.org/1549) script. As far as possible, I've tried to strip out stuff that's specific to our environment (we use the Custom Attributes as an asset management database and to track which machines were deployed from which templates). There's probably going to be stuff in there that doesn't make much sense, but if you've got a bit of an understanding of PowerShell, you should be able to cut and keep the bits you want.

<script src="https://gist.github.com/GuruAnt/7216369.js"></script>


