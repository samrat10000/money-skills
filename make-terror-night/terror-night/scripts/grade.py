"""grade.py <frames_dir> <out_dir> [vhs=0|1|<strength>] [tear=0|1]
The ONE grade for every Night Terror shot (LOOK.md section 5): light luma grain weighted to the shadows
(never dots), and the camcorder/VHS treatment ONLY on found-footage shots. Same numbers as the teaser
master that was approved (make-teaser EDIT.md). Writes graded PNGs with the same names.
"""
import sys, os, glob
import numpy as np
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
opt = dict(a.split('=', 1) for a in sys.argv[3:] if '=' in a)
VHS = float(opt.get('vhs', '0')); TEAR = opt.get('tear', '0') == '1'
os.makedirs(dst, exist_ok=True)
rng = np.random.default_rng(7)

def grain(a, amt):
    H, W = a.shape[:2]
    n = np.asarray(Image.fromarray(rng.normal(128, 40, (H // 2, W // 2)).clip(0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)).astype(np.float32)[..., None]
    return a + (n - 128) / 40 * 255 * amt * (0.6 + 0.4 * (1 - a / 255))      # stronger in shadows, never dots

def vhs(a, k=1.0):
    H, W = a.shape[:2]; out = a.copy(); sh = max(1, int(3 * k))
    out[:, sh:, 0] = a[:, :-sh, 0]; out[:, :-sh, 2] = a[:, sh:, 2]          # chroma misregistration 3 px
    for _ in range(int(4 * k)):                                              # tracking wobble bands
        y = rng.integers(0, H - 40); h = rng.integers(4, 30); s = rng.integers(-int(10 * k), int(10 * k) + 1)
        out[y:y + h] = np.roll(out[y:y + h], s, 1)
    if rng.random() < .3 * k:                                                # head-switch noise at the bottom
        out[H - 24:] = out[H - 24:] * .6 + rng.integers(40, 200, (24, W, 1))
    b = np.asarray(Image.fromarray(out.clip(0, 255).astype(np.uint8)).resize((W // 2, H), Image.BILINEAR).resize((W, H), Image.BILINEAR)).astype(np.float32)
    b[::2] *= .94                                                            # faint scanlines
    lum = b.mean(2, keepdims=True); return lum + (b - lum) * .82             # tape desaturation

files = sorted(glob.glob(os.path.join(src, '*.png'))); n = len(files)
for i, f in enumerate(files):
    a = np.asarray(Image.open(f).convert('RGB')).astype(np.float32)
    a = grain(a, .035 if VHS else .022)
    if VHS: a = vhs(a, VHS)
    if TEAR and i >= n - 8:
        k = (i - (n - 8)) / 8; a = vhs(a, 1 + 4 * k) * (1 - k * .9)          # tape tear to black
    Image.fromarray(a.clip(0, 255).astype(np.uint8)).save(os.path.join(dst, os.path.basename(f)))
print('graded', n, 'frames ->', dst)
