#!/usr/bin/env bash
# preview_encode.sh <frames_dir> <sound.wav> <out NNN_name_vN.mp4> [step]
# 720x1280 review clip: mild hqdn3d (no black dots), crf 17, AAC 192k. step=2 -> frames rendered every 2nd frame
# are blended up to 24 fps (say so in the critique; never for fast motion).
set -e; D="$1"; A="$2"; O="$3"; STEP="${4:-1}"
if [ "$STEP" = 2 ]; then IN=(-framerate 12 -pattern_type glob -i "$D/f*.png"); VF="minterpolate=fps=24:mi_mode=blend,"; else IN=(-framerate 24 -pattern_type glob -i "$D/f*.png"); VF=""; fi
ffmpeg -y -loglevel error "${IN[@]}" -i "$A" -vf "${VF}hqdn3d=3:3:5:5,scale=720:1280:flags=lanczos,format=yuv420p" \
  -af apad -c:v libx264 -crf 17 -c:a aac -b:a 192k -movflags +faststart -shortest "$O"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$O"
