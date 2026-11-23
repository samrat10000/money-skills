"""LOOK TEST: proves a fresh agent / machine reproduces the Night Terror look in ONE still before any shot.
Builds a dark pre-war corridor corner (worn floor, wainscot wall, door frame, flyer), drops in a cast GLB,
lights it ONLY with practicals (camcorder lamp + one emergency lamp + a far fire glow), puts the ink hull
on everything, renders with the locked recipe (AgX Medium High Contrast, f/4, practical light) and writes
look_test.png. Then compare it side by side with reference/ep1_v7_quality_bar.jpg (LOOK.md section 7).

  blender -b -P scripts/look_test.py -- BLEND=<cast/out/rig/brute/brute.blend> (or GLB=<brute-v2.glb>) OUT=<dir> RES=.5 SAMP=32 [DEVICE=GPU]
  (or: python3 scripts/look_test.py with the `bpy` module, same KEY=VALUE args)
"""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'engine', 'cast'))
args = dict(a.split('=', 1) for a in (sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else sys.argv[1:]) if '=' in a)
import bpy
from mathutils import Vector as V
import castlib as L, mats as M

GLB = args.get('GLB', ''); BLEND = args.get('BLEND', ''); OUT = args.get('OUT', os.path.join(HERE, '..', 'out', 'look_test'))
RES = float(args.get('RES', '.5')); SAMP = int(args.get('SAMP', '32')); DEVICE = args.get('DEVICE', 'CPU')
os.makedirs(OUT, exist_ok=True)

sc = L.reset(); col = L.collection('set')
# ---- the locked render recipe (reference/SHOT_RULES_ep1.md)
sc.view_settings.view_transform = 'AgX'
try: sc.view_settings.look = 'AgX - Medium High Contrast'
except TypeError: sc.view_settings.look = 'Medium High Contrast'
sc.view_settings.exposure = float(args.get('EXPOSURE', '-.5'))
sc.render.resolution_x, sc.render.resolution_y = 1080, 1920; sc.render.resolution_percentage = int(RES * 100)
sc.cycles.samples = SAMP; sc.cycles.use_adaptive_sampling = True; sc.cycles.adaptive_threshold = .05
sc.cycles.use_denoising = True; sc.cycles.max_bounces = 4; sc.cycles.diffuse_bounces = 2; sc.cycles.glossy_bounces = 2
sc.render.filter_size = 1.2
if DEVICE == 'GPU':
    pr = bpy.context.preferences.addons['cycles'].preferences
    for kind in ('OPTIX', 'CUDA', 'HIP', 'METAL'):
        try: pr.compute_device_type = kind; pr.get_devices(); break
        except Exception: pass
    for d in pr.devices: d.use = True
    sc.cycles.device = 'GPU'
w = bpy.data.worlds.new('w'); sc.world = w; w.use_nodes = True
w.node_tree.nodes['Background'].inputs[0].default_value = (0, 0, 0, 1)   # no ambient wash, ever
vs = w.node_tree.nodes.new('ShaderNodeVolumeScatter'); vs.inputs['Density'].default_value = .012   # thin dust/smoke so lamps make beams
w.node_tree.links.new(vs.outputs[0], w.node_tree.nodes['World Output'].inputs['Volume'])

def box(name, loc, size, mat, ink=.006):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.name = name
    o.scale = size; bpy.ops.object.transform_apply(scale=True); L.link(o, col)
    b = o.modifiers.new('bv', 'BEVEL'); b.width = min(.012, min(size) / 3); b.segments = 2
    bpy.ops.object.modifier_apply(modifier='bv'); L.setmat(o, mat)
    if ink: L.hull(o, col, ink)
    return o

floor = M.toon_flat('Floor_worn_tile', '#4a4640', shade='#3a3733', rough=.22, scale=60.)   # wet, so practicals reflect
wall = M.toon_flat('Wall_plaster', '#5b5a4e', shade='#4a4940', rough=.8, scale=40.)
wood = M.toon_flat('Wainscot_oak', '#4a2e1c', shade='#2a190f', rough=.45)
paper = M.toon_flat('Flyer', '#c9c1a6', shade='#8d866f', rough=.9)
box('floor', (0, 0, -.05), (4, 6, .1), floor, ink=0)
box('wall_L', (-1.2, 0, 1.5), (.12, 6, 3), wall)
box('wall_back', (0, 2.6, 1.5), (4, .12, 3), wall)
box('wainscot', (-1.12, 0, .45), (.05, 6, .9), wood, ink=.004)
box('rail', (-1.08, 0, .92), (.07, 6, .05), wood, ink=.003)
for x in (-.45, .45): box('door_jamb', (x + .4, 2.52, 1.05), (.09, .08, 2.1), wood, ink=.004)
box('door_head', (.4, 2.52, 2.13), (1.0, .08, .09), wood, ink=.004)
box('flyer', (-1.13, .4, 1.4), (.01, .22, .3), paper, ink=.002)

