# MISTAKES: what went wrong and the fix (do not repeat)

| # | Mistake | Director's words / symptom | Fix (now a rule) |
|---|---|---|---|
| 1 | Ep1 v2 drawn by code (pycairo) with a 3D toon character pasted on a 2D BG | "not up to the mark... this will not make me stand out" | One world, one look: everything in the toon cel pipeline, painted BG, comp (PIPELINE) |
| 2 | Story 21 s, too thin | "the story line is not that good... needs to be at least 45-65 sec" | STORY.md skeleton, 45-65 s, hook + escalation + spectacle + stinger |
| 3 | Crow made of primitives | "made of ovals", "wings look cut out", "feet hovering" | Real CC0 rigged model, contact lock, Facing 0.72 rim (R4) |
| 4 | Eye glint as a bone-parent offset | two white dots floating a head-height above the crow | Place the glint each frame from the bones on the camera-facing eye (PIPELINE tricks) |
| 5 | Reach in-between by local slerp, then by IK with a bad pole | the arm swung out sideways, then the elbow jutted | Solve the IK pole numerically, keep the elbow low, check every in-between at full size (R5) |
| 6 | Hood undersized | hood looked tiny | Real garment scale from a reference (R8) |
| 7 | Clothes, roofs, verges, field were plain shapes | "look like they are just made of shapes... depth is missing in the field" | R8 detail list |
| 8 | Rim on the back edge, flat grey light | (self-check) p95 0.58, no glow | Rim only on sun-facing edges, veiling glare, targets p95 0.8-0.95 (R2, R7) |
| 9 | Thin outline vanished at distance | (self-check) | Outline at least 0.00075 x camera distance (R2) |
| 10 | Bare asphalt in the lower third | (self-check) | Road paint, text, grates, leaves, tyre marks (R8) |
| 11 | Handlebar as two rods, a hand resting on top | "Nobody ever grabs a handle like that, and a cycle handle is never like that" | Reference-matched parts, real grip (R4, R8) |
| 12 | Cast scaled down from teen models | the grandma and kids read as teens, the shopkeeper as about 20 | Child proportions, elderly hunch and outfit, middle-age build (CHARACTERS) |
| 13 | Relative Blender outdir | the cels landed in C:\test\ | Always use an absolute outdir (PIPELINE) |
| 14 | Start-Process ExitCode empty | an exit check would fail | `$null = $p.Handle` (ENVIRONMENT) |
| 15 | `git add` of a whole shot folder | 831 render files staged | Commit explicit paths only (ENVIRONMENT) |
| 16 | Files sent as chat attachments | "I can't see them" | Push to GitHub or a private review page and give links (R12) |
| 17 | Showed a compressed preview as the main file | "it shouldn't be degraded" | Full-size PNGs + crf 14 clips (R0) |
| 18 | Music analysed only by loudness | called it an organ drone; the director heard a piano | Detect note attacks; trust the director's ear; say what you can't hear (SOUND) |
| 19 | ColorRamp fed sRGB colours | everything far too light | `lin()` conversion (R2) |
| 20 | Built changes beyond a locked version without asking | (v6 crow experiment) | A locked version changes only with the director's OK. Make experiments as separate files (R11) |
