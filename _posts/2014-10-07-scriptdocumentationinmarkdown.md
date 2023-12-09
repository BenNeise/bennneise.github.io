---
layout: post
title: Auto-generating PowerShell documentation in MarkDown
date: '2014-10-07 18:43:34'
tags: powershell
---


![Markdown logo](/assets/post-images/2014-10-07-scriptdocumentationinmarkdown.png){: .center-image} 

I don't mind writing documentation for my scripts, but I find that most documentation writing exercises tends to suffers from two problems:-

- **Duplicated effort**  - I tend to document my script inline, (so that `Get-Help` will work), why do I need to document the same details elsewhere?
- **Keeping it up-to-date**  - The only thing worse than *no* documentation, is clearly outdated documentation.

I had a folder full of PS1 scripts, each of which had the necessary headers. However, I needed to get this documentation into our repository of choice (a GitLab wiki).

So, in order to save me duplicating some effort, I wrote up a quick function that'll read the inline documentation from all the PowerShell scripts in a folder, and output a markdown formatted document per script, as well as an index document which links to the others. This imports nicely into a GitLab wiki. At first I thought I'd be lucky, and someone would have created an `ConvertTo-Markdown` function, but of course a PowerShell object doesn't map to a document in the same way that it maps to a table, or a CSV.

