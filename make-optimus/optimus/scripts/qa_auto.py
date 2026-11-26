"""qa_auto.py - numbers before pictures (Optimus rule 1).

Usage:
  python qa_auto.py frames <dir> [--expect N]     a rendered cut: PNG frames f####.png
  python qa_auto.py video  <file.mp4>             a clip or a whole episode (picture + sound)
Prints a few lines; every line starting with FLAG needs a look. Needs numpy, Pillow, ffmpeg on PATH.

Checks
  frames : count vs --expect, 0-byte/missing numbers, black frames (mean luma < 3.5), blown frames (> 235),
           frozen runs (frame diff ~0 for >= 6 frames), STUTTER (a stall: motion < 50% of the local median,
           then a lurch > 140% within 6 frames; the 'camera eased to a stop every N frames' bug), exposure of the shot.
  video  : the same picture checks on decoded frames + integrated loudness, true peak, silence runs.
"""
import sys, os, glob, re, subprocess
import numpy as np
from PIL import Image

def luma_small(path, w=135, h=240):
    return np.asarray(Image.open(path).convert('L').resize((w, h)), np.float32)

def picture_checks(frames):
    """frames: list of (label, 2-D luma array). Returns printable lines."""
    out = []; L = [f for _, f in frames]; n = len(L)
    if not n: return ['FLAG no frames']
    mean = np.array([f.mean() for f in L])
    blk = [frames[i][0] for i in range(n) if mean[i] < 3.5]; blown = [frames[i][0] for i in range(n) if mean[i] > 235]
    if blk: out.append(f'FLAG black frames: {len(blk)} ({blk[0]}..{blk[-1]})')
    if blown: out.append(f'FLAG blown frames: {len(blown)} ({blown[0]}..{blown[-1]})')
    d = np.array([np.abs(L[i] - L[i - 1]).mean() for i in range(1, n)]) if n > 1 else np.array([])
    run = 0
    for i, x in enumerate(d):
        run = run + 1 if x < .15 else 0
        if run == 6: out.append(f'FLAG frozen run starting near {frames[i - 4][0]}')
    st = []
    for i in range(3, len(d) - 3):
        med = np.median(d[max(0, i - 6):i + 7]) + 1e-6
        if d[i] < .5 * med and max(d[i + 1:i + 7]) > 1.4 * med and med > 2: st.append(frames[i + 1][0])
    if st: out.append(f'FLAG stutter (stall then lurch) at {", ".join(map(str, st[:6]))}{" ..." if len(st) > 6 else ""}')
    out.append(f'exposure mean luma {mean.mean():.0f} (min {mean.min():.0f}, max {mean.max():.0f}); motion median {np.median(d) if len(d) else 0:.1f}')
    return out

def check_frames(dirpath, expect=None):
    fs = sorted(glob.glob(os.path.join(dirpath, 'f*.png')))
    nums = [int(re.findall(r'(\d+)', os.path.basename(f))[-1]) for f in fs]
    out = [f'{dirpath}: {len(fs)} frames' + (f' / expected {expect}' if expect else '')]
    if expect and len(fs) < expect: out.append(f'FLAG missing {expect - len(fs)} frames')
    zero = [os.path.basename(f) for f in fs if os.path.getsize(f) == 0]
    if zero: out.append(f'FLAG 0-byte frames: {zero[:5]}')
    if nums:
        gaps = sorted(set(range(nums[0], nums[-1] + 1)) - set(nums))
        if gaps: out.append(f'FLAG gaps in numbering: {gaps[:8]}')
    good = [(n_, luma_small(f)) for n_, f in zip(nums, fs) if os.path.getsize(f) > 0]
    return out + picture_checks(good)

def check_video(path):
    W, H = 135, 240
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vf', f'scale={W}:{H},format=gray', '-f', 'rawvideo', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
    out = [f'{path}: {len(a)} frames'] + picture_checks([(i, a[i]) for i in range(len(a))])
    e = subprocess.run(['ffmpeg', '-v', 'info', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    s = e[e.rfind('Summary'):]
    I = re.search(r'I:\s+(-?[\d.]+)', s); TP = re.search(r'Peak:\s+(-?[\d.]+)', s)
    if I:
        out.append(f'loudness {I.group(1)} LUFS, true peak {TP.group(1) if TP else "?"} dBTP')
        if TP and float(TP.group(1)) > -1.0: out.append('FLAG true peak above -1 dBTP')
    sil = subprocess.run(['ffmpeg', '-v', 'info', '-i', path, '-af', 'silencedetect=n=-45dB:d=0.6', '-vn', '-f', 'null', '-'], capture_output=True, text=True).stderr
    runs = re.findall(r'silence_start: ([\d.]+)', sil)
    if runs: out.append(f'FLAG silence (< -45 dB, > 0.6 s) at {", ".join(runs[:6])} s')
    return out

if __name__ == '__main__':
    if len(sys.argv) < 3: print(__doc__); sys.exit(1)
    mode, target = sys.argv[1], sys.argv[2]
    exp = int(sys.argv[sys.argv.index('--expect') + 1]) if '--expect' in sys.argv else None
    lines = check_frames(target, exp) if mode == 'frames' else check_video(target)
    print('\n'.join(lines)); print('RESULT', 'FLAGGED' if any(l.startswith('FLAG') for l in lines) else 'CLEAN')
