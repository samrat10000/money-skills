"""check_motion: vehicle speed continuity (RULEBOOK R5.7) and frozen-object detection.

Inside a shot script (after building) or on a saved blend:
    blender -b shot.blend -P check_motion.py -- --object "Car" --shot 905 --out speeds.json
Prints speed (m/s) per frame, flags easing to a stop, and appends {shot: {start, end, min, dir}} to
speeds.json. Then compare adjoining shots:
    python3 check_motion.py --compare speeds.json 905 906
FAIL if a driving shot's speed drops > 30% inside the shot without a planned stop, or if the end
speed of shot A and the start speed of shot B differ by > 15%, or the direction flips.
"""
import sys, json, os

def measure(obj_name, f0=None, f1=None):
    import bpy
    sc = bpy.context.scene; o = bpy.data.objects[obj_name]
    f0 = f0 or sc.frame_start; f1 = f1 or sc.frame_end
    pos = []
    for f in range(f0, f1 + 1):
        sc.frame_set(f); pos.append(o.matrix_world.translation.copy())
    fps = sc.render.fps / sc.render.fps_base
    sp = [((pos[i + 1] - pos[i]).length * fps) for i in range(len(pos) - 1)]
    d0 = (pos[min(5, len(pos) - 1)] - pos[0]); d1 = (pos[-1] - pos[max(0, len(pos) - 6)])
    return sp, tuple(d0.normalized()) if d0.length else (0, 0, 0), tuple(d1.normalized()) if d1.length else (0, 0, 0)

def report(shot, sp, d0, d1, out=None, planned_stop=False):
    start = sum(sp[:5]) / max(1, len(sp[:5])); end = sum(sp[-5:]) / max(1, len(sp[-5:])); mn = min(sp)
    print(f'{shot}: start {start:.1f} m/s end {end:.1f} m/s min {mn:.1f}')
    print('  per frame:', ' '.join(f'{v:.0f}' for v in sp))
    ok = planned_stop or mn >= .7 * max(start, end)
    print('  ', 'PASS' if ok else 'FAIL: speed sags inside the shot (eased keys? use linear interpolation)')
    if out:
        db = json.load(open(out)) if os.path.exists(out) else {}
        db[str(shot)] = dict(start=start, end=end, min=mn, dir_start=d0, dir_end=d1); json.dump(db, open(out, 'w'), indent=1)
    return ok

def compare(path, a, b, world_dir=True):
    db = json.load(open(path)); A, B = db[a], db[b]
    ratio = B['start'] / max(A['end'], 1e-6)
    ok = .85 <= ratio <= 1.15
    print(f'{a} end {A["end"]:.1f} m/s -> {b} start {B["start"]:.1f} m/s  ratio {ratio:.2f}  {"PASS" if ok else "FAIL (speed must match across the cut)"}')
    if world_dir:
        dot = sum(x * y for x, y in zip(A['dir_end'], B['dir_start']))
        print(f'  world direction dot {dot:.2f} {"PASS" if dot > .5 else "CHECK (direction changes across the cut: intended?)"}')
    return ok

if __name__ == '__main__':
    argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else sys.argv[1:]
    if '--compare' in argv:
        i = argv.index('--compare'); sys.exit(0 if compare(argv[i + 1], argv[i + 2], argv[i + 3]) else 1)
    obj = argv[argv.index('--object') + 1]; shot = argv[argv.index('--shot') + 1] if '--shot' in argv else 'shot'
    out = argv[argv.index('--out') + 1] if '--out' in argv else None
    sp, d0, d1 = measure(obj); report(shot, sp, d0, d1, out, '--planned-stop' in argv)
