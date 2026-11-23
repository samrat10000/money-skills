"""Night Terror teaser v2 sound design: NO music, only real recorded sounds (Sam 2026-11-23).
Trailer cold open (near silence + one ping), rain bed, siren, car reveal revs, drift, thunder, monster, booms, VHS stinger.
python sound_v2.py SFXDIR OUT.wav      (timeline = teaser_edit.py SEQ v2, 24 fps, 491 frames)
Sources: Openverse / Freesound CC0 + CC-BY recordings (credits in sfxlib/*/index.json -> CREDITS_v2.txt).
"""
import sys, os, glob, numpy as np, soundfile as sf
from scipy import signal
import pyloudnorm as pyln

SR, FPS, NF = 48000, 24, 491
DUR = NF / FPS
SFX, OUT = sys.argv[1], sys.argv[2]
rng = np.random.default_rng(11)
mix = np.zeros((int(DUR * SR) + SR, 2), np.float32)
F = lambda f: f / FPS                                  # frame -> seconds

_cache = {}
def load(key):
    if key not in _cache:
        p = glob.glob(os.path.join(SFX, key + '_*.wav'))[0]
        a, sr = sf.read(p, dtype='float32', always_2d=True)
        if sr != SR: a = signal.resample_poly(a, SR, sr, axis=0).astype(np.float32)
        if a.shape[1] == 1: a = np.repeat(a, 2, 1)
        _cache[key] = a[:, :2]
    return _cache[key]

def db(x): return 10 ** (x / 20)

def clip(key, a=0., b=None, pitch=1.0, reverse=False, fi=.01, fo=.05, gain=0., lp=None, hp=None, rev=0., pan=0., width=1.):
    _last[0] = key; x = load(key); i0 = int(a * SR); i1 = len(x) if b is None else int(b * SR)
    x = x[i0:i1].copy()
    if reverse: x = x[::-1].copy()
    if pitch != 1.0:                                   # varispeed: pitch down = slower and bigger
        up, dn = 1000, int(round(1000 * pitch))
        x = signal.resample_poly(x, up, dn, axis=0).astype(np.float32)
    if hp: x = signal.sosfilt(signal.butter(2, hp, 'hp', fs=SR, output='sos'), x, axis=0)
    if lp: x = signal.sosfilt(signal.butter(2, lp, 'lp', fs=SR, output='sos'), x, axis=0)
    n = len(x); fi_n = min(n, int(fi * SR)); fo_n = min(n, int(fo * SR))
    env = np.ones(n, np.float32)
    if fi_n: env[:fi_n] = np.linspace(0, 1, fi_n) ** 2
    if fo_n: env[-fo_n:] *= np.linspace(1, 0, fo_n) ** 1.5
    x = x * env[:, None]
    m = x.mean(1, keepdims=True); x = m + (x - m) * width        # stereo width
    x = x * np.array([min(1, 1 - pan), min(1, 1 + pan)], np.float32)
    if rev: x = reverb(x, rev)
    return (x * db(gain)).astype(np.float32)

