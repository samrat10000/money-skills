"""Brightness numbers for QA (previews lie). python pixel_stats.py <frame.png> [--ref <reference.png>]
Targets (RULEBOOK R7): p95 about 0.8-0.95, p99 >= 0.95, p5 about 0.12-0.19 at the shot's key frame."""
import sys, argparse, numpy as np
from PIL import Image
ap = argparse.ArgumentParser(); ap.add_argument('img'); ap.add_argument('--ref'); a = ap.parse_args()
def st(p):
    x = np.asarray(Image.open(p).convert('RGB')).astype(np.float32) / 255
    return dict(mean=x.mean(), p5=np.percentile(x, 5), p50=np.percentile(x, 50), p95=np.percentile(x, 95), p99=np.percentile(x, 99))
s = st(a.img); print(a.img, ' '.join('%s %.3f' % kv for kv in s.items()))
if a.ref:
    r = st(a.ref); print(a.ref, ' '.join('%s %.3f' % kv for kv in r.items()))
    print('delta', ' '.join('%s %+.3f' % (k, s[k] - r[k]) for k in s))
flags = []
if s['p95'] < 0.75: flags.append('FLAT: p95 < 0.75 (no glow / highlights)')
if s['p99'] < 0.90: flags.append('NO PEAK: p99 < 0.90')
if s['p5'] > 0.22: flags.append('WASHED: p5 > 0.22 (no deep shadows)')
print('\n'.join(flags) if flags else 'OK against R7 targets')
