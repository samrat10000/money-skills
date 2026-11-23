# money-skills

Sam's reusable, model-agnostic skills. Each folder is one self-contained skill pack with its own README,
installer and rules. Works with Claude Code (desktop app, CLI, VS Code extension), Codex and other agents.

| folder | skill | use |
|---|---|---|
| [make-teaser/](make-teaser/) | `/teaser` | 15-25 s viral vertical teaser from an idea, a poster or your assets, any art style, final quality in one round |
| [make-anime-reel/](make-anime-reel/) | `/anime-reel` | 15-65 s 2D / toon anime story reels and episodes, shot by shot with self-QA, to the 5 O'CLOCK quality bar |

## Install everything
```
git clone https://github.com/samrat10000/money-skills $HOME\money-skills
powershell -ExecutionPolicy Bypass -File $HOME\money-skills\install-all.ps1
```
macOS / Linux: `git clone https://github.com/samrat10000/money-skills ~/money-skills && bash ~/money-skills/install-all.sh`

Or install one skill with its own `install/` script. Update later with `git pull`, then run the installer again.

## Adding a new skill
Create a folder `make-<thing>/` with `README.md`, `AGENTS.md`, the skill folder (with `SKILL.md`),
`install/install.ps1` and `install/install.sh`, then add a row to the table above.
