---
layout: post
title: Using SDelete to maximise the amount of disk space reclaimed during conversion
  to thin-provisioned disks
date: '2009-10-28 13:48:15'
tags:
- virtualisation
- vsphere
---

We're currently neck-deep in migration at the moment, but despite the workload, it's always worth considering what we can do now, that might save us some time and effort later on.

One of the reasons we were moving to vSphere was the ability to thin-provision (TP) our disks, which we're hoping will allow us to increase the amount of machines that we can provision without needing to allocate more storage (currently 18 TB).  I found an article by [Duncan Epping over at Yellow Bricks](http://www.yellow-bricks.com/2009/07/31/storage-vmotion-and-moving-to-a-thin-provisioned-disk/) suggesting the use of [Sysinternals SDelete](http://technet.microsoft.com/en-ca/sysinternals/bb897443.aspx) utility before the conversion to TP.

Essentially, as deleted files are not zeroed in Windows, and because VMware looks at the raw disk when "deallocating" space during conversion to think provisioned disks; deleted data are not reclaimed.  Running SDelete in the Windows guest before converting the disk to thin provisioned format zeroes the deleted data and should allow the maximum amount of space to be reclaimed.

While I don't doubt that this is all correct, I wasn't sure how much extra space it would allow us to reclaim. The majority of our guests are relatively small windows clients, almost all of which have non-persistent hard drives; of course ÔÇô once they've been made non-persistent, the drive is effectively frozen, and subsequent use won't increase the amount of non-zeroed slack space.

What's the best way to see whether this is worthwhile? Run an experiment of course!


# Method

I took one of our standard Windows XP guests which had been migrated to the new vSphere infrastructure. It had a 10GB hard drive, currently persistent, but which has been ÔÇô for the majority of it's 9 month existence ÔÇô non-persistent. I examined how much disk space it was using, this was the pre-TP "Control". I then cloned it without customization. One of the clones was converted to TP during a Storage vMotion operation. The other had slack space zeroed using SDelete (this process took around 3 minutes). It was then converted to Thin Provisioned disk format using Storage vMotion in the same way as the first machine.


# **Results**

Here's what happened

![](/content/images/2016/01/DiskSpaceUsed1.png)

## Normal (Thick) Disk

- Provisioned Storage: 10.50 GB
- Not-shared Storage: 10.00 GB
- Used Storage: 10.00GB

## Converted to Thin Provisioned

- Provisioned Storage: 10.50 GB
- Not-shared Storage: 5.05 GB
- Used Storage: 5.05 GB

## Converted to Thin Provisioned, **after** running SDelete

- Provisioned Storage: 10.50 GB
- Not-shared Storage: 4.21 GB
- Used Storage: 4.21 GB


# Conclusion

Zeroing slack space on this typical machine saved me 0.84 GB (8.4%). For the minimal effort involved, I think this is worthwhile (I have about 500 more machines almost exactly the same as this).

The percentage of free space reclaimed would likely be higher on persistent machines, or larger machines which see frequent creation and deletion of files.


