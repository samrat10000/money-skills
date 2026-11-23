# RULEBOOK: every rule, its test, and the rejection that created it

Format: **ID. Rule.** *Test:* how you prove it. *Why:* the director's words or the failure behind it.
MUST rules are hard fails. If the user's current request contradicts a rule, the user wins: write the override
in `DECISIONS.md`.

---------------------------------------------------------------------------------------------------------
## T0. Format, naming, delivery
- **T0.1 MUST** 1080x1920, 24 fps, H.264 yuv420p, AAC 192-256k, `+faststart`. Episodes 60-100 s.
- **T0.2 MUST** No title text, logos or captions over the picture. Diegetic text (phone screens, signs, door
  numbers) is fine. *Why:* v1 "NIGHT TERROR / DEAD ROADS" over the best shot was rejected.
- **T0.3 MUST** Number every shot and name files `NNN_short_name_vN.mp4` (e.g. `125_brute_block_v2.mp4`).
  Shot numbers step by 10 so inserts fit (125 between 120 and 130). New version = new file name, forever.
- **T0.4 MUST** Deliver each shot alone the moment it passes QA: clip (720x1280 preview is fine during
  production) + 2-4 stills + an honest critique (great / still weak / what you will fix in the final).
- **T0.5 MUST** Files > 20 MB also get a direct download link (GitHub raw + blob page). Phone previews of big
  attachments have no download button.
- **T0.6** The full episode is cut ONLY from approved shots, at full 1080 from the GPU box.

## T1. Story and structure
- **T1.1 MUST** No missing steps. Every location change is shown or caused: wake -> phone -> keys -> door ->
  corridor -> stairs -> lobby -> garage -> car -> phone on the seat -> ignition. *Test:* read the shot list
  aloud as cause -> effect; any "how did he get here?" fails. *Why:* v6 "he never takes the keys, never
  gets in the car, the ending phone feels from another film".
- **T1.2 MUST** No cold open that spoils the monster. The threat is revealed in escalating pieces (sound ->
  sign -> silhouette -> partial -> full). *Why:* v6 opened with a half-second Stalker flash.
- **T1.3** A found-footage reason for every camera (the camcorder device). POV shots are the camcorder.
- **T1.4** Plant and pay off: the cliffhanger image must be set up earlier (phone tossed on the seat in 070
  pays off in 160).
- **T1.5** Every monster encounter is connected to Sam by an eyeline or an action (the Screamer turns toward
  HIS window). A monster "somewhere" is filler. *Why:* v6 "the Screamer isn't connected to Sam".
- **T1.6** Each shot has ONE wow detail written in its shot card (water sheeting off a tyre, the phone glow on
  the empty seat, the handprint blooming on the glass).
- **T1.7** End: hit -> cut to black on the impact -> 1-1.5 s black silence -> the quiet final image (held,
  long enough to read).

## T2. Dialogue and voice
- **T2.1 MUST** One line at a time, at least 0.3 s of breath between lines, never overlapping. *Test:*
  dialogue table start/end times; no overlaps. *Why:* v6 four overlaps, five buried lines.
- **T2.2 MUST** Distinct voices: friend, radio and Sam never share a voice. The radio is a robotic EAS voice.
- **T2.3 MUST** Phone voices go through the phone-speaker band (HP 350, LP 3400, light bit crush, tiny echo).
- **T2.4 MUST** Call drops: never beeps or interference tones. Break the caller's own words (packet-loss gaps,
  stutter repeats, low-bitrate crunch), cut mid-word, a small click, dead line (`engine/ep1/snd7/calldrop.py`).
  *Why:* "the beep beep is irritating".
- **T2.5** Lines are written short and natural (panicked fragments, names repeated: "Akash? Akash!").
- **T2.6** The picture timing is planned against the dialogue table from day one; lines never sit on a shot
  that contradicts them.

