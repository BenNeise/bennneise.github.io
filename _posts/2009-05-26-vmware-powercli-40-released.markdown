---
layout: post
title: VMware PowerCLI 4.0 released
date: '2009-05-26 13:21:14'
tags:
- powercli
- script
- virtualisation
---


![powerCliLogo](/content/images/2016/01/powerCliLogo.png)
I came back from a week's holiday this morning to find that VMware PowerCLI 4.0 has been released as the successor to VI Toolkit 1.5. The jump from 1.5 to 4.0 is for [version number consolidation, rather than being than indicative of major changes](http://blogs.vmware.com/vipowershell/2009/05/powercli-is-official-whats-new.html).

They have however fixed one of the bugs that's been annoying me, which is the [inability to change drives to non-persistent](http://communities.vmware.com/thread/194369?tstart=0), so I'll need to revisit some of my old scripts from v1.0 and check that they still work.

You can download it from the [community page](http://communities.vmware.com/community/developer/windows_toolkit). I'll follow up with more information when I get a chance to investigate it fully.


