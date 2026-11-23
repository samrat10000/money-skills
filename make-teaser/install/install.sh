#!/usr/bin/env bash
# Installs the money-skills teaser skill for Claude Code and Codex.
set -e
SRC="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p ~/.claude/skills ~/.codex/prompts ~/.codex/skills
rm -rf ~/.claude/skills/teaser ~/.codex/skills/teaser
cp -r "$SRC/teaser" ~/.claude/skills/teaser
cp -r "$SRC/teaser" ~/.codex/skills/teaser
cp "$SRC/codex/teaser.md" ~/.codex/prompts/teaser.md
echo "Installed: ~/.claude/skills/teaser, ~/.codex/skills/teaser, ~/.codex/prompts/teaser.md"
echo "Python deps: pip install -r $SRC/teaser/requirements.txt  (and ffmpeg on PATH)"
