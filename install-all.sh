#!/usr/bin/env bash
# Runs every skill pack's installer.
set -e; cd "$(dirname "$0")"
for f in */install/install.sh; do echo "== $f"; bash "$f"; done
