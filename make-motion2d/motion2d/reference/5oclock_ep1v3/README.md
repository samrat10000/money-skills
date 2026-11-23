# Reference: 5 O'CLOCK Episode 1. What each file is and how to use it

These are the real, approved outputs, rules and research from building 5 O'CLOCK Ep1. Treat them as the quality bar:
**your shot must look at least this good.** Open the frames before you build, and compare your probes side by side with them,
including the brightness numbers (p5/p95/p99).

## Frames (the quality bar)
| file | what it is | what it teaches |
|---|---|---|
| `01_speaker_v4_f048.jpg` | Shot 01, the shot the director locked ("v4 was more better, keep v4"): a crow on the 5 PM loudspeaker at sunset | THE look: thin warm ink line, flat cel colour with one shadow tone, warm backlit rim, painted sky with crisp sunlit clouds, sun glow, dust in the beam. A real CC0 crow model, feet locked to the horn. Every new shot is compared with this. |
| `02_mirror_v1_f036.jpg` | Shot 02, the curve mirror (passed: "this is good, go with this") | Mirror/screen inserts: glass rendered as UV emission with a painted insert, ink seat line, edge falloff, sheen and dirt. Organic leaves with real outlines; backlit leaves glow warm. |
| `03_kiriyama_v2_f060.jpg` | Shot 03, the town, after the director's "perfect, but..." note | The detail level: roofs with tile columns and rows, eave and ridge tiles, antennas; clothes with a real cut on a washing line with pegs; textured verges; a rice field with depth (lit raised edges, converging rows, poles shrinking into haze). |
| `04_ride_v4_f048.jpg` | Shot 04, Sam riding home past the Yamada shop | Rim on the sun-facing edges only, veiling sun glare so the frame isn't flat (p95 about 0.8), a detailed road (centre line, 徐行 road text, tyre marks, leaves), keeping left (Japan). The shop window shows his reflection half a second late (the hidden rewatch detail). |
| `04_ride_v4_hands_f048.png` | A full-size close-up of the hand on the handlebar, after "nobody ever grabs a handle like that" | A real grip: fingers wrap around and under, thumb around, hand axis across the bar. A real mamachari comfort bar, not two straight rods. Check every hand that holds anything against this. |

## Rules and story
| file | what it is | how to use it |
|---|---|---|
| `SHOT_RULES.md` | The rule book: the exact recipe of the locked shot 01, plus every dated director note since (crow "made of ovals", cut-out wings, hovering feet, clothes, roofs, field depth, rim side, outline width, road paint, grips...) | The main instruction for building any shot. Re-read it at the start of every shot. |
| `storyboard.html` | The Ep1 story page (18 shots, cast, world, dialogue plan, how it gets made) | The example of an approved story, and the level of story to aim for. |
| `story_DECISIONS.md` | The director's exact words on what he approved and rejected while the story was chosen | Learn his taste: real and grounded, rules, a lone survivor, one concept, nothing gimmicky, pictures over text. |
| `story_IDEAS.md` | Every story version, the 5 rejected pitches, and the 5 O'CLOCK series bible and open questions | Never re-pitch a rejected idea. Keep the series consistent. |
| `project_DECISIONS.md` | Every project decision with its reason, plus the to-do list | Why things are the way they are (workflow: one perfect shot then rules, shot by shot with the 1-minute rule, sound last). |
| `project_WORKING.md` | The full work log: what was done, where the files are, how to rerun | Pick up mid-project without asking. |

## Research
| file | what it is | how to use it |
|---|---|---|
| `granite-waves-study.html` | The analysis of the Granite Waves hand-drawn anime reels, the art form we follow | Copy the art form and the level of animation only (line, flat cel, painted soft BG, one accent, held poses with small precise motion). Never its characters, scenes or story. |
| `REEL_RESEARCH.md` | Instagram research (numbered "log" reels, hooks, comment patterns, series formats), the narrator voice analysis, the night-road void reel | Use it to plan hooks and series devices, and to direct the narrator (low, close, tired, silence between lines). |
| `MUSIC_REFERENCE.md` | Measured analysis of the piano reel the director chose as the music reference | Build the score to match: piano from the first second, about 65 BPM, quick octave figures over a held bed, rests. Real instruments only. |

## How to run it
| file | what it is |
|---|---|
| `RENDER_NOTES.md` | Rendering on the director's PC (RTX 3050): exact commands, speeds (about 0.6 s per cel frame, about 3 s per comp frame), traps (an absolute outdir, args after `--`, BelowNormal priority) |
| `01_speaker/` ... `04_ride/` | The real build, paint and comp scripts of each approved shot. Copy the one closest to your shot and change only what it needs |
| `assets/` | The toon Sam build (`build_sam.py`, `render_sam.py`), the cast tools (`cast_render.py`, `build_cast.py`), `cast_list.md` (11 CC0 VRoid characters, licences, and which suits Grandma, the kids, the shopkeeper and Mom), and `SOURCES.md` (licences). Note: the first cast pass read too young, so apply the aging rules before use. |
