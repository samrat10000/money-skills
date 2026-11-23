# ASSETS: what exists, where it is, how to get it, how to add more

## Get the asset pack
The heavy files live on this repo's `terror-night-assets` branch (4 parts, 341 MB, md5 of the joined zip
`0199be7edcfbc42516dcb0f521c7ef5b`), so `main` stays light. They unpack INTO `terror-night/engine/`.
- macOS/Linux/cloud: `bash scripts/fetch_assets.sh`
- Windows: `powershell -ExecutionPolicy Bypass -File scripts\fetch_assets.ps1`
- By hand: download `terror-night/tn_assets.zip.part00..03` from
  `https://github.com/samrat10000/money-skills/tree/terror-night-assets/terror-night`, join them in order
  (`cat part* > tn_assets.zip` / `copy /b part00+part01+part02+part03 tn_assets.zip`), unzip into `terror-night/`.
- Viewer GLBs (Brute v2, Stalker v5, earlier cast) are in `terror-night/glb/` on the same branch.

## Inventory (after unpacking)
| path (under engine/) | what | status |
|---|---|---|
| ep1/car/nt.glb | the Night Terror with full cabin (front -Y; driver x+.4; passenger x-.4; dash y-.85) | in every car shot |
| ep1/car/Night_Terror_Fastback_v2.glb | the user's original upload | source |
| cast/out/rig/brute/brute.blend | Brute v2 (brute2.py; wedge skull, torn cheeks, fused hi-vis vest) | APPROVED direction, skull sharpened |
| cast/out/rig/stalker/stalker.blend | Stalker v5: bull skull, ember-vein eyes, antlers (from the teaser) | final; stitched-mouth tear still TODO |
| cast/out/rig/screamer, crawler, runner, walker2, husk | infected cast, rigged | used in Ep1 |
| cast/sam/sam.blend | faceless Sam rig (hoodie, glasses, lean) used by pent7.py | shots never show his face |
| pent7/nyc_plate_clean.png, nyc_ink.png | Midtown night plate (brand signs painted out) + ink version | CC BY 3.0 (Wikimedia/Panoramio): keep the credit; verify the author on the original file page before publishing |
| pent7/phone_screen_akash.png, phone_screen_connected.png | PIL-made phone screens (alert + incoming "Akash", connected call) | phone_screen.py remakes them |
| ep1/vo/*.wav | Ep1 dialogue (ElevenLabs, the user's account), named by timecode_speaker | 16 lines + voicemail |
| sfx7/<category>/ + sfx7/index.json | real CC0/CC-BY recordings with title, creator, licence | credit CC-BY ones |
| music/sfx/*.wav | early SFX takes (partly AI-generated): replace with real recordings when touched | legacy |
| ep1/tex/*.png (in the repo) | PIL-made decals: hex tile, smears, claws, flyers, door numbers, EXIT, B1 PARKING | |
| mh/ (in the repo) | MakeHuman CC0 base mesh, skeleton, weights, targets | builders need it |

## Loading in a shot
`K.char('brute', V(x, y, 0), rot_z)` loads `cast/out/rig/brute/brute.blend` under one root empty and keeps the
skeleton (`K.char_rig(root)`). `nt_car(loc, rot)` loads the car and returns `car, parts, glow_material, spots`.

## Rebuilding / adding a character (gate G3)
1. 3+ real references in `refs/<name>/` (Pinterest via the user's browser, film stills), `refs/README.md`.
2. Copy the closest builder (`cast/brute2.py` for a hulk, `husk.py` skeletal, `crawler.py`, `screamer.py`,
   `survivor.py` for humans/friends). Builders: MakeHuman targets -> subdivide -> numpy displacement sculpt ->
   cuts (lips, nose, sockets) -> teeth/claws/spurs as tapered tubes -> garments by bone weights -> materials ->
   pose -> ink hull -> turnaround renders.
3. Turnaround: `ONLY=front34,side,face RES=.5 SAMP=24 OUT=out/<name> python3 <builder>.py` (cloud ~3-5 min).
   Look; Director's eye; fix; 3 passes; send the sheet to the director before using it in shots.
4. Rig for shots: `KEEP_RIG=1 OUT=$PWD/out/rig/<name> RES=.12 SAMP=1 python3 <builder>.py` (`rigall.sh`).
5. Viewer GLB: `DEC=.3 DECH=.15 python3 export.py out/rig/<name>/<name>.blend <name>.glb`.
6. Test it in the scene's real light before the full shot (exposure surprises: T5.7).
Prefer a real artist-made CC0/CC-BY model as the base for anything non-human (sketchfab CC0, Poly Haven,
Quaternius): download on the user's machine if the cloud is blocked. Never primitives for anatomy.

## The user's other asset sources
- Vehicles from the user (GLB uploads; compress with gltf.report or zip when uploads are size-limited).
- `glb-vehicle-builder` skill (in make-motion2d/companion) for new stylized vehicles with ink outlines.
- Ep2 repo `dead-roads-ep2` (rider, trike, truck, scanned CC0 PBR textures).
