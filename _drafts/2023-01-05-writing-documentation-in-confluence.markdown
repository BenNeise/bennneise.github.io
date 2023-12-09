---
layout: post
comments: true
title: Confluence documentation for developers
date: '2022-01-05 09:15:00'
tags: documentation confluence
---

In this post, I'll go through some of the things I've found useful when writing documentation, with specific reference to Confluence.

I'm not a Confluence expert, but these are things that I've found to be a ggood starting point for those looking to improve documentation. 

This article is mainly targetted at developers who have been asked to write some documents in Confluence. Or they've maybe been asked to to create a new wiki, or maybe to tame and organise an existing one. 


# Structure

The first thing we need to think about is the structure of your wiki.

## Multiple wikis?

Per page permissions on Confluence are a bit complex to maintain. Permissions are permissive, so to give someone permission on a specific page, you would have to give them permission on the whole wiki. If they shouldn't see anything else, then you'd need to restrict all other pages. This isn't really a feasible long-term strategy.

## Structure within the wiki

I am a fan of using the [Diátaxis structure](https://diataxis.fr/), with some additions.


### How-to Guides

How to guides are the easy.

* The page title should start with "How to"


### Tutorials

Tutorials are a little more complex, and generally people get confused between these and How To Guides.

Tips

* You should try to link keep your tutorials short, and link them together. 


### Technical Reference

Technical information. Lists of IP addresses, or server names. 

Ideally this information should either be things which are not subject to frequent change, or you should find a way to have them dynamically update.

<div class="note">I regard out of date information as being worse than no information. Aside from the obvious hazard of old or misleading information, having stale data poisons the consumer of your documentation. "If that page is out of date, then how much more of this is out of date?".</div>


### Topics

In depth information


### Administration

I found that it's useful to have an admin section. 


### Projects

Because of the neat integrations between Confluence and Jira, I've found it really useful to produce "Project Summary Reports" in Confluence. These dynamically update, and can include information on  

# Style

I'd rather not be too prescriptive about writing style, but there are some things that help you if you're getting started:


## Have an introduction/abstract

Use this to (succinctly) describe the purpose of the page. Consider making it an Excerpt so that it can be summarised in search results, or other pages.


## Use built in styles for headings

Save heading 1 for the page title, and use headings 2+ for content.If you start using Heading 5 or Heading 6, your document might be too big.


## Use Table of contents

For longer pages add a Table of Contents to allow people to jump to specific sections.

If you've used the headings correctly, your table of contents will autogenerate.

<div class="info">Sometimes you'll see a blank line at the start of your Table of Contents. This happens when the <b>Table of Contents</b> itself is formatted as a <b>Header</b> element. Select it, and format it as a <b>Paragraph</b>.</div>

## Use Notes, Tip, Warnings and Info

<div class="info">Info is good for pulling out specific information, i.e., common errors or issues when running through a process</div>

<div class="note">Notes are useful for much the same information as info, but have more visual impact</div>

<div class="tip">Tips are obviously tips</div>

<div class="warning">Warnings are warnings</div>

## Use tables

Tables allow you to present information in an easy to read format.


## Use codeblocks

Use codeblocks to present code.

For single "snippets" of code in the middle of a , avoid using the style  preformatted, as this tends to change the format of the entire paragraph. You can use the Monospace Font, but I don't think it's obvious enough, instead just use bold font.

## Use labels

Tags allow for linking to related pages.


## Use images

If you find an online image that you like, save it locally then upload it. Don't paste it directly into the page as this creates a hotlink, which won't work when you're not on the VPN. Hotlinks also depend on the source page not removing the image (or replacing it with something else!).


### Flavour images

Consider adding an image to the page. I tend to align these near the top, and to the right , as that space is normally empty. This isn't just for fun, the image provides a mental cue to help you remember the page ("Oh yeah, the page with the Necronomicon on it").

### Inline images

Make sure to give them plenty of space. If you're using a numbered list, you can add line-breaks without numbers by holding Shift and pressing Return.

Also consider using a drop-shadow to differentiate the image from the background. This is especially true if the image contains a lot of white. Otherwise they just look like text.

Consider your audience when adding these types of images. For long How-to documents for technical people, overuse of images makes them difficult to follow. You can just say "Click Next" without needing an image of the screen. For tutorials though, there's probably no such things as too many images! 


## Use extracts

Extracts allow you to summarise a page, and use that summary in another page.


## Use templates

Still looking at this myself!

This is cool though

Create from template


## Use comments

You can add comments to sections on the wiki by highlighting a section (when not in Edit mode), and pressing the button.

Comments can be "resolved" to show that items have been fixed


## Create a Related Items section

If pages have been labelled sensibly, then you can have a related pages section at the bottom of the page, using the **Content by Label** macro

You can filter out labels by preceding them with "-". For example to show all pages with the **salt** label, but exclude those with the **vinegar** label, set up the filter as `salt, -vinegar`


# Tips

## Don't rely on exotic plugins

Future you will be grateful if you ever need to migrate to a new instance. Or if the plugin starts costing an unreasonable amount of money. 


## Make it  easy for people to contibute good content

Some documentation is better than no documentation

Don't get too hung up on the platonic ideal of documentation. A few bullet points on a page in the wrong section is still infinitely better than a perfect page which only ever exists in your head.


## Don't fight Confluence

For code blocks, I think that dark backgrounds look better. But I'm not going to remember to change all my code blocks from the default formatting. Even if I do, I'm not going to convince everyone else to change all of their code blocks to RDark. Consistency is more important here, use defaults, and native functionality wherever possible.


## Sharing pages

Use the **Share** button on the top right of a page to generate a short-link. This short-link is more "robust", and will not be changed when the page title changes.


## Search boxes

The Confluence default search is terrible because it searches all of the things. Consider embedding a Page Tree Search macro at the top of your sections, which will only search pages under the current page.


## Paste as plain text

Pasting from a word document is a bit of a shortcut to having something like serviceable, but it'll also tend to paste in a lot of "cruft". It's better to paste in as plain text, and add Confluence-native formatting and markup.

Paste without formatting on macOS with Option + Shift + Command + V or on Windows with Ctrl + Shift + V


## Mix things up

Try to avoid a "wall of text" by using tables, images, lists, columns, callouts, etc to break things up.

Columns and sections can be a little difficult to get started with, but they make sense soon enough.


## Dynamic content
If you've followed the advice about tagging, then you can start to generate dynamic content based on tags

The main VDC page on the private wiki uses the excerpts from the sub pages to describe each section
VDC Links is generated by looking for pages labelled with shared-links and vdc
VDC News is generated by looking  for blog posts labelled with vdc 


## Integrating JIRA

Jira ♥ Confluence, and you can use this to do some pretty neat integrations. For example, a wiki page with all of the issues from an Epic, or a pie chart showing progress.


## Dates

Confluence will convert dates types in the correct format into date objects 09 Feb 2021 , I'm yet to work out what purpose this serves other than providing a visual cue that it's a date.


## Names

You can tag specific people much like you can on Twitter. People will be notified that they have been tagged in a page only if they have access to the page.


## Automate where possible

The [PowerShell module ConfluencePS](https://atlassianps.org/module/ConfluencePS/) makes it pretty easy to automate the creation of pages. Scheduled (in Jenkins for example) this allows you to create pages which periodically update themselves.


## Use HTML view

If you're having trouble with formatting, click the HTML editor (<>) in the top right hand corner to edit the page as raw HTML. Sometimes this is useful for removing ugly formatting, or extraneous line-breaks. 


## List of page hits

You can generate a list of how many times pages have been viewed. This can help work out which pages are popular to help improve regularly used information, or to remove (or better promote) unread pages.


# Blog posts

While the document above has focussed on Wiki articles, much of the information will also apply to confluence-hosted blog posts.

When writing a blog post, it's handy to start with a Who/What/Why/Where/When structure (even if you remove the headings before publishing). Some notes specific to blog posts:-

* Blog posts should be used for transient information. For changes, you might want to create permanent wiki articles, and then link to them from a blog post "Our product now does X! Check it out here ..."
* You can set any date on an unpublished blog article, but you can't change it once it's published
