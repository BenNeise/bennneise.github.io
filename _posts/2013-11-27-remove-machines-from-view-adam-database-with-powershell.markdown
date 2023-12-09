---
layout: post
title: Remove machine objects from VMWare View's ADAM database with PowerShell
date: '2013-11-27 16:45:16'
tags: vmware-horizon-view powershell
---

<div class="info">26/02/14  -  I've updated this script to accept pipeline input and work a little more efficiently when removing multiple machines.</div>

It's one of those things that shouldn't happen, but which inevitable does. Someone removes a View managed VM from vSphere, and View refuses to realise it's gone. It also sometimes happens when machines fail to provision correctly (i.e., due to lack of available storage). The [procedure](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1008658) is easy enough to follow, but it's time-consuming and prone to error. In order to make the cleanup operation easier, I wrote up a quick function below. It relies on the free [Quest AD CMDLets](http://www.quest.com/powershell/activeroles-server.aspx "Quest AD CMDLets").

```powershell
#Requires -PSSnapin Quest.ActiveRoles.ADManagement
 
function Remove-StuckVDIMachineFromAdamDatabase {
    <#
    .Synopsis
    Removes an object from View's ADAM database
    
    .Description
    Finds a computer object in View's ADAM database which represents a machine.
    Probably one stuck in a Deleting "(Missing)" state. Deletes it (with confirmation)
 
    .Parameter Computer
    The name of the computer to search for.
 
    .Parameter ConnectionServer
    The connection server. Is set by default to "yourconnectionserver".
 
    .Example
    Removes a desktop called "Desktop01"
    
    Remove-StuckVDIMachineFromAdamDatabase -Computer "Desktop01"    

    .Example
    Removes each of an array of computernames passed as an argument

    Remove-StuckVDIMachineFromAdamDatabase $arrRogueEntries

    .Example
    Uses the pipeline to remove each of an array of stuck machines

    $arrPipeline | Remove-StuckVDIMachineFromAdamDatabase 
    
    .Notes
    Ben Neise 26/02/2014
    
    #>
    param (
        [Parameter(
            Mandatory = $true,
            Position = 0,
            ValueFromPipeline = $true,
            ValueFromPipelineByPropertyName = $true
        )]
        [Array]
        $Computer,
 
        [Parameter(
            Mandatory = $false,
            Position = 1
        )]
        [String]
        $ConnectionServer = "MyConnectionServer"
    )
    Begin {
        Try {
            Connect-QADService -Service $ConnectionServer -ErrorAction "Stop" | Out-Null
        }
        Catch {
            Write-Error "Can't connect to QADService on $ConnectionServer"
        }
        $objAdamDB = Get-QADObject -IncludeAllProperties -SizeLimit 0 -SearchRoot "OU=Servers,DC=vdi,DC=vmware,DC=int"
    }
    Process {
        foreach ($comp in $Computer){
            $objAdamDB | Where-Object {$_."pae-DisplayName" -eq $comp} | foreach-Object {
                Write-Output ("Found ADAM record: " + $_."pae-DisplayName")
                $_ | Remove-QADObject
            }
        }
    }
    End {
        Disconnect-QADService -Service $ConnectionServer
    }
}
```

You'll want to change **yourconnectionserver** to  - *well*  - your connection server. Obviously the normal caveats apply: the ones about running scripts you download from the internet in your Production environment.


