# CLAUDE.md (make-terror-night)

(All paths below are relative to this make-terror-night/ folder.)
When the user asks for a Night Terror episode, shot, creature, set or sound pass, an episode of a new series
in the same 3D ink-realism horror style, or types `/terror-night`:

1. Read `terror-night/SKILL.md` completely, then every file in its reading order (`DISCIPLINE.md`,
   `SERIES_BIBLE.md`, `RULEBOOK.md`, `QA.md`, `PIPELINE.md`, `SOUND_VOICE.md`, `ENVIRONMENT.md`, `TOKENS.md`,
   `PLAYBOOK_EP1.md`, `MISTAKES.md`, and `ASSETS.md` before touching a model).
2. If `terror-night/engine/ep1/car/nt.glb` is missing, fetch the asset pack first (`scripts/fetch_assets.*`).
3. Follow the phases and gates exactly. A gate passes only with evidence logged in the project's `QA_LOG.md`.
4. After building ANY element, LOOK at it (contact sheet, crops) and run the Director's eye list in `QA.md`
   before moving on or sending.
5. Never claim done, synced or good-sounding without a file, a number or a listening reading.
6. Keep `EPISODE_STATE.md` current so any agent or account can continue the work.
