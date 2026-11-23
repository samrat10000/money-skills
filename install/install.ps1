# Installs the money-skills teaser skill for Claude Code and Codex (Windows).
$src = Split-Path -Parent $PSScriptRoot
foreach ($d in "$HOME\.claude\skills", "$HOME\.codex\prompts", "$HOME\.codex\skills") { New-Item -ItemType Directory -Force -Path $d | Out-Null }
foreach ($d in "$HOME\.claude\skills\teaser", "$HOME\.codex\skills\teaser") { if (Test-Path $d) { Remove-Item -Recurse -Force $d } }
Copy-Item -Recurse "$src\teaser" "$HOME\.claude\skills\teaser"
Copy-Item -Recurse "$src\teaser" "$HOME\.codex\skills\teaser"
Copy-Item "$src\codex\teaser.md" "$HOME\.codex\prompts\teaser.md"
Write-Host "Installed: ~/.claude/skills/teaser, ~/.codex/skills/teaser, ~/.codex/prompts/teaser.md"
Write-Host "Python deps: pip install -r $src\teaser\requirements.txt  (and ffmpeg on PATH)"
