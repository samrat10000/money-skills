---
name: teaser
description: Build a 15-25 s viral vertical teaser (IG Reels / YouTube Shorts) from an idea, a poster, or existing assets (PNGs, clips, 3D models, a full episode), in any chosen art style, to final quality in one round. Use when the user types /teaser or asks for a teaser, hype clip or trailer-style reel.
---

# /teaser: one-round, final-quality teaser

Usage: `/teaser <idea or title> [style=<style>] [assets=<path or list>] [poster=<file>] [length=<seconds>]`

Examples:
- `/teaser Night Terror: Dead Roads, the Stalker poster finale style=3d-ink poster=stalker_poster.png`
- `/teaser 5 O'CLOCK episode 2 style=anime assets=C:\Users\cross\Downloads\xc\anime-5oclock`
- `/teaser a kaiju wakes under Mumbai harbour` (idea only: you build everything)

This skill is the distilled result of a teaser that took ~6 rejected rounds (v1 to final v2) before the
director called it "absolutely crazy". Every rule here exists because a real version was rejected for
breaking it. Your job is to hit the final quality on the FIRST version you show.

## Non-negotiable operating contract (read first, every time)

1. **Read the whole skill before you act.** Read in this order: this file, `DISCIPLINE.md`, `RULEBOOK.md`, `QA.md`,
   `STYLES.md`, then the pipeline file for your style (`PIPELINE_3D.md` for 3D/ink/comic-3D,
   `PIPELINE_2D.md` for 2D/anime/comic/pixel), then `SOUND.md`, `EDIT.md`, `ENVIRONMENT.md`.
   `MISTAKES.md` is the history behind the rules; skim it once. Do not start building until you have
   read them. If your context was compacted, re-read `RULEBOOK.md` and `QA.md` and your
   `TEASER_STATE.md` before continuing.
2. **Phases are gated.** You may not start phase N+1 until phase N's gate in `QA.md` is passed and
   logged in `QA_LOG.md`. A gate passes only with evidence (a contact sheet you actually looked at,
   a number from a script, a listening-tool reading), never with "looks fine".
3. **No shortcuts.** Never skip a probe render, a contact sheet, a QA script, or a listening check to
   save time. Never deliver placeholder sound, placeholder models or frozen frames as "final".
   Never say "done" for anything you have not verified by looking at it or measuring it.
4. **You are your own harshest reviewer.** After building ANY element (a model, a camera move, a
   shot, a sound cue, the edit) run its checklist in `QA.md`, then the "Director's eye" pass: list
   the 5 things the director would most likely reject and check each one. Fix, then re-check.
   Minimum review passes: 2 for every shot, 3 for the hero shot and the hero creature/character.
5. **One look, one clock.** Every shot shares one look recipe and one timeline file
   (`timeline.json`). Picture, sound and edit all read the same frame numbers.
6. **Keep state on disk.** Maintain `TEASER_STATE.md` (phase, what is done, what is next, file
   paths) and append to `QA_LOG.md`, `DECISIONS.md`, `MISTAKES.md`, `TOOLS.md` in the project's
   teaser folder. This is what lets a smaller model, a new session or another AI continue without
   losing quality.
7. **Model routing.** Creative, modelling, animation and QA-verdict work runs on the strongest model
   available (Opus / GPT-5-class, high effort). Routine work (render queues, encodes, file moves,
   downloads, frame extraction) may run on a cheap model or subagent (Sonnet / Haiku / mini), but
   their output is always QA-checked by the strong model. A small model running this skill alone
   must still run every gate; the gates are what make it reliable.
8. **Never change the user's system settings** (power, sleep, drivers, display). Ask the user.
   Never type passwords; ask the user to sign in.

## Inputs: decide the path in Phase 0

| What you got | Path |
|---|---|
| Full assets (models/rigs, sets, clips, an episode) | **Path A**: inventory, reuse, build only the missing pieces. |
| A poster only | **Path B**: the poster IS the hero frame. Rebuild its world, characters and camera as assets first, then the teaser. |
| An idea only | **Path C**: write the concept, design the hero frame (poster-grade still), build assets, then the teaser. |
| Clips only (no 3D) | **Path D**: edit-led teaser: select, re-time, grade, sound-design. New shots only if a beat is missing. |

Always confirm WHICH poster/character is the hero before building (the first plan was built around
the wrong poster and had to be redone).

## Phases

