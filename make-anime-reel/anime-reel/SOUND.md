# SOUND: last, sparse, real

Sound starts only after every shot's animation is approved. The dialogue script is written in Phase 1.

## Voices
- Real people, or natural TTS that doesn't sound AI-made. The narrator, the hero and special voices (a double, a town PA) each get their own direction.
- The recipe measured from the art-form reference:
  - a low, tired, close-mic voice;
  - 60-90% of the energy below 250 Hz;
  - weight at the start of a line, then a fade;
  - lines of 1.5-3 s with gaps of 1-3 s; silence is acting.
  - Mix: cut below 70 Hz, lift 150-250 Hz, roll off above 6-8 kHz, light compression, no reverb (dry booth).
- A double or mirror voice: the hero's take processed drier, closer and a hair lower.
- A town PA voice: calm, polite, slightly too slow, heard through an outdoor PA with a mountain echo.
- Name takes `<LINE>_takeA.mp3`, `_takeB.mp3`, ... The mix script uses the first file per prefix, so put the chosen take first.

## Score
- Real instruments, piano-led, starting with the picture. The reference reel had a piano entering in the first second,
  about 65 BPM, quick 3-5 note figures doubled in octaves over a held bed, and rests between phrases.
- Never use AI music generators for the final.
- Pick the take whose piano starts within the first second and has the clearest rests.
- **The score thins under every line and swells in the gaps.** Duck 8-10 dB under voices with a gentle sidechain. Never a hard pause.
- SFX from CC0/CC-BY sources (Openverse, Freesound, VSCO-2 CE samples) are logged in `CREDITS.txt`.
- A 5 PM chime of real tuned percussion (marimba or glockenspiel from VSCO-2 CE) is placed exactly on picture cues.

## Mix (`scripts/mix_ref.py` is the working example)
- Place every element by frame from the timeline. The script prints `WARNING:` if a line runs into the next one.
  Fix every warning before mastering.
- Master: `ffmpeg -i mix.wav -af loudnorm=I=-15:TP=-1.5:LRA=11 mix_norm.wav`. Check the reading on the output file.
- Mux per shot: cut the mastered track at the shot boundaries and mux it with each shot. Then the full cut.
