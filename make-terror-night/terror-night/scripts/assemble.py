"""assemble_v8.py: Night Terror Ep1 v8 assembly (re-runnable as renders land).
For each of the 30 shots: take the v8 1080 render when ALL its frames exist, else a logged fallback
(v7 approved 720p preview upscaled, a v7 1080 render, or black). Grade per LOOK.md (light grain on every shot,
VHS + REC + timecode only on the hidden-watcher shots, tape stop on 165), encode each shot at its exact frame
count, concat, lay ep1_v8_mix.wav under it, write IG / master / phone files and a SOURCES report.
Run:  python assemble_v8.py            (needs numpy, Pillow, ffmpeg on PATH)
"""
import os, sys, glob, json, subprocess, shutil, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

XC = r'C:\Users\cross\Downloads\xc'
V8 = rf'{XC}\ep1pc\out\v8'; V7F = rf'{XC}\ep1pc\out\v7final'; KEEP = rf'{XC}\ep1pc\v7keep'
P7 = rf'{XC}\ep1pc\v8cloud\pent7\out007v8'
OUT = rf'{XC}\ep1pc\edit8'; SH = rf'{OUT}\shots'; os.makedirs(SH, exist_ok=True)
MIX = os.environ.get('MIX', rf'{XC}\ep1pc\v8cloud\v8\ep1_v8_mix.wav')
W, H, FPS = 1080, 1920, 24

# shot, frames, [sources in priority order], watcher?   source kinds: ('v8', cut, first) | ('mp4', path) | ('pngs', dir)
SHOTS = [
 ('000_hook', 168, [('v8', 400, 1)], 'watch'),
 ('001_ring', 95, [('mp4', rf'{KEEP}\001_ring_v2.mp4')], ''),
 ('002_phone', 47, [('mp4', rf'{KEEP}\002_phone.mp4')], ''),
 ('003_answer', 83, [('mp4', rf'{KEEP}\003_answer_v2.mp4')], ''),
 ('004_look_outside', 174, [('mp4', rf'{KEEP}\004_look_outside.mp4')], ''),
 ('004w_watcher', 60, [('v8', 404, 1)], 'watch'),
 ('005_bridge', 92, [('mp4', rf'{KEEP}\005_bridge_v2.mp4')], ''),
 ('006_screamer_still', 96, [('v8', 406, 1), ('mp4', rf'{KEEP}\006_screamer_v1.mp4')], ''),
 ('007_grab', 48, [('pngs', P7), ('mp4', rf'{KEEP}\007_grab_v1.mp4')], ''),
 ('030_corridor', 72, [('mp4', rf'{KEEP}\030_corridor_v1.mp4')], ''),
 ('040_stairwell', 311, [('mp4', rf'{KEEP}\040_stairwell.mp4')], ''),
 ('041_stairwell_ext', 132, [('v8', 441, 313)], ''),
 ('050_lobby', 96, [('mp4', rf'{KEEP}\050_lobby_v2.mp4')], ''),
 ('055_b1_stairs', 70, [('v8', 455, 1)], ''),
 ('060_garage', 96, [('mp4', rf'{KEEP}\060_garage_v1.mp4')], ''),
 ('070_in_the_car', 84, [('v8', 471, 1), ('mp4', rf'{KEEP}\070_in_the_car_v1.mp4')], ''),
 ('080_ignition', 36, [('mp4', rf'{KEEP}\080_ignition_v1.mp4')], ''),
 ('090_gate_burst', 84, [('v8', 490, 1)], ''),
 ('095_watcher_street', 60, [('v8', 495, 1)], 'watch'),
 ('100_tyre_cam', 36, [('mp4', rf'{KEEP}\100_tyre_cam_v1.mp4')], ''),
 ('110_chase', 60, [('mp4', rf'{KEEP}\110_chase_runners_v1.mp4')], ''),
 ('120_drift', 36, [('mp4', rf'{KEEP}\120_drift_v1.mp4')], ''),
 ('125_brute_jturn', 144, [('v8', 525, 1), ('mp4', rf'{V7F}\125_brute_block_v2_silent.mp4')], ''),
 ('130_overpass_park', 72, [('v8', 530, 1), ('mp4', rf'{V8}\130_overpass_park_v8_silent.mp4')], ''),
 ('135_dash_reveal', 60, [('v8', 535, 1), ('mp4', rf'{XC}\ep1pc\out\v8_old\135_dash_reveal_v8_50mm_silent.mp4')], ''),
 ('140_crash_zoom', 48, [('v8', 540, 1), ('mp4', rf'{V8}\140_crash_zoom_v8_silent.mp4')], ''),
 ('150_scream', 60, [('v8', 550, 1), ('mp4', rf'{V7F}\150_stalker_v1_silent.mp4')], ''),
 ('152_watcher_bridge', 48, [('v8', 552, 1)], 'watch'),
 ('155_black', 36, [('black',)], ''),
 ('160_empty_seat', 252, [('v8', 160, 1), ('mp4', rf'{KEEP}\160_empty_seat_v1.mp4')], ''),
 ('165_rec_end', 36, [('v8', 565, 1)], 'watch_tear'),
]

