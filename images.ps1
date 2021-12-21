$ErrorActionPreference = "Stop"

$htmlFiles = Get-Childitem -Path "_site" -Recurse -Filter "*.html"

forEach ($htmlFile in $htmlFiles){
    Write-Output $htmlFile.fullName
    $html = New-Object -Com "HTMLFile"
    # Write HTML content according to DOM Level2 
    $HTML.IHTMLDocument2_write((Get-Content -Path $htmlFile))

}