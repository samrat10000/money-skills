"""motion_lib: make creatures move like living things (RULEBOOK R5). Pure Python + bpy for keying.

Extracted from the approved Night Terror Stalker (reference/night_terror/teaser_shots.py, stalker_body
and eye_saccades). Import inside your shot script:
    import sys; sys.path.insert(0, '<skill>/blender'); from motion_lib import *

Core idea: describe a motion as a few key poses (curve), then spread it along a bone chain through
springs that lag more toward the tip (chain). Add noise drift, strain tremor and per-side timing so
nothing is mirrored or mechanical. accumulate() all channels, then bake() once to quaternions.
"""
import math, random

FPS = 24

def curve(keys, n):
    """smoothstep between (frame, value) keys -> list of n+1 values (index = frame)"""
    out = [0.] * (n + 1)
    for f in range(n + 1):
        if f <= keys[0][0]: out[f] = keys[0][1]; continue
        out[f] = keys[-1][1]
        for (fa, va), (fb, vb) in zip(keys, keys[1:]):
            if fa <= f <= fb:
                u = (f - fa) / max(1, fb - fa); u = u * u * (3 - 2 * u); out[f] = va + (vb - va) * u; break
    return out

def spring(sig, hz, zeta=.5, sub=8):
    """second-order follower: lags, overshoots hard stops, settles (overlap + follow-through)"""
    w = 2 * math.pi * hz; x, v = sig[0], 0.; out = []; dt = 1 / FPS / sub
    for t in sig:
        for _ in range(sub):
            a = w * w * (t - x) - 2 * zeta * w * v; v += a * dt; x += v * dt
        out.append(x)
    return out

class Noise:
    """smooth 1D value noise, deterministic per seed: n(t) in about [-1, 1]"""
    def __init__(self, seed):
        r = random.Random(seed); self.p = [r.uniform(-1, 1) for _ in range(512)]
    def __call__(self, t):
        i = math.floor(t); u = t - i; u = u * u * (3 - 2 * u)
        return self.p[i % 512] * (1 - u) + self.p[(i + 1) % 512] * u

def tremor(n, active, amp=1.5, hz=8., seed=0):
    """strain tremor (deg) only where active[f] is truthy"""
    nz = Noise(seed); return [amp * (1 if active[f] else 0) * nz(f / FPS * hz) for f in range(n + 1)]

def drift(n, amp=.9, hz=.45, seed=1):
    """never perfectly still: slow noise drift (deg)"""
    nz = Noise(seed); return [amp * nz(f / FPS * hz) for f in range(n + 1)]

def breathing(n, period=1.7, amp=1.4, seed=2):
    """noise-modulated breathing rate (not a metronome sine)"""
    nz = Noise(seed); return [amp * math.sin(2 * math.pi * (f / FPS / period + .12 * nz(f / FPS * .3))) for f in range(n + 1)]

def add(*sigs): return [sum(v) for v in zip(*sigs)]
def scale(sig, k): return [k * v for v in sig]
def delay(sig, frames): return [sig[max(0, f - frames)] for f in range(len(sig))]

class Accumulator:
    """collect (bone, axis, degrees-per-frame) channels, then bake them to quaternion keys"""
    def __init__(self, rig): self.rig = rig; self.ch = {}
    def acc(self, bone, axis, arr):
        if self.rig.pose.bones.get(bone) is None: return False
        self.ch.setdefault(bone, []).append((axis, arr)); return True
    def chain(self, bones, axis, sig, hz0=3.4, hz_step=.85, zeta=.45, weights=None):
        """spread one motion along a chain; each segment takes a share and lags more than the last"""
        weights = weights or [1. / len(bones)] * len(bones); hz = hz0
        for b, w in zip(bones, weights):
            self.acc(b, axis, scale(spring(sig, hz, zeta), w)); hz *= hz_step
    def bake(self, f0=1, f1=None):
        from mathutils import Quaternion, Vector
        for bn, parts in self.ch.items():
            pb = self.rig.pose.bones[bn]; pb.rotation_mode = 'QUATERNION'; ml = pb.bone.matrix_local.to_quaternion()
            last = f1 or (len(parts[0][1]) - 1)
            for f in range(f0, last + 1):
                q = Quaternion((1, 0, 0, 0))
                for ax, arr in parts: q = Quaternion(Vector(ax).normalized(), math.radians(arr[f])) @ q
                pb.rotation_quaternion = ml.inverted() @ q @ ml; pb.keyframe_insert('rotation_quaternion', frame=f)

def side_plans(base, n_sides=2, offsets=((0, 0, 1.0), (7, 5, .62))):
    """per-side variants of one plan: (frame offset of rise, frame offset of slam, height factor).
    Default: the second side rises 7 frames later, slams 5 frames later, 62% as high (never mirrored)."""
    return [dict(base, up0=base['up0'] + o[0], peak=base['peak'] + o[0], down=base['down'] + o[1], hi=base['hi'] * o[2])
            for o in offsets[:n_sides]]

def saccade_keys(n, fixations, snap=2., overshoot=.12, tremor_deg=(.5, .4), seed=910):
    """eye look-around: fixations = [(frame, yaw, pitch)]; returns per-frame (yaw, pitch) in degrees.
    Holds each fixation, snaps to the next in ~2 frames with a small overshoot, micro-tremor while holding."""
    nz = [Noise(seed), Noise(seed + 1)]; out = []
    for f in range(n + 1):
        y, p = fixations[-1][1], fixations[-1][2]
        for (fa, ya, pa), (fb, yb, pb) in zip(fixations, fixations[1:]):
            if fa <= f <= fb:
                u = min(1., (f - fa) / snap)
                k = 1 - (1 - u) ** 3 + (overshoot * math.sin(math.pi * min(1., (f - fa) / (2 * snap))) if f - fa <= 2 * snap and fb - fa > 2 * snap else 0)
                y, p = ya + (yb - ya) * k, pa + (pb - pa) * k; break
        out.append((y + tremor_deg[0] * nz[0](f / FPS * 14), p + tremor_deg[1] * nz[1](f / FPS * 16)))
    return out

def mirrored_score(a, b):
    """correlation of two limb curves; > 0.8 means 'moves like a machine' (RULEBOOK R5.1 test)"""
    n = min(len(a), len(b)); ma, mb = sum(a[:n]) / n, sum(b[:n]) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b)); da = math.sqrt(sum((x - ma) ** 2 for x in a[:n])); db = math.sqrt(sum((y - mb) ** 2 for y in b[:n]))
    return num / (da * db + 1e-9)
