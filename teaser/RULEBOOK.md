# RULEBOOK: every rule, with its test

Format: **ID. Rule.** *Test:* how you prove it passes. *Why:* the rejection that created it.
"MUST" rules are hard fails. If a rule conflicts with an explicit instruction from the user in the
current request, the user wins; write the override in `DECISIONS.md`.

---------------------------------------------------------------------------------------------------
## R0. Output format and platform
- **R0.1 MUST** 1080x1920 vertical, 24 fps, H.264 yuv420p, AAC 256k, `+faststart`. Length 15-25 s
  (default target 19-21 s). *Test:* `qa_check.py` header line.
- **R0.2 MUST** No text, titles, logos or captions burned into the video unless the user asks.
  The post caption carries the words. *Why:* "Nothing written on it... just the title I write with the post."
- **R0.3 MUST** A teaser is NEW footage. Do not reuse shots from released episodes unless asked.
- **R0.4** Frame 1 must already be a striking image (it is the thumbnail). No fade up from black longer than 6 frames.
- **R0.5 MUST** Deliver: `<name>_final_IG.mp4` (crf 17), `<name>_final_master.mp4` (crf 12 or lower),
  `<name>_final_phone.mp4` (720x1280, < 15 MB), `CREDITS_sound.txt`, per-shot clips.

## R1. References and research first
- **R1.1 MUST** Never build a character, creature, body, skull, hand or pose without 3+ real
  reference images. Save them to `refs/`. *Test:* `refs/README.md` lists them per asset.
  *Why:* the deer skull "looked like popcorn"; the first Sam body read as a bodybuilder.
- **R1.2** Find 2-3 viral teaser/trailer references for pacing and camera (footsteps before the
  reveal, found-footage camcorder POV, survivor POV). First-person dread is the top-performing hook
  in this niche (15-33 s outliers).
- **R1.3** Compare renders SIDE BY SIDE with the reference before showing anyone. *Test:* a
  `*_vs_refs.jpg` contact sheet exists for each hero asset.
- **R1.4** Confirm which poster / which hero character. *Why:* plan v1 used the wrong poster.

## R2. Structure and pacing (the beat grammar that worked)
- **R2.1** Cold open: near silence plus ONE clean real metal strike (a steel pipe on concrete, a
  bell), ringing into the ambience. Never a spring/boing/cartoon ping. Then the world fades in.
- **R2.2** Reveal the threat in pieces, escalating: sign of it (ripples in a puddle in time with
  footsteps, lamps dying) -> its point of view -> a silhouette in a flash -> a crash zoom to its head
  -> an extreme close-up of its living eye -> the full hero frame. The full creature is seen only at
  the climax.
- **R2.3** Cuts get shorter toward the climax (e.g. 1.5 s -> 0.4 s), then the hero shot runs long
  (5-6 s) so it can breathe.
- **R2.4 MUST** No black gaps except ONE intentional dark beat (0.5-0.8 s) right before the stinger.
  *Test:* `qa_check.py` reports black runs; only the planned one may exist. *Why:* "at the 11th
  second there is a black screen, that is total off."
- **R2.5** End with a found-footage stinger (camcorder clicks on, the creature right at the lens,
  VHS glitch) held ~2 s. *Why:* "hold it 2 seconds longer so it's noticeable."
- **R2.6** Each shot has ONE "wow" detail written in the shot list (water sheeting off a tyre, glass
  raining on the car, the car reflected in the eye).
- **R2.7** If a poster exists, the hero shot lands on the EXACT poster framing (same camera, lens,
  subject scale, car mark). *Test:* overlay hero frame on poster at 50% opacity; key edges line up.

## R3. Camera
- **R3.1** Default grammar: real operator camera, handheld micro-shake, late reframes, eye height or
  physically plausible rigs. Never drone-smooth floaty moves, never slideshow pans/zooms on stills,
  never sweep/slide transitions.
- **R3.2** Use these proven moves (pick 8-12): puddle macro; 20 mm tyre cam on the asphalt; windshield
  POV; bystander camcorder on the kerb (flinch + late pan, VHS); creature POV from height (slow
  breathing sway); low side-follow keeping the car centred; lightning-flash silhouette (4-10 frames);
  crash zoom over an occluder to the face, then pull back; ECU of the eye; hero poster frame with
  impact kicks; car passing the lens to black; camcorder stinger.
- **R3.3** Every shot moves (dolly, track, push, handheld). A locked shot must be a deliberate choice
  with motion inside the frame.
- **R3.4** Camera kicks (decaying rotational jolt, ~2 deg, ~10 frames) on impacts and on the scream.
- **R3.5 MUST** Focus is on the subject. *Test:* probe frame at 100%: the subject's edges are sharp.
  *Why:* the eye close-up v1 rendered as a blurry skull because the camera aimed between the eyes,
  at bone. Ray-cast a clear line of sight to the subject; focus distance = that distance.
- **R3.6** Keep the lens clear: no spray, rain particle, prop or parked car crossing the lens unless
  planned. *Test:* check the last 10 frames of every moving shot.

