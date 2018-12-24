---
layout: post
title: AppSense and VMware View Horizon Linked Clones
date: '2014-02-24 13:36:47'
---

The move from persistent physical desktops, to non-persistent linked clones (with a separate user personalisation layer) requires rethinking the way in which machines are configured and software is deployed. The challenge is to deliver a consistent, highly available platform with the maximum efficiency. In this case efficiency means utilising Horizon ViewÔÇÖs ability to dynamically provision just enough desktops, while ensuring that the necessary configuration changes are delivered by AppSense.

## Computer configuration

We do the bulk of computer configuration via GPO. This includes things like removing unnecessary Windows Features, optimisation of machines for use as VDI hosts, and using Group Policy Preferences to configure local groups and accounts.

Generic platform software (Java, Flash, Microsoft Office, the App-V Client, etc.) and Windows hotfixes are installed to the all of the Pool Masters via SCCM. Pool specific applications are also deployed to specific pool masters via manually configured SCCM Device Collections. This ensures consistency within pools and ÔÇô where possible ÔÇô between pools. Consistency is obviously important for the users and the people supporting them, but also helps with storage de-duplication.

This process effectively takes a vanilla Windows 7 machine as input, and outputs a configured corporate virtual machine desktop. This means that the majority of changes have been applied before AppSense gets involved.

### Deploying AppSense Agents

The AppSense Client Configuration Agent and the Environment Manager Agent are also deployed to all of the pool masters. We do this via an SCCM package, which configures the MSI so that the clients look towards either the Production, or BCP, AppSense instance (based on their OU).

`MSIEXEC /I "ClientCommunicationsAgent64.msi" /Q WEB_SITE="http://appsense:80/"`

To avoid all linked-clones sharing the Pool MasterÔÇÖs AppSense SID, we need to remove the SID from the pool master. This┬áis done via a shutdown script on a GPO linked to the pool masterÔÇÖs OU.


## User configuration

User configuration is done via AppSense on the linked clones themselves.

As the Environment Manager Configuration is modified at a greater frequency than the pool masters are updated, we donÔÇÖt want it installed on the pool master prior to deployment. Rather we want the machines to download the newest configuration as it becomes available. AppSense allows us to deliver the latest version of the configuration.

![AppSense Configuration Schedule](/content/images/2016/01/AppSense-Configuration-Schedule.png)

Remember, that as weÔÇÖve already applied computer settings via GPO, we donÔÇÖt need to worry about restarting the computer after the AppSense configuration has been installed (which we would need to do in order to apply AppSense start-up actions). WeÔÇÖve also pre-deployed the agents (Environment and Client Communication), which means that the installation of the configuration should proceed fairly quickly.


### Ensuring the machine is ÔÇ£readyÔÇØ for the user

However, this approach did introduce an issue where View was provisioning Linked Clones and marking them as ÔÇ£AvailableÔÇØ (and potentially allowing users to log on) before the configuration had been downloaded. This would result in users getting machines which had not yet had the configuration applied.┬áIn order to give AppSense enough time to deploy new configurations, we introduced an artificial delay to the start-up of the VMware View Agent (WSNM). The OUs which contain the linked clones, have the following start-up script:

```
Get-Service -Name "WSNM" | Stop-Service | Set-Service -StartUpType "Manual"
Start-Sleep -Seconds 300
Get-Service -Name "WSNM" | Start-Service | Set-Service -StartUpType "Automatic"
```
This script results in machines showing as ÔÇ£Agent UnreachableÔÇØ for the first five minutes after starting-up which gives AppSense enough time to deploy the configuration.