import json, subprocess, numpy as np, sys
t=json.load(open('v8_timeline.json')); dur=t.pop('_dur'); f=sys.argv[1] if len(sys.argv)>1 else 'ep1_v8_mix.wav'
a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-f','f32le','-ac','2','-ar','48000','-'],capture_output=True).stdout,np.float32).reshape(-1,2)
m=a.mean(1); sr=48000; names=list(t); out=[]
for i,n in enumerate(names):
    s=t[n]; e=t[names[i+1]] if i+1<len(names) else dur
    x=m[int(s*sr):int(e*sr)]; hs=[20*np.log10(np.sqrt(np.mean(x[j:j+sr//2]**2))+1e-9) for j in range(0,len(x)-sr//2,sr//2)]
    out.append(f'{n}:{20*np.log10(np.sqrt(np.mean(x*x))+1e-9):.0f}/{min(hs):.0f}')
print('  '.join(out))
