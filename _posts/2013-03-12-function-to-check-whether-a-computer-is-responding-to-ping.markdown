---
layout: post
title: function to check whether a computer is responding to Ping
date: '2013-03-12 12:20:17'
tags: powershell
---


A lot of my scripts use Active Directory to create lists of servers. Unfortunately, AD often contains decomissioned computer objects, which can cause certain queries to time-out

I wrote this quick function so that before running WMI queries against a server, we could do a quick check to see whether it was online.

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
      [string]$Computer = ""
    )
    $objPing = Get-WmiObject -Class Win32_PingStatus -Filter "Address='$Computer'"
    if ($objPing.StatusCode -eq 0){
        $boolPingable=$true
    }
    else {
        $boolPingable=$false
    }
    Return $boolPingable
}
```