## R4. Characters and creatures
- **R4.1 MUST** Never hand-build organic creatures from primitives (ovals, tubes, sticks). Start from
  a real artist-made model (CC0/CC-BY) or a proper sculpt/loft, then customise. *Why:* the crow "made
  of ovals", the Stalker "looks like sticks".
- **R4.2 MUST** Limbs read as anatomy: shoulder mass, elbows, bony wrists, hands with fingers and
  talons/claws, digitigrade or hooved legs where fitting. Hunched shoulders, shoulder blades pushing
  through skin. *Test:* turnaround sheet (front, side, back, 3/4, hand close-up) vs references.
- **R4.3 MUST** Horror bone is SHARP: bone ends taper to spurs and hooks; no round caps, no
  "popcorn" lumps, no symmetrical blobs. Skulls are angular with hard brow ridges and flat plates.
- **R4.4 MUST** Teeth: crooked blades of mixed sizes, broken stumps, roots showing through eroded
  bone. Never neat square molars or uniform cone teeth. Mouth interior: dark, rough, wrinkled,
  recessed rotting flesh. Never a glossy/chrome/lilac tongue or a hollow black hole.
- **R4.5 MUST** Eyes: never a flat emissive dot, never snake slits. A wet dark orb sunk deep in the
  socket with glowing cracked veins and a hot core (ember-vein eye), a specular highlight, and eye
  saccades (see R5.6).
- **R4.6** No fake-looking decorations (red plastic-looking spikes, cow-print patches). Use bone
  ridges, chipped vertebrae, scars.
- **R4.7 MUST** Humans: perfect anatomy (hands, fingers, elbows, arm length). Relaxed hands hang palm
  toward the thigh. Arms never squeezed inward. If a human face cannot match reality, keep it out of
  frame, in silhouette or behind the camera (POV). No AI video/image people.
- **R4.8 MUST** Everything is grounded: feet/hands/tyres touch the surface (no hovering, no sinking).
  *Test:* side-view probe frame; contact points within 1 cm. *Why:* "the Crawler looked under the ground".
- **R4.9** Tyres read as RUBBER (matte, squashed, sidewall bulge), never metal.
- **R4.10** Scale sells it: giants are framed against known-size objects (cars, lamps, windows).

## R5. Motion
- **R5.1 MUST** Living creatures are never mirrored. Left and right limbs have different timing,
  height and amplitude. *Test:* plot (or print) the two limbs' rotation curves; correlation < 0.8.
  *Why:* "moving its hands up and down at the same time like a machine".
- **R5.2 MUST** Motion travels through the WHOLE chain (shoulder -> upper arm -> forearm -> wrist ->
  fingers), each segment lagging more (spring follow-through, overshoot, settle). Never rotate only
  the end bone. Use `blender/motion_lib.py`.
- **R5.3** The head leads, the body follows. Weight shifts between supports. Raised limbs tremble
  under strain. Impacts are staggered (L then R a few frames apart) and the legs absorb them.
- **R5.4** Nothing is ever perfectly still: low-frequency noise drift on every limb, breathing with a
  noise-modulated rate (not a sine metronome).
- **R5.5 MUST** Jaws hinge from the jaw bone at the back of the skull and open DOWNWARD. Never infer
  hinge or snout direction from geometry guesses. *Test:* print the jaw tip position at closed vs
  open; it must move down and slightly back. *Why:* the jaw opened backward on the long bull skull.
- **R5.6** Eyes do saccades: hold a fixation, snap to the next in ~2 frames with a small overshoot,
  micro-tremor while holding, then lock onto the target. *Why:* "eyes moving, that's crazy".
- **R5.7 MUST** Vehicles in driving shots use LINEAR interpolation and constant speed. Never let two
  Bezier keys ease a car to a halt. Speed and direction MATCH across cuts. *Test:*
  `blender/check_motion.py` prints speed per frame; the first and last 5 frames of adjoining shots
  are within 15%. *Why:* "the car seems to stop, then the side shot starts at full speed."
- **R5.8** Skids and drifts: the rear steps out and over-rotates (~20-30 deg past target), swings
  back and settles over 15-25 frames, the slide bleeds speed (no dead stop), the body rolls to the
  outside, dives, then rocks on its springs. Wheels spin and throw spray. *Why:* "make the skid more
  realistic"; "car never stops dead".
- **R5.9** No car light flicker or toggling unless the story says so. Headlights on once and stay on.
- **R5.10** Slow motion only where earned (one moment max), rendered as real high-fps slow-mo (render
  more frames, never frame-blend a 24 fps shot), never repeated, never as filler.
- **R5.11** Real character animation always; no frozen poses (except an intentional held beat with
  breathing/noise on it).

## R6. Look and image quality
- **R6.1 MUST** One look across all shots: same grade, lens, grain, line treatment, render engine,
  samples class. Never mix a photo plate look, a photoreal look and an ink-3D look. *Why:* Ep1 v6.
