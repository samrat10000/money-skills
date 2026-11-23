# Downloads the Night Terror asset pack from the terror-night-assets branch and unpacks it into terror-night\engine.
# Usage: powershell -ExecutionPolicy Bypass -File scripts\fetch_assets.ps1
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $PSScriptRoot
if (Test-Path "$here\ENGINE_PATH.txt") { $here = Split-Path -Parent (Get-Content "$here\ENGINE_PATH.txt") }   # installed copy: unpack into the repo clone
$tmp = Join-Path $env:TEMP ("tn_assets_" + [guid]::NewGuid().ToString("N").Substring(0, 8))
git clone --depth 1 --single-branch --branch terror-night-assets https://github.com/samrat10000/money-skills $tmp
$parts = Get-ChildItem "$tmp\terror-night" -Filter "tn_assets.zip.part*" | Sort-Object Name | ForEach-Object { $_.FullName }
$zip = "$tmp\tn_assets.zip"
cmd /c ("copy /b " + ($parts -join "+") + " `"$zip`"") | Out-Null
Write-Host ("md5: " + (Get-FileHash -Algorithm MD5 $zip).Hash + "  (expected 0199BE7EDCFBC42516DCB0F521C7EF5B)")
Expand-Archive $zip -DestinationPath $here -Force
if (Test-Path "$tmp\terror-night\glb") { New-Item -ItemType Directory -Force "$here\assets_glb" | Out-Null; Copy-Item "$tmp\terror-night\glb\*" "$here\assets_glb\" }
Remove-Item -Recurse -Force $tmp
Write-Host "Assets unpacked into $here\engine (check engine\ep1\car\nt.glb and engine\cast\out\rig\)"
