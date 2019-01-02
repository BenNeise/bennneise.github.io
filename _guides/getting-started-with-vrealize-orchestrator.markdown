---
layout: post
title: Getting started with vRealize Orchestrator
---

## What is vRealize Orchestrator?

![vROLogo](/assets/vro_logo.png)

[VMware vRealize Orchestrator](https://www.vmware.com/uk/products/vrealize-orchestrator.html) (vRO) is a a (mostly) GUI based application which can help you automate and orchestrate a wide range of tasks. Originally an application called _Dunes Virtual Services Orchestrator_, the company _Dunes Technologies_ was purchased by VMware in 2007. Something of a hidden-gem, vRealize Orchestrator has since been included as part of vSphere and/or vRealize Automation entitlements. 

As it's interface is a little different to most other VMware products, it can be a little intimidating. Also, as with [other automation solutions](https://ifttt.com/), VMware also have a tough job selling it ("What can I do with it?" ... "Well, _anything_"). As such a lot of Administrators might be aware of it, but have probably been considering getting around to looking at it "some day".

## How can vRO help you?

vRO is an automation and Orchestration solution. You write Workflows which can then be executed. There are a number of pre-canned workflows which can be dragged-and dropped onto a new workflow to execute in sequence. Workflows can have multiple inputs, and you can make some reasonably presentable and simple to use forms.

From simple tasks ("Snapshot a machine") to more complex, layered solutions with a number of external dependencies. Being VMware, it excels at managing vSphere machines, but it also provides a number of other integrations.

## What can I automate with vRealize Orchestrator?

Out of the box vRO offers functionality to integrate with a number of VMware Products (vSphere, vRealize Automation, NSX) as well as Active Directory. There are also a number of plugins available for other vendor's products (such as F5 and InfoBlox).

If you can't find a plugin for your exact requirements, RO also has the ability to execute PowerShell and SSH on hosts, as well as making SOAP/REST calls to anything with an API.

## Assumptions
I'm going to assume you've got as far as having a working vRO server, and you can get logged-in.

## Your first workflow

1. Using the drop-down to the right of the **VMware vRealize Orchestrator** logo, switch to **Design view**
1. Let's create a folder for your new work. In the left-panel, right-click on the top element (yourname @ your server), and select **New Folder**. Give it a name, and click OK. 
1. Now we'll create a workflow inside that folder. Right-click the folder and select **New Workflow**. Call it **Hello World**, and click **Ok**.
1. The workflow will now be opened for editing. On the **General** tab. you can see (among some other things) the **Name** and **Description**
1. Select the **Schema** tab. You should see a **Scriptable Task** in the left pane (if not, search for it). Drag it from that window into the blue line between the green start arrow and the end target
1. Right-click the **Scriptable Task**, and select **Edit**
1. Select the **Scripting** pane, enter the following: `System.log("Hello, world!");`, click **Close**
1. Click **Close**
1. Click the green **Run** arrow above the editing panel
1. Run it after saving
1. Save and close
1. In the navigator, you'll see an execution under the workflwo
1. Right-click and run, you'll see a new exection

## Adding inputs
1. Right click your workflow and click `Duplicate workflow`.
1. Set **New workflow name** as `Hello you`. **Workflow folder** should already be set as the folder you created earlier. You can leave **Copy Version History** as **Yes**.
1. Right-click the new **Hello you** workflow it and selecting **Edit**
1. Select the **Inputs** tab
1. Add a paramater by clicking the yellow arrow, a new item should appear in the panel below
1. Click the default name `arg_in_0` and change the name to `name`
1. Click the **Schema** tab again, right click on the Scriptable Task and select Edit
1. Switch to the **In** tab, and click the button **Bind to workflow parameter / attribute**. Check the box next to `name`.
1. Switch to the Scripting tab, update your script to the following: `System.log("Hello " + name);`. You'll see that name is in pink 
1. Run the workflow by clicking on the **Run** button in the **Schema** view, you should see it output your name in the **Logs** pane.

## Next steps

I'll add another post soon where you can get the workflow to do something more interesting/useful.