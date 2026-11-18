# /// script
# dependencies = ["soundfile", "numpy", "scipy"]
# ///
# Places each VO line on the half-beat grid after the previous one; writes audio/vo.wav + vo_timeline.json
import json, math, soundfile as sf, numpy as np
from scipy.signal import resample_poly
B = json.load(open('beats.json')); P = B['period']; OFF = B['offset']
script = json.load(open('audio/script.json'))
GAP = {'n2': .25, 'n3': .45, 'c1': .3, 'v1': .15, 'n4': .35, 'n5': .4, 'n6': .4, 'n7': .15, 'c2': .3, 'v2': .1, 'n8': .35, 'n9': .35}
SR = 48000; out = np.zeros(int(60 * SR)); tl = []; t = 0.15
for key, voice, lang, text in script:
    s, sr = sf.read(f'audio/vo/{key}.wav')
    s = resample_poly(s, SR, sr)
    if tl:
        ideal = tl[-1]['end'] + GAP.get(key, .3)
        half = P / 2
        t = OFF + math.ceil((ideal - OFF) / half - 0.35) * half   # snap to half-beat, allow slightly early
        t = max(t, tl[-1]['end'] + 0.08)
    i = int(t * SR); out[i:i + len(s)] += s * (1.0 if key[0] == 'n' else 1.05)
    tl.append({'key': key, 'start': round(t, 3), 'end': round(t + len(s) / SR, 3), 'text': text, 'voice': voice})
for r in tl: print(f"{r['key']:3} {r['start']:6.2f}-{r['end']:6.2f}  beat {(r['start']-OFF)/P:6.2f}")
assert tl[-1]['end'] < 59.0, 'runs long'
peak = np.max(np.abs(out)); out = out / peak * 0.89
sf.write('audio/vo.wav', out.astype(np.float32), SR)
json.dump(tl, open('vo_timeline.json', 'w'), ensure_ascii=False, indent=1)
