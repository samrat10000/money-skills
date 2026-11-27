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

## v7 "final" cut (11-24): director "disappointed"
Kept as perfect: phone + answer, blast, stairwell, garage + car opening, rolling out, the empty-seat ending.
- Screamer: an "absolute trash" scream swapped in for the superb earlier one; it turned without moving its
  legs (floating). -> Approved sounds are locked (T13.7); a still creature + camera push (T13.5).
- Key grab: Sam still sitting on the sofa. -> One body, one place (T13.1).
- Corridor: Sam's voice read female. -> Locked voice cast (T14.1).
- Stairs -> lobby -> garage jumped. -> No geography jumps (T13.3); build the connecting moves.
- Phone picked up by an invisible hand in the car. -> Show the hands (dashcam on the driver) (T13.2).
- Car sound "trash". -> Real V8 + tyre recordings at teaser grade (T14.4).
- The car drove through the Brute and nothing happened. -> Collision check + a shown outcome (T13.4).
- Old Stalker in the bridge scene instead of the teaser model and its skull movement. -> Latest approved only (T13.6).
- Narration buried under the call. -> Narration only in gaps, 9-12 dB above the bed (T14.2).
- Background music. -> None; one climax piece only (T14.3).
- Self-found: the tripod wide 4x in 20 s, two different cars, the missing gate/aerial, 720p and probe frames
  in a "final", a dead gap before the ignition, every scene the same loudness. -> T13.8, T13.6, T16.1, T14.5.
- Root cause: the cut was called final without the full-cut review. -> G6.5 twice, T16.

## Process mistakes
- Sending whole episodes; waiting on approvals between steps; status chatter; look-test loops; cloud finals.
- Asking the GPU box session to install software on a coordinator's say-so: it correctly refused; the user's
  own OK is needed (T12.2). Ask the user directly, early.

## Ep1 v8 resume (2026-11-25, Claude Code on the Asus)
- **Ducking that never let go.** `mix_v8.py env()` ran its follower every 48 samples with per-sample coefficients: attack
  1.4 s, release ~17 s. Every line kept all SFX/beds 10-16 dB down for ~17 s ("the sound effects are not there"). Rule: any
  control-rate envelope uses `exp(-step/(t*SR))`; test = render a 1 s line over a constant bed and check the bed is back
  within 0.5 dB 1 s after the line ends.
- **A queue that encodes partial cuts.** A stopped Blender still produced an mp4 for cut 525 at 63/144 frames, which the
  queue then SKIPPED as done. Rule: encode only when the expected frame count is present.
- **Set pieces that do not exist.** The hook's "tower beyond erupts" had no tower: the fireball floated in black. Rule: every
  event in the shot card has geometry under it; probe the frame AFTER the event, not only before.
- **Dashcam looking up at an overpass**: at 50 mm the deck face fills half the frame. Aim above the creature's head with a
  longer lens (85 mm) so the parapet is the bottom edge.
- **Blown moon (150 v8).** The overpass `moondisc` (emit 40) reads as a white ball when it lands beside a close-up. Rule:
  any emissive disc/sky object that can enter a close frame gets emit <= 4 so it glows through fog; check every frame edge.
- **Event out of frame (152 v8).** A long-lens watcher aimed at the landing spot never shows the fall itself. Rule: a
  tracking long lens STARTS on the subject and follows the event; probe the event frames (T9.6).
- **Fixes need a second pass.** A queue already past a cut will not revisit it: archive the old frames + mp4 to `v8_old`,
  then a `queue_after.ps1` waits for the running queue and re-runs it (only cuts without an mp4 render).
- **One Blender per cut creeps (Ep1 v8 night of 2026-11-25).** On the 4 GB card the hook went from 19 s to 3-8 min per
  frame over ~100 frames; a "no frame in 8 min" watchdog never fired because slow frames still landed. Rule: ALWAYS render
  in 25-frame chunks with a fresh Blender per chunk (`scripts/queue_template.ps1` does it); watch seconds-per-frame against
  the cut's first chunk, not just "any frame lately".
- **AAC overshoot (Ep1 v8 final).** A WAV master at -1.0 dBTP measured +0.3 dBFS after the AAC mux. Rule: master to
  <= -2.4 dBTP (`master.py` ceiling .58) and measure the FINAL mp4s, not the WAV; a 128k phone encode needs ~-0.6 dB more.
- **hide_render kills the light (152).** Hiding an emissive moon removed the street's key light (frames went black). To
  drop a visible disc but keep its light and reflections: `obj.visible_camera = False`. Set materials on the OBJECT slot
  when the mesh uses object-linked materials (a mesh-material swap silently did nothing on 150).
- **Crowds vs a 4 GB GPU.** 44 rigged + 22 duplicate zombies took ~25 min/frame even with texture 1024 + simplify 1
  (VRAM 3.9 GB, spilling to shared memory). Rule: probe ONE frame of every crowd shot on the target GPU before queueing;
  over ~3.5 GB, render the crowd as a separate pass or cut rigged count, decided with the director.
- **Process control from Git Bash.** `powershell -Command "Stop-Process ..."` / `Start-Process` inside a bash string
  failed silently twice (an orphan Blender held the GPU 30 min, a queue never started). Use the PowerShell tool directly
  and verify with a process listing afterwards.