- **R6.2** The poster is the quality bar: every shot must be "wallpaper-worthy".
- **R6.3 MUST** Every shot is READABLE on a phone at arm's length: the subject covers >= 8% of the
  frame (or is a clear silhouette against a lit background), and the subject region is not crushed
  black. *Test:* `blender/vis_check.py` coverage + mean luma of the subject's bbox region > 0.08.
  *Why:* the giant (4% of frame), the Brute behind a roof edge and the falling slab "barely showed".
- **R6.4** Silhouettes need light behind them: fog/haze plus a backlight aimed at the lens, kept out
  of frame.
- **R6.5** Rain must look real: visible streaks with motion blur, splash crowns on the ground, wet
  reflective asphalt with noise-driven roughness, sparse drops on glass (never a Voronoi dot pattern
  over the whole pane), rain only outside in interiors.
- **R6.6 MUST** Grain is LIGHT: luma noise ~2% amplitude (ffmpeg `noise=alls=3` equivalent), no
  black dots, no speckle. VHS treatment only on camcorder/found-footage shots. *Why:* "too much
  grain, black dots".
- **R6.7** Textures are smooth at phone scale: scale fine patterns up (x4) so they do not shimmer or
  read as dots. Previews at >= 20 spp, finals 32-64 spp + denoiser.
- **R6.8** Fire moves slowly and burns in several places with smoke; never fast jitter in one spot.
  Night skies are never pitch black: fire-lit clouds, stars, ash, rain.
- **R6.9** No AI look: no glossy, symmetric, over-graded, morphing or warping imagery. Add real-camera
  imperfections (micro-shake, sensor noise, slight focus breathing, halation, lens smudge, chroma edge).
- **R6.10** No dither/halftone dot patterns unless the user explicitly asks for that style.

## R7. Sound (see SOUND.md for the recipe)
- **R7.1 MUST (teaser default)** No background music bed. Real recorded sounds only. If the user asks
  for music: real recorded instruments, continuous through the whole teaser with no cut-outs between
  shots, never AI-generated music. *Why:* "the music is cutting in between"; "no background music,
  just those sounds".
- **R7.2 MUST** Only real recordings (CC0 / CC-BY, credited). No code-synthesised SFX for anything
  the audience can identify (tyres, engines, rain, creatures). *Why:* "tyre hiss... not like code
  sounds, those earlier were cheap"; "the engine sounded like an EV".
- **R7.3 MUST** Creature vocals are locked to the jaw keys: a growl starts on the frame the jaw drops
  and covers the whole open-mouth hold; the scream's ATTACK (onset, not file start) lands on the jaw
  snap. *Why:* "the monster opened his mouth and the roar comes a lot later".
- **R7.4 MUST** Never pitch breaths down (reads as a human moan). Keep growls short (a long low growl
  masks other cues and reads as an idling engine).
- **R7.5** Car: double "vroom" rev on the reveal, a gear-change bark on a cut, a three-layer drift
  screech that dies when the next big cue starts, a real wet-road tyre hiss bed under driving shots,
  passby peak exactly where the car fills the lens.
- **R7.6** Thunder crack lands on the flash frame; glass tails end at the cut (a glass tail under
  thunder reads as a crash); a sub-drop and reverse swell lead into the hero cut; booms/hits on big cuts.
- **R7.7 MUST** Master at -14 LUFS integrated, true peak <= -1.0 dBTP, with a lookahead limiter.
- **R7.8 MUST** Never claim how audio sounds without measuring/listening (earshot or equivalent, plus
  spectrogram/onset checks). *Test:* G5 readings logged.
- **R7.9** Dialogue (if any): one line at a time with a breath after it; music/ambience thins under
  each line; never overlap lines. Phone call drops break the caller's words, never beeps.

## R8. Process, files and delivery
- **R8.1 MUST** Number every shot and name files `NNN_short_name_vN.ext` (e.g. `910_eye_closeup_v3.mp4`).
  New version = new filename; never overwrite a version the user has seen.
- **R8.2** Per-shot review clips plus key PNG frames, each with your honest critique, before or with
  the full cut. The full cut is built only from QA-passed shots.
- **R8.3 MUST** Every file > 20 MB also gets a direct download link (GitHub raw + blob page), because
  phone previews of big attachments have no download button.
- **R8.4** Logs: append to `WORKING.md`, `DECISIONS.md`, `MISTAKES.md`, `TOOLS.md` after every review.
- **R8.5** Before reusing any old shot or asset, re-read the user's past notes on it.
- **R8.6** Progress reports use numbers (frames done / total, s per frame, ETA in the user's time zone)
  and a text bar, only when asked or at a real milestone. No chatter.
- **R8.7** Send fewer, finished versions. The first version the user sees must already pass every
  gate. Iterate internally, not on the user's time.

## R9. Rendering and compute (see ENVIRONMENT.md)
- **R9.1** Render finals on the user's GPU machine when it is online; the cloud is the fallback,
  never a reason to stop.
- **R9.2** Chunk renders (12-frame Blender processes), skip-existing, delete 0-byte placeholders on
  restart, detached batch, done-marker file. Watch VRAM: if the GPU sits at full memory and low power
  draw, memory is spilling; close the browser, simplify textures/geometry.
- **R9.3** Probe before every full render (2-5 frames at 360x640, 12-20 spp, one contact sheet).
