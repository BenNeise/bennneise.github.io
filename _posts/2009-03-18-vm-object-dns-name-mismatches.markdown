---
layout: post
title: Resolving Virtual Machine object name and DNS name mismatches using PowerCLI
date: '2009-03-18 12:50:13'
tags: powershell vmware-vsphere
---


We were working recently to align our guest virtual machine object names (the ones shown in vSphere) with their DNS names. As we have over 800 guests, this would have taken us a while to compile by hand. In order to make the process a little easier, I wrote the following PowerShell script to flag machines where the hostname differs from the object name.

<!--more-->

```powershell
# Get all of the VMs as an object
$virtualMachines = Get-VM

# Loop through all of the VMs
forEach ($virtualMachine in $virtualMachines){
    
    # Get the VM Guest object (which contains the DNS information)
    $guest = Get-VMGuest -VM $virtualMachine
    
    # Sometimes the FQDN is empty or blank, so we screen those out
    if ($guest.Hostname){
        # The host name is the first part of the FQDN, so we split it, and take the first (0) segment as our host name
        $virtualMachineHostName = $guest.Hostname.split('.')[0]
    }
    else {
        $virtualMachineHostName = $null
    }
    # Check that the host name is not null, and if the hostname does not match the VM name, echo the results
    if (($virtualMachineHostName) -and ($virtualMachine.Name -notlike $virtualMachineHostName)){
        # Write the results on one line, the VM object name, then the host name
        Write-Output -InputObject "$($virtualMachine.name): $virtualMachineHostName"
    }
}
```

This worked perfectly. While I could have had the script rename these machine objects to the hostname, it was safer to look at each one individually. Even so, the script saved us a few hours of tedious work.

Remember that renaming the object doesn't fix the file and folder names on the datastore. If you do your datastore management via vSphere, this won't matter to you. If you manage files on the datastore directly, then I expect you'll already know how to resolve this.