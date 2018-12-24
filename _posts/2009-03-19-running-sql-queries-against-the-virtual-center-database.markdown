---
layout: post
title: Running SQL Queries against the Virtual Center Database
date: '2009-03-19 11:37:17'
---


In a [previous post](http://ben.neise.co.uk/index.php/guides/getting-started-with-powercli/), I mentioned that without the VI Toolkit there is no real way of extracting information from the VC database.

This isnÔÇÖt *entirely* true. Before I discovered the toolkit, I was using SQL to query the Virtualcenter database directly.

### List XP Machines and their RAM allocation

<div class="wp_syntax"><table><tr><td class="code"><span style="color: #993333; font-weight: bold;">SELECT</span> VPX_VM<span style="color: #66cc66;">.</span>GUEST_OS<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>MEM_SIZE_MB <span style="color: #993333; font-weight: bold;">FROM</span> VC_DB<span style="color: #66cc66;">.</span>dbo<span style="color: #66cc66;">.</span>VPX_VM VPX_VM <span style="color: #993333; font-weight: bold;">WHERE</span><span style="color: #66cc66;">(</span>VPX_VM<span style="color: #66cc66;">.</span>GUEST_OS<span style="color: #66cc66;">=</span><span style="color: #ff0000;">'winXPProGuest'</span><span style="color: #66cc66;">)</span>

</td></tr></table></div>
### List Information about Templates

<div class="wp_syntax"><table><tr><td class="code"><span style="color: #993333; font-weight: bold;">SELECT</span> VPX_VM<span style="color: #66cc66;">.</span>LOCAL_FILE_NAME<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>GUEST_OS<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>IS_TEMPLATE<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>MEM_SIZE_MB<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>HOST_ID<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>ID <span style="color: #993333; font-weight: bold;">FROM</span> VC_DB<span style="color: #66cc66;">.</span>dbo<span style="color: #66cc66;">.</span>VPX_VM VPX_VM <span style="color: #993333; font-weight: bold;">WHERE</span><span style="color: #66cc66;">(</span>VPX_VM<span style="color: #66cc66;">.</span>IS_TEMPLATE<span style="color: #66cc66;">=</span><span style="color: #cc66cc;">1</span><span style="color: #66cc66;">)</span><span style="color: #993333; font-weight: bold;">ORDER</span><span style="color: #993333; font-weight: bold;">BY</span> VPX_VM<span style="color: #66cc66;">.</span>LOCAL_FILE_NAME

</td></tr></table></div>
### Host names and memory

<div class="wp_syntax"><table><tr><td class="code"><span style="color: #993333; font-weight: bold;">SELECT</span> VPX_HOST<span style="color: #66cc66;">.</span>ID<span style="color: #66cc66;">,</span> VPX_HOST<span style="color: #66cc66;">.</span>DNS_NAME<span style="color: #66cc66;">,</span><span style="color: #993333; font-weight: bold;">CAST</span><span style="color: #66cc66;">(</span>VPX_HOST<span style="color: #66cc66;">.</span>MEM_SIZE <span style="color: #993333; font-weight: bold;">AS</span><span style="color: #993333; font-weight: bold;">BIGINT</span><span style="color: #66cc66;">)</span><span style="color: #993333; font-weight: bold;">FROM</span> VC_DB<span style="color: #66cc66;">.</span>dbo<span style="color: #66cc66;">.</span>VPX_HOST VPX_HOST <span style="color: #993333; font-weight: bold;">ORDER</span><span style="color: #993333; font-weight: bold;">BY</span> VPX_HOST<span style="color: #66cc66;">.</span>DNS_NAME

</td></tr></table></div>
### Guest Information

<div class="wp_syntax"><table><tr><td class="code"><span style="color: #993333; font-weight: bold;">SELECT</span> VPX_VM<span style="color: #66cc66;">.</span>LOCAL_FILE_NAME<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>DNS_NAME<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>GUEST_OS<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>IS_TEMPLATE<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>IP_ADDRESS<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>MEM_SIZE_MB<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>GUEST_STATE<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>POWER_STATE<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>HOST_ID<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>ID<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>BOOT_TIME <span style="color: #993333; font-weight: bold;">FROM</span> VC_DB<span style="color: #66cc66;">.</span>dbo<span style="color: #66cc66;">.</span>VPX_VM VPX_VM <span style="color: #993333; font-weight: bold;">WHERE</span><span style="color: #66cc66;">(</span>VPX_VM<span style="color: #66cc66;">.</span>IS_TEMPLATE<>;<span style="color: #cc66cc;">1</span><span style="color: #66cc66;">)</span><span style="color: #993333; font-weight: bold;">ORDER</span><span style="color: #993333; font-weight: bold;">BY</span> VPX_VM<span style="color: #66cc66;">.</span>DNS_NAME<span style="color: #66cc66;">,</span> VPX_VM<span style="color: #66cc66;">.</span>LOCAL_FILE_NAME

</td></tr></table></div>These were based on ideas from [WayneÔÇÖs World of IT](http://waynes-world-it.blogspot.com/2008/04/vmware-clustervirtual-center-statistics.html). While itÔÇÖs a lot less friendly to work with, the advantage is that itÔÇÖs a lot quicker than the VI ToolkitÔÇÖs *Get-* commands, and I still use them from time-to-time.

Although you could use this approach to modify entries in the database, I would only ever feel comfortable using this to extract information.


