# Teaser 1 (Night Terror poster teaser): what worked
- Plan first: pixelated animatic (animatic.py, about 6 s to render) inside a storyboard artifact. Sam approved shots from it before any 3D render.
- Reuse the Ep1 kit: teaser.py runs the shots2.py helpers (camera, shot_cam, kick, nt_car, chase_set, stalker_alive, render) through exec, with one function per shot (cut901..cut912).
- Render speed on the Asus: one Blender process per 6 frames (stops VRAM and persistent-data growth), NOPERSIST, NOFOG, LIGHTPATHS (3 bounces), 20 samples, adaptive, OptiX denoise. This took 6-18 min/frame down to about 3 min/frame.
- Detached batch run_full.ps1 skips frames already rendered and deletes 0-byte placeholders on start, so a rerun simply resumes.
- The cloud (bpy 5.1.2, 4 CPU cores) renders these scenes in 75-140 s/frame, faster than the Asus on heavy shots. Run it as a nohup queue (scratchpad/cq2.sh) and keep the session busy with 10-minute wait calls so the container doesn't idle out.
- Probe before committing a render: probe.py renders 2-5 frames at 360x640 and 12-16 samples. One contact sheet catches framing, focus and model problems.
- Per-shot review: grade each shot with teaser_edit.py (look.lens, grain, VHS on 904/912), post it as NUMBER_name.mp4, and assemble only after Sam passes the shots.
- Bull skull v3 (bullskull.py + swap_bullskull.py) swaps into the rigged Stalker blend without re-rigging: upper parts go on the 'head' vertex group, lower parts on 'jaw', and names keep the 'Stalker skull/teeth/eye/jaw' prefixes so stalker_alive still finds them.
- Ember-vein eye: a wet black orb with Voronoi distance-to-edge veins (noise-warped, Generated coords) and a hot core, sunk deep in the socket. Sam liked it.
- 911 life: stalker_body() keys spine breathing and a rear-up, lifts and spreads the front blade-stilts and slams them at frame 60, claws the chest arms and crouches the hind legs. The car skid over-rotates (yaw 144) and settles by frame 46, with body roll.
- Live progress for Sam: xc\teaser\watch_teaser.ps1 (read-only frame counter with bars and ETA).
- Diagnose PC speed without Remote Control: teaser.py starts nvidia-smi -l 20 (csv in the out folder) and logs the Cycles devices at render_init. Read the files over folder access.

## 2026-11-22 evening
- 911 v2 (139 f) and 910 v3 (eye saccades) rendered on the PC, clips 911_poster_finale_v2 and 910_eye_closeup_v3 posted.
- Visibility check without rendering: vis.py projects the subject's bounding box through the shot camera (world_to_camera_view) and prints the frame coverage and depth.
- 12-frame chunks ran at ~17 s/frame vs ~28 s with 6-frame chunks (the fixed setup is ~80 s per chunk), so use 12+.
- Fix pass run_fix.ps1 (903/906/907/908, fog on) started on the PC at 18:59.

## 2026-11-23 ~01:30 IST: teaser v2 sound + v5 monster
- Stalker v5 (swap_spine.py): red spikes removed, bone dorsal ridge, hunched shoulders. Installed on the PC (md5 0dfdc2eb...), render of 911/906/912 restarted (window closed once at f28, resumed).
- Sound v2 (teaser/edit/sound_v2.py + sound_v2_trims.py, credits CREDITS_v2.txt): no music, 37 real CC0/CC-BY recordings. Trims picked with `earshot find`; each moment verified with `earshot match` on the mix; SOLO=key1,key2 env renders single stems for debugging. Master: lookahead limiter, -14.0 LUFS, -1.4 dBTP.
- Lessons: a long low pitched growl masks a distant siren (reads as "engine idling"): keep growls short. Glass tail under thunder reads as a car crash: end glass at the cut. Passby peak must sit where the car fills the lens (F391), not before.
- Edit SEQ v2: no black before 911, 912 = 52 frames, total 491 frames (20.46 s).
- 2026-11-23 04:40 IST: night_terror_teaser_v2.mp4 (+ _phone) delivered from out_v4 frames (pulled via git branch claude/project-thread-b8yfdd, teaser/xfer_v4, commit 769e003; folder tools were unavailable). HQ pass (out_hq, RES 1.0, 32 spp, ~28 s/frame on the PC) pending transfer via teaser/xfer_hq on the same branch; then rebuild with ROOTS hq frames first.
- 2026-11-23 08:12 IST: FINAL delivered: night_terror_teaser_final_master.mp4 (crf 12) + _IG.mp4 (crf 17), 911/906/912 from HQ pass (1080x1920, 32 spp), transfer commit abe6e36.
- 2026-11-23 14:30 IST: final v2 (night_terror_teaser_final_v2_IG.mp4, GitHub teaser/final commit 727317b): 905/906 rebuilt (constant 35 m/s, linear keys, spray, parked wreck cleared), sound_v3 with real wet-road hiss (Sam: 'Perfect sound'). Rendered in the cloud (Asus offline): ~4.7 min/frame at RES 1, 32 spp, fog.
