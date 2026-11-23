# AGENTS.md (make-teaser)

(All paths below are relative to this make-teaser/ folder.)
This repo holds skills. When the user asks for a teaser, a trailer-style reel, or types `/teaser`:

1. Read `teaser/SKILL.md` completely, then every file in its reading order
   (`DISCIPLINE.md`, `RULEBOOK.md`, `QA.md`, `STYLES.md`, the pipeline file, `SOUND.md`, `EDIT.md`, `ENVIRONMENT.md`).
2. Follow the phases and gates exactly. A gate passes only with evidence logged in `QA_LOG.md`.
3. After building ANY element, run its checklist and the Director's eye pass before moving on.
   Look at your renders (open the images) or run `teaser/scripts/qa_check.py`,
   `teaser/blender/vis_check.py`, `teaser/blender/check_motion.py`.
4. Never claim something is done, synced or sounds good without a file, a number or a listening reading.
5. Keep `TEASER_STATE.md` updated so any agent can continue the work.
