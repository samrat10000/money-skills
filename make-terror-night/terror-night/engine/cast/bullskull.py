"""Stalker head v2: a dead BULL skull (Sam 2026-11-22): broad flat frontal shield, poll crest, orbits flared out
to the sides, long narrow face, open nasal notch, thin premaxilla prongs. Wrongness that makes it scary:
splintered blade teeth (no square molars, no clean cones) erupting where cattle have none, roots exposed through
eroded bone, shrunken dried gums, tatters of dried hide, a cracked forehead, deep sockets with ember eyes.
Local space like skull.py: origin at the cranium centre, snout toward -Y, top +Z. Antler pedicles at (+-.036, .012, .066)."""
import math, random
import bpy, bmesh
from mathutils import Vector, noise
import castlib as L, mats as M
V = lambda *a: Vector(a[0] if len(a) == 1 else a)

def _bool(o, cutter, op='DIFFERENCE'):
    m = o.modifiers.new('b', 'BOOLEAN'); m.operation = op; m.object = cutter; m.solver = 'EXACT'
    L.apply_all(o); bpy.data.objects.remove(cutter)

def _remesh(o, vs, it=3):
    r = o.modifiers.new('rm', 'REMESH'); r.mode = 'VOXEL'; r.voxel_size = vs
    if it:
        s = o.modifiers.new('sm', 'SMOOTH'); s.factor = .5; s.iterations = it
    L.apply_all(o)

def _ring(name, c, nrm, r, t, col, n=28):
    nrm = V(nrm).normalized(); up = V(0, 0, 1) if abs(nrm.z) < .9 else V(1, 0, 0)
    a = nrm.cross(up).normalized(); b = nrm.cross(a).normalized()
    pts = [V(c) + (a * math.cos(2 * math.pi * k / n) + b * math.sin(2 * math.pi * k / n)) * r for k in range(n + 1)]
    return L.tube(name, pts, [t] * len(pts), col, sides=10, cap=False)

def blade_tooth(name, col, root, tip_dir, length, width, rng, rootlen=.012, curve=(0, 0, 0), broken=False, thin_axis=(1, 0, 0)):
    """a flattened, slightly curved, chipped blade tooth with a long exposed root. Not a cone: lens-shaped section,
    uneven edges, crooked tip; broken ones end in a jagged stump."""
    d = V(tip_dir).normalized(); cv = V(curve)
    pts, rr = [], []
    n = 9
    for i in range(n):
        t = i / (n - 1)
        s = -rootlen + (length + rootlen) * t                 # root starts above the gum line, inside the bone
        p = V(root) + d * s + cv * (max(t - .35, 0) ** 2) * length * 2.2
        pts.append(p)
        if broken and t > .62: r = width * .55 * (1 + .25 * rng.uniform(-1, 1))
        else: r = width * (.75 + .35 * math.sin(min(t, .5) * math.pi)) * (1 - t ** 1.6) + .00035
        rr.append(r)
    if broken: pts, rr = pts[:7], rr[:7]
    o = L.tube(name, pts, rr, col, sides=10)
    ta = V(thin_axis).normalized()
    for v in o.data.vertices:                                   # lens section: squash across the jaw, keep width along it
        # nearest axis point
        k = min(range(len(pts)), key=lambda j: (v.co - pts[j]).length)
        off = v.co - pts[k]
        along = off.dot(ta)
        v.co = pts[k] + off - ta * along * .58
        v.co += V(rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(-1, 1)) * width * .06   # chips, uneven enamel
    return o

