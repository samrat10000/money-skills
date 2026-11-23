# PLAYBOOK: Night Terror Episode 1 "The Call" (v7), every shot

The worked example. Copy its level of planning for every episode. It is also the live plan for finishing Ep1:
statuses are as of 2026-11-23 (update the project's `EPISODE_STATE.md`, not this file, while working).

Concept: the camcorder never stops recording. Sam left it on a tripod filming a skyline timelapse when the
phone rang; he carries it handheld through the building; in the car he props it on the dash; it keeps
recording after he is gone. References: Cloverfield, [REC], The Last of Us opening.
Length ~96 s. 0-53.5 s real sound + voices only; the score drops on the ignition at 53.5 s.
Storyboard: `reference/storyboard_v7.html`.

Status key: APPROVED (director passed it) / SENT (awaiting notes) / QUEUED / TODO.

## Act 1: The call (0-27 s, penthouse, `engine/pent7/runs.sh`)
| shot | time | camera / action | lights | sound / lines | status, notes |
|---|---|---|---|---|---|
| 001_ring | 0-4 | `CAMV=t` tripod camcorder frames the burning skyline; Sam asleep in the chair at the frame edge, hand resting in his lap; phone rings on the side table at 0.3 s and lights his face from below | city glow .3 #8a9cc8, lamp .25, fire lights .35, phone glow 6 | rain on glass, fridge hum, far siren, real ringtone + vibration on wood | APPROVED v2. v1 notes: fire jittered too fast and in one place; sky pitch black; hand hovered in an L. Fix: slow burning blocks in many places with smoke, fire-lit clouds + stars + ash + rain, hand rests until he wakes. |
| 002_phone | 4-6 | `CAMV=p` 50 mm f/2.8 insert: emergency banner + "Akash" calling, thumb swipes | screen | ring stops dead on the swipe | SENT |
| 003_answer | 6-9.5 | `CAMV=s` behind his right shoulder: phone up to the ear, face turned away | screen goes black at the ear (proximity) | Sam "Akash? It's like... four in the-" | APPROVED v2. v1: phone sank into his head (looked AI). Fix: IK to a point beside the ear, push out until bbox > 12.5 cm from head centre. |
| 004_look_outside | 9.7-17 | `CAMV=t` tripod frame: he stands (heels planted) and goes to the glass, silhouette; a tower erupts at 14.3 s (ERUPT_F=110), shockwave flash, smoke | eruption light | Akash (phone) "Are you seeing this? Sam. Look outside." boom, glass rattle, car alarms; Sam whispers "...oh my God." | APPROVED ("looks awesome now") |
| 005_bridge | 17.2-21.1 | `CAMV=s` over the shoulder, fire reflected in the glass | | Akash "Don't take the bridge, they closed the-" broken by `calldrop.py`; Sam "Akash? Akash!" | APPROVED v2. v1: beep-train drop was "irritating"; fix = broken words, click, dead line. |
| 006_screamer | 21.2-25 | 006a cut41: 135->150 mm across the street, the Screamer on the opposite roof turns its head to HIS window; 006b cut6 (SLOW=2) CU scream to the sky | `relight_roof`: blue x.12, slow fire from the street, key+rim fire, rain glow .02 | the scream alone, echoing; world drops to a rumble; glass hums (`s006.sh`) | SENT v1. Keep: the director loved this scream (v5). |
| 007_grab | 25-27 | `CAMV=g KITCHEN=1`: the camcorder is ripped off the tripod (frame swings, handheld from now on), keys from the counter, door chain, deadbolt | camcorder lamp switches on at f13 (CAMLAMP 24) | miniDV handling, click, running steps on wood, keys jingle | SENT v1 |

## Act 2: Getting out (27-53.5 s, no score; a heartbeat sub from the stairwell door)
| shot | time | camera / action | lights | sound / lines | status, notes |
|---|---|---|---|---|---|
| 030_corridor | 27-30 | cut30: POV corridor, neighbour door PH-C ajar (TV flicker, someone crying), dead elevator, shoulder the EXIT door (opens f58-72) onto the stair hint | emergency spots 45 + 60 W (one strobing), camcorder lamp 26 warm, exposure .35 | marble steps, muffled sob, TV hiss, buzz, siren, push-bar clunk (`s030.py`) | SENT v1. Final: real TV static on PH-C. |
| 040_stairwell | 30-40 | cut40: POV run down a pre-war stairwell (`pov_stairs`, 18 cm dip per tread), door 6C open with TV static and a body, hand-smear trail, 5th-floor strobe; clicks from below at 35 s; at 38 s the lamp swings onto the Crawler climbing up; he vaults a flight | camcorder lamp spot 28 W 72 deg blend .5, strobing emergency lamp | footsteps on every tread, breathing, strobe tick (`stair_snd.py`); Sam "come on, come on" (31.0), "-Jesus!" (38.2) | APPROVED. THE LOOK BAR: "damn cool, I want this realism in all the other clips". |
| 050_lobby | 40-44 | cut50: abandoned doorman desk (lamp, phone off the hook), the horde floods the fire-lit avenue beyond the brass doors; tilt up through the glass shows hundreds; a hand slaps the glass at f57 (handprint f58); back off to B1 PARKING | desk lamp 40 W (shadowless shade), strobing emergency light, camcorder lamp 30, exposure .3 | glass slap, crowd through glass, rain, off-hook tone (`s050.py`) | SENT v2. v1 note: "too much grain, black dots" -> SAMP >= 20, sparse glass drops, textures x4 smoother. Final: denser crowd at the glass, fire texture on the orange building, end on B1 PARKING. |
| 060_garage | 44-50 | cut60: dolly into the garage; four tubes clunk on one by one (f10/22/34/46, constant keys, emission keyed too); the Night Terror revealed headlights OFF; steam | tubes only, exposure .6 | tube clunks + hum, steam, steps; Sam "Keys, keys, keys..." (45.0) | SENT v1. Rebuilds the v5 garage reveal the director called "best scene ever"; headlights must not flicker. |
| 070_in_the_car | 50-53.5 | cut70: dashcam view (lens 18, sensor 30 vertical) as he props the camcorder; settle wobble; he tosses the phone onto the passenger seat (keys f27-f42, lands face up), screen lights f37-62 | dash glow, cabin fill 40 W, phone glow | camera handling, thump, keys, vibration; crank at 2.9 s; Sam "Please start. Please." (51.3) | SENT v1. Weak: cabin dark before the phone lands. |

## Act 3: The run (53.5-76 s, the score drops on the ignition)
| shot | time | camera / action | sound / lines | status, notes |
|---|---|---|---|---|
| 080_ignition | 53.5 | cut80 (wraps cut10): headlights come on ONCE at f11 and stay on (spots 1200 W, glow 30 -> 28) | engine start, clunk, SCORE DROP | SENT v1. Final: tame the headlight haze blowout. |
| 090_gate_burst | 53.5-57 | the car bursts through the garage gate: ONE-take bullet time (`warp_shot`: live 1x -> ~3% -> camera glides -> back to 1x), never an orbit-freeze cut | boom on the hit | TODO (v5 cut61/151/161 exist; re-check v4/v5 notes: freezes must be one take) |
| 095_aerial | 57-62 | aerial of the burning city, headlights threading the avenue (drone lift, real scale), into the low pass | score, wind | TODO (not built) |
| 100_tyre_cam | 59-62 | cut12: 20 mm on the wet asphalt at the tyre, water sheeting off | tyre hiss, V8 | SENT v1 |
| 110_chase_runners | 62-67.3 | cut13: rain chase through runners | radio (robotic EAS) "...remain indoors. Do not attempt to leave the-"; Sam "Yeah? Watch me." (65.5) | SENT v1. Weak: runners hard to see; light them. |
| 120_drift | 67.3-71 | cut16: ONE smooth Tokyo drift to a stop: rear steps out, over-rotates, settles, bleeds speed; no slow-mo | three-layer drift screech; Sam "No no no no-" (68.0) | SENT v1. Weak: reads as a straight slide; add yaw over-rotation + settle (teaser 911 skid recipe). |
| 125_brute_block | 71-76 | cut125: low handheld behind the car (x -2.9); Brute v2 stomps into a headwash spot (650 W, off before the car moves) and roars (jaw f34); the V8 growls back (squat f58-62); the car swerves right past it; ends on its silhouette, ember eyes | stomps, deep roar (s125.py), rev + exhaust pop, tyre spin, whoosh | SENT v1. v2 QUEUED on the GPU box: wheel flare fixed (headwash off at f64), headwash 380 W, deeper roar. |

## Act 4: The overpass and the empty seat (76-96 s, the score thins to a sub drone)
| shot | time | camera / action | sound / lines | status, notes |
|---|---|---|---|---|
| 130_overpass | 76-79 | cut130 (cut20 + `relight_overpass`): stopped under the overpass in rain, tilt up to the Stalker against the moon | rain, thunder, Stalker clicks, idle; Sam (speaker) "Akash, pick up. Pick up, man." | SENT v1 |
| 140_stalker_cu | 79-81 | cut140 (cut21 + relight + `stalker_cu_light`): CU skull, ember eyes, lightning | clicks, breath (never pitched-down moans) | QUEUED. Lighting fixed (fire rim 900 W, cold rim 650 W, headlight spill 1400 W from below, fog <= .0008). |
| 150_stalker_scream | 81-84 | cut150 (cut22 + same light): it stares, mouth hanging, the stitched mouth tears open (gums, crooked blade teeth, wet interior, saliva strands), head snaps up, scream at the sky, lunge at the windshield, glass cracks, cut to black on the hit | its own scream, jaw-locked; impact | QUEUED. TODO in the rig: the stitched-mouth tear (v5 note "mouth is a hole"). |
| 155_black | 84-85.5 | black, silence | | in the edit |
| 160_empty_seat | 85.5-96 | cut160: dashcam still recording; driver door open (hidden), rain blowing in only outside the door, wipers/idle, phone on the passenger seat lights "Akash calling" at f24 and buzzes | rain, idle, two buzzes, Akash voicemail (88.5) "Sam, it's me. I'm at the... I don't know where I am. If you get this, don't come to-" through the phone band, click, dead line (`s160.py`) | SENT v1. Weak: phone screen reads as a white bar (tilt to lens, emission 2.2); open door barely visible (add the door edge with rain on it); was rendered STEP=2. |

## Finishing Ep1 (in this order)
1. GPU box: 125 v2, 140, 150 (queued with `scripts/run_cut_asus.ps1`), then the stitched-mouth rig fix + 150 v2.
2. Build 090_gate_burst (warp_shot one take) and 095_aerial.
3. Fixes listed per shot above, each through G4.
4. 1080 finals of every approved shot on the GPU box (pent7 runs with `RES=1080 SPP=48 DEVICE=GPU`).
5. Dialogue placement per the table, the EAS radio voice, the score from 53.5 s (Flow Music, around the lines).
6. Edit + master (G6), deliver with download links.
