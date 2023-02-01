---
layout: post
title: Function to check whether a computer is responding to Ping
date: '2013-03-12 12:20:17'
---


A lot of my scripts use Active Directory to create lists of servers. Unfortunately, AD often contains decomissioned computer objects, which can cause certain queries to time-out

I wrote this quick function so that before running WMI queries against a server, we could do a quick check to see whether it was online.

```powershell
Function IsPingable {
    <#
    .Synopsis
    Pings a server and returns TRUE or FALSE.
     
    .Description
    Uses WMI to ping a server, and returns TRUE if a status code of 0 is returned, otherwise returns FALSE. Useful for quick checks to see if a server exists and is online.
     
    .Parameter Computer
    The computer's Hostname, FQDN, or IP to be pinged.
 
    .Example
    IsPingable -Computer "SERVER01"
 
    Pings SERVER01
     
    .Notes
    Ben Neise 12/03/13
     
    #>
    Param (
      [Parameter(
          Mandatory=$true,
          Position=0
      )]
      [string]$Computer = ""
    )
    $objPing = Get-WmiObject -Class Win32_PingStatus -Filter "Address='$Computer'"
    If ($objPing.StatusCode -eq 0){
        $boolPingable=$true
    }
    Else {
        $boolPingable=$false
    }
    Return $boolPingable
}
```