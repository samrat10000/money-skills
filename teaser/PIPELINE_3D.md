# PIPELINE_3D: Blender recipe (3d-ink, 3d-real, comic-3D, pixel, sketch)

Proven on Night Terror: Dead Roads (Blender 5.0.1, Cycles, scripts driven by env vars). Working
reference code: `reference/night_terror/teaser_shots.py` (one function per shot, cut901..cut912) and
`reference/night_terror/shots_helpers.py` (camera, shot_cam with real handheld data, kick, linear,
suspension, spin_wheels). Generic helpers: `blender/motion_lib.py`, `blender/vis_check.py`,
`blender/check_motion.py`.

## 1. Project layout
```
teaser/
  brief.md  look.md  timeline.json  beat_sheet.md  TEASER_STATE.md  QA_LOG.md
  refs/  assets/  shots/teaser.py (one function per shot: cutNNN)  out/cNNN/f0001.png
  clips/NNN_name_vN.mp4  edit/ (sound.py, edit.py)  final/
```
- One script builds every shot from code: `CUT=911 RES=1.0 SAMP=32 FR=1,12 DEVICE=GPU OUTROOT=out blender -b -P shots/teaser.py`.
- Env vars: `CUT, RES, SAMP, FR (a,b), DEVICE (GPU/CPU), OUTROOT, NOFOG, LIGHTPATHS, TEXLIM, NOPERSIST`.
- Output `out/c<CUT>/f%04d.png`, `use_overwrite=False`, `use_placeholder=True` (restarts resume).

## 2. Building shots
- Reuse the series kit (city/set builder, materials, car, cast) so every shot matches.
- Camera: `camera(lens)` + `shot_cam(c, [(frame, loc, target, lens, focus)], f0, f1, shake, rshake)`.
  Handheld = real recorded camera-shake data (Camera Shakify CC0 presets, e.g. WALK_TO_THE_STORE),
  not sine noise. Typical: shake .002-.006 m, rshake .05-.22 deg. `kick(c, frames, 2.2)` on impacts.
- Lenses that worked: 18 mm hero (poster), 20 mm tyre cam, 24-28 mm side-follow, 35 mm POV,
  80 mm lightning silhouette, 135-150 mm eye ECU (f/5.6, focus = ray-cast distance).
- Vehicles: keys every ~10 frames for paths, then `linear(car)` (R5.7). Wheel spin from distance
  travelled (`spin_wheels`). Suspension pitch/roll curves added per frame. Spray particles off each
  wheel while sliding.
- Drift recipe (911): keys (frame, x, y, yaw): approach straight, rear steps out, over-rotate ~10-30
  deg past the final yaw, swing back, settle by +15-25 frames; roll curve to 3-4 deg outside then
  -1.8 back and settle; pitch dive on braking. Keep the car moving until the planned stop.
- Animated props: build at the origin and let keys place them. A box whose mesh has its location
  baked in will double-offset when you key `.location` (the slab fell 22 m out of frame). Re-centre
  origin (`data.transform(-loc)`) before keying.
- Parenting: set location, then `view_layer.update()` BEFORE `matrix_parent_inverse`; bind with
  `matrix_world = HM @ matrix_world` (not `= HM`) to keep scale.

## 3. Creatures (see RULEBOOK R4/R5)
- Start from a real model or a lofted sculpt; swap heads/parts into the existing rig by vertex group
  (upper skull -> 'head', lower jaw -> 'jaw') and keep object-name prefixes so animation code still
  finds parts.
- Motion: `motion_lib.chain()` spreads a curve along the bone chain through springs (hz 3-5, zeta
  .4-.55, each segment lagging more); separate plans per side (different start, peak, height, reach);
  staggered slams 5 frames apart; strain tremor (noise 7-9 Hz, 1-3 deg) while raised; drift noise
  (.45 Hz) always; spine breathing with noise-modulated rate; neck counters the rear-up so the face
  stays on target; fingers close one after another (lag 1.2 frames each), splay outward, tap idly,
  clench on the ground; hind legs crouch on their own side's impact.
- Jaw: use the rig's jaw bone for hinge and direction; growl-open hold, then snap wide. Export the jaw
  key frames to `timeline.json` for the sound.
- Eyes: ember-vein orb material (wet dark base, Voronoi distance-to-edge veins warped by noise,
  emission ~1.6-2.5 at render scale, hot core), sunk in the socket; `motion_lib.saccades()`.

## 4. Visibility and lighting
- `vis_check.py`: projects the subject's bbox through the camera; prints frame coverage and depth for
  key frames. Fix before rendering if coverage < 8%.
- Silhouettes: fog ON + an area backlight behind the subject aimed at the lens, kept out of frame.
- Lightning: 2 flashes (frame n and n+3), key light from above-behind, 4-10 frame shot.
- Lamps dying: a wave of emission keys travelling toward the camera.

## 5. Render settings
- Probe: RES .33 (360x640), 12-20 spp, 2-5 frames, CPU or GPU.
- Final: RES 1.0, 32 spp (64 for very dark/volumetric), adaptive sampling, OptiX denoiser on GPU
  (OIDN on CPU), max bounces 3-6, glossy 1-2, transmission 2, volume bounces 0-1, caustics off,
  texture limit 2048, persistent data OFF when chunking.
- Chunk: one Blender process per 12 frames (6-frame chunks were slower: ~80 s fixed setup per chunk).
- Asus RTX 3050 4 GB: ~14-28 s/frame at 1080x1920, 32 spp when VRAM is free (close the browser;
  31 Chrome processes filled VRAM and made it 3-12 min/frame). Cloud CPU: 75-280 s/frame.
- Diagnose slowness: GPU 100% util + full VRAM + low watts (~34 W of ~70) = memory spill. Not thermal.

## 6. Pixel / sketch post (if chosen)
- See STYLES.md. Render colour + normal passes; edges from the normal pass at full res; colour at 1/2.
