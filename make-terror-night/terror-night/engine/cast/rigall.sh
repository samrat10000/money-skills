#!/bin/bash
cd "$(dirname "$0")"
# builds every rigged cast blend into out/rig/<name>/<name>.blend (what city.char() loads). brute2.py = Brute v2.
for n in walker2 runner crawler screamer brute2 husk; do
  o=${n%2}; [ "$n" = walker2 ] && o=walker2
  mkdir -p out/rig/$o
  KEEP_RIG=1 OUT=$PWD/out/rig/$o RES=.12 SAMP=1 python3 -u $n.py > out/rig/$o.log 2>&1
  echo "$n $? $(grep -a -c 'RIG KEPT' out/rig/$n.log)"
done
