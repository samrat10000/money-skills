# Installs the Optimus skill for Claude Code and Codex (Windows).
$src = Split-Path -Parent $PSScriptRoot
foreach ($d in "$HOME\.claude\skills\optimus", "$HOME\.codex\skills\optimus") { Remove-Item -Recurse -Force $d -ErrorAction SilentlyContinue; New-Item -ItemType Directory -Force $d | Out-Null; Copy-Item -Recurse "$src\optimus\*" $d }
"Installed: ~/.claude/skills/optimus, ~/.codex/skills/optimus"
