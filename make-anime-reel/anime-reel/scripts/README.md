# scripts

| script | what | notes |
|---|---|---|
| toonlib_v4.py | toon material, `lin()`, outline hull, mesh helpers | exec'd by the build scripts |
| build_ref_shot.py | shot 01 v4b (crow lands on a Showa loudspeaker): the locked quality bar | needs `CROW_GLB` set to the CC0 raven GLB; args after `--` |
| paint_bg.py | painted sunset sky, clouds, fbm mountains, tower | `python paint_bg.py bg.png sunx suny` |
| comp_ref.py | composite (parallax, light wrap, bloom, dust, grade, grain) | `python comp_ref.py <celdir> <bg.png> <outdir>` |
| contact_sheet.py | contact sheets and full-size crops for QA | open the output and describe it |
| pixel_stats.py | p5/p95/p99 brightness against R7 targets / a reference frame | |
| run_shot.ps1 | full shot at BelowNormal priority, timed, keeps old outputs | Windows |
| build_sam.py | builds the toon hero (VRoid base + hoodie, glasses, headphones, toon mats) | edit ROOT and VRM paths at the top |
| cast_render.py | front render + licence meta of every .vrm in a folder | `blender -b --python cast_render.py -- <dl> <out>` |
| build_cast.py | first-pass townsfolk from VRoid samples | the first pass read too young. Apply CHARACTERS.md aging rules |
| mix_ref.py | voice + score + SFX mix placed by time, prints WARNING on overlaps | `python mix_ref.py <score> <audio_dir> <out.wav>` |

Copy them into each shot's `src/` folder and change only what the shot needs. Keep the `argv` line for `--` args.
