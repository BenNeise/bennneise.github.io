---
layout: page
title: Using Confluence to document your platform
summary: Tips and advice on documenting your platform using Confluence
tags: documentation confluence
image: /assets/guide-images/confluence/confluence-logo.png
---

* TOC
{:toc}

# Introduction

In this post, I'll go through some of the lessons I've learned when writing documentation, with specific reference to features and functions available in [Confluence](https://www.atlassian.com/software/confluence).

This article is mainly targetted at platform engineers who are using Confluence. Maybe they've been asked to document a new platform, maybe they've been asked to to create a new wiki, or maybe to tame and organise an existing one. 

I won't profess to being a Confluence expert, but these are things that I've found to be a good starting point for those looking to improve documentation. I've also tried to describe only what's available out-of-the-box with Confluence, rather than relying on plugins, or other bespoke additions. 


# What's to like about Confluence?

There are certainly trendier solutions for documentation than Confluence ([Backstage](https://backstage.io/) or [ReadTheDocs](https://about.readthedocs.com/)), but in a corporate setting, you will probably find that the majority of your users already have access to Confluence. You'll probably also discover that the majority of your team at least have _some_ experience of using it.

The biggest argument for Confluence is often just that it's incumbent. 

It's worth recognising that Confluence also does a lot of things "for free"...

* Simple web-based GUI means that there is a low barrier to entry. People can start reading and contributing quickly
* Integrated version control / change tracking
* Integrated authentication

Typically in larger organisations, Confluence is also managed by an existing team. This tends to be an advantage where the Platform team doesn't necessarily need to take responsibility for availability and recovery.


# Structure

Much like building a house, or planning a garden, the first thing you want to think about is the overall structure of your documentation.

If you're looking at an existing body of unorganised documentation, don't be afraid to be bold about re-organising it.


## One wiki, or multiple wikis?

Per-page permissions on Confluence are complex to maintain. Permissions are permissive, so to give someone permission on a specific page, you would have to give them permission on the whole wiki. If they shouldn't see anything else, then you'd need to restrict all other pages. This isn't really a feasible long-term strategy.

Having multiple wikis means that you can have different content targetted towards different audiences. I've found it useful to have a wiki for your platform consumers with instructions on how to use your product/platform, and a wiki for your support teams, with instructions on how to maintain and support the platform. Keeping them separate helps reinforce the different writing styles, and content that each requires. 


## Consider the structure within your wiki

I am a fan of using the [Diátaxis structure](https://diataxis.fr/), with some additions.


### How-to Guides

How to guides are the easiest type of content to create and describe, as they probably form the majority of existing content. 

* You will find a built-in template for How to guides in Confluence, by clicking the **...** to the right of the **Create** button used to create new pages. 
* The page title should start with "How to ..." this makes them easy to find, sort, and also focusses your mind on what you're helping the reader to do.
* How to pages on the "internal" wiki will focus on how to do things like code promotion, or how to resolve common errors. 
* How to pages on the "external" wiki will focus on how to use the platform, and also how to resolve common errors 


### Tutorials

Tutorials are a little more complex, and generally people get confused between these and _How To_ Guides.

From [diataxis.fr](https://diataxis.fr/tutorials-how-to/)...

> A tutorial serves the needs of the user who is at study. Its obligation is to provide a successful learning experience. A how-to guide serves the needs of the user who is at work. Its obligation is to help the user accomplish a task. These are completely different needs and obligations, and they are why the distinction between tutorials and how-to guides matters: tutorials are learning-oriented, and how-to guides are task-oriented.

* You should try to keep your tutorials short, and link them together. For example, have a guide on getting an API token which links to a tutorial about using that key to deploy a machine using Terraform. Your readers will find it easier to find the time to run through a short (<1hr) tutorial than a longer


### Topics

The Topics section is for in depth information.

If you have been using labels well, you can use this as a collection. For example, a Topics page on backups might be a link to the SLA document in the [Technical Reference](#technical-reference), as well as a link to How To documents on restoration processes. The Topics essentially acts as a framework from which to hang the other articles.  


### Technical Reference

This section of the wiki is used to store (boring!) technical, information. Lists of IP addresses, server names, architectural diagrams. These should be presented as-is, without context. That context can be provided in other pages (like [Topics](#topics)) which link to them 

Ideally this information should either be things which are not subject to frequent change, or you should find a way to have them dynamically update.

<div class="note">I regard out of date information as being worse than no information. Aside from the obvious hazard of old or misleading information, having stale data poisons the consumer of your documentation. "If that page is out of date, then how much more of this is out of date?".</div>


### Administration

I found that it's useful, particularly on the internal wiki, to have an administration section. This includes some information which doesn't fit elsewhere, and also some documentation that's frequently accessed. 

* A description of the wiki itself ("This wiki is designed to help users of the platform), and links to other wikis
* Your team's contact details, usernames, Active Directory groups and Distribution Lists
* New starter guides
* Working practices
* New starter curriculum
* Useful links to other places in the wiki, or other wikis


### Projects

Because of the neat integrations between Confluence and Jira, I've found it really useful to produce "Project Summary Reports" in Confluence. These dynamically update, and can include information on the current state of projects. I've found that Project Managers  in particular appreciate having an easy to read status report, which doesn't require them to write custom Jira filters!


### Frequently Asked Questions

When I started implementing the Diataxis style, we had a significant. With almost religious zeal, I tried to rework all of the FAQ articles into the existing diataxis sections, but it _just wasn't possible_. I think there's a valid case for an FAQ section. Engineers are often asked questions ... the same questions ... and it's incredibly useful to point the question-asker to a well formatted, complete page which answers their questions, and can point them onward to further documentation. 

# Style

I'd rather not be too prescriptive about writing style, as I feel it might discourage contributions; but there are some things that help you if you're getting started:


## Have an introduction, or abstract

Use this to (succinctly) describe the purpose of the page. Consider making it an [Excerpt](https://confluence.atlassian.com/doc/excerpt-macro-148062.html) so that it can be summarised in search results, or other pages. 

If you start this introduction with _"In this page we will ..."_, then it helps keep the page, and your mind focussed. 


## Use built-in styles for headings

I like to save **Heading 1** for the page title, and use **Heading 2** for content. If you start using **Heading 5** or **Heading 6**, your document might be too big.


## Use Table of Contents

For longer pages add a [Table of Contents](https://confluence.atlassian.com/doc/table-of-contents-macro-182682099.html) macro to allow people to jump to specific sections.

If you've used the headings correctly, your table of contents will autogenerate.

<div class="tip">Sometimes you'll see a blank line at the start of your Table of Contents. This happens when the <b>Table of Contents</b> itself is formatted as a <b>Header</b> element. Select it, and format it as a <b>Paragraph</b>.</div>

## Use the Notes, Tip, Warnings and Info formatting macros

Confluence has macros for formatting information. There are a number of formatting macros.

I liked these options so much, that I've used the same types on this blog

<div class="info"><b>Info</b> is good for pulling out specific information, i.e., common errors or issues when running through a process</div>

<div class="note"><b>Notes</b> are useful for much the same information as info, but have more visual impact</div>

<div class="tip"><b>Tips</b> can be used to give the users hints. Use liberally.</div>

<div class="warning"><b>Warnings</b> will draw attention to something that the reader should not do. Use sparingly.</div>

## Use codeblocks

Use codeblocks to present code.

```
IDENTIFICATION DIVISION.
PROGRAM-ID. IDSAMPLE.
ENVIRONMENT DIVISION.
PROCEDURE DIVISION.
    DISPLAY 'HELLO WORLD'.
    STOP RUN.
```

For single "snippets" of code in the middle of a line, avoid using the style **Preformatted**, as this tends to change the format of the entire paragraph. You can use the `Monospace Font`, but I don't think it's obvious enough, instead I just use bold.

## Use Labels

Labels allow for linking to related pages. They also unlock some more dynamic options for maintaining your content. 

For example, assuming you've been using labels for your content you could have a Topic page, with an introduction, then have a How to section with links to pages labelled
How to section
* use the filter content by label to get all pages with "kb and "cheese
Tutorials section
* use the content by label to get all tutorials
Technical reference section
* use the filter content by label to get all pages with "kb and "cheese

As people create (and remove) pages, as long as they're tagged correctly, your Topic page should be kept up-to-date. 
0
Try to be consistent with your labelling. For example, maybe stick to singular case (to avoid having, for example a label of `virtual machine` and one for `virtual machines`). Also maybe expand all acronyms (so you don't have a label for `vm` and one for `virtual-machine`).


## Use images

If you find a online image that you like (and [you're legally able to use](https://www.searchenginejournal.com/using-images-legally-online-guide/319403/)!), save it locally then upload it. Don't paste it directly into the page as this creates a hotlink. Hotlinks depend on the source page not removing the image (or replacing it with something else!).


### Flavour images

Consider adding an image to the page. I tend to align these near the top, and to the right , as that space is normally empty. This isn't just for fun, the image provides a mental cue to help you remember the page ("Oh yeah, the page with the Necronomicon on it").

### Inline images

Make sure to give your images plenty of space. If you're using a numbered list, you can add line-breaks without restarting the numbers by holding **Shift** and pressing **Return**.

<div class="tip">Consider using a drop-shadow to differentiate the image from the background. This is especially true if the image contains a lot of white. Otherwise they just look like text.</div>

Consider your audience when adding these types of images. For long [How-to documents](#how-to-guides) for technical people, overuse of images makes them difficult to follow. You can just say "Click Next" without needing an image of the screen. For tutorials though, where there's an expectation that the user is more naïve there's probably no such things as too many images - they help reassure the user that they are on the right track.


## Use comments

You can add comments to sections on the wiki by highlighting a section (when not in Edit mode), and pressing the 💬 button.

<div class="tip">Comments can be "resolved" to show that items have been fixed</div>


## Create a Related Items section

If pages have been labelled sensibly, then you can have a related pages section at the bottom of the page, using the [Content by Label](https://confluence.atlassian.com/doc/content-by-label-macro-145566.html) macro.

<div class='tip'>You can filter out labels by preceding them with "-". For example to show all pages with the <b>salt</b> label, but exclude those with the <b>vinegar</b> label, set up the filter as <code>salt, -vinegar</code></div>


# General Hints & Tips

## Don't rely on exotic plugins

Future-you will be grateful if you ever need to migrate to a new instance. Or if the plugin starts costing an unreasonable amount of money.


## Make it  easy for people to contribute good content

_Some_ good documentation is better than _no_ documentation.

Don't get too hung up on the platonic ideal of documentation. A few bullet points on a page in the wrong section is still infinitely better than a perfect page which only ever exists in your head.


## Don't fight Confluence, or your team

For [code blocks](#use-codeblocks), I personally think that dark backgrounds look better. But I'm not going to remember to change all my code blocks from the default formatting. Even if I do, I'm not going to convince everyone else to change all of _their_ code blocks to **RDark**. 

Consistency is more important here, use defaults, and native functionality wherever possible. The idea is to settle on a "house style" that doesn't require too much work.


## Share page links using the share link

Use the **Share** button on the top right of a page to generate a short-link. This short-link is more "robust", and will not be changed when the page title changes.


## Search boxes

The Confluence default search is terrible because it searches all of the things. Consider embedding a [Page Tree Search](https://confluence.atlassian.com/doc/page-tree-search-macro-163938353.html) macro at the top of your sections, which will only search pages under the current page.


## Learn how to paste as plain text

Pasting from a word document is a bit of a shortcut to having something like serviceable, but it will also tend to paste in a lot of "cruft". It's better to paste in as plain text, and add Confluence-native formatting and markup.

<div class='tip'>Paste without formatting on macOS with <b>⌥ + Shift + ⌘ + V</b> or on Windows with <b>Ctrl + Shift + V</b></div>


## Mix things up

Try to avoid a "wall of text" by using tables, images, lists, columns, call-outs, etc to break things up.

[Columns and sections](https://confluence.atlassian.com/doc/column-macro-51872396.html) can be a little difficult to get started with, but they make sense soon enough. Personally, I tend to avoid them for most content pages (I think if you're using complex layouts, it's an indication that your page is trying to do more than one thing), but the more elaborate columns-based options can make for good, visually interesting, landing pages. 


## Integrating JIRA

Jira ♥ Confluence, and you can use this to do some pretty neat integrations. For example, [a wiki page with all of the issues from an Epic](https://confluence.atlassian.com/doc/jira-issues-macro-139380.html), or a [pie chart showing the states of various Issues](https://confluence.atlassian.com/doc/jira-chart-macro-427623467.html).


## Dates

By prefixing dates with `//`, Confluence will convert dates into date objects. At the very least, this provides a visual indication that it's a date, and enforces the format (which is useful when working on international teams).


## Tag people by name, like you're on Twitter

You can tag specific people much like you can on [~~Twitter~~](https://twitter.com/) [_X_](https://twitter.com/). People will be notified that they have been tagged in a page only if they have access to the page.


## Automate content creation where possible

The [PowerShell module ConfluencePS](https://atlassianps.org/module/ConfluencePS/) makes it pretty easy to automate the creation of pages. Scheduled tasks (in Jenkins for example) this allows you to create pages which periodically update themselves.

Automating content creation goes beyond the scope of this introduction document, but it's worth keeping in mind that without either **effort** or **automation**, content will become stale. 


# Conclusion

Confluence is a safe, traditional choice for hosting documentation. But it's a safe traditional choice for a number of reasons. 

I've barely scratched the surface of Confluence functionality, but the guidance above (particularly [Labels](#use-labels) and [Headings](#use-built-in-styles-for-headings)), should provide a foundation on which you can build some more advanced functionality. 
