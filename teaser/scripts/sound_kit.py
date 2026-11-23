"""sound_kit: the mixing toolkit behind the approved music-free teaser mix (SOUND.md).

Usage in your own sound.py:
    from sound_kit import Mix
    m = Mix(sfx_dir='sfxlib', duration_s=20.46)          # sfx files named <key>_<anything>.wav
    T = m.timeline('timeline.json')                       # shot start times (s) + events (s)
    m.put(m.clip('ping_0', 39.25, 41.22, gain=-4, rev=.5, fi=.002, fo=.6), .05)   # cold-open strike
    bed = m.automate(m.loop('rain_7', 3, 40, m.dur + 1), 0, [(0, -60), (1, -15), (17.2, -15), (17.3, -60)])
    m.put(bed, 0)
    m.at(m.clip('lion_5', 2.1, 5.0, pitch=.75, rev=.3), T['ev']['jaw_snap'])     # ATTACK on the jaw snap
    m.master('sound.wav', lufs=-14)
Debug: env SOLO=key1,key2 renders only those sources; EXCL=key removes them.
Needs numpy, scipy, soundfile, pyloudnorm.
"""
import os, glob, json, numpy as np, soundfile as sf
from scipy import signal

def db(x): return 10 ** (x / 20)

class Mix:
    def __init__(self, sfx_dir, duration_s, sr=48000, fps=24, seed=11):
        self.dir, self.sr, self.fps, self.dur = sfx_dir, sr, fps, duration_s
        self.mix = np.zeros((int(duration_s * sr) + sr, 2), np.float32)
        self.rng = np.random.default_rng(seed); self._c = {}; self._irs = {}; self._last = ''
        self.solo = [k for k in os.environ.get('SOLO', '').split(',') if k]
        self.excl = [k for k in os.environ.get('EXCL', '').split(',') if k]

    def F(self, frame): return frame / self.fps

    def timeline(self, path):
        tl = json.load(open(path)); t, f = {}, 0
        for name, n in tl['seq']:
            t.setdefault(name, f / self.fps); f += n
        t['end'] = f / self.fps; t['ev'] = {k: v / self.fps for k, v in tl.get('events', {}).items()}
        return t

    def load(self, key):
        if key not in self._c:
            p = glob.glob(os.path.join(self.dir, key + '_*.wav')) or glob.glob(os.path.join(self.dir, key + '.wav'))
            a, sr = sf.read(p[0], dtype='float32', always_2d=True)
            if sr != self.sr: a = signal.resample_poly(a, self.sr, sr, axis=0).astype(np.float32)
            if a.shape[1] == 1: a = np.repeat(a, 2, 1)
            self._c[key] = a[:, :2]
        return self._c[key]

    def clip(self, key, a=0., b=None, pitch=1., reverse=False, fi=.01, fo=.05, gain=0., lp=None, hp=None, rev=0., pan=0., width=1.):
        """trim a..b seconds, varispeed pitch (<1 bigger/slower; NEVER on breaths), filters, fades, pan, reverb"""
        self._last = key; SR = self.sr; x = self.load(key)
        x = x[int(a * SR):(len(x) if b is None else int(b * SR))].copy()
        if reverse: x = x[::-1].copy()
        if pitch != 1.: x = signal.resample_poly(x, 1000, int(round(1000 * pitch)), axis=0).astype(np.float32)
        if hp: x = signal.sosfilt(signal.butter(2, hp, 'hp', fs=SR, output='sos'), x, axis=0)
        if lp: x = signal.sosfilt(signal.butter(2, lp, 'lp', fs=SR, output='sos'), x, axis=0)
        n = len(x); env = np.ones(n, np.float32); fi_n = min(n, int(fi * SR)); fo_n = min(n, int(fo * SR))
        if fi_n: env[:fi_n] = np.linspace(0, 1, fi_n) ** 2
        if fo_n: env[-fo_n:] *= np.linspace(1, 0, fo_n) ** 1.5
        x = x * env[:, None]; m = x.mean(1, keepdims=True); x = m + (x - m) * width
        x = x * np.array([min(1, 1 - pan), min(1, 1 + pan)], np.float32)
        if rev: x = self.reverb(x, rev)
        return (x * db(gain)).astype(np.float32)

    def reverb(self, x, wet, t60=2.2):
        SR = self.sr
        if t60 not in self._irs:
            n = int(t60 * SR); tt = np.arange(n) / SR
            ir = self.rng.normal(0, 1, (n, 2)).astype(np.float32) * np.exp(-6.9 * tt / t60)[:, None]
            ir = signal.sosfilt(signal.butter(2, 4500, 'lp', fs=SR, output='sos'), ir, axis=0)
            self._irs[t60] = ir / np.sqrt((ir ** 2).sum(0))
        ir = self._irs[t60]
        w = np.stack([signal.fftconvolve(x[:, c], ir[:, c]) for c in range(2)], 1)[:len(x) + len(ir) // 2]
        out = np.zeros_like(w); out[:len(x)] = x
        return (out * (1 - wet * .5) + w * wet * .6).astype(np.float32)

    def put(self, x, t):
        k = self._last
        if self.solo and not any(k.startswith(s) for s in self.solo): return
        if any(k.startswith(s) for s in self.excl): return
        i = int(t * self.sr)
        if i < 0: x = x[-i:]; i = 0                    # starts before t=0: trim the head
        x = x[:max(0, len(self.mix) - i)]; self.mix[i:i + len(x)] += x

    def onset(self, x, rel=-10):
        """time (s) of the attack: first point the envelope crosses max + rel dB"""
        e = np.convolve(np.abs(x).mean(1), np.ones(480) / 480, 'same'); return float(np.argmax(e > e.max() * db(rel)) / self.sr)

    def peak_at(self, x):
        e = np.convolve(np.abs(x).mean(1), np.ones(2400) / 2400, 'same'); return float(e.argmax() / self.sr)

    def at(self, x, t):
        """place so the ATTACK lands on t (never align by file start)"""
        self.put(x, t - self.onset(x))

    def peak_on(self, x, t):
        """place so the loudest moment lands on t (passbys, whooshes)"""
        self.put(x, t - self.peak_at(x))

    def automate(self, x, t0, pts):
        tt = t0 + np.arange(len(x)) / self.sr
        g = np.interp(tt, [p[0] for p in pts], [p[1] for p in pts])
        return x * db(g)[:, None].astype(np.float32)

    def loop(self, key, a, b, dur, xf=.8):
        """seamless bed from a trim, crossfaded onto itself"""
        self._last = key; SR = self.sr; seg = self.load(key)[int(a * SR):int(b * SR)]
        n = int(dur * SR); x = np.zeros((n, 2), np.float32); i = 0; X = int(xf * SR); ramp = np.linspace(0, 1, X)[:, None]
        while i < n:
            s = seg.copy()
            if i: s[:X] *= ramp
            s[-X:] *= ramp[::-1]
            j = min(n, i + len(s)); x[i:j] += s[:j - i]
            if j >= n: break
            i = j - X
        return x

    def limiter(self, x, ceil_db=-1.5, rel=.08, look=.002):
        c = db(ceil_db); a = np.abs(x).max(1); L = int(look * self.sr)
        need = np.minimum(1, c / np.maximum(a, 1e-9))
        need = np.lib.stride_tricks.sliding_window_view(np.pad(need, (0, L), constant_values=1), L + 1).min(1)
        g = np.empty_like(need); r = np.exp(-1 / (rel * self.sr)); cur = 1.
        for k in range(len(need)):
            cur = need[k] if need[k] < cur else need[k] + (cur - need[k]) * r; g[k] = cur
        return x * g[:, None]

    def master(self, out_path, lufs=-14., tail=.6):
        import pyloudnorm as pyln
        SR = self.sr; out = self.mix[:int(self.dur * SR) + int(tail * SR)]
        out = self.automate(out, 0, [(0, 0), (self.dur, 0), (self.dur + tail, -60)])
        meter = pyln.Meter(SR); lu = meter.integrated_loudness(out)
        if not self.solo:
            out *= db(lufs - lu)
            for _ in range(3): out = self.limiter(out); out *= db(lufs - meter.integrated_loudness(out))
            out = self.limiter(out)
        sf.write(out_path, out, SR, subtype='PCM_24')
        print('LUFS in', round(lu, 1), 'out', round(meter.integrated_loudness(out), 1), 'peak dB', round(20 * np.log10(np.abs(out).max()), 1))
