---
layout: post
title: Formatting PowerShell tables with jQuery and DataTables
date: '2012-08-22 11:09:55'
tags: powershell
---

One of the great things about PowerShell is its ability to easily export objects to HTML, which  - with a little CSS  - makes it straightforward to create great-looking reports. But static lists of data aren't enough any more, the people _demand_ interactivity.

<!--more-->

[DataTables](http://datatables.net) is a plug-in for the [jQuery](http://jquery.com/) JavaScript library which is great for displaying interactive HTML tables, with options for sorting and filtering. You can have a look at some of the [examples](http://datatables.net/examples/) on their page to see how powerful it is.

Unfortunately for us, DataTables requires that HTML tables be formatted in a [particular](http://datatables.net/usage/) way, with the THEAD and TBODY sections declared, and this formatting is not the same as the tables output from the ConvertTo-HTML CMDlet.

For example, say we want to get a list of VMware services running on the current machine. We're going to output the HTML table to a text file, and then use a server-side-include to integrate it into a larger page (with headings, a style sheet, navigation etc.). We can generate the HTML easily with the following command.

`Get-Service -Name VMware* | Select-Object Name,Status | ConvertTo-HTML -Fragment`

By looking at the output generated, we can see that, although valid HTML, it doesn't have the THEAD and TBODY sections required by DataTables.

```html
<table>
    <colgroup>
        <col/><col/>
    </colgroup>
    <tr><th>Name</th><th>Status</th></tr>
    <tr><td>vmware-converter-agent</td><td>Running</td></tr>
    <tr><td>vmware-converter-server</td><td>Running</td></tr>
    <tr><td>vmware-converter-worker</td><td>Running</td></tr>
</table>
```

The following jScript, added to the HEAD section of the document dynamically changes all the incorrectly formatted tables on the page, and allows them to be displayed as DataTables.

```html
<script type="text/javascript">
    $(document).ready(function(){
        $('table').each(function(){
            // Grab the contents of the first TR element and save them to a variable
            var tHead = $(this).find('tr:first').html();
            // Remove the first COLGROUP element
            $(this).find('colgroup').remove();
            // Remove the first TR element
            $(this).find('tr:first').remove();
            // Add a new THEAD element before the TBODY element, with the contents of the first TR element which we saved earlier.
            $(this).find('tbody').before('<thead>' + tHead + '</thead>');
        });
        // Apply the DataTables jScript to all tables on the page
        $('table').dataTable( {
            // Put your datatable options here
        });
    });
</script>
```

It may not be the most elegant use of jScript, as I was learning as I went along, but hopefully it might save someone else some time.