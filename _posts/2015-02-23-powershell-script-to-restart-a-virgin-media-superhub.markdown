---
layout: post
title: PowerShell script to restart a Virgin Media SuperHub
date: '2015-02-23 10:49:03'
---


![SuperHub](/content/images/2016/01/er_photo_141727.jpg)

**Update 23/03/15 ÔÇô Looks like thereÔÇÖs been [an update](http://community.virginmedia.com/t5/Set-up/Super-Hub-1-amp-Super-Hub-2ac-New-Firmware/td-p/2777016) to the SuperHub which broke the [original version ](https://gist.github.com/GuruAnt/6bff34ad037275723969/d2555a9265baaf1b735d2a6b2aaeadb12a63d2b3) of the script. It has now been updated.**

Sometimes, after a week or so of uptime, I find that wireless access through my Virgin Media SuperHub gets very slow (wired access is fine). Like most IT issues, the issue can be fixed with a restart, but as itÔÇÖs a wireless issue, restarting the router [via the web interface](http://help.virginmedia.com/system/selfservice.controller?CMD=VIEW_ARTICLE&ARTICLE_ID=138977&CURRENT_CMD=SEARCH&CONFIGURATION=1001&PARTITION_ID=1&USERTYPE=1&LANGUAGE=en&COUNTY=us&VM_CUSTOMER_TYPE=Cable) is sometimes out of the question. I usually end up having to go next door and restart the router manually.

To save this occasional annoyance, I wanted to schedule a restart for the router each morning when IÔÇÖm unlikely to be using it. So, over the weekend, I wrote up this little PowerShell function to restart the router remotely using the web interface.

<script src="https://gist.github.com/GuruAnt/6bff34ad037275723969.js"></script>

IÔÇÖve integrated this function into a script, and set it as a scheduled task to run every morning at 5am. (I figure that if IÔÇÖm awake and on the internet at 5am, then I could probably do with a break anyway.)

IÔÇÖm not sure yet what causes the network slowdown, it might be interference from a neighbourÔÇÖs network, or electrical interference, but this seems to be enough to stop it happening.


