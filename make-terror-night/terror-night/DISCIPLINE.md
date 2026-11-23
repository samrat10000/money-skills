# DISCIPLINE: make every agent behave like the best run

The director observed that the Claude desktop/cloud runs gave better results than the VS Code extension, and
that Codex needed constant correction ("you are doing this wrong"). The difference was never talent. It was:
(1) planning before building, (2) LOOKING at its own renders, (3) a Director's eye pass before sending,
(4) not stopping early, (5) having the right tools installed (image viewing, Blender, ffmpeg, sound tools,
companion skills). These rules force all five on any agent.

## For every agent
1. **Plan files before code.** `brief.md`, `storyboard` (shot cards), `dialogue_table.md`, `EPISODE_STATE.md`.
   If they do not exist, you may not build.
2. **Todo list mirrors the gates and shots** (`G4 125_brute_block probe 1/2`). Mark done only with evidence
   in `QA_LOG.md`.
3. **Look at every render yourself.** Open the PNG / contact sheet with your image tool and describe what you
   see in specifics ("the Brute's skin reads cream-pale under the 2600 W spot; face unreadable") before
   judging. If you cannot view images, say so and run the numeric checks in `scripts/`.
4. **Root cause before re-render.** Write the cause in one sentence first ("rain_here box overlaps the camera
   because rain_anim jitters +-0.6 m"), then change code. Never re-render hoping it changes.
5. **No silent downgrades.** Never lower resolution, samples, frame count (STEP=2), shot count or sound layers
   without writing it in `DECISIONS.md` and saying it in the delivery note.
6. **No fake completion.** "Rendered" needs the frame count; "synced" needs the frame of the cue; "sounds
   good" needs a listening reading (earshot or equivalent). If a step failed, say so with the error.
7. **Re-read the rules at each phase start** and after every compaction. Long sessions forget rules.
8. **Continue autonomously.** Do not ask "should I continue?" between shots. Stop only at G2 (plan approval,
   once), for a creative choice that changes the story, for anything irreversible, or a true blocker.
   If the director is silent, keep going on the recommended option and say what you chose.
9. **Re-check old notes before reusing anything.** v6 died because five reused v5 shots were the very shots
   the director had asked to fix. Search `DECISIONS.md`/`MISTAKES.md` for the shot number first.
10. **Small model mode.** If you are a small/fast model: follow the recipes and parameters in `PLAYBOOK_EP1.md`
    and the engine code exactly (they are proven), run every checklist line, add one extra review pass, and
    escalate creative calls (new creature design, story changes) to a stronger model or the user with images.

## How the director works (adapt to it)
- Gives notes from a phone, often by voice, short ("coolll", "Progress", "keep going"). Treat "Progress" as:
  reply with numbers (shots done / total, frames, s/frame, ETA in IST), one still, nothing else.
- Wants each finished shot immediately, with your honest self-critique, and wants you to keep working.
- Hates chatter and repeated questions. One batched question at most, or a decision card with a recommended
  option, and keep working on the recommended option while waiting.
- Watches token cost. See `TOKENS.md`.
- Time zone IST (UTC+5:30). Use it for every time you write.

## Claude Code, VS Code extension
- Start with the skill invoked (`/terror-night ...`). If it is not listed: "Read
  `~/.claude/skills/terror-night/SKILL.md` and follow it exactly."
- Strongest model, high effort for P1-P4 and creature work (`/model opus`). Plan mode for P2.
- Allow the Read tool on PNG/JPG (that is how you look at contact sheets).
- Run Blender renders in the background (`run_in_background`) and keep working; never sleep-poll.
- Install the companions (`COMPANION_SKILLS.md`): the desktop app had them, the extension does not by default.
- Before the context fills, update `EPISODE_STATE.md`; after compaction re-read SKILL, RULEBOOK, QA, STATE.

## Codex (CLI / IDE)
- Put `AGENTS.md` in the working folder and start with: "Run the terror-night skill: read
  terror-night/SKILL.md and every file it lists, then follow it for: <task>."
- Highest reasoning effort for planning, creatures and animation.
- Codex tends to build then stop or claim success from "it compiled". After every build step run the QA
  checklist, open the probe image (or run `scripts/contact_sheet.py` and attach it), write the QA_LOG entry.
- Codex must not invent new looks: copy the light/lens/MB/grain numbers from `SHOT_RULES.md`.

## Any other AI
Load SKILL.md as the task instruction, give it file access to this folder. The same phases, gates and engine
apply. If it cannot run code, it can still write the plan (G0-G2) and the `cutNNN()` functions for a capable
runner to execute.