## T3. Camera
- **T3.1** Default = handheld camcorder: operator micro-shake (`real_shake` / shakify data), late reframes,
  eye height. Walking = step-synced POV (heel-strike dip ~18 cm per stair tread, sway, look up and across,
  not at the floor). Never drone-floaty moves, never slideshow pans on stills, never sweep/whip transitions.
  *Why:* v1 "slideshow", v4 "whip transitions = slideshow".
- **T3.2** Proven moves: tripod timelapse frame; phone insert; over-the-shoulder at the glass; long-lens CU
  across the street (135 mm); handheld rip off the tripod; POV corridor; POV stairs; tilt-up through the
  glass to reveal crowd scale; dolly into the garage as tubes clunk on; dashcam lens 16-18 mm; 20 mm tyre cam
  on the asphalt; low chase follow; crash zoom over an occluder to a face then pull back; ECU of the eye;
  low camera behind the car as a monster steps into the headlights.
- **T3.3** Camera kicks (decaying ~2 deg jolt over ~10 frames) on impacts, revs, screams.
- **T3.4 MUST** Focus on the subject: focus distance = ray-cast distance to the subject; f/4-f/6 so ink lines
  survive. *Test:* subject edges sharp at 100% in the probe.
- **T3.5 MUST** The lens is clear: no rain particle, prop, car body or set wall between camera and subject
  unless planned. *Test:* first and last frames of every moving shot. *Why:* 160 test had rain streaks
  inside the cabin in front of the lens; 125 test had the car fender hiding the Brute.
- **T3.6** Freeze/bullet time only as ONE continuous take (live 1x -> ramp to ~3% -> camera glides -> ramp back
  from where the camera ended). Never orbit-freeze then cut to a new angle. Never frame-blended slow-mo.
  Slow-mo max once per episode, only where earned. *Why:* v3/v4/v5 notes.
- **T3.7** Show scale with camera moves, not with slow-mo: tilt up through the glass to the horde, drone
  lift over the avenue. *Why:* v5 "no slow-mo at 14 s; move the camera to show how BIG the horde is".

## T4. Characters, creatures, anatomy
- **T4.1 MUST** Real references (3+) for every creature/character/skull/hand before building; compare side by
  side (`*_vs_refs.jpg`). *Why:* "popcorn" skull; bodybuilder Sam.
- **T4.2 MUST** No organic primitives (ovals, tubes, sticks, cones as anatomy). Start from the MakeHuman CC0
  base (`engine/cast/`), a real CC0/CC-BY model, or a proper sculpt. *Why:* "earthworm", "sticks", "potato".
- **T4.3 MUST** Horror skulls are angular: wedge cranium, flat temples, brow plate, crest/ridge, wide jaw,
  bone ends tapering to spurs. Never round or egg-shaped from the front. *Test:* front-view silhouette is
  not an ellipse. *Why:* Brute v1 potato; "the skull is still slightly round from the front" (Brute v2 note).
- **T4.4 MUST** Teeth = crooked blades of mixed length, some missing or broken, dark-stained; mouth interior
  dark, wet, wrinkled; never neat squares, never a hollow black hole. *Why:* Stalker v5 "mouth is a hole".
- **T4.5 MUST** Eyes: tiny ember or ember-vein orbs deep in the sockets, specular highlight, saccades for
  close-ups. Never flat dots, never snake slits, never white glowing human eyes on a monster.
