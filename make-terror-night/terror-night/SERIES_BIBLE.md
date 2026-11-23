# SERIES BIBLE: Night Terror: Dead Roads

Use this as canon for Night Terror, and as the TEMPLATE for any new series made with this skill (copy the
headings, fill them for the new world before planning an episode).

## Premise
The city falls at 3:12 AM. A virus (with an alien/mutation angle) turns people into infected that mutate in
stages: Walker / Runner -> Husk -> Screamer / Crawler / Brute -> Stalker. Sam, a young man in a New York
high-rise, escapes in his own modified car, the **Night Terror**, and sets out to reach his three friends in
three cities, one rescue per season. Episodes are 60-100 s vertical web-series chapters for Instagram Reels
and YouTube Shorts, each one night, each ending on a cliffhanger.

Tone: grounded found-footage horror (Cloverfield, [REC]), the opening of The Last of Us, car action with
weight. Never campy, never cartoony, never "AI".

## Recurring devices
- **The camcorder that never stops recording.** Sam's miniDV camcorder (tripod timelapse at the window ->
  handheld -> propped on the dash as the dashcam). It explains every handheld shot, keeps Sam's face off
  camera, and lets the last shot be the dashcam watching an empty seat. Use it every episode.
- **The phone.** Calls from friends carry the story (Akash). The phone lights faces from below, rings on
  surfaces, drops calls by breaking words (never beeps). A phone planted earlier pays off later.
- **The emergency radio**: a robotic EAS voice ("...remain indoors. Do not attempt to leave the-"), never the
  same voice as any character.
- **Headlights on once and they stay on.** Car lights never flicker or toggle unless the story says so.
- **Cliffhanger**: cut to black on the hit, a beat of silence, then a quiet final image (empty seat, a
  voicemail, a click in the dark).

## Cast (humans)
- **Sam** (the director's own character): South Asian man, late 20s, 6 ft, lean ectomorph (narrow
  shoulders, slim arms, flat chest, NOT a bodybuilder), long wavy black shoulder-length hair (not thick),
  centre part, red/wine rectangular glasses ALWAYS on, light stubble, ALWAYS a black oversized hoodie and
  baggy jeans (never shirtless, never skinny jeans). **His face is never shown clearly**: silhouette, back,
  hands, over-the-shoulder, POV, or behind the camcorder. Every attempt at his face (MakeHuman v1-v5, AI
  video) was rejected as "ewy", "terrible", "looks AI". Hands: perfect anatomy, relaxed hands palm to thigh,
  fingers never splayed outward.
- **Akash** (friend 1): voice only in Ep1 (phone + voicemail). ElevenLabs male voice distinct from the radio.
- **Friends 2-3**: placeholders `f1/f2/f3` exist (survivor.py); looks and names not yet set by the director.
- **The rider** (Ep2 side story, "The 43rd Round"): white choppy bob, goggles over a headset, bomber jacket,
  tall tan boots, gloves, bandolier, on the IVORY trike. Built from survivor.py (rider v3.2).

## The car: Night Terror
Sam's black fastback muscle car with a full cabin (`car/nt.glb`, older `Night_Terror_Fastback_v2.glb`).
Local axes: front is -Y, dashboard at y -0.85, driver seat x +0.4, passenger seat x -0.4 (cushion z .83-.95).
In sets it sits at (.4, -2, 0) unrotated; headlight spots just in front of the nose (y -5.65 world when the
root is at (.4,-2)). Grumbling 3-4 L V8 (never an EV whine). Tyres are RUBBER (matte, squashed, sidewall
bulge). Second vehicle: the Bandit armored buggy (military refit, woodland camo) and the IVORY trike.

