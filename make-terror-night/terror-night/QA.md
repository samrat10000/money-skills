# QA: the self-review loop, the Director's eye, and gates G0-G7

This loop replaces the director pointing out mistakes. Run it for EVERY element. Log each pass in the
project's `QA_LOG.md` (`templates/qa_log.md`).

## The element loop
```
for element in plan:                      # a creature, a set, a shot, a sound pass, the edit
    build(element)
    evidence = probe(element)             # ONE contact sheet + crops + numbers / a listening reading
    LOOK at the evidence yourself         # describe it in specifics before judging
    checklist(element)                    # every line PASS/FAIL with a one-line reason
    director_eye(element)                 # the list below, in writing
    if any FAIL: write the root cause in one sentence, fix it, re-probe
    stop when all PASS and passes >= 2 (3 for the hero shot, any new creature, the first shot of a look)
    after 4 failing passes: write the blocker in EPISODE_STATE.md, tell the user with the image
```
- A fix can break what passed: re-check all lines after each fix.
- Compare against the shot card: if the shot stops doing what the plan says, it fails.
- Self-critique must be specific and numeric ("Brute is 6% of frame and behind the fender: move camera to
  x -2.9, lens 30 -> 34").

## The Director's eye (the director's real triggers, in order of how often they fired)
Write the answer to each line before sending anything:
1. **AI / cheap look?** Anything glossy, plastic, symmetric, round/cute, potato, popcorn, stick-like, "made
   of ovals", a photoreal object in the ink world, a face that looks generated?
2. **Machine motion?** Mirrored limbs, one hinge only, frozen pose, linear creature motion, floaty camera?
3. **Story gap?** Can the viewer say how he got here, why this camera exists, whose phone this is?
4. **Readable in 0.5 s on a phone?** Subject size, contrast against the background, focus, not hidden behind
   a fender/wall/rain.
5. **Sound real and on the frame?** Any synthetic tone, beep, boing, EV whine, a roar arriving late, a breath
   pitched down into a moan, a growl masking a line?
6. **Dialogue clean?** Overlaps, buried lines, the same voice for two people, a line on the wrong shot?
7. **Continuity?** Lights toggling, car stopping between cuts, wrong car model, props jumping, rain inside.
8. **Grain/noise?** Black dots, speckle, blotchy fog, shimmering textures at phone size.
9. **Repeat offender?** Is this a shot/asset the director already asked to change (search the logs)?
10. **As good as the bar?** Side by side with `reference/` approved stills (040 stairwell, 001 v2, 005 v2,
    060 garage, Brute v2 sheet, teaser 910/911): same light quality, detail density, ink, grain?

## Contact sheets
- `scripts/contact_sheet.py` makes a labelled grid. 3-6 frames for a probe (first, last, each key moment).
- Look at it full size AND at phone size (360 px wide). The phone view decides readability.
- Motion check: a strip of every 2nd frame of the action at small size (timing, asymmetry, follow-through).
- ONE sheet per probe. No look-test loops: fix with intent, then probe again.

---------------------------------------------------------------------------------------------------------
## G0 Intake
- [ ] brief.md: episode goal, length, acts, hero threat, path (A/A+/B/C), hard rules that apply
- [ ] asset inventory with approval status and past notes per asset
- [ ] EPISODE_STATE.md created with the shot table

## G1 Story
- [ ] the cause -> effect chain has no gaps (T1.1); the camera device is defined (T1.3)
- [ ] threat revealed in pieces; no spoiler cold open (T1.2); every monster tied to Sam by eyeline/action
- [ ] cliffhanger planted earlier (T1.4)
- [ ] real-world research notes for the location (materials, signage, architecture)

## GL Look test (before the first shot on any new machine or model)
- [ ] `scripts/look_test.py` still passes the 5 checks in LOOK.md section 7, side by side with `reference/look_test_expected.png`; logged in QA_LOG.md

## G2 Plan
- [ ] storyboard page: every shot `NNN_name`, time range, lens/height/move, practical lights, what moves,
      wow detail, dialogue, sound cues, the cut into the next shot
- [ ] dialogue table: no overlaps, >= 0.3 s breaths, distinct voices, phone band marked (T2)
- [ ] score plan: where it is silent, where it drops, how it thins under lines (T7.2-T7.3)
- [ ] no title text, no reused shot that had notes against it (T8.1)
- [ ] director's go-ahead (or proceeding on the recommended plan, stated)

## G3 Each asset (creature, character, car change, set)
- [ ] 3+ references saved; side-by-side sheet made (T4.1)
- [ ] turnaround: front, side, 3/4, face/head close-up, hands, mouth open
- [ ] T4.2-T4.9 line by line (no primitives, angular skull, teeth, eyes, skin, story detail, hands, grounding)
- [ ] rig test: chains bend, jaw opens down, rig saved where `city.char()` loads it (`cast/out/rig/<n>/<n>.blend`)
- [ ] exposure test in the scene's light (a creature that reads in the studio can blow out under a spot)
- [ ] 3 passes; then send stills to the director BEFORE building shots on it

## G4 Each shot
Probe (3-6 frames, RES .3-.5, SAMP 12-20):
- [ ] framing as planned; subject readable >= 8% or a clean silhouette; nothing between lens and subject
- [ ] practical lights only; no blown subject; no light ball in frame; rain only where it belongs
- [ ] matches SHOT_RULES numbers (exposure band, lens, MB, DOF f-stop, ink visible)
Motion:
- [ ] living things asymmetric with follow-through; no frozen frames; vehicles linear and speed-matched
- [ ] lights: on once, stay on; emissive meshes keyed with their lights
Full render:
- [ ] all frames present (count), none 0-byte / black / pink
- [ ] same look as the approved bar (one frame side by side)
- [ ] sound built for the shot (`snd7/sNNN.py`), cues on frames
- [ ] clip `NNN_name_vN.mp4` + stills + honest critique sent
- [ ] 2 passes minimum (3 for hero/first shot)

## G5 Sound and voice
- [ ] real recordings only, credited (sfx7/index.json -> CREDITS.txt)
- [ ] cue table vs frames: every cue within 1 frame of its cause; vocal onsets on jaw keys
- [ ] dialogue: no overlaps, breaths kept, phone band, call drops by broken words
- [ ] no score before the drop; score continuous after it, thinning under lines
- [ ] listening reading per key moment (earshot or equivalent), described in words
- [ ] -14 LUFS / <= -1 dBTP on the master

## G6 Edit and master
- [ ] built only from approved shots at 1080 from the GPU box
- [ ] no unplanned black, no frozen runs, no sound drop-outs at cuts
- [ ] light grain only, one grade
- [ ] IG file (crf 17), master (crf <= 12), phone preview (720x1280 < 15 MB), credits, download links
- [ ] watched 3 times: picture, sound, as a viewer at phone size; Director's eye on the whole episode

## G6.5 Full-cut review (twice, before ANY delivery of a cut)
Watch the whole cut with sound, then walk the shot table row by row:
- [ ] every shot is its approved, current, full-resolution version (no probes, no 720p, no old model)
- [ ] same hero car, same creature versions, same costume in every shot (T13.6)
- [ ] every cut: out-frame of N vs in-frame of N+1 side by side, place / direction / light continuous (T13.3)
- [ ] no leftover doubles, no invisible hands, no pass-throughs, no floating turns (T13.1, .2, .4, .5)
- [ ] no framing repeated in the first 30 s; the hook states place + time + event (T13.8, T15.1)
- [ ] every line audible and in its locked voice; no narration over calls (T14.1, T14.2)
- [ ] no music except the one climax piece; vehicle and creature sounds are real and approved (T14.3, T13.7)
- [ ] no dead air (look for drops below -40 dB in a per-half-second loudness scan that are not meant)
- [ ] dynamics: quiet scenes quiet, action loud (T14.5)
Log both passes in QA_LOG.md. If anything fails, it is not final (T16.1).

## G7 Learn
- [ ] every director note of this episode is in SHOT_RULES.md + MISTAKES.md with a general rule and a test
- [ ] skill update proposed (RULEBOOK line, PLAYBOOK entry) for anything new
