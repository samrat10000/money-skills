#!/usr/bin/env bash
# Installs the money-skills terror-night skill for Claude Code and Codex, and fetches its asset pack.
set -e
SRC="$(cd "$(dirname "$0")/.." && pwd)"
if [ ! -f "$SRC/terror-night/engine/ep1/car/nt.glb" ] && [ "${SKIP_ASSETS:-0}" != 1 ]; then
  bash "$SRC/terror-night/scripts/fetch_assets.sh" || echo "Asset fetch failed: run terror-night/scripts/fetch_assets.sh later (needs GitHub access)."
fi
mkdir -p ~/.claude/skills ~/.codex/prompts ~/.codex/skills
rm -rf ~/.claude/skills/terror-night ~/.codex/skills/terror-night
# The skill text is copied; the heavy engine/ (code + 370 MB of assets) stays in this clone and is referenced.
for d in ~/.claude/skills/terror-night ~/.codex/skills/terror-night; do
  mkdir -p "$d"; (cd "$SRC/terror-night" && tar cf - --exclude=./engine .) | (cd "$d" && tar xf -)
  echo "$SRC/terror-night/engine" > "$d/ENGINE_PATH.txt"
done
cp "$SRC/codex/terror-night.md" ~/.codex/prompts/terror-night.md
echo "Installed: ~/.claude/skills/terror-night, ~/.codex/skills/terror-night, ~/.codex/prompts/terror-night.md"
echo "Python deps: pip install -r $SRC/terror-night/requirements.txt ; ffmpeg + Blender 5.0.1 (see COMPANION_SKILLS.md)"
