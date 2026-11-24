# SOUND + VOICE: real, on the frame, one line at a time

## Order of work
1. Each shot gets its own real-sound pass when the shot is built (`engine/ep1/snd7/sNNN.py`), so every
   preview the director sees already sounds real.
2. Dialogue is recorded once, in a batch, from the locked dialogue table (credits are limited).
3. No background music (T14.3). The one climax piece is placed on the LOCKED cut, landing on the hit.
4. Final mix + master on the full episode.

## Sources (real recordings only)
- **Openverse API** (`https://api.openverse.org/v1/audio/?q=...&license=cc0,by`, send a browser
  User-Agent). Mostly Freesound CC0/CC-BY. Download into `sfx7/<category>/`, record title, creator, licence
  in `sfx7/index.json`; CC-BY needs a credit line in `CREDITS.txt`.
- Freesound CDN direct (`cdn.freesound.org`) works when the API is blocked.
- Ep1 library (asset pack): rainglass, siren, fridge, ring, vib, stairs, runwood, shoe, keys, camhandle,
  pushbar, glassknock, rattle, static, buzz, alarm, boom, scream, sob, horde, growl, breath, sting,
  calldrop, stairamb; plus music/sfx (rain_city, rain_close, thunder, engine_start, engine_drive,
  exhaust_pop, tire_spin, skid, whoosh, stomp, brute_roar, growl, stalker_click/screech, impact).
  NOTE: music/sfx files were partly AI-generated takes (AudioLDM2) in an early version; prefer the sfx7 real
  recordings and replace any music/sfx cue with a real one when you touch it.
- Never: synthesized buzz/beeps, code-made engines (a "physical V8 model" read as noise at idle and the
  first engine read "like an EV"), Karplus-Strong guitar ("irritates the ears"), AI music beds.

## Recipes that were approved
- Wake-up (001): rain on glass, fridge hum, a far siren; the ringtone and the phone vibration rattling on wood,
  aligned to the screen-on frame; the ring stops dead on the swipe (8 ms fade).
- Eruption: a deep boom (SFX, not music), the glass rattles, car alarms far below.
- Call drop (005 v2, approved): `calldrop.py` breaks the caller's last words (packet-loss gaps, stutter
  repeats, crunch), cuts mid-word, click, dead line. NO beeps.
- Screamer (006): CC0 screams (freesound joseppujol 221547 + nick121087 333832) slowed to 0.8 with a street
  echo; the world drops to a low rumble under it; the glass hums.
- Stairwell (040, approved): marble footsteps on every tread on the footfall frames, stairwell room tone,
  breathing, the strobe ticking, a heartbeat sub from the stairwell door.
- Lobby (050): glass slap on the hand-contact frame, crowd moans muffled through glass, rain, the desk phone
  off-hook tone.
- Garage (060): tube clunk + hum per tube on its light key; steam hiss; footsteps on concrete.
- Ignition (080): real V8 starter crank, catch, two revs (T14.4). No music here.
- Brute (125): stomps on footfalls; roar = brute_roar slowed to 0.78 + a sub layer at 0.5 + a throat growl at
  0.7 with light crush; the V8 growl back = engine_start rev tail + exhaust pop on the body squat frame; tyre
  spin + whoosh on the swerve.
- Empty seat (160): rain blowing in, the idle, two phone buzzes, the voicemail through the phone band, a click,
  dead line.
- Drift (make-teaser SOUND.md): three layers (tyre squeal, scrub, rumble), dies when the next big cue starts.
- Creature vocals lock to the jaw keys (onset, not file start). Never pitch breaths down (reads as a moan).

## Dialogue
- Tool: ElevenLabs (the user's account in their browser; the user signs in). Male "Jack John - Conversational"
  type voice for Sam, a different male voice for Akash, and a robotic/EAS treatment for the radio. Use
  delivery tags like `[panicked, out of breath]`, `[whispered]`, `[voice cracking]`. Generate all lines in one
  batch; download; trim silence; name `TT.T_speaker.wav` by timecode (`ep1/vo/`).
- Table (`templates/dialogue_table.md`): time, shot, who, line, delivery, channel (room / phone / radio).
- Placement: one line at a time, >= 0.3 s breath, never under a scream or a big hit. Phone channel:
  `highpass=f=350,lowpass=f=3400,acrusher=bits=10:mix=.25,aecho=0.8:0.3:12:0.1`.

## Score
- **CURRENT RULE (director, 2026-11-24, RULEBOOK T14.3): NO background music in Night Terror.** Only real
  recordings, plus ONE short piece (6-8 s) at the climax creature encounter, blended in, landing on the hit.
  (Superseded: the v7 rule "score from the ignition to the end".) Everything below about scoring applies
  only to that one piece, or to a series whose director asks for a score.
- Source the director loved: Google Flow Music (flowmusic.app, in the user's browser; they sign in). Prompt
  for an original Stranger Things-like vibe (pulsing 80s analog synth arps + orchestra + real electric guitar
  with bass doubling, slightly detuned, a tuned grand piano opening), never copying a theme melody. The
  director rejected raw AI-music takes (ACE-Step) as "trash"; an orchestral score from CC0 samples (VSCO-2,
  Karoryfer Shinyguitar, Splendid Grand Piano) was "promising" and its ending "perfect".
- Score AROUND the lines: sparse bed under dialogue, gentle sidechain duck (3-6 dB), full energy between lines.

## Mix numbers
- Preview per shot: loudnorm I=-18..-20, TP -2, alimiter .89.
- Master: -14 LUFS integrated, true peak <= -1 dBTP, lookahead limiter (pedalboard's Limiter adds makeup
  gain: avoid it or compensate).
- SFX under a scream window anchored about music -3 dB RMS (the director called that scream level "perfect").

## Listening
Never claim how audio sounds without a reading. Tools: earshot (describe, timeline, critique an mp4 against
cuts; install notes in COMPANION_SKILLS.md), or at least onset detection + a spectrogram PNG you look at.
Phone-speaker check: high-pass at 200 Hz and confirm key cues still read.
