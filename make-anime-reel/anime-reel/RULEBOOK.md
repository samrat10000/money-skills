# RULEBOOK: every rule, with its test

Each rule says what to do and how to test it. The words in quotes are the director's own notes that created the rule.
A project's own `SHOT_RULES.md` adds to this book and wins where the two disagree. `reference/5oclock/SHOT_RULES.md` is the original.

## R0. The director and the product
- The animation is the product. "The animation is the thing that will stand it out from others. So it shouldn't be degraded."
  - Show full-size PNGs and high-quality clips (crf 14). A compressed preview is only ever an extra.
- "100 times" more detail and precision than average. Aim to beat the art-form reference, not match it.
- It must never look AI-made. That means:
  - no image or video generators for picture content;
  - no morphing, warping or puppet-stretch;
  - no glossy, symmetric, over-graded look.
  - Test: would a frame pass as a cel from a TV anime? If it looks generated, it is rejected.
- Story first, then characters. The concept must engage, not just look good ("the story line is not that good... it's not something that will engage").
- Pictures over text. Show storyboards, contact sheets and clips. Keep messages short and plain.
- Respect cost. No endless exploration and no look-test loops. Probe at low resolution, render full only after the probes pass.

## R1. References first (never guess)
- Art form: collect 3-6 frames of the target look (here: the Granite Waves hand-drawn anime reels: thin dark line,
  flat cel, one shadow tone, painted soft BG, one accent colour, held poses with small precise motion).
  Copy the art form and the level of animation, never the characters, scenes or story.
- Every character, creature and real-world prop gets 3-6 photo or reference images in `refs/` before modelling:
  a bicycle handlebar, a crow, a Showa loudspeaker horn, roof tiles, a koban, a randoseru.
  - Test: put your render next to the reference. The silhouette, proportions and parts must match.
- Human motion is checked against real reference footage (how a person rides, sweeps, holds a phone).

## R2. The look: toon cel layer (Blender EEVEE)
- Render the cel layer with a transparent film at 1080x1920, Standard view transform, 16 TAA samples, PNG RGBA.
- Toon material: Diffuse BSDF > Shader to RGB > RGB to BW > x0.5 > ColorRamp (CONSTANT) > Emission.
  - **ColorRamp colours are LINEAR.** Convert sRGB design colours with `lin()` (`scripts/toonlib_v4.py`). If you skip this, everything renders far too light.
  - Thresholds are tiny: lit at about 0.035, highlight at about 0.075 (after the x0.5). Measure the BW values with a debug render before choosing.
- Rim light: (Layer Weight Facing > 0.40) AND (dot(normal, sun) > -0.15), mixed to a warm rim colour (1.0, 0.66-0.82, 0.45-0.58).
  - Use Facing 0.72 on creatures so wings don't stripe. Flat cards get no rim.
  - **The rim goes only on the edges facing the sun** (normal . sun > 0.10). A rim on the back or far edge is wrong.
    Test: on a full-size crop, the rim sits on the sun side.
- Ink: warm near-black (0.10, 0.06, 0.08), as an inverted hull with backface culling.
  - Line width scales with distance: at least 0.00075 x camera distance. A 1.6 mm hull vanished at 4 m; 3 mm reads.
  - Props get 0.003-0.008 m by size. Test: at full size the outline reads on every character and prop edge.
- Lights: world about 0.12, cool fill sun 0.35, warm key sun 5.0 low behind the subject.
- Props: two tones plus a rust or dirt multiply from object-space noise. Paint shadow (0.27, 0.25, 0.37), lit (0.62, 0.66, 0.60).

## R3. The look: painted background (numpy, `scripts/paint_bg.py`)
- Paint at 110% size so it can push and drift.
- Sky gradient stops: top (0.13,0.12,0.27), 0.22 (0.30,0.20,0.38), 0.42 (0.70,0.36,0.42), 0.58 (0.97,0.55,0.36),
  0.70 (1.0,0.76,0.48), 0.80 (1.0,0.86,0.62).
- Sun: a disk plus two glows (0.05 and 0.22 falloff), placed where the Blender sun projects on screen (the build prints `SUN_SCREEN x y`).
- Clouds: 3 stratus layers from stretched fbm with crisp edges, sunlit undersides near the sun and thin gold rims.
- Mountains are fbm ridges, never sine waves, with haze. Add landmarks (the 1964 radio tower with a blinking red light) and rooftops.

## R4. Characters and creatures
- **Never build organic characters or creatures from primitives** (ovals, spheres, cards). The director rejected that
  three times: "made of ovals", "cut out wings", "hovering feet". Start from a real, artist-made,
  rigged CC0/CC-BY model and use its own animation clips (`CHARACTERS.md`).
- Prep: smooth shading, Subdivision level 2, toon material, inverted-hull outline.
- Real scale first, then frame for drama with the camera.
- **Contact:** feet and toes are locked to the surface every frame. Measure the lowest toe in world space and offset the body.
  Never float. Test: a full-size crop of the feet in every held pose.
- **Hands that hold anything must really grip it.** ("Nobody ever grabs a handle like that.")
  - The fingers wrap around the object and the thumb opposes from the other side.
  - The palm is in contact, and the wrist stays roughly in line with the forearm.
  - On handlebars, the hand axis runs across the bar, palm down on top.
  - If IK can't reach (error > 2 cm), move the body or the part. Never leave a hand floating or resting on top.
  - Test: close-up renders of each hand from the side, top and front before the full render.
