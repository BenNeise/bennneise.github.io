---
layout: post
comments: true
title: Platform Engineering - The Fundamentals of Developer Experience
date: '2023-11-29 15:30:00'
tags: platform-engineering
redirect_from:
  - /2023/11/29/Platform-Engineering-Fundamentals.html
---

![A developer wearing builders clothes and a hard hat, sitting at a desk in front of a computer](/assets/platform-engineer.png){: .center-image }

Teams launching new internal developer platforms often fall into the trap of creating technically-advanced solutions, using cutting edge tooling, but forgetting to think much about usability from the customer perspective. I think this is typically because these platforms been built by engineers who have inevitably been immersed in those specific technologies for so long that they've forgotten what it's like to approach it for the first time.

<!--more-->

Having a complicated, clunky product that developers don't see value in using, can result in low uptake, and - if left unfixed - may result in [shadow IT](https://en.wikipedia.org/wiki/Shadow_IT), competing platforms with similar functionality, or numerous "tactical solutions". Sadly, once a platform has been labeled by it's users as _broken_, it can be a difficult message to change.

Fortunately, there are some straightforward, fundamental things that you can help avoid this pitfall.

If you’ve been working in Platform Engineering for a while, then hopefully this may just help describe you are already doing. But, if you’re just getting started, or if you’ve built something and you’re struggling to gain traction, these tips might help you create a great platform that developers love.

# Branding & communication

In almost all companies, developers will have some degree of choice about which platform to use. As well as the public cloud staples, there might be different internal platforms, maybe some legacy thing that should have decommissioned long ago. There may be incentives to get them to use something particular, but smart engineers will always be able to find a reason to use their tool of choice. 

Like it or not, those users will frequently judge your platform based on little more than your landing page. Or worse, they may not be aware of your platform at all. This is why it's essential to have a cohesive, well publicised brand.

Human beings will attribute personality to anything (even a [pencil](https://www.youtube.com/watch?v=uAwSVOlOgH8&t=5s)). This is why companies like [Monzo focus so much on the language used to communicate with customers](https://monzo.com/tone-of-voice/).  Your users **will** attribute a personality to your platform, and it is within your power to help define this.

- Your platform should have a good name. You should use this name consistently in internal documentation and communications. 
- Your platform should also have a recognisable logo. Consider having vinyl stickers made. People love stickers, and it's a great way of getting your platform noticed. 
- It should be possible to find your platform easily, using it's name, on your corporate intranet. You should have a landing page describing your product in clear terms. The landing page should also link to the customer-facing documentation
- You should engage with your customers. Your pipeline will depend on your specific organisation, but reaching out to Product Managers, Project Managers, Architects and other engineering teams will help you
- Speaking the same language as your customer, in the same forums, helps you to understand their problems better, and encourages them to see you as a trusted partner, rather than a reluctant provider.
- Publicise your long-term roadmap, acknowledging any common functionality gaps and helping people to identify when those features should be available

# Simplify onboarding

Do people need to jump through multiple administrative hoops to use your platform? Do they need to spend ages configuring tools and environments? How easy is it for people to go from having an idea, to getting their application up-and-running?

- Don't rely on humans for (most) onboarding. Having your engineers hand-hold people is fine when you're just starting out, but will soon become a bottleneck to adoption. Focus on being hands-off for as much of the process as possible.
- Use your organisation's existing tooling for onboarding. Do you use SharePoint? ServiceNow? Can you integrate your onboarding into those existing mechanisms? That makes the process more discoverable for your users. Delegating this may also allow you to use their existing authentication, approval and attestation/auditing tooling. 
- During the automated onboarding, don’t ask questions that you don’t need the answers to. It’s easy to fall into a trap of requesting a lot of information from a customer up-front "just in case", but every question you ask increases the complexity of accessing your platform. Instead of asking for the customer's e-mail address, cost center or is this maybe something that you can get from other sources like Active Directory? 
- Similarly don't request approvals with no real benefit. Approvals shouldn't be used for visibility, and if you find yourself regularly approving requests from new customers without performing any real due-diligence, then it's likely you are just adding delay to a process that doesn't require it.
- Hide complex processes, especially those that can’t yet be automated. Perhaps your platform needs to integrate with a legacy system for which there is no practical API. You could instead raise a ticket to the appropriate team on behalf of your user. I've seen this called [Flintstoning](https://stackingthebricks.com/the-fine-art-of-flintstoning/) or [Do-nothing scripting](https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/).

# Focus on customer service

Good customer service is one of those things that’s really easy to talk about, but very difficult to put into practice. Good platform engineers are hard to find, and good platform engineers who enjoy engaging with customers are even rarer.

What does customer service even mean in terms of building a platform? 

- Be where your customers are, and engage with them on their own terms. Do they use Slack? Then you should have a channel. Do they use Jira? Or Asana? Then you should consider tracking backlog items there. (I encourage you to make your own platform backlog open to your customers, letting them help to prioritise new features). 
- Be diligent about answering questions and responding to requests quickly. Ideally respond with links to documentation! From your perspective, the customer's question is just one of the many things you need to do that day, but oftentimes, that customer is now blocked waiting on a response from you. For every customer that escalates, or chases, you should assume that there are many more who simply work around you. 
- Appreciate that the platform is often the “front door” for your customers to consume a number of services. You may not be directly responsible for backups, or monitoring, or observability; but as customers are consuming those services via your platform, then you will bear some responsibility for their service. Consider it in your best interest to help those teams to provide your customers a great service. 

# Have great customer-facing documentation

The majority of your customers are developers, and developers [love good documentation](https://hackernoon.com/nerds-dont-respond-to-marketing-try-technical-documentation-instead). 

- Structure your documentation. The [Diátaxis](https://diataxis.fr/) framework is a good start, but don’t be afraid of extending it to support your specific use-case. For example a "Getting started" guide, and an FAQ could probably exist within the framework, but it might be worth bringing them out to the forefront. 
- Have a clear tutorial on your simplest possible use-case. For example, an imperative command-line to deploy an application or virtual machine. The tutorial doesn’t need to create anything useful, you’re just trying to encourage users to make that first step
- Use that tutorial as a springboard to link to more complex tutorials. Try to have some representative tutorials: using your API, creating complex architectures
- Constantly prune your documentation. Read through it yourself, check that hyperlinks are not stale, consolidate. Maintenance of documentation is like gardening, it will never be perfect or complete, and requires constant work to prevent deterioration. 
- To support this, the platform team should be able to update the documentation with minimal friction. Sure… your solution which builds the documentation automatically from code might be really clever. But if the developers cannot make changes quickly, inertia will just make it more likely that your documentation goes stale. It might not be trendy, but Confluence and SharePoint exist for a reason.

# Conclusion

There's obviously more to building a great developer platform than the short list of tips above. But hopefully the advice will help you if you are either planning on building a new platform; or you are just getting ready to launch and wondering what you still need to do.

If you have been building platforms for a while, and have got any other tips, please feel free to add them in the comments below. 
