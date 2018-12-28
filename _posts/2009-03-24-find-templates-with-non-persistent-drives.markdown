---
layout: post
title: Find vSphere templates with non-persistent disks
date: '2009-03-24 11:41:00'
tags:
- script
---


As we're running a development lab, we use a lot of templates for machine deployment and a lot of non-persistent disks to allow machines to be easily restored to a clean-state. We've had issues where machines with non-persistent disks were converted to templates. In this case guest customisation will fail.

This script looks at your templates, and outputs a list of those with non-persistent drives.

<script src="https://gist.github.com/BenNeise/7213597.js"></script>


