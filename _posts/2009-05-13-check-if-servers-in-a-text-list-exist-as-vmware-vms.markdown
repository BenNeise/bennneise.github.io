---
layout: post
title: Check if servers in a text list exist as VMware VMs
date: '2009-05-13 12:30:15'
tags: vmware-vsphere powershell
---


I got handed a list of around 1,000 servers today, and asked if any of them were part of our VI environment.

Rather than work through it by hand, I wrote the following script.

<!--more-->

```powershell
# Check if Servers on Text List exist on VMware
# Assumes that the VM object name matches the server's DNS name

# Set this to the text file containing the list of servers, one per line
$strServerList = "C:\path\to\textFile.txt"

# Create empty array for servers which are found
$arrFoundServers = @()

# Assign all of the VM objects to a variable
$objVMs = Get-VM

# Read the list of servers, and assign it to a variable
$strServersOnList = (Get-Content -Path $serverlist)

# Loop through each VM
foreach ($objVM in $objVMs){
	# Loop through each server on the list
	foreach ($strServer in $strServersOnList){
		# If the current VM object name matches the current item on the list
		if ($objVM.Name -Like $strServer){
			# Add it to the array of found machines
			$arrFoundServers += $objVM
		}
	}
}

# Display the list of found machines
$arrFoundServers
```

If your VM object names do not match the DNS names on the list, then this won't work, but I suppose you could combine this with some logic from the [script I wrote to find mismatches](https://ben.neise.co.uk/2009/03/18/vm-object-dns-name-mismatches.html).