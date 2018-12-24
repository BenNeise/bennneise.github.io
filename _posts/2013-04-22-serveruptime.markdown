---
layout: post
title: Server Uptime (2013 Scripting Games practice)
date: '2013-04-22 08:50:23'
tags:
- 2013-scripting-games
- script
- server
- uptime
- wmi
---


I'm not sure yet if I'll take part in the [2013 Scripting Games](http://blogs.technet.com/b/heyscriptingguy/archive/2013/04/17/2013-scripting-games-competitor-s-guide.aspx); but as the the [practice exercise](http://blogs.technet.com/b/heyscriptingguy/archive/2013/04/18/advanced-practice-for-2013-scripting-games.aspx) dovetailed nicely with a requirement I had, I thought I'd give it a shot.

<script src="https://gist.github.com/GuruAnt/5434335.js"></script>

It was quite different to write something "properly", rather than just knocking something out that'd do the job. I'm not sure that's *exactly* the way I would have done it without the supplied specification; I would have probably just returned total hours and total days, that would have made it easier to sort on a single column when output to an HTML table with formatted with the [jQuery DataTables plugin](http://www.datatables.net/) (which is how I tend to format the output from most scripts). Also the exercise allowed you to assume that the server was online, whereas in the real world, I'd probably use [a simple check to see whether the server was responding to Ping or not](http://ben.neise.co.uk/index.php?s=ping).

This is though, the first time that I've written a function which would accept pipeline input, and the first time I've use the ValidateNotNullOrEmpty parameter validation; as such it's pushed me a little out of my comfort-zone, which is definitely a good thing.


