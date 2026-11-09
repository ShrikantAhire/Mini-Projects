"""Cut Shorts from the main video's voiceover: line ranges -> one audio file + a spec for build_shorts.py."""
import json, subprocess, numpy as np, soundfile as sf
T = json.load(open('vo_timing.json'))['lines']
VO = '../project/assets/vo.wav'
CLIPS = {
 "clip1-head":    (["What goes through a shy", "kid's head before \"hi\""], [(1,3),(5,5),(19,30)]),
 "clip2-liking":  (["Kids think they're", "less liked than they are"], [(40,49)]),
 "clip3-reject":  (["How the fear of rejection", "makes itself come true"], [(50,62)]),
 "clip4-parents": (["3 things to do for", "a shy child"], [(78,89)]),
 "clip5-mirror":  (["Why a friendly smile can", "look like teasing"], [(71,77)]),
}
audio, sr = sf.read(VO)
if audio.ndim > 1: audio = audio.mean(axis=1)
spec = {}
for name, (title, ranges) in CLIPS.items():
    parts = []; segs = []; pos = 0.0
    for (a, b) in ranges:
        c0 = max(0, T[a-1]['start'] - 0.12); c1 = T[b-1]['start'] + T[b-1]['dur'] + 0.25
        parts.append(audio[int(c0*sr):int(c1*sr)])
        for i in range(a, b+1):
            l = T[i-1]; s0 = l['start'] - c0 + pos
            segs.append((l['text'], round(s0, 3), round(s0 + l['dur'], 3), i))
        pos += c1 - c0
        parts.append(np.zeros(int(0.35*sr))); pos += 0.35
    clip = np.concatenate(parts[:-1]); pos -= 0.35
    sf.write(f'el/{name}.wav', clip, sr)
    spec[name] = {"title": title, "dur": round(len(clip)/sr, 3), "segs": segs}
    print(name, round(len(clip)/sr, 1), 's', len(segs), 'lines')
open('clips_spec.py','w').write('SHORTS = ' + repr(spec) + '\n')
