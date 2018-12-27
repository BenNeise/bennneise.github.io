---
layout: post
title: vSphere 4.0 Update 1 Released
date: '2009-11-20 13:22:27'
tags:
- powercli
- vcenter
- virtualisation
- vsphere
---


VMware have released update 1 for vSphere 4.0.

The following enhancements have been made to ESX (from the [release notes](http://www.vmware.com/support/vsphere4/doc/vsp_esx40_u1_rel_notes.html#whatsnew)):-

> **VMware View 4.0 support**** -** This release adds support for VMware View 4.0, a solution built specifically for delivering desktops as a managed service from the protocol to the platform.
> 
> **Windows 7 and Windows 2008 R2 support  -**This release adds support for 32-bit and 64-bit versions of Windows 7 as well as 64-bit Windows 2008 R2 as guest OS platforms. In addition, the vSphere Client is now supported and can be installed on a Windows 7 platform. For a complete list of supported guest operating systems with this release, see the [*VMware Compatibility Guide*](http://www.vmware.com/resources/compatibility/search.php).
> 
> **Enhanced Clustering Support for Microsoft Windows  -** Microsoft Cluster Server (MSCS) for Windows 2000 and 2003 and Windows Server 2008 Failover Clustering is now supported on an VMware High Availability (HA) and Dynamic Resource Scheduler (DRS) cluster in a limited configuration. HA and DRS functionality can be effectively disabled for individual MSCS virtual machines as opposed to disabling HA and DRS on the entire ESX/ESXi host**. **Refer to the *[Setup for Failover Clustering and Microsoft Cluster Service](http://www.vmware.com/pdf/vsphere4/r40_u1/vsp_40_u1_mscs.pdf)* guide for additional configuration guidelines.
> 
> **Enhanced VMware Paravirtualized SCSI Support****  -** Support for boot disk devices attached to a Paravirtualized SCSI ( PVSCSI) adapter has been added for Windows 2003 and 2008 guest operating systems. Floppy disk images are also available containing the driver for use during the Windows installation by selecting F6 to install additional drivers during setup. Floppy images can be found in the <tt>/vmimages/floppies/</tt> folder.
> 
> **Improved vNetwork Distributed Switch Performance**** -** Several performance and usability issues have been resolved resulting in the following:
> 
> - Improved performance when making configuration changes to a vNetwork Distributed Switch (vDS) instance when the ESX/ESXi host is under a heavy load
> - Improved performance when adding or removing an ESX/ESXi host to or from a vDS instance
> 
> **Increase in vCPU per Core Limit**** -** The limit on vCPUs per core has been increased from 20 to 25. This change raises the supported limit only. It does not include any additional performance optimizations. Raising the limit allows users more flexibility to configure systems based on specific workloads and to get the most advantage from increasingly faster processors. The achievable number of vCPUs per core depends on the workload and specifics of the hardware. For more information see the *[Performance Best Practices for VMware vSphere 4.0](http://www.vmware.com/pdf/Perf_Best_Practices_vSphere4.0.pdf)* guide.
> 
> **Enablement of Intel Xeon Processor 3400 Series**  - Support for the Xeon processor 3400 series has been added. For a complete list of supported third party hardware and devices, see the [VMware Compatibility Guide](http://www.vmware.com/resources/compatibility/search.php).

vCenter 4.0 has also been updated, and now has full compatibility with Windows 7 x86 and x64 versions. Saving the [various hacks that were necessary to get it working](http://xtravirt.com/running-vmware-vsphere-client-windows-7).

Also, the PowerCLI has been updated, and can be found [here](http://blogs.vmware.com/vipowershell/2009/11/powercli-40-u1-is-out.html). There are 68 new CMDLETS, which [Alan Renouf does a great job of explaining](http://www.virtu-al.net/2009/11/20/powercli-bring-on-the-next-version/). I'm especially looking forward to trying out Get\Set-CustomAttribute (no more manipulation of the View object), Move-VMTemplate (no more converting templates to machines), and Get\Set-VMQuestion (for those times when the datastores run out of space for the REDO files necessitated by Non-Persistent disks).

I'm looking forward to investigating the new PowerCLI functionality, and I'm also looking forward to not needing to  manually customise the dozen or so Windows 7 guests I'm deploying next week!


