import sys, json, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
sys.path.insert(0,'.')
from lines import LINES
k=Kokoro('/root/.cache/hyperframes/tts/models/kokoro-v1.0.onnx','/root/.cache/hyperframes/tts/voices/voices-v1.0.bin')
SPEED=0.82; GAP=0.45; LEAD=0.6
out=[]; meta=[]; t=LEAD; sr=None
for i,(ch,text,pause) in enumerate(LINES):
    spoken=text.replace('"','').replace('Om','Ohm')
    samples,sr=k.create(spoken,voice='bm_george',speed=SPEED,lang='en-gb')
    # trim leading/trailing near-silence
    a=np.abs(samples); idx=np.where(a>0.01)[0]
    if len(idx): samples=samples[max(0,idx[0]-int(0.03*sr)):idx[-1]+int(0.08*sr)]
    d=len(samples)/sr
    meta.append({"i":i+1,"chapter":ch,"text":text,"start":round(t,3),"dur":round(d,3)})
    out.append(samples); t+=d
    g=GAP+pause
    out.append(np.zeros(int(g*sr),dtype=samples.dtype)); t+=g
    print(i+1, round(d,2), flush=True)
lead=np.zeros(int(LEAD*sr),dtype=out[0].dtype)
audio=np.concatenate([lead]+out+[np.zeros(int(1.5*sr),dtype=out[0].dtype)])
sf.write('vo.wav',audio,sr)
json.dump({"sr":sr,"total":round(len(audio)/sr,3),"lines":meta},open('vo_timing.json','w'),indent=1)
print('TOTAL',len(audio)/sr)
