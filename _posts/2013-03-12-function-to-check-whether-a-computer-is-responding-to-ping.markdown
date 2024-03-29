---
layout: post
title: PowerShell function to check whether a computer is responding to Ping
date: '2013-03-12 12:20:17'
tags: powershell
---

<div class="info">This function will not work on PowerShell Core. But you should probably be using <a href="https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/test-connection?view=powershell-7.4">Test-Connection</a> regardless.</div>

A lot of my scripts use Active Directory to create lists of servers. Unfortunately, AD often contains decommissioned computer objects, which can cause certain queries to time-out

I wrote this quick function so that before running WMI queries against a server, we could do a quick check to see whether it was online.

<!--more-->

```powershell
function IsPingable {
    <#

    .SYNOPSIS
    Pings a server and returns TRUE or FALSE.
     
    .DESCRIPTION
    Uses WMI to ping a server, and returns TRUE if a status code of 0 is returned, otherwise returns FALSE. Useful for quick checks to see if a server exists and is online.
     
    .PARAMETER Computer
    The computer's Hostname, FQDN, or IP to be pinged.
 
    .EXAMPLE
    IsPingable -Computer "SERVER01"
 
    Pings SERVER01
     
    .NOTES
    Ben Neise 12/03/13
     
    #>
    param (
      [Parameter(
          Mandatory=$true,
          Position=0
      )]
      [string]$Computer
    )
    
    $objPing = Get-WmiObject -Class "Win32_PingStatus" -Filter "Address='$Computer'"
    if ($objPing.StatusCode -eq 0){
        $boolPingable = $true
    }
    else {
        $boolPingable = $false
    }

    return $boolPingable
}
```