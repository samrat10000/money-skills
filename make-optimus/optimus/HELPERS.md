# HELPERS: small-model helpers for chores

Give a helper (a small/fast model subagent, e.g. `model: haiku`) only jobs that are pure procedure with a checkable
result. Keep judgment with the strong model.

| give to a helper | keep with the strong model |
|---|---|
| upload files to a release and return the links | anything that decides if a shot is good |
| encode / re-encode / extract frames / make a contact sheet | root-cause diagnosis |
| move/copy/rename per an explicit map, then list the result | creative fixes, new shots, creature motion |
| download assets/SFX from given URLs + write credits | plans, estimates, director-facing summaries |
| run a given script and report the printed numbers | reading the numbers and deciding |

## Brief template (a helper starts cold: give it everything)
```
Task: <one sentence>.
Working dir: <absolute path>.
Run exactly:
  1. <command>
  2. <command>
Expected: <what success prints / which files exist with which sizes>.
If anything differs from Expected: stop and report the exact error. Do not improvise, do not retry differently.
Report: <the 2-5 lines you need back, e.g. URLs, sizes, counts>.
```
Then verify the result yourself with one cheap check (a listing, a size, an API query) before telling the user.

## When NOT to use a helper
Tiny jobs (one command): the briefing costs more than doing it. Anything touching running renders or the user's system
settings. Anything where a wrong result is expensive and hard to notice.
