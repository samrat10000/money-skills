# Teaser 1: what Sam rejected or what broke, and the fix
- Used the Brute poster first. Sam meant the reindeer/Stalker poster. Fix: rebuilt the animatic around the Stalker. Lesson: confirm which poster/character first.
- 910 v1 rendered as a blurry skull surface. The camera aimed at the midpoint between the eyes, behind bone. Fix: ray-cast for a clear line of sight to one eye, shoot side-on, focus = distance.
- Deer skull "looks funny, round, like popcorn", with square molars and cone teeth, and the eye was "just a red dot". Fix: bull skull (lofted single mass, not unions of tubes), crooked blade teeth of mixed sizes with broken stumps, and the ember-vein eye.
- Sam pinned rounded bone ends ("make it sharper at the end, not round"). Fix: every bone end tapers to a spur (poll corners, zygomatic arch, mandible angle, coronoid, premaxilla beak, nasal tips). Lesson: rounded caps read cute; points read scary.
- Hide patches on the skull read as cow-print spots. Fix: removed them from visible areas.
- Blob objects lost their scale when bound (matrix_world = HM overwrote it), giving giant red spheres. Fix: matrix_world = HM @ matrix_world.
- Tongue/throat looked like chrome or a lilac balloon (too glossy, SSS). Fix: rough, dark, wrinkled rotting flesh, recessed.
- 911 v1: only the skull moved and the skid stopped dead. Fix: stalker_body() for limbs/spine, plus an over-rotating, settling skid with roll.
- Asus asleep overnight. I can't change power settings (not allowed), so Sam set them himself.
- Cloud background jobs die when the session idles. Keep the turn busy, or chunk the work.
- Asus "slow" (3-12 min/frame): not throttling (GPU 100%, 1972 MHz, 63 C) but VRAM full (3.9/4.0 GB) with power at only 34 W, so memory was spilling to system RAM. Fix: TEXLIM env (Simplify texture limit 2048) in teaser.py, plus the read-only nvidia-smi logger (gpu_CUT_FR.csv in teaser\out). A commit to the PC once went out stale (old file size), so check the file size/grep on the PC after every commit.

## 2026-11-22 dark shots 903/906/907/908
- NOFOG (speed) removed the world fog, and the giant/Brute/slab only read as silhouettes against lit fog. Fix: fog ON for those cuts + an area "backlight" behind the subject aimed at the lens (lights the fog, keep it out of frame or it shows as a coloured blob).
- 903 giant was 100 m away (4% of frame width): moved to 68 m. 907 Brute sat 1.6 m back from a roof edge seen from below at 50 deg, so the roof hid it: moved to the edge, camera pulled back, 80 mm.
- 908: city.box() bakes its location into the mesh, so keying .location doubled it and the slab fell 22 m past the road, out of frame. Re-centre the origin (data.transform(-loc)) before keying any box.
- Overwriting a file on the PC with device_commit_files can silently stay stale. Commit to a NEW filename, check md5, then cat it over the target.

## 2026-11-22 911 v2 rejected (monster)
- Jaw opened BACKWARD: stalker_alive guessed the snout direction from eye-vs-skull-centre; the long bull skull flipped it, so the hinge sat at the snout tip. Fix: hinge + direction from the rig's 'jaw' bone. Once fixed, the old scream pitch (-46) pointed the face at the sky: retuned so the head thrusts at the low camera.
- Arms moved "like a machine": both stilts keyed from one curve and only the end bones rotated (one hinge). Fix: per-side plans with offset timing/height, motion spread over every chain segment (m1-m3) through springs that lag more toward the tip, staggered slams, weight shift, strain tremor, out-of-step chest arms.
- Sam's bar: the 910 eye close-up realism ("fabulous") for the whole creature.
- v2.1 (Sam 01:43 IST): the spring_ping opening sounded like a cartoon boing; replaced by ping_0 steel pipe strike (unpitched). Never use 'spring' samples for trailer pings.
- v2.2 (Sam 01:57 IST): (1) pitched-down "dragon breathing" (breath_2) read as a human moan at ~6 s: never pitch breaths down; removed everywhere. (2) Roar came ~1 s after the jaw opened: the scream layers were placed by clip start, not by their attack, and nothing covered the jaw hanging open (911 f16-35). Fix: read the jaw keys (shots2 stalker_alive J_ + shift_keys offset), place every vocal by its ATTACK (onset()) on the jaw snap, run a growl through the whole open-mouth hold.
- 905->906 'car stops then flies' (Sam 2026-11-23): two Bezier keys ease a car to a halt. Always linear(car) for driving shots and match speed across cuts.
