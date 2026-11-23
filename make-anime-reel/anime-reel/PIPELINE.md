# PIPELINE: build and render a shot

Proven on 5 O'CLOCK Ep1 shots 01-04. Reference code:
- `scripts/build_ref_shot.py`: shot 01 v4b, the crow on a loudspeaker, the locked quality bar
- `scripts/toonlib_v4.py`
- `scripts/paint_bg.py`
- `scripts/comp_ref.py`
Copy them per shot into `<project>/<NN_name>/src/` and change only what the shot needs.

## Layers per shot
1. **Cel layer:** Blender EEVEE, transparent film. Characters, creatures, props, sets that move or need 3D (RULEBOOK R2).
   - It writes `cel_NNN.png` and `meta.json` (sun screen position, horizon, landmark positions per frame for the painter and comp).
   - Optional extra passes: `refl_NNN.png` for a delayed or mirrored reflection camera (a shop window), or glass UV emission for mirror inserts.
2. **Painted BG:** numpy painter at 110% size from `meta.json` (RULEBOOK R3).
3. **Composite:** parallax push, light wrap, bloom, veiling glare, dust motes, grade, vignette, grain (RULEBOOK R7).
4. **Encode:** `ffmpeg -y -framerate 24 -i fullc/%03d.png -c:v libx264 -crf 14 -preset slow -pix_fmt yuv420p NN_name_vN.mp4`

## Exact commands (Windows, Blender 5.0.1 portable)
```
# 1. cel layer: args go AFTER --, and the outdir MUST be absolute (a relative one wrote into C:\test\)
C:\path\blender501\blender.exe -b --python build_sNN.py -- C:\abs\path\full 1.0 all          # or 1,24,48 for probes, 0.5 for 50%
# 2. background (sun position from SUN_SCREEN or meta.json)
python paint_bg.py bg.png <sun_x> <sun_y>        # or: python paint_bgNN.py full\meta.json
# 3. composite
python comp_sNN.py full bg.png fullc            # shot-specific signature, see the script docstring
# 4. encode (line above)
```
`scripts/run_shot.ps1` runs all four at **BelowNormal priority** (other renders on the PC have priority) and times each step.
The build scripts need this line after `import sys`, so they work under blender.exe and under the bpy pip module:
`argv = sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else sys.argv[1:]; sys.argv = [sys.argv[0]] + argv`

## Order of work per shot
1. Layout: camera, set, key poses. Probe 4-6 frames at 40-50%. Contact sheet and crops (QA loop).
2. Animation: clips blended on twos, contact locks, follow-through. Probe every in-between of the big moves.
3. Light: sun position, rim side, values (measure the BW values with a debug render before setting ramp thresholds).
4. Detail pass (RULEBOOK R8): roads, roofs, clothes, signage, depth cues.
5. Full render, comp, encode. Final QA. Keep old outputs: rename `full/` and `fullc/` to `full_vN/` and `fullc_vN/` before re-rendering.

## Speed (measured)
| Machine | Cel frame (1080x1920) | Comp frame | 72-96 frame shot |
|---|---|---|---|
| RTX 3050 laptop, EEVEE | 0.6-1.5 s | 3-4 s | 5-9 min total |
| Cloud CPU (4 cores, bpy) | about 10-25 s | about 3-5 s | 20-40 min |
Probe at low resolution, and render full only after the probes pass. Run only one GPU render at a time.

## Proven tricks
- **Glint/eye bead:** compute it each frame from the head and beak bones, on the camera-facing eye, nudged toward the lens. Never use a bone-parent offset.
- **IK elbow/knee:** solve the pole by searching candidates and measuring the joint position. Keep elbows low in reaches.
- **Feet on surfaces:** after posing, measure the lowest toe tail in world space, then offset the root.
- **Late reflection:** a second camera mirrored across the window plane renders `refl_NNN.png` with a frame delay, and the comp puts it into the glass holdout.
- **Japanese text** (signs, road paint): fonts `C:/Windows/Fonts/YuGothM.ttc`, or `msgothic.ttc` as fallback.
- **Veiling glare:** when the sun is hidden behind a building, add a broad soft glow around the sun position in the comp.
