# ENVIRONMENT: machines, priorities, tokens, delivery

## Compute
- **Render box:** the home Asus (RTX 3050 4 GB), folder `C:\Users\cross\Downloads\xc`, Blender 5.0.1 portable `xc\blender501\blender.exe`
  with the VRM add-on installed, Python 3.12 (numpy, scipy, Pillow, pypng, pycairo), ffmpeg on PATH.
- Run everything at **BelowNormal** priority. Other jobs on the PC (teasers) come first. Never stop someone else's job.
  One GPU render at a time.
- `Start-Process ... -PassThru`, then `$null = $p.Handle` before `WaitForExit()`. Without the Handle line, ExitCode comes back empty.
- The cloud (pip `bpy`, CPU) is a fallback: about 20-40x slower for cels.
- Never change power, sleep, driver or system settings. Ask the user.

## Folders and logs (per project)
- `xc\<project>\`: `WORKING.md` (log), `DECISIONS.md` (decisions and to-do, with the director's words), `SHOT_RULES.md`, `REEL_STATE.md`.
- Several AIs (Claude accounts, VS Code extension, Codex) hand off through these files. Read them first and update them before stopping.

## Git
- Push only to the agreed branch, never `main`. Commit explicit paths only.
  Render folders (`full*/`, `fullc*/`, logs, mp4s in `src/`) must never be added.
- If a push is rejected because another session pushed, use `git pull --rebase` and then push again. On a conflict in a rules file, keep both sides.
- Each file must be under 100 MB.

## Model and token rules
| Work | Model |
|---|---|
| Story, character and creature design, animation code, lighting, QA verdicts | strongest (Opus-class / GPT-5-class) at high effort |
| Renders, encodes, copies, downloads | cheap model or subagent, checked afterwards |
- One contact sheet per probe. No endless look-tests, no page dumps, no progress chatter. Report once per finished step.

## Delivery
- Attachments sent from a PC session may not reach the director's chat. Push to GitHub and give the tree link (and raw link).
- A private Artifact review page works for galleries (stills + clips), and stays private to the owner.
