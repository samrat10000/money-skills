# SOUND: the music-free, real-recording teaser mix

Approved result ("Perfect sound"): 37 real CC0/CC-BY recordings, no music bed, -14 LUFS.
Working reference: `reference/night_terror/sound_design.py` (+ `sound_trims.py`). Reusable kit:
`scripts/sound_kit.py` (clip, put, at/onset, loop, automate, reverb, limiter, master).

## 1. Sources (real recordings only)
- Openverse API (`api.openverse.org/v1/audio/?q=...&license=cc0,by`, send a browser User-Agent):
  mostly Freesound CC0/CC-BY. Freesound directly if reachable. Keep every source URL, author and licence
  in `sfxlib/index.json` and write `CREDITS_sound.txt`. CC-BY means the caption must say
  "Sound: Freesound contributors" (or the named authors).
- Google Flow Music (flowmusic.app, the user signs in) only for designed hits or if the user asks for
  music. Never AI music otherwise. Never synthesised guitar.
- Download 3-6 candidates per cue; pick by listening tool + spectrogram, not by file name.

## 2. Cue sheet (fill per teaser in timeline.json)
| beat | cue | placement rule |
|---|---|---|
| cold open | one steel/metal strike, reverb tail ~2 s, at t=0.05 s | never spring/boing |
| first lamp/sign | sub thump at -16 dB, low-pass 150 Hz | felt, not heard |
| world | rain bed (loop with 0.8 s crossfades), automated: swell in over 1 s, duck on POV/eye, -60 dB in planned silences | never drops at a normal cut |
| interior shots | rain-on-roof drum, wipers, muffled engine (LP 900 Hz) | cut exactly at the shot end |
| city | distant police siren panned, reverb .25, loudest on the street camcorder | |
| car reveal | double rev "vroom vroom" + water splash on the tyre cam | starts 2-3 frames after the cut |
| driving | real wet-road tyre hiss bed + passby with its PEAK where the car fills the lens; V8 echo between buildings | `peak_at()` alignment |
| cut between two driving shots | gear-change bark 2 frames BEFORE the cut | speed continuity in sound too |
| glass | glass shatter 0.5 s, HP 500 Hz, ends at the cut | never under thunder |
| lightning | thunder crack on the flash frame (-0.05 s), rolling body under it, low boom | |
| impacts | trailer hit + debris + boom on the landing frame | |
| crash zoom | whoosh whose PEAK hits the arrival frame + hit + short pitched growl | |
| eye ECU | world drops away: heartbeat (LP 300), low chest rumble, reverse thunder swell into the next cut, sub-drop leading the hero cut | no breath sounds |
| hero cut | big boom on the cut, engine scream into the drift, 3 drift screech layers (0, +0.05, +0.10 s) that die when the scream starts, skid scrub-out, splash | |
| creature | snarl on the frame the jaw drops (attack-aligned), growl covering the whole open-mouth hold, swelling; scream = 3-4 animal layers (elk, lion, tiger, deep roar), pitched .55-.8, ATTACK on the jaw snap; slams on each claw impact; decays into a growl | `at(x, t)` = onset alignment |
| car past lens | passby + whoosh + low thunder + felt whomp as the body blacks out the lens, tape-stop | |
| dark beat | dead silence | |
| stinger | tiny click, VHS static bursts, a close growl right on the lens, final hit + static cut | |

## 3. Mixing rules
- Place every cue by FRAME from `timeline.json` (frame / 24). Jaw, impact, flash and passby frames come
  from the shot code, not from watching.
- Use `onset()` (attack detection, -10 dB threshold) to align attacks, never the file start.
- Varispeed pitch for size (pitch < 1 = bigger and slower). Never on breaths.
- Short growls; long low growls mask the siren and read as an idling engine.
- Stereo: beds wide, point sources panned to their screen side; LP filters for distance; reverb for
  street canyons (t60 ~2.2 s).
- Master: integrated loudness -14 LUFS, lookahead limiter ceiling -1.5 dB, iterate limit -> re-measure
  3 times; 24-bit WAV, then AAC 256k in the mp4.
- Debug: `SOLO=key1,key2` renders single stems; `EXCL=` removes stems.

## 4. Listening check (G5)
- earshot (Leonxlnx/earshot): `earshot find` to pick trims, `earshot match` per moment on the mix,
  `earshot critique final.mp4` for sync to cuts. If earshot cannot install, use CLAP/AST tagging plus
  onset and spectrogram plots, and say which tool you used.
- For each key moment write: time, what should be heard, what the tool hears. Fix mismatches.
- Phone check: high-pass 200 Hz + low-pass 8 kHz; the drift, scream and rain must still read.
