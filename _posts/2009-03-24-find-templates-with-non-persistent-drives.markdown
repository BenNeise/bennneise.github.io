---
layout: post
title: Find vSphere templates with non-persistent disks
date: '2009-03-24 11:41:00'
tags: vmware-vsphere powershell
---


As we're running a development lab, we use a lot of templates for machine deployment and a lot of non-persistent disks to allow machines to be easily restored to a clean-state. We've had issues where machines with non-persistent disks were converted to templates. In this case guest customisation will fail.

This script looks at your templates, and outputs a list of those with non-persistent drives.

<!--more-->

```powershell
# Set up an empty array
$arrTemplatesWithPersistentDrives = @()

# Get all the template objects
$objTemplates = Get-Template

# Loop through each template
ForEach ($objTemplate in $objTemplates){
  # Get the drives associated with that template
  $objHardDisks = $objTemplate | Get-HardDisk
  # Loop through each drive
  ForEach ($objHardDisk in $objHardDisks){
    # If any of the drives are non-persistent, add the template object to the empty array
    If ($objHardDisk.Persistence -match "non"){
      $arrTemplatesWithPersistentDrives += $objTemplate
    }
  }
}

# List the names of the unique templates in the array (as a template with more than one non-perisistent drive would appear more than once)
$arrTemplatesWithPersistentDrives | Sort-Object -Unique | Select-Object Name
```