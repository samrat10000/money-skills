# DISCIPLINE: making every agent (VS Code extension, Codex, small models) behave like the best run

Observed: the Claude desktop app produced better results than the VS Code extension, and Codex needed
constant correction ("you are doing this wrong"). The difference is not talent; it is discipline:
planning before building, looking at its own output, and not stopping early. These rules force it.

## For every agent
1. **Plan file first.** Before any code or render, write `beat_sheet.md`, `look.md`, `timeline.json`
   and `TEASER_STATE.md`. If they don't exist, you are not allowed to build.
2. **Todo list mirrors the gates.** Create a todo/checklist item for every gate and every shot
   (`G4 911_poster_finale probe 1/3`). Mark items done only with evidence logged in `QA_LOG.md`.
3. **Look at your own output.** After every render or edit, open the PNG / contact sheet with your
   image-reading tool and describe what you see, specifically, before judging it. If your tool cannot
   view images, run the numeric checks (`vis_check.py`, `check_motion.py`, `qa_check.py`) and say that
   the visual check still needs a vision-capable model or the user.
4. **No silent downgrades.** Never lower resolution, samples, length, number of shots or sound layers
   to finish faster without writing it in `DECISIONS.md` and telling the user.
5. **No fake completion.** Do not say "rendered", "synced", "fixed" or "sounds great" unless a file,
   number or listening reading proves it. If a step failed, say so with the error.
6. **Root-cause before re-render.** When a check fails, write the cause in one sentence first
   ("two Bezier keys ease the car to a stop"), then change code. Never re-render hoping it changes.
7. **Re-read the rule book at each phase start** (RULEBOOK sections for that phase). Long sessions
   and context compaction make agents forget rules; re-reading is mandatory, not optional.
8. **Continue autonomously.** Do not stop after one shot to ask "should I continue?". Move through
   the phases; only stop for the user at G2 (plan approval, once) or a true blocker.
9. **Small model mode.** If you are a smaller/faster model: do exactly the steps, run every checklist
   line, do the extra pass (minimum passes +1), prefer the proven recipes and parameters in the
   reference code over inventing new ones, and escalate creative judgment calls (new creature design,
   story) to a stronger model or to the user with images.

## Claude Code, VS Code extension
- Start the session with the skill invoked (`/teaser ...`). If the extension does not list it, say:
  "Read `~/.claude/skills/teaser/SKILL.md` and follow it exactly."
- Use the strongest model and high effort/thinking for phases 0-4 (`/model opus`; effort high).
- Use plan mode for Phase 2 (write the plan), then leave plan mode to build.
- Allow the image Read tool on PNG/JPG (that is how it looks at contact sheets).
- Long jobs: run renders in the background and keep working; check results when they finish; never
  "sleep"-poll for minutes.
- Before context fills, update `TEASER_STATE.md`; after a compaction, re-read SKILL.md, RULEBOOK.md,
  QA.md and TEASER_STATE.md before the next action.
- Subagents (Sonnet/Haiku) only for render queues, encodes, downloads, file moves; give them exact
  commands and expected outputs; verify their result yourself.

## Codex (CLI / IDE)
- Put `AGENTS.md` (repo root of this skill pack) in the working folder or reference it, and start with:
  "Run the teaser skill: read teaser/SKILL.md and every file it lists, then follow it for: <idea>."
- Use the highest reasoning effort for planning and creature/animation work.
- Codex tends to build then stop: the gates are mandatory. After each build step, run its QA
  checklist and write the QA_LOG entry before the next step.
- Codex must view its renders (attach/open images) or run the numeric checks; "it compiled" is not QA.

## Any other AI
- Load SKILL.md as the system/task instruction and give it file access to this folder. The same
  phases, gates and scripts apply. If it cannot run code, it can still produce the plan (G0-G2) and
  the shot scripts, and a capable runner executes them.
