# Installs the money-skills terror-night skill for Claude Code and Codex (Windows), and fetches its asset pack.
$src = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path "$src\terror-night\engine\ep1\car\nt.glb") -and $env:SKIP_ASSETS -ne "1") {
  try { & powershell -ExecutionPolicy Bypass -File "$src\terror-night\scripts\fetch_assets.ps1" }
  catch { Write-Host "Asset fetch failed: run terror-night\scripts\fetch_assets.ps1 later (needs GitHub access)." }
}
foreach ($d in "$HOME\.claude\skills", "$HOME\.codex\prompts", "$HOME\.codex\skills") { New-Item -ItemType Directory -Force -Path $d | Out-Null }
foreach ($d in "$HOME\.claude\skills\terror-night", "$HOME\.codex\skills\terror-night") { if (Test-Path $d) { Remove-Item -Recurse -Force $d } }
# The skill text is copied; the heavy engine\ (code + 370 MB of assets) stays in this clone and is referenced.
foreach ($d in "$HOME\.claude\skills\terror-night", "$HOME\.codex\skills\terror-night") {
  robocopy "$src\terror-night" $d /E /XD "$src\terror-night\engine" /NFL /NDL /NJH /NJS | Out-Null
  Set-Content -Path "$d\ENGINE_PATH.txt" -Value "$src\terror-night\engine"
}
Copy-Item "$src\codex\terror-night.md" "$HOME\.codex\prompts\terror-night.md"
Write-Host "Installed: ~/.claude/skills/terror-night, ~/.codex/skills/terror-night, ~/.codex/prompts/terror-night.md"
Write-Host "Python deps: pip install -r $src\terror-night\requirements.txt ; ffmpeg + Blender 5.0.1 (see COMPANION_SKILLS.md)"
