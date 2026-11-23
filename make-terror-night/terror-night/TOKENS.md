# TOKENS: how to get the result in one round and spend a fraction of the tokens

Episode 1 took 7 versions over 5 days. Most of the cost was NOT rendering; it was rework and looking.
Here is where the tokens went and the rule that prevents each leak.

| leak in Ep1 | cost | rule |
|---|---|---|
| Whole-episode versions rejected (v1-v6), each re-rendered and re-mixed | days | Shot-by-shot delivery; the plan is approved as pictures first (G2). |
| Reusing shots the director had already asked to fix (v6) | a full version | Search the logs for every shot number before reuse (T8.1). |
| Look-test loops (9 penthouse look tests, many lobby stills) | heavy | ONE contact sheet per probe; fix with intent; max 2 probe rounds before a full render. |
| Guessing positions by rendering | heavy | Print bbox / positions from the scene (`BLEND=1`, a short bpy print) instead of rendering to see where things are. |
| Building humans' faces (MakeHuman Sam v1-v5, AI video) | a day | Never show Sam's face. Decided once, forever. |
| AI music / AI SFX experiments | a day | Real recordings + Flow Music only. |
| Synthetic sounds the director then rejected | many rounds | Real recordings from the start (T7.1). |
| Low-res cloud finals that needed re-rendering | hours | Finals only on the GPU box at 1080. Cloud = probes. |
| Long polling and status chatter | steady drain | Background renders + notifications; reply only with results, blockers or questions. |
| Reading huge files / logs into context | steady drain | `tail -c`, `grep`, head; never cat a render log or a big .py whole if you only need one function. |
| Re-deriving the pipeline in each new session | per session | This skill + EPISODE_STATE.md + SHOT_RULES.md. Read them, do not rediscover. |

## Model routing
- Strong model (Opus-class, high effort): story, plan, creature design, shot code, QA verdicts.
- Cheap model or subagent (Sonnet/Haiku-class): render queues, encodes, file moves, downloads, frame
  extraction, asset packaging. Give exact commands and expected outputs; verify the result yourself.
- At most 2 heavy threads/sessions at once on the same account.

## Budget per shot (target)
- Plan card: written once in P2.
- Probe: 1-2 rounds x 3-6 frames, 1 contact sheet each.
- Full render: 1 (GPU box), 1 contact sheet of the result, 1 clip.
- Sound: 1 mixer script run + 1 listening reading.
- Delivery: 1 message.
If a shot needs a third probe round, stop and write the root cause down before touching code again.

## Switching accounts / tools mid-episode
Everything needed to continue is on disk: `EPISODE_STATE.md` (shot table, statuses, next action),
`SHOT_RULES.md`, the logs, the engine code and the asset pack. A new session (any account, VS Code extension,
Codex) reads SKILL.md -> EPISODE_STATE.md and continues at the next action without re-planning.
