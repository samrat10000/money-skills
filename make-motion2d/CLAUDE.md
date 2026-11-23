# CLAUDE.md: make-motion2d

When the user asks for a 2D / anime / toon reel, an episode or a shot of one, or types `/motion2d`:
1. Read `motion2d/SKILL.md` completely, then every file in its reading order.
2. Follow the phases and gates exactly. A gate passes only with evidence logged in `QA_LOG.md`.
3. After building ANY element, run `python motion2d/scripts/qa_frames.py <frames> --ref <locked frame>`, open the
   contact sheet and the crops, describe them, and go through the Director's eye list in `motion2d/QA.md`.
4. Never claim done/fixed/synced without a file or a number. Keep the project's `STATE.md` current.
5. Deliver each shot on its own and keep going; turn every director note into a dated rule in `SHOT_RULES.md`.
