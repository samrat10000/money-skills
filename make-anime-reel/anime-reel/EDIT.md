# EDIT: cuts, assembly, text, deliverables

## Timeline
- One file, `timeline.json` (or the shot list), holds each shot's start and end in frames at 24 fps.
  Picture, voices and score all read the same numbers.
- Most shots run 3-5 s. Hold the hook for 2-3 s. Hold the stinger about 2 s. The total matches the plan (45-65 s for an episode).
- Cut on action or on a held pose. Never cut mid-ease to a stop.
  Keep screen direction across cuts (if Sam rides left to right, the next shot continues left to right). Keep the same light and hour.

## Assembly
- Use only approved shot versions, by exact file name (`NN_name_vN.mp4` or its `fullc_vN/` frames).
- Silent cut first:
  `ffmpeg -f concat -safe 0 -i list.txt -c copy full_silent.mp4`, or re-encode from the frames for exact cuts.
- Then add sound (SOUND.md) and make the per-shot clips with sound by cutting the mixed track at the shot boundaries.

## On-screen text
- The default is no on-screen text in the picture. The story is told by the image.
- If a log stamp is used (a series device), put it small at the top ("KIRIYAMA · DAY 004 · 17:00"), not in the bottom 15%.
- Subtitles, if wanted, are burned into the lower third above the IG UI. Use big, bold type with one emotional line at a time.

## Deliverables
- Per shot: `NN_name_vN.mp4` (crf 14), with 4-5 full-size PNGs (`NN_name_vN_fNNN.png`) and a close-up crop of the risky area.
- Episode: `<project>_epN_full.mp4` (crf 14 master) plus `_phone.mp4` (crf 23 preview, under 20 MB).
- Always give a link the director can open from their phone (GitHub tree page plus raw link).
