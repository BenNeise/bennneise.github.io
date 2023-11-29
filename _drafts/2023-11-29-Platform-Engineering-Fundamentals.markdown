---
layout: post
comments: true
title: Platform Engineering - The Fundamentals of Developer Experience
date: '2023-11-29 17:30:00'
---

# Platform Engineering - The Fundamentals of Developer Experience

If you’ve been working in Platform Engineering for a while, then these should be familiar to you, but if you’re just getting started, or if you’ve built a platform and you are struggling to gain users, these tips might help you create a great platform that developers love. 

# Have great customer-facing documentation

The majority of your customers are developers, and developers [love good documentation](https://hackernoon.com/nerds-dont-respond-to-marketing-try-technical-documentation-instead). 

- Structure your documentation. The [Diátaxis](https://diataxis.fr/) framework is a good start, but don’t be afraid of extending it to support your specific use-case.
- Have a clear tutorial on your simplest possible use-case. For example, an imperative command-line to deploy an application or virtual machine. The tutorial doesn’t need to create anything useful, you’re just trying to encourage users to make that first step
- Use that tutorial as a springboard to link to more complex tutorials. Try to have some representative tutorials: using your API, creating complex architectures
- Constantly prune your documentation. Read through it yourself, check that hyperlinks are not stale.
- The platform team should be able to update the documentation with minimal friction. Sure… your solution which builds the documentation automatically from code might be really clever. But if the developers cannot make changes quickly, inertia will just make it more likely that your documentation goes stale. It might not be trendy, but Confluence and SharePoint exist for a reason.

# Simplify onboarding

Do people need to jump through hoops to use your platform? How easy is it for people to go from having an idea, to getting their application up-and-running?

- Don’t ask questions that you don’t need the answers to. It’s easy to fall into a trap of requesting a lot of information from a customer up-front
- Similarly don't request approvals with no real benefit. Approvals shouldn't be used for visibility, and if you find yourself regularly approving requests from new customers without performing any real due-dilligence, then it's likely you are just adding delays.
- Hide complex processes, especially those that can’t yet be automated. Perhaps your platform needs to integrate with a legacy system for which there is no practical API. You could instead raise a ticket to the appropriate team on behalf of your user. I've seen this called [Flintstoning](https://stackingthebricks.com/the-fine-art-of-flintstoning/).

# Customer service

This is one of those things that’s really easy to talk about, but very difficult to put into practice. Good platform engineers are hard to find, and good platform engineers who enjoy engaging with customers are even rarer.

What does customer service even mean in terms of building a platform? 

- Be where your customers are, and engage with them on their own terms. Do they use Slack? Then you should have a channel. Do they use Jira? Or Asana? Then you should consider tracking backlog items there. 
- Be diligent about answering questions and responding to requests. Ideally respond with links to documentation!
- Appreciate that the platform is often the “front door” for engaging

# Branding & communication

In almost all companies, developers will have some degree of choice about which platform to use. It’s essential to have a cohesive brand. Human beings will attribute personality to anything. This is why companies like [Monzo focus so much on the language used to communicate with customers](https://monzo.com/tone-of-voice/).  Your users will attribute a personality to your platform, and it is within your power to help define this.

Do you want to be seen as solid and reliable? Then use a reassuring tone of voice. 

Or are you a fun

- Your platform should have a good name. This might be a three-letter-acronym
- Your platform should have a recognisable logo. Stickers
- It should be possible to find your platform easily on your corporate intranet. You should have a landing page describing your product in clear terms. The landing page should also link to the customer-facing documentation
