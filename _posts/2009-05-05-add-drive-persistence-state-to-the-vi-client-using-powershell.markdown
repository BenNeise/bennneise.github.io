---
layout: post
title: Add disk persistence information to the VI Client using PowerShell
date: '2009-05-05 12:02:40'
tags: vmware-vsphere powershell
---


I've further adapted [Hugo's script](http://www.peetersonline.nl/index.php/vmware/add-snapshot-information-to-the-vi-client-using-powershell/) to add a custom attribute which shows the drive persistence state(s) when the script was run.

<!--more-->

The script also adds drive state information for templates as well as VM objects.

```powershell
$VCServerName = "MyVCServer"
$VC = Connect-VIServer $VCServerName
$SI = Get-View ServiceInstance
$CFM = Get-View $SI.Content.CustomFieldsManager

# Variables
$CustomFieldName = "HD Persistence"
$ManagedObjectType = "VirtualMachine"

# Check if the custom field already exists
$myCustomField = $CFM.Field | Where-Object {$_.Name -eq $CustomFieldName}
if (!$myCustomField){
	# Create Custom Field
	$FieldCopy = $CFM.Field[0]
	$CFM.AddCustomFieldDef($CustomFieldName, $ManagedObjectType, $FieldCopy.FieldDefPrivileges, $FieldCopy.FieldInstancePrivileges)
}

# Get the machine objects
$objVMs = (Get-VM) + (Get-Template)
# Loop through each of the machine objects
foreach ($objVM in $objVMs){
	$strPersistence = ""
	$objHardDisks = $objVM | Get-HardDisk
	# Count the number of hard drives
	$intHardDisks = ($objHardDisks | Measure-Object).count
	# Loop through each of the hard disks
	foreach ($objHardDisk in $objHardDisks){
		# Replace default persisstence states with initials for brevity
		switch ($objHardDisk.Persistence) {
			Persistent {
				$strPersistenceInitial = "P"
			}
			IndependentPersistent {
				$strPersistenceInitial = "IP"
			}
			IndependentNonPersistent {
				$strPersistenceInitial = "INP"
			}
		}
		# Concatenate the initial onto the persistence string
		$strPersistence = "$strPersistence" + $strPersistenceInitial
		# If there are more hard drives to add
		if ($intHardDisks -gt 1) {
			# Append a comma and a space (there may be a more elegant way of doing this)
			$strPersistence = "$strPersistence" + ", "
			# Count down the number of hard drives
			$intHardDisks -= 1
		}
	}
	# Add the $strPersistence to custom attribute $CustomFieldName (HD Persistence)
	if ($strPersistence){
		$VMView = $objVM | Get-View
		$VMView.setCustomValue($CustomFieldName,$strPersistence)
	}
}
```