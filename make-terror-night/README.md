# make-terror-night (money-skills)

`/terror-night`: episodes, shots, creatures and sound passes for the 3D ink-realism horror web series
**Night Terror: Dead Roads** (or any new series in the same style), built shot by shot to final quality.
It is the method behind Episode 1 v7: seven versions of director notes, every mistake and its fix, the
locked look recipe, the self-check loop, the full 17-shot playbook, and the real production engine
(Blender Python) with the cast rigs, the Night Terror car, the sound library and the dialogue.

## Use
```
/terror-night <episode | shot=NNN ... | creature | idea> [assets=<folder>] [poster=<file>] [length=<s>] [style=3d-ink|3d-real|comic]
```
- `/terror-night finish episode 1`: resumes from `terror-night/PLAYBOOK_EP1.md` + your `EPISODE_STATE.md`.
- `/terror-night episode 2 "Roadkill" length=90`: a new episode in the same world (plan as pictures first).
- `/terror-night shot=125 brute block`: one shot through probe, QA, render, sound, delivery.
- `/terror-night idea="..."`: a new series: series bible, pitches, cast, one perfect shot, then the rest.

## Install (Claude desktop app, CLI, VS Code extension, any account; Codex)
Windows:
```
git clone https://github.com/samrat10000/money-skills $HOME\money-skills
powershell -ExecutionPolicy Bypass -File $HOME\money-skills\make-terror-night\install\install.ps1
```
macOS / Linux: `bash ~/money-skills/make-terror-night/install/install.sh`

The installer (1) downloads the asset pack (341 MB, from the `terror-night-assets` branch) into
`terror-night/engine/`, (2) copies the skill text to `~/.claude/skills/terror-night/` and
`~/.codex/skills/terror-night/` with `ENGINE_PATH.txt` pointing back at the engine in this clone, (3) copies
the Codex prompt to `~/.codex/prompts/terror-night.md`. `SKIP_ASSETS=1` skips the download.
Then install the companions and tools in `terror-night/COMPANION_SKILLS.md` (Blender 5.0.1, ffmpeg, Pillow in
Blender's Python, earshot, the sibling skills via `install-all`). Re-run after `git pull` to update.

**VS Code extension:** open the folder you render in (e.g. `C:\Users\cross\Downloads\xc`), start with
`/terror-night ...` (or "Read ~/.claude/skills/terror-night/SKILL.md and follow it exactly"), strongest model,
high effort, allow image reading. `DISCIPLINE.md` makes the extension behave like the desktop app.

**Codex:** keep this repo in or next to the working folder (it reads `AGENTS.md`), or use `/terror-night`
(`/prompts:terror-night` on newer versions). Highest reasoning effort.

**Any other AI:** "Read make-terror-night/terror-night/SKILL.md and every file it lists, then follow it exactly for: <task>."

## What is inside
| path | what |
|---|---|
| terror-night/SKILL.md | entry point: contract, phases, what made v7 work, file map |
| DISCIPLINE, SERIES_BIBLE, RULEBOOK (T0-T12), QA (G0-G7), PIPELINE, SOUND_VOICE, ENVIRONMENT, TOKENS, ASSETS | the rule book |
| PLAYBOOK_EP1.md | all Ep1 v7 shots: timing, code, lights, sound, director notes, status, what is left |
| MISTAKES.md | every rejection v1 -> v7 and the fix |
| engine/ | shots2.py + v7sets.py (all shots), city.py, anim.py, cast builders, penthouse, sound mixers, MakeHuman CC0 base |
| scripts/ | fetch_assets, run_cut_asus.ps1 (chunked GPU renders), preview_encode, contact_sheet, make_kit |
| templates/ | EPISODE_STATE, shot_card, dialogue_table, qa_log, SHOT_RULES |
| reference/ | approved stills + quality-bar sheet, storyboard v7, SHOT_RULES_ep1, the original logs |

## Requirements
Blender 5.0.1 (GPU box: OptiX) or `pip install bpy==5.0.*` for cloud probes; Python 3.10+ with
`pip install -r terror-night/requirements.txt`; ffmpeg; Pillow inside Blender's Python.
