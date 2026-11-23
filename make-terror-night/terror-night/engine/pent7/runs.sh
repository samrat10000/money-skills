#!/usr/bin/env bash
# Ep1 v7 penthouse shots 001-007 exactly as approved/sent (pent7.py is env-driven).
# Needs from the asset pack: cast/sam/sam.blend (faceless Sam rig), pent7/nyc_plate_clean.png (CC BY 3.0 plate,
# credit in ASSETS.md), pent7/phone_screen_akash.png + phone_screen_connected.png (made by phone_screen.py).
# Finals: RES=1080 SPP=48 DEVICE=GPU (on the GPU box). Previews below: RES=432 SPP=16 (cloud CPU).
set -e; cd "$(dirname "$0")"; ENG="$(cd .. && pwd)"
RES=${RES:-432}; SPP=${SPP:-16}
COMMON="SAMBLEND=$ENG/cast/sam/sam.blend CASTLIB=$ENG/cast PLATE=$PWD/nyc_plate_clean.png TSIDE=-1 ANIM=1 RENDER_ANIM=1 FIREL=.35 LAMP=.25 CITYGLOW=.3 CITYCOL=#8a9cc8 FIRE_E=2.5 TONGUE=.3 NOSMOKE=1 RES=$RES SPP=$SPP"
run() { mkdir -p out$1; shift_=$1; shift; env $COMMON "$@" OUT=$PWD/out$shift_/f python3 pent7.py > out$shift_.log 2>&1; echo "$shift_ done"; }
case "${1:-all}" in
 001|all) run 001 PHONE_PNG=$PWD/phone_screen_akash.png CAMV=t TX=1.6 TY=3.0 AX=.2 AZ=.65 PHONE_TABLE=1 NFRAMES=96 BUZZ=8 LIFT0=30 LIFT1=70 WMAX=.18 ERUPT_F=9999 GLOW=6 ;;&
 002|all) run 002 PHONE_PNG=$PWD/phone_screen_akash.png PHONE2=$PWD/phone_screen_connected.png CAMV=p PX=.08 PY=-.17 PZ=.19 LENS=50 FSTOP=2.8 PHONE_TABLE=1 NFRAMES=48 BUZZ=1 SWAP=36 PLIFT=38 LIFT0=200 LIFT1=300 WMAX=.18 ERUPT_F=9999 GLOW=6 ;;&
 003|all) run 003 PHONE_PNG=$PWD/phone_screen_connected.png CAMV=s SX_=-.55 SY_=1.05 SZ_=.1 SAX=-.05 LENS=30 NFRAMES=84 BUZZ=1 LIFT0=1 LIFT1=20 W0=.6 EAR0=12 EAR1=32 ERUPT_F=9999 GLOW=2 ;;&
 004|all) run 004 PHONE_PNG=$PWD/phone_screen_connected.png CAMV=t TX=1.6 TY=3.0 AX=.2 AZ=.7 NFRAMES=175 BUZZ=-100 LIFT0=1 LIFT1=2 W0=1 EAR0=0 EAR1=1 ST0=14 ST1=58 ERUPT_F=110 GLOW=2 ;;&
 005|all) run 005 PHONE_PNG=$PWD/phone_screen_connected.png CAMV=s SX_=-.6 SY_=.85 SZ_=.55 SAX=-.05 LENS=30 NFRAMES=94 BUZZ=-100 LIFT0=1 LIFT1=2 W0=1 EAR0=0 EAR1=1 ST0=-10 ST1=-9 ERUPT_F=-60 GLOW=2 ;;&
 007|all) run 007 PHONE_PNG=$PWD/phone_screen_connected.png CAMV=g KITCHEN=1 NFRAMES=48 BUZZ=-100 LIFT0=1 LIFT1=2 W0=1 EAR0=0 EAR1=1 ERUPT_F=-60 GLOW=2 ;;
esac
