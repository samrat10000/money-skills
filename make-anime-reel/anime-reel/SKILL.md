---
name: anime-reel
description: Make a 15-65 s vertical 2D/toon anime story reel (IG Reels / YouTube Shorts) from an idea, a story, a poster or existing assets, to the hand-drawn-anime quality of the 5 O'CLOCK series, shot by shot with built-in self-QA, so the first version shown is already near final. Use when the user types /anime-reel or asks for a 2D / anime / toon / motion-graphics reel, episode or shot.
---

# /anime-reel: final-quality anime story reels, shot by shot

Usage: `/anime-reel <idea | episode title> [style=toon-anime|2d-flat|comic|3d-ink|<describe>] [assets=<folder>] [poster=<file>] [story=<file>] [length=<s>] [shots=<list>]`

Examples:
- `/anime-reel 5 O'CLOCK episode 2 assets=C:\Users\cross\Downloads\xc\anime-5oclock`
- `/anime-reel a girl delivers letters to a town that no longer exists length=60`
- `/anime-reel shots=05 assets=...` (build or fix only shot 05 of an existing episode)

This skill is the distilled result of building 5 O'CLOCK Episode 1. That work went from a rejected
procedural 2D reel ("not up to the mark") through crows "made of ovals" to shots the director called
"perfect" and "absolutely crazy". Every rule here exists because a real version was rejected for
breaking it. Your job is to hit the final quality on the FIRST version you show.

## Operating contract (read first, every time)

1. **Read the whole skill before you act.** Read in this order: this file, `DISCIPLINE.md`, `RULEBOOK.md`,
   `QA.md`, `STORY.md`, `PIPELINE.md`, `CHARACTERS.md`, `EDIT.md`, `SOUND.md`, `ENVIRONMENT.md`.
   Skim `MISTAKES.md` once. Open `reference/5oclock/` frames, since they are the visual bar.
   After any context compaction, re-read `RULEBOOK.md`, `QA.md` and your `REEL_STATE.md` before the next action.
2. **Gates.** Phase N+1 starts only after phase N's gate in `QA.md` passes. Evidence goes in `QA_LOG.md`:
   a contact sheet you actually opened and described, pixel numbers from `scripts/pixel_stats.py`,
   a full-size crop you looked at. "Looks fine" is not evidence.
3. **No shortcuts.** Never skip a probe render, contact sheet, crop or numeric check. Never deliver
   primitives as characters, frozen frames as animation, or a compressed preview as the main deliverable.
   Never say "done" for anything you have not verified on the real output file.
4. **You are your own harshest reviewer.** After building ANY element (a model, a pose, a prop, a
   camera move, a shot, an in-between), run its checklist in `QA.md`, then the Director's-eye pass:
   write the 5 things the director is most likely to reject and check each one at full size.
   Minimum passes per shot is 3 and maximum is 6. After 6, show the best version with an honest list of remaining flaws.
5. **One perfect shot first, then rules.** The first shot of a new project is built to the highest
   standard, approved, then written down as `SHOT_RULES.md` (exact recipe and numbers). Every later shot
   follows it. Every director note becomes a dated rule that applies to ALL upcoming shots.
6. **State on disk.** Keep `REEL_STATE.md` (phase, shot table with status, next action, paths) and
   append to `QA_LOG.md`, `DECISIONS.md` (with the director's exact words), `WORKING.md` (what was
   done, where, how to rerun) in the project folder. A new session, a smaller model or another AI must be
   able to continue from these alone.
7. **Model routing.** Story, character design, animation code, lighting and QA verdicts run on the
   strongest model available at high effort. Renders, encodes, copies and downloads can go to a
   cheap model or subagent, and the strong model checks their output.
8. **Never** change the user's system settings, type passwords, post online, push to `main`, or
   overwrite a version the director has seen. A new version gets a new file name (`NN_name_vN`).

## Inputs: pick the path in Phase 0

| You got | Path |
|---|---|
| Full assets (characters, sets, shot scripts, an episode folder) | **A**: inventory, reuse, build only what is missing. Read the project's `SHOT_RULES.md`, `DECISIONS.md`, `WORKING.md` first. |
| A story / script but no assets | **B**: lock the shot list, then build the cast (CC0 rigged models, see `CHARACTERS.md`), sets and BGs. |
| A poster or key art | **C**: the poster is the hero frame. Rebuild its world, characters and light as assets, then the reel. |
| An idea only | **D**: write the story (`STORY.md`), get it approved, then path B. |

