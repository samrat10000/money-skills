#!/usr/bin/env bash
# Packs engine/ (code + unpacked assets, no renders) into a render kit for a GPU box, split into parts small
# enough for a file-copy tool. Usage: bash scripts/make_kit.sh [part_size, default 24M] -> kit/ep1kit.zip.partNN
set -e; cd "$(dirname "$0")/.."; SZ="${1:-24M}"; mkdir -p kit
zip -q -r kit/ep1kit.zip engine -x 'engine/*/out/*' 'engine/**/__pycache__/*' '*.blend1'
split -b "$SZ" -d kit/ep1kit.zip kit/ep1kit.zip.part
md5sum kit/ep1kit.zip; ls kit
echo "On Windows: cmd /c copy /b part00+part01+... ep1kit.zip ; Get-FileHash -Algorithm MD5 ep1kit.zip ; Expand-Archive"
