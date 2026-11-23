# MISTAKES: every rejection of Night Terror Ep1 (v1 -> v7) and the fix

Read once. Each line became a rule in RULEBOOK.md. Dates are 2026-11 (IST).

## v1 (11-19): 35 s, 8 shots
- Zombies in frozen poses; slideshow pans; not enough real angles. -> Real character animation, many real
  handheld angles (T6.1, T3.1).
- No background music; weak SFX; music cut out suddenly at the end. -> Continuous score, real SFX (T7.3).
- 10-11 s sweep transition read as a slideshow. -> Real cuts only (T3.1).
- Big "NIGHT TERROR / DEAD ROADS" title over the best shot. -> No titles (T0.2).
- Wanted real slow-mo moments (blended slow-mo looked fake). -> True slow-mo by time remap, once (T3.6).
- The Crawler looked like it sank into the ground. -> Grounding check (T4.9).
- Ending cut to the Stalker with no payoff. -> Cliffhanger structure (T1.7).
- LOVED: the Stalker/"reindeer" reveal (10/10).

## Sound and music (11-19 to 11-20)
- Engine sounded like an EV; steps/rain unreal. -> Real recordings (T7.1).
- AI music takes (ACE-Step) "trash, don't match the story". -> Never deliver raw AI music.
- Synthesized Karplus-Strong guitar "irritates the ears". -> Real guitar samples or Flow Music.
- A 0.5 s insert felt misplaced. -> No sub-1 s inserts.
- Crawler entrance sound "pathetic"; later "crawler sound hated". -> Sparse real claw taps on hand plants.
- Scream level and the orchestral ending were "perfect": keep.

## v2-v3 (11-20)
- Rider's arms and hands looked broken (squeezed inward). -> Hand/arm anatomy check before rendering (T4.8).
- Wanted "bullet time" (world freezes, camera moves A->B), not 90s blended slow-mo. -> warp_shot.
- The Stalker must act (head turns, eyes glow, jaw opens). -> stalker_alive.
- Wheels spun backwards and the car bounced. -> Spin sign, car-aligned pivots, motion_steps 6, body on springs.

## v4 (11-20)
- Orbit freezes that cut to a new angle broke the flow; whip transitions = slideshow. -> ONE-take freezes.
- Warp camera passed through parked props (pink/white frames). -> Hide small props within .45 m of the path.
- Stalker must stare with the mouth open, then scream at the sky with its own scream.

## v5 (11-20 10:34 PM): "best so far"
- KEEP: the Screamer, the garage scene ("best scene ever"), the Stalker scream.
- Too much Crawler footage, bad angle, hated crawler sound.
- No slow-mo at 14 s: move the camera to show how BIG the horde is (T3.7).
- Garage headlights flickered on/off: keep them off, light the car with tube lights, headlights on ONCE (T6.6).
- The 29 s skid must be one smooth Tokyo drift, no slow-mo, no stop-start (T6.5).
- The Brute needs the car's engine growl, and looked like a "potato": redesign scarier (T4.3).
- Stalker mouth needs horror: blood/drool, a stitched mouth that tears open (T4.4).
- New: Sam waking up to the call, the alert, keys, the escape, garage, aerial, low ground shots.

## Sam's character (11-20 to 11-21)
- MakeHuman Sam v1/v2 "ewy", bodybuilder, fingers outward; v4/v5 "terrible". AI video (Flow/Veo) Sam "looks
  AI". -> Sam's face is never shown: silhouette, back, hands, POV (T4.8). Final, never revisit.
- Procedural Manhattan read blocky/CG after 9 look tests. -> A real NYC night plate re-painted in ink style.

## v6 (11-22 12:24 PM): REJECTED as a whole
- Five reused v5 shots were the exact shots the director had asked to fix (crawler blur, freezing skid,
  potato Brute, hollow Stalker mouth, flickering headlights). -> Search the logs before reusing (T8.1).
- The v5 garage reveal (his favourite) was replaced by a dark POV. -> Keep what he loves.
- Three looks mixed (orange photo city, photoreal phone, ink 3D); the VHS blur killed the ink lines. -> One
  look; camcorder feel from camera work + light grain, not blur (T5.2).
- Story gaps: no keys, no exit, no lobby, never gets in the car, the ending phone "random". (T1.1, T1.4)
- The Stalker flashed in the first half second. -> No spoiler cold open (T1.2).
- Voices overlapped (4), lines buried (5), Akash and the radio shared one voice, a synthetic buzz opened the
  episode, the score was built for the v5 clock and fought the dialogue. (T2.1, T2.2, T7.1, T7.2)
- Cheap stairwell (scope-circle torch, blotchy walls, pipe rail); walking/stair animation bad. -> Pre-war
  stairwell + POV with footfalls, never third-person walking (T6.7).
- Screamer not connected to Sam. -> Eyeline (T1.5).
- 432 px cloud renders stretched to HD. -> Finals at 1080 on the GPU box.

## v7 (11-22 onward), shot by shot
- 001 v1: fire jittered too fast, one place; sky pitch black; hand hovering in an L. -> T5.6, rest pose.
- My own catches before sending 001: fire glow floating in the sky, the phone screen upside down to camera,
  a visible point-light ball. -> Look at every probe.
- 003 v1: the phone sank into the side of his head and looked AI-made. -> T4.10.
- 005 v1: beep-train call drop "irritating". -> calldrop.py (T2.4). v2 approved.
- 050 v1: "too much grain, black dots" (all-over Voronoi glass bump, 10 spp fog noise, speckled marble and
  paint). -> T5.3, T5.4.
- Lobby set: rain fell inside and the street showed through the floor. -> Rain outside only, floor raised.
- Corridor: a solid void box hid the stair space; an area light faced the wrong way; doors swung into the
  corridor. -> Build the room; check -Z facing; check the ajar sign.
- Garage: tube meshes glowed while their lights were off. -> Key emission with the light.
- 070: the phone was invisible/odd (bx() applied the transform), landed face down, cabin too dark. -> Build at
  origin, key into place; Principled emission; fill 40 W.
- 152: a different car model (white/blue livery). -> Excluded; one car (T8.2).
- 140/150 Stalker close-ups read flat red with stick arms (a 40 W red "ember" point light flooding, pink
  fog). -> Ember x.3, fire rim + cold rim + headlight spill, fog <= .0008 (T5.9).
- Brute v1 "potato" (round bald head, pink skin, cone spikes). v2 approved ("coolll"); then "the skull is
  still slightly round from the front": wedge cranium (taper the top 30%), crown ridge, flat temples, wide jaw.
- 125 v1 test frames: the car fender hid the Brute (camera too close to the car); a 2600 W headwash blew the
  Brute's skin to cream; a white flare when the car drove through that light. -> Camera at x -2.9, 650 then
  380 W, light keyed off before the car moves.
- 160 test: rain streaks inside the cabin in front of the lens (rain box overlapped the camera). -> T5.5.
  The phone screen at emission 5 blew to a white bar; 2.2 better, tilt it toward the lens.

## Process mistakes
- Sending whole episodes; waiting on approvals between steps; status chatter; look-test loops; cloud finals.
- Asking the GPU box session to install software on a coordinator's say-so: it correctly refused; the user's
  own OK is needed (T12.2). Ask the user directly, early.
