# PIPELINE: the engine and how a shot is made

Everything is Blender 5.x Python (bpy), built from code. No hand-made .blend scenes except the character rigs
and the car GLB. That is what makes shots reproducible by any agent and fixable by editing numbers.

## Layout (engine/ + the asset pack unzipped into it, see ASSETS.md)
```
engine/
  ep1/shots2.py      # entry point: CUT=<n> picks cut<n>(); render() reads env; execs v7sets.py first
  ep1/v7sets.py      # all v7 sets and shots (cut30/40/41/50/60/70/80/125/130-160, cut6 override) + PIL textures
  ep1/city.py (K)    # materials (asphalt, concrete, facade, carpaint, glass), street kit, sky, rain, char() loader, car
  ep1/anim.py (A)    # creature/zombie motion: shamble, sprint, crawl, scream, idle, stomp
  ep1/shakify_data.py# real handheld camera shake tables (real_shake)
  ep1/tex/           # PIL-made decals: hex tile, smear, claw, flyers, door numbers, exit/B1 signs
  ep1/snd7/          # per-shot sound mixers sNNN.py + calldrop.py
  ep1/car/nt.glb     # the Night Terror (asset pack)
  ep1/vo/            # dialogue WAVs, silence-trimmed (asset pack)
  cast/              # character builders (MakeHuman CC0 base -> sculpt -> garments -> rig) + out/rig/<n>/<n>.blend
  pent7/             # penthouse (Act 1): pent7.py env-driven + runs.sh with the exact approved settings
  mh/                # MakeHuman CC0 base mesh, skeleton, weights, targets
  sfx7/, music/sfx/  # real CC0/CC-BY sound library + index.json credits (asset pack)
```
`city.py` puts `engine/cast` on sys.path; `shots2.py` puts `engine/ep1` on it. Paths are all relative.

## Running a shot
```
cd engine/ep1
# cloud / CPU probe (Linux, pip bpy or blender -b):
FR=40,40 MB=.25 OUTROOT=$PWD/out/t125 CUT=125 RES=.3 SAMP=12 THREADS=4 python3 -u shots2.py
# full preview in the cloud:
MB=.25 OUTROOT=$PWD/out/v7b CUT=125 RES=.4 SAMP=20 THREADS=4 python3 -u shots2.py
# final on the GPU box (Windows PowerShell; see scripts/run_cut_asus.ps1 for chunking):
$env:CUT='125'; $env:RES='1'; $env:SAMP='48'; $env:MB='.25'; $env:DEVICE='GPU'; $env:OUTROOT='C:\...\out'; $env:FR='1,30'
& C:\Users\cross\Downloads\xc\blender501\blender.exe -b --python shots2.py
```
Env: `CUT` (shot function), `RES` (1.0 = 1080x1920), `SAMP`, `FR=a,b` (frame range), `STEP` (every Nth frame),
`MB` (motion-blur shutter, .15-.25), `SLOW` (true slow-mo by time remap), `THREADS`, `DEVICE=GPU` (OptiX +
OptiX denoiser), `OUTROOT` (frames -> `OUTROOT/c<CUT>/f####.png`), `BLEND=1` (save the scene for debugging).
Frames skip-if-exist (`use_overwrite=False`, `use_placeholder=True`): rerunning resumes; delete 0-byte files
after a crash. `v7sets.py` needs Pillow inside Blender's Python (`<blender>/5.0/python/bin/python.exe -m pip
install pillow`, only with the user's OK on their PC).

## Writing a new shot (the pattern every v7 shot uses)
```python
def cut125():                                   # 125_brute_block: one line saying what the shot is
    nf = 120; rng, car, parts, br = brute_set(nf)   # 1) a set function builds the world (reuse or write one)
    for l_ in bpy.data.lights:                       # 2) relight to PRACTICAL light only
        if l_.type == 'AREA' and l_.color[2] > l_.color[0]: l_.energy *= .3
    br.location = V((-.1, -10.0, 0)); rg = K.char_rig(br)   # 3) cast, placed and animated with anim.py
    A.stomp(rg, br, 1, 26, speed=.8); A.scream(rg, 27, nf, f_scream=34, amp=.9)
    for f, p, r in path: key(car, f, loc=V(p), rot=(0, 0, math.radians(4 + r)))   # 4) vehicles: keys
    spin_wheels(parts, 60, nf, 23); suspension(car, 1, nf, amp=.004, pitch=[...])  #    wheels + springs
    c = camera(24)                                   # 5) camera: shot_cam keys + real shake + kicks
    shot_cam(c, [(f, loc, target, lens, focus), ...], 1, nf, shake=.018, rshake=.35, seed=125)
    kick(c, [34, 36, 60], 1.8); c.data.dof.aperture_fstop = 4.0
    sc.view_settings.exposure = .4                   # 6) exposure in the approved band
    return 1, nf