def build(col, seed=13):
    rng = random.Random(seed)
    P = []
    # ---------------------------------------------------------------- one lofted mass: cranium -> orbits -> long tapering face (no separate "finger" bones)
    import bmesh as _bm
    def prof(y):
        # half width, top z, bottom z along the skull (poll at +y, nose tip at -y)
        k = [(.075, .046, .056, -.02), (.05, .058, .06, -.05), (.0, .056, .058, -.052), (-.05, .064, .052, -.05), (-.09, .066, .046, -.048),
             (-.13, .05, .036, -.046), (-.19, .04, .024, -.044), (-.25, .03, .012, -.041), (-.285, .024, .004, -.04), (-.3, .012, -.008, -.034)]
        for (y0, *a0), (y1, *a1) in zip(k, k[1:]):
            if y1 <= y <= y0:
                t = (y0 - y) / (y0 - y1); t = t * t * (3 - 2 * t)
                return [a0[i] + (a1[i] - a0[i]) * t for i in range(3)]
        return k[-1][1:] if y < k[-1][0] else k[0][1:]
    bm = _bm.new(); rings = []; NS = 40; NY = 60
    for j in range(NY + 1):
        y = .075 - (.4 * j / NY); hw, zt, zb = prof(y); zc = (zt + zb) / 2; hh = (zt - zb) / 2
        ring = []
        for i in range(NS):
            th = 2 * math.pi * i / NS; c, s_ = math.cos(th), math.sin(th)
            ex = 3.2 if s_ > 0 else 2.2                                            # flat top, narrower rounded underside
            x = hw * math.copysign(abs(c) ** (2 / ex), c) * (1 if s_ > 0 else .82)
            z = zc + hh * math.copysign(abs(s_) ** (2 / ex), s_)
            # orbit flare: the upper side walls kick out hard around the orbits (cow skull silhouette from the front)
            fl = .022 * math.exp(-((y + .088) / .02) ** 2) * max(0., min(1., (s_ + .1) / .6)) * max(0., abs(c) - .2) / .8
            x += math.copysign(fl, c)
            ring.append(bm.verts.new((x, y, z)))
        rings.append(ring)
    for j in range(NY):
        for i in range(NS):
            bm.faces.new((rings[j][i], rings[j][(i + 1) % NS], rings[j + 1][(i + 1) % NS], rings[j + 1][i]))
    bm.faces.new(list(reversed(rings[0]))); bm.faces.new(rings[-1])
    P.append(L.mesh_obj('f loft', bm, col))
    P.append(L.tube('f poll', [(-.092, .078, .024), (-.066, .066, .032), (-.03, .072, .05), (0, .077, .06), (.03, .072, .05), (.066, .066, .032), (.092, .078, .024)],
                    [.0008, .012, .02, .022, .02, .012, .0008], col, sides=14))              # poll corners end in sharp spurs
    for sx in (1, -1):
        P.append(L.tube(f'fcrest{sx}', [(.05 * sx, -.115, -.008), (.044 * sx, -.16, -.014), (.034 * sx, -.21, -.02)], [.003, .0045, .002], col, sides=8))
        P.append(L.tube(f'zyg{sx}', [(.056 * sx, -.13, -.014), (.066 * sx, -.1, -.02), (.068 * sx, -.05, -.026), (.062 * sx, .01, -.03), (.056 * sx, .05, -.034), (.054 * sx, .072, -.04)],
                        [.0008, .007, .009, .008, .005, .0008], col, sides=10))
        P.append(L.tube(f'tub{sx}', [(.036 * sx, -.14, -.026), (.046 * sx, -.15, -.034), (.054 * sx, -.158, -.044)], [.008, .004, .0007], col, sides=8))
        P.append(L.tube(f'ped{sx}', [(.03 * sx, .0, .036), (.036 * sx, .012, .066)], [.017, .015], col, sides=12))
        # bare premaxilla: two thin bony prongs forming a split beak (cattle have no upper front teeth), sharp tips
        P.append(L.tube(f'pmx{sx}', [(.018 * sx, -.25, -.034), (.017 * sx, -.29, -.04), (.011 * sx, -.322, -.043), (.005 * sx, -.345, -.042)],
                        [.0075, .006, .0035, .0006], col, sides=10))
        # nasal bones end in two points overhanging the nasal opening
        P.append(L.tube(f'nas{sx}', [(.01 * sx, -.2, .016), (.009 * sx, -.25, .01), (.006 * sx, -.285, .006)], [.008, .005, .0006], col, sides=8))
    skull = L.join(P, 'Stalker skull'); _remesh(skull, .0018, 3)
    # ---------------------------------------------------------------- cavities
    for sx in (1, -1):
        _bool(skull, L.blob('c', (.071 * sx, -.089, .019), (.018, .018, .018), col, seg=32, ring=24))          # deep orbit
        _bool(skull, L.blob('c', (.058 * sx, -.02, .0), (.012, .03, .018), col))                               # temporal fossa
        _bool(skull, L.blob('c', (.03 * sx, -.245, -.012), (.016, .06, .016), col, seg=32, ring=24))           # nasal notch (side)
        _bool(skull, L.blob('c', (.022 * sx, -.06, .056), (.004, .006, .006), col))                            # supraorbital foramen
        _bool(skull, L.blob('c', (.047 * sx, -.13, -.042), (.011, .06, .008), col))                            # eroded alveolar bone: roots show
    _bool(skull, L.blob('c', (0, -.27, -.006), (.016, .05, .014), col))                                        # nasal cavity
    _bool(skull, L.blob('c', (.026, -.035, .055), (.011, .016, .02), col, rot=(0, .4, .5)))                       # punched-in forehead hole
    # ---------------------------------------------------------------- bone surface: pitting, sutures, fracture lines, weathering
    cr = [(V(.026, -.035, .055), V(-.4, -1, .1)), (V(.026, -.035, .055), V(.3, 1, .05)), (V(-.02, .03, .05), V(-.6, -1, 0))]
    for v in skull.data.vertices:
        p = v.co
        d = .0007 * noise.noise(p * 150) + .0013 * noise.noise(p * 40) + .0006 * noise.noise(p * V(20, 260, 20))
        d -= .0011 * max(0, 1 - abs(noise.noise(p * 24 + V(3, 1, 0))) * 13)            # sutures
        for c0, cd in cr:                                                                  # cracks radiating from the hole
            q = p - c0; cdn = cd.normalized(); along = q.dot(cdn)
            if 0 < along < .09:
                perp = (q - cdn * along).length + .002 * noise.noise(p * 300)
                d -= .0016 * max(0, 1 - perp / .0011) * (1 - along / .09)
        v.co = p + v.normal * d
    L.smooth(skull)

    # ---------------------------------------------------------------- lower jaw: long thin mandible bars, tall ramus to the joint
    jp = []
    for sx in (1, -1):
        mt = (L.tube(f'mand{sx}', [(.052 * sx, .048, -.03), (.054 * sx, .045, -.06), (.048 * sx, .015, -.08), (.04 * sx, -.06, -.078),
                                       (.03 * sx, -.15, -.072), (.016 * sx, -.23, -.066), (.006 * sx, -.29, -.06)],
                         [.011, .014, .013, .011, .009, .006, .002], col, sides=14))
        for v in mt.data.vertices:                                      # a tall thin vertical plate, not a round bar
            cx = (.052 if v.co.y > .03 else .052 - (.03 - v.co.y) * .16) * sx
            v.co.x = cx + (v.co.x - cx) * .5
            if v.co.y < .02: v.co.z = -.072 + (v.co.z + .072) * 1.7
        jp.append(mt)
        jp.append(L.tube(f'angle{sx}', [(.052 * sx, .03, -.072), (.055 * sx, .06, -.088), (.057 * sx, .084, -.106)], [.012, .005, .0007], col, sides=10))  # hooked angular spur
        jp.append(L.tube(f'coro{sx}', [(.05 * sx, .03, -.04), (.049 * sx, .02, -.018), (.047 * sx, .012, .004)], [.007, .004, .0007], col, sides=8))       # coronoid point
    jaw = L.join(jp, 'Stalker jaw'); _remesh(jaw, .0019, 3)
    _bool(jaw, L.blob('c', (.044, -.08, -.066), (.012, .05, .006), col))
    _bool(jaw, L.blob('c', (-.042, -.1, -.065), (.011, .04, .006), col))
    for v in jaw.data.vertices: v.co += v.normal * (.0008 * noise.noise(v.co * 130) + .0008 * noise.noise(v.co * 40))
    L.smooth(jaw)

    # ---------------------------------------------------------------- teeth: crooked splintered blades, irregular rows
    up, lo = [], []
    # upper: irregular, crowded, overlapping blades of very different sizes; two big hooked fangs per side; broken stumps between
    ys = [-.03, -.045, -.06, -.075, -.092, -.106, -.12, -.137, -.152, -.168, -.184, -.2, -.218, -.236, -.256, -.278, -.298]
    for sx in (1, -1):
        for i, y in enumerate(ys):
            if rng.random() < .08: continue
            t = i / (len(ys) - 1)
            x = (.034 - .014 * t) * sx + rng.uniform(-.0025, .0025)
            fang = i in (5, 12)
            ln = .05 + rng.uniform(0, .012) if fang else .012 + .018 * rng.random() ** 1.5 + .008 * t
            w = .0075 if fang else .0048 + .0022 * rng.random()
            dirv = V((.3 if fang else .18) * sx + rng.uniform(-.18, .18), rng.uniform(-.35, .2) + (.25 if fang else 0), -1)
            up.append(blade_tooth(f'tu{sx}{i}', col, (x, y + rng.uniform(-.003, .003), -.04), dirv, ln, w, rng, rootlen=.016,
                                  curve=(0, .12 if fang else rng.uniform(-.04, .1), 0), broken=(not fang) and rng.random() < .25))
    # lower: crowded crooked row, a few long ones rising outside the upper jaw, and a forward-raking comb at the chin
    yl = [-.02, -.036, -.052, -.068, -.083, -.098, -.114, -.13, -.146, -.162, -.178, -.195, -.212, -.23, -.25, -.268]
    for sx in (1, -1):
        for i, y in enumerate(yl):
            if rng.random() < .08: continue
            t = i / (len(yl) - 1)
            x = (.036 - .02 * t) * sx + rng.uniform(-.002, .002)
            big = i in (3, 10)
            ln = .04 + rng.uniform(0, .01) if big else .01 + .016 * rng.random() ** 1.4 + .006 * t
            dirv = V((.35 if big else .15) * sx + rng.uniform(-.15, .15), rng.uniform(-.15, .3), 1)
            lo.append(blade_tooth(f'tl{sx}{i}', col, (x, y, -.064 + .003 * t), dirv, ln, .0068 if big else .0045 + .0018 * rng.random(), rng,
                                  rootlen=.012, curve=(0, -.1 if big else -.04, 0), broken=(not big) and rng.random() < .22))
        for k in range(3):
            x = (.005 + k * .007) * sx
            lo.append(blade_tooth(f'tc{sx}{k}', col, (x, -.284 + k * .008, -.058), V(.15 * sx * k, -1, .45 + .15 * rng.uniform(-1, 1)),
                                  .028 + rng.uniform(-.004, .012), .0055, rng, rootlen=.01, curve=(0, 0, .07), broken=rng.random() < .3,
                                  thin_axis=(0, 0, 1)))
    teeth_up = L.join(up, 'Stalker teeth'); teeth_lo = L.join(lo, 'Stalker jaw teeth')

    # ---------------------------------------------------------------- shrunken dried gums along both rows
    gu, gl = [], []
    for sx in (1, -1):
        gu.append(L.tube(f'gu{sx}', [((.034 - .014 * (y / -.298)) * sx, y, -.041) for y in ys], [.0048] * len(ys), col, sides=10))
        gl.append(L.tube(f'gl{sx}', [((.036 - .02 * (y / -.268)) * sx, y, -.064) for y in yl], [.0046] * len(yl), col, sides=10))
    gums_up = L.join(gu, 'Stalker teeth gum'); gums_lo = L.join(gl, 'Stalker jaw gum')
    for o in (gums_up, gums_lo):
        _remesh(o, .0015, 2)
        for v in o.data.vertices: v.co += v.normal * .0018 * noise.noise(v.co * 160)

    # ---------------------------------------------------------------- mouth inside: no hollow mouth. dark palate/throat + rotting tongue
    throat = L.blob('Stalker skull throat', (0, -.06, -.036), (.026, .1, .008), col)
    tongue = L.blob('Stalker jaw tongue', (0, -.08, -.068), (.012, .08, .004), col)
    for v in tongue.data.vertices: v.co.z += .003 * math.sin(v.co.y * 60) + .002 * noise.noise(v.co * 90)

    # ---------------------------------------------------------------- tatters of dried hide clinging to the back of the skull and the jaw hinge
    def tatters(src, name, region, thr, push):
        h = L.dup(src, name, col)
        L.keep_verts(h, lambda p: region(p) and noise.noise(p * 34 + V(7, 2, 1)) > thr)
        for v in h.data.vertices: v.co += v.normal * push
        s = h.modifiers.new('so', 'SOLIDIFY'); s.thickness = .0011; s.offset = 1
        L.apply_all(h)
        for v in h.data.vertices: v.co += v.normal * .0008 * noise.noise(v.co * 200)
        return h
    skin_s = tatters(skull, 'Stalker skull hide', lambda p: p.y > .03 and p.z < .0, .2, .0012)
    skin_j = tatters(jaw, 'Stalker jaw hide', lambda p: p.y > -.01, .25, .0011)

    # ---------------------------------------------------------------- eyes: wet orbs sunk deep in the sockets
    eyes = []
    for sx in (1, -1):
        e = L.blob(f'Stalker eye{sx}', (.057 * sx, -.089, .018), (.0085, .0085, .0085), col, seg=32, ring=24)
        eyes.append(e)
    # a faint ember deep in the forehead hole and nasal cavity, as if something burns inside the skull
    embers = [L.blob('Stalker skull ember', (.022, -.035, .044), (.007, .01, .008), col),
              L.blob('Stalker skull ember.n', (0, -.265, -.012), (.008, .03, .006), col)]
    return {'skull': skull, 'jaw': jaw, 'teeth': teeth_up, 'jaw_teeth': teeth_lo, 'gums': [gums_up, gums_lo],
            'throat': throat, 'tongue': tongue, 'hide': [skin_s, skin_j], 'eyes': eyes, 'embers': embers,
            'orbits': [V(.071 * sx, -.089, .019) for sx in (1, -1)]}

