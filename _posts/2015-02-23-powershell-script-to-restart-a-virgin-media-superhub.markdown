---
layout: post
title: PowerShell script to restart a Virgin Media SuperHub
date: '2015-02-23 10:49:03'
tags: home powershell
---


![SuperHub](/assets/er_photo_141727.jpg){: .center-image]}
<div class="info">This almost certainly will not work anymore, but I'm leaving it here in case it's useful to anyone doing anything similar.</div>

Sometimes, after a week or so of uptime, I find that wireless access through my Virgin Media SuperHub gets very slow (wired access is fine). Like most IT issues, the issue can be fixed with a restart, but as it's a wireless issue, restarting the router [via the web interface](http://help.virginmedia.com/system/selfservice.controller?CMD=VIEW_ARTICLE&ARTICLE_ID=138977&CURRENT_CMD=SEARCH&CONFIGURATION=1001&PARTITION_ID=1&USERTYPE=1&LANGUAGE=en&COUNTY=us&VM_CUSTOMER_TYPE=Cable) is sometimes out of the question. I usually end up having to go next door and restart the router manually.

<!--more-->

To save this occasional annoyance, I wanted to schedule a restart for the router each morning when I'm unlikely to be using it. So, over the weekend, I wrote up this little PowerShell function to restart the router remotely using the web interface.

```powershell
function Restart-VirginRouter {
    <#
    .Synopsis
    Restarts a Virgin Media Suberhub.

    .Description
    Restarts a Virgin Media Suberhub using the web interface.
    
    .Parameter RouterIP 
    The IP address of the router.

    .Parameter Username
    The username used to log into the web interface.

    .Parameter Password,
    The password used to log into the web interface.

    .Example
    Restart-VirginRouter -RouterIP "192.168.0.1" -Username "admin" -Password "hunter2"

    Restarts the router using the specified credentials.

    .Notes
    Ben Neise 23/02/15

    #>
    param (
    
    [Parameter(
        Mandatory = $true,
        Position = 1
    )]
    [string]    
        $RouterIP,
    
    [Parameter(
        Mandatory = $true,
        Position = 2
    )]
    [string]    
        $Username,

    [Parameter(
        Mandatory = $true,
        Position = 3
    )]
    [string]    
        $Password
    )

    # Login
    $loginParams = @{
        VmLoginUsername = $username;
        VmLoginPassword = $password;
        VmLoginErrorCode = 0;
        VmChangePasswordHint = 0
    }
    $r1 = Invoke-WebRequest -Uri ("http://" + $routerIP + "/") -SessionVariable "Session" -Verbose
    Invoke-WebRequest -Uri ("http://" + $routerIP + $r1.forms[0].action) -Method "POST" -Body $loginParams -WebSession $Session -Verbose

    # Restart
    $restartParams = @{
        VmDeviceRestore = 0;
        VmDeviceReboot = 1
    }
    $r2 = Invoke-WebRequest -Uri ("http://" + $routerIP + "/VmRgRebootRestoreDevice.asp") -WebSession $Session -Verbose
    Invoke-WebRequest -Uri ("http://" + $routerIP + $r2.forms[0].action) -Method "POST" -Body $restartParams -WebSession $Session -Verbose
}
```

I've integrated this function into a script, and set it as a scheduled task to run every morning at 5am. (I figure that if I'm awake and on the internet at 5am, then I could probably do with a break anyway.)

I'm not sure yet what causes the network slowdown, it might be interference from a neighbour's network, or electrical interference, but this seems to be enough to stop it happening.


