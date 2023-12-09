---
layout: post
title: Invoke a PowerShell script directly from Subversion
date: '2013-11-18 16:30:54'
tags: powershell

---

I've been thinking about doing something like this for a while. By adding this to PowerShell profiles, I can ensure that other people who use my scripts/functions are using the latest versions by having them run directly from a Subversion URL. This negates the requirement for them to have a local SVN repo (and for them to keep it up to date).

Our Subversion is set up for basic, rather than AD integrated, authentication, but I imagine AD integrated authentication would be easier to implement (probably using **Invoke-WebRequest** with the **UseDefaultCredentials** parameter). Rather than prompt the user at each use, I set up a service account which has only Read permissions on the repository, and hardcoded the Base64String encoded username and password into the internal version of this script.

The terrifying looking regex was based on [SqlChow](http://sqlchow.wordpress.com/2013/09/07/using-verbal-expressions-to-make-regex-easy-in-powershell/)ÔÇÿs example, with **PS1** appended to the end.

```powershell
function Invoke-SubversionScript {
    <#
    .SYNOPSIS
    Runs a script directly from Subversion.
    
    .DESCRIPTION
    Given a valid Subversion URL and credentials (Basic authentication) invokes the script on the local machine.
    
    .PARAMETER Url
    The URL of the script. Should be a valid URL, and end in PS1

    .PARAMETER Username
    The username used to access Subversion (Basic authentication).
    
    .PARAMETER Password
    The password for the account used to access Subversion (Basic authentication).
    
    .EXAMPLE
    Runs the script at the specified URL.
    
    Invoke-SubversionScript -Url "http://subversion/svn/repository/folder/SCOM2012functions.ps1" -Username "Domain\Username" -Password "Password1"
    
    .NOTES
    Ben Neise 18/11/2013
    
    #>
	param (
        [ValidateScript({$_ -Match '^(?:http)(?:s)?(?:://)(?:www\.)?(?:[^\ ]*).ps1$'})]
        [Parameter(Mandatory=$true,Position=0)]
        [String]
		$Url,

        [Parameter(Mandatory=$false,Position=1)]
        [String]
        $Username = "",
        
        [Parameter(Mandatory=$false,Position=2)]
        [String]
        $Password = ""
	)
    process {
        
        $strAuthentication = 'Basic ' + [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($Username + ":" + $Password ))
       
        $objWebClient = New-Object System.Net.WebClient
        $objWebClient.Headers.Add("Content-Type", "application/xml")
        $objWebClient.Headers.Add("Accept", "application/xml")
        $objWebClient.Headers.Add("Authorization", $strAuthentication )

        try {
            $strCommand = $objWebClient.DownloadString($Url)
        }
        catch {
            Write-Error -Message "Can't read URL"
            exit
        }
    }
    end {
        Invoke-Expression -Command $strCommand
    }
}
```


