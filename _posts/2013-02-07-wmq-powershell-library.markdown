---
layout: post
title: Using the WebSphere MQ PowerShell library
date: '2013-02-07 14:48:28'
tags: powershell
---


![WebSphereMQLogo](/assets/ibm-websphere.jpeg)

I've been doing some work with IBM WebSphere MQ recently. Specifically I've been helping to create a (temporary) reporting and monitoring tool which will periodically check channel status and depth of certain queues. While the application has it's own command-line utility ([MQSC](http://publib.boulder.ibm.com/infocenter/wmqv6/v6r0/index.jsp?topic=%2Fcom.ibm.mq.amqzag.doc%2Ffa15950_.htm)) I've been trying to work using the [WebSphere MQ Windows PowerShell library](http://www-01.ibm.com/support/docview.wss?uid=swg24017698).

<!--more-->

After downloading the file I followed the installation instructions, and immediately ran into the following error when trying to load the snap-in.

```powershell
Add-PSSnapin : The Windows PowerShell snap-in 'IBM.PowerShell.WebSphereMQ' is not installed on this machine. At line:1 char:13 + Add-PSSnapin <<<<; IBM.PowerShell.WebSphereMQ + CategoryInfo : InvalidArgument: (IBM.PowerShell.WebSphereMQ:String) [Add-PSSnapin], PSArgumentException + FullyQualifiedErrorId : AddPSSnapInRead,Microsoft.PowerShell.Commands.AddPSSnapinCommand
```

It seems that this was because I was running it in the (default) 64-bit PowerShell session, rather than an x86 session. This means that if you're running reports, you need to specify the x86 version of PowerShell (on my system this is in `%SystemRoot%\syswow64\WindowsPowerShell\v1.0\powershell.exe`).

The CMDLets also require some server components to be installed (although it will not indicate that there's anything wrong until running a command crashes your Powershell.exe session. I got it working with the options shown below (although I'm not entirely sure which were the critical components).

![WebSphere MQ Setup Options](/assets/WebSphere-MQ-Setup-Options.png)

The documentation provided is pretty good, especially if you're not used to PowerShell. There's a "cookbook" provided in the ZIP file, which is filled with examples. These do tend to focus on running commands locally on the server, if you're running commands remotely, it takes a bit of work to string the necessary commands together to check a remote queue manager.

```powershell
Get-WMQChannelStatus -Channel (` Get-WMQChannel -Name "NAME.OF.CHANNEL" -Qmgr (` Get-WMQQueueManager -Connections (` New-WMQQmgrConnDef -Name "QMGR" -Hostname "SERVER" -Port "nnnn" -Channel "CHANNEL"` ) ) )
```

I also noticed an issue with the Get-ChannelStatus CMDLet, where some channels return a valid status, others return nothing, but most would give me the following error:-

```powershell
Get-WMQChannelStatus : String was not recognized as a valid DateTime. At D:\WebSphereMQAppMonitor\WebSphereMQAppMonitor.ps1:134 char:41 + Get-WMQChannelStatus <<<<; -Channel $channel + CategoryInfo : NotSpecified: (:) [Get-WMQChannelStatus], FormatException + FullyQualifiedErrorId : System.FormatException,WebSphereMQ.GetWMQChannelStatus
```

I believe this is a culture/localisation issue. I tried a number of workarounds based on that assumption, but couldn't get anything to work. I ended up using a horrible cludge; using PowerShell to invoke the [standalone MQSC](http://www-01.ibm.com/support/docview.wss?uid=swg24007769) client, then parsing the results back into a PowerShell object.

We eventually managed to get something which would get the required data, and - as it's PowerShell, it could be presented easily in a any of a number of formats.


