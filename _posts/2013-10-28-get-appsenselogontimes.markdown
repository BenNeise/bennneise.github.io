---
layout: post
title: Get logon timings from AppSense client log
date: '2013-10-28 14:51:35'
---


I'm doing logon tuning just now for non-persistent VDI desktops  - seeing long it takes to deploy App-V packages on a per-user basis to a generic desktop based on AD group membership. To assist with the tuning, I thought it would be useful to write a quick PowerShell function to gather information from the AppSense event logs in a way that allowed easy sorting, display, recording and comparison.

```powershell
Function Get-AppSenseLogonTimes {
	<#
	.Synopsis
	Returns information about AppSense logon events as recorded by the AppSense event log 
	
	.Description
	Returns, via the AppSense Event log, the Logon Time, Node Name, Action, Start Time and Duration of AppSense logon actions.
	Useful for tuning and optimising AppSense logons.
	The Policy Configuration item "Send events to the Appsense event log" should be enabled for this to work.
	
	.Parameter ComputerName
	The target computer name.

	.Example
	Gets AppSense Logon times from Server1
	
	Get-AppSenseLogonTimes -ComputerName "Server1"
	
	.Notes
	Ben Neise 28/10/2013
	
	#>
	Param (
		[String]
		$ComputerName = $env:localhost
	)
	Try {
		Get-Eventlog -ComputerName $ComputerName -LogName AppSense | Select-Object `
	    @{Name="Logon Time";Expression={@($_.ReplacementStrings[0])}},
	    @{Name="Node Name";Expression={@($_.ReplacementStrings[1])}},
	    @{Name="Action";Expression={@($_.ReplacementStrings[2])}},
	    @{Name="Start Time";Expression={@($_.ReplacementStrings[3])}},
	    @{Name="Duration";Expression={[int]$_.ReplacementStrings[4]}} 
	}
	Catch {
		Write-Error "Can't get AppSense logs from $ComputerName"
	}
}
```
Example output, sorted and piped to Out-Gridview

![Get-AppSenseLogonTimes_ExampleOutput](/assets/Get-AppSenseLogonTimes_ExampleOutput.png)

You need to have **Send events to the AppSense event log** set to **Yes**.

![AppSenseEvents](/assets/AppSenseEvents.png)

If you're using persistent desktops, the function might not be as useful as-is unless you clear the AppSense log at log-off, or parse the results in some way that you only get events for a single logon.

As for the results of the tuning, it looks like we can get 4-5 larger applications (Project, Visio, etc) deployed on a per-user basis while only adding 7-12 seconds to the logon. However, this required a custom installer, which executes the App-V installation in a child-process. Executing the Add-AppvClientPackage CMDlet with a Custom Action caused AppSense to wait until the package had completely loaded before continuing. The slight (3-4 second) delay between logon completing and the application appearing in the Start Menu is acceptable, and delivery using AppSense in this manner is still better than SCCM which can take a minute or two.


