---
layout: post
title: Displaying vSphere disk properties (including provisioning & persistence)
date: '2014-02-18 13:29:33'
---


I was doing some tidying of old scripts and came across something I thought it might be useful, so I tidied it up and added some documentation.

![Screenshot showing results of script](/assets/DiskInformation.png)

This PowerShell script uses the [vSphere PowerCLI](https://www.vmware.com/support/developer/PowerCLI/index.html) to display a list of virtual machine disks, file-names, modes (persistent or non-persistent), sizes and whether or not the disk is [thinly provisioned](https://www.vmware.com/products/vsphere/features/storage-thin-provisioning.html). You'll need to connect to one or more vSphere servers first.

```powershell
# Create an empty array for results
$arrResults = @()

# Get the .net view of the virtual machines
$objVMViews = Get-View -ViewType "VirtualMachine" | Where-Object {!$_.Config.Template}

# Loop through the .net view objects representing the machines
ForEach ($objVMView in $objVMViews){
  # Loop through the .net view's devices
  ForEach ($objDevice in $objVMView.Config.Hardware.Device) {
    # Where the device is a virtual disk
    If ($objDevice.GetType().Name -eq "VirtualDisk"){
      # Create a new object to represent the virtual disk
      $objVirtualDisk = New-Object PSObject
      # Append properties to the disk object based on the view object
      $objVirtualDisk | Add-Member -Name "Name" -MemberType NoteProperty -Value $objVMView.Name
      $objVirtualDisk | Add-Member -Name "DeviceLabel" -MemberType NoteProperty -Value $objDevice.DeviceInfo.Label
      $objVirtualDisk | Add-Member -Name "FileName" -MemberType NoteProperty -Value $objDevice.Backing.FileName
      $objVirtualDisk | Add-Member -Name "DiskMode" -MemberType NoteProperty -Value $objDevice.Backing.DiskMode
      $objVirtualDisk | Add-Member -Name "SizeGB" -MemberType NoteProperty -Value ($objDevice.CapacityInKB / 1024 / 1024)
      # If there is a ThinProvisioned property, then the disk is sparse
      If ($objDevice.Backing.ThinProvisioned){
        $objVirtualDisk | Add-Member -Name "ThinProvisioned" -MemberType NoteProperty -Value $True}
      Else {
        $objVirtualDisk | Add-Member -Name "ThinProvisioned" -MemberType NoteProperty -Value $False
      }
      # Append the virtual disk object to the array of results
      $arrResults += $objVirtualDisk
    }
  }
}
# Display the results on screen
$arrResults | Format-Table
```

It's likely that I based the original version of this script on someone else's work as it contained a couple of techniques which I don't tend to use (like [using Select-Object to create object properties](http://blogs.msdn.com/b/mediaandmicrocode/archive/2008/11/26/microcode-powershell-scripting-tricks-select-object-note-properties-vs-add-member-script-properties.aspx)), but I'm afraid I can't remember where, and searching for a couple of keywords brings back no results.