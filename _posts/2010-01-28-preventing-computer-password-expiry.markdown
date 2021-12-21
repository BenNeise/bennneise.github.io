---
layout: post
title: Preventing computer password expiry
date: '2010-01-28 14:53:45'
tags:
- powercli
- script
---


If, like me, you work with non-persistent virtual machines on Windows domains, you will be familiar with your machines becoming periodically disconnected from the domain. This usually manifests itself in the following error message when you attempt to log on:-

> "The trust relationship between this workstation and the primary domain failed."

The problem is detailed in this [KB Article](http://support.microsoft.com/kb/162797). What happens is that every 30 days (by default) the client initiates a computer password change on the domain controller. This computer password is used to authenticate the computer as the computer object in AD, and is distinct from the user's password. When the non-persistent machine resets, the passwords go out of synchronisation and domain authentication fails.

As per [Microsoft's KB article](http://support.microsoft.com/kb/154501/), this can be fixed by disabling the client-initiated computer password changes. This change can be implemented using Local or Group Policy, with a shell script, or by directly editing the registry. Instructions for each of these are below.

# Using local, or group policy

Set the key shown below to **Enabled**  
[![](http://ben.neise.co.uk/wp-content/uploads/2010/01/GPO.png "GPO")](http://ben.neise.co.uk/wp-content/uploads/2010/01/GPO.png)

# Using REGEDIT

Set the below value to **1**  
[![](http://ben.neise.co.uk/wp-content/uploads/2010/01/Regedit.png "Regedit")](http://ben.neise.co.uk/wp-content/uploads/2010/01/Regedit.png)

# Using Windows shell script

```batch
:: Set registry key to disable computer password expiry
REG ADD "HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters" /v DisablePasswordChange /t REG_DWORD /d 1 /f
```

If you've got access to the Domain Controller, you can also set a GPO so that **Domain Controller: Refuse Machine Password Changes** is **Enabled**. This is in `Windows Settings \ Security Settings \ Local Policies \ Security Options` (the same location as the **Domain Member: Disable Machine Account Password Changes**).

If you need to rejoin machines that have already fallen off the domain, you can skip the reboot after removing it from the domain, so:

1. Shut the machine down
2. Make the drives Persistent
3. Start the machine and log in
4. Remove the machine from the domain
5. Add the machine to the domain
6. Reboot
7. Shut-down and make Non-Persistent

Skipping the middle reboot saves a couple of minutes (which adds up if you have a lot to do). The above processes can also be scripted through the use of PowerCLI with Invoke-VMCommand and either NETDOM (for XP/Vista) or PowerShell for Windows 7.

While this issue also happens with machines which have been off the domain for some time, non-persistent machines (as used in a lab, or test environment) require that this issue be systematically fixed as it's more than an occasional annoyance.


