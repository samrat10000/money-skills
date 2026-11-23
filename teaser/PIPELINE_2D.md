# PIPELINE_2D: anime, 2D, comic (2D)

The 2D look is the most fragile: anything that looks generated, stretched or morphing is rejected.
Lessons from 5 O'CLOCK (anime reel series): the crow made of ovals was rejected three times until a
real artist-made model was used; "one shot perfect first, then the rest is easy".

## Two valid builds
1. **3D-for-2D (recommended for creatures, vehicles, camera moves):** model/rig in Blender, render with
   a toon shader (Shader-to-RGB with 1 hard shadow band, flat fills) + an outline pass (inverted hull or
   Freestyle/Line Art at 1.5-2.5 px at 1080 wide), characters stepped on twos (render every frame, hold
   pairs in the edit), camera on ones. Backgrounds as painted plates (projected onto simple geometry for
   parallax).
2. **Layered 2D (for held, graphic shots):** painted background plate, character layers drawn as clean
   vector/ink shapes, animated by real per-frame drawing changes (blinks, hair, cloth, fingers), never
   by warping a still. Camera = parallax between layers + handheld micro-shake.

## Rules specific to 2D
- Line: clean, thin, dark (not pure black: #1b1a1f-ish), consistent weight per shot; thicker on outer
  silhouette.
- Colour: flat cel + ONE shadow tone per material; one accent colour per scene; painted soft-focus
  backgrounds with depth haze.
- Animation: held poses with small precise real motion; smear/impact frames (1-2) on hits; no
  puppet-stretch, no morph transitions.
- Organic creatures: never from primitives (R4.1). Use a real model (CC0) + subdivision + toon + hull
  outline; lock feet/toes to surfaces every frame (no hovering).
- Text in the world (signs, notebooks) is drawn, never typed in a system font, unless a screen UI.

## The perfect-shot recipe rule
Make shot 1 (or the hero shot) perfect first. Then write `SHOT_RULES.md`: line weights, colours (hex),
shadow threshold, light directions, model sources, timing (ones/twos), camera shake values, post
settings. Every later shot follows SHOT_RULES.md exactly. Gate G4 adds: "matches SHOT_RULES.md".

## Post for 2D
- Light paper/film grain (~1.5%), slight chromatic fringe at frame edges, no heavy glow.
- VHS/analog treatment only on found-footage/broadcast shots.
- Sound recipe is identical (SOUND.md).
