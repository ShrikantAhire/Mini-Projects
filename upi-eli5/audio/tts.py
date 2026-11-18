# /// script
# dependencies = ["kokoro-onnx>=0.4", "soundfile", "numpy"]
# ///
import sys, json, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
model_dir, script, outdir = sys.argv[1:4]
speed = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
k = Kokoro(model_dir + '/kokoro-v1.0.onnx', model_dir + '/voices-v1.0.bin')
tot = 0
for key, voice, lang, text in json.load(open(script)):
    s, sr = k.create(text, voice=voice, speed=speed, lang=lang)
    # trim leading/trailing silence
    a = np.abs(s); thr = 0.01; idx = np.where(a > thr)[0]
    s = s[max(idx[0]-int(.02*sr),0): idx[-1]+int(.05*sr)]
    sf.write(f'{outdir}/{key}.wav', s, sr); d = len(s)/sr; tot += d
    print(f'{key:3} {d:5.2f}s  {len(text.split()):3}w')
print('total speech', round(tot,2))
