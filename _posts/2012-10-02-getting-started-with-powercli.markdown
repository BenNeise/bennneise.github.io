---
layout: post
title: Getting started with VMware PowerCLI
date: '2012-10-02 13:08:12'
tags:
- powershell-2
---


In 2007, I moved from working as an application packager  - responsible for a handful of (VMware Workstation) virtual machines, to a new role supporting a consolidated infrastructure for over 200 packagers who required around a thousand virtual machines on VMware vSphere (at that point still called Virtual Infrastructure).

While I was (and I still am) impressed by VMware's hypervisor based virtualisation, there were a few things that started to grate with such an otherwise excellent product:-

- Performing repetitive tasks  - for example setting a group of virtual hard-drives to non-persistent  - using the vSphere Client GUI was time-consuming (and RSI inducing!).
- There was also no real way of extracting information from vCenter in any structured way. For example, if I wanted to know how many of our Microsoft Windows XP guests had over 512MB RAM allocated to them, they had to be counted manually.

I had a look into [running scripts on the host](http://www.amazon.com/Scripting-VMware-Power-Tools-Infrastructure/dp/1597490598), and toyed with the [Remote CLI Appliance](http://www.vmware.com/download/vi/drivers_tools.html), but it was the [VMware PowerCLI](http://communities.vmware.com/community/vmtn/vsphere/automationtools/windows_toolkit) that unlocked the functionality I'd been looking for.

VMware [PowerCLI](http://communities.vmware.com/community/vmtn/vsphere/automationtools/windows_toolkit) utilises [Windows PowerShell ](https://docs.microsoft.com/en-us/powershell/)to provide a command-line driven interface for your virtual infrastructure. This can dramatically reduce the amount of time taken to perform almost all batch-style tasks, facilitates event driven actions, and enables some pretty advanced reporting functionality.

This is nowhere near a proper introduction in how to use PowerShell or PowerCLI, but should give enough information to get you started, and hopefully make you want to find out more.


## PowerCLI pre-requisites

PowerShell is included in recent versions of Windows; but if you don't have it, you'll need to [download and install the appropriate version of Windows PowerShell](http://support.microsoft.com/kb/968930) for your operating system.

Then you need to [download and install VMware vSphere PowerCLI](http://www.vmware.com/support/developer/PowerCLI/index.html) (registration required).

If you're running PowerShell for the first time you need to change the default execution policy. To do this:

1. As a user with local Administrator rights, run Windows PowerShell (on machines with [UAC](http://en.wikipedia.org/wiki/User_Account_Control), right-click and **Run as Administrator**)
2. In that window, run the command

`Set-ExecutionPolicy - ExecutionPolicy RemoteSigned`

This allows you to run local scripts which have not been signed with a digital signature (which will almost certainly include the scripts you're using to learn). Scripts from remote sources will still require signing.


## Security considerations

The PowerShell security model is designed to address some of the failures of VBScript which was a common attack vector for viruses and other malware. PowerShell scripts (which have a PS1 suffix) do not run by default when invoked in Windows. Also, as noted above, the default execution policy is not to run unsigned scripts. In order to run a script, you need to modify the execution policy, and then run the script name from the command line. While this helps to prevent them from being launched by accident, it does tend to complicate things for new users.

In vSphere, users running PowerCLI scripts have the same permissions as they would get if they logged into vSphere Client. However, as with all scripting languages, when modifications can be made easier and faster, the potential impact of mistakes is made greater. PowerShell includes [specific measures to alleviate risk](http://www.computerperformance.co.uk/powershell/powershell_whatif_confirm.htm), and it's worth being familiar with this functionality before trying anything more complex.


## PowerShell fundamentals

PowerShell works using *CMDlets*. These are typically fairly descriptive, and great care has been taken to make them work in a consistent and logical way. Most CMDlets follow the format *verb-noun*, with modifiers for the target of the action, and any CMDlet specific options. They are not case sensitive.

The downside of the commands being so descriptive is that they are sometimes quite long. In order to alleviate this PowerShell allows Aliases to be created. Most common Windows Shell commands already exist in PowerShell as aliases. For example **CD**, **DIR**, **CLS** & **REN** all work as expected. I find these quite useful when working interactively (entering commands at the prompt for immediate execution), but I tend to avoid them in scripts for the sake of readability.

When launching scripts, you need to use absolute paths. For example, if you want to launch the script **C:\Scripts\ExampleScript.ps1**, when you're in **C:\Scripts** you would either need to enter the whole path, or use **./ExampleScript.ps1.**

In order to use PowerShell, you need to import the PowerCLI commands using

`Add-PSSnapin VMware.VimAutomation.Core`

Running the VMware vSphere PowerCLI shortcut created when you install the application does this on launch.

![PowerCLI_Shortcut](/content/images/2016/01/PowerCLI_Shortcut.GIF)

Running the standard PowerShell shortcut does not.

![PowerShell_Icon](/content/images/2016/01/PowerShell_Icon.png)

You can however add it to your [PowerShell profile](http://www.howtogeek.com/50236/customizing-your-powershell-profile/), which will enable it in all PowerShell sessions, no matter which shortcut you use to launch them.

PowerShell is object-oriented, meaning that the information returned from commands can be easily used as the input for another command.

If you want to put comments into your scripts, PowerShell ignores anything after the **#** symbol.


## Some simple CMDlets

Here are a couple of commands to get you started. Open up the PowerCLI command line using the VMware vSphere PowerCLI shortcut, then enter them as shown.

`Get-Help`

Can display help on the various cmdlets. Running this as above shows the syntax for getting help.

`Get-Command`

Use to find out all the commands containing certain keywords. For exampleÔÇª

`Get-Command *VM`

ÔÇªuses the wildcard character (*) to show all commands that end with VM, this shows all the CMDlets that can be used to operate on virtual machines. Let's try a simple oneÔÇª

`Get-VM`

You should now get an error message saying `You are not currently connected to any servers. Please connect first using Connect-VIServer or one of its aliases.`. Let's do thatÔÇª

`Connect-VIServer Name_of_your_vCenter_Server`

This uses your current windows credentials to connects to the specified server (if you do not have permission, you will be prompted for alternate credentials). You need to connect before you run any VMware specific PowerShell commands. Now try this againÔÇª

`Get-VM`

You should now be looking at a list of virtual machines managed by your vCenter server. You can reduce the scope by adding switches, for exampleÔÇª

`Get-VM  -Name A*`

ÔÇªgets all machines with names starting "A". For more information, try

`Get-Help Get-VM -Detailed`

Variables in PowerShell are always preceded by a $ symbol. You can set a variable to the result of any kind of PowerShell command, for example, you can store the results of a Get-VM in a variableÔÇª

`$objVMs = Get-VM`

then use that variable any time you need it, typing

`$objVMs`

Will display the virtual machine objects stored in the variable. This variable is a collection of objects, each object representing a virtual machine, so we can run more commands against this variable:

`Get-VMGuest -VM $objVMs`

This lists the State, IP Address and guest OS of all your machine objects.

Instead of using variables for commands like this, you can also pipe the result of one command, straight into another. The equivalent of the above command, using pipes rather than variables is

`Get-VM | Get-VMGuest`

The objects output byt he first command are piped straight into the second command. Pipes are used extensively in PowerShell, and many cmdlets can be linked together using pipes. This means you can run some complex commands in PowerShell at the command prompt in one line, rather than resorting to writing a script.

Have a play around with these commands in your test environment before moving onto the next section. As long as you're using **Get-** based commands, (rather than **Set-** or **Remove-**) you shouldn't make any changes, but append **-WhatIf** and/or **-Confirm** to the end of your Cmdlets if you're feeling extra-cautious.


## Example scripts

Like batch files, PowerShell scripts are simply collections of commands linked together into a text file.

Here are a couple of example scripts, showing what can be done. Copy into notepad, and save with a PS1 extension. You should run **Connect-VIServer** interactively before running any of the scripts (or add it as the first line to the script file).

### Get information about a specific machine

<script src="https://gist.github.com/BenNeise/5442438.js" type="text/javascript"></script>This script asks the user for a machine name (using **Read-Host**), then gets the object representing the machine of that name. It then displays the machine object name (the name vSphere uses, the one you used to search) and the machine's power state. It then tries to get the object representing the VM guest, and from that object, it displays the hostname and IP address

### Get all Windows XP machines with more than 2 GB of RAM

<script src="https://gist.github.com/BenNeise/5442585.js" type="text/javascript"></script>  
 This script could easily be modified and used as a component to make modifications on machines fulfilling certain criteria.


## What else can you do?

Almost anything that can be done in the GUI can be done in PowerShell. Machines can be deployed, customized, switched on, migrated between hosts and resource pools etc. Or you could get the last time a machine was switched on, and by whom.

You can also use PowerCLI to report on the status of guests and hosts. Check out Alan Renouf's excellent [PowerCLI Daily Report](http://www.virtu-al.net/2009/08/18/powercli-daily-report-v2/), or Hugo Peeter's script to [track free space in your datastores](http://www.peetersonline.nl/index.php/vmware/track-datastore-free-space/).

One drawback of the API is that performance of cmdlets (especially **Get-VM**) is quite slow. Hopefully this will be addressed in future versions.


## Further resources

There are many tools, example scripts and on-line resources available. Your first stop for help should be the [VMware vSphere PowerCLI Community](http://communities.vmware.com/community/vmtn/vsphere/automationtools/windows_toolkit). I also recommend you keep [Alan Renouf's PowerCLI reference card](http://www.virtu-al.net/2009/05/17/icomasoft-powercli-reference-card/) close-to-hand when you're just starting out.


