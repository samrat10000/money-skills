"""vis_check: is the subject readable in this shot? (RULEBOOK R6.3, gate G4)

Run inside the shot script after the shot is built, or from Blender with a saved blend:
    blender -b shot.blend -P vis_check.py -- --objects "Stalker*,Car*" --frames 1,20,40
Prints, per frame: screen coverage of the subjects' combined bbox (0-1 of frame area), on-screen
fraction, nearest depth, and whether the camera's focus distance is within 15% of the subject depth.
FAIL if coverage < 0.08 (unless the shot is a planned silhouette with a backlight).
"""
import bpy, sys, fnmatch
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

def subjects(patterns):
    return [o for o in bpy.data.objects if o.type in {'MESH', 'CURVE', 'ARMATURE', 'EMPTY'} and any(fnmatch.fnmatch(o.name, p) for p in patterns)
            and o.type != 'EMPTY']

def check(patterns, frames, min_cov=.08):
    sc = bpy.context.scene; cam = sc.camera; ok_all = True
    objs = [o for o in subjects(patterns) if o.type == 'MESH']
    if not objs: print('vis_check: no objects match', patterns); return False
    for f in frames:
        sc.frame_set(f); dg = bpy.context.evaluated_depsgraph_get()
        xs, ys, zs = [], [], []
        for o in objs:
            oe = o.evaluated_get(dg)
            for c in oe.bound_box:
                p = world_to_camera_view(sc, cam, oe.matrix_world @ Vector(c)); xs.append(p.x); ys.append(p.y); zs.append(p.z)
        if max(zs) <= 0: print(f'f{f}: subject behind camera  FAIL'); ok_all = False; continue
        x0, x1 = max(0, min(xs)), min(1, max(xs)); y0, y1 = max(0, min(ys)), min(1, max(ys))
        cov = max(0, x1 - x0) * max(0, y1 - y0)
        full = (max(xs) - min(xs)) * (max(ys) - min(ys)); onscreen = cov / full if full > 0 else 0
        depth = min(z for z in zs if z > 0)
        fd = cam.data.dof.focus_distance if cam.data.dof.use_dof else None
        focus_ok = fd is None or abs(fd - depth) / max(depth, .01) < .15 or fd >= depth
        ok = cov >= min_cov
        ok_all &= ok
        print(f'f{f}: coverage {cov:.3f} on-screen {onscreen:.2f} depth {depth:.2f} m focus {fd} {"PASS" if ok else "FAIL (<%.2f)" % min_cov}{"" if focus_ok else "  FOCUS?"}')
    return ok_all

if __name__ == '__main__':
    argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
    pats = ['*']; frs = [bpy.context.scene.frame_start, bpy.context.scene.frame_end]; mc = .08
    for i, a in enumerate(argv):
        if a == '--objects': pats = argv[i + 1].split(',')
        if a == '--frames': frs = [int(x) for x in argv[i + 1].split(',')]
        if a == '--min': mc = float(argv[i + 1])
    print('RESULT', 'PASS' if check(pats, frs, mc) else 'FAIL')
