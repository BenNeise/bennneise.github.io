---
layout: post
title: Add disk size information to the VI Client using PowerShell
date: '2009-04-29 11:41:47'
---


This is based on Hugo Peeters' script to [add snapshot information to the VI client using PowerShell](http://www.peetersonline.nl/index.php/vmware/add-snapshot-information-to-the-vi-client-using-powershell/).

Our users occasionally need larger machines created for packaging big applications.  After increasing the size, we used to append the VM Object name (e.g, "PACKVM01  - 10GB"), but this caused a mismatch between the virtual machine object name in VIC and the DNS host name. Also, it looked untidy!

We needed a new way for VIC users to easily see which were the larger machines, so I modified Hugo's script to add disk size as a custom attribute.

```powershell
$VCServerName = "MYVCSERVER"
$VC = Connect-VIServer -Server $VCServerName
$SI = Get-View ServiceInstance
$CFM = Get-View $SI.Content.CustomFieldsManager
 
# Variables
$CustomFieldName = "HD Size (GB)"
$ManagedObjectType = "VirtualMachine"

# Check if the custom field already exists
$myCustomField = $CFM.Field | Where {$_.Name -eq $CustomFieldName}
If (!$myCustomField){
	# Create Custom Field
	$FieldCopy = $CFM.Field[0]
	$CFM.AddCustomFieldDef($CustomFieldName, $ManagedObjectType, $FieldCopy.FieldDefPrivileges, $FieldCopy.FieldInstancePrivileges)
}
 
$objVMs = Get-VM
ForEach ($objVM in $objVMs){
	$objTotalDiskSize = 0
	# Sum the total size of all disks attached to the VM
	ForEach	($objHardDisk in ($objVM | Get-HardDisk)){
			$objTotalDiskSize += ($objHardDisk.CapacityKB/1024/1024)
			}
	If ($objTotalDiskSize){
		# Round the size to one decimal place
		$objHDSize = "{0:N1}" -f $objTotalDiskSize
		$VMView = $objVM | Get-View
		$VMView.setCustomValue($CustomFieldName,$objHDSize)
	}
}
```