## v9 review pass (11-26/27)
- **Lights aimed away from the subject.** Both "city fire on him" AREA lights (hook 000, 004w) had `rot=(0, radians(-90), 0)`,
  which points the light's -Z along +x, i.e. AWAY from Sam into the street; 004w's also sat outside the glass. Sam stayed a
  black column for two versions while the comment said "lights his front". Rule: for every key light, print its world
  direction (`lo.matrix_world.to_3x3() @ Vector((0,0,-1))`) against the vector to the subject in the dry run; the dot product
  must be > 0.7. Put lights that must reach an interior INSIDE the glass and set `visible_camera = False`.
- **Explosion inside the roof.** The hook fireball was centred 3 m above a roof whose crown was at 47 m: the roof sliced it
  flat (a pasted sprite) and its only light sat above the roof, so the camera face stayed black. Rule: an explosion bursts
  OUT of the camera-facing face, has a light IN FRONT of that face and one above, and blown-out emissive floors under it;
  ray-test the fireball centre from the camera (DRY) before rendering.
- **Blender 5 layered actions.** `action.fcurves` no longer exists; a cut crashed in the queue. Always go through the
  `_fcurves(action)` helper (layers -> strips -> channelbags).
- **Phone encode true peak.** 128 kbps AAC re-encode overshot to -0.2 dBTP from a -1.4 dBTP master. The phone encode gets
  `volume=-1.2dB`; measure every delivered file with ebur128 peak=true.
- **qa_auto stutter false positive in near-black frames**: frame diff collapses when luma < 8 (car passing over the lens).
  Check luma alongside motion before chasing a stall.

## v9 rejected by the director (11-27): "worse than v8"
Director's words (condensed): the explosion is on Sam's window, he would be dead; the facades still lack the details I asked
for; Sam in the chair is a block, nobody sleeps like that; the phone text still overflows and it is the same phone; the engine
sound is worse than v8; the Brute hit looks like a push; the bridge was epic in v8 and you made it worse; subtitles placed
wrong; half my report is not done. Rules born from it (apply to EVERY shot, every episode):
- **Story check on every shot card:** where is the hero, can this physically happen to him, does it contradict the shot before
  or after? An explosion must be far from the hero, readable as far (depth, scale cues, haze), never on his building.
- **Never "defer" a director's note silently.** A pass ships only when every note ID has a frame/number proving it is done.
  If something truly cannot be done, ask BEFORE the pass, never announce it in the release notes.
- **Approved = frozen.** Anything the director called good (shot, sound, timing) stays byte-identical unless he names it.
  When fixing one moment of an approved shot (152 jump), splice the fix into the approved version, do not rebuild around it.
- **A/B against the previous version** for every changed shot and every changed sound, before calling it better.
- **Review depth:** 3-4 full looks per shot + full-size crops of faces, hands, phone screens, subtitles; Optimus look limits
  never apply to the final review.
- **Characters:** the hero must be a detailed model (face, hands, clothing folds) in a natural pose for the action (sleeping =
  head dropped, shoulders slumped, arms heavy, hands loose). A dark lump or a low-poly hood fails the shot.
- **Sound I cannot hear:** keep the sound the director approved; change only what he names; measure the A/B (spectrum,
  loudness per bus) and describe the difference honestly.
- **Subtitles:** a consistent low band (bottom ~20-24% of frame, clear of IG UI), never on the action; check every cue on a frame.
- **Research references first** (how films shoot car hits, distant explosions, phone screens) before building a hero moment.

## v10 build (11-27): fakes found while fixing the director's notes
- **Fake windows.** The approved stairwell 'windows' were rain glass 8 cm in front of a SOLID wall; the city glow and the fire
  light sat behind the wall (no outside, no light in, 'jittery' glass). Rule: every window/door that the story looks through
  gets a real opening (boolean or wall segments) and is ray-probed (DRYPX through the glass must hit the outside).
- **Fake door.** The 'LOBBY door' was a label on a wooden apartment door in a solid wall, its light behind the wall. Rule: a
  door the hero goes through is a real door in a real opening that opens on screen, with real-world signage (NYC stair
  re-entry sign: STAIR A / FLOOR L).
- **Floating hands since v8.** The driver's arms were IK-clamped (seat .34 m too far back): both hands hung in front of his
  chest, never on the wheel or the key. Rule: print the wrist world position vs its target (DRYBONE) for every hand pose;
  > 5 cm = fix the body placement, not the camera.
- **Wrong side of the light / stale matrices.** After parenting appended objects, matrix_world is stale until
  view_layer.update(): every position test after a parent/append starts with an update.
- **No PIL inside Blender.** Textures drawn with PIL must be generated by the system Python first (make_tex_v10.py);
  v7sets._tex() only loads cached files.
- **Decal orientation.** A decal facing -y must be rot (90, 0, 0); (90, 0, 180) mirrors the text and flips images.
- **One long-lens rule:** a window frame/mullion 2-3 m in front of the subject crosses him at 500 mm; hide the bar or move
  the camera (parallax), never accept a bar through the hero.
- **Story distance.** A 250 m 'safe' blast drowned in haze (soft sun, no punch); the right fix for 'too close to Sam' was the
  director's own reference spot (v8) + the stronger v9 look. Try the director's reference before inventing.
- **Backslash escapes, again (v10 night).** Scripted edits wrote rf'{KEEP}\002_...' / '\060_...' through a normal Python
  string: '\0..' became control characters, the assembler fell back to a black MISSING placeholder for 060. Rule: after any
  scripted edit of a file holding Windows paths, scan it for control characters (ord < 32) and re-run the assembler's
  source table; a MISSING/STAND-IN line blocks the release.