- Anatomy: hands, fingers, elbows, necks and knees must be right. Broken limbs read as AI.
  - Lean characters stay lean.
  - Children have child proportions: a big head ratio (about 1:5.5), shorter legs and torso. Scaling an adult or teen model is not enough.
  - The elderly get a hunch, bent knees and age-appropriate clothes.
- Eye glint: a tiny white bead placed EVERY FRAME from the head and beak bones on the camera-facing eye.
  A bone-parent offset left both glints floating a head-height above the crow.
- Painted far or mirror figures use bezier silhouettes with a shoulder and hood slope, a leg gap, shoes and a contact shadow. Never boxes.

## R5. Motion
- Characters animate on twos (hold every drawing 2 frames). Hold on threes for weight. The camera moves on ones.
- Blend the model's own clips (fly, flare, stand, walk) per bone with quaternion slerp.
- Landings: wings or arms up, body pitched up about 40°, legs forward, then a damped settle, a fold in about 0.4 s and a ruffle.
- Birds hold, then snap the head. People breathe. Hair, hoodie strings, bags, leaves and cloth follow through.
- **In-betweens are drawings too.** Look at every in-between at full size.
  - An IK in-between that juts the elbow sideways is a fail. Solve the pole position numerically.
  - A local-rotation slerp that swings the arm out is a fail.
  - The good in-between keeps the elbow low with the hand travelling in front of the body.
- Fast moves get smear frames. Nothing is frozen unless the story asks for it.
- Shot length: hold long enough to read (3-5 s for most shots), and end on a held pose.

## R6. Camera and framing
- Low angle, looking slightly up at the subject against the sky. 38 mm lens, vertical sensor fit.
- Subject in the upper-middle third, with the low sun behind it.
- Slow pushes of 2.5-3.5% over a shot, with a small sine drift. Multi-plane parallax: the BG moves slower than the cel layer.
- Keep the bottom 15% (IG UI) free of anything important. Keep the sun on screen and low (sx 0.8-0.9) when the look depends on it.

## R7. Composite (`scripts/comp_ref.py`)
- BG blur sigma 2.2. BG push 1.2% over the shot, cel push about 3.5%.
- Light wrap: blurred BG x the cel's inner edge x (0.45 x beam + 0.08). Bloom: threshold 0.82, sigma 28, x0.28. Warm beam haze x0.6.
- Dust motes: 70 in the sun beam, on twos. Grade: x1.04, then + (0.035, 0.02, 0.05). Vignette 0.30, grain 0.018 (more in the shadows).
- When a building hides the sun, keep a veiling glare so the frame doesn't go flat.
- Targets at the shot's key frame: p95 about 0.8-0.95, p99 at least 0.95, p5 about 0.12-0.19 (`scripts/pixel_stats.py`).

## R8. Real-world detail (the "it's just shapes" notes)
- Clothes: a real garment cut (sleeves, collar or neck hole, hems, legs), folds, seams and prints. Pegs and hangers where things hang.
- Roofs: tile columns as well as rows, the eave tile edge, ridge end tiles, antennas, water heaters, weathering.
- Grass, verges, footpaths: patchy colour, tufts, kerbs, drains, ruts, edge lines.
- Big flat areas (fields, plazas, water) need depth cues:
  - raised edges that catch the light;
  - converging rows;
  - repeated objects shrinking into the distance (poles, sheds, racks);
  - haze.
- Roads: centre line, lane-edge line, painted road text in the right language (とまれ, 徐行), grates, manholes, cracks, leaves, tyre marks.
- Organic props get real outlines (a maple leaf has 7 pointed lobes, a serrated edge and a stem notch). Backlit leaves and cloth glow warm and saturated.
- Mirrors and screens: render the glass as UV emission (16-bit PNG, read with pypng) and map the painted insert through it.
  Add an ink seat line, edge falloff, faint sheen and dirt.
- Country rules: Japan keeps left. Signage, road paint and shop signs use the setting's language and correct glyphs.

## R9. Story rules (see STORY.md)
- One spine: one hero, one place, one clock, one rule per reel, one thing that grows each episode.
- Hook in the first 1-2 s. Escalate. End on a cliffhanger plus a stinger. Add one hidden detail for rewatches.
- Real and grounded: "a boy who lives in Japan... strange things are happening... it must feel REAL... rules... only survivor".
- Never reuse rejected pitches. Inspirations (Chainsaw Man, Pacific Rim, Kaiju No. 8) mean tone, not copying.

## R10. Sound (see SOUND.md)
- Sound comes last, after all animation is approved. Write the dialogue script early.
- Real voices or natural TTS only, never anything that sounds AI-made. The score uses real instruments and is piano-led. No AI music.
- The music thins under every line and swells in the gaps. Silence is part of the acting.

## R11. Process rules
- Make one shot perfect, write it into rules, then do the rest. ("We need to make one short perfect, and rest is easy.")
- Every director note becomes a dated rule for all upcoming shots.
- Shot by shot: notify the director when each is done. With no answer in about 1 minute, move on. Notes are fixed after the current shot.
- Write down every improvement and every decision, because the skill grows from them.
- Never overwrite a version the director has seen.

## R12. Delivery
- Per shot: the clip (crf 14, 1080x1920, 24 fps) plus 4-5 full-size PNGs (start, key moment, close-up crop, end), and an honest critique.
- Big files (over 20 MB) go to the director's GitHub (never `main`), with the tree link and the raw link.
  Files attached in a chat session may not reach the director's project view, so always give a link.
