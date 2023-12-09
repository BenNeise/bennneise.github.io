---
layout: post
title: Creating shortcuts to PowerShell Scripts
date: '2011-07-27 10:09:40'
tags: powershell microsoft-windows
---


You've probably noticed that when you double-click on a PowerShell script, it is opened for editing rather than being run. This is useful from a security standpoint, and while administrators have no problem opening up the shell and running the script, you've probably made something useful that you want to share with users, and users always need a bit more hand-holding.

![PowerShell shortcut properties](/assets/psshortcut.png)

Assuming that your PowerShell installation is in the default location, you need to append the path to your script in the shortcut path like so:

`%windir%\System32\WindowsPowerShell\v1.0\powershell.exe C:\Scripts\MyUsefulScript.ps1`

If you are wanting to run a PowerCLI (VI Toolkit) script, you also need to add `Add-PSSnapin VMware.VimAutomation.Core` to your script, as the VMware Cmdlets are not loaded by default unless you run it from the VMware Toolkit Shortcut.