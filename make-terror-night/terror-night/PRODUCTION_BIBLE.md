# PRODUCTION BIBLE: Night Terror (the authoritative reference; update after every episode and every review)

The director's standing order (2026-11-26): "a cinematic horror series that feels like a coherent, meticulously directed
film, with persistent characters, believable environments, natural performances, exceptional sound design and consistent
visual quality. Every frame intentional, every environment connected, every character keeps its identity."
Read this before planning any shot. RULEBOOK T17 turns each section into a test.

## 1. Approved asset registry (ONE current version each; change only by a deliberate, propagated upgrade)
| asset | approved version / file | identity that must never drift | status / open work |
|---|---|---|---|
| Sam | `cast/sam/sam.blend` (MakeHuman CC0 base) | body, clothes, hair; face never readable; voice ElevenLabs "Jack John" (male, ~100-140 Hz) | hands on objects need IK grips (R13) |
| Akash | voice only, ElevenLabs "Adam", always through the phone-speaker bus | one phone voice in every call and voicemail | |
| Apartment (penthouse) | `pent7/pent7.py` sets (sofa, chair, window wall, kitchen counter, door) | layout, sofa, furniture, window positions, warm lamp + city-fire light | MUST become one persistent set that the hook/watcher shots also film (R1b); today `watcher_set()` rebuilds an approximation: forbidden from Ep2 on |
| Sam's phone | `pent7/phone_screen*.py/png` | body, bezel, screen proportions, UI, ringtone, buzz | REDESIGN pending (R3): text inside bounds, original UI, animated incoming call; then reuse everywhere |
| Hero car "Night Terror" | `ep1/car/nt.glb` | exterior, interior, dimensions | interior detail + gripping hands pending (R13) |
| Car sound kit | `v8cloud/v8/mix_v8.py`: start+idle = `xsfx/idle2.mp3` (Chrysler V8, exhaust), revs/drive/pass-by = `tsfx/rev2_9.mp3` (V8); buses `car` (exterior, street reflections), `cari` (cabin, low-passed), `carf` (far) | ONE engine identity; perspective changes only by distance/EQ | build a standalone kit folder for Ep2 |
| Stalker (reindeer/bull skull) | teaser model via `v8bridge.teaser_stalker()`; jaw hinge = rig `jaw` bone TAIL, snout dir = tail->head (JAWTEST verified) | anatomy, antlers, ember eyes, saccades | strongest non-boss: powerful, deliberate, fast when it acts |
| Brute v2 | `cast/out/rig/brute` | wedge skull, torn cheeks, heavy stomp | never frozen; stumble/idle after impacts |
| Screamer | v5 rig + v5 scream stems (LOCKED sound) | stands still, scream onset via reverse-reverb swell | |
| Camcorder (hidden watcher) | `scripts/assemble.py rec_overlay()` | REC + blinking dot TL, segmented battery + tape counter TR, burned-in date/time BL (starts 3:47:02 AM, one continuous clock + tape across the episode), Lucida Console white + dark shadow, faint interlace, VHS 0.8 | reusable as is |

## 2. Location chain (spatial continuity; draw a floor plan before shooting a new location)
Penthouse (window faces the burning skyline) -> apartment door -> corridor -> stair door -> stairwell (marble treads, iron
balusters, windows onto the SAME city) -> LOBBY door -> lobby (glass storefront onto the avenue) -> B1 PARKING door ->
service stair -> garage -> ramp + roll gate -> avenue -> overpass/bridge.
Every doorway: reach, handle, door opens, the NEXT space is visible through it and identical to the next shot, move through,
the next shot continues the movement (match on action). Ep1 still has jumps at apartment door -> corridor, corridor -> stair
door, and LOBBY door -> v7 lobby (deferred, R7/R8/R10).

## 3. Camera and cinematography
- Two found-footage cameras: Sam's camcorder (handheld, step-synced, lamp) and the hidden watcher (long lens from far,
  REC OSD, focus hunting, breathing). Never reveal the watcher.
