---
layout: post
title: Server Uptime (2013 Scripting Games practice)
date: '2013-04-22 08:50:23'
tags: powershell microsoft-windows
---


I'm not sure yet if I'll take part in the [2013 Scripting Games](http://blogs.technet.com/b/heyscriptingguy/archive/2013/04/17/2013-scripting-games-competitor-s-guide.aspx); but as the the [practice exercise](http://blogs.technet.com/b/heyscriptingguy/archive/2013/04/18/advanced-practice-for-2013-scripting-games.aspx) dovetailed nicely with a requirement I had, I thought I'd give it a shot.

<!--more-->

```powershell
function Get-Uptime {
    <#
    .SYNOPSIS
    Gets uptime of computers via WMI and displays results in hours, mins and seconds.
    
    .DESCRIPTION
    Gets uptime of computers and displays results in hours, mins and seconds. Written for http://blogs.technet.com/b/heyscriptingguy/archive/2013/04/18/advanced-practice-for-2013-scripting-games.aspx
    
    .PARAMETER ComputerName
    The hostname, alias, or IP of the computer from which to get the uptime

    .PARAMETER LogFile
    Path to the optional logfile
    
    .EXAMPLE
    Get the uptime of a single server via the pipeline.
    
    "server01" | Get-Uptime
    
    .EXAMPLE
    Get the uptime of a single server via parameter

    Get-Uptime -ComputerName "server01"

    .EXAMPLE
    Get the uptime of a single server and log errors to a file

    Get-Uptime -ComputerName "server01" -Log "C:\Log.txt"
    
    .NOTES
    Ben Neise 2012-19-04
    
    #>
    param (  
        [Parameter(
            Position = 0,
            Mandatory = $true,
            ValueFromPipeline = $true,
            ValueFromPipelineByPropertyName = $true
        )]
        [Alias("ComputerName")]
        [String[]]$strComputers,
    
        [Parameter(
            Position = 1,
            Mandatory = $false
        )]
        [ValidateNotNullOrEmpty()]
        [Alias("Log")]
        [String]$strLogFilePath
    ) 
    process {
        # Get the current time, we do this before the iterating to avoid processing time affecting the uptime results
        $objCurrentTime = Get-Date
        # Iterate through the computers
        foreach ($strComputer in $strComputers) {
            Write-Output -InputObject "Checking uptime on computer:" $strComputer
            if ($strLogFilePath){
                # If the logfile has been defined, write a status message
                ((Get-Date -Format HH:mm:ss) + " - Checking computer: " + $strComputer)  | Out-File $strLogFilePath -Append -Encoding ASCII
            }
            try {
                # Use the .net Static Class System.Net.Dns to resolve computer name to FQDN
                # Then split and convert to uppercase to get a neater hostname
                $strComputer = ([System.Net.Dns]::GetHostEntry($strComputer)).HostName.Split(".")[0].ToUpper()
            }
            catch {
                Write-Output -InputObject "ERROR: DNS can't resolve:" $strComputer
                if ($strLogFilePath){
                    # If the logfile has been defined, write an error message
                    ((Get-Date -Format HH:mm:ss) + " - ERROR: DNS can't resolve: " + $strComputer)  | Out-File $strLogFilePath -Append -Encoding ASCII
                }
                Continue
            }
            try {
                # Get the WMI object representing the Operating System
                $objWMIOperatingSystem = Get-WMIObject -Class Win32_OperatingSystem -Computer $strComputer -ErrorAction SilentlyContinue
                # Convert the WMI date/time into an object
                $objTimeLastStartup = [System.Management.ManagementDateTimeconverter]::ToDateTime($objWMIOperatingSystem.LastBootUpTime)
                # Create a new object for displaying the results
                $objUptime = New-Object PSObject
                $objUptime | Add-Member -Name "Name" -MemberType NoteProperty -Value $strComputer
                # As hours and days are calculated separately, and as we're only reporting hours, the number of days * 24 needs added to the "hours" property
                $objUptime | Add-Member -Name "Hours" -MemberType NoteProperty -Value (($objCurrentTime - $objTimeLastStartup).Hours + (($objCurrentTime - $objTimeLastStartup).Days * 24))
                $objUptime | Add-Member -Name "Minutes" -MemberType NoteProperty -Value ($objCurrentTime - $objTimeLastStartup).Minutes
                $objUptime | Add-Member -Name "Seconds" -MemberType NoteProperty -Value ($objCurrentTime - $objTimeLastStartup).Seconds
                Return $objUptime
            }
            catch {
                Write-Output -InputObject "ERROR: Can't get computer startup time from WMI on:" $strComputer
                if ($strLogFilePath){
                    # If the logfile has been defined, write an error message
                    ((Get-Date -Format HH:mm:ss) + " - ERROR: Can't get computer startup time from WMI on: " + $strComputer)  | Out-File $strLogFilePath -Append -Encoding ASCII
                }
                Continue
            }
        }
    }
}
```

It was quite different to write something "properly", rather than just knocking something out that'd do the job. I'm not sure that's *exactly* the way I would have done it without the supplied specification; I would have probably just returned total hours and total days, that would have made it easier to sort on a single column when output to an HTML table with formatted with the [jQuery DataTables plugin](http://www.datatables.net/) (which is how I tend to format the output from most scripts). Also the exercise allowed you to assume that the server was online, whereas in the real world, I'd probably use [a simple check to see whether the server was responding to Ping or not](http://ben.neise.co.uk/index.php?s=ping).

This is though, the first time that I've written a function which would accept pipeline input, and the first time I've use the ValidateNotNullOrEmpty parameter validation; as such it's pushed me a little out of my comfort-zone, which is definitely a good thing.