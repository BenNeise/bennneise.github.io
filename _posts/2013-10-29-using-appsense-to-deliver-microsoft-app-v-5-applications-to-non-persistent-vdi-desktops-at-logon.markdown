---
layout: post
title: Using AppSense to deliver Microsoft App-V 5 applications to non-persistent
  VDI desktops at logon
date: '2013-10-29 13:37:13'
tags: vmware-horizon-view
---


I'm currently working on user-centric application delivery to non-persistent VDI desktops. The rationale for this is that the more applications which can be delivered dynamically, the fewer pools we need to provision. This suits applications like Microsoft Project and Visio, which both tend to be used by a small number of people on each pool. These apps are too expensive to deploy to non-users, and need [locked-down to fulfil license requirements if deployed under Citrix](http://www.appsense.com/media/19839/microsoft_license_control_whitepaper_us.pdf "AppSense - Microsoft Application License Control  in virtual environments"). User-based deployment via App-V allows the application to be targeted to users in existing pool; however, the non-persistent nature of the desktop means that the application needs delivered quickly (and silently) at each logon.

While App-V integrates with SCCM, user-targeted applications can take a couple of minutes to be available. This isn't really an option for this kind of non-persistent desktop deployment as it's likely to result in confused users whose "missing" applications appear as they're on the phone to the service desk.

We needed a way to deliver applications to users, based on their AD group membership during logon. AppSense (which we already had deployed) seemed ideal. AppSense has wizard-based integration for App-V, but the dialog only allows you to select App-V 4's **SFT** files, not the new **APPV** files created by version 5.

![An App-V dialog box](/assets/post-images/App-VDialog.png){: .center-image }

I started by running a custom (PowerShell) script, using the [new CMDLets](http://blogs.technet.com/b/appv/archive/2012/12/03/app-v-5-0-client-powershell-deep-dive.aspx "App-V 5.0 Client PowerShell Deep Dive"). The script itself is pretty straightforward, checking to see if the CMDLets are loaded (and loading if necessary), adding the client-package from the file, and publishing it. We need to set the `-Global` paramater on the `Publish-AppvClientPackage` as we're running the script under **System** context, and we want it to be visible to the user.

![An App-V Custom Dialog](/assets/post-images/CustomAction.png){: .center-image }

The problem was that AppSense would wait until the script executed before completing the logon. With some of the larger applications, this resulted in a delay of 10-15 seconds before the desktop was usable.

Invoking the PowerShell executable with the command above passed as an argument above worked as intended, but required encoding the path argument in order to escape the pipe character. This meant that a simple installation like

```
PowerShell.exe  -Command {Add-AppvClientPackage -Path "\\apps\app-v$\Microsoft Office Project 2010\Microsoft Office Project 2010.appv" | Publish-AppvClientPackage  -Global}
```

Would turn into this:-

```
PowerShell.exe  -EncodedCommand {QQBkAGQALQBBAHAAcAB2AEMAbABpAGUAbgB0AFAAYQBjAGsAYQBnAGUAIAAtAFAAYQB0AGgAIAAiAFwAXABhAHAAcABzAFwAYQBwAHAALQB2ACQAXABNAGkAYwByAG8AcwBvAGYAdAAgAE8AZgBmAGkAYwBlACAAUAByAG8AagBlAGMAdAAgADIAMAAxADAAXABNAGkAYwByAG8AcwBvAGYAdAAgAE8AZgBmAGkAYwBlACAAUAByAG8AagBlAGMAdAAgADIAMAAxADAALgBhAHAAcAB2ACIAIAB8ACAAUAB1AGIAbABpAHMAaAAtAEEAcABwAHYAQwBsAGkAZQBuAHQAUABhAGMAawBhAGcAZQAgAC0ARwBsAG8AYgBhAGwA}
```

Not the most human-readable command, and it would be difficult to manage more than a few applications.

I got around this by writing up a script which would accept the **APPV** file path as an argument. I converted it to an EXE (using [PowerShell Studio](http://www.sapien.com/software/powershell_studio "PowerShell Studio 2012")) and put it on a share. Conversion to EXE avoided changing the [security policy](http://technet.microsoft.com/en-us/library/ee176961.aspx "Using the Set-ExecutionPolicy Cmdlet") to **Bypass** from **RemoteSigned** (or the requirement to deploy a certificate), and also simplified the command-line used in AppSense. The result looks like this:-

![An App-V execution dialog](/assets/post-images/Execution.png){: .center-image }

This action is run under the **User** - **Logon** node with a condition based on the user's AD group membership. All assigned App-V installations are run synchronously.

As the user's logon no longer waits for the execution to complete, the applications can take around 5-10 seconds to become available after the user is presented with their desktop. The delivery is quick, silent, and easy to document for handover to the team members who will be doing the day-to-day application management.

I'm sure AppSense will add support for App-V 5 in a future release, and it'll be interesting to see what kind of functionality they build-in.