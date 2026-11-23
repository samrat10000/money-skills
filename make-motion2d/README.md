# make-motion2d (money-skills)

`/motion2d`: 2D anime / toon motion-graphics reels and episodes (9:16, 15-90 s), built shot by shot to
final quality from an idea, a poster or your assets. It's the method behind 5 O'CLOCK Ep1 v3: every
director note, every mistake and its fix, the exact look recipe, the self-check loop, and the full plan of
all 18 shots (cuts, camera, voices, joins).

## Use
```
/motion2d <idea | episode | shot=NN ...> [style=toon-anime|3d-ink|comic|vector-2d|pixel|sketch-ink] [assets=<folder>] [poster=<file>] [length=<s>]
```
- With assets (characters, sets, a previous episode): point `assets=` at the project folder. It reuses the cast and the locked look.
- Only a poster: `poster=`. The poster becomes the hero frame, and it builds the cast and world first.
- Only an idea: it writes the story (as pictures), builds the cast, makes one perfect shot, then the rest.

## Install (Claude desktop app, CLI, VS Code extension, any account; Codex)
Windows:
```
git clone https://github.com/samrat10000/money-skills $HOME\money-skills
powershell -ExecutionPolicy Bypass -File $HOME\money-skills\make-motion2d\install\install.ps1
```
macOS / Linux: `bash ~/money-skills/make-motion2d/install/install.sh`

It copies `motion2d/` to `~/.claude/skills/motion2d/` and `~/.codex/skills/motion2d/`, the Codex prompt
to `~/.codex/prompts/motion2d.md`, and the companion skills (`companion/`: ig-reel, ig-viral, ig-caption,
ig-human, glb-vehicle-builder, remotion-*) to both skill folders. Then read `motion2d/COMPANION_SKILLS.md`
for the built-in skills and tools to turn on (Blender + VRM add-on, ffmpeg, earshot, the Chrome extension).
Re-run after `git pull` to update.

**VS Code extension:** open the project folder (e.g. `C:\Users\cross\Downloads\xc\anime-5oclock`) as the
workspace, pick the strongest model with high effort, and start with `/motion2d ...`. `motion2d/DISCIPLINE.md`
lists the extra rules that make the extension and Codex match the desktop app.

**Codex:** keep this folder in or next to the working folder (Codex reads `AGENTS.md`), use high reasoning,
and start with `/motion2d ...` or "Read make-motion2d/motion2d/SKILL.md and follow it for: <task>".

## Requirements
Blender 5.0.1 + VRM add-on 4.10.5 (or `pip install bpy` for cloud tests), Python 3.10+ with
`pip install -r motion2d/requirements.txt`, ffmpeg. A GPU box for full renders (an RTX 3050 does a
96-frame shot in about 9 minutes).
