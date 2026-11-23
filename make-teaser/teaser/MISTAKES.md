# MISTAKES: the iteration history behind the rules

Night Terror: Dead Roads poster teaser, 2026-11-21 to 2026-11-23. Each line: what was shown -> what
the director said -> root cause -> rule. Read once; these are the traps a fresh model falls into.

| # | Version | Director's note | Root cause | Rule |
|---|---|---|---|---|
| 1 | plan v1 | "You took the wrong poster, the reindeer one is the main" | assumed which poster | R1.4 |
| 2 | render | 12 min/frame overnight, "too slow" | one long Blender process, persistent data, VRAM growth | R9.2 |
| 3 | 910 v1 | (self-caught) eye shot was a blurry skull | camera aimed between the eyes, at bone | R3.5 |
| 4 | 909/910/912 | skull "round, like popcorn", "squarish teeth", "conical teeth", eye "just a red dot", "no snake eye" | primitive unions, uniform teeth, flat emission | R4.3-R4.5 |
| 5 | skull v3 | "make it sharper at the end, not round" (pinned 3 spots) | rounded bone caps | R4.3 |
| 6 | skull | hide patches read as cow-print spots; tongue looked chrome/lilac | wrong materials | R4.4, R4.6 |
| 7 | 911 v1 | "you're just moving the skull, move the arms and legs"; skid "more realistic" | only head keys; skid stopped dead | R5.2, R5.8 |
| 8 | 902-908 v1 | (self-caught) giant, Brute, glass, slab not visible | fog disabled for speed; subjects 4% of frame; prop key bug | R6.3, R6.4 |
| 9 | Asus slow | 3-12 min/frame | VRAM full (browser + scene), not throttling | R9.2 |
| 10 | 911 v2 | "the mouth opens backward"; "moving its hands up and down like a machine, both at a time"; "realism totally missing" | jaw hinge guessed from geometry; one curve for both arms; only end bones rotated | R5.1, R5.2, R5.5 |
| 11 | 910 v3 | "fabulous, this is the realism I want in 911" | (success: ember-vein eye + saccades) | R4.5, R5.6 |
| 12 | teaser v1 | "music is cutting in between, should flow" | score cut per shot | R7.1 |
| 13 | teaser v1 | at 6-7 s "the car stops, then the other scene starts moving" | Bezier ease between two keys; no speed match | R5.7 |
| 14 | teaser v1 | "at the 11th second there is a black screen, total off" | black spacer before hero | R2.4 |
| 15 | teaser v1 | "hold the glitch ending 2 seconds longer" | stinger too short to register | R2.5 |
| 16 | teaser v1 | arms "a proper fold and then it drops like sticks", "looks funny"; wanted wendigo-style monster | stick-blade limbs, no hands | R4.1, R4.2 |
| 17 | teaser v1 | "no background music, exact real sounds... drifting you always do wrong... $1 billion sound effects... pin-drop trailer opening" | music bed; weak synthetic drift | R7.1, R7.2, R7.5, R2.1 |
| 18 | Stalker v4 | "shoulders could improve, these red spikes look fake" | decorative spikes | R4.6, R4.2 |
| 19 | sound v2 | "weird sound in the first second" | spring "boing" sample as the ping | R2.1 |
| 20 | sound v2 | "someone moaning at 6 s"; "the roar comes a lot later than the mouth" | pitched-down breath; clips placed by file start | R7.3, R7.4 |
| 21 | final v1 | "5 s and 6 s car shots: it stops then runs at full speed"; "car sounds can be even better" | eased keys again in 905; thin car sound | R5.7, R7.5 |
| 22 | final v1 | "tyre hiss must be crazy, not code sounds" | synthesised hiss | R7.2 |
| 23 | delivery | 42 MB file "too large to preview", no download button on phone | attachment only | R8.3 |
| 24 | Ep1 | "too much grain, black dots" | Voronoi glass bump, low spp, speckled textures | R6.6, R6.7 |
| 25 | Ep1 v6 | three looks mixed; reused shots with known problems; voices overlapping | no look lock; no note re-check | R6.1, R8.5, R7.9 |
| 26 | Ep1 | MakeHuman and AI-video humans rejected ("looks AI") | wrong approach for humans | R4.7 |
| 27 | final v2 | "absolutely crazy", "Perfect sound" | all of the above applied | (the bar) |

Approved and loved (keep doing): puddle macro opening, lightning silhouette, windshield POV with the
giant, crash zoom ("so damn good"), eye ECU with saccades ("crazy"), hero skid ("perfect shot"), VHS
glitch stinger ("crazy, perfect"), shot numbers in names, per-shot clips with critique.

Process lessons: confirm the hero first; probe before every full render; check frame counts after
every transfer; write to a new filename and verify md5 after copying to another machine; render in the
cloud in parallel when the PC is offline; send one finished version, not a string of tests.
