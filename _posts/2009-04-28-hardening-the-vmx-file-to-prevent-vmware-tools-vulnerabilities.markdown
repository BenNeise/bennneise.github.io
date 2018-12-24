---
layout: post
title: VMware Tools vulnerabilities
date: '2009-04-28 09:21:51'
tags:
- virtualisation
---


[Virtual Foundry's article on hardening the VMX file to prevent VMware Tools vulnerabilities](http://virtualfoundry.blogspot.com/2009/04/hardening-vmx-file.html) made me a little bit nervous, but after reading it I remembered that most of the guests on our farm are single user, non-persistent machines, and therefore even if a user is capable of causing damage, the effects are limited.

The article is still pretty interesting, although in most cases I think the vulnerabilities are academic, and only worth taking precautions against in the most demanding of environments.