# ---------------------------------------------------------------- materials
def bone_mat(name='Stalker_Bone2'):
    b = M.NB(name)
    n = b.noise(30, 6, .6); n2 = b.noise(6, 4, .6, vec=b.mapping(loc=(3, 3, 3)))
    c = b.ramp(n, [(.25, M.C('#8a7656')), (.55, M.C('#c9b892')), (.8, M.C('#e2d6b8'))])
    c = b.mix(b.mr(n2, .5, .72), c, M.C('#4a2a1c'))                                  # weathering / old blood stains
    c = b.mix(b.mr(b.noise(90, 3, .6), .6, .75, 0, .35), c, M.C('#2b1a12'))          # grime in the pores
    b.bump(n, .35, .001); b.bump(b.noise(220, 3, .6), .15, .0004)
    return b.finish(c, rough=.62)

def teeth_mat(name='Stalker_Teeth2'):
    b = M.NB(name)
    sep = b.node('ShaderNodeSeparateXYZ'); b.link(b.co, sep.inputs[0])
    n = b.noise(160, 4, .6)
    c = b.ramp(n, [(.3, M.C('#7c6440')), (.6, M.C('#b89f6c')), (.85, M.C('#d8c69a'))])
    c = b.mix(b.mr(b.noise(25, 4, .6), .45, .7), c, M.C('#3a2414'))                  # rot stains toward the roots
    b.bump(n, .3, .0005)
    m = b.finish(c, rough=.32, spec=.55)
    return m

