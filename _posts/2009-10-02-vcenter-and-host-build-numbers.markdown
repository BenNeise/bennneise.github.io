---
layout: post
title: vCenter and host build numbers
date: '2009-10-02 09:53:07'
tags: vmware-vsphere
---


This is based on [Carter Shanklin's PowerShell snippets to query VC and ESX build version numbers](http://communities.vmware.com/message/1013433#1013433).

This script loops through the list of vCenter servers, and gets their version and build info, as well as the version and build info for it's connected hosts.

<!--more-->

```powershell
# Script to connect to a list of vCenter Servers, and get their version numbers, as well as the version numbers of their hosts
# Ben Neise
# 02/10/09

# Array of vCenter Servers
$arrVCenterServers = @("server1","server2","server3")

# Create empty arrays for the results
$arrTableVCs = @()
$arrTableHosts = @()

# Loop through the array of vCenter servers specified above
foreach ($strVCenterServer in $arrVCenterServers){

	# Connect to the VC
	$objVCenterServer = Connect-VIServer $strVCenterServer

	# Version info about the VC you are connected to
	$viewVCenterServer = Get-View "serviceinstance"

	# Add custom attributes to each VC objects for version and build
	$objVCenterServer | Add-Member -Name Version -Type "noteproperty" -Value ($viewVCenterServer.content.about.Version) -Force
	$objVCenterServer | Add-Member -Name Build -Type "noteproperty" -Value ($viewVCenterServer.content.about.Build) -Force

	# Add the VC object to the results array
	$arrTableVCs += $objVCenterServer

	# When connected to loop through the hosts managed by the VC
	foreach ($objHost in (Get-VMhost | Sort-Object)){

		# Get the view for the current host
		$viewHost = $objHost | Get-View

		# Add custom attributes to the host object for VC server, Host and Version
		$objHost | Add-Member -Name "VCServer" -Type "noteproperty" -Value $objVCenterServer.Name -Force
		$objHost | Add-Member -Name "Host" -Type "noteproperty" -Value $viewHost.Name -Force
		$objHost | Add-Member -Name "Version" -Type "noteproperty" -Value $viewHost.Config.Product.Version -Force

		# Add the host object to the results array
		$arrTableHosts += $objHost
	}
	# Disconnect from the VC server
	Disconnect-VIServer -Confirm:$False
}

# Output the VC results (can be modified to output to a CSV with Export-CSV)
$arrTableVCs | Select-Object Name, Version, Build | Sort-Object Name

# Output the Host results (can be modified to output to a CSV with Export-CSV)
$arrTableHosts | Select-Object VCServer, Host, Version, Build | Format-Table

```


