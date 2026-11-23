# LOOK: the Night Terror style, as numbers (3D + sketch-ink outlines + practical light + camcorder)

The look is NOT a filter. It is five layers that must all be present. A fresh agent proves it can make
them with the one-still LOOK TEST (section 7) before building any shot. Numbers here are the ones that
passed with the director; never invent new ones (copy them, then tune inside the given bands).

## 1. Ink outlines (the "sketch" in the style)
- Method: **inverted hull**, not Freestyle. `castlib.hull(obj, col, t)` (engine/cast/castlib.py) duplicates
  the mesh, pushes every vertex out along its normal by `t`, flips the faces and gives it the `Ink` material.
  Freestyle was not used: it is slow per frame, flickers on moving cameras and does not export to GLB.
- Ink material: emission near-black `(.004, .003, .006)` mixed with Transparent by **Geometry > Backfacing**
  (Cycles ignores backface culling), `use_backface_culling = True` for Eevee/GLB viewers.
- The hull must not light or shadow anything: `visible_shadow/diffuse/glossy/transmission = False`.
- Thickness `t` (metres) by object scale, the numbers in the approved builds:

  | object | t |
  |---|---|
  | creature body (Stalker, Brute) | .0045 |
  | human body / clothes (survivor) | .0032-.0035 |
  | skull, jaw, antlers, rags | .0022-.003 |
  | ribs, claws, teeth, thin spurs | .0015-.002 |
  | set boxes, door frames, rails (`bx(..., ink=)`, `join_ink`, `rail_run`) | .003-.006 |
  | tiny or flat items (decals, flyers under 5 cm, lettering) | none |
- Cut the hull where it would sit inside a hollow (Husk face: `L.delete_faces` on hull faces inside the cavity).
- Vehicles: crease lines (thin 5-sided tubes on edges > 38 deg) + a hull, see the glb-vehicle-builder skill.
- Test: at phone size (720x1280) the silhouette of every subject and every set edge near the subject shows a
  dark line; no line doubles, wobbles or floats off the surface; no black blobs on thin parts.
- Never blur it away: VHS/softening killed the ink in v6 (MISTAKES.md). Grain and VHS go on AFTER, light.

## 2. Painted materials (the "3D" in the style)
- `engine/cast/mats.py` is the material library. Each is procedural (noise ramps + voronoi + bump), then
  baked by `mats.bake` for GLBs. Shots load the rig `.blend`, which keeps the full procedural detail; the GLB
  is for viewers and blocking only (it renders flatter).
- Creatures: `zombie_skin` (base/dark/light/bruise/vein/rot/blood palette, veins as distorted-noise ridges,
  voronoi cracks, grime, scratches, 6 bump layers, roughness .3-.62, SSS .06). Skin is dark and desaturated,
  wet red only in cracks (RULEBOOK T4.6), never pink, never one flat colour.
- Cloth: `flannel`, `denim`, `canvas`, `leather` with grime and blood. Bone/teeth: `bone`, `teeth_m`.
  Eyes: `eye_m` with low emission (.6); creature ember eyes are emission inside a deep socket, not a dot.
- Sets: `toon_flat` with a fine noise scale (40-60) and a shade only slightly darker than the base, so
  plaster and tile read smooth at phone size (a scale of 5 reads as camouflage blotches). Pattern scales x.25.
- Hex conversion: always `castlib.lin('#hex')` (sRGB to linear) for colours.

## 3. Lighting (only lights that exist in the scene)
- World: black background, no ambient. A thin world Volume Scatter (density .008-.015 indoors; outdoors cap
  .0008 near creatures, see `stalker_cu_light`) so lamps make beams.
- Practicals and their numbers: camcorder lamp SPOT 26-30 W, 72 deg, blend .5, warm `#ffd9a8`, parented to
  the camera; emergency lamp POINT 45-70 W red, one strobing (`strobe`, constant interpolation); fluorescent
  tube = visible emissive fixture + matching AREA light (60-150 W); fire glow AREA through windows/doors with
  `fire_flicker` keys every ~6 frames; headlights SPOT on the car nose; phone screen emission 2.2.
- Creature close-ups: `stalker_cu_light` (warm key + blue rim + under-bounce), red point lights cut to 30%.
- Wet floors (roughness .2-.3) so practicals reflect. Exposure per set inside -0.9..+1.1 so the subject reads.

## 4. Camera and lens (the "real" in the style)
- AgX + **Medium High Contrast** look, `filter_size` 1.2, MB shutter .15-.25 (POV runs .6), DOF f/4 close /
  f/6 wide, focus = ray-cast distance to the subject, lens 18-30 mm handheld, 50 mm lock-offs.
- Every camera is a real object: tripod, handheld camcorder, dash, POV. See CAST_AND_CAMERA.md.

## 5. The one grade (after render, never in the render)
- `scripts/grade.py <frames> <out> [vhs=1] [tear=1]`: luma grain at half resolution, amplitude .022 (.035 on
  VHS shots), stronger in shadows, never dots. Then `preview_encode.sh` (hqdn3d 3:3:5:5, crf 17).
- Camcorder / VHS treatment ONLY on found-footage beats (director loved it on the teaser camcorder shots):
  chroma misregistration 3 px, 4 tracking-wobble bands, head-switch noise on 30% of frames, horizontal half-res
  smear, scanlines x.94, desaturate to .82; tape tear to black over the last 8 frames of a hero shot.
- One grade for the whole episode. No LUT hopping, no photo-plate look next to the ink look (T5.1).

## 6. Realism rules that sit on top (from RULEBOOK.md, the ones that break the look most often)
- Nothing reads as AI: no smooth plastic skin, no symmetric creatures, no stick limbs, no round "potato" heads.
- Contact: feet and hand plants touch the floor on contact frames; the car's tyres squash.
- Detail density in the 3 m around the subject (flyers, claw marks, smears, numbers, worn edges).
- Light grain only; no black dots; previews at SAMP >= 20.

## 7. The LOOK TEST (gate GL: run once per machine / model before the first shot)
```
blender -b -P scripts/look_test.py -- BLEND=<engine>/cast/out/rig/brute/brute.blend OUT=out/look_test RES=.3 SAMP=20
python3 scripts/grade.py out/look_test out/look_test/graded
```
(`python3 scripts/look_test.py BLEND=...` works with the `bpy` module; add `DEVICE=GPU` on the GPU box.)
It builds a dark corridor corner, loads the Brute v2 rig, lights it only with practicals and renders one
still in ~10 s at RES .3. Put it side by side with `reference/look_test_expected.png` and
`reference/ep1_v7_quality_bar.jpg`. PASS only if all are true, logged in QA_LOG.md:
1. Dark frame, lit only by visible sources (tube, red emergency glow, camcorder lamp); the background is black, not grey.
2. Ink line visible on the creature silhouette, spikes, claws and the door frame at phone size.
3. Skin reads painted and wet-cracked, the hi-vis vest and jeans read as fabric, not flat colour.
4. Floor reflects the red lamp; fog shows a soft beam; no blotchy camouflage walls.
5. After grade.py: grain is fine and even; no dots.
If the result is grey and flat, the subject was loaded from the GLB, or the world has ambient light. If it
is black, the camcorder lamp is not parented to the camera or exposure is below -0.9.
