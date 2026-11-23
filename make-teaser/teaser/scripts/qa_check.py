#!/usr/bin/env python3
"""Automated final/shot QA for a teaser (gate G6, also usable on single shot clips).

python3 qa_check.py video.mp4 [--timeline timeline.json] [--allow-black N] [--json report.json]
python3 qa_check.py --frames out/c911 --expect 139          (frame folder check)

Checks: format, duration, black runs, frozen runs, detected cuts (vs timeline), motion energy at
cuts (catches "the car stops at the cut"), audio loudness / peak / silent gaps.
Exit code 1 if any hard check fails. Needs ffmpeg + numpy (pyloudnorm optional).
"""
import argparse, json, os, subprocess, sys, glob
import numpy as np

def probe(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', path],
                         capture_output=True, text=True).stdout
    return json.loads(out)

def frames_gray(path, w=90, h=160):
    p = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vf', f'scale={w}:{h}', '-pix_fmt', 'gray',
                        '-f', 'rawvideo', '-'], capture_output=True)
    a = np.frombuffer(p.stdout, np.uint8)
    return a.reshape(-1, h, w).astype(np.float32) / 255.

def audio(path, sr=48000):
    p = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vn', '-ac', '2', '-ar', str(sr), '-f', 'f32le', '-'],
                       capture_output=True)
    a = np.frombuffer(p.stdout, np.float32)
    return a.reshape(-1, 2) if a.size else None

def runs(mask, min_len):
    out, start = [], None
    for i, m in enumerate(list(mask) + [False]):
        if m and start is None: start = i
        if not m and start is not None:
            if i - start >= min_len: out.append((start, i - 1))
            start = None
    return out

