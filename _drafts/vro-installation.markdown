---
layout: post
title: vRealize Orchestrator - Installing vRO Standalone
summary: How to create your first workflow using VMware vRealize Orchestrator
---

## What is vRealize Orchestrator?

![vROLogo](/assets/vro_logo.png){: .center-image}

[VMware vRealize Orchestrator](https://www.vmware.com/uk/products/vrealize-orchestrator.html) (vRO) is a a run-book style  application which can help you automate and orchestrate a wide range of tasks. Originally an application called _Dunes Virtual Services Orchestrator_, the company _Dunes Technologies_ was purchased by VMware in 2007. Something of a hidden-gem, vRealize Orchestrator has since been included as part of vSphere and/or vRealize Automation entitlements. vRealize Orchestrator is natively integrated into vRealize Automation or it can be deployed stand-alone as a Linux appliance.

As it's interface is a little different to most other VMware products, it can be a little intimidating. Also, as with [other automation solutions](https://ifttt.com/), VMware also have a tough job selling it ("What can I do with it?" ... "Well, _anything_"). As such a lot of Administrators might be aware of it, but have probably been considering getting around to looking at it "some day".

## How can vRO help you?

vRO is an automation and Orchestration solution. You write Workflows which can then be executed. There are a number of pre-canned workflows which can be dragged-and dropped onto a new workflow to execute in sequence. Workflows can have multiple inputs, and you can make some reasonably presentable and simple to use forms.

From simple tasks ("Snapshot a machine") to more complex, layered solutions with a number of external dependencies. Being VMware, it excels at managing vSphere machines, but it also provides a number of other integrations.

## What can I automate with vRealize Orchestrator?

Out of the box vRO offers functionality to integrate with a number of VMware Products (vSphere, vRealize Automation, NSX) as well as Active Directory. There are also a number of plugins available for other vendor's products (such as F5 and InfoBlox).

If you can't find a plugin for your exact requirements, vRO also has the ability to execute PowerShell and SSH on hosts, as well as making SOAP/REST calls to anything with an API.

## How to Install vRealize Orchestrator

### Before installing vRO

#### Ensure compatibility
Before you go ahead and install vRealize Orchestrator, make sure that the version being installed is compatible with the version of vCenter Server you’ll eventually want to orchestrate. Again, by orchestrate, I mean the process of managing a vCenter Server instance using vRO.  To ensure compatibility, use the VMware Product Interoperability. This will give you an overview of what works with what

Use the [VMware interoperability tool](https://www.vmware.com/resources/compatibility/sim/) to determine product compatibility.

#### Download the appliance
You should be able to download the vRealize OVA from the [VMware website](https://my.vmware.com/group/vmware/details?downloadGroup=VROVA_750&productId=742&rPId=29675)

Orchestrator is distributed as an OVA appliance. This means there’s little you need to do other than ensuring that the following hardware resources are available; 2 vCPUs, 6 GB of RAM and at least 21 GB of disk space. 

Regarding licensing, you’re free to use vRO as long as you have a valid vCenter Server license.

#### Sort networking

While it's downloading sot networking. Get an IP address, netmask, etc. Create DNS A & PTR records.


### Deploying and configuring the OVA

1. Log into the web interface of the vSphere server on which you wish to deploy your vRealize Orchestrator appliance. Note: that this does not necessarily have to be the vCenter Server you want to orchestrate.
1. Using the **Deploy OVF Template** option, locate the downloaded OVA file using the **Browse** button and click **Next**.
![DeployOVA](/assets/deployOva.png)
1. Review the details, click *8Next**
1. Accept the EULA, click **Next**
1. Specify a location where you want the appliance installed. Press **Next**.
1. Specify the host and resource pool to which the appliance will be deployed. Press Next.
1. Review the provisioning settings and accept the license agreement. Press Next in both cases.
1. Select the virtual disk format (thin or thick) and the datastore where the appliance is created. Press Next.
1. Select the network you want the appliance connected to. Press Next.
1. This is where the bulk of the settings are specified. Type in the hostname you want to be assigned to the appliance making sure you have a corresponding DNS A record created for it. It’s best to use static IP addressing meaning you’ll need to set the appliance’s IP address, gateway address, DNS server, and subnet mask. Finally, type in a password for the root account and the domain name; this must match the name of the DNS zone under which you created the A record. Press Next.
1. Review the settings one last time and press Finish to kick the OVA deployment process.
1. Once the appliance has finished deploying, proceed to power it up as you would with any other

### Configuring the vRealize Orchestrator application
Configuring vRO is a multi-faceted affair. As you can see from the appliance’s console screenshot, there are a number of links to various components of vRO these being Orchestrator Control Center, Orchestrator Server, and Appliance Configuration.

#### Orchestrator Control Center
To begin with, decide if you want to deploy a standalone or clustered setup of Orchestrator. For simplicity’s sake, let’s go for a standalone setup. In addition, decide on whether you want to use vRO authentication or vSphere SSO. I’ve chosen the latter since SSO is better suited to managing user accounts and permissions. We’ll use Control Center to do this is as follows:

1. Navigate to `https://your_orchestrator_server_IP_or_DNS_name:8283/vco-controlcenter`. Log in as root.
1. Using the deployment type drop-down box, select **Standalone Orchestrator**. Make sure that the hostname and port number are correct. Press **Next**.
1. Select **vSphere** from the **Configure the authentication provider** drop-down box. Type in the FQDN of the vCenter Server you want to orchestrate and press **Connect**.
1. Press **Accept Certificate** to accept the SSL certificate retrieved from vCenter. Make sure that the common name matches the FQDN specified for vCenter.
1. Type in the credentials for a vCenter administrative account such as `administrator@vsphere.local` and press Register.
1. In the Admin Group field, type in `vsphere.local\Administrators` and click on the Search button to ensure the group exists. Press Save Changes when done.
1. If the changes are successfully committed, you are redirected back to Control Center’s homepage. Before proceeding, you must first sign out and log back in using an SSO account. Go to the far upper right corner of the screen, click on the cog wheel and sign out. Log back in as administrator@vsphere.local.
1. From the home screen, hit the Validate Configuration option to make sure vRO is properly configured.
1. If a server restart is required, you’ll need to reboot the appliance. To do this, navigate to https://your_orchestrator_server_IP_or_DNS_name:5480 and log in as root – use the password set during installation. Hit the Reboot button from the default page as shown next.

IMPORTANT: If you configured vRO to use vSphere authentication as per this post and the hostname specified for the vCenter Server does not match that specified in the SSL certificate (common name), you will not be able to connect to Control Center after rebooting the appliance. This KB article, which I tried, fixes the problem, however, note that you’ll have to go back and re-configure vRO from scratch.

### Integrating vRO with vCenter Server
The next part of the configuration process will register vCenter Server with vRO to enable orchestration. This is a two-part process where we first add the vCenter Server instance to vRO and then register vRO as a vCenter Server extension. To do this, we need to use the standalone vRO client which can be downloaded from the vRO Server page. The client is what enables us to execute workflows against vCenter. Here’s how.

1. Download the Orchestrator client for the relevant OS (Windows, Linux and Mac) from https://your_orchestrator_server_IP_or_DNS_name:8281/vco/.
1. Unzip the archived contents to a folder. Execute vROWorkflowDesigner.exe if you’re running this on Windows. Once you do, type in the vRO’s IP address or hostname and the SSO credentials; the ones you usually use to log in vCenter.
1. Click on the Workflow tab and expand Configuration under the vCenter branch. Select the Add a vCenter Server instance workflow and hit the Play button.
1. Type in the FQDN of the vCenter Server you want to add and make to answer Yes to the Will you orchestrate this instance option. You can choose to ignore any SSL warnings. Press Next.
1. Leave the session option set to Yes and type in the SSO credentials. Leave the domain value blank. Press Submit.
1. Check that there’s nothing wrong with the endpoint names – ex. incorrect FQDN – and press Submit.

If the details provided were correct, the workflow should complete successfully


#### Registering vRO as a vCenter Server extension
Next, we need to register vRO as an extension in vCenter. To do this, we simply execute a second workflow from the same workflow branch as before.

1. Select the Register vCenter Orchestrator as a vCenter Server extension workflow and press Play.
1. Click on Not Set in the vCenter Server instance field. Doing this takes you to a second screen. Expand vSphere vCenter Plug-Ins, highlight the https//<your-vCenter-Server> link as shown and press the Select button.
1. Leave the external address field blank and press Submit.

The workflow should successfully execute if all the details provided were correct.

### Making sure it all works
In theory, at least, you should have a working instance of vRO readily integrated with the vCenter Server you want to orchestrate. In practice, however, the install is rarely plain sailing with some of the common ailments included a missing vRO interface in vSphere Web Client or a non-registered extension.

We first need to verify whether Orchestrator has vCenter Server visibility or not. To do this, we’ll keep on using the standalone client.

1. Change over to the Inventory tab and expand the vSphere vCenter Plug-in branch. You should be able to see the vSphere objects created in vCenter as shown next.
1. We need to restart the vCenter Server (the one you want to orchestrate) to make sure the extension registers correctly. If you have vCSA deployed, SSH to the appliance and run a reboot command from the shell. If you’re running the Windows version, just reboot the machine.
1. Once vCenter is back up, use vSphere Web Client to log in vCenter Server. Select Administration from the Home menu. Under Solution -> Client Plug-Ins, verify that the vCenter Orchestrator plugin has been successfully registered. You can also check the status bar or event monitoring for any events showing that the vRO extension has registered correctly.
1. Go to the Home screen in vSphere Web Client, and verify that the vRealize Orchestrator is now listed under Inventories. Clicking on the icon will launch the Orchestrator plug-in inside vSphere client which essentially gives you access to the functionality provided by the standalone vRealize Orchestrator Client. If the vRO icon is still listed under Plug-ins for installation, you’ll then need to run the registration workflow again.

#### Testing it out by running a workflow
At some point, you’ll be prompted to delegate permission to vRO. Just tick the Remember my decision box so you won’t have to grant permission every time you use vRO.

As a basic test, I’m going to schedule the deletion of a VM I no longer need. To this, I simply right-click on the VM in question and select Shutdown and delete virtual machine. It’s then just a question of filling in the blanks as shown next. You can include multiple VMs to the job if required.
From the Orchestrator main page under Home, you’ll be able to view pending and completed workflows by clicking on Scheduled workflows as shown next.
And sure enough, the test VM was deleted successfully.

## Conclusion
This was quite a lengthy post and I must draw the line here. In terms of workflows and other functionality, there’s a ton more to cover once you have completed the install vRealize Orchestrator, which I’ll try to do in one or more future posts. In the meantime, I need to get up to speed with the product myself since it’s quite a handful. If you want to get a better idea of what you can use vRO for, have a look at this vRO blog.
