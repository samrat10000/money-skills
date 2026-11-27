#!/usr/bin/env bash
# Installs the Optimus skill for Claude Code and Codex.
set -e
SRC="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p ~/.claude/skills ~/.codex/skills
for d in ~/.claude/skills/optimus ~/.codex/skills/optimus; do rm -rf "$d"; mkdir -p "$d"; cp -r "$SRC/optimus/." "$d/"; done
echo "Installed: ~/.claude/skills/optimus, ~/.codex/skills/optimus"