```powershell
function GenerateScriptDocumentationInMarkdown {
    <#
    .Synopsis
    Generates documentation for a folder-full of scripts using the integrated Get-Help CMDlets.
    
    .Description
    Generates a .markdown documentat for each PS1 script in a folder which has the necessary headers required by Get-Help. Also generates an index document which lists (and links to) all generated documentats. Each file name  is preceeded with "script_ps1_" so that they are listed together when viewing the Wiki documents.
    
    .Parameter SourceScriptFolder
    Source folder where the scripts are located

    .Parameter DocumentationOutputFolder
    Output folder where the documentation will be created

    .Parameter DocumentationIndexPath
    The path to a file which will be created, with relative links to the documents which  were created
    
    .Example
    GenerateScriptDocumentationInMarkdown -SourceScriptFolder "C:\Git\Lab\Project1\scripts"  -DocumentationOutputFolder "C:\Git\Lab\Project1.wiki\" -DocumentationIndexPath "C:\Git\Lab\Project1.wiki\scripts_Ps1.markdown"
    
    Generates a markdown document for each script in C:\Git\Lab\Project1\scripts in the folder C:\Git\Lab\Project1.wiki\ with an index document at C:\Git\Lab\Project1.wiki\scripts_Ps1.markdown
   
    .Notes
    Ben Neise 06/10/14
    
#>
    param (
        [Parameter(
            Mandatory = $true,
            Position = 0
        )]
        [ValidateScript({
            Test-Path $_ -PathType 'Container'
        })] 
        [string] 
        $SourceScriptFolder,

        [Parameter(
            Mandatory = $true,
            Position = 1
        )]
        [ValidateScript({
            Test-Path $_ -PathType 'Container'
        })] 
        [string] 
        $DocumentationOutputFolder,

        [Parameter(
            Mandatory = $true,
            Position = 2
        )]
        $DocumentationIndexPath
    )
    
    $arrParameterProperties = @(
        "DefaultValue",
        "ParameterValue",
        "PipelineInput",
        "Position",
        "Required"
    )

    $scriptNamePrefix = "script_ps1_"
    $scriptNameSuffix = ".markdown"

    # Initialise a counter for the progress bar
    $i = 0

    # Index header
    "# PowerShell Scripts`r`n" | Out-File -FilePath $DocumentationIndexPath

    # Get the scripts from the folder
    $scripts = Get-Childitem $SourceScriptFolder -Filter "*.ps1"
    forEach ($script in $scripts){
        $i ++
        Write-Progress -Activity "Documenting scripts" -Status ("Script $i of $($scripts.count)") -CurrentOperation ("Documenting: $($Script.BaseName)") -PercentComplete ($i / $scripts.count * 100)
        $help = Get-Help $script.FullName -ErrorAction "SilentlyContinue"
        if ($help.getType().Name -eq "String"){
            # If there's no inline help in the script then Get-Help returns a string
            Write-Error -Message "Inline help not found for script $($script.FullName)"
        } else {
            
            # Set output filename 
            $outputFile = $DocumentationOutputFolder + $scriptNamePrefix + $script.BaseName + $scriptNameSuffix

            # Add the script basename and synposis to the index 
            "## [" + $script.BaseName + "](" + $scriptNamePrefix + $script.BaseName + ")" | Out-File -FilePath $DocumentationIndexPath -Append
            
            if ($help.synopsis){
                $help.synopsis + "`r`n" | Out-File -FilePath $DocumentationIndexPath -Append
            } else {
                "No Synopsis`r`n" | Out-File -FilePath $DocumentationIndexPath -Append
            }

            # Add the script base name to the script specific document
            "# " + $script.BaseName + "`r`n" | Out-File -FilePath $outputFile

            if ($help.Synopsis){
                "## Synposis" | Out-File -FilePath $outputFile -Append
                $help.Synopsis + " `r`n" | Out-File -FilePath $outputFile -Append
            } else {
                Write-Warning -Message "Synposis not defined in file $($script.fullname)"
            }
            
            if ($help.Syntax){
                "## Syntax" | Out-File -FilePath $outputFile -Append
                "``````PowerShell`r`n" + ($help.Syntax | Out-String).trim().Replace($SourceScriptFolder,"") + "`r`n``````" | Out-File -FilePath $outputFile -Append
            } else {
                Write-Warning -Message "Syntax not defined in file $($script.fullname)"
            }
            
            if ($help.Description){
                "## Description" | Out-File -FilePath $outputFile -Append
                $help.Description.Text + "`r`n" | Out-File -FilePath $outputFile -Append
            } else {
                Write-Warning -Message "Description not defined in file $($script.fullname)"
            }

            
            if ($help.Parameters){
                "## Paramaters" | Out-File -FilePath $outputFile -Append
                forEach ($item in $help.Parameters.Parameter){
                    "### " + $item.name | Out-File -FilePath $outputFile -Append
                    "- **Type**: " + $item.Type.Name | Out-File -FilePath $outputFile -Append
                    forEach ($arrParameterProperty in $arrParameterProperties){
                        if ($item.$arrParameterProperty){
                            "- **$arrParameterProperty**: " + $item.$arrParameterProperty | Out-File -FilePath $outputFile -Append
                        }
                    }
                }
            } else {
                Write-Warning -Message "Parameters not defined in file $($script.fullname)"
            }

            if ($help.Examples){
                "## Examples `r`n" | Out-File -FilePath $outputFile -Append
                forEach ($item in $help.Examples.Example){
                    "`r`n### " + $item.title.Replace("--------------------------","").Replace("EXAMPLE","Example") | Out-File -FilePath $outputFile -Append
                    if ($item.Code){
                        "``````PowerShell`r`n" + $item.Code + "`r`n``````" | Out-File -FilePath $outputFile -Append
                    }
                    if ($item.Remarks){
                        $item.Remarks | Out-File -FilePath $outputFile -Append
                    }
                }
            } else {
                Write-Warning -Message "Examples not defined in file $($script.fullname)"
            }
        }
    }
    Write-Progress -Activity "Documenting scripts" -Completed
}

GenerateScriptDocumentationInMarkdown -SourceScriptFolder "C:\Git\Lab\evp-vm-build\scripts"  -DocumentationOutputFolder "C:\Git\Lab\evp-vm-build.wiki\" -DocumentationIndexPath "C:\Git\Lab\evp-vm-build.wiki\scripts_Ps1.markdown"
```

The documentation generated looks something like [this](https://stackedit.io/viewer#!provider=gist&gistId=9cc7c75d1937de12f6a2&filename=TestPingDocumentation.markdown).

Not sure how useful this will be to other people, as it's a pretty specific set of circumstances. I'm also not 100% satisfied with it, as the help object returned by Get-Help is a bit of a chimera of object types, which has made the code a bit ugly.


