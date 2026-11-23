#!/usr/bin/env python3
"""Grade + treatment + assembly from timeline.json (EDIT.md). No text on screen.

python3 edit_assemble.py timeline.json OUT.mp4 [AUDIO.wav]
env ROOTS=dirA:dirB   frame roots searched in order, frames at <root>/<shot>/f%04d.png
                      (<shot> = the timeline name, e.g. 911_poster_finale, or c911 if you set "dirs")
env CRF=16            12 master, 17 IG, 16 review
env LOOKDIR=path      folder with a series look.py exposing lens(PIL.Image) -> PIL.Image (optional)
env ALLOW_MISSING=1   only for drafts; finals must have every frame (script exits 1 otherwise)
"""
import os, sys, json, subprocess, numpy as np
from PIL import Image

tl = json.load(open(sys.argv[1])); OUT = sys.argv[2]; AUDIO = sys.argv[3] if len(sys.argv) > 3 else None
W, H, FPS = tl.get('w', 1080), tl.get('h', 1920), tl.get('fps', 24)
VHS = {k: v for k, v in tl.get('vhs_strength', {}).items()} or {k: 1.0 for k in tl.get('vhs', [])}
DIRS = tl.get('dirs', {})                       # optional: {"911_poster_finale": "c911"}
TEAR = tl.get('tape_tear', [])                  # shots whose last 8 frames tear to black
ROOTS = [r for r in os.environ.get('ROOTS', '.').split(':') if r]
rng = np.random.default_rng(5)
try:
    sys.path.insert(0, os.environ.get('LOOKDIR', '')); from look import lens
except Exception:
    lens = None

def frame(shot, i):
    for r in ROOTS:
        p = os.path.join(r, DIRS.get(shot, shot), f'f{i:04d}.png')
        if os.path.exists(p) and os.path.getsize(p) > 0: return Image.open(p).convert('RGB')
    return None

def grain(a, amt):
    """light luma grain (RULEBOOK R6.6): ~2% normal, 3.5% VHS; stronger in shadows, never dots"""
    n = rng.normal(0, amt, (H // 2, W // 2)).astype(np.float32)
    n = np.asarray(Image.fromarray(((n * 40 + 128).clip(0, 255)).astype(np.uint8)).resize((W, H), Image.BILINEAR)).astype(np.float32)[..., None]
    return a + (n - 128) / 40 * 255 * amt * (0.6 + 0.4 * (1 - a / 255))

def vhs(a, k=1.0):
    out = a.copy(); sh = max(1, int(3 * k))
    out[:, sh:, 0] = a[:, :-sh, 0]; out[:, :-sh, 2] = a[:, sh:, 2]
    for _ in range(int(4 * k)):
        y = rng.integers(0, H - 40); h = rng.integers(4, 30); s = rng.integers(-int(10 * k), int(10 * k) + 1)
        out[y:y + h] = np.roll(out[y:y + h], s, 1)
    if rng.random() < .3 * k: out[H - 24:] = out[H - 24:] * .6 + rng.integers(40, 200, (24, W, 1))
    b = np.asarray(Image.fromarray(out.clip(0, 255).astype(np.uint8)).resize((W // 2, H), Image.BILINEAR).resize((W, H), Image.BILINEAR)).astype(np.float32)
    b[::2] *= .94; lum = b.mean(2, keepdims=True)
    return lum + (b - lum) * .82

ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                       *(['-i', AUDIO] if AUDIO else []), '-c:v', 'libx264', '-preset', 'slow', '-crf', os.environ.get('CRF', '16'),
                       '-pix_fmt', 'yuv420p', *(['-c:a', 'aac', '-b:a', '256k', '-shortest'] if AUDIO else []), '-movflags', '+faststart', OUT],
                      stdin=subprocess.PIPE)
missing, last = [], None
for shot, n in tl['seq']:
    for i in range(1, n + 1):
        if shot == 'black':
            a = np.zeros((H, W, 3), np.float32)
        else:
            im = frame(shot, i)
            if im is None: missing.append((shot, i)); im = last or Image.new('RGB', (W, H))
            last = im; im = im.resize((W, H), Image.LANCZOS)
            if lens: im = lens(im)
            a = np.asarray(im).astype(np.float32)
            a = grain(a, .035 if shot in VHS else .022)
            if shot in VHS: a = vhs(a, VHS[shot])
            if shot in TEAR and i > n - 8:
                k = (i - (n - 8)) / 8; a = vhs(a, 1 + 4 * k) * (1 - k * .9)
                if i == n: a *= 0
        ff.stdin.write(a.clip(0, 255).astype(np.uint8).tobytes())
ff.stdin.close(); ff.wait()
print('frames', sum(n for _, n in tl['seq']), 'missing', len(missing), missing[:10])
if missing and os.environ.get('ALLOW_MISSING') != '1':
    print('FAIL: missing frames; a final may not hold frames (EDIT.md 4)'); sys.exit(1)
