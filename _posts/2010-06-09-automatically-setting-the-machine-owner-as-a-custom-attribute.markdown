---
layout: post
title: Automatically setting the machine owner as a custom attribute
date: '2010-06-09 08:49:58'
tags: vmware-vsphere powershell
---

As we are constantly creating, moving, renaming and deleting machines, it's difficult enough to keep track of machines I have deployed myself; never mind keeping track of what the other team members are doing.

In order to try make it easier to find the owner of a machine, we implemented a custom attribute "Infrastructure Consultant", which the analyst should complete. Inevitably, despite the best of intentions, this is occasionally missed, and we end up with machine of unknown provenance.

The following script sorts this by finding machines where the custom attribute is empty, then populating it with a best guess, based on the machine's event log.

<!--more-->

It looks for three types of events:-

- "Deploying..." covers machines which have been deployed from another template
- "Creating..." covers machines which have been imported via VMware Converter
- "Clone of..." covers machines cloned from existing machines

This seems to cover everything on our environment. If you find something else, then it should be simple enough to add it.

```powershell
# Name of the custom attribute which we are wanting to check/update $strCAInfrastructureConsultant = "Infrastructure Consultant"
# Loop through all the machines
foreach ($objVM in (Get-VM | Sort-Object Name)){
    Write-Output -InputObject "Checking " -NoNewline
    Write-Output -InputObject $objVM -ForegroundColor Blue
    # If the specified custom attribute is empty
    if ($objVM.CustomFields.Item($strCAInfrastructureConsultant) -eq ""){
        # Find the username of the person who created the machine. As this is returned in Domain\Username format, we split it, and take the second portion
        $strInfrastructureConsultant = ((@(($objVM | Get-ViEvent | Where-Object {$_.FullFormattedMessage -match "Deploying*" -or $_.FullFormattedMessage -match "Creating*" -or $_.FullFormattedMessage -match "Clone of*"} | Select-Object Username)))[0].Username).Split("\")[1]
        Write-Output -InputObject "Adding " -NoNewline -ForegroundColor DarkGray
        Write-Output -InputObject $strInfrastructureConsultant -NoNewline -ForegroundColor White
        Write-Output -InputObject " as Infrastructure Consultant" -ForegroundColor DarkGray
        # Write that username to the custom attribute
        ($objVM | Get-View).setCustomValue($strCAInfrastructureConsultant,$strInfrastructureConsultant)
    }
}
```
This doesn't take a long time to run, and will hopefully catch all those occasions where we forget to complete the custom attributes on the machine. It could of course be easily modified to check/update any other custom attribute.


