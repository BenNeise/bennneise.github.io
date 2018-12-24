---
layout: post
title: Changing drive letter assignments after deploying a virtual machine from a
  template
date: '2010-01-22 13:36:31'
tags:
- powercli
- script
- virtualisation
---


We've had an ongoing problem with "Sequencing" machines for [Microsoft Application Virtualisation](http://en.wikipedia.org/wiki/Microsoft_Application_Virtualization) (formerly SoftGrid). The virtual machine template is correctly set up with a secondary drive set to Q:\ (the drive letter is integral to the sequencing process). However, when the machines are deployed from the template, the Sysprep part of the customization process [results in the drive being "reset"](http://social.technet.microsoft.com/forums/en-US/itprovistadeployment/thread/694daccd-a48d-4529-9aaa-555cda297038) to the lowest available ÔÇô in this case D:\.

At first, we manually changed these assignments using the Disk Management MMC before setting the drives to non-persistent. Lately, I've been using a DISKPART script, which speeds up the process, but still requires logging into each machine.

I saw Arnim [van Lieshout's post on **Invoke-VMScript** yesterday](http://www.van-lieshout.com/2010/01/powercli-get-wmi-info-from-isolated-guests/), and realised that this could be used to run the DISKPART script on multiple machines. In order to get the TXT file used by DISKPART onto the machine, I'm also using the **Copy-VMGuestFile** command found in [PowerCLI 4.0 Update 1](http://www.vmware.com/support/developer/windowstoolkit/wintk40u1/windowstoolkit40U1-200911-releasenotes.html).

```
# Change drive letter assignment from D to Q
# Gets the specific VMs we're after as an object
$objVMs = Get-Folder "Sequencers" | Get-VM | Sort-Object Name
# Assign the command line required for DISKPART to a variable
$strScript = "IF EXIST D:\ DISKPART /S C:\DiskPart_Change_C_To_Q.txt" 
# Loop through the VMs ForEach ($objVM in $objVMs){ 
    # Let the user know
    Write-Host Copying file to $objVM
    Copy-VMGuestFile -Source "C:\Tools\DiskPart_Change_C_To_Q.txt" -Destination "c:\" -LocalToGuest -VM $objVM -HostUser root -HostPassword password -GuestUser Administrator -GuestPassword password 
Write-Host Changing disk partitions on $objVM
    Invoke-VMScript $strScript -vm $objVM -HostUser root -HostPassword password -GuestUser Administrator -GuestPassword password -ScriptType "bat"
}
```
The TXT file contained the following:-

`SELECT VOLUME 2 ASSIGN LETTER=Q`

This requires root credentials for the host, and administrator rights on the target machine, but, as Arnim notes, will work in the absence of client network connectivity.

This is a bit of a hack; leaving the TXT file behind on the C drive; using root credentials rather than an account with the least effective permissions; and having the script contain the credentials in plain-text. However, I'm enthusiastic about using this solution in a more structured way in future. I'm already thinking about using it to defragment and [SDelete](http://technet.microsoft.com/en-us/sysinternals/bb897443.aspx) our thick-provisioned virtual machines before converting them to Thin provisioned disks.