**Phase 0: Intake (5-10 min).**
- Parse the idea, style, length, platform. Default: 1080x1920, 24 fps, 17-21 s, no on-screen text.
- Inventory every asset (list file, type, what it shows, quality 1-5). For each character/creature,
  note if it already passed the director's review.
- Ask the user at most ONE batched question, only if the hero character/poster or the style is
  ambiguous. Otherwise choose and state your choice.
- Write `TEASER_STATE.md` and `brief.md` (logline, hero, style, length, hard rules that apply).

**Phase 1: Research + references (15-30 min).** See `RULEBOOK.md` section R1.
- Find 3-6 real reference images per creature/character/prop (anatomy, silhouette, skull, hands)
  and 2-3 viral teaser/trailer references for pacing and camera. Save them in `refs/` with a
  `refs/README.md` saying what each one is for.

**Phase 2: Beat sheet + shot list + animatic (the plan).**
- Use `templates/beat_sheet.md`: a cold open, 8-14 shots, each with number_name, frames, camera
  (lens, move, height), subject, the "wow" detail, the sound cue, and the continuity contract with
  the next shot (speed, direction, light).
- Build a pixel/block animatic with scratch timing (`templates/` explains how) and a storyboard page.
  Run gate G2. Show the storyboard + animatic to the user and get the go-ahead (one message).
  If the user is away, proceed on your recommended plan and say so.

**Phase 3: Assets.** Build or adapt every model, rig, set and texture. Reference-first, real
models before primitives (see R4). Gate G3 per asset: turnaround contact sheet vs references.

**Phase 4: Shots.** For each shot: build, probe render (2-5 key frames, low res), contact sheet,
QA checklist, fix, re-probe. Then the full-quality render. Gate G4 per shot. Hero shot first, since
it is the quality bar and the longest render.

**Phase 5: Sound design.** Real recordings only, placed by frame from `timeline.json`. Gate G5
(listening tool + sync check). See `SOUND.md`.

**Phase 6: Edit, grade, master.** Assemble from QA-passed frames, apply the one look, grain/VHS,
encode masters. Run `scripts/qa_check.py` on the final. Gate G6.

**Phase 7: Deliver.** Per-shot review clips (`NNN_name_vN.mp4`) + full teaser (IG file, master,
phone preview) + credits + a direct download link for every file > 20 MB (see `ENVIRONMENT.md`).
Write a short honest critique: what is great, any known flaw. Append lessons to the logs.

## The five things that made the final great (never lose these)

1. **One continuous chase.** Cars never ease to a stop between cuts; the speed and direction carry
   across every cut, so the whole teaser feels like one unbroken event.
2. **Real sound, no music bed.** Near-silence cold open with one clean metal strike, real rain,
   thunder, siren, V8 revs, three-layer drift screech, real wet-road tyre hiss, monster vocals locked
   to the jaw frames, booms on hits, -14 LUFS.
3. **The monster is revealed in pieces** (footstep ripples, POV, silhouette, crash zoom, extreme
   close-up of a living eye with saccades) and only shown whole on the hero poster frame.
4. **The creature is alive**: asymmetric, follow-through on every joint, weight shifts, tremor,
   real hands/claws, sharp bone, a jaw that hinges correctly.
5. **A found-footage stinger** after one short dark beat, held long enough to land (~2 s).

When in doubt, re-read `RULEBOOK.md`. When something is not covered, apply the spirit: real,
continuous, alive, readable, synced, never AI-looking.

## Files in this skill
| file | what |
|---|---|
| DISCIPLINE.md | agent behaviour rules (VS Code extension, Codex, small models) |
| RULEBOOK.md | every rule with its test (R0-R9) |
| QA.md | the self-review loop, Director's eye, gates G0-G6 checklists |
| STYLES.md | the style switch (3d-ink, 3d-real, comic, anime, 2d, pixel, sketch) |
| PIPELINE_3D.md / PIPELINE_2D.md | build + render recipes |
| SOUND.md / EDIT.md | real-sound design and the edit/grade/encode recipe |
| ENVIRONMENT.md | machines, model routing, token rules, delivery links |
| MISTAKES.md | the iteration history behind the rules |
| templates/ | beat_sheet.md (with the proven 14-shot skeleton), qa_log.md, TEASER_STATE.md |
| scripts/ | qa_check.py, contact_sheet.py, sound_kit.py, edit_assemble.py |
| blender/ | motion_lib.py, vis_check.py, check_motion.py |
| reference/night_terror/ | the approved teaser's real code, logs, credits and final contact sheet (the quality bar) |
