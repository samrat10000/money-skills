#!/usr/bin/env bash
# Downloads the Night Terror asset pack (rigs, car, faceless Sam rig, sound library, dialogue, plates; 341 MB)
# from the repo's terror-night-assets branch and unpacks it into terror-night/engine/.
# Private repo: needs git access (gh auth login / credential helper). Usage: bash scripts/fetch_assets.sh
set -e
HERE="$(cd "$(dirname "$0")/.." && pwd)"
[ -f "$HERE/ENGINE_PATH.txt" ] && HERE="$(dirname "$(cat "$HERE/ENGINE_PATH.txt")")"   # installed copy: unpack into the repo clone
TMP="${TMPDIR:-/tmp}/tn_assets_$$"
git clone --depth 1 --single-branch --branch terror-night-assets https://github.com/samrat10000/money-skills "$TMP"
cat "$TMP"/terror-night/tn_assets.zip.part* > "$TMP/tn_assets.zip"
echo "md5: $(md5sum "$TMP/tn_assets.zip" | cut -d' ' -f1)  (expected 0199be7edcfbc42516dcb0f521c7ef5b)"
unzip -q -o "$TMP/tn_assets.zip" -d "$HERE"
[ -d "$TMP/terror-night/glb" ] && mkdir -p "$HERE/assets_glb" && cp "$TMP"/terror-night/glb/* "$HERE/assets_glb/"
rm -r "$TMP"
echo "Assets unpacked into $HERE/engine (check: engine/ep1/car/nt.glb, engine/cast/out/rig/*/)"
