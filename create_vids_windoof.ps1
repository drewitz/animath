Get-ChildItem -Filter *.py py |
Foreach-Object {
    manim render py/$_
}