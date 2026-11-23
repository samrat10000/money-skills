# ENVIRONMENT: machines, renders, delivery

## Machines
| machine | use | notes |
|---|---|---|
| GPU render box (the director's home Asus TUF F17, RTX 3050 4 GB) | ALL finals and long renders | Blender 5.0.1 portable at `C:\Users\cross\Downloads\xc\blender501\blender.exe` (OptiX works on driver 566.07; Blender 5.3 needs driver 580+). Set to never sleep. Folder `C:\Users\cross\Downloads\xc`. ffmpeg is installed (WinGet yt-dlp.FFmpeg). Pillow must be in Blender's Python for v7sets.py (ask the user first). |
| Office laptop (`C:\Users\Developer\Downloads\xc`) | commands only | no usable GPU: never render there |
| Cloud container (4 CPU, 16 GB) | probes, sound, encodes, planning, git | Cycles CPU ~60-80 s/frame at RES .4 SAMP 20; use when the GPU box is unreachable, never as a reason to stop |

Speed reference: Asus 1080x1920 OptiX ~4-10 s/frame (64 spp, denoiser, adaptive, reduced bounces, persistent
data); CPU OIDN costs +5.6 s/frame. Cloud is 10-20x slower.

## Getting the engine onto the GPU box
- The render kit is the engine + rigs + car + textures as one zip (`scripts/make_kit.sh` builds it; the asset
  pack has a ready copy). Ship it in < 25 MB parts when the only route is a file-copy tool, join with
  `cmd /c copy /b part00+part01+... kit.zip`, check the MD5 (`Get-FileHash -Algorithm MD5`), `Expand-Archive`.
- Or `git clone` this repo on the box and run `scripts/fetch_assets.ps1`.
- Run with `scripts/run_cut_asus.ps1 -Cut 125 -Frames 120` (30-frame chunks, waits while another
  blender.exe is running, never kills it, logs per chunk, encodes an mp4 at the end).
- Share the GPU fairly with other projects: chunks, check `tasklist | findstr blender` before each.

## Remote Control (Claude app)
A Remote Control session runs Claude Code on the box with the user's tools. Give it a complete brief (paths,
commands, chunking, what to report). It cannot install software without the user's own OK in words; ask the
user directly and early. While it runs, the thread's folder tools are paused.

## Delivery
- Previews: `NNN_name_vN.mp4` (720x1280, crf 17) + stills, in the project's previews folder.
- Big files (> 20 MB): also push to a GitHub branch and give both links:
  `https://github.com/<owner>/<repo>/raw/<branch>/<path>` (direct download) and the `/blob/` page. Keep each
  file < 100 MB. The repo is private: the user must be signed in on their phone.
- Final: `<show>_ep<N>_IG.mp4` (crf 17, -14 LUFS), `_master.mp4` (crf <= 12), `_phone.mp4` (< 15 MB),
  `CREDITS.txt`.

## Logs (append-only, mirrored to the box under `xc\logs\<episode>`)
`WORKING.md`, `DECISIONS.md`, `MISTAKES.md`, `TOOLS.md`, `SHOT_RULES.md`, `QA_LOG.md`, `EPISODE_STATE.md`.

## Usage limits
If work stops because the usage limit ran out, resume every paused thread automatically when it refills
(the director's limit resets every 5 hours; schedule a check 5 minutes after each reset). Before the limit,
write the exact resume point into `EPISODE_STATE.md`.

## Browser work (user's Chrome via the Claude extension)
References (Pinterest), ElevenLabs, Flow Music: the user signs in; never type passwords. Downloads land in the
user's Downloads folder; stage them from the device. The cloud cannot reach elevenlabs.io or pinimg.