def run(cmd): subprocess.run(cmd, check=True)

def frames_from(src, n):
    """-> (list of HxWx3 uint8 arrays or a generator, label, full_res) or None if this source is not complete."""
    k = src[0]
    if k == 'v8':
        _, cut, first = src
        fs = [rf'{V8}\c{cut}\f{first + i:04d}.png' for i in range(n)]
        if all(os.path.exists(f) and os.path.getsize(f) > 0 for f in fs):
            return (lambda: (np.asarray(Image.open(f).convert('RGB')) for f in fs)), f'v8 c{cut} 1080 ({n} f)', True
        have = sum(os.path.exists(f) and os.path.getsize(f) > 0 for f in fs)
        return None if have < n else None
    if k == 'pngs':
        fs = sorted(glob.glob(os.path.join(src[1], '*.png')))
        if len(fs) >= n:
            return (lambda: (np.asarray(Image.open(f).convert('RGB').resize((W, H), Image.LANCZOS)) for f in fs[:n])), f'pngs {src[1]}', Image.open(fs[0]).size == (W, H)
        return None
    if k == 'mp4':
        if not os.path.exists(src[1]): return None
        def gen(p=src[1]):
            pr = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'scale={W}:{H}:flags=lanczos', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
            while True:
                b = pr.stdout.read(W * H * 3)
                if len(b) < W * H * 3: break
                yield np.frombuffer(b, np.uint8).reshape(H, W, 3)
            pr.wait()
        w = int(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width', '-of', 'csv=p=0', src[1]], capture_output=True, text=True).stdout.strip() or 0)
        # Sam 2026-11-25: the approved Ep1 keep shots stay 720p upscaled for this episode (override of T16.1, logged in WORKING_EP1_V8.md);
        # every NEW render is native 1080 (rule T0.7).
        return gen, f'mp4 {os.path.basename(src[1])} ({w}px wide{"" if w == W else ", UPSCALED, approved by Sam"})', True
    if k == 'black':
        return (lambda: (np.zeros((H, W, 3), np.uint8) for _ in range(n))), 'black (planned)', True

# ---------------- grade (LOOK.md section 5; same numbers as terror-night/scripts/grade.py) + the watcher's camcorder overlay
rng = np.random.default_rng(7)
def grain(a, amt):
    nz = np.asarray(Image.fromarray(rng.normal(128, 40, (H // 2, W // 2)).clip(0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)).astype(np.float32)[..., None]
    return a + (nz - 128) / 40 * 255 * amt * (0.6 + 0.4 * (1 - a / 255))
def vhs(a, k=1.0):
    out = a.copy(); sh = max(1, int(3 * k))
    out[:, sh:, 0] = a[:, :-sh, 0]; out[:, :-sh, 2] = a[:, sh:, 2]
    for _ in range(int(4 * k)):
        y = rng.integers(0, H - 40); h = rng.integers(4, 30); s = rng.integers(-int(10 * k), int(10 * k) + 1)
        out[y:y + h] = np.roll(out[y:y + h], s, 1)
    if rng.random() < .3 * k: out[H - 24:] = out[H - 24:] * .6 + rng.integers(40, 200, (24, W, 1))
    b = np.asarray(Image.fromarray(out.clip(0, 255).astype(np.uint8)).resize((W // 2, H), Image.BILINEAR).resize((W, H), Image.BILINEAR)).astype(np.float32)
    b[::2] *= .94; lum = b.mean(2, keepdims=True); return lum + (b - lum) * .82
try: FONT = ImageFont.truetype(r'C:\Windows\Fonts\lucon.ttf', 50)
except Exception: FONT = ImageFont.load_default()
def rec_overlay(img, i):          # 2026-11-26 R5: an authentic late-90s consumer camcorder OSD (Hi8 / VHS-C), reusable for every watcher shot
    """REC + blinking dot (top left), segmented battery + tape counter (top right), burned-in date/time (bottom left).
    Monospaced white with a 2 px dark shadow, slightly soft, as character-generator text was. No timecode (pro cameras only)."""
    from PIL import ImageFilter
    W_, H_ = img.size; lay = Image.new('RGBA', (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    i = i + OSD_F0; sec = 3 * 3600 + 47 * 60 + 2 + i / FPS; cnt = 6 + i / FPS      # one tape, one clock: 3:47 a.m. as Sam says, running through the episode
    def txt(x, y, t, col=(238, 238, 232, 255)):
        d.text((x + 3, y + 3), t, font=FONT, fill=(0, 0, 0, 170)); d.text((x, y), t, font=FONT, fill=col)
    if (i // 12) % 2 == 0: d.ellipse((74, 112, 106, 144), fill=(0, 0, 0, 150)); d.ellipse((70, 108, 102, 140), fill=(226, 34, 30, 255))
    txt(116, 102, 'REC')
    bx = W_ - 250; d.rectangle((bx + 3, 115, bx + 133, 145), outline=(0, 0, 0, 160), width=4)
    d.rectangle((bx, 112, bx + 130, 142), outline=(238, 238, 232, 255), width=4); d.rectangle((bx + 130, 120, bx + 138, 134), fill=(238, 238, 232, 255))
    for k in range(3): d.rectangle((bx + 9 + k * 40, 119, bx + 41 + k * 40, 135), fill=(238, 238, 232, 255))
    txt(W_ - 250, 160, f'{int(cnt // 3600)}:{int(cnt % 3600 // 60):02d}:{int(cnt % 60):02d}')
    h12 = int(sec // 3600) % 12 or 12
    txt(70, H_ - 230, 'NOV 26 2026'); txt(70, H_ - 165, f'{h12}:{int(sec % 3600 // 60):02d}:{int(sec % 60):02d} AM')
    lay = lay.filter(ImageFilter.GaussianBlur(.8))
    out = img.convert('RGBA'); out.alpha_composite(lay); out = np.asarray(out.convert('RGB')).copy()
    out[1::2, 1:] = out[1::2, :-1]                    # faint interlace: odd field 1 px late
    return Image.fromarray(out)

def grade_shot(name, n, kind, gen, outmp4):
    enc = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-vf', 'hqdn3d=3:3:5:5', '-c:v', 'libx264', '-crf', '12', '-preset', 'medium', '-pix_fmt', 'yuv420p', outmp4], stdin=subprocess.PIPE)
    last = None; i = 0
    for a in gen():
        if i >= n: break
        last = a; i += write(enc, a, i, n, kind)
    while i < n:                      # short source: hold the last frame (logged)
        i += write(enc, last if last is not None else np.zeros((H, W, 3), np.uint8), i, n, kind)
    enc.stdin.close(); enc.wait()
    return i

PAD = {}
OSD_F0 = 0
CUR = ''
LIFT = {'055_b1_stairs': (20, 50, .72)}   # 2026-11-26 R11: the black stretch of the service stair read as dead time: gentle gamma lift (frames a-b, gamma)
def write(enc, a, i, n, kind):
    f = a.astype(np.float32)
    if CUR in LIFT:
        a0, b0, gm = LIFT[CUR]
        if a0 <= i <= b0:
            w = math.sin(math.pi * (i - a0) / (b0 - a0)); f = f * (1 - w) + (255 * (f / 255) ** gm) * w
    if kind:
        f = grain(f, .035); f = vhs(f, .8)
        if kind == 'watch_tear' and i >= n - 8:
            k = (i - (n - 8)) / 8; f = vhs(f, 1 + 4 * k) * (1 - k * .9)
        im = Image.fromarray(f.clip(0, 255).astype(np.uint8)); im = rec_overlay(im, i); f = np.asarray(im)
    else:
        f = grain(f, .022)
    enc.stdin.write(np.asarray(f).clip(0, 255).astype(np.uint8).tobytes()); return 1

def main():
    only = set(sys.argv[1:])
    report = []; global OSD_F0; ep_f = 0
    for name, n, srcs, kind in SHOTS:
        OSD_F0 = ep_f; ep_f += n; global CUR; CUR = name
        mp4 = rf'{SH}\{name}.mp4'
        got = None
        for j, s in enumerate(srcs):
            got = frames_from(s, n)
            if got:
                if j > 0: got = (got[0], 'STAND-IN (v8 not rendered yet): ' + got[1], False)
                break
        if not got:
            got = (lambda n=n: (np.zeros((H, W, 3), np.uint8) for _ in range(n))), 'MISSING (black placeholder: v8 render not finished)', False
        gen, label, full = got
        tag = json.dumps([name, label, 'osd2' if kind else '', str(LIFT.get(name, ''))])
        stamp = mp4 + '.src'
        if (not only or name in only) and not (os.path.exists(mp4) and os.path.exists(stamp) and open(stamp).read() == tag):
            k = grade_shot(name, n, kind, gen, mp4); open(stamp, 'w').write(tag)
            print(f'{name}: {k} f from {label}', flush=True)
        report.append((name, n, label, full))
    with open(rf'{OUT}\concat.txt', 'w') as fh:
        for name, *_ in report: fh.write(f"file 'shots/{name}.mp4'\n")
    run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', rf'{OUT}\concat.txt', '-c', 'copy', rf'{OUT}\picture.mp4'])
    tot = sum(r[1] for r in report)
    final = all(r[3] and not r[2].startswith(('MISSING', 'STAND-IN')) for r in report)
    base = rf'{OUT}\night-terror-ep1-v8-{"final" if final else "assembly"}'
    run(['ffmpeg', '-y', '-v', 'error', '-i', rf'{OUT}\picture.mp4', '-i', MIX, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k',
         '-t', f'{tot / FPS:.3f}', '-movflags', '+faststart', base + '_master.mp4'])
    run(['ffmpeg', '-y', '-v', 'error', '-i', base + '_master.mp4', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart', base + '_IG.mp4'])
    run(['ffmpeg', '-y', '-v', 'error', '-i', base + '_master.mp4', '-vf', 'scale=720:1280:flags=lanczos', '-c:v', 'libx264', '-b:v', '850k', '-maxrate', '1000k', '-bufsize', '2000k',
         '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', base + '_phone.mp4'])
    with open(rf'{OUT}\SOURCES.md', 'w') as fh:
        fh.write(f'# Ep1 v8 {"FINAL" if final else "ASSEMBLY (not final, T16.1)"}: {tot} frames = {tot / FPS:.1f} s\n\n| shot | frames | source | 1080 native |\n|---|---|---|---|\n')
        for name, n, label, full in report: fh.write(f'| {name} | {n} | {label} | {"yes" if full else "NO"} |\n')
    print(open(rf'{OUT}\SOURCES.md').read()); print('->', base)

if __name__ == '__main__': main()
