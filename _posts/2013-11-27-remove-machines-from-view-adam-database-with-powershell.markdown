---
layout: post
title: Remove machine objects from VMWare View's ADAM database with PowerShell
date: '2013-11-27 16:45:16'
---

**26/02/14  -  I've updated this script to accept pipeline input and work a little more efficiently when removing multiple machines.**

It's one of those things that shouldn't happen, but which inevitable does. Someone removes a View managed VM from vSphere, and View refuses to realise it's gone. It also sometimes happens when machines fail to provision correctly (i.e., due to lack of available storage). The [procedure](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1008658) is easy enough to follow, but it's time-consuming and prone to error. In order to make the cleanup operation easier, I wrote up a quick function below. It relies on the free [Quest AD CMDLets](http://www.quest.com/powershell/activeroles-server.aspx "Quest AD CMDLets").

<script src="https://gist.github.com/BenNeise/7678224.js"></script>

You'll want to change **yourconnectionserver** to  - *well*  - your connection server. Obviously the normal caveats apply: the ones about running scripts you download from the internet in your Production environment.


