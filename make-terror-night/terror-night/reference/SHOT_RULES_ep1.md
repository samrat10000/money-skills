# SHOT_RULES: Night Terror Ep1 v7 (the locked recipe)

Locked from: 040_stairwell (2026-11-22 2:03 PM IST). The director's words: "damn cool, I want this realism
in all the other clips". Source: engine/ep1/v7sets.py cut40, sound engine/ep1/snd7/stair_snd.py.

1. Engine/look: Cycles, AgX Medium High Contrast, exposure 0 for the stairwell (other sets -0.9..+1.1,
   chosen so the subject region reads), ink hulls (`L.hull` / `join_ink`) on rails, frames, doors, props.
2. Lights: practical only. Camcorder lamp spot 26-30 W, 72 deg, blend .5, parented to the camera, warm.
   Emergency lamps 45-60 W, one strobing (`strobe`). Fire glow through windows (`fire_flicker`, slow keys).
   Tubes and headlights keyed on once with constant interpolation. No blue ambient wash.
3. Camera: POV stairs `pov_stairs` (heel-strike dip ~18 cm per tread, sway, noise), look up and across;
   handheld shake small (`real_shake` preset); MB .15-.25; DOF f/6 (f/4 for close-ups); focus on the subject.
4. Textures: marble with fine thin veins, pattern scales x.25 (smooth at phone size), sparse rain drops on
   glass; previews SAMP >= 20; finals 48-64 + OptiX denoiser; encode hqdn3d=3:3:5:5; light grain only.
5. Dressing density: hex-tile landings, worn marble treads, cast-iron balusters, oak rail, brass elevator
   cage, flyers, spray tags, claw marks, hand smears, door numbers, hose cabinets.
6. Sound bed: footsteps on every footfall frame on the right surface, room tone, breathing, strobe tick, a
   heartbeat sub; no score before the ignition.
7. Render: probe RES .3-.5 SAMP 12-20 (cloud); final RES 1 SAMP 48 DEVICE=GPU on the GPU box.

## 10. Improvement log
- 11-22 "fire jitters too fast" (001) -> fire keys every ~6 frames, many places, smoke -> test: 2 s strip.
- 11-22 "sky must not be pitch black" -> fire-lit clouds + stars + ash + rain -> test: sky luma > .03.
- 11-22 "hand must not hover in an L" -> rest pose until the action -> test: side probe of the hand.
- 11-22 "phone sank into his head" (003) -> IK outside the ear, bbox > 12.5 cm from head centre.
- 11-22 "beep beep is irritating" (005) -> calldrop.py broken words, click, dead line.
- 11-23 "too much grain, black dots" (050) -> SAMP >= 20, sparse glass drops, textures x4, hqdn3d, light grain.
- 11-23 Brute "potato" -> wedge skull, brow plate, torn cheeks, dark skin -> test: front silhouette not an ellipse.
- 11-23 "skull still slightly round from the front" -> taper the top 30% of the cranium, crown ridge, wide jaw.
