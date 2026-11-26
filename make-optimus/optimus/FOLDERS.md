# FOLDERS: one layout for every project

```
<root>/                                  e.g. C:\Users\cross\Downloads\xc
  <project>/                             night-terror, 5oclock, <new series>
    episodes/
      ep01-<name>/
        edit/          assembler inputs/outputs, per-shot graded clips, SOURCES.md
        renders/       raw frames per cut (cNNN/fNNNN.png), render logs, queue log
        sound/         episode mix script, stems, master
        logs/          EPISODE_STATE.md, QA_LOG.md, REVIEW_<date>.md, DECISIONS.md
        previews/      per-shot delivery clips + stills
        deliveries/    final master / IG / phone, CREDITS.txt (also published as a release)
      ep02-<name>/ ...
    shared/
      engine/          the production code used by every episode (+ paths.py / paths.ps1)
      assets/          characters/ creatures/ vehicles/ sets/ props/ ui/   (approved, versioned, in the bible)
      sound/           sfx library (+ index.json credits), kits (e.g. car_v8/), voices/, music/
      references/      approved stills, moodboards, research
      PRODUCTION_BIBLE.md (or a link to the skill's bible)
  _tools/        blender, ffmpeg wrappers, drivers, queue/keep-awake scripts shared by projects
  _skills/       the money-skills clone
  _archive/      everything retired: old versions, experiments, benchmarks (never deleted without the user)
```

## Rules
- A project folder is self-contained: its episodes + its shared assets. Nothing of one project inside another.
- Episode folders hold only episode-specific files; anything used twice moves to `shared/`.
- Version suffixes in file names (`_v3`), never overwrite a version the director has seen.
- Each project has its own git repo if it has code (or the root repo with media ignored); renders and media go to
  GitHub releases, never into git history.

## The paths file
`shared/engine/paths.py`:
```python
import os
ROOT = os.environ.get('PROJ_ROOT', os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SHARED = os.path.join(ROOT, 'shared'); ASSETS = os.path.join(SHARED, 'assets'); SOUND = os.path.join(SHARED, 'sound')
def ep(n): return next(os.path.join(ROOT, 'episodes', d) for d in os.listdir(os.path.join(ROOT, 'episodes')) if d.startswith(f'ep{n:02d}'))
BLENDER = os.environ.get('BLENDER', os.path.join(os.path.dirname(ROOT), '_tools', 'blender501', 'blender.exe'))
```
`paths.ps1` mirrors it for queues. Scripts import these; no absolute paths anywhere else.

## Migration procedure (only when NOTHING is rendering)
1. Inventory: every top-level folder -> size, what it is, which project, keep/archive. Show the old -> new map to the user.
2. Grep every script/doc for absolute paths; list what must change.
3. Move with `robocopy /MOVE` (or `git mv` inside repos), project by project.
4. Leave a junction at each old path that scripts or notes still use (`mklink /J old new`) until they are updated.
5. Update scripts to `paths.*`; update state files and skills.
6. Smoke test: one probe frame, one mix rebuild, one assembler run, the watcher. Log it in the episode QA_LOG.