_irs = {}
def reverb(x, wet, t60=2.2):
    if t60 not in _irs:
        n = int(t60 * SR); tt = np.arange(n) / SR
        ir = rng.normal(0, 1, (n, 2)).astype(np.float32) * np.exp(-6.9 * tt / t60)[:, None]
        ir = signal.sosfilt(signal.butter(2, 4500, 'lp', fs=SR, output='sos'), ir, axis=0)
        _irs[t60] = ir / np.sqrt((ir ** 2).sum(0))
    ir = _irs[t60]
    w = np.stack([signal.fftconvolve(x[:, c], ir[:, c]) for c in range(2)], 1)[:len(x) + len(ir) // 2]
    out = np.zeros_like(w); out[:len(x)] = x
    return (out * (1 - wet * .5) + w * wet * .6).astype(np.float32)

SOLO = [k for k in os.environ.get('SOLO', '').split(',') if k]     # debug: render only these sources
_last = ['']
def put(x, t, bus=None):
    if SOLO and not any(_last[0].startswith(k) for k in SOLO): return
    if any(_last[0].startswith(k) for k in os.environ.get('EXCL', '').split(',') if k): return
    i = int(t * SR); x = x[:max(0, len(mix) - i)]
    mix[i:i + len(x)] += x
    if bus is not None: bus.append((t, len(x) / SR))

def automate(x, t0, pts):
    """gain automation in dB at absolute seconds [(t, dB), ...] for a clip placed at t0"""
    tt = t0 + np.arange(len(x)) / SR
    g = np.interp(tt, [p[0] for p in pts], [p[1] for p in pts])
    return x * db(g)[:, None].astype(np.float32)

def loop(key, a, b, dur, xf=.8):
    """seamless bed: crossfade a trim of the recording onto itself"""
    _last[0] = key; seg = load(key)[int(a * SR):int(b * SR)]; n = int(dur * SR); x = np.zeros((n, 2), np.float32); i = 0; X = int(xf * SR)
    ramp = np.linspace(0, 1, X)[:, None]
    while i < n:
        s = seg.copy()
        if i: s[:X] *= ramp
        s[-X:] *= ramp[::-1]
        j = min(n, i + len(s)); x[i:j] += s[:j - i]
        if j >= n: break
        i = j - X
    return x

# ============================================================== TIMELINE (frames of the v2 edit)
# 901@0 902@24 903@60 904@101 905@135 906@164 907@178 908@188 909@207 910@226 911@274 black@413 912@431 black@483 end 491
T = {k: F(v) for k, v in dict(c901=0, c902=24, c903=60, c904=101, c905=135, c906=164, c907=178, c908=188, c909=207,
                                c910=226, c911=274, blk=413, c912=431, end=483).items()}
TR = {}   # earshot best-moment trims, filled below
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sound_v2_trims.py')).read())

# ---- cold open: near silence, one ping that rings out, then the rain arrives
# (v2.1: the spring_ping sample sounded like a cartoon "boing" to Sam; replaced by one clean low bell strike)
put(clip('ping_0', 39.25, 41.22, gain=-4, rev=.5, fi=.002, fo=.6), .05)   # a steel pipe struck on concrete: one ringing metal note

put(clip('hit_6', *TR['hit_6'], gain=-16, lp=150, fi=.002, fo=.6), .75)             # the bokeh lamps die: felt in the sub, not heard
# ---- rain bed: outside (city, heavy) and inside the car (roof drum); ducked into silence for the eye and the black beat
rain = loop('rain_7', *TR['rain_7'], DUR + 1)
rain = automate(rain, 0, [(0, -60), (.35, -40), (1.0, -15), (2.45, -14), (2.6, -24), (4.15, -24), (4.25, -12), (9.3, -12),
                          (9.6, -24), (11.3, -26), (11.42, -10), (16.9, -11), (17.25, -60), (17.95, -60), (18.0, -20), (20.1, -22), (20.2, -60)])
put(rain * db(10), 0)
roof = loop('rainroof_4', *TR['rainroof_4'], 2.0)
put(automate(roof, T['c903'], [(T['c903'], -9), (T['c904'] - .1, -9), (T['c904'], -60)]), T['c903'])
wip = clip('wiper_2', 0, 3, gain=-16, lp=3000); put(automate(wip, T['c903'], [(T['c903'], -16), (T['c904'] - .1, -16), (T['c904'], -60)]), T['c903'] + .2)

# ---- police siren far off in the city, drifting across the opening
sir = clip('siren_8', 10, 25, gain=0, lp=6000, rev=.25, fi=1.5, fo=1.5, pan=-.3)
put(automate(sir, 1.2, [(1.2, -60), (2.4, -8), (4.1, -8), (4.3, 2), (5.55, 2), (5.7, -4), (7, -4), (9.3, -14), (10.6, -60)]), 1.2)   # loudest on the street camcorder

# ---- 902 car reveal: "vroom vroom" right on the tyre cam, with the tyre throwing water
put(clip('rev_4', *TR['rev_4'], gain=-3, fi=.005, fo=.25, rev=.15), T['c902'] + .08)
put(clip('rev2_9', *TR['rev2_9'], gain=-9, fi=.01, fo=.4, lp=6000), T['c902'] + .1)
put(clip('splash_0', *TR['splash_0'], gain=-8, fo=.3), T['c902'] + .55)
put(clip('rev2_0', *TR['rev2_0'], gain=-14, lp=900, fi=.2, fo=.4), T['c903'])          # muffled engine inside the cabin

# ---- 903 the giant ahead: the street hums, a far growl rolls down the canyon of buildings
put(clip('rumble_1', 0, 2.0, gain=-12, fi=.6, fo=.5), T['c903'] + .2)
put(clip('bear_6', 0, 1.6, pitch=.7, gain=-9, lp=1200, rev=.6, fi=.15, fo=.6), T['c903'] + .45)     # ends at the camcorder cut

# ---- 904 bystander camcorder: tape hiss under it, siren closer
put(clip('static_5', 9, 9 + (T['c905'] - T['c904']), gain=-18, hp=1500, lp=7000, fi=.01, fo=.02), T['c904'])

# ---- 905 monster POV high above: wind, slow wet breath right in our ear
# v2.2: the pitched breath here read as a human moan (Sam). High above the street: the car far below, rain, the siren
# v2.3 (Sam 2026-11-23: car sound must be crazier, tyre hiss REAL): real recordings of cars tearing past on wet asphalt
def peak_at(x):
    e = np.convolve(np.abs(x).mean(1), np.ones(2400) / 2400, 'same'); return float(e.argmax() / SR)
bed = clip('wetbed_8', 25, 30, gain=-2, hp=250, fi=.15, fo=.3)                          # constant wet-tyre roar under both shots
put(bed[:int((T['c907'] + .25 - T['c905'] + .1) * SR)], T['c905'] - .1)
far = clip('wethiss_1', 47.5, 52.5, gain=-4, lp=5000, rev=.3, fi=.05, fo=.3)             # 905: the car rips out from under us
put(far, T['c905'] + .25 - peak_at(far))
put(clip('rev2_9', *TR['rev2_9b'], gain=-6, lp=3500, rev=.35, fi=.08, fo=.3)[:int((T['c906'] + .2 - T['c905']) * SR)], T['c905'])   # V8 echoing up the canyon
near = clip('wethiss_1', 90.265, 95.265, gain=2, fi=.03, fo=.35)                         # 906: hiss + spray right past the lens
put(near, T['c906'] + .3 - peak_at(near))
put(clip('rev2_9', *TR['rev2_9'], gain=-2, fi=.005, fo=.25), T['c906'] - .06)           # gear-change bark on the cut

# ---- 906 side-follow: the car tears past, glass rains down
pa, pb = TR['passby_1']; pp = TR['passby_peak']
put(clip('passby_1', pa, pa + pp + .55, gain=-5, fi=.05, fo=.4), T['c906'] + .3 - pp)     # peaks mid-shot, gone by the lightning
put(clip('glass_2', TR['glass_2'][0], TR['glass_2'][0] + .5, gain=-8, hp=500, fo=.2, rev=.2), T['c906'] + .05)

# ---- 907 lightning: crack on the first flash, roll under the second
put(clip('thunder_2', 3.30, 7.855, gain=9, fi=.003, fo=1.2), F(180) - .05)          # the crack lands on the flash
put(clip('thunder_5', *TR['thunder_5'], gain=-5, lp=1500, fi=.05, fo=1.2), F(180) - .45)  # rolling body under it
put(clip('boom_2', *TR['boom_2'], gain=-12, lp=200, fo=1.0), F(180))

# ---- 908 facade slab falls
put(clip('hit_6', *TR['hit_6'], gain=-7, fi=.002, fo=.5), T['c908'])     # the cut itself lands
put(clip('debris2_2', *TR['debris2_2'], gain=-4, fo=.6, rev=.2), F(194))
put(clip('boom2_7', 0, 2.5, gain=-6, fi=.005, fo=.8), F(196))

# ---- 909 crash zoom: whoosh into a trailer hit on the skull
wh = clip('whoosh_0', *TR['whoosh_0'], gain=-4, fo=.05)
put(wh, F(213) - TR['whoosh_peak'])
put(clip('hit_5', *TR['hit_5'], gain=-1, fi=.002, fo=.9), F(213))
put(clip('roar_5', 0, 1.2, pitch=.72, gain=-7, lp=2500, fo=.4), F(214))

# ---- 910 the eye: the world drops away, a heartbeat, a low wet rumble, then the sub drop into the hero
put(clip('heart_2', *TR['heart_2'], gain=-8, lp=300, fi=.05, fo=.2), T['c910'] + .1)
put(clip('bear_6', 0, 1.4, pitch=.6, gain=-13, lp=700, fi=.3, fo=.5), T['c910'] + .5)       # a low rumble in its chest, no breath (read as a moan)
rs = clip('thunder_2', *TR['thunder_2'], reverse=True, gain=-6, lp=1800, fi=.6, fo=.01)     # reverse swell sucks into the cut
put(rs, T['c911'] - len(rs) / SR)
sd = clip('subdrop_4', *TR['subdrop_4'], gain=-2, fi=.005, fo=.6)
put(sd, T['c911'] - TR['subdrop_lead'])

# ---- 911 hero: impact on the cut, engine screams into the drift, tyres, the monster screams, slams, car past the lens
put(clip('boom_2', *TR['boom_2'], gain=-2, fi=.002, fo=1.5), T['c911'])
put(clip('rev2_9', *TR['rev2_9b'], gain=-5, fi=.005, fo=.3), T['c911'] - .05)
for k, g, ofs in (('drift_1', -2, 0.), ('drift2_0', -5, .05), ('drift_6', -8, .1)):          # three screech layers
    a, b = TR[k]; L = F(309) - T['c911'] - .1 - ofs
    put(clip(k, a, min(b, a + L), gain=g, fi=.04, fo=.3), T['c911'] + .15 + ofs)     # tyres die as the scream starts
put(clip('drift2_9', *TR['drift2_9'], gain=-12, lp=2000, fi=.05, fo=.4), F(306))       # the skid scrubs out
put(clip('splash_0', *TR['splash_0'], gain=-7, fo=.4), F(300))
# jaw (shots2 stalker_alive 'scream' keys +10 frames): hangs open 20-24 deg from 911 f16 (global 289), clamps at f35, snaps wide at f36-40
def onset(x, rel=-10):
    e = np.convolve(np.abs(x).mean(1), np.ones(480) / 480, 'same'); return float(np.argmax(e > e.max() * db(rel)) / SR)
def at(x, t): put(x, t - onset(x))                                                      # place a clip so its attack lands on t
snarl = clip('tiger_3', *TR['tiger_3'], pitch=.62, gain=-8, lp=2200, fi=.03, fo=.25)     # throat snarl as the jaw drops open
at(snarl[:int(.45 * SR)], F(288))
g = clip('bear_6', 0, 2.593, pitch=.72, gain=-7, lp=1800, fi=.02, fo=.15); n = int((F(310) - F(289)) * SR)
g = g[int(onset(g) * SR):][:n]; g = g * np.linspace(.8, 1.15, len(g))[:, None]          # starts on its attack, swells until the jaw snaps
put(g, F(289))
sc = F(309)                                                                             # the scream: four animals, one monster
at(clip('elk_0', *TR['elk_0'], pitch=.62, gain=1, fi=.005, fo=.6, rev=.35), sc)
at(clip('lion_5', *TR['lion_5'], pitch=.75, gain=0, fi=.005, fo=.5, rev=.3), sc + .02)
at(clip('tiger_3', *TR['tiger_3'], pitch=.8, gain=-3, fi=.005, fo=.4), sc + .04)
at(clip('roar_5', *TR['roar_5'], pitch=.55, gain=-6, lp=900, fi=.005, fo=.6), sc)
for f, g in ((334, -1), (339, -3)):                                                       # claw slams
    put(clip('hit_6', *TR['hit_6'], gain=g, fi=.002, fo=.8), F(f))
    put(clip('debris2_2', *TR['debris2_2'], gain=g - 8, lp=3000, fo=.5), F(f) + .02)
put(clip('lion_1', *TR['lion_1'], pitch=.7, gain=-12, lp=1600, fi=.2, fo=.6, rev=.4), F(350))   # the scream decays into a growl
put(clip('passby_1', *TR['passby_1'], gain=0, fi=.1, fo=.3), F(391) - TR['passby_peak'])
put(clip('whoosh_0', *TR['whoosh_0'], gain=-6, pitch=.8), F(391) - TR['whoosh_peak'] / .8)
put(clip('thunder_2', *TR['thunder_2'], gain=-12, lp=700, fi=.5, fo=1.5), F(392))
put(clip('hit_6', *TR['hit_6'], gain=-5, lp=500, fi=.002, fo=.5), F(392))            # the car body blacks out the lens: a felt whomp
put(clip('tapestop_1', *TR['tapestop_1'], gain=-8, fo=.05), F(405))

# ---- black beat: dead silence, then the camcorder snaps on: click, static, the thing breathes right on the lens
click = np.zeros((int(.03 * SR), 2), np.float32); click[:60] = rng.normal(0, .6, (60, 2)); click[60:] = rng.normal(0, .05, (len(click) - 60, 2)) * np.linspace(1, 0, len(click) - 60)[:, None]
_last[0] = 'click'; put(click * db(-16), T['c912'] - .02)
put(clip('static_5', 9, 11.2, gain=0, hp=800, fi=.005, fo=.05), T['c912'])
put(clip('static_5', 4.0, 4.4, gain=-2, hp=500, fi=.002, fo=.1), T['c912'])
put(clip('growl_1', *TR['growl_1'], pitch=.8, gain=10, fi=.02, fo=.4, rev=.1), T['c912'] + .25)
put(clip('hit_5', *TR['hit_5'], gain=-6, fi=.002, fo=.5), T['end'])
put(clip('static_5', 4.0, 4.15, gain=0, fi=.002, fo=.03), T['end'] - .15)

# ============================================================== master: glue, -14 LUFS, true-peak safe
out = mix[:int(DUR * SR) + int(.6 * SR)]
out = automate(out, 0, [(0, 0), (DUR, 0), (DUR + .6, -60)])
meter = pyln.Meter(SR); lu = meter.integrated_loudness(out)
if not SOLO: out *= db(-14 - lu)
def limiter(x, ceil_db=-1.5, rel=.08, look=.002):
    """lookahead peak limiter: smooth gain reduction so hits stay punchy without clipping"""
    c = db(ceil_db); a = np.abs(x).max(1); L = int(look * SR)
    need = np.minimum(1, c / np.maximum(a, 1e-9))
    need = np.lib.stride_tricks.sliding_window_view(np.pad(need, (0, L), constant_values=1), L + 1).min(1)   # look ahead L samples
    g = np.empty_like(need); r = np.exp(-1 / (rel * SR)); cur = 1.
    for k in range(len(need)):
        cur = need[k] if need[k] < cur else need[k] + (cur - need[k]) * r
        g[k] = cur
    return x * g[:, None]
if not SOLO:
    for _ in range(3):                                  # limit, re-measure, settle on -14 LUFS
        out = limiter(out); out *= db(-14 - meter.integrated_loudness(out))
    out = limiter(out)
sf.write(OUT, out, SR, subtype='PCM_24')
print('LUFS in', round(lu, 1), 'out', round(meter.integrated_loudness(out), 1), 'peak dB', round(20 * np.log10(np.abs(out).max()), 1))
