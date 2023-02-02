---
layout: post
title: Changing StandByAction using PowerShell script created with help from Onyx
date: '2009-11-27 11:09:33'
---


We're currently having some issues caused by the [convergence of vSphere 4.0, IndependentNonPersistent drives, StandBy and DRS](http://communities.vmware.com/thread/244259?tstart=0) (I'll post more on that later).  As a workaround, we needed to modify 228 machines so that they did not go into hibernation. You can do this though the vSphere Client by right clicking the virtual machine, click **Edit Settings**, go to the **Options Tab**, then select **Power Management**, and changing the radio button. We were wanting to change from "Suspend the virtual machine" to "Put the guest OS into standby mode and leave the virtual machine powered on".

![PowerSettings](/content/images/2016/01/PowerSettings.PNG)

To do this the machines need to be powered down. We had an imminent maintenance window, but it wouldn't allow us the time to make this change manually (even if we wanted to), this necessitated some automation. Unfortunately I had no idea how to go about editing this setting using the PowerCLI, even after a little search through the [VMware PowerCLI community](http://communities.vmware.com/community/vmtn/vsphere/automationtools/windows_toolkit).

This seemed like the perfect opportunity to try out [Project Onyx](https://labs.vmware.com/flings/onyx).

[Carter Shanklin's video](http://blogs.vmware.com/vipowershell/2009/11/project-onyx-is-here.html) does a good job of explaining how to Onyx up and running, and it worked exactly as described (even on my Windows 7 machine).

1. [Download the Onyx files](http://bit.ly/vmwOnyx15) and extract to a folder
2. Run the Onyx executable
3. Click the **Connect** button, and connect to your VirtualCenter server
4. Once that's launched, start vSphere client, but instead of connecting to your VirtualCenter server, connect to **http://localhost:1545** (Carter actually says **1445** in the video, but you can see on screen that he's using **1545**). Use your normal credentials.
5. Ignore the warning about unencrypted traffic (as Carter explains, the unencrypted traffic is local-only, the network traffic is still encrypted
6. Click the **Start **button on Onyx
7. In vSphere client make whatever changes it is that you're wanting to record.
8. Click the **Pause** button on Onyx, and you'll see in the window a script has been created.
9. Copy this into your favourite PowerShell editor, and modify until it's suitable for your purposes.


The original capture from the Onyx Window
```
$spec = New-Object VMware.Vim.VirtualMachineConfigSpec $spec.changeVersion = "2009-11-27T09:16:04.570821Z" $spec.powerOpInfo = New-Object VMware.Vim.VirtualMachineDefaultPowerOpInfo $spec.powerOpInfo.defaultPowerOffType = "soft" $spec.powerOpInfo.defaultSuspendType = "hard" $spec.powerOpInfo.defaultResetType = "soft" $spec.powerOpInfo.standbyAction = "checkpoint" $_this = Get-View -Id 'VirtualMachine-vm-1074' $_this.ReconfigVM_Task($spec)
```

A second capture changing the setting back to isolate the exact line that makes the changes
```
$spec = New-Object VMware.Vim.VirtualMachineConfigSpec $spec.changeVersion = "2009-11-27T09:16:33.872017Z" $spec.powerOpInfo = New-Object VMware.Vim.VirtualMachineDefaultPowerOpInfo $spec.powerOpInfo.defaultPowerOffType = "soft" $spec.powerOpInfo.defaultSuspendType = "hard" $spec.powerOpInfo.defaultResetType = "soft" $spec.powerOpInfo.standbyAction = "powerOnSuspend" $_this = Get-View -Id 'VirtualMachine-vm-1074' $_this.ReconfigVM_Task($spec)
```
And a finished script, which will run it against all machines in a specified blue folder. Comment/uncomment one of the `$specVM.powerOpInfo.standbyAction` lines to choose which option you want.
```PowerShell
$objVMs = Get-Folder "Folder Name" | Get-VM forEach ($objVM in $objVMs){
    $specVM = New-Object VMware.Vim.VirtualMachineConfigSpec
    $specVM.powerOpInfo = New-Object VMware.Vim.VirtualMachineDefaultPowerOpInfo
    $specVM.powerOpInfo.standbyAction = "checkpoint" 
    # Put the guest OS into StandBy Mode and leave the Virtual Machine powered On
    #$specVM.powerOpInfo.standbyAction = "powerOnSuspend"
    # Suspend the Virtual Machine
    $viewVM = Get-View -Id $objVM.Id
    $viewVM.ReconfigVM_Task($specVM)
}
```
I was actually surprised at how easy this was; and I think it's going to make me a bit more adventurous with what I attempt to do via the PowerCLI.