## Creatures (all original designs; build to these specs)
| creature | design | motion | sound |
|---|---|---|---|
| Walker | MakeHuman base, torn clothes, grey rot | shamble, limp, arms dangle | wet moans (real) |
| Runner | lean, torn, fast | sprint, period .62 s | breath + feet |
| Crawler | long-limbed, belly to ground, hooked claws | crawl, hand plants every .8 s; must be GROUNDED (never sinks) | claw taps on hand plants; director hated the old crawler sound, keep it sparse and real |
| Screamer | gaunt, on rooftops | turns its head toward the window, then screams at the sky (slow-mo allowed once) | real human scream slowed .8 + street echo |
| Husk | grey rotting skeletal, open ribcage, very long arms, hooked fingers, hanging shreds, torn pants, boots | stalk | dry clicks |
| Brute v2 | 2.4 m hulk: SMALL wedge skull sunk forward under a massive hunched back, bony brow plate, knotted crown ridge, wide heavy jaw, torn cheeks with crooked broken fangs, tiny red ember eyes deep in the sockets, dark necrotic skin with wet red cracks, swollen club right arm, few thick dark bone spurs, a shredded hi-vis work vest fused into the flesh (it was a construction worker) | stomp, roar with the jaw | deep roar (slowed .78 + octave sub + throat growl), footfall booms; the car's V8 growls back |
| Stalker (hero monster) | giant, wendigo-like: real dead BULL/cow skull (long, angular, NOT round/popcorn), sharp tapered bone spurs, burnt antlers (left one can snap), stitched mouth that tears open (gums, crooked blade teeth, wet dark interior, saliva strands), ember-vein eyes deep in the sockets with saccades, hunched, long bony arms with clawed hands, digitigrade hooved legs, spine spikes | alive: asymmetric, head leads, follow-through on every chain segment, weight shifts, tremor, staggered impacts | clicks/chitter, a distinct scream to the sky, jaw-locked growls |

Rejected looks to never repeat: "potato" Brute (round bald head, pink skin, cone spikes), "popcorn" round deer
skull, "earthworm" ringed tubes, stick limbs that fold then drop, flat red dot eyes, snake slits, hollow mouth.

## Locations (built in the engine)
- **Penthouse** (pent7.py): NYC high-rise, one wall floor-to-ceiling glass, the real Manhattan night plate
  re-painted in ink style, burning blocks with slow fire + smoke, fire-lit clouds, stars, rain + ash outside,
  leather chair, side table, kitchen with door chain, deadbolt, keys on the counter.
- **Corridor** (cut30): emergency light strobing, neighbour door PH-C ajar with TV flicker and crying, dead
  elevator, EXIT door with push bar, flyers, decals.
- **Pre-war stairwell** (cut40, APPROVED LOOK): marble treads worn in the middle, cast-iron balusters, oak rail
  with ink, hex-tile landings, peeling plaster, brass elevator cage, door 6C open with TV static, hand smears.
- **Lobby** (cut50): brass storefront doors, doorman desk with lamp and phone off the hook, the horde on the
  fire-lit avenue outside (44 rigged + 22 far duplicates + 260 silhouettes), a slap on the glass, B1 PARKING.
- **Garage** (cut60): fluorescent tubes that clunk on one by one, steam, the car revealed headlights OFF.
- **Streets / chase**: wet asphalt with reflections, dead lamps, sedans, rain, runners.
- **Overpass**: the Stalker encounter; practical red ember + fire rim + cold rim + headlight spill.

## Look (the approved recipe)
3D ink realism: physically lit Cycles renders with inverted-hull ink outlines on sets, props, creatures and
the car. Dark frames lit only by practical lights. One palette: cold blue night, sodium orange for fire and
street lamps, red only for blood and eyes. Light film grain only. Camera = a real camcorder or a real rig.
Full numbers in `RULEBOOK.md` T5 and `PLAYBOOK_EP1.md`.

## Episode history
- Ep1 "The Call" (v7, ~96 s): see `PLAYBOOK_EP1.md`.
- Ep2 (dead-roads-ep2 repo): the rider and the trike, roadkill, the truck crash zoom, the Stalker leap.
- Ep3 "Tunnel Vision" (planned): the Night Terror T-bones the Stalker mid-air, the tunnel clearance snaps its
  left antler, abandoned cars with a seated husk in each. Hook "IT NEVER LANDED." No slow-mo.
- Teaser (make-teaser skill): 19 s, the Stalker poster finale.
