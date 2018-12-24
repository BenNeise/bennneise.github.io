---
layout: post
title: Defining the CloneFrom attribute of a Blueprint via Build Profile in vRealize
  Automation
date: '2015-05-15 18:03:58'
---


![vRealize Automation](/content/images/2016/01/vRA-Product-Icon-Mac_0.png)

Using┬ávRealize Automation (vRA) to allow your users to deploy their own infrastructure in minutes is great, but if the first thing they┬áneed to do is apply a bunch of patches, theyÔÇÖre not going to be happy. ItÔÇÖs essential that you keep your templates up to date.

Doing so is fairly straightforward ÔÇô clone the existing template, convert it to a running machine, power it on, apply all updates., shut it down and convert it to a template again. You can create a vRealize Automation workflow to do this fairly easily. But once youÔÇÖve done that ÔÇª┬áhow do you go about updating┬áyour vRA blueprints to use the new template?

Normally you would click the browse button┬ánext to the **Clone from** box in the **Build Information**┬átab of the blueprint. This would present you with a list of templates on the attached compute. You would select┬áthe updated version of your template, and save your changes.┬áIf youÔÇÖre using the same parent template for multiple blueprints, then this means you could end up doing this on┬áa large number of blueprints.

So, whatÔÇÖs the alternative?

What we can do instead is we select the parent template using a custom attribute called **CloneFrom**. We can then assign this property using a **Build Profile**, which is then applied to multiple blueprints ([this page contains a good description of Build Profiles](http://www.virtualizationteam.com/cloud/vcac-6-custom-properties-build-profiles-property-dictionary.html)).

Once implemented, we can ÔÇô by updating a single Build Profile ÔÇô update every blueprint which uses this Build Profile. (Even if youÔÇÖare automating the creation and maintenance of Blueprints, updating a single Build Profile property is easier than updating the Clone from property on multiple blueprints.)

As we can (via the Property Dictionary) offer a choice of Custom Properties to the user who is┬árequesting a machine, we can now offer a selection┬áof parent┬áVM templates. Fort example we could present a user with different versions of the template, or we could present a selection of templates with different base applications installed.

One nice effect of this is that as these machines use the same Blueprint, this means that theyÔÇÖre drawn from the same **Maximum per user**. This prevents users from┬ágaming the system by deploying the maximum number of machines for each blueprint type. For example, say youÔÇÖve got a couple┬áof Windows blueprints available to your developers (Vanilla and SQL) with the maximum per user set to 3┬áon each flavour, if the user wants┬á5┬áVanilla, machines┬áthey could deploy 3 vanilla servers and 2 SQL Servers, and just remove┬áor ignore the SQL installation. But, if you have a single blueprint with┬áparent template defined as an attribute, then┬áthe limit for that blueprint is applied across all machines deployed from that blueprint.


# Instructions


## Optional ÔÇô Creating a ÔÇ£placeholderÔÇØ template

One complication is that you must┬ádefine a value in the **Clone from** property of the **Build Information** tab of the blueprint; despite┬áthe fact that itÔÇÖs just going to be overridden by a custom property. In order to avoid confusion, we using a ÔÇ£placeholderÔÇØ┬áVM template which weÔÇÖve┬ánamed┬á**UseCustomProperty**, this should make it clear to anyone else looking at the Blueprint, that weÔÇÖre setting the parent template via attribute.

In vSphere client, all you need to do is create a new machine named **UseCustomProperty**. It does not need to have an operating system installed, but it does need to have a disk. The size of this disk wil be the size shown to the user when they request a machine, so this size should be the same as your template. Of course, as itÔÇÖs Thin Provisioned it only takes up a fraction of that space.


## Creating a Build Profile which can be used to assign a parent template

1. Log into vCAC
2. Go to **Infrastructure**┬á> **Blueprints**┬á> **Build Profiles**
3. Click **New Build Profile**
4. Give the build profile a sensible name and description.
5. Under **Custom Properties**, create a **New Property**
6. Set the **Name** of the property to **CloneFrom**, and set the value to be the name of your template
7. Save your changes ÔÇô remember to click the little green check-mark, before clicking **Ok**!


## Updating a machine to use a parent template┬áassigned via Build Profile

1. Log into vCAC
2. Go to **Infrastructure** > **Blueprints**┬á> **Blueprints**
3. Edit the blueprint of the machine you wish to update
4. Optional: On the **Build Information**┬átab, modify the **Clone from. F**rom the browse menu, select your placeholder machine
5. On the **Properties**┬átab, next to **Build Profiles**, select your Build Profile.
6. Save your changes by clicking **Ok**


## Updating the parent template of a machine already using a parent assigned using a Build Profile

1. Log into vCAC
2. Go to **Infrastructure** > **Blueprints** > **Build Profiles**
3. Edit the build profile for the template which you wish to update
4. Under **Custom Properties**, modify the **CloneFrom **property, setting the new value to be the name of your updated template.
5. Save your changes ÔÇô remember to click the little green check-mark, before clicking **Ok**!


