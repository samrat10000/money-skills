# DISCIPLINE: make every agent work like the best run

What we saw:
- The Claude desktop app gave the best results.
- The VS Code extension gave weaker ones.
- Codex needed constant correction ("you are doing this wrong") and did not check its own work.

The difference is discipline, not talent. The best run planned before building. It looked at every output at full size, measured instead of guessing, fixed root causes, logged everything, and kept going without being told. These rules force that behaviour.

## Rules for every agent
1. **Plan files before code.** `REEL_STATE.md`, `shot_list.md`, `dialogue_script.md` and the project
   `SHOT_RULES.md` (or this skill's `RULEBOOK.md`, if the project has none yet) must exist before any build.
2. **Todo list mirrors the gates and shots.** One item per gate and per shot pass
   (`G4 04_ride pass 2/3`). Tick an item only after its evidence is in `QA_LOG.md`.
3. **Look at your own output, at full size.**
   - After every render, open the contact sheet AND full-size crops of faces, hands, feet, contact points and the newest change.
   - Describe what you see in specific words before you judge it ("toes sit 2 px inside the horn edge", not "looks good").
   - If your tool can't view images, run `scripts/pixel_stats.py` and the crop scripts, and say the visual check is still pending for a vision model or the director.
4. **Check every small part against the plan.** Before moving on, write one line per element: what the plan
   asked for, what the render shows, pass or fail. That covers the prop, the pose, the in-between, the light side and the road text.
5. **Measure instead of guessing.**
   - IK pole positions: search candidate positions and measure the joint, rather than eyeballing it.
   - Brightness: take the p5/p95/p99 numbers.
   - Glints and contact: get the screen position from a projection, never from a guessed offset.
6. **Root cause before re-render.** Write the cause in one sentence, then change the code. Never re-render
   hoping the result changes.
7. **No silent downgrades.** Never lower resolution, samples, frame count, detail or length to save time
   without writing it in `DECISIONS.md` and telling the director.
8. **No fake completion.** "Rendered", "fixed" and "matches" each need a file or a number. If a step failed,
   say so with the error.
9. **Re-read the rules at each phase start** and after every compaction. Long sessions forget rules.
10. **Keep going on your own.** After showing a shot, start the next one if there is no answer within about 1 minute.
    Stop only at G1 (story approval) or for a real blocker. Notes are applied after the current shot.
11. **Small-model mode.** If you are a smaller or faster model:
    - run every checklist line and do one extra pass;
    - copy the proven recipes and numbers from `scripts/` and `reference/` instead of inventing new ones;
    - escalate new creature, character or story design to a stronger model or to the director, with images.
12. **Version hygiene.** A new version gets a new name. Keep the previous output folders (`full_v1/`, `fullc_v1/`).
    Commit only explicit paths. Never `git add` a folder that holds render output.

## Claude Code: desktop app, CLI, VS Code extension
- Start with the skill invoked: `/anime-reel ...`. If the extension doesn't list it, say:
  "Read ~/.claude/skills/anime-reel/SKILL.md and every file it lists, then follow it exactly for: <task>."
- Model: the strongest available (Opus-class) at high effort for story, design, animation code and QA.
  Use Sonnet/Haiku subagents only for render queues, encodes and copies, and give them exact commands.
- **Parity with the desktop app.** The desktop sessions had these extra skills and tools. Install the same ones
  where you work, or the VS Code session will be weaker:
  - Plugins/skills (in Claude Code: `/plugin` to browse your org catalog, `/skills` to check):
    - `remotion-best-practices`, `remotion-render`: motion-graphics and title work
    - `ig-reel`: hooks, beat sheet
    - `ig-caption`: caption and hashtags
    - `ig-human`: remove AI fingerprints from text
    - `ig-viral`: research what's working
    - `glb-vehicle-builder`: stylised GLB props with ink outline
    - `dataviz`: charts, only if needed
  - Built-ins the desktop app had: image reading (the Read tool on PNG/JPG; allow it), a browser (for references), and
    background tasks (run renders in the background, don't sleep-poll).
  - Memory notes: tell the session the render machine facts in `ENVIRONMENT.md`.
  - `make-anime-reel/install/install.ps1` copies `anime-reel/` into `~/.claude/skills/` and `~/.codex/skills/`; `install-all.ps1` at the repo root installs every skill pack.
- Use plan mode for Phase 1 (story and shot list). Leave plan mode to build.
- Allow image reading. Contact sheets and crops are how the agent sees.
- Run long renders in the background and keep working. Check them when they finish.
- Before context fills, update `REEL_STATE.md`. After compaction, re-read SKILL, RULEBOOK, QA and REEL_STATE.

## Codex (CLI / IDE)
- Keep `AGENTS.md` (repo root) in or next to the working folder. Start with:
  "Run the anime-reel skill: read anime-reel/SKILL.md and every file it lists, then follow it for: <task>."
- Use the highest reasoning effort for story, design, animation and QA.
- **Codex tends to build, then stop or declare success.** That is forbidden here.
  - After each build step, run its `QA.md` checklist.
  - Open the images (or run `pixel_stats.py` and `contact_sheet.py`) and write the QA_LOG entry before the next step.
  - "It compiled" or "it rendered" is not QA.
- Codex must write a numbered self-critique after every probe and fix the worst 3 issues before showing anything.
- Use the same skills where Codex supports them (`~/.codex/skills/`), plus ffmpeg, Python with numpy/scipy/Pillow/pypng, and Blender 5.x.

## Any other AI
Load SKILL.md as the task instruction and give it file access to this folder. The phases, gates and scripts
are the same. If it can't run code, it still writes the story, the shot list and the shot scripts, and a capable
runner executes and checks them.
