# QA: the self-review loop and the gates

## The loop (every shot, every asset, every fix)
1. **Probe.** Render 4-6 key frames at 40-50% resolution: start, the key pose, every in-between of a big move, the end.
2. **Look.**
   - `python scripts/contact_sheet.py <dir> <out.png> --frames 1,13,25,...` makes a contact sheet. OPEN it.
   - `python scripts/contact_sheet.py ... --crop x0,y0,x1,y1` makes full-size crops of faces, hands, feet, contact points and the newest change. OPEN them.
3. **Measure.** `python scripts/pixel_stats.py <frame.png> [--ref <reference frame>]` gives p5/p95/p99/mean. Compare with R7's targets.
4. **Write the critique** in `QA_LOG.md`: numbered, specific, harsh. List the worst 3 issues first, with one sentence of root cause each.
5. **Fix** the worst 3, then re-probe, comparing with the previous sheet AND the references side by side.
6. Repeat until every checklist line passes. That takes **3 passes minimum and 6 maximum.**
   After 6, show the best version with an honest list of what is still wrong.
7. **Full render** at 100%. Then a 10-12 frame contact sheet across the whole shot, plus full-size crops again,
   plus a check that the frame count and duration are right. Only then show it.

## The Director's-eye pass (after every element)
Write the 5 things this director is most likely to reject, and check each one at full size. From the history:
- Does any character or creature look built from shapes (ovals, cut-out cards)?
- Is anything floating (feet, toes, a hand on a grip)?
- Does every hand really grip what it holds?
- Is any real-world object guessed instead of matching a reference?
- Is the rim on the wrong side? Is the light flat or grey (p95 < 0.75)?
- Are big areas bare (plain road, flat field, plain roof, shapeless clothes)?
- Is there a glitch (a floating glint, z-fighting, a missing object, flicker, a popping hold)?
- Does any in-between have a bad drawing (an elbow jut, an arm swinging out)?
- Does anything look AI-made, glossy or symmetric?

## Checklists

### Character / creature (G-asset)
- [ ] Built from a real, artist-made rigged model (licence noted), not primitives
- [ ] Silhouette reads as the real thing in pure black
- [ ] Proportions match the age and body type (child about 1:5.5 head ratio; elderly hunch; lean stays lean)
- [ ] Outline reads at the shot distance (at least 0.00075 x camera distance)
- [ ] Turnaround contact sheet (front, 3/4, side) placed next to the references

### Shot (G4)
- [ ] Silhouette and readability of every subject
- [ ] Anatomy: hands, fingers, elbows, necks, knees; every hand grips
- [ ] Contact: feet, toes and wheels sit on surfaces every frame; contact shadows present
- [ ] Motion: on twos, holds and snaps, follow-through, weight; every in-between checked at full size
- [ ] Light: one direction matching the painted sun; rim on the sun side; p95 about 0.8-0.95, p99 at least 0.95
- [ ] Detail: roads, roofs, clothes, verges, depth cues on flat areas, correct-language signage
- [ ] Composition: subject in the upper-middle third; bottom 15% clear; sun on screen if the look needs it
- [ ] Continuity with the previous and next shot (direction of travel, time of day, costume, props)
- [ ] The shot's "wow" detail and its hidden rewatch detail are clearly there
- [ ] Technical: right frame count and duration; no flicker, missing objects, transparency holes or z-fighting; no stray glints
- [ ] Nothing looks AI-made

### Assembly (G5)
- [ ] Only approved shot versions are used (by file name)
- [ ] The cut times match the timeline, and the total length matches the plan
- [ ] Continuity across every cut (screen direction, light, speed)

### Sound (G6)
- [ ] Every line sits where the script says; nothing overlaps the next line (mix script WARNING lines = 0)
- [ ] The music starts as planned (piano in the first second) and thins under the lines
- [ ] Loudness I=-15 LUFS, TP=-1.5 (loudnorm), checked on the file

## Gates
| Gate | Passes when |
|---|---|
| G0 Intake | `REEL_STATE.md` + brief + asset inventory written |
| G1 Story | storyboard page + shot list + dialogue script shown; the director approved (or the director is away and you logged your choice) |
| G2 Look | references in `refs/`; look recipe chosen; one look-test frame next to the art-form reference |
| G3 Hero shot | hero shot through 3+ passes and shown; on approval, `SHOT_RULES.md` written from it |
| G4 Each shot | shot checklist all ticked with evidence; clip + PNGs shown; the director notified |
| G5 Assembly | silent cut from approved shots, continuity checked |
| G6 Sound | voices + score mixed, loudness met, per-shot clips with sound + full cut delivered |
