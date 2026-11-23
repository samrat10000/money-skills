# make-anime-reel: `/anime-reel`

Make 15-65 s vertical 2D / toon anime story reels and episodes (IG Reels / YouTube Shorts) from an idea, a story,
a poster or existing assets. It works shot by shot, with built-in self-QA, so the first version you see is already near final.
It is distilled from building 5 O'CLOCK Episode 1. Every rule comes from a real note the director gave.

## Use
```
/anime-reel <idea | episode> [style=toon-anime|2d-flat|comic|3d-ink|<describe>] [assets=<folder>] [poster=<file>] [story=<file>] [length=60] [shots=05]
```
- `assets=` a project folder (characters, shot scripts, SHOT_RULES.md): continues that series in its locked look.
- Only a story or an idea: it writes and storyboards the story first, gets your OK, then builds the cast, the hero shot and every other shot.

## Install
Windows (Claude Code desktop, CLI, VS Code extension, Codex):
```
git clone https://github.com/samrat10000/money-skills $HOME\money-skills
powershell -ExecutionPolicy Bypass -File $HOME\money-skills\make-anime-reel\install\install.ps1
```
macOS / Linux: `bash ~/money-skills/make-anime-reel/install/install.sh`
Then `pip install -r anime-reel/requirements.txt`. You also need ffmpeg, plus Blender 5.x with the VRM Add-on v4.10.5.

**Same results everywhere (VS Code extension, other accounts, Codex):**
- Install the plugins the desktop sessions used, listed in `anime-reel/DISCIPLINE.md` under "Parity":
  `remotion-best-practices`, `remotion-render`, `ig-reel`, `ig-caption`, `ig-human`, `ig-viral`, `glb-vehicle-builder`.
- Allow image reading, so the agent can open its contact sheets.
- Use the strongest model at high effort for story, design, animation and QA.
- Codex reads `AGENTS.md` automatically. Start it with: "Run the anime-reel skill: read anime-reel/SKILL.md and every file it lists, then follow it for: <task>."
- Any other AI: give it this folder and the same sentence.

## What's inside
| file | what |
|---|---|
| anime-reel/SKILL.md | entry: contract, input paths, phases, what made the reel stand out |
| DISCIPLINE.md | agent behaviour (desktop app, VS Code extension, Codex, small models) and the plugins to install |
| RULEBOOK.md | every rule with its test (R0-R12) |
| QA.md | self-review loop, Director's eye, numeric targets, gates G0-G6 |
| STORY.md, PIPELINE.md, CHARACTERS.md, EDIT.md, SOUND.md, ENVIRONMENT.md | story, render recipe, cast, cuts, sound, machines |
| MISTAKES.md | 20 mistakes and their fixes |
| scripts/ | the real code of the locked shot, comp, painted sky, cast tools, QA tools (contact sheets, brightness checks), shot runner |
| reference/5oclock/ | approved frames (the quality bar), SHOT_RULES, story page, decisions, research |
