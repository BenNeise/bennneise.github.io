---
layout: post
title: Datastore alerts via Twitter
date: '2010-05-06 13:28:41'
---


With thin provisioning currently being implemented in our environment, and plans to expand the use of Linked Clones, it's become apparent that we're going to have to start paying close attention to our datastores.

[Eric Gray](http://www.vcritical.com/about/) has done some great stuff with using [VMware vCenter alarms with PowerShell to automatically migrate machines](http://www.vcritical.com/2009/10/powershell-prevents-datastore-emergencies/). And Carter Shanklin's got a [great description of a different method](http://blogs.vmware.com/vipowershell/2009/09/how-to-run-powercli-scripts-from-vcenter-alarms.html), but I was after something which didn't involve making any modifications to the vCenter server. Not everyone here is familiar with the PowerShell/PowerCLI, and I didn't want to put something in place which would require this knowledge to support (or more likely, require me to be dragged off whatever I'm doing to take a look!).

I decided to use a scheduled task, running from the reporting server (which already runs the scheduled tasks for the maintenance and reporting scripts). This would periodically check the datastores, and tweet if they exceeded a certain threshold. The team supporting the servers can easily set up their phones for Twitter alerts from the specific user

I spent some time trying to do this using pure PowerShell, using the techniques described by [Mike Ormond](http://blogs.msdn.com/mikeormond/archive/2009/01/30/updated-twitter-powershell-script.aspx) and [Joe Pruitt](http://devcentral.f5.com/weblogs/Joe/archive/2008/12/30/introducing-poshtweet---the-powershell-twitter-script-library.aspx), but I could not get it to work via our proxy (rather annoyingly it worked intermittently). As a workaround, I ended up using [Blue Onion](http://blueonionsoftware.com/blog.aspx)'s command-line twitter client [TweetC](http://blueonionsoftware.com/blog.aspx?p=b46a526d-03ea-40a2-8563-6f66f4838a57). This stores the twitter username and password in an INI file, and can be called from within a PowerShell script.

```powershell
# Load the PowerCLI
Add-PSSnapin VMware.VimAutomation.Core
# Your VI server $strVIServer = "yourVIServer"
# Percentage free space at which you would like a message
$intThreshold = 10
# Connect to the VI server
Connect-VIServer $strVIServer
# Loop through the datastores
ForEach ($objDatastore in (
    Get-Datastore | Sort-Object FreeSpaceMB | Select-Object Name, @{Name="PercentageFreeSpace"; Expression={[math]::round(($_.FreeSpaceMB / $_.CapacityMB * 100), 1)}})
    ){
    If ($objDatastore.PercentageFreeSpace -lt $intThreshold){
        $objName = $objDatastore.Name $objFreeSpace = $objDatastore.PercentageFreeSpace E:\Tools\tweetC\tweetc.exe "$objName has only $objFreeSpace % remaining"
    }
}
# Disconnect from the VI server
Disconnect-VIServer -Confirm:$false
```

The Twitter account is protected (to save it from getting followed by porn-bots). I can now set it up for device alerts, which should hopefully give me a head's up on any potential problems. I could also implement other alerts in this method. For example, you could ping a critical machine, and tweet if it's not available:

`If ((Get-WmiObject -Class Win32_PingStatus -Filter "Address='CriticalMachineHostname'").StatusCode -ne 0){ E:\Tools\tweetC\tweetc.exe "Critical machine not reposnding to pings!" }`

Ideally I'd like to revisit this, and remove the requirement for TweetC, but in the meantime it seems to be working great.