Confirm the hero character and the reference look at the start (one batched question at most). If the director is away, choose, state your choice, and continue.

## Phases
0. **Intake.** Brief, path, style, length, platform (default 1080x1920, 24 fps), asset inventory.
   Write `REEL_STATE.md`. Gate G0.
1. **Story + script** (`STORY.md`). Logline, beat sheet, shot list with timecodes, dialogue script
   (narrator + characters), the hidden rewatch detail. Show it as a storyboard page with pictures and very little text. Gate G1 needs the director's approval.
2. **References + look** (`RULEBOOK.md` R1/R2). Art-form reference frames, 3-6 photo refs per
   character, creature and prop, and the look recipe. Gate G2.
3. **Hero shot** (`PIPELINE.md`). Build the first or hardest shot to final quality, make the probes and full render, and show it.
   On approval, write `SHOT_RULES.md` from it. Gate G3.
4. **Shots, one by one.** Build, probe, self-QA (3-6 passes), render the full shot, show it. Notify the director when each shot is done.
   If no answer comes within about 1 minute, start the next shot. Any note gets applied after the current shot, to that shot, and as a rule for every later one. Gate G4 per shot.
5. **Assembly** (`EDIT.md`). Silent cut from approved shots only, with the continuity check. Gate G5.
6. **Sound last** (`SOUND.md`). Voices and real-instrument score only after all animation is approved. Mix, loudness. Gate G6.
7. **Deliver.** Per-shot clips, the full cut, full-size PNGs, direct links, an honest critique. Update the logs.

## The things that made 5 O'CLOCK stand out (never lose them)
1. **Hand-drawn anime look, not 3D, not procedural:** thin warm ink line, flat cel colour with one
   shadow tone, a warm backlit rim, painted skies with crisp-edged sunlit clouds, soft depth of field, one accent colour.
2. **Real, artist-made rigged characters and creatures** (CC0), never primitives. Feet locked to surfaces,
   hands that really grip, anatomy checked at full size.
3. **Animation on twos with weight:** holds, then snaps; landings with flare, settle and ruffle; follow-through on
   hair, cloth, straps, leaves. The camera moves on ones (slow 2.5-3.5% pushes).
4. **Light that sells the hour:** a low sun on screen, bloom, veiling glare, dust motes in the beam, light wrap,
   rim on the sun-facing edges, p95 brightness about 0.8-0.95.
5. **Real-world detail everywhere:** road paint, kerbs, drains, roof tiles, garment cut, signage in the right
   language, depth cues on flat areas. One small wrong detail per shot for rewatchers.
6. **Sound last and sparse:** few lines, silence as acting, a piano-led real-instrument score that
   thins under each line.

## Files
| file | what |
|---|---|
| DISCIPLINE.md | how every agent must behave (Claude app, VS Code extension, Codex, small models), plus the skills/tools to install for parity |
| RULEBOOK.md | every rule with its test (R0 to R12), from the director's notes |
| QA.md | self-review loop, Director's eye, numeric targets, gates G0 to G6 |
| STORY.md | story rules, beat-sheet skeleton, dialogue script format |
| PIPELINE.md | cel layer (Blender EEVEE toon), painted BG, composite, encode, exact commands |
| CHARACTERS.md | CC0 VRoid/VRM and GLB characters, aging/scaling a cast, licences |
| EDIT.md | cuts, timings, continuity, on-screen text, assembly, deliverables |
| SOUND.md | voices, score, mix and loudness, done last |
| ENVIRONMENT.md | machines, Blender, priorities, model and token rules, delivery |
| MISTAKES.md | every mistake made and its fix |
| templates/ | REEL_STATE.md, shot_list.md, dialogue_script.md, qa_log.md |
| scripts/ | toonlib_v4.py, paint_bg.py, comp_ref.py, build_ref_shot.py, contact_sheet.py, pixel_stats.py, run_shot.ps1, cast_render.py, build_sam.py, build_cast.py, mix_ref.py |
| reference/5oclock/ | the approved shots' frames, SHOT_RULES.md, story page, decisions, research (the quality bar) |
