---
layout: post
title: Getting started with Quest AD CMDlets
date: '2013-04-22 21:15:10'
---



# Why use the Quest CMDLets?

When I started writing scripts to┬áquery┬áand modify Active Directory, the [PowerShell AD Module](http://social.technet.microsoft.com/wiki/contents/articles/12031.active-directory-powershell-ad-module-properties.aspx)┬áwasnÔÇÖt quite as mature as it is these days. ┬áEven now, thereÔÇÖs still a bit of [debate about which set of tools is the best](http://windowsitpro.com/blog/and-preferred-set-ad-cmdlets).

ThereÔÇÖs obviously a trade-off between the (now) widely available, integrated, and Microsoft Supported CMDLets and the Quest CMDLets, which need to be downloaded and installed.

While IÔÇÖm in the process of re-writing a few older scripts to remove the dependency on the Quest tools, theyÔÇÖre still my ÔÇ£go-toÔÇØ for simple queries and one-liners. A large part of my preference is probably due to familiarity.


# Downloading and Installing

Download the x86 or x64 package from [Quest](http://www.quest.com/powershell/activeroles-server.aspx), and install.  
 You can either run the ActiveRoles Management Shell for Active Directory, which looks like this:-

[![Quest CMDLet Icon](http://ben.neise.co.uk/wp-content/uploads/2013/04/QuestCMDLetIcon.jpeg)](http://ben.neise.co.uk/wp-content/uploads/2013/04/QuestCMDLetIcon.jpeg)

ÔÇªor start a PowerShell session using your ÔÇ£vanillaÔÇØ shortcut, and run the following command to loads the CMDLets

Add-PSSnapin Quest.ActiveRoles.ADManagement


# Some simple one-liners

Get a user by display name

Get-QADUser -Name "Ben Neise"

Get a user by SamAccountName

Get-QADUser -SamAccountName Ben.Neise

Unlock an account

Get-QADUser -SamAccountName Ben.Neise | Unlock-QADUser

Get a computer by description

Get-QADComputer -Description "Ben Neise"

Reset a password

Get-QADUser -Name "Ben Neise" | Set-QADUser -UserPassword 'Password1'

Find all locked accounts

Get-QADUser | Where-Object {$_.AccountIsLockedOut -eq $true}

You may notice it complaining at this point about

WARNING: This search was configured to retrieve only the first 1000 results. To retrieve more results, increase the size limit using the -SizeLimit parameter or set the default size limit using Set-QADPSSnapinSettings with the -DefaultSizeLimit parameter. Use 0 as the value of size limit to retrieve all possible search results.

So re-run with the suggested parameter

Get-QADUser -SizeLimit 0 | Where-Object {$_.AccountIsLockedOut -eq $true}


# Using the CMDLets in scripts

To ensure that the CMDLets are loaded into the session, you may want to use something like the following. This will load the CMDLets if theyÔÇÖre not already loaded, and exit with an error code if it canÔÇÖt load them.

If (!(Get-PSSnapin -ErrorAction SilentlyContinue | Where-Object {$_.name -eq "Quest.ActiveRoles.ADManagement"})){ Write-Host ("Snapin not currently loaded - Adding Snapin") Add-PSSnapin IBM.PowerShell.WebSphereMQ If (!(Get-PSSnapin -ErrorAction SilentlyContinue | Where-Object {$_.name -eq "Quest.ActiveRoles.ADManagement"})){ Write-Host ("Could not load Quest.ActiveRoles.ADManagement Snapin") # Exit and return an error value (which is picked-up by ActiveBatch) Exit 1 } }