- Match on action, screen direction, eyeline, 180-degree line across every cut. The out-frame of N and the in-frame of N+1
  are compared side by side for every cut (G6.5).
- Long-lens follow cameras are keyed EVERY frame on a smoothed track of the subject (never keys every N frames with
  per-segment easing: that stutters, Ep1 095).
- The hook: frame 1 already shows a person and an open question (who is filming him?), the first hard event lands
  within ~1.3 s, narration states place + time over the aftermath.

## 4. Lighting
Practical only (lamps, fire, headlights, phone screens, the burning city). A low storm-cloud volume is the canvas that fire
and blasts light from below; without it night skies stay black. Emissive discs (moon) never in a close frame: use
`visible_camera = False` to keep their light. Every hero moment is lit where it actually happens (move lamps when blocking
changes, Ep1 125).

## 5. Animation standards
- Characters always alive: breathing, weight, idle sway; never a frozen pose, never crossed legs at rest.
- After every impact: a reaction on real steps (stumble), then recovery.
- Creature jumps: anticipation (crouch) -> launch with upward velocity -> ballistic arc (stylised gravity allowed) with the
  body pitching and limbs reaching -> impact compression -> recovery. Never translate a body down a straight line.
- Vehicles: one continuous speed curve across cuts (a stop happens once), J-turns pivot round a travelling rear axle,
  weight on springs, contact-checked against every body (gap <= 15 cm at the hit, never negative).
- Hands: IK to grips, fingers wrap, no clipping; if a hand cannot be shown correctly, frame so the action reads otherwise,
  never an object moving by itself.

## 6. Sound design standards
- Every recurring object has ONE sound identity (car engine, phone ring/buzz, doors, monster voices, camcorder handling).
- Perspective = the same source through distance/EQ/reverb buses, never a different recording.
- Onsets are designed: big vocal onsets get a swell (reverse reverb of the source) and a rising bed; nothing starts cut.
- Lines 9-12 dB above their bed, the bed ducks with a fast (~0.35 s) release; phone voices on the shared phone bus.
- Master -14 LUFS; measure the FINAL mp4s (AAC adds ~1 dB of overshoot): <= -1 dBTP there.

## 7. Visual effects
Explosions: flash (frame-filling light), staged fireball growth, secondary bursts, smoke shells, environment lit (facades,
clouds, interiors through glass), camera kick + sound on the frame. Benchmark the director named: the final-episode
explosion of Demon Slayer: Hashira Training Arc (scale, layered smoke, light on everything).

## 8. Shot-by-shot QC (before "final")
| area | verify |
|---|---|
| character | correct model, clothes, anatomy, recognisable |
| asset | approved version (section 1) |
| environment | architecture, materials, background detail, same as before |
| animation | natural, alive, physical contact |
| continuity | position, direction, door state, light, audio across the cut |
| lighting | readable, consistent, no light balls |
| camera | composition, smooth (per-frame) moves, perspective |
| sound | sync on frames, smooth onsets, lines intelligible |
| pacing | no dead time, no repeated actions, no abrupt jumps |
| VFX | integrated, lights its surroundings |
| render | flicker, clipping, deformation, artifacts |
Then the whole episode continuously, twice (G6.5). Look for what the director has NOT mentioned.

## 9. Lessons log (newest first)
- 2026-11-26 director review of Ep1 (R1-R23, `logs/REVIEW_2026-11-26_SAM.md` in the project): outstanding = garage car
  sequence ("100/10", the benchmark), stairwell run, bridge stop, final departure. Fixed in the review pass: hook (frame-1
  person + 1.3 s boom + real buildings + clouds lit + Sam faces the window), 095 stutter, one V8 engine, scream onset,
  voicemail level, Stalker leap, Stalker jaw direction, 125 single stop + rear-axle J-turn + Brute stumble, 004w front light,
  camcorder OSD, 055 dead time. Deferred (need persistent assets first): persistent penthouse set, phone redesign, door-open
  transitions + real LOBBY signage, stairwell windows/light, car interior + hand grips.
