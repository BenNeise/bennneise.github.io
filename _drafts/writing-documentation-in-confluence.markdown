---
layout: page
title: Writing documentation in Confluence
summary: A simple introduction to using Confluence to write documentation.
---


# Introduction

This page documents some general guidance on writing VDC documentation, and how to take advantage of various tools and techniques in Confluence.

Don't rely on exotic plugins
Make it (reasonably) easy for people to contibute good content

# Structure

## Multiple wikis?

For example

We might have a document on the Public wiki detailing what backup levels are available and how to request a restore. This is what our customers want to know.
We might have a document on the Operations wiki explaining how the Netbackup filters work, and the steps required to re-integrate a machine with VDC after it's been restored from backup. This might be required for troubleshooting by the Backup and Operations teams
And we might have a document on the Private wiki explaining how the Custom Property which defines available backup levels works, only the VDC team

## Structuring content within the wiki
The basic wiki structure is based on the description from this article.

### Tutorials

Isn't a tutorial just a how-to?

One easy way to think of the difference between a How-to guide and a Tutorial is the output. A How-to article usually has some kind of productive output (something is fixed, or something useful is created), whereas the output of a Tutorial is just "knowledge". It might be a "Hello world" type exercise.

Tutorials are likely to be used more frequently on the public wikis than the private wikis, but you should still consider creating them for new team members.


### How-to Guides

### Technical Reference

### Topics

With a couple of additions

Administration
Projects



# Style

I'd rather not be too prescriptive about writing style, but there are some things that help you if you're getting started:

* Have an introduction/abstract where you (succinctly) describe the purpose of the page. Consider making it an Excerpt so that it can be summarised in search results, or other pages.

Creating pages
These are in "descending order of importance. You don't need to do them all, all-of-the-time.

## Use built in styles for headings
Save heading 1 for the page title, and use headings 2+ for content.If you start using Heading 5 or Heading 6, your document might be too big.

## Use Table of contents
For longer pages add a Table of Contents to allow people to jump to specific sections.

Click Insert more content ()
Select Table of contents
If you've used the headings correctly, your table of contents will autogenerate. 

Sometimes you'll see a blank line at the start of your Table of Contents

This happens when the Table of Contents itself is formatted as a Header element. Select it, and format it as a Paragraph.

## Use Notes, Tip, Warnings and Info
Info is good for pulling out specific information, i.e., common errors or issues when running through a process

Notes are useful for much the same information as info, but have more visual impact

Tips are obviously tips

Warnings are warnings



Use tables
Tables allow you to present information in an easy to read format.

A 	Table
Use codeblocks
Use codeblocks to present code.

1
2
3
4
5
6
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLOWRD.
 
PROCEDURE DIVISION.
DISPLAY "SIMPLE HELLO WORLD".
STOP RUN.
For single "snippets" of code in the middle of a , avoid using the style  preformatted, as this tends to change the format of the entire paragraph. You can use the Monospace Font, but I don't think it's obvious enough, instead just use bold font.

Use labels
Tags allow for linking to related pages.

## Use images
If you find an online image that you like, save it locally then upload it. Don't paste it directly into the page as this creates a hotlink, which won't work when you're not on the VPN. Hotlinks also depend on the source page not removing the image (or replacing it with something else!).

## Flavour images
Consider adding an image to the page. I tend to align these near the top, and to the right , as that space is normally empty. This isn't just for fun, the image provides a mental cue to help you remember the page ("Oh yeah, the page with the Necronomicon on it").

## Inline images
Make sue to give them plenty of space. If you're using a numbered list, you can add line-breaks without numbers by holding Shift and pressing Return.

Also consider using a drop-shadow to differentiate the image from the background. This is especially true if the image contains a lot of white. Otherwise they just look like text:



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

Create a related items section
If pages have been labelled sensibly, then you can have a related pages section at the bottom of the page, using the Content by Label macro

Page:
SovLabs Assessment (Technology Products)
vdc
Page:
Sky DE Capacity Model (Technology Products)
vdc
Page:
VRA 8 Code Moving (Technology Products)
vdc
You can filter out labels by preceding them with "-". For example to show all pages with the vdc label, but exclude those with the spark label, set up the filter as vdc, -spark
Other tips
Some documentation is better than no documentation
Don't get too hung up on the platonic ideal of documentation. A few bullet points on a page in the wrong section is still infinitely better than a perfect page which only ever exists in your head.

Don't fight Confluence
For code blocks, I think that dark backgrounds look better. But I'm not going to remember to change all my code blocks from the default formatting. Even if I do, I'm not going to convince everyone else to change all of their code blocks to RDark. Consistency is more important here, use defaults, and native functionality wherever possible.

Sharing pages
Use the Share button on the top right of a page to generate a short-link. This short-link is more "robust", and will not be changed when the page title changes

Search boxes
The Confluence default search is terrible because it searches all of the things. Consider embedding a Page Tree Search macro at the top of your sections, which will only search pages under the current page.

Paste as plain text
Pasting from a word document is a bit of a shortcut to having something like serviceable, but it'll also tend to paste in a lot of "cruft". It's better to paste in as plain text, and add Confluence-native formatting and markup.

Paste without formatting on macOS with Option + Shift + Command + V or on Windows with Ctrl + Shift + V

Mix things up
Try to avoid a "wall of text" by using tables, images, lists, columns, callouts, etc to break things up.

Columns and sections can be a little difficult to get started with, but they make sense soon enough.

Dynamic content
If you've followed the advice about tagging, then you can start to generate dynamic content based on tags

The main VDC page on the private wiki uses the excerpts from the sub pages to describe each section
VDC Links is generated by looking for pages labelled with shared-links and vdc
VDC News is generated by looking  for blog posts labelled with vdc 
Integrating JIRA
Jira ♥ Confluence, and you can use this to do some pretty neat integrations. For example, a wiki page with all of the issues from an Epic, or a pie chart showing progress. Have a look at some examples:-

VDC Roadmap 2021
VDC Sky DE
Dates
Confluence will convert dates types in the correct format into date objects 09 Feb 2021 , I'm yet to work out what purpose this serves other than providing a visual cue that it's a date.

## Names
You can tag specific people much like you can on Twitter, e.g., Neise, Ben. People will be notified that they have been tagged in a page only if they have access to the page.

Automate where possible
The PowerShell module ConfluencePS makes it pretty easy to automate the creation of pages. Scheduled (in Jenkins for example) this allows you to create pages which periodically update themselves.

For example

VDC Blueprints Information on the public wiki uses blueprint metadata and the property dictionary to generate blueprint specific API help for VDC users. Each page corresponds to a blueprint ID
VDC Certificates on the team wiki, pulls information from CMDM and uses it to display the certificates belonging to VDC
Use HTML view
If you're having trouble with formatting, click the HTML editor (<>) in the top right hand corner to edit the page as raw HTML. Sometimes this is useful for removing ugly formatting, or extraneous line-breaks. 

## List of page hits
You can generate a list of how many times pages have been viewed. The VDC one is here. This can help work out which pages are popular to help improve regularly used information, or to remove (or better promote) unread pages.

# Blog posts

While the document above has focussed on Wiki articles, much of the information will also apply to blog posts.

When writing a blog post, it's handy to start with a Who/What/Why/Where/When structure (even if you remove the headings before publishing). Some notes specific to blog posts:-

* Blog posts should be used for transient information. For changes, you might want to create permanent wiki articles, and then link to them from a blog post "VDC now does X! Check it out here ..."
* You can set any date on an unpublished blog article, but you can't change it once it's published
