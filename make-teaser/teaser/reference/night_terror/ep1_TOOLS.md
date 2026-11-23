# Ep1: every tool, repo, skill, site and MCP used, and what for (append only)

## 3D and rendering
- Blender 5 as a Python module (`pip install bpy`, cloud) builds every shot from scripts. Cycles CPU renders previews and layout probes.
- Blender 5.0.1 portable on Sam's Asus (`xc\blender501\blender.exe`) renders finals: GPU OptiX, OptiX denoiser. Blender 5.3 needs NVIDIA driver 580+ (Studio 621.24 installer is in xc\nvidia-driver).
- Own libraries:
  - cast/castlib.py: boxes, tubes, blobs and the inverted-hull ink.
  - ep1/city.py (K): materials, sky, characters, rigs, the Night Terror car.
  - ep1/anim.py (A): crawl, shamble, scream, sprint, stomp, idle.
- Sam's character: models/sam/sam.py (MakeHuman-based body, hoodie and jeans). The face is kept hidden.
- Stalker head: models/bullskull.py and swap_bullskull.py, from the teaser thread.
- camera_shakify data (scratch ext/camera_shakify) for handheld camera noise.
- PIL and numpy generate textures (hex tile, blood smear, notices, flyers, graffiti, claw marks, phone screens). The NYC plate was cleaned with PIL.

## Sound
- ElevenLabs makes all the dialogue: Sam is "Jack John", Akash is "Adam" (the voice thread picked them). Files are in /mnt/project-files/voice/ep1.
- Openverse API (api.openverse.org, WordPress/openverse) supplies the CC0 and CC-BY recordings, which come from Freesound. Credits are in scratch sfx7/index.json and /mnt/project-files/tools/openverse_fetch.py.
- Google Flow Music (flowmusic.app, through Sam's Chrome, Sam signs in himself) makes the score and designed SFX. The v5 score is locked.
- ffmpeg does mixing and filters: loudnorm, band-pass for the phone, aecho, sidechaincompress, rubberband, alimiter and acrusher.
- earshot (Leonxlnx/earshot, MIT) is the listening tool, but it can't install in this cloud right now because download.pytorch.org is blocked by the proxy.
- Clipwing real-sfx (Clipwing/skills): an SFX-on-beats helper. Source is in /mnt/project-files/tools.
- Earlier versions also used:
  - AudioLDM2 (cvssp/audioldm2) for AI SFX.
  - LAION CLAP for ranking SFX.
  - A physical V8 engine model (v8.py).
  - ACE-Step AI music, which Sam rejected.

## AI video (tried, rejected)
- Google Flow / Veo 3.1 Lite / Omni 1.2 Flash (flow.google.com through Sam's Chrome) made "Sam waking up" samples. Rejected because they looked AI-made.

## Skills (Claude)
- artifact-design: storyboard and teardown pages (the v6 storyboard, the v7 teardown and plan artifacts).
- glb-vehicle-builder (Sam's own skill): the Night Terror and Bandit car style (ink outlines, chunky tyres).
- ig-reel, ig-viral, ig-caption, ig-human: reel research and captions for the series.
- claude-in-chrome: Sam's Chrome for Flow Music, Flow video, Instagram research and Pinterest reference screenshots.

## Claude Code tools and MCPs
- Remote devices MCP: folder access to xc on the Asus (list, stage, commit) and Remote Control sessions to run Blender on the Asus.
- hearthbot: thread messages, checklist, decision cards and the coordinator.
- claude-code-remote: send_later wake-ups, the environment network allowlist and triggers for the usage-limit resume.
- Artifact tool: storyboards. Project memory: ep1-v7-plan, ep1-dialogue, camera-grammar and others.
- rtk token saver (installed in its own thread) cuts shell output tokens.

## Websites and references
- Wikimedia Commons: the Midtown night plate from the Empire State Building (CC BY 3.0, panoramio). Brand signs were painted out.
- Pinterest, through Sam's Chrome: references for Sam's look and the bull skull.
- Instagram, through Sam's Chrome: viral reel research.
- Pexels and Pixabay: looked at for plates.
- snd7/calldrop.py (own numpy script): realistic phone call drop from a VO line. Args: src dst chop_start cut_time.
