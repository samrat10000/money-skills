---
name: optimus
description: Run any creative production (Night Terror, 5 O'CLOCK, teasers, 2D reels, any new series) at the same extreme quality for far fewer tokens - automatic QA before looking at images, assets built once, plan-once/render-overnight/review-once passes, small model helpers for chores, the standard project folder layout. Use with every production skill, and when the user types /optimus or asks to save tokens or organize the project.
---

# /optimus: extreme results, minimum tokens

Optimus is the operating layer under every production skill (terror-night, teaser, motion2d, anything new). Those skills
say WHAT good looks like; Optimus says how to get there spending the fewest tokens. Quality is never traded for tokens:
when a rule here would lower quality, the production skill wins.

Where tokens really go (measured on Night Terror Ep1, 2026-11-25/26): reading images, reading big code/log files,
re-deriving context in new sessions, rework after a shot fails late, and chatty status turns. Waiting on renders costs
almost nothing when it is event-driven. Every rule below attacks one of those.

## The 10 rules

1. **Numbers before pictures.** After every render run `scripts/qa_auto.py` (frames present, black/frozen runs, motion
   stutter, exposure, loudness, true peak). Open an image only when a check flags OR for the one designed look per shot
   (one phone-size contact sheet + crops of the critical region: face, hands, jaw, tyres). Never open full frames to
   "see how it's going".
   Crop by CODE, not by guessing: locate the subject (a colour/brightness mask, a projected bone position) and crop
   around its centre; three guessed crops of the Stalker's head missed, one located crop nailed it.
2. **Debug with probes that print, not renders.** Positions, collisions, gaps, ray hits, jaw direction, light energy:
   print them from the scene (dry runs) instead of rendering to look. A printed number costs a line; a test frame costs
   an image + minutes.
3. **Build every recurring asset ONCE** (characters, sets, props, vehicle, phone, UI overlays, sound kits) as a saved,
   versioned file in `<project>/shared/assets/`, registered in the project's production bible. Shots load them; nobody
   rebuilds an approximation per shot (that caused most rework in Ep1).
4. **One plan per pass.** Turn the director's notes into a numbered issue list once (`R1..Rn`, saved in the episode's
   `logs/`), map each to a shot and a fix, estimate, then execute. Every later message refers to the IDs.
5. **Render in one overnight queue, review in one sitting.** Chunked (25 frames per fresh process), detached, resumable,
   expected-frame guard, a finisher that re-runs until every cut has its output. Batch all probes of a shot into ONE
   session and ONE contact sheet. Max 2 probe rounds per shot; before a 3rd, write the root cause in one sentence.
6. **Event-driven waiting.** A watcher script exits only on: a finished cut, a failure, a stall. Hourly safety checks
   answer in one line when work is progressing. No sleep-polling, no "still rendering" messages.
7. **Small-model helpers for chores.** Uploads, encodes, file moves, downloads, frame extraction, packaging: give a
   small/fast model the exact commands + expected output, verify the result yourself. The strong model keeps: plans,
   creative decisions, shot/creature design, QA verdicts, root-cause diagnosis.
8. **Read narrow.** `grep -n` for the function, `sed -n a,bp` the lines, `tail -c` logs. Never cat a whole engine file or
   render log. Keep state files short and current so a new session reads 3 files, not the history.
9. **State on disk, always.** Each episode keeps `logs/EPISODE_STATE.md` (shot table + next action), `logs/QA_LOG.md`
   (one line per check), the review files, and the project's production bible. A new session or account resumes from
   those alone. Lessons go into the production skill the same session.
10. **Short replies.** Results, numbers, blockers, decisions. Tables for multi-shot status. No narration of tools.

## Standard folder layout (every project)
See `FOLDERS.md`. In short:
```
<root>/<project>/episodes/epNN-name/{edit,renders,sound,logs,previews,deliveries}
<root>/<project>/shared/{engine,assets,sound,references}
<root>/_tools  <root>/_skills  <root>/_archive
```
One `paths` file per project (`shared/engine/paths.py` + `paths.ps1`) holds the roots; scripts never hard-code absolute
paths. Moves happen only when nothing is rendering, with junctions left at old paths and a smoke test after.

## Per-pass checklist (copy into the episode's logs)
- [ ] notes -> numbered issues -> shot map -> estimate (one message to the director)
- [ ] fixes coded; each verified by a printed probe where possible
- [ ] <= 2 visual probe rounds per shot, one sheet each
- [ ] one detached queue for the whole pass + finisher + watcher + keep-awake
- [ ] `qa_auto.py` on every finished cut; look only where flagged + the one designed look
- [ ] assemble, full-cut review twice (numbers first), deliver with links
- [ ] lessons -> production skill + bible; state files updated

## Files
| file | what |
|---|---|
| FOLDERS.md | the standard project layout, the migration procedure, the paths file |
| HELPERS.md | how to brief a small-model helper (template) and which jobs to give it |
| scripts/qa_auto.py | automatic shot/episode QA: frames, black/frozen runs, stutter, exposure, loudness, true peak |
| scripts/token_report.py | tokens per session / time window from the local transcripts; the end-of-pass verdict line: "Optimus: WORKING / NOT WORKING" = tokens per finished shot down AND director corrections not up |
