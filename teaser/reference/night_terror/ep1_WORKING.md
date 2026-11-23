# Ep1: what worked (append only)

## Pipeline
- Blender 5 Python (bpy) scripts build every shot from code. Previews and layout run in the cloud (Cycles CPU, RES .3-.5, 8-16 spp). Finals run on Sam's Asus RTX 3050 with Blender 5.0.1 portable `xc\blender501\blender.exe`, OptiX only, adaptive sampling, the OptiX denoiser, reduced bounces and persistent data (about 4 s per frame at 1080x1920).
- Shot scripts: scratch ep1/shots2.py (`CUT=n`, env RES, SAMP, FR, STEP, MB, OUTROOT, DEVICE=GPU), the v7 sets in ep1/v7sets.py, and the penthouse in pent7/pent7.py (env-driven camera, animation and lighting).
- Always set `use_overwrite=False` and `use_placeholder=True`, so a restarted container resumes instead of starting over.
- Low-cost checking loop: render 3-6 key frames at RES .35-.5 and look at one contact sheet. Check positions with a bbox print from a saved .blend instead of guessing, then render the full shot.

## Look (Sam approved it on 040_stairwell: "damn cool, I want this realism everywhere")
- Dark, lit only by practical lights: the camcorder lamp (spot 28 W, 72 degrees, blend .5), flickering or strobing emergency lamps, and fire glow through windows. Exposure 0, AgX Medium High Contrast.
- Real New York detail: hex-tile landings, marble treads (fine thin veins), iron balusters, an oak rail, a brass elevator, flyers, spray graffiti, claw marks and hose cabinets.
- Ink: inverted-hull outlines on rails and frames (`L.hull`). Keep motion blur low (MB .15-.25) and DOF at f/6, so the lines survive.
- POV walking camera driven by footfalls: a heel-strike dip, sway and noise (`pov_stairs`). Keep the shake small and look up and across, not at the treads.
- Penthouse: the real NYC night plate behind the glass (brand signs painted out). Fires are burning blocks whose own windows turn orange with slow flicker, plus rising smoke plumes and a soft halo. The sky has fire-lit drifting clouds and stars in the gaps. Rain and ash are on shader planes outside the glass, with Voronoi drops on the glass.
- Phone: PIL-made screens (alert plus "Akash" incoming, then the connected call), swapped by a keyed mix. The screen goes black at the ear (proximity sensor).
- Character: the stand-up uses an aim-based pose blend, with the root solved every frame so the heels stay planted. The phone goes to the ear with two-bone IK (shoulder to ear, pole out-forward-down). Keep the face away from camera or in silhouette.

## Sound
- Real CC0 recordings from Openverse (`api.openverse.org`, browser User-Agent): footsteps on marble or stairs, stairwell tone, sirens, light buzz, ringtone, phone vibrating on a table, rain on a window, fridge hum, a distant explosion, car alarms and glass rattle. Keep the credits in sfx7/index.json.
- Mixing: ep1/snd7/stair_snd.py and s001.py (env VO, PH for the phone speaker band-pass, FX, ring and vibration aligned to the screen keys). Steps sit on the footfall frames. There is no score before the ignition.
- ElevenLabs lines are in /mnt/project-files/voice/ep1 (silence-trimmed WAVs in ep1/vo).

## Process
- Send each shot as `NNN_short-name.mp4` as soon as it renders, with my own critique, and keep building the next shot while Sam watches.
- When Sam asks for progress, answer with numbers and a still.

## 2026-11-22 7:06 PM IST
- 005_bridge v2 APPROVED by Sam (realistic broken-up call drop, no beeps).
- 006_screamer relit to the v7 look: relight_roof() in v7sets.py kills the blue moon wash, slow-breathing fire from the street + key and rim fire lights, rain glow lowered, lens 85->135 on 006a. Scream = CC0 freesound (joseppujol 221547 + nick121087 333832) slowed .8 with a street echo; mix ep1/snd7/s006.sh.
- 006_screamer_v1 sent (relit). 007_grab_v1 sent: CAMV=g KITCHEN=1 in pent7.py; kitchen dressed (cabinets, fridge, sink, door chain/deadbolt/peephole, coat, mat); camcorder SPOT lamp parented to the camera switches on at f13 (CAMLAMP env). Sound: CC0 miniDV handling, camera click, running wood steps, keys jingle (credits in sfx7/index.json). Script r007.sh.
- 030_corridor_v1 sent: cut30 in v7sets.py (side_door, wall_with_holes, EXIT door on a pivot, stair hint behind it, emergency lights with strobe, PH-C TV). Sound: ep1/snd7/s030.py (marble steps, muffled CC0 sob, TV hiss, buzz, siren, push-bar clunk, stair ambience).

## PAUSED 2026-11-22 11:31 PM IST (Sam: one thread at a time, teaser first)
Resume point for Ep1 v7:
- 050_lobby: cut50 is in scratch ep1/v7sets.py; 4 test stills were rendered (ep1/out/t50).
  - Good: the horde in the fire-lit avenue through the brass storefront.
  - To fix: f16 is too dark (the desk isn't readable). f88 lands on a blank wall, so the swing must hit the B1 PARKING door at x=LW, y=GY+6.6. The tilt-up crowd (frame ~52) is unchecked.
  - Memory: 16 GB. 44 rigged horde + 22 far dups + 260 silhouette blobs fits; 130 rigged ones went OOM.
  - Next: fix it, full render at RES .4 SAMP 10, then the sound (glass slap, crowd moans, rain, desk phone tone) and send it to the coordinator as 050_lobby_v1.mp4.
- Then 060 garage reveal + car (v5 c11 look, re-check Sam's notes), the phone on the seat, ignition at 53.5 with the score, then the chase and ending.
- Previews go via the coordinator (thread attachment cap reached), with a new filename per version.
- Approved so far: 040, 001, 003, 004, 005 v2. Sent and awaiting notes: 002, 006_v1, 007_v1, 030_v1.
- 2026-11-23 ~1:25 AM IST: 050_lobby_v1 sent (cut50; rain only outside, lobby floor raised over the street, desk lamp shade with no shadow). Sound ep1/snd7/s050.py. Fix in the final: denser crowd near the glass, fire texture on the orange building, end framing on B1 PARKING. Next: 060 garage reveal (re-check Sam's v5 c11 notes first).
- 2026-11-23 ~4:40 AM IST: 050_lobby_v2 sent (SAMP 20, sparse glass drops, textures 4x smoother, mild hqdn3d). Next planned shot: 060 garage reveal (re-check Sam's v5 c11 notes first). Low-token mode: rendering only.
- 2026-11-23 ~10:40 AM IST:
  - Sent 060_garage_v1 (cut60: tubes clunk on one by one, headlights off), 080_ignition_v1 (cut80: headlights on once and stay on), and 100_tyre_cam_v1 (cut12).
  - Skipped c152: it uses a different car model, which breaks continuity.
  - Held 070_in_the_car: it needs a cockpit built first (creative work); waiting on Sam's go.
  - Rendering now: cut13 (chase through runners) and cut16 (skid, no slow-mo).

- 2026-11-23: 160_empty_seat built (cut160 in v7sets.py): dashcam view, driver door hidden = open, rain only outside the door (first test had rain inside the cabin in front of the lens: rain_here box must sit outside the car, rain_anim jitters +-.6 m), phone on passenger seat buzzes from f24, screen emission 2.2 (5 blew out). Rendering STEP=2 RES .4 SAMP 20 in cloud. Sound s160.py: rain, idle, two buzzes, Akash voicemail on phone-speaker chain at 3.5 s, click, dead line, no beep.
