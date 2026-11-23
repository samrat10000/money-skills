# Ep1 mistakes Sam caught, and the fix (append only)

- v1: Music cut out suddenly, slideshow transitions, title text over the best shots, and the Crawler looked like it was under the ground. Fix: continuous score, real cuts, no titles, and characters grounded on surfaces.
- v1 sound: the engine sounded like an EV, and the steps and rain sounded unreal. Fix: a physical V8 model plus real recordings.
- v2: The rider's arms and hands looked broken. Fix: anatomy checks on hands before rendering.
- MakeHuman Sam v1-v5 was rejected ("ewy", bodybuilder, "terrible"), and AI video Sam was rejected (looked AI). Fix: keep his face hidden.
- v6 (rejected 2026-11-22):
  - Voices overlapped and lines were buried. Fix: one line at a time.
  - A synthetic buzz at the start. Fix: real sounds only.
  - The reindeer showed in the first second. Fix: no cold open.
  - A cheap-looking stairwell with no horror. Fix: the pre-war NYC stairwell, which Sam approved.
  - Bad walking and stair animation. Fix: POV camera with footfalls, and no third-person walking.
  - The music fought the dialogue. Fix: no score before the ignition.
  - The Stalker's mouth looked hollow. Fix: the new bull skull.
  - The phone in the car felt random. Fix: plant the phone on the seat.
  - I reused v5 shots Sam had already asked to fix. Fix: re-check his old notes before reusing any shot.
  - I mixed three looks (photo plate, photoreal phone, ink 3D). Fix: one look.
- 001_ring v1:
  - The distant fire jittered too fast and showed in only one spot. Fix: slow burning blocks in many places, with smoke.
  - The sky was pitch black. Fix: fire-lit clouds, stars, rain and ash.
  - The hand hovered in an L shape. Fix: it rests in his lap and only reaches out when he wakes.
- My own catches: the fire glow floating in the sky looked fake, the phone screen was upside down for the camera, and a visible point-light ball showed in frame. All fixed before sending.
- 003_answer v1 (Sam 2026-11-22 4:23 PM IST): the phone sank into the side of his head and looked AI-made. He liked the hand placement and the phone's look. Fix: two-bone IK targets a point beside the ear, then pushes outward until every phone bbox corner is more than 12.5 cm from the head centre (HEAD_R, EAR_OUT env).

## 005_bridge sound (2026-11-22 ~6 PM IST)
- Sam: the repeated "beep beep" signal-cut sound (CC0 "Cell Phone Interference Noise" + distant car alarm) was irritating.
- Fix: no beeps for a dropped call. snd7/calldrop.py breaks the caller's own words (packet-loss gaps, stutter repeats, crunchy low bitrate), cuts mid-word, then a small click and a dead line. Use it for every call drop.
- Door pivots: set the empty's location, then call bpy.context.view_layer.update() BEFORE parenting with matrix_parent_inverse. Otherwise the children jump. Area lights face -Z, so check the rotation sign. A solid "void" box behind an opening door hides everything; build an open room instead.

## 050_lobby grain (Sam 2026-11-23 1:39 AM IST)
- Sam: "too much grain, black dots". A little grain is fine.
- Causes:
  - The rain-glass material bumped a Voronoi cell pattern over the WHOLE pane, which reads as dots.
  - 10 spp cloud previews with fog volumes leave noise blotches.
- Fixes:
  - m_glass_rain now has sparse drops only, with a weaker bump.
  - Previews at SAMP 20 or more. Finals on the Asus at 64+ spp with the OptiX denoiser.
  - Encode with a mild hqdn3d, and add only a light, even film grain (noise alls=3) if any.
- Applies to every later shot.
- 070 phone: bx() with rot=(0,0,0) applies the transform, so the mesh's origin sits at the world origin. Keying .location on it then double-offsets it and rotates it around the world origin. Build animated props AT the origin and let the keys place them. Use a Principled emission material (not K.emit) when the strength must be keyed.
