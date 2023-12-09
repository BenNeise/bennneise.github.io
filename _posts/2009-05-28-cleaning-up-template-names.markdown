---
layout: post
title: Cleaning up VM template names
date: '2009-05-28 13:45:02'
tags: vmware-vsphere powershell
---


I wrote this today to remove occurrences of the string "Tmpl" anywhere in the name of the template, and then to re-name the template with "Tmpl" as a prefix. It had a higher purpose than keeping everything nice and neat, but it's rather specific to our environment so I won't bother going into the details.

<!--more-->

```powershell
# Get all templates
$objTemplates = Get-Template

# Loop through the templates
foreach ($objTemplate in $objTemplates){
	# Set the $StrInterimTemplateName variable to the template name, replacing the string "Tmpl" with an empty string
	$StrInterimTemplateName = ($objTemplate.Name -replace("Tmpl",""))
	# As the string we've just removed might be anywhere in the name, we need to replace double spaces with single
	$StrInterimTemplateName = ($StrInterimTemplateName -replace("  "," "))
	# And also remove trailing spaces from the start, or the end of the string
	$StrInterimTemplateName = $StrInterimTemplateName.Trim()
	# Display on screen what we're doing (as the "Set-Template" with -WhatIf isn't very clear
	Write-Host Changing `[($objTemplate.Name)`] to `[ Tmpl $StrInterimTemplateName `]
	# Change the Template Name to the $StrInterimTemplateName variable preceeded by "Tmpl", uncomment the #-WhatIf if testing
	Set-Template -Template $objTemplate -Name "Tmpl $StrInterimTemplateName" #-WhatIf
}
```

Despite being quite specific in it's current form, this could easily be modified to rename virtual machines (or indeed any other PowerShell object).

While I suspect there's a more elegant way to do this in fewer steps, it's not *particularly* hacky.