# /// script
# dependencies = ["soundfile", "numpy"]
# ///
# 100 Hz mouth-open envelope of the placed VO -> lipsync.json
import json, soundfile as sf, numpy as np
s, sr = sf.read('audio/vo.wav'); hop = sr // 100
n = len(s) // hop
rms = np.array([np.sqrt(np.mean(s[i*hop:(i+1)*hop]**2)) for i in range(n)])
db = 20*np.log10(rms + 1e-9); env = np.clip((db + 42) / 26, 0, 1)
# light smoothing + a little chatter so the mouth reads as syllables
env = np.convolve(env, np.ones(3)/3, mode='same')
json.dump({'fps': 100, 'env': [round(float(x), 3) for x in env]}, open('lipsync.json', 'w'))
print(n, 'frames, mean', env.mean().round(3))
