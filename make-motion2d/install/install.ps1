# Installs the motion2d skill (+ companion skills) for Claude Code and Codex (Windows).
$src = Split-Path -Parent $PSScriptRoot
foreach ($d in "$HOME\.claude\skills", "$HOME\.codex\prompts", "$HOME\.codex\skills") { New-Item -ItemType Directory -Force -Path $d | Out-Null }
$skills = @(@{n = "motion2d"; p = "$src\motion2d" }) + (Get-ChildItem "$src\companion" -Directory | ForEach-Object { @{n = $_.Name; p = $_.FullName } })
foreach ($s in $skills) {
  foreach ($root in "$HOME\.claude\skills", "$HOME\.codex\skills") {
    $dst = Join-Path $root $s.n
    if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
    Copy-Item -Recurse $s.p $dst
  }
}
Copy-Item "$src\codex\motion2d.md" "$HOME\.codex\prompts\motion2d.md"
Write-Host "Installed motion2d + $($skills.Count - 1) companion skills into ~/.claude/skills and ~/.codex/skills, and ~/.codex/prompts/motion2d.md"
Write-Host "Next: pip install -r $src\motion2d\requirements.txt ; ffmpeg on PATH ; read motion2d\COMPANION_SKILLS.md"
