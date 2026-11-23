#!/usr/bin/env python3
"""Labelled contact sheet from a video or a frame folder (the "LOOK" step of the QA loop).

python3 contact_sheet.py SRC OUT.jpg [--frames 1,20,40,60] [--n 8] [--cols 4] [--width 1600] [--phone]
SRC = video file or folder of f0001.png frames. --phone also writes OUT_phone.jpg at 360 px wide
(readability check on a phone). --strip makes a motion strip (every 2nd frame of --range a,b).
"""
import argparse, os, glob, subprocess, io
from PIL import Image, ImageDraw

def load_video_frame(path, idx, fps=24):
    p = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{(idx - 1) / fps:.4f}', '-i', path, '-frames:v', '1',
                        '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True)
    return Image.open(io.BytesIO(p.stdout)).convert('RGB')

def count_video(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries',
                          'stream=nb_read_packets', '-of', 'csv=p=0', path], capture_output=True, text=True).stdout
    return int(out.strip().split(',')[0])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src'); ap.add_argument('out')
    ap.add_argument('--frames'); ap.add_argument('--n', type=int, default=8)
    ap.add_argument('--cols', type=int, default=4); ap.add_argument('--width', type=int, default=1600)
    ap.add_argument('--phone', action='store_true'); ap.add_argument('--strip'); ap.add_argument('--label', default='')
    a = ap.parse_args()
    folder = os.path.isdir(a.src)
    files = sorted(glob.glob(os.path.join(a.src, 'f*.png'))) if folder else None
    total = len(files) if folder else count_video(a.src)
    if a.strip:
        s, e = map(int, a.strip.split(',')); idx = list(range(s, e + 1, 2)); a.cols = min(len(idx), 12)
    elif a.frames:
        idx = [int(x) for x in a.frames.split(',')]
    else:
        idx = sorted(set(max(1, round(1 + i * (total - 1) / max(1, a.n - 1))) for i in range(a.n)))
    ims = []
    for i in idx:
        im = Image.open(files[i - 1]).convert('RGB') if folder else load_video_frame(a.src, i)
        ims.append((i, im))
    cw = a.width // a.cols; ch = int(cw * ims[0][1].height / ims[0][1].width)
    rows = (len(ims) + a.cols - 1) // a.cols
    sheet = Image.new('RGB', (cw * a.cols, ch * rows + 24), (20, 20, 20))
    d = ImageDraw.Draw(sheet)
    d.text((6, 4), f'{a.label or os.path.basename(a.src)}  ({total} frames)', fill=(255, 255, 255))
    for k, (i, im) in enumerate(ims):
        x, y = (k % a.cols) * cw, (k // a.cols) * ch + 24
        sheet.paste(im.resize((cw, ch), Image.LANCZOS), (x, y))
        d.rectangle([x, y, x + 46, y + 14], fill=(0, 0, 0)); d.text((x + 3, y + 1), f'f{i}', fill=(255, 220, 0))
    sheet.save(a.out, quality=90)
    print('wrote', a.out, 'frames', idx)
    if a.phone:
        p = os.path.splitext(a.out)[0] + '_phone.jpg'
        sheet.resize((360 * a.cols // 2, int(sheet.height * (360 * a.cols // 2) / sheet.width)), Image.LANCZOS).save(p, quality=85)
        print('wrote', p, '(view this one as the phone-size readability check)')

if __name__ == '__main__':
    main()
