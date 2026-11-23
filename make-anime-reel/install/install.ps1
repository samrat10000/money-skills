# Installs the anime-reel skill for Claude Code and Codex (Windows).
$src = Split-Path -Parent $PSScriptRoot
foreach ($d in "$HOME\.claude\skills", "$HOME\.codex\prompts", "$HOME\.codex\skills") { New-Item -ItemType Directory -Force -Path $d | Out-Null }
foreach ($d in "$HOME\.claude\skills\anime-reel", "$HOME\.codex\skills\anime-reel") { if (Test-Path $d) { Remove-Item -Recurse -Force $d } }
Copy-Item -Recurse "$src\anime-reel" "$HOME\.claude\skills\anime-reel"
Copy-Item -Recurse "$src\anime-reel" "$HOME\.codex\skills\anime-reel"
Copy-Item "$src\codex\anime-reel.md" "$HOME\.codex\prompts\anime-reel.md"
Write-Host "Installed: ~/.claude/skills/anime-reel, ~/.codex/skills/anime-reel, ~/.codex/prompts/anime-reel.md"
Write-Host "Python deps: pip install -r $src\anime-reel\requirements.txt  (and ffmpeg on PATH, Blender 5.x + VRM add-on)"
