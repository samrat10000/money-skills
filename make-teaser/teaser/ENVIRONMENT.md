# ENVIRONMENT: machines, models, tokens, delivery

## Compute
- **Render box:** the user's home Asus TUF F17 (RTX 3050 4 GB), folder `C:\Users\cross\Downloads\xc`,
  Blender 5.0.1 portable `xc\blender501\blender.exe` (OptiX works on driver 566.07; Blender 5.3 needs
  driver 580+). The OFFICE laptop (`C:\Users\Developer\...`) has no usable GPU: never render there.
  Before starting any remote session, check the device PATH, not just the machine name (both show as
  TREX).
- **Order:** Asus when online -> cloud if the Asus is offline or the user says "render on cloud".
  Never wait idle for the PC: start the cloud render in parallel and use whichever finishes first.
- **Batch:** detached PowerShell batch (`Start-Process powershell -WindowStyle Minimized ...`), 12-frame
  chunks, skip-existing, done-marker files (`DONE_<pass>.txt`), progress file, logs per cut. Only one
  Blender render on the GPU at a time (two halve each other).
- **Keep awake:** never change power settings. A temporary `SetThreadExecutionState` helper that exits
  on a done-marker is acceptable. Ask the user to set sleep to Never on AC.
- **Cloud:** `pip install bpy` (Blender as a module) renders on CPU; run long jobs with nohup and keep the
  session alive; chunk them so a container restart resumes.
- **Live progress for the user:** a read-only watcher script on the PC (frame counter, s/frame, ETA).

## Models and effort (token rules)
| Work | Claude | Codex / OpenAI | Others |
|---|---|---|---|
| Plan, story, beat sheet, creature design, animation code, QA verdicts | Opus (high effort) | GPT-5-class, reasoning high | best available |
| Render queues, encodes, transfers, downloads, frame pulls | Sonnet or Haiku subagent | mini model | small model |
- One contact sheet per probe; no endless look-test loops; no page-text dumps; no progress chatter.
- At most 2 heavy threads/sessions at once.
- If a usage limit stops the work, resume automatically when it refills (state is in TEASER_STATE.md).

## Delivery
- Big files (> 20 MB): push to the user's GitHub repo and give BOTH links:
  `https://github.com/<owner>/<repo>/raw/<branch>/<path>` (direct download) and the `/blob/` page
  (download icon). Phone previews of big attachments have no download button. Keep each file < 100 MB.
- Names: `NNN_name_vN.mp4` for shots, `<project>_final_IG.mp4`, `_master`, `_phone`.

## Tools that were used (see reference/night_terror/*_TOOLS.md for the full list)
Blender 5.x (bpy), Camera Shakify data (CC0), ffmpeg, numpy, PIL, scipy, soundfile, pyloudnorm,
earshot (listening), Openverse/Freesound (CC0/CC-BY sound), Pinterest/web search for references
(screenshots in the user's browser when the CDN blocks the cloud), storyboard artifact page.
