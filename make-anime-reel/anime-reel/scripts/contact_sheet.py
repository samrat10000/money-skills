"""Contact sheet or full-size crops for QA.
  python contact_sheet.py <frames_dir> <out.png> [--frames 1,13,25] [--cols 6] [--width 240]
  python contact_sheet.py <frames_dir> <out.png> --frames 48 --crop 380,860,860,1200 [--zoom 2]
Frames are found as NNN.png, cel_NNN.png or NNNN.png. Open the output image and describe it before judging."""
import sys, os, glob, argparse
from PIL import Image, ImageDraw
ap = argparse.ArgumentParser(); ap.add_argument('dir'); ap.add_argument('out')
ap.add_argument('--frames'); ap.add_argument('--cols', type=int, default=6); ap.add_argument('--width', type=int, default=240)
ap.add_argument('--crop'); ap.add_argument('--zoom', type=float, default=1.0); ap.add_argument('--bg', default='205,150,140')
a = ap.parse_args()
def find(f):
    for pat in ('%03d.png', 'cel_%03d.png', '%04d.png', '*_f%03d.png'):
        g = glob.glob(os.path.join(a.dir, pat % f))
        if g: return g[0]
    raise SystemExit('frame %d not found in %s' % (f, a.dir))
allf = sorted(glob.glob(os.path.join(a.dir, '*.png')))
frames = [int(x) for x in a.frames.split(',')] if a.frames else None
paths = [find(f) for f in frames] if frames else allf[::max(1, len(allf) // 12)][:12]
bg = tuple(int(c) for c in a.bg.split(','))
def load(p):
    im = Image.open(p).convert('RGBA'); b = Image.new('RGBA', im.size, bg + (255,)); b.alpha_composite(im); return b.convert('RGB')
ims = [load(p) for p in paths]
if a.crop:
    x0, y0, x1, y1 = (int(v) for v in a.crop.split(','))
    ims = [im.crop((x0, y0, x1, y1)) for im in ims]
    ims = [im.resize((int(im.width * a.zoom), int(im.height * a.zoom)), Image.LANCZOS) for im in ims]
    W, H = ims[0].size; cols = min(a.cols, len(ims))
else:
    W = a.width; H = int(ims[0].height * W / ims[0].width); ims = [im.resize((W, H), Image.LANCZOS) for im in ims]; cols = min(a.cols, len(ims))
rows = (len(ims) + cols - 1) // cols; sh = Image.new('RGB', (W * cols, (H + 18) * rows), (20, 18, 24)); d = ImageDraw.Draw(sh)
for i, (im, p) in enumerate(zip(ims, paths)):
    x, y = (i % cols) * W, (i // cols) * (H + 18); sh.paste(im, (x, y)); d.text((x + 4, y + H + 3), os.path.basename(p), fill=(230, 225, 220))
sh.save(a.out); print('wrote', a.out, sh.size, len(ims), 'frames')
