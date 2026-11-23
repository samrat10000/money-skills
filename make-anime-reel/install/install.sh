#!/usr/bin/env bash
# Installs the anime-reel skill for Claude Code and Codex.
set -e
SRC="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p ~/.claude/skills ~/.codex/prompts ~/.codex/skills
rm -rf ~/.claude/skills/anime-reel ~/.codex/skills/anime-reel
cp -r "$SRC/anime-reel" ~/.claude/skills/anime-reel
cp -r "$SRC/anime-reel" ~/.codex/skills/anime-reel
cp "$SRC/codex/anime-reel.md" ~/.codex/prompts/anime-reel.md
echo "Installed: ~/.claude/skills/anime-reel, ~/.codex/skills/anime-reel, ~/.codex/prompts/anime-reel.md"
echo "Python deps: pip install -r $SRC/anime-reel/requirements.txt  (and ffmpeg on PATH, Blender 5.x + VRM add-on)"
