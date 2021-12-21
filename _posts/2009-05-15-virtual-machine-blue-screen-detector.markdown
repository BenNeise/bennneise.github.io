---
layout: post
title: Virtual machine BSoD detector
date: '2009-05-15 14:27:26'
tags:
- powercli
- script
---


[Carter Shanklin](http://www.twitter.com/cshanklin) has used [Microsoft Office Document Imaging Library (MODI)](http://www.codeproject.com/KB/office/modi.aspx?fid=172151&df=90&mpp=25&noise=3&sort=Position&view=Quick&fr=76&select=1629759) to improve Eric Sloof's [script](http://www.ntpro.nl/blog/archives/1100-Virtual-Machine-Blue-Screen-detector.html) [ to detect Blue Screens of Death (BSoDs)](http://www.ntpro.nl/blog/archives/1100-Virtual-Machine-Blue-Screen-detector.html); it now captures the errors and converts them to text.

![BlueScreenDetector](/assets/BlueScreenDetector.jpg)

From Eric's blog:

> [F]irst it captures a screenshot of a virtual machine. Secondly it uses the Toolkit Extensions to copy it to the local drive. When the PNG image is saved on the local drive, it's converted to TIFF. The TIFF image will be used to extract the text using OCR.

It's the kind of thing that naive users expect computers to be able to do, but which actually turn out to be rather difficult. It's an incredible use of the various technologies involved  - PowerCLI, the Toolkit Extensions, MODI and PrimalForms.


