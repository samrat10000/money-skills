# make-teaser (money-skills)

A reusable, model-agnostic teaser skill. Drop the folder into any AI (Claude Code desktop or VS Code
extension, Codex, others), give it an idea, a poster or your assets, and it runs the same proven
process with built-in self-QA.

| skill | use | entry |
|---|---|---|
| `teaser/` | 15-25 s viral vertical teaser (IG Reels / Shorts) in any art style, final quality in one round | `/teaser <idea>` |

## Use
```
/teaser <idea or title> [style=3d-ink|3d-real|comic|anime|2d|pixel|sketch] [poster=<file>] [assets=<folder>] [length=20]
```
- Have assets (models, rigs, clips, an episode)? Point `assets=` at them. The skill inventories and reuses them.
- Only a poster? `poster=` it. The poster becomes the hero frame and the skill builds the assets first.
- Only an idea? Just type it. The skill designs the hero frame, builds everything, then the teaser.

## Install

### Claude Code (desktop app, CLI, VS Code extension, any account)
Windows PowerShell:
```
git clone https://github.com/samrat10000/money-skills $HOME\money-skills
powershell -ExecutionPolicy Bypass -File $HOME\money-skills\make-teaser\install\install.ps1
```
macOS / Linux:
```
git clone https://github.com/samrat10000/money-skills ~/money-skills && bash ~/money-skills/make-teaser/install/install.sh
```
This copies `teaser/` to `~/.claude/skills/teaser/` (personal skill, works in every project and in the
VS Code extension) and `/teaser` becomes available. Re-run after `git pull` to update.
Alternative per project: copy `teaser/` to `<project>/.claude/skills/teaser/`.
On claude.ai you can also save it from the skill card Claude offers, or upload the `teaser` folder as a zip
under Settings > Capabilities > Skills.

VS Code extension tip: pick the strongest model with high effort for planning and building; the skill's
`DISCIPLINE.md` forces planning, self-review and no shortcuts so the extension matches the desktop app.

### Codex (CLI or IDE)
- Put this repo in (or next to) your working folder. Codex reads `AGENTS.md` (root and `make-teaser/`) automatically.
- Optional slash prompt: `install.sh`/`install.ps1` also copy `codex/teaser.md` to `~/.codex/prompts/`,
  so `/teaser <idea>` works (on newer Codex versions custom prompts may show as `/prompts:teaser`).
  If your Codex supports skills folders, `~/.codex/skills/teaser/` gets a copy too.
- Start with high reasoning effort.

### Any other AI
Give it file access to this folder and say: "Read make-teaser/teaser/SKILL.md and every file it lists, then follow it
exactly for: <idea>."

## Requirements
ffmpeg, Python 3.10+ with `pip install -r make-teaser/teaser/requirements.txt`; Blender 5.x for 3D styles
(or `pip install bpy` for headless cloud renders).