```
Key helpers (shots2.py): `key, linear, aim, camera, shot_cam(keys: (frame, loc, target, lens, focus)),
real_shake, kick, pov_cam (step-synced POV), phone_light (camcorder lamp parented to camera), nt_car,
spin_wheels, suspension, rain_here(center, size, count, f0, f1), lamp_spot, area, flicker, lightning,
steam, debris, dress, base_street, horde_set, garage_set, chase_set, brute_set, overpass_set,
stalker_alive, freeze_world, warp_shot (one-take bullet time)`. v7sets.py: `bx (box), slope_box, join_ink
(ink hulls), baluster, rail_run, light, strobe, fire_flicker, stairhall, door, side_door, elevator, window,
wall_decal, pov_stairs, relight_roof, relight_overpass, stalker_cu_light, m_marble/m_paint/m_iron/m_wood/
m_brass/m_tile/m_img/m_static/m_glass_rain`. city.py: `asphalt, concrete, facade, emit, metal, carpaint,
glass_dark, box, building, lamp, sedan, street, sky, rain, char, char_rig, setup_render`.

Gotchas (each one cost a re-render):
- `bx()` with a rotation applies the transform; build animated props at the origin and key them into place.
- Pivots: set the empty's location, `bpy.context.view_layer.update()`, then parent with the inverse.
- Area lights face -Z; check the rotation sign. A "void" box behind a door hides the room behind; build it.
- Keyable emission needs a Principled material (`Emission Strength` socket), not the flat emit helper.
- `rain_here` + `rain_anim` jitter +-0.6 m: keep the box >= 1 m from the camera and inside the right space.
- Use the car's real cabin (nt.glb has seats, dash): driver x +.4, passenger x -.4, dash y -.85 (local).
- Big crowds: 44 rigged + 22 duplicates + 260 joined silhouette blobs fits 16 GB; 130 rigged OOMs.
- A creature under a hard spot: start the key at ~650 W, not 2600 W (dark skin blows to cream).
- The car pulling through a light placed at its nose gives a white flare: key that light off before it moves.

## Probe -> look -> fix -> render
1. Probe 3-6 key frames: `FR=n,n` per frame, RES .3, SAMP 12 (~1 min/frame on 4 CPUs). Make ONE contact sheet
   (`scripts/contact_sheet.py`) and look at it full size and at 360 px.
2. Checklist + Director's eye (QA.md). Fix the cause in code. Re-probe only the frames that failed.
3. Full render: ALWAYS the GPU box at RES 1 (T0.7: no shot that can reach a cut is ever rendered below 1080). Ep1 v8
   numbers on the RTX 3050 4 GB: SAMP 32, PERSIST=0, VSTEP=10, MB .2 -> 26-50 s/frame for most sets, 125-140 s/frame
   for the Brute street and the overpass. PERSIST=1 overflowed the 4 GB VRAM (9+ min/frame). Cloud = probes only.
4. Sound: `python3 snd7/sNNN.py` (pattern below) -> `NNN_snd.wav`.
5. Encode the preview (`scripts/preview_encode.sh`):
   `ffmpeg -framerate 24 -i f%04d.png -i NNN_snd.wav -vf "hqdn3d=3:3:5:5,scale=720:1280:flags=lanczos,format=yuv420p"
   -c:v libx264 -crf 17 -c:a aac -b:a 192k -shortest NNN_name_vN.mp4`. If STEP=2 was used:
   `-framerate 12 ... -vf "minterpolate=fps=24:mi_mode=blend,..."` and say so in the critique.
6. One contact sheet of the final clip (4 frames), look, send with the critique.

## Sound mixer pattern (snd7/s125.py, s160.py)
numpy buses at 48 kHz: `ld(file, ss, t)` decodes with ffmpeg; `put(bus, audio, time, gain, fade)` places by
TIME = frame / 24; filter chains per bus in one ffmpeg `filter_complex` (phone band for voices, lowpass for
idle, echo for big spaces); `alimiter` + `loudnorm I=-18..-20` for previews. Cue times come from the shot's
keys (jaw open frame, footfall frames, light-on frames, rev frame). `calldrop.py src dst chop_start cut_time`
for a dropped call.

## Character pipeline (engine/cast)
MakeHuman CC0 base (`mh.py`, `zbuild.Char(name, targets)`), subdivide, per-vertex displacement sculpt in numpy
(noise strands, grooves, swelling, skull shaping), cut lips/nose/sockets, add teeth/claws/spurs as tapered
tubes, garments cut from the body by bone weights (`z.garment`), procedural Cycles materials (mats.NB node
builder), pose, ink hull (`L.hull`). `KEEP_RIG=1 OUT=out/rig/<n>` keeps the skeleton -> what shots load.
Turnaround: `ONLY=front34,side,face RES=.5 SAMP=24 python3 <builder>.py`. Reference: `brute2.py` (Brute v2,
approved), `stalker.py` + `bullskull.py/swap_bullskull.py` (Stalker head; the final v5 rig is in the asset pack).


## Windows / Asus gotchas (each cost time in the 2026-11-25 session)
- `python3` on Windows is the Microsoft Store stub: call `python`. `/tmp` in Git Bash is not where Python writes; use
  `os.environ['TMP']`. Cloud shell scripts (`master.sh`, `r007v8.sh`) do not run as-is: use `scripts/master.py` and a
  `.ps1` port (`pent7.py` runs fine under `blender.exe -b --python pent7.py` with the same env vars, DEVICE=GPU PERSIST=0).
- This ffmpeg build has NO `-pattern_type glob`: make contact sheets with PIL (`scripts/contact_sheet.py`) or `%04d`.
- Patching Windows paths with Python string replacements in a heredoc: `\0..` becomes an octal escape and eats the path,
  `\U` breaks the string. Use the Edit tool, a .py file with raw strings, or `chr(92)`; then grep the result.
- Give Python/PIL Windows paths (`C:\...`), not Git Bash `/c/...` paths.
- Queue: `scripts/queue_template.ps1` (expected frames per cut, skips done mp4s, resumes frames, PARTIAL guard), started
  DETACHED: `Start-Process powershell -ArgumentList '-ExecutionPolicy Bypass -Command "& <queue.ps1> *>> <log>"' -WindowStyle Hidden`.
- A second job (e.g. one pent7 shot) waits in its own detached script with `while (tasklist | findstr /i blender.exe)`;
  it slips in between the main queue's cuts.

## Sound tools (scripts/)
- `master.py in.wav out.wav [start_gain_dB]`: gain into `alimiter` (ceiling .68: true peak runs ~1.5 dB over the sample
  ceiling), iterates to -14 LUFS / <= -1 dBTP, 24-bit out. Start at the last run's gain to converge in 1-2 passes.
- `scan.py mix.wav`: per shot RMS / quietest half second from `v8_timeline.json` (dead air, sagging action, T14.5).
- `STEMS=1 python mix_v8.py` prints each scene's measured bed level and applied gain: read it before changing levels.
- The mixer writes `v8_timeline.json`; scan and the assembler follow it. A shot's length lives in ONE place (SHOTS).

## Edit (scripts/assemble.py)
Per shot: native frames when ALL exist, else a labelled STAND-IN, else black MISSING; the one grade (grain everywhere;
VHS + REC/timecode/battery OSD drawn with PIL shapes, never font glyphs, only on the hidden-watcher shots; tape tear on the
last); each shot encoded at its exact frame count (short sources hold the last frame), concat, mux the master WAV, IG
(crf 17), master (crf 12), phone (720x1280, < 15 MB), `SOURCES.md`. Re-run after every finished cut; unchanged shots skip.
- VRAM creep on the 4 GB card: after ~60-90 frames in one Blender process, VRAM reaches ~3.8 GB and frames go from
  ~100 s to ~260 s. Check `nvidia-smi` when a cut slows; stop the queue + blender.exe, delete the 0-byte PNG, restart the
  queue: the cut resumes at the same frame with fresh VRAM (~2.2 GB). Shot-by-shot clips: `edit8\deliver_shot.py <shot>`.