- **T4.6** Skin: dark, desaturated, rough (roughness .6-.8), with wet red cracks only in grooves; no pink
  plastic, no shiny grey/silver. Bone spurs dark (#2e2820-#6a5e4a), few and thick, not yellow cones.
- **T4.7** A story detail on each creature (the fused hi-vis vest says "construction worker").
- **T4.8 MUST** Humans: perfect hands and arms (no squeezed-in arms, no splayed fingers, palms to thighs).
  Sam's face never readable (silhouette, back, POV). *Why:* rider v2 "arms look broken", MakeHuman Sam.
- **T4.9 MUST** Grounding: feet, hands, hooves, tyres touch the surface. *Test:* side-view probe. *Why:* v1
  "the Crawler looks like it sinks into the ground".
- **T4.10 MUST** Props held in hands sit outside the body: a phone at the ear rests on the OUTSIDE of the ear
  (two-bone IK to a point beside the ear, then push out until every bbox corner is > 12.5 cm from the head
  centre). *Why:* 003 v1 "the phone sank into his head and looked AI".

## T5. Look, light and image quality (the approved 040 recipe)
- **T5.1 MUST** Practical light only: every light has a visible or obvious source (camcorder lamp spot 26-30 W,
  72 deg, blend .5; emergency lamps 45-60 W, one strobing; fluorescent tubes; fire glow through windows;
  headlights; phone screen 2-6 emission). No blue ambient wash (`relight_roof`/`relight_overpass` cut blue
  area lights to 12-15%). No point-light balls in frame.
- **T5.2 MUST** One look across all shots: same engine (Cycles), AgX Medium High Contrast, exposure in the
  -0.9..+1.1 band per set, ink hulls on sets/props/creatures/car, MB .15-.25, DOF f/4-f/6, light grain.
  Never mix a photo plate look, a photoreal product look and the ink-3D look. *Why:* v6 mixed three looks.
- **T5.3 MUST** Light, even film grain only (ffmpeg `noise=alls=3` equivalent at most), no black dots, no
  speckle. Previews >= 20 spp, finals 48-64 spp + OptiX denoiser, encode with mild `hqdn3d=3:3:5:5`. *Why:*
  050 lobby "too much grain, black dots".
- **T5.4 MUST** Textures smooth at phone size: scale fine patterns (marble, paint, noise) x4 larger
  (mapping/noise scales x.25); rain on glass = SPARSE drops (Voronoi distance < .09 masked by noise > .55,
  bump strength .08), never a Voronoi cell pattern over the whole pane.
- **T5.5 MUST** Rain only where it is: outside the glass in interiors, outside an open car door. `rain_here`
  boxes must not contain the camera (rain_anim jitters +-0.6 m: keep >= 1 m margin).
- **T5.6** Fire: slow (keys every ~6 frames, slow random), in several places, with smoke, lighting clouds from
  below. Night skies have fire-lit clouds, stars, ash, rain. Never a glowing oval, never fast jitter. *Why:*
  001 v1 "fire jitters too fast".
- **T5.7** Exposure checks on the subject: a key light at 2600 W on a dark creature blows its skin to cream;
  650 W read right. Faces/eyes not blown; subject region mean luma > .08.
- **T5.8** Dense, real, specific dressing (see SERIES_BIBLE locations): signs, numbers, flyers, smears, claw
  marks, worn treads, cables, puddles. Brand logos painted out.
- **T5.9 MUST** Readable on a phone at arm's length in 0.5 s: subject >= 8% of frame or a clean silhouette
  against a lit background (fog + backlight). Thin pink/red fog walls that flatten a creature: lower volume
  density to <= .0008. *Why:* 140/150 Stalker read "flat red"; fix = fire rim + cold rim + headlight spill.

## T6. Motion
- **T6.1 MUST** Real character animation always; no frozen poses (held beats still breathe).
- **T6.2 MUST** Creatures never mirrored; head leads, chain follow-through, weight shifts, tremor, staggered
  impacts (make-teaser `motion_lib.py`, `stalker_body`). *Why:* "both arms up and down like a machine".
- **T6.3 MUST** Jaws hinge from the rig's jaw bone and open DOWN; vocals locked to the jaw keys.
- **T6.4 MUST** Cars: linear interpolation at speed, constant speed through cuts, wheels spin the right way
  (spin sign, car-aligned pivots, motion_steps 6), body on springs (`suspension()`); never ease to a dead stop
  between shots. *Why:* "wheels spun backwards", "car seems to stop".
- **T6.5 MUST** Drifts are ONE smooth motion: rear steps out, over-rotates, settles, bleeds speed; body rolls;
  no slow-mo, no stop-start. *Why:* v5 "29 s skid must be one smooth Tokyo drift".
- **T6.6 MUST** Headlights on once (constant interpolation keys), stay on. Tubes clunk on one by one and stay
  on. Emission keyed to match the light (a tube mesh may not glow while its light is off).
- **T6.7** Never show Sam walking in third person (v6 walk/stair animation rejected). Use POV with footfalls,
  stand-ups solved with planted heels, hands in frame.
- **T6.8** Animated props are built AT the origin and placed by keys (bx() with rot applies the transform;
  keying a moved mesh double-offsets it). Pivots: set location, `view_layer.update()`, THEN parent.

## T7. Sound (see SOUND_VOICE.md)
- **T7.1 MUST** Only real recordings (CC0/CC-BY, credited) for anything identifiable. No synthetic buzz,
  boings, code-made engines or Karplus guitar. *Why:* v6 "fake synthetic buzz"; "engine sounds like an EV".
- **T7.2 MUST** No score before the planned drop (Ep1: the ignition at 53.5 s); before it only real sound.
- **T7.3 MUST** Music never cuts out between shots; score around the lines (sparse under dialogue, gentle
  duck), never paused for them.
- **T7.4 MUST** Every cue on its picture frame (footstep on the heel strike, roar onset on the jaw drop, rev
  on the body squat, tube clunk on the light key). *Test:* cue table vs frame keys.
- **T7.5** Each shot's sound is built when the shot is built (`snd7/sNNN.py`), so every preview has real
  sound; the final mix rebalances.
- **T7.6 MUST** Master -14 LUFS integrated, true peak <= -1 dBTP (previews -18..-20 LUFS are fine).

## T8. Reuse and continuity
- **T8.1 MUST** Before reusing a shot/asset, read every past note on it. Keep what the director loved
  untouched (the stairwell, the garage reveal, the Screamer scream, the Stalker/reindeer reveal).
- **T8.2 MUST** One car model throughout (c152 used a different livery: excluded).
- **T8.3** Object continuity: what is placed in one shot is in the same place in later shots.

## T9. Rendering
- **T9.1** Probe first: 3-6 key frames at RES .3-.5, SAMP 12-20, ONE contact sheet; fix; then full render.
- **T9.2** Finals on the GPU box (OptiX, denoiser, adaptive .05, bounces 4/2/2/4, persistent data), chunks
  of 30 frames, `use_overwrite=False` + `use_placeholder=True` so restarts resume; share the GPU with other
  jobs (check for a running blender.exe before each chunk, never kill it).
- **T9.3** Cloud CPU only for probes or when the GPU box is unreachable; 16 GB RAM: no more than ~44 rigged
  characters + duplicates + silhouettes (130 rigged went OOM).
- **T9.4** If you must cut corners (STEP=2 + frame blend), say so in the critique; never on fast motion.

## T10. Process
- **T10.1** Logs after every review (WORKING, DECISIONS verbatim, MISTAKES, SHOT_RULES, TOOLS).
- **T10.2** Progress answers = numbers + one still. No chatter between results.
- **T10.3** If the usage limit stops work, resume every paused thread automatically when it refills.
- **T10.4** Send fewer, finished versions; iterate internally.

## T11. Platform / virality
- **T11.1** First frame is a striking image (thumbnail). Hook in the first 2 s by sound + picture.
- **T11.2** First-person dread, found-footage POV and a creature reveal in pieces are the strongest hooks in
  this niche; end on a question (cliffhanger) to drive the next-episode follow.

## T12. Safety and the user's machine
- **T12.1 MUST** Never enter passwords, never accept terms, never buy. The user signs in.
- **T12.2 MUST** Never install software on the user's PC without their explicit OK in words (Pillow for
  Blender's Python needed it). Never change power/driver/display settings.