# ---- the subject: a cast GLB (ink hull added if it has none), else a placeholder column
subj = []
def ground(objs, y=.9):
    pts = [o.matrix_world @ V(c) for o in objs if o.type == 'MESH' for c in o.bound_box]
    mz = min(p.z for p in pts)
    for r in {o for o in objs if o.parent is None}: r.location += V((0, y, -mz))
if BLEND and os.path.exists(BLEND):          # PREFERRED: the rig .blend keeps the full procedural materials
    with bpy.data.libraries.load(BLEND) as (src, dst): dst.collections = [c for c in src.collections]
    for c in dst.collections:
        sc.collection.children.link(c)
        for o in list(c.all_objects):
            if o.type in ('LIGHT', 'CAMERA'): bpy.data.objects.remove(o)
    subj = [o for c in dst.collections for o in c.all_objects]; bpy.context.view_layer.update(); ground(subj)
elif GLB and os.path.exists(GLB):            # viewer GLB: baked textures, flatter; fine for blocking only
    bpy.ops.import_scene.gltf(filepath=GLB)
    subj = [o for o in bpy.context.selected_objects if o.type == 'MESH']
    for o in subj: L.link(o, col)
    if not any('hull' in o.name.lower() or any(m.material and 'ink' in m.material.name.lower() for m in o.material_slots) for o in subj):
        for o in list(subj): L.hull(o, col, .004)
    ground(list(bpy.context.selected_objects))
else:
    box('placeholder', (0, .9, .9), (.5, .4, 1.8), M.zombie_skin('Skin_test'), ink=.005)

# ---- practical light only
cam_d = bpy.data.cameras.new('cam'); cam = bpy.data.objects.new('cam', cam_d); col.objects.link(cam); sc.camera = cam
cam.location = (.6, -4.6, 1.6); cam_d.lens = 30; cam_d.sensor_fit = 'VERTICAL'
d = V((0, .9, 1.45)) - cam.location; cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
cam_d.dof.use_dof = True; cam_d.dof.aperture_fstop = 4.0; cam_d.dof.focus_distance = d.length
lamp = bpy.data.lights.new('camcorder_lamp', 'SPOT'); lamp.energy = 28; lamp.spot_size = math.radians(72)
lamp.spot_blend = .5; lamp.color = L.lin('#ffd9a8'); lamp.shadow_soft_size = .02
lo = bpy.data.objects.new('camcorder_lamp', lamp); col.objects.link(lo); lo.parent = cam; lo.location = (.06, -.05, 0)
em = bpy.data.lights.new('emergency', 'POINT'); em.energy = 70; em.color = L.lin('#ff3b22'); em.shadow_soft_size = .05
eo = bpy.data.objects.new('emergency', em); col.objects.link(eo); eo.location = (-.9, 2.2, 2.7)
fire = bpy.data.lights.new('fire_through_door', 'AREA'); fire.energy = 120; fire.size = .9; fire.color = L.lin('#ff8a3c')
fo = bpy.data.objects.new('fire', fire); col.objects.link(fo); fo.location = (.4, 3.6, 1.2); fo.rotation_euler = (math.radians(90), 0, 0)

# a fluorescent tube that exists in the set (visible fixture + its light), hung just in front of the subject
tube = box('tube_fixture', (.1, -.2, 2.75), (.08, 1.2, .05), M.flat('Tube_emit', '#e8f0ff', emit=1.2), ink=0)
tl = bpy.data.lights.new('tube_light', 'AREA'); tl.shape = 'RECTANGLE'; tl.size = .08; tl.size_y = 1.2
tl.energy = 60; tl.color = L.lin('#dfe8ff'); to = bpy.data.objects.new('tube_light', tl); col.objects.link(to); to.location = (.1, -.2, 2.7)
sc.render.filepath = os.path.join(OUT, 'look_test.png')
bpy.ops.render.render(write_still=True)
print('LOOK_TEST', sc.render.filepath)