def check_frames(folder, expect):
    fs = sorted(glob.glob(os.path.join(folder, 'f*.png')))
    empty = [f for f in fs if os.path.getsize(f) == 0]
    nums = sorted(int(os.path.basename(f)[1:5]) for f in fs if os.path.getsize(f) > 0)
    missing = [i for i in range(1, expect + 1) if i not in nums] if expect else []
    ok = not empty and not missing and (not expect or len(nums) == expect)
    print(f'[{"PASS" if ok else "FAIL"}] frames {folder}: {len(nums)} ok, {len(empty)} empty, missing {missing[:20]}')
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('video', nargs='?')
    ap.add_argument('--timeline'); ap.add_argument('--json')
    ap.add_argument('--allow-black', type=int, default=None, help='max number of black runs allowed (default: from timeline, else 1)')
    ap.add_argument('--frames'); ap.add_argument('--expect', type=int, default=0)
    a = ap.parse_args()
    if a.frames: sys.exit(0 if check_frames(a.frames, a.expect) else 1)

    rep, fails = {}, []
    def res(name, ok, msg, hard=True):
        print(f'[{"PASS" if ok else ("FAIL" if hard else "WARN")}] {name}: {msg}')
        rep[name] = dict(ok=bool(ok), msg=msg)
        if not ok and hard: fails.append(name)

    info = probe(a.video)
    v = [s for s in info['streams'] if s['codec_type'] == 'video'][0]
    num, den = map(int, v['r_frame_rate'].split('/')); fps = num / den
    dur = float(info['format']['duration'])
    res('format', (v['width'], v['height']) == (1080, 1920) or (v['width'], v['height']) == (720, 1280),
        f"{v['width']}x{v['height']} {fps:.2f} fps {v.get('pix_fmt')} {dur:.2f} s")
    res('fps', abs(fps - 24) < .01, f'{fps:.3f}')
    res('duration', 12 <= dur <= 30, f'{dur:.2f} s (target 15-25)', hard=False)

    tl = json.load(open(a.timeline)) if a.timeline else None
    g = frames_gray(a.video)
    n = len(g); mean = g.reshape(n, -1).mean(1); p99 = np.percentile(g.reshape(n, -1), 99, axis=1)
    # black runs: the whole frame is near black (a dark night shot still has lights, so use the 99th percentile)
    isblack = (mean < .02) & (p99 < .06)
    blk = runs(isblack, 3)
    planned = sum(1 for s in (tl or {}).get('seq', []) if s[0] == 'black' and s[1] >= 3) if tl else None
    allow = a.allow_black if a.allow_black is not None else (planned if planned is not None else 1)
    blk_s = [f'{s / fps:.2f}-{e / fps:.2f}s' for s, e in blk]
    res('black_runs', len(blk) <= allow, f'{len(blk)} runs (allowed {allow}): {blk_s}')
    # frozen runs (identical frames) excluding black
    diff = np.abs(np.diff(g, axis=0)).reshape(n - 1, -1).mean(1)
    frozen = [r for r in runs(diff < .0015, 3) if not isblack[r[0]]]
    res('frozen_runs', not frozen, f'{len(frozen)} runs of >=4 identical frames: {[f"{s / fps:.2f}s x{e - s + 2}" for s, e in frozen][:10]}')
    # cuts: consecutive frames stop correlating (works for dark shots too)
    x = g.reshape(n, -1) - g.reshape(n, -1).mean(1, keepdims=True); x /= (np.linalg.norm(x, axis=1, keepdims=True) + 1e-6)
    dc = 1 - (x[1:] * x[:-1]).sum(1)
    cuts = []
    for i in range(len(dc)):
        if dc[i] > .6 and dc[i] > 2 * np.median(dc[max(0, i - 6):i + 6]) and (not cuts or i + 1 - cuts[-1] > 2): cuts.append(i + 1)
    rep['cuts'] = cuts
    if tl:
        exp, f = [], 0
        for name, k in tl['seq']:
            exp.append(f); f += k
        exp = exp[1:]
        miss = [e for e in exp if not any(abs(e - c) <= 1 for c in cuts) and not (isblack[min(e, n - 1)] or isblack[max(0, e - 1)])]
        res('cuts_vs_timeline', not miss, f'{len(cuts)} detected; timeline cuts not found (±1 f): {miss[:12]}', hard=False)
        res('length_vs_timeline', abs(f - n) <= 1, f'video {n} frames, timeline {f}')
    # motion energy around cuts: low-res optical "activity" = mean abs diff within the shot
    stalls = []
    for c in cuts:
        before = diff[max(0, c - 6):c - 1]; after = diff[c:c + 5]
        if len(before) and len(after) and not isblack[c - 1] and not isblack[min(c, n - 1)]:
            if before.mean() < .004 and after.mean() > .02: stalls.append(c)
    res('motion_at_cuts', not stalls, f'shots that go still right before a busy cut: {[f"{c / fps:.2f}s" for c in stalls]} (coarse; rain/noise can hide a stopping car, so blender/check_motion.py is the real vehicle-speed test)', hard=False)

    # audio
    au = audio(a.video)
    if au is None:
        res('audio', False, 'no audio stream')
    else:
        sr = 48000
        peak = 20 * np.log10(np.abs(au).max() + 1e-9)
        try:
            import pyloudnorm as pyln
            lufs = pyln.Meter(sr).integrated_loudness(au.astype(np.float64))
        except Exception:
            lufs = 20 * np.log10(np.sqrt((au ** 2).mean()) + 1e-9) - 0.7  # rough RMS fallback
        res('loudness', -15.5 <= lufs <= -12.5, f'{lufs:.1f} LUFS (target -14)')
        res('peak', peak <= -0.9, f'{peak:.1f} dBFS sample peak (target <= -1.0)')
        blk_len = int(sr / 10)
        rms = np.sqrt((au[:len(au) // blk_len * blk_len].reshape(-1, blk_len, 2) ** 2).mean((1, 2)))
        sil = runs(20 * np.log10(rms + 1e-9) < -60, 6)
        res('audio_silence', len(sil) <= (allow + 1), f'silent gaps >=0.6 s: {[f"{s / 10:.1f}-{e / 10:.1f}s" for s, e in sil]} (only planned dark beats allowed)', hard=False)
        res('audio_length', abs(len(au) / sr - dur) < .3, f'audio {len(au) / sr:.2f} s vs video {dur:.2f} s')
    if a.json: json.dump(rep, open(a.json, 'w'), indent=1)
    print('RESULT:', 'FAIL ' + ','.join(fails) if fails else 'PASS (review WARN lines yourself)')
    sys.exit(1 if fails else 0)

if __name__ == '__main__':
    main()
