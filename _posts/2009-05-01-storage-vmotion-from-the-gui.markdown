---
layout: post
title: Storage vMotion from the GUI
date: '2009-05-01 13:01:02'
---


While I'm a big fan of the command-line, there are times when you just want to be able to do something from the GUI.

Storage vMotion is usually only available using the [rCLI Appliance](http://www.vm-help.com/esx/esx3i/Import_RCLI_Appliance.html) but this [VI plug-in](http://sourceforge.net/projects/vip-svmotion/) allows you to do this task from the context menu in VIC, simply install, restart VIC if necessary, then get moving those VMs.

![SVMotion screenshot](/content/images/2016/01/svmotionplugin.jpg)

An option to move more than one VM at a time would be nice, and you still can't move non-persistent machines; but it's still easier than connecting to the rCLI.


