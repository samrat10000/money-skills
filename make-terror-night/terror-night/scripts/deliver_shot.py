"""deliver_shot.py <shot_name> [...]: per-shot delivery clip (T0.4): the graded shot from edit8\\shots + its slice of the
mastered mix -> previews\\<shot>_v8.mp4 (720x1280, crf 17) + 3 stills (first / middle / last). Run assemble_v8.py first."""
import sys, os, json, subprocess
E = os.path.dirname(os.path.abspath(__file__)); X = os.path.dirname(E)
MIX = os.path.join(X, 'v8cloud', 'v8', 'ep1_v8_mix.wav'); TL = json.load(open(os.path.join(X, 'v8cloud', 'v8', 'v8_timeline.json')))
PV = os.path.join(E, 'previews'); os.makedirs(PV, exist_ok=True)
for name in sys.argv[1:]:
    key = name.split('_')[0]
    src = os.path.join(E, 'shots', name + '.mp4'); out = os.path.join(PV, name + '_v8.mp4')
    n = int(subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout)
    t0 = TL['040'] + 311 / 24 if key == '041' else TL[key]      # 041 is the continuation inside the 040 slot
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-ss', f'{t0:.4f}', '-t', f'{n / 24:.4f}', '-i', MIX, '-map', '0:v', '-map', '1:a',
                    '-vf', 'scale=720:1280:flags=lanczos', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                    '-shortest', '-movflags', '+faststart', out], check=True)
    for tag, fr in (('a', 0), ('b', n // 2), ('c', n - 1)):
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-vf', f"select=eq(n\\,{fr})", '-frames:v', '1', os.path.join(PV, f'{name}_v8_{tag}.jpg')], check=True)
    print(name, n, 'f ->', out)
