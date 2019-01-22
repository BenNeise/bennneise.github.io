---
layout: post
title: Automatically converting machines to thin provisioned format
date: '2010-03-18 10:19:06'
tags:
- onyx
- script
- virtualisation
---


I haven't been posting too much here recently I'm afraid. A lot of the things that I'm currently working on are pretty specific to the environment here, and are not particularly useful (or indeed, interesting) to anyone else.

One of the things I've been doing might be more generally useful. We needed to convert around 700 of our machines to thin-provisioned format. When migrating to the new environment we'd stuck to traditional "thick" machines, as there was a lot of upheaval, and we didn't have the necessary monitoring in place. Now that things have settled, we were looking to take advantage of the thin format to save us some space. We had already run [SDELETE](http://ben.neise.co.uk/index.php/2009/10/using-sdelete-to-maximise-the-amount-of-disk-space-reclaimed-during-conversion-to-thin-provisioned-disks/) on the (non-persistent) machines during the migration, so we were ready to go.

The conversion process is fairly simple: a new option during a storage vMotion. However, the idea of doing this 700 times did not appeal to me, so I wrote the script below to automate the process.

```powershell
# Convert Machines To Thin Provisioned
# Ben Neise 16/03/10
# Create an empty array
$arrMachinesToBeConverted = @()
Write-Host "Getting virtual machine objects" -ForegroundColor Blue
Write-Host ""
# Select the broad category of VMs we're looking at, for example all the machines in a specific blue folder
$objVMs = Get-Folder "Projects" | Get-VM | Sort-Object Write-Host "Generating list of candidates" -ForegroundColor Blue
Write-Host ""
# Loop through all the virtual machines selected
ForEach ($objVM in $objVMs){
    Write-Host "Investigating " -NoNewline Write-Host $objVM -ForegroundColor Blue -NoNewline
    # Skip the rest of the loop if the machine is thin provisioned
    If ($objVM | Get-HardDisk | Where-Object {$_.StorageFormat -like "Thin"}){
        Write-Host " - disks are already thin provisioned" -ForegroundColor DarkGray continue
    } # Skip the rest of the loop is the machine is switched on and non-persistent
    If ($objVM | Where-Object {$_.PowerState -ne "PoweredOff"} | Get-HardDisk | Where-Object {$_.Persistence -notlike "IndependentPersistent"}){
        Write-Host " - switched on and non-persistent" -ForegroundColor DarkGray continue
    }
    # Skip the rest of the loop if the machine is powered-on, and has snapshots
    If ($objVM | Where-Object {$_.PowerState -ne "PoweredOff" -and ($objVM | Get-Snapshot)}) {
        Write-Host " - switched on and with snapshots" -ForegroundColor DarkGray continue
    } 
    # Skips the rest of the loop if the machine has a shared drive and is not set up as fault tolerant (indicating that it's a Linked Clone) 
    # Thanks to Keshav Attrey for this method - http://www.vmdev.info/?p=546) 
    $viewVM = $objVM | Get-View -Property Name,Summary,Config.Hardware.Device
    $unshared = $viewVM.Summary.Storage.Unshared
    $committed = $viewVM.Summary.Storage.Committed
    $ftInfo = $viewVM.Summary.Config.FtInfo 
    If (($unshared -ne $committed) -and (($ftInfo -eq $null) -or ($ftInfo.InstanceUuids.Length -le 1))){
        Write-Host "The machine is a linked clone" -ForegroundColor DarkGray continue
    }
    Write-Host "Added to the list of machines to be converted" $arrMachinesToBeConverted += $objVM
}
Write-Host "Starting Storage vMotions" -ForegroundColor Blue
Write-Host $arrMachinesToBeConverted.Count -ForegroundColor Blue -NoNewline
Write-Host " machines to be converted" -ForegroundColor DarkGray
Write-Host ""
ForEach ($objVM in $arrMachinesToBeConverted | Sort-Object){
    # Get the biggest datastore
    $objBiggestDatastore = Get-Datastore | Sort-Object -Property FreeSpaceMB -Descending
    # Select the datastore from the top of the previously generated list (index 0) and remove the preceeding "Datastore-" from it's ID to give us the MOID
    $strTargetDatastore = ($objBiggestDatastore[0].Id).replace('Datastore-','')
    # Let the user know what's going on
    Write-Host "Migrating machine " -NoNewline 
    Write-Host $objVM -ForegroundColor Blue -NoNewline
    Write-Host ", to Thin Provisioned format on datastore " -NoNewline
    Write-Host $objBiggestDatastore[0] -ForegroundColor Blue -NoNewline
    Write-Host "" 
    # Get the view of the VM we're moving
    $viewVM = Get-View -VIObject $objVM
    # Remove the preceding "HostSystem-" from the VM's Host's ID, giving us the Host's MOID
    $strTargetHost = ($objVM.host.id).replace('HostSystem-','')
    # Create a task specification for the relocation
    $specRelocate = New-Object VMware.Vim.VirtualMachineRelocateSpec
    # Add the target datastore to the specification using the MOID
    $specRelocate.datastore = New-Object VMware.Vim.ManagedObjectReference $specRelocate.datastore.type = "Datastore"
    $specRelocate.datastore.value = $strTargetDatastore
    # Add the host to the specification using the MOID
    $specRelocate.host = New-Object VMware.Vim.ManagedObjectReference
    $specRelocate.host.type = "HostSystem"
    $specRelocate.host.value = $strTargetHost 
    # This is the specification property that makes the disk Thin Provisioned
    $specRelocate.transform = "sparse" 
    # Create the task where the previously specified task is applied to the view of the target VM
    $task = $viewVM.RelocateVM_Task($specRelocate, $priority) 
    # Start the task, and wait for it to complete before continuing
    Get-VIObjectByVIView $task | Wait-Task | Out-Null
}

```

It works through the collection of virtual machine objects in `$objVMs`, and adds them to an array if they pass certain criteria. They must be:-

- Not be currently thin provisioned
- Not switched on and non-persistent
- Not switched on with snapshots
- Not a linked clone (thanks to [Keshav Attrey](http://www.vmdev.info/?page_id=2) for his [method of finding linked clones](http://www.vmdev.info/?p=546))

It then starts a separate loop going through each machine object in the array. I could have integrated the migration task into the first loop, but this approach means you can add a human "sanity-check" if you've got certain machines you don't want to migrate.

The script finds the datastore with the largest amount of free space, and then the actual migration is done using code which I generated using Onyx. The free space on the datastores is re-evaluated before every move. This makes the script quite slow, but this isn't something you want to rush.


