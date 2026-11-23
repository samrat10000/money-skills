# COMPANION SKILLS AND TOOLS

The desktop/cloud runs had more skills and tools than a fresh VS Code extension or Codex. Install these so
every app gets the same results.

## Sibling skills in this repo (install with ../../install-all.ps1)
| skill | when |
|---|---|
| `make-teaser` (`/teaser`) | the episode's or season's teaser; its `blender/motion_lib.py` (stalker_body, eye_saccades, check_motion, vis_check) is the creature-motion library to reuse here |
| `make-motion2d` (`/motion2d`) | 2D/anime episodes; also ships the companion account skills: ig-reel, ig-viral, ig-caption, ig-human, glb-vehicle-builder, remotion-* |

Use: `ig-viral` for niche research before planning, `ig-reel` for hook options, `ig-caption` + `ig-human` for
the post caption (no title text in the video), `glb-vehicle-builder` for new vehicles/props.

## Built into Claude (turn on, don't copy)
Settings > Capabilities > Skills: skill-creator, deep-research, pdf, docx, pptx, xlsx. Public copies:
https://github.com/anthropics/skills.

## Tools (install once per machine)
| tool | why | install |
|---|---|---|
| Blender 5.0.1 (portable) | all shots | blender.org; on Windows use the portable zip; GPU = OptiX |
| Pillow inside Blender's Python | v7sets.py textures | `<blender>\5.0\python\bin\python.exe -m ensurepip` then `-m pip install pillow` (user's OK) |
| Python 3.10+ with numpy pillow | sound mixers, contact sheets | `pip install -r requirements.txt` |
| bpy (pip) | headless cloud renders | `pip install bpy==5.0.*` |
| ffmpeg | encode, mix | on PATH |
| earshot | listen to audio with numbers | source + install notes in the project's tools folder (`tools/SOUND-TOOLS.md`): `pip install -e earshot[mcp]`, `claude mcp add earshot -- python -m earshot mcp` |
| Claude in Chrome | Pinterest refs, ElevenLabs, Flow Music | Chrome Web Store; the user signs in |
| GitHub access | asset pack, delivery links | `gh auth login` or the app's GitHub connector |

## Session start check
1. You can open a PNG and describe it. 2. `blender -b --version` (or `python -c "import bpy"`). 3. `python -c
"import numpy, PIL"`. 4. `ffmpeg -version`. 5. The asset pack is unpacked (`engine/ep1/car/nt.glb` exists).
If any fails, say so before building.
