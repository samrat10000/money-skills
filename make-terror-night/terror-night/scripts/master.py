"""master.py in.wav out.wav : -14 LUFS integrated, true peak <= -1.5 dBTP (gain into a lookahead limiter, iterate). Windows-safe port of master.sh."""
import sys, subprocess, re
src, dst = sys.argv[1], sys.argv[2]; g = float(sys.argv[3]) if len(sys.argv) > 3 else 0.
def meas(f):
    o = subprocess.run(['ffmpeg', '-v', 'info', '-i', f, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    s = o[o.rfind('Summary'):]
    return float(re.search(r'I:\s+(-?[\d.]+)', s).group(1)), float(re.search(r'Peak:\s+(-?[\d.]+)', s).group(1)), float(re.search(r'LRA:\s+(-?[\d.]+)', s).group(1))
for it in range(10):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-af', f'volume={g}dB,alimiter=limit=0.68:attack=1:release=60:level=false', '-ar', '48000', '-c:a', 'pcm_s24le', dst], check=True)
    I, TP, LRA = meas(dst); print(f'it {it} gain {g:+.2f} I {I} TP {TP} LRA {LRA}')
    if abs(I + 14) < .3 and TP <= -1.0: break
    g = round(g + (-14. - I) * 1.3, 2)