def gum_mat(name='Stalker_Gum'):
    b = M.NB(name)
    n = b.noise(80, 6, .65)
    c = b.ramp(n, [(.3, M.C('#140608')), (.6, M.C('#3a1216')), (.85, M.C('#5e2a22'))])
    b.bump(n, .5, .001)
    return b.finish(c, rough=.38, spec=.5)

def hide_mat(name='Stalker_Hide'):
    b = M.NB(name)
    n = b.noise(55, 7, .7); v = b.voronoi(120)
    c = b.ramp(n, [(.3, M.C('#120a08')), (.55, M.C('#2e1c14')), (.8, M.C('#4a3122'))])
    b.bump(n, .6, .0012); b.bump(v, .25, .0005)
    return b.finish(c, rough=.7)

def wet_flesh(name='Stalker_Throat'):
    b = M.NB(name)
    n = b.noise(60, 6, .6)
    w = b.noise(140, 4, .6)
    c = b.ramp(n, [(.3, M.C('#0c0304')), (.65, M.C('#2e0a0c')), (.9, M.C('#4a1616'))])     # rotting, wrinkled flesh, not chrome
    b.bump(n, .7, .002); b.bump(w, .4, .0006)
    return b.finish(c, rough=.45, spec=.3, cav=True)

def ember_eye(name='Stalker_Eye2', strength=3.):
    """not a flat red dot: a wet black orb split by glowing vein-cracks around a burning core"""
    m = bpy.data.materials.new(name); m.use_nodes = True; nt = m.node_tree; N = nt.nodes; Lk = nt.links
    bs = N.get('Principled BSDF')
    bs.inputs['Base Color'].default_value = (.01, .004, .004, 1); bs.inputs['Roughness'].default_value = .04
    bs.inputs['Coat Weight'].default_value = 1.; bs.inputs['Coat Roughness'].default_value = .02
    tc = N.new('ShaderNodeTexCoord')
    vo = N.new('ShaderNodeTexVoronoi'); vo.feature = 'DISTANCE_TO_EDGE'; vo.inputs['Scale'].default_value = 5.
    nz = N.new('ShaderNodeTexNoise'); nz.inputs['Scale'].default_value = 3.; nz.inputs['Detail'].default_value = 6.
    Lk.new(tc.outputs['Generated'], nz.inputs['Vector'])
    mv = N.new('ShaderNodeVectorMath'); mv.operation = 'MULTIPLY_ADD'; Lk.new(nz.outputs['Color'], mv.inputs[0]); mv.inputs[1].default_value = (.35, .35, .35)
    Lk.new(tc.outputs['Generated'], mv.inputs[2])
    Lk.new(mv.outputs[0], vo.inputs['Vector'])
    cr = N.new('ShaderNodeMapRange'); cr.inputs['From Min'].default_value = 0.; cr.inputs['From Max'].default_value = .025
    cr.inputs['To Min'].default_value = 1.; cr.inputs['To Max'].default_value = 0.; Lk.new(vo.outputs['Distance'], cr.inputs['Value'])
    # burning core: brighter toward the eye's facing side (object +-X)
    sep = N.new('ShaderNodeSeparateXYZ'); Lk.new(tc.outputs['Generated'], sep.inputs[0])
    sub = N.new('ShaderNodeMath'); sub.operation = 'SUBTRACT'; Lk.new(sep.outputs['X'], sub.inputs[0]); sub.inputs[1].default_value = .5
    ab = N.new('ShaderNodeMath'); ab.operation = 'ABSOLUTE'; Lk.new(sub.outputs[0], ab.inputs[0])
    core = N.new('ShaderNodeMapRange'); core.inputs['From Min'].default_value = .44; core.inputs['From Max'].default_value = .5
    core.inputs['To Min'].default_value = 0.; core.inputs['To Max'].default_value = 1.; Lk.new(ab.outputs[0], core.inputs['Value'])
    mx = N.new('ShaderNodeMath'); mx.operation = 'MAXIMUM'; Lk.new(cr.outputs[0], mx.inputs[0]); Lk.new(core.outputs[0], mx.inputs[1])
    ramp = N.new('ShaderNodeValToRGB'); Lk.new(mx.outputs[0], ramp.inputs['Fac'])
    e = ramp.color_ramp.elements; e[0].position = .0; e[0].color = (0, 0, 0, 1); e[1].position = 1.; e[1].color = (1., .32, .06, 1)
    mid = e.new(.45); mid.color = (.45, .02, .01, 1)
    Lk.new(ramp.outputs['Color'], bs.inputs['Emission Color']); bs.inputs['Emission Strength'].default_value = strength
    return m

def ember_mat(name='Stalker_Ember', strength=3.):
    return L.mat_flat(name, L.lin('#ff3a10'), rough=.5, emit_s=strength)
