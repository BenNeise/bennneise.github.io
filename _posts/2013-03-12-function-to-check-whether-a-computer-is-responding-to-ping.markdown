---
layout: post
title: Function to check whether a computer is responding to Ping
date: '2013-03-12 12:20:17'
---


A lot of my scripts use Active Directory to create lists of servers. Unfortunately, AD often contains decomissioned computer objects, which can cause certain queries to time-out

I wrote this quick function so that before running WMI queries against a server, we could do a quick check to see whether it was online.

<script src="https://gist.github.com/GuruAnt/5434695.js"></script>


