# QA: gates, checklists and the self-review loop

The loop below is what replaces the director pointing out mistakes. Run it for EVERY element.
Log each run in `QA_LOG.md` (template in `templates/qa_log.md`).

## The element loop (BUILD -> LOOK -> SCORE -> FIX -> RE-LOOK)

```
for element in plan:
    build(element)
    evidence = probe(element)          # contact sheet / script numbers / listening readings
    LOOK at the evidence yourself      # open the image; read the numbers. Never skip.
    score = checklist(element)         # every line PASS/FAIL with a one-line reason
    director_eye(element)              # name the 5 most likely rejections; check each
    if any FAIL: fix the root cause, then repeat from probe
    passes += 1
    stop only when: all PASS AND passes >= minimum (2 per shot, 3 for hero shot / hero creature)
    if 5 passes still fail: write the blocker in TEASER_STATE.md and tell the user, with images
```

Rules of the loop:
- Fix ROOT causes, not symptoms (the "stop then fly" car was two Bezier keys, not a bad cut point).
- After a fix, re-check the items that passed before; fixes break other things.
- Compare against the plan (`beat_sheet.md`): if the shot no longer does what the plan says, it fails.
- Self-critique must be specific: "left hand rises 4 frames after right, OK; right hand tremor
  invisible at phone size, FAIL, raise amplitude 1.3 -> 2.5 deg".

## Director's eye (run after every checklist)
Answer in writing: "If the director watched this on a phone right now, what would they reject?"
Always check these known triggers first:
1. Does anything look like AI, CG-cheap, plastic, toy-like, round/cute where it should be scary?
2. Does anything move like a machine (mirrored, linear, one hinge, frozen)?
3. Does anything stop, freeze, jump or go black that should flow?
4. Is the subject readable in 0.5 s on a phone (size, contrast, focus)?
5. Is every sound real and on the exact frame of its picture cause?
6. Is the music/sound continuous across the cut?
7. Is it as good as the poster / the approved hero shot?

## Contact sheets (how to look)
- `scripts/contact_sheet.py` makes a labelled grid. Use 6-12 frames: first, last, every planned key
  frame (impact, jaw snap, cut-in, cut-out) and 2 in-betweens.
- Look at the sheet at full size AND at phone size (downscale to 360 px wide). The phone view
  decides readability.
- For motion, also make a motion strip: every 2nd frame of the action at small size, so timing,
  asymmetry and follow-through are visible.
- ONE contact sheet per probe. Do not loop endless look-tests; fix with intent, then re-probe.

---------------------------------------------------------------------------------------------------
## Gate G0: Intake
- [ ] brief.md has: logline, hero character/poster (confirmed), style, length, platform, input path (A/B/C/D)
- [ ] asset inventory with quality scores; missing assets listed
- [ ] TEASER_STATE.md created

## Gate G1: References
- [ ] 3+ references per creature/character/prop, saved, explained in refs/README.md
- [ ] 2+ pacing/camera references noted with what you take from each

## Gate G2: Plan (beat sheet + animatic)
- [ ] 8-14 shots, numbered `NNN_name`, total length within target
- [ ] cold open = silence + one clean real hit; threat revealed in escalating pieces (R2.2)
- [ ] cuts shorten toward climax; hero shot 4-6 s; one dark beat only before the stinger
- [ ] every shot: lens, move, height, subject, wow detail, sound cue, continuity contract
- [ ] continuity contracts: speed/direction/light written for every adjacent pair of moving shots
- [ ] no on-screen text; no reused episode shots
- [ ] animatic plays with scratch timing; storyboard page made; plan sent / or proceeding on recommended plan

## Gate G3: Each asset (model, rig, set)
- [ ] turnaround sheet (front, side, back, 3/4, close-ups of hands/head/teeth/eyes) vs references
- [ ] R4.1-R4.10 checked line by line (sharp bone, real hands, no primitives look, eyes, teeth, grounding, rubber tyres)
- [ ] rig test: every chain bends smoothly, jaw opens DOWN from the back hinge (print positions)
- [ ] materials: no glossy/plastic surfaces where they should be organic; textures not dotty at phone size
- [ ] scale check next to a car/human
- [ ] 3 passes for hero creature/character

## Gate G4: Each shot
Probe (2-5 frames, 360x640, 12-20 spp):
- [ ] framing matches the plan; subject coverage >= 8% or clear silhouette (`vis_check.py`)
- [ ] focus on subject; nothing blocks the lens; no stray lights/blobs in frame
- [ ] exposure: subject region not crushed (mean luma > 0.08), highlights not blown on faces/eyes
Motion (motion strip):
- [ ] living things asymmetric, follow-through, weight, tremor, no frozen frames (R5.1-R5.4, R5.11)
- [ ] vehicles linear and speed-matched to neighbours (`check_motion.py`) (R5.7)
- [ ] skids over-rotate and settle; body roll; spray (R5.8)
- [ ] camera: handheld/real, kicks on impacts, no floaty drone (R3)
Full render:
- [ ] all frames present, none 0-byte, none black/broken, no pink/missing textures
- [ ] same look as the hero shot (compare one frame side by side)
- [ ] shot clip encoded as `NNN_name_vN.mp4` with your critique
- [ ] 2 passes minimum (3 for hero)

## Gate G5: Sound
- [ ] only real recordings; every source credited in CREDITS_sound.txt
- [ ] each cue placed by frame from timeline.json; vocal attacks on jaw keys (onset-aligned)
- [ ] listening-tool pass per moment: describe what is heard at each key time and compare with the plan
- [ ] no moans (no pitched-down breaths), no boings, no synthetic buzz, no glass tail under thunder
- [ ] continuity: ambience/rain bed never drops out at a cut unless it is the planned silence
- [ ] -14 LUFS integrated (±0.5), true peak <= -1.0 dBTP
- [ ] phone-speaker check: low-pass the mix at 200 Hz high-pass (phone speaker sim) and confirm the key cues still read

## Gate G6: Final edit
Run `python3 scripts/qa_check.py final.mp4 --timeline timeline.json` and confirm:
- [ ] resolution, fps, duration in target
- [ ] black runs: only the planned dark beat
- [ ] frozen runs (identical consecutive frames > 3): none, except planned holds
- [ ] cut list matches timeline.json (±1 frame)
- [ ] motion energy does not collapse to ~0 at any cut between two moving shots (catches "car stops")
- [ ] audio: loudness/peak in spec; no silent gaps except the planned ones; audio not cut off at the end
- [ ] watch the full teaser 3 times: once for picture, once for sound, once as a viewer on phone size
- [ ] Director's eye pass on the whole teaser
- [ ] deliverables per R0.5 and download links per R8.3
