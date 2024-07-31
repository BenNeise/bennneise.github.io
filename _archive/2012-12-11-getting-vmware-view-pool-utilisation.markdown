---
layout: post
title: Getting VMWare View pool utilisation
date: '2012-12-11 15:36:28'
tags: vmware-horizon-view powershell
---



We needed a way to keep track of how many users had been granted permission on a pool to ensure that there were plenty of provisioned desktops.

Knowing that it's possible to list the number of machines in a pool, and the entitled users and groups using View CMDLets on a connection server via a PSRemote session, and knowing that it's possible to enumerate the total number of users in a group (including indirect membership); it's then just a case of combining the numbers into a single report  - minimum provisioned machines vs maximum number of users.

This script depends on the [Quest AD CMDLets](http://www.quest.com/powershell/activeroles-server.aspx). Some day I'm going to try and wean myself off the Quest tools, as I don't like having to install pre-requisites on all the machines I use. Some-day, but not today.

```powershell
if (!(Get-PSSnapin -ErrorAction SilentlyContinue | Where-Object {$_.Name -eq "Quest.ActiveRoles.ADManagement"})){
    Add-PSSnapin Quest.ActiveRoles.ADManagement
}
#requires -PSSnapin Quest.ActiveRoles.ADManagement
# Create a remote session object to the View connection server
$objRemoteSession = New-PSSession -ComputerName "LON-VICS-01"
# Load the View snapin in the remote session
Invoke-Command -Session $objRemoteSession -ScriptBlock {
    . "C:\Program Files\VMware\VMware View\Server\extras\PowerShell\add-snapin.ps1"
} # Get pools via the remote session
$objPools = Invoke-Command -Session $objRemoteSession -ScriptBlock {
    Get-Pool
}
# Get pool entitlements via the remote session
$objEntitlements = Invoke-Command -Session $objRemoteSession -ScriptBlock {
    Get-PoolEntitlement
}
# Remove the remote session
Remove-PSSession -Session $objRemoteSession
# Filter out manual pools (where deliveryModel would be "Manual", and sort for neat logging
$objPools = $objPools | Where-Object {$_.deliveryModel -eq "Provisioned"} | Sort-Object pool_id
# Loop through the pools
foreach ($objPool in $objPools){
    Write-Output -InputObject "Checking:" $objPool.pool_id
    # Get the groups which are entitled to the pool
    $arrEntitlementsToCurrentPool = @($objEntitlements | Where-Object {$_.pool_id -eq $objPool.pool_id})
    $intUsers = 0
    foreach ($arrEntitledObject in $arrEntitlementsToCurrentPool){
        $objADObject = Get-QADObject $arrEntitledObject.sid 
        Switch ($objADObject.Type) {
            "user" {$intUsers ++}
            "group" {$intUsers += ($objADObject | Get-QADGroupMember -SizeLimit 0 -Indirect).Count}
            Default {Write-Output -InputObject "Entitled object is not a user or group"}
        }
    }
    $objPool | Add-Member -Name "EntitledUsers" -MemberType NoteProperty -Value $intUsers
}
# Display the results, using calculated values to give more descriptive names to the columns
$objPools | Select-Object @{` Name="Pool";Expression={@($_.pool_id)}}, @{Name="Minimum desktops";Expression={@($_.minimumCount)}}, @{Name="Maximum users";Expression={@($_.EntitledUsers)}}, @{Name="Commitment";Expression={@([int]](($_.EntitledUsers / $_.minimumCount) * 100))}} | Sort-Object Pool
```

Although this displays results on screen, there are of course all the normal ways to output the object to HTML, CSV, XML and so on. I'll leave it to your imagination.