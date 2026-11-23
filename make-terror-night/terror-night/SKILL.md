---
name: terror-night
description: Make an episode (or a single shot, set, creature or sound pass) of the 3D ink-realism horror web series "Night Terror: Dead Roads", or of any new series in the same style, shot by shot to final quality, using the bundled Blender engine, the cast and car assets and the full rule book. Use when the user types /terror-night or asks for a Night Terror episode, shot, monster, scene or the series look.
---

# /terror-night: a horror episode that passes the director on the first look

Usage: `/terror-night <episode, shot or idea> [shot=<NNN>] [assets=<folder>] [poster=<file>] [length=<s>] [style=3d-ink|3d-real|comic]`

Examples:
- `/terror-night finish episode 1` (reads `PLAYBOOK_EP1.md` + the project's `EPISODE_STATE.md`, renders what is left)
- `/terror-night episode 2 "Roadkill" length=90` (new episode in the same world)
- `/terror-night shot=125 brute block` (one shot: plan, build, probe, render, sound, deliver)
- `/terror-night a new creature: a drowned subway conductor` (asset only, through gate G3)
- `/terror-night idea="a lighthouse keeper hears the fog breathe" style=3d-ink` (new series, same method)

This skill is the distilled method behind Night Terror Episode 1, which went through SEVEN rejected versions
(v1 to v6 rejected, v7 rebuilt shot by shot) before the director said "damn cool, I want this realism in all
the other clips" (040 stairwell), "it looks awesome now" (003/004), "this is good, move ahead" (005 v2) and
"coolll" (Brute v2). Every rule here exists because a real version was rejected for breaking it. Each
rejection cost a full day of renders and tokens. Your job: reach the v7 level on the FIRST version you show,
then go beyond it.

## Non-negotiable operating contract (read first, every time)

1. **Read the whole skill before you act**, in this order: this file, `DISCIPLINE.md`, `SERIES_BIBLE.md`,
   `RULEBOOK.md`, `QA.md`, `PIPELINE.md`, `SOUND_VOICE.md`, `ENVIRONMENT.md`, `TOKENS.md`. Then
   `LOOK.md` (the style as numbers + the one-still LOOK TEST), `CAST_AND_CAMERA.md` (every character + movement + camera mode -> code), `PLAYBOOK_EP1.md` (the full worked episode, shot by shot, with code names) and `MISTAKES.md` (the
   rejection history). `ASSETS.md` before touching any model. After a context compaction re-read
   `RULEBOOK.md`, `QA.md` and the project's `EPISODE_STATE.md` before the next action.
2. **Plan as pictures first.** No shot is built before the episode plan exists as a storyboard page with
   per-shot timing, camera, sound, dialogue and the "wow" detail (`templates/shot_card.md`). The director
   approves the plan ONCE. If the director is away, proceed on your recommended plan and say so.
3. **One perfect shot first, then the recipe is law.** The first shot of a new look is iterated until the
   director locks it (Ep1: 040_stairwell). Its numbers (exposure, lights, lens, MB, DOF, grain) become
   `SHOT_RULES.md` in the project, and every later shot must match or beat it.
4. **Every note becomes a rule for every shot.** When the director comments on one shot, write the note
   verbatim + the general rule + its test in `SHOT_RULES.md` AND `MISTAKES.md`, and apply it to all
   later shots, not only the one commented on. Before reusing ANY old shot, re-read every past note on it.
5. **Shot-by-shot delivery.** Each shot goes to the director as its own clip `NNN_name_vN.mp4` + key
   stills + an honest critique (what is great, what is still weak) the moment it is done. Never send the
   whole episode as the first look. Never overwrite a version the director has seen. Keep building the
   next shot while they watch; fold their notes in after finishing the current shot.
6. **You are your own harshest reviewer.** After building anything, LOOK at it (one contact sheet per probe,
   full-size crops of faces, hands, mouths, eyes, tyres) and run the Director's eye list in `QA.md`.
   Fix the root cause, re-probe. Minimum review passes: 2 per shot, 3 for the hero shot and every new
   creature/character. Then and only then send it.
7. **Real only.** Real recorded sound (CC0/CC-BY, credited), real artist-grade models or proper builds
   (never primitive-blob creatures), real camera behaviour, real practical light. Nothing may read as AI.
8. **Keep state on disk** in the project's `logs/` folder: `EPISODE_STATE.md` (shot table with status),
   `SHOT_RULES.md`, `WORKING.md`, `DECISIONS.md` (director's words verbatim + decision + why),
   `MISTAKES.md` (rejected + fix), `TOOLS.md`, `QA_LOG.md`. Append only. Any model must be able to resume
   from these alone.
9. **Never** enter passwords, buy, accept terms, post online or change system settings; ask the user.
   Never install software on the user's machine without their own explicit OK in words.
   Never claim "done", "fixed", "synced" or "sounds good" without a file, a number or a listening reading.

**Where the engine is:** `engine/` next to this file in the repo clone (`~/money-skills/make-terror-night/terror-night/engine`).
An installed copy in `~/.claude/skills/terror-night/` has `ENGINE_PATH.txt` with the real path. Work and render
there (or copy it into the project). If `engine/ep1/car/nt.glb` is missing, run `scripts/fetch_assets.sh` / `.ps1`.

## Inputs: decide the path in Phase 0

| What you got | Path |
|---|---|
| This skill's asset pack (cast rigs, car, sets, sound, VO) | **A**: inventory (`ASSETS.md`), reuse, build only what is missing. Default for Night Terror. |
| A previous episode's `EPISODE_STATE.md` / logs | **A+**: resume: the bar is that episode's best approved shot; never redo approved work. |
| A poster only | **B**: the poster is the hero frame; build its world, cast and camera first (G3), then the episode. |
| An idea only (new series) | **C**: series bible first (`SERIES_BIBLE.md` is the template), 3 pitches as picture strips, then cast, then the first perfect shot. |

## Phases (gates are in QA.md; never skip one)

- **P0 Intake.** Defaults: 1080x1920, 24 fps, H.264 yuv420p, 60-100 s per episode, no on-screen titles.
  Inventory assets (file, what it shows, approved or not, past notes). Write `EPISODE_STATE.md` + `brief.md`.
  Ask at most ONE batched question, only if the hero, the length or the style is ambiguous.
- **P1 Story.** One night, one goal (get out / get to someone), one escalating threat, every scene caused by
  the one before (no missing steps: if he ends in a car, we see the keys, the exit, the garage, him getting
  in). A found-footage reason for the camera (Ep1: the camcorder that never stops recording). Cliffhanger
  that was planted earlier (the phone on the seat). Research real-world specifics of the location.
- **P2 Plan.** Storyboard page (HTML artifact or `storyboard.html`) with acts, per-shot `NNN_name`, time
  range, camera (lens, height, move), practical lights, what moves, wow detail, dialogue lines (one at a
  time), sound cues, and the cut into the next shot. The dialogue table (`templates/dialogue_table.md`).
  Gate G2. One go-ahead.
- **P3 Assets.** Cast, car, sets, props, textures; reference-first; turnaround sheet vs refs (G3).
- **P3.5 LOOK TEST** (`LOOK.md` section 7): one still, ~10 s, must pass before any shot on a new machine or model.
- **P4 First perfect shot.** Probe (3-6 key frames at RES .35-.5, SAMP >= 20, one contact sheet) -> QA ->
  fix -> full render on the GPU box -> sound -> clip -> send. Lock it, write `SHOT_RULES.md`.
- **P5 Remaining shots** in story order, each through G4 + G5 and delivered on its own.
- **P6 Voice + score** on the locked picture: dialogue first (ElevenLabs or the user's tool), then the
  score written AROUND the lines (no score before the planned drop). Gate G5.
- **P7 Edit + master**: cut only from approved shots, one grade, light grain, -14 LUFS, encode IG/master/
  phone versions, direct download links (G6).
- **P8 Learn.** Append every lesson to `SHOT_RULES.md`/`MISTAKES.md` and propose updates to this skill.

## What made v7 work (never lose these)

1. **Practical light only.** Dark frames lit by things that exist in the scene: the camcorder lamp, strobing
   emergency lamps, fluorescent tubes clunking on one by one, fire glow through windows, headlights, a phone
   screen. No ambient blue wash, no invisible floodlights, no light balls in frame.
2. **A camera that is a real object in the story.** Tripod -> handheld camcorder -> propped on the dash ->
   still recording after he is gone. Step-synced handheld walking, late reframes, kicks on impacts.
3. **Dense real-world detail** (pre-war New York: hex tile, marble treads worn in the middle, iron balusters,
   oak rail, brass elevator, flyers, claw marks, hand smears, door numbers, B1 PARKING sign).
4. **Real sound, one line at a time.** Rain, sirens, footsteps on the right surface on the right frame,
   breathing, the strobe ticking; dialogue never overlaps; the score only starts on the ignition.
5. **Creatures that are alive and anatomically scary** (bull-skull Stalker with ember-vein eyes and saccades,
   Brute v2 with a wedge skull and torn cheeks), never round, never mirrored, never stick-limbed.
6. **Continuity of objects and causes**: the phone tossed on the seat in 070 is the phone ringing in 160.

## Files

| file | what |
|---|---|
| DISCIPLINE.md | agent behaviour for Claude desktop, VS Code extension, Codex and small models |
| SERIES_BIBLE.md | the world, cast, car, creatures, locations, look and story devices of Night Terror |
| RULEBOOK.md | every rule with its test and the rejection that created it (T0-T12) |
| QA.md | the self-review loop, Director's eye list (Sam's real triggers), gates G0-G7 |
| PIPELINE.md | the engine: how a shot is coded, env vars, render recipes (cloud CPU / Asus GPU), encode |
| SOUND_VOICE.md | real SFX, call drops, dialogue, score rules, mix numbers |
| ENVIRONMENT.md | machines, Asus render kit, Remote Control, delivery links, model routing |
| TOKENS.md | how to get the result in one round and spend 10x fewer tokens |
| ASSETS.md | asset manifest, download links, how to rebuild or add a character |
| LOOK.md | the style as numbers: ink hull recipe + thickness table, painted materials, practical lights, AgX lens, the one grade + VHS, and the LOOK TEST every new machine/model must pass first |
| CAST_AND_CAMERA.md | every character (builder, rig, movement call) and every camera mode (tripod, POV, dashcam, handheld doc, crash zoom, tyre cam) with code and numbers |
| PLAYBOOK_EP1.md | Episode 1 v7, all shots: timing, code, lights, sound, director notes, status |
| MISTAKES.md | every rejection v1 -> v7 and the fix |
| COMPANION_SKILLS.md | the sibling skills (make-teaser, make-motion2d) and tools to install |
| templates/ | EPISODE_STATE.md, shot_card.md, dialogue_table.md, qa_log.md, SHOT_RULES_template.md |
| scripts/ | look_test.py, grade.py, contact_sheet.py, preview_encode.sh, run_cut_asus.ps1, fetch_assets.sh/.ps1, make_kit.sh |
| engine/ | (in the repo clone; an installed copy names it in `ENGINE_PATH.txt`) the real production code: ep1/ (shots2.py, v7sets.py, city.py, anim.py, snd7/ mixers), cast/ (character builders), pent7/ (penthouse), mh/ (MakeHuman CC0 base) |
| reference/ | approved stills (the quality bar), the v7 storyboard, the original logs |
