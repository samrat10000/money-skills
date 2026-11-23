"""Swap the Stalker's deer skull for the bull skull (bullskull.py) inside the rigged blend, keep body/antlers/rig.
python3 swap_bullskull.py IN.blend OUT.blend [PREVIEW_DIR]   (bpy module)  env SAMP, RES, VIEWS=a,b,c"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy
from mathutils import Vector, Matrix, Euler
import castlib as L, mats as M, bullskull as BS
M.STYLE['cavity'] = True; M.STYLE['cav_kw'] = {'dist': .05, 'strength': .55}
src, dst = sys.argv[1], sys.argv[2]; prev = sys.argv[3] if len(sys.argv) > 3 else None
bpy.ops.wm.open_mainfile(filepath=src)
rig = bpy.data.objects['Stalker rig']; C = rig.users_collection[0]
for n in ('Stalker skull', 'Stalker skull hull', 'Stalker jaw', 'Stalker jaw hull', 'Stalker teeth', 'Stalker eye1', 'Stalker eye-1'):
    if n in bpy.data.objects: bpy.data.objects.remove(bpy.data.objects[n])

HS = 1.5; HR = Euler((math.radians(28), 0, math.radians(-6))).to_matrix()
NK2 = Vector((0, -.52, 2.21))
HO = NK2 - HR @ Vector((0, .095, -.035)) * HS
HM = Matrix.Translation(HO) @ HR.to_4x4() @ Matrix.Scale(HS, 4)
d = BS.build(C)
bone_m, teeth_m, gum_m, hide_m, fl_m, eye_m, emb_m = BS.bone_mat(), BS.teeth_mat(), BS.gum_mat(), BS.hide_mat(), BS.wet_flesh(), BS.ember_eye(), BS.ember_mat()
upper = [(d['skull'], bone_m), (d['teeth'], teeth_m), (d['gums'][0], gum_m), (d['throat'], fl_m), (d['hide'][0], hide_m)] + \
        [(e, eye_m) for e in d['eyes']] + [(e, emb_m) for e in d['embers']]
lower = [(d['jaw'], bone_m), (d['jaw_teeth'], teeth_m), (d['gums'][1], gum_m), (d['tongue'], fl_m), (d['hide'][1], hide_m)]
def bind(o, m, grp):
    o.matrix_world = HM @ o.matrix_world; L.apply_transform(o); L.setmat(o, m)
    vg = o.vertex_groups.new(name=grp); vg.add(list(range(len(o.data.vertices))), 1., 'REPLACE')
    am = o.modifiers.new('Armature', 'ARMATURE'); am.object = rig
    o.parent = rig
for o, m in upper: bind(o, m, 'head')
for o, m in lower: bind(o, m, 'jaw')
for o, grp in ((d['skull'], 'head'), (d['jaw'], 'jaw')):
    h = L.hull(o, C, t=.0022); h.parent = rig
    h.modifiers.clear(); am = h.modifiers.new('Armature', 'ARMATURE'); am.object = rig
print('BULLSKULL in', [o.name for o, _ in upper + lower])
bpy.ops.wm.save_as_mainfile(filepath=dst)

if prev:
    os.makedirs(prev, exist_ok=True); sc = bpy.context.scene
    for o in list(sc.objects):
        if o.type in ('CAMERA', 'LIGHT') or o.name.startswith('floor'): bpy.data.objects.remove(o)
    sc.world = bpy.data.worlds.new('w') if sc.world is None else sc.world
    sc.world.use_nodes = True; sc.world.node_tree.nodes['Background'].inputs['Color'].default_value = (.004, .004, .006, 1)
    def light(n, loc, e, size, col, tgt):
        ld = bpy.data.lights.new(n, 'AREA'); ld.energy = e; ld.size = size; ld.color = col
        lo = bpy.data.objects.new(n, ld); sc.collection.objects.link(lo); lo.location = loc
        lo.rotation_euler = (Vector(tgt) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler(); lo.visible_camera = False
    HC = HM @ Vector((0, -.1, 0))
    light('key', HC + Vector((-1.2, -1.4, .9)), 90, 1.2, (1, .93, .85), HC)
    light('rim', HC + Vector((1.3, 1.0, .6)), 70, .8, (1, .2, .1), HC)
    light('fill', HC + Vector((.8, -1.6, -.6)), 12, 1.5, (.4, .5, 1), HC)
    for sx in (1, -1):                                       # glow inside each socket
        pd = bpy.data.lights.new('sock', 'POINT'); pd.energy = .25; pd.color = (1, .2, .05); pd.shadow_soft_size = .005
        po = bpy.data.objects.new('sock', pd); sc.collection.objects.link(po); po.location = HM @ Vector((.07 * sx, -.047, .012))
    pb = rig.pose.bones['jaw']
    cam = bpy.data.objects.new('cam', bpy.data.cameras.new('cam')); sc.collection.objects.link(cam); sc.camera = cam
    cam.data.lens = 60
    sc.render.engine = 'CYCLES'; sc.cycles.samples = int(os.environ.get('SAMP', '32')); sc.cycles.use_denoising = True
    R = float(os.environ.get('RES', '.5')); sc.render.resolution_x = int(1080 * R); sc.render.resolution_y = int(1350 * R)
    sc.view_settings.view_transform = 'AgX'
    views = {'front34': (Vector((-.55, -.85, .12)), 0), 'side': (Vector((1, -.05, .05)), 0), 'scream': (Vector((-.3, -1, -.35)), 32),
             'eye': (Vector((.85, -.5, .1)), 0)}
    for nm in os.environ.get('VIEWS', 'front34,side,scream,eye').split(','):
        dv, jaw_deg = views[nm]
        pb.rotation_mode = 'XYZ'; pb.rotation_euler = (math.radians(jaw_deg), 0, 0)
        tgt = HC if nm != 'eye' else HM @ Vector((.07, -.047, .012))
        dist = .95 if nm != 'eye' else .32
        cam.location = tgt + dv.normalized() * dist
        cam.rotation_euler = (tgt - cam.location).to_track_quat('-Z', 'Y').to_euler()
        sc.render.filepath = os.path.join(prev, f'{nm}.png'); bpy.ops.render.render(write_still=True)
        print('PREVIEW', nm)
