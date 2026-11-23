# CAST_AND_CAMERA: every character, how it moves, every camera, how it is coded

One-page index. Looks and rules live in `SERIES_BIBLE.md`; this file maps each one to its builder, its
animation call and its camera call so a shot can be planned without searching the engine.

## Characters

| who | builder (engine/cast/) | rig / file | movement (engine/ep1/anim.py) | approved / notes |
|---|---|---|---|---|
| Sam (hero) | MakeHuman base (`mh.py`, `zbuild.py`) | `cast/sam/sam.blend` (pent7) | posed + keyed in `pent7.py`; in sets: hands, back, silhouette | Face NEVER shown (v1-v5 rejected). Hands palm to thigh, never splayed. Hoodie, red glasses, long wavy hair. |
| Akash | none (voice only in Ep1) | VO through the phone band | n/a | Phone + voicemail only (`s160.py`). |
| Friends f1-f3, the rider | `survivor.py` | `out/rig/<name>` | `idle`, `sprint` | Looks not set by the director yet; rider v3.2 for Ep2. |
| Walker | `walker2.py` | `out/rig/walker` | `shamble(limp, arms='dangle', drag)` | Wet moans. |
| Runner | `runner.py` | `out/rig/runner` | `sprint(period=.62)` | Breath + feet. |
| Crawler | `crawler.py` | `out/rig/crawler` | `crawl(period=1.6)`, hand plant every .8 s | Must be GROUNDED (v1 "under the ground"). Sparse real claw taps. |
| Screamer | `screamer.py` | `out/rig/screamer` | `scream(f_scream)` toward the sky | One slow-mo allowed. |
| Husk | `husk.py` | `out/rig/husk` | `shamble` slow / stalk | Must match the director's first white-background reference. |
| Brute v2 | `brute2.py` (+ `anatomy.py`, `skull.py`) | `out/rig/brute/brute.blend`, `glb/brute-v2.glb` | `stomp(period=1.7)` then `scream(f_scream=34)`, jaw opens | APPROVED ("coolll"); wedge skull fix applied. 125_brute_block. |
| Stalker v5 (hero monster) | `stalker.py` + `bullskull.py` / `swap_bullskull.py` | `out/rig/stalker/stalker.blend` (GLB export open bug: "body hull not enabled for rendering", toggle `hide_render` off before baking) | `idle` + head-led saccades, `scream`; asymmetric, follow-through, staggered impacts | Real bull skull, ember-vein eyes, stitched mouth that tears (tear still TODO). |
| The car "Night Terror" | asset `car/nt.glb` | `nt_car(loc, rot_z)` in shots2.py | `spin_wheels(parts,f0,f1,dist)`, `suspension(car,f0,f1,pitch=...)` | Rubber tyres, V8 sound, front is -Y, driver seat x +.4. |
| Bandit buggy, IVORY trike | `glb-vehicle-builder` skill | separate GLBs | same car helpers | Ep2 / side reels. |

Movement rules (from rejections): no frozen poses; every creature asymmetric (never mirrored), head leads,
weight shifts, feet planted on the ground every contact frame; check feet vs floor on the contact sheet.

## Camera grammar (the camera is a real object in the story)

| mode | code (engine/ep1/shots2.py unless noted) | numbers that passed | Ep1 shots |
|---|---|---|---|
| Tripod camcorder | `pent7.py` `CAMV=t` (also `a` over-shoulder, `p` phone insert, `g` grab, `s`, `b`) | static, 1-2 mm drift, VHS/miniDV look | 001, 004 |
| Rip off the tripod -> handheld | `CAMV=g` | swing + settle, camcorder lamp on at f13 | 007 |
| First-person POV run | `pov_cam(c, pts, f0, f1, eye=1.62, bob=.035, step_hz=2.6, jolt=[...])` | f/2, shutter .6, focus .8 x target dist | 030 |
| POV stairs (THE LOOK BAR) | `pov_stairs(c, foot, looks, f0, f1)` (v7sets.py) | 18 cm dip per tread, lamp 28 W 72 deg | 040 APPROVED |
| Handheld documentary (default for ground coverage) | `shot_cam(c, keys, f0, f1, shake, rshake)` + `real_shake` (`SHAKE=WALK_TO_THE_STORE`) | eye height 1.5-1.7 m, shake .018, rshake .35, aim lags 3-5 f, late reframes | 125 (low x -2.9), most exteriors |
| Impact kick | `kick(c, frames, amp=1.5)` (2.4 in POV) | decays over 10 frames | 125 roar, 040 vault |
| Dashcam (camcorder propped on the dash) | cut70 / cut160 in v7sets.py | lens 18, sensor 30 vertical, settle wobble, idle vibration | 070, 160 |
| Freeze-and-orbit one-take | `warp_shot(base, w0, w1, n_freeze, n_resume, pivot_local, sweep_deg, ...)` | one continuous move | 090_gate_burst (TODO) |
| Keyed path / crane / aerial | `cam_path(o, frames, locs, targets, lenses, focus)` | real scale, drone only for reveals | 095_aerial (TODO) |
| Creature close-up light | `stalker_cu_light()` (v7sets.py) | warm key + blue rim + under-bounce, fog density <= .0008 | 140, 150 |

Moves the director called "crazy" in Ep2 (reuse in every episode; code lives in the dead-roads-ep2 repo,
rebuild them with `shot_cam` keys):
1. **Low side-follow**: 22 mm, 1.6 m high, drifts with the vehicle, aim swings to keep the flying body centred, shutter .25.
2. **Lock-off THUD**: static 50 mm over the shoulder; the vehicle rocks twice, puddle ripples, nothing shown yet.
3. **Crash zoom over the roof**: start 32 mm on the shoulder, arc UP and over the roof to ~2.5 m from the
   creature's face while zooming 32 -> 58 mm, hold on eyes/jaw, race back up and over. Stay above roof height until the push.
4. **Tyre cam**: 20 mm at 0.3 m beside the front tyre, the vehicle stops a hand's width away, crane up as the antlers rise. f/4, focus 3.4 m.

Grammar: centre framing, one continuous move per beat, a lens change inside the move, a low road camera,
subject centre-frame through fast action. Handheld documentary shake recipe: 0.4-1.5 Hz sway of 2-4 cm,
6-9 Hz micro-jitter ~3 mm, roll 0.5-1 deg.
