---
layout: post
title: Using the vRealize 7.x REST API to get a tenant's Event Broker subscriptions
date: '2018-02-14 10:37:07'
tags: vmware-aria-automation
---

After migrating from vRealize Automation (vRA) 6.2, we've recently started the long-overdue work of investigating the new functionality introduced with the event broker. We're still using the state-change triggered workflows for machine life-cycle integration between vRA and vRealize Orchestration (vRO), and that's going to be a big-job to change; but I thought I could maybe look at one of our other requirements which was to ensure that changes to blueprints made using the GUI get stored in source control.

<!--more-->

I managed to configure a simple use-case which was a trigger which will fire whenever a change is made to a blueprint. I got everything working in our development environment, then wanted to move the work to the live environment.

Our normal process for promoting objects (blueprints, reservations, property definitions, etc.) is to use the REST API to GET the JSON from the development environment, then PUT/POST it to live. This ensures that the GUIDs are consistent, and saves someone having to recreate complex objects. We've got some internal PowerShell modules to help with this, and some Jenkins jobs to manage promotion.

As this was the first subscription we've created, we had none of this available, so my first task was checking that I could GET the JSON representing the event broker subscription which I'd just created.

The [documentation](https://code.vmware.com/apis/164/vra-advanced-designer#!/get45operation/get_api_event_broker_subscriptions) suggested that I should be able to run the following operation:-

`GET https://<vraServer>/advanced-designer-service/api/event-broker/subscriptions`

However, when I tried this, in [Postman](https://www.getpostman.com/) using a Tenant Administrator account, I got the following response:-

```javascript
{
    "errors": [
        {
            "code": 50505,
            "message": "System exception.",
            "systemMessage": "Access is denied",
            "moreInfoUrl": null
        }
    ]
}
```
When I tried using `administrator@vsphere.local`, the result was slightly better as I got an empty array.

The documentation _does_ make some reference to per-tenant scoping:-

> **Workflow Subscriptions**
> 
> Workflow subscriptions use the event broker service to monitor the registered services for event messages in vRealize Automation, and then run a specified vRealize Orchestrator workflow when the conditions in the subscription are met.
> 
> To configure the subscription, you specify the event topic, the triggering conditions, and the workflow that runs when triggered.
> 
> Tenant administrators can create and manage the workflow subscriptions that are specific to their tenant. The system administrator can create and manage system workflow subscriptions. The created system workflow subscriptions are active for events in any tenant and for system events.

So. on a hunch, I tried scoping the query, in much the same way as the other XaaS (Advanced Service Designer) queries:-

`GET https://<vraServer>/advanced-designer-service/api/tenants/<tenantId>/event-broker/subscriptions/`

In this case, as I was using the default tenant, the `tenantId` was simply `vsphere.local`. This worked perfectly, allowing me to GET the JSON.

Now, the next job is to wrap-up all of the CRUD operations into our PowerShell module!