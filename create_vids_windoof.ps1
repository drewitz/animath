Get-ChildItem -Filter *.py py |
Foreach-Object {
    manim render py/$_
}

Write-Output "vid_data = " $(Get-Content data.json) ";" | Out-File docs\vid_data.js
