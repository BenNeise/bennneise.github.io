---
layout: post
comments: true
title: Home Documentation
date: '2023-12-1 09:00:00'
---

![Interior of house, covered in sticky labels](/assets/post-images/2023-12-01-home-documentation.png)

While reading through my RSS feeds last week, I came across a [HackerNews post](https://news.ycombinator.com/item?id=38444577) about [Home Documentation](https://luke.hsiao.dev/blog/housing-documentation/).

I've a huge fan of documenting all of the things, and I was currently revisiting both the content, and the platform on which I document, so I thought I'd add my 2¢. 

<!--more-->

# Requirements

I'm going to focus more on content, than the specific platform, but my requirements are probably fairly typical.

- The solution needs to be available (and up to date/synchronised) on Windows, macOS laptops, iOS phones and Android
- Needs to be accessible and easily updated by the whole family. Needs to be WYSIWYG, no markdown, and _certainly_ no checking things into Git! Luke's solution is clever, but he's either only using it for himself, or he lives in a house of developers!
- I'd prefer to avoid self-hosting, as it's likely that the run book itself would need to contain instructions for fixing whatever self-hosted solution I ended up using. Using a trusted cloud provider also means I can use things like MFA. 
- It shouldn't cost me anything extra
- Ideally it shouldn't require signing-up to another service

I love [Notion](https://www.notion.so/), but paying for the the whole family for something they'd barely use irks me. [Microsoft OneNote](https://www.onenote.com/?public=1) is _okay_, but the free-form format tends towards mess. So I settled on Microsoft Loop, which I get via my Microsoft 365 Family subscription, and whose iOS app has recently become generally available.


# What does the document contain?

## Financial information

Probably the most important section. I'm aware that I'm a single-point-of-failure in the household for knowing ~~exactly~~ roughly _where everything is_.

Also, it's not nice to think about, but [bad things happen](https://www.moneysavingexpert.com/news/2015/05/are-you-secretly-hurting-your-spouse-by-looking-after-the-family-finances/), and this forms a bit of a living will.

So, what kind of things are stored here?

- **Insurance details** for the home and our cars. The next time you are insuring your home or car, also make sure to note down all of the details they require: driver's license numbers, average mileage, the [job title and industry you tweaked to get the best rate](https://www.moneysavingexpert.com/insurance/car-insurance-job-picker/). Even though most comparison sites will store the details, you should also be checking rates for those companies which are not on the comparison sites.  
- **Current and savings account details**, who they are with, and what they are for.
- Our **address history**. The dates we moved in and out of each house. 
- **Utilities**. Who provides our gas, electric, internet. mobile phones and TV? What plans are we on. What's the contract end date and is there an early termination charge
- **Subscriptions**. Who are we paying for what. Yes... you know about Microsoft Game Pass, but did you know about _second_ Microsoft Game Pass (because Microsoft don't really support [gaming families](https://www.theverge.com/2023/7/14/23795351/microsoft-xbox-game-pass-friends-and-family-plan-preview-end)).


## Home maintenance

This section cotains more practical information about the house. 

- **Home insurance details** (again! These are in the financial section, which is where [Loop Components](https://support.microsoft.com/en-us/office/get-started-with-microsoft-loop-9f4d8d4f-dfc6-4518-9ef6-069408c21f0c) come in handy)
- **Replacement items**. Which particular (Ikea) glasses and plates do we use? What was size of bin bags works best in the kitchen bin?
- **Bulb types**. We have an old house, and use a suprisingly wide range of bulb types. 
- Which **paint colors** did we use for each room?


## Vehicle Details

- **Insurance details** (synchronised with the Financial section)
- **Car history**. When did we buy the cars? Previous owners
- **MOT & Service dates**


## Home Technology

Like a lot of people that work in IT. I like playing around with various solutions. And while the family certainly appreciate the benefits of having, say, a PiHole; it's not always appreciated as much when it breaks. And I'm out of the house. I'm sure a lot of us have had those phoencalls, wehere we try to describe from memory exactly which cable needs pulled. 

- [What to do when the internet breaks](https://www.youtube.com/watch?v=t2F1rFmyQmY)
- Which particular application do you need to download to program that one color changing wifi bulb we use in the fireplace, which is inexplicably a different brand to all the others. 
- What models of printer do we have, and what ink/toner do they consume? What's the name of the mobile application that lets me print from my phone, and how do I set it up? 
- Links to various web interfaces for internal services. The router admin page. The printer admin page.
- Links to various external web interfaces. Hive. Ring. 


## Misc

- Our Christmas card list and addresses
- Travel documents
- Plant care instructions, indoor & outdoor. Saves hanging onto those little plastic tags that tell you when [it likes to feed](https://www.youtube.com/watch?v=QETfA9_b7wM). 


# What shouldn't be stored

- **Passwords**. With all of that juicy personally-identifiable-data, the document is probably already a fairly big liability if it were to be compromised, but I think the advantages of having all of this in one place outweigh the risks. Besides, I was part of the [Equifax breach](https://www.equifax.co.uk/incident.html) ... all of this information is probably on the dark web anyway.
- **Scanned documents & PDF files**. Simply because I've not yet found a good way to embed them in Microsoft Loop. There's probably something I can do with linking to OneDrive, but I've not yet worked it out. I tend to keep a OneDrive folder with scanned correspondence, and PDF files for things like the instruction manual for the dishwasher. 


# Potential Improvements

I love the idea of adding videos & photos.

I'm also considering adding task boards for home improvements. It might not be quite as feature complete as Jira or Asana, but it satisfies some of those same requirements (ease of use).

Network diagrams. One of the things that Notion supports, which Loop does not yet are [Mermaid diagrams](https://mermaid.js.org/). 
