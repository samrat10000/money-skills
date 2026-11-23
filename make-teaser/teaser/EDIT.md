# EDIT: grade, treatment, assembly, encode

Working reference: `reference/night_terror/edit_assemble.py`. Generic version: `scripts/edit_assemble.py`
(reads `timeline.json`).

## 1. timeline.json (the one clock)
```json
{"fps": 24, "w": 1080, "h": 1920,
 "seq": [["901_puddle_macro", 24], ["902_tyre_cam", 36], ["903_windshield_pov", 41], ...,
         ["911_poster_finale", 139], ["black", 18], ["912_vhs_stinger", 52], ["black", 8]],
 "vhs": ["904_camcorder", "912_vhs_stinger"],
 "events": {"jaw_drop": 289, "jaw_snap": 309, "slam_L": 334, "slam_R": 339, "passby": 391, "flash": 180}}
```
Event frames are global (start of shot + local frame). Shot code writes them; sound reads them.

## 2. Per-frame treatment (order matters)
1. Resize to 1080x1920 (Lanczos).
2. Lens look (the series' `look.lens` if present): halation on highlights, subtle anamorphic streak on
   point lights, vignette, split tone, chroma fringe at edges.
3. Grain: Gaussian luma noise at half resolution, upscaled bilinear, amplitude .022 (normal shots),
   .035 (VHS shots), weighted toward shadows. Never more (R6.6).
4. VHS (found-footage shots only): chroma misregistration 3 px, 4 tracking-wobble bands, head-switch
   noise at the bottom (30% of frames), horizontal half-res smear, faint scanlines (x.94), desaturate .82.
5. Tape tear to black over the last 8 frames of the hero shot (VHS ramp 1 -> 5, fade .9).
6. Encode: ffmpeg rawvideo pipe -> libx264 `-preset slow -crf 16` (review), crf 12 (master), crf 17 (IG),
   720x1280 crf 23 (phone). `-pix_fmt yuv420p -movflags +faststart`, AAC 256k.

## 3. Transfers between machines
- PC -> cloud: encode each cut folder to near-lossless mp4 (`-crf 8 -preset slow -pix_fmt yuv444p`),
  push to a git branch, pull and extract frames. Verify frame counts before and after.
- Always check frame counts per folder (`qa_check.py --frames out/c911 --expect 139`).

## 4. Assembly rules
- Build only from shots that passed G4. ROOTS search order: newest approved pass first.
- Missing frames: the script must print them and fail the gate (never silently hold the last frame in a final).
- After assembly run `scripts/qa_check.py final.mp4 --timeline timeline.json` (G6).
