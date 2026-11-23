# STYLES: the style switch

Pick the style in Phase 0 (`style=` argument, or ask once). The style changes ONLY the look recipe
(shading, line, colour, post). Structure, camera grammar, motion rules, sound, continuity and every
QA gate stay identical. Write the chosen style's recipe into `look.md` and apply it to every shot.

If the user describes a style not listed ("like X but darker"), write a new preset in this same
format, show one hero still as a look test, and lock it once approved.

| key | name | pipeline file |
|---|---|---|
| `3d-ink` | 3D + black ink outline (house style, "3D pencil sketch") | PIPELINE_3D.md |
| `3d-real` | Photoreal 3D found footage | PIPELINE_3D.md |
| `comic` | Comic book (bold ink, flat colour, graphic shadows) | PIPELINE_3D.md (toon) or PIPELINE_2D.md |
| `anime` | 2D anime (thin ink, flat cel + 1 shadow tone, painted backgrounds) | PIPELINE_2D.md |
| `2d` | 2D hand-drawn / painted | PIPELINE_2D.md |
| `pixel` | Pixel art (limited palette, no dithering) | PIPELINE_3D.md + post |
| `sketch` | Sketch-ink that draws in, line boil | PIPELINE_3D.md + post |

---------------------------------------------------------------------------------------------------
## 3d-ink (default for Night Terror)
- Render: Blender Cycles, AgX Medium High Contrast, exposure 0, practical lights only (lamps, headlights,
  fire, lightning), wet asphalt, volumetric haze where silhouettes need it.
- Line: inverted-hull outline (solidify, flipped normals, black emission/holdout material) on hard
  objects, thickness ~0.6-1.2% of object size; ink crease tubes on key edges. Keep motion blur low
  (0.15-0.25 shutter) and DOF moderate (f/5.6-8) so lines survive.
- Colour: painted, chunky shapes, bold ink, high detail. Night palette: sodium orange + cold blue,
  one red accent (the eyes).
- Post: halation, slight anamorphic streak on lights, vignette, split tone (warm highs, cool lows),
  chroma fringe at edges, light grain (~2%), VHS only on camcorder shots.

## 3d-real
- Same as 3d-ink without outlines; real-camera imperfections stronger (sensor noise in shadows, focus
  breathing, lens smudge, rolling-shutter wobble on whip pans). Higher samples (64+). Real photo plates
  allowed ONLY if every shot uses the same treatment (R6.1).

## comic
- Toon BSDF / shader-to-RGB with 2-3 hard light bands, flat fills, thick variable ink (outer line 2x
  inner), graphic black shadow shapes. Colour: limited palette per scene (4-6 colours + black).
- No halftone dots by default (the user dislikes dot patterns); use flat or hatch-line shading. Add dots
  only if asked.
- Motion: may use 12 fps "on twos" for characters, but the camera still moves at 24 fps.

## anime
- Ref: the art FORM of hand-drawn anime reels (e.g. Granite Waves): clean thin dark line, flat cel colour
  with ONE shadow tone, soft painted backgrounds with depth haze, one strong accent colour, held poses
  with small precise real animation, cinematic camera.
- Character animation on twos (12 fps), effects and camera on ones. Smears/impact frames allowed on
  hits (1-2 frames).
- Never AI images/video, no morphing or puppet-stretch, perfect hand anatomy.
- See PIPELINE_2D.md: 3D toon render + line pass, or hand-built 2D layers; backgrounds painted.

## 2d
- As anime but with the user's specified medium (ink wash, gouache, painted). Lock the brush/texture
  set in look.md; paper texture constant, not boiling unless chosen.

## pixel
- Render at 1/6 resolution, quantise to a fixed palette (16-32 colours), mode filter after quantising,
  NEAREST upscale. NO dithering. Transitions as tile wipes (5x5 px tiles), never per-pixel noise.
- Keep subjects big: at 180x320 effective resolution the subject must cover >= 15%.

## sketch
- Line drawing redrawn every 2 frames (12 fps boil), ragged diagonal reveal, then optional switch to
  ink or pixel. Paper tone background; graphite grey lines with darker accents.

---------------------------------------------------------------------------------------------------
## What never changes, whatever the style
Beat grammar (R2), camera grammar (R3), anatomy and motion (R4, R5), readability (R6.3), real sound
(R7), naming and delivery (R8), every gate in QA.md.
