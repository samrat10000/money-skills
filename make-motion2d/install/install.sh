#!/usr/bin/env bash
# Installs the motion2d skill (+ companion skills) for Claude Code and Codex.
set -e
SRC="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p ~/.claude/skills ~/.codex/prompts ~/.codex/skills
for p in "$SRC/motion2d" "$SRC"/companion/*/; do
  n="$(basename "$p")"
  for root in ~/.claude/skills ~/.codex/skills; do rm -rf "$root/$n"; cp -r "$p" "$root/$n"; done
done
cp "$SRC/codex/motion2d.md" ~/.codex/prompts/motion2d.md
echo "Installed motion2d + companion skills into ~/.claude/skills and ~/.codex/skills, and ~/.codex/prompts/motion2d.md"
echo "Next: pip install -r $SRC/motion2d/requirements.txt ; ffmpeg on PATH ; read motion2d/COMPANION_SKILLS.md"
