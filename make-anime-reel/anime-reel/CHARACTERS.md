# CHARACTERS: real rigged models, never primitives

## Sources that worked (free licences)
- **VRoid samples (CC0)**, https://opengameart.org/content/vroid-studio-cc0-models, 11 .vrm files:
  - AvatarSample_D, D_Darkness, E, F, G
  - Base_Female, Base_Male, HairSample_Female, HairSample_Male
  - Sakurada Fumiriya, Sendagaya Shino
  The page licence is CC0. The VRM metadata says CC0, or VRoid Hub terms (everyone, commercial use, modification and redistribution allowed, no credit needed).
  Note each one in `SOURCES.md` or `cast_list.md`.
- **Crow:** Teh_Bucket "Raven" (CC0) GLB, from raw.githubusercontent.com/nrknithin/html-anime/main/models/library/crow/model.glb.
  It may be meshopt-compressed; if import fails, run `npx @gltf-transform/cli copy in.glb out.glb` first. opengameart.org is blocked from some clouds.
- VRoid Studio (free) can create new base characters when no sample fits.

## Import
- Use the VRM Add-on for Blender v4.10.5 (MIT), installed as an extension (`bl_ext.user_default.vrm`).
  - Script: `addon_utils.enable('bl_ext.user_default.vrm', default_set=True)`, then `bpy.ops.import_scene.vrm(filepath=...)`.
  - Cloud bpy: install the add-on zip into the bpy user extensions first.
- `scripts/cast_render.py` renders a front view of every .vrm in a folder at 512x1024 and reads the licence meta. Use it to build a cast sheet.

## Making a hero (`scripts/build_sam.py`)
- Base model, then toon materials (RULEBOOK R2), an outline hull, and costume pieces built from the body:
  - hoodie sleeves as a shell of the arm skin;
  - a hood roll and hood back on the upper back (full size, not undersized);
  - drawstrings, glasses, headphones.
- Keep the costume accurate to the real garment (RULEBOOK R8).
- Body type: lean stays lean (narrow shoulders, slim arms).

## Aging and resizing a cast (lessons from the first pass, where everyone read as a teen)
- **Kids (8-10)** need a head-to-body ratio of about 1:5.5: shorter legs (leg bones about 0.8) and a shorter torso, a slightly larger head, no adult waist.
  Child clothes, plus a randoseru. Uniform scaling of a teen model reads as a small teenager. That fails.
- **Elderly:** remove the youthful outfit meshes (the school skirt and socks).
  Spine hunch 20-30°, bent knees, a shorter stride, grey hair, an age-appropriate outfit (long skirt, apron, cardigan), and a prop (a bamboo broom).
- **Middle-aged men:** a thicker waist and torso (shape keys or bone scale), rounded shoulders, a heavier stance, and costume cues (apron, headband).
- Test each one with a front and 3/4 turnaround next to photo references of real people of that age.
