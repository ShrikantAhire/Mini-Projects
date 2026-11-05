"""Build vo.wav + vo_timing.json from one MP3 per chapter (el/<chapter>.mp3).
Line boundaries come from ElevenLabs Scribe word timestamps (line_times.py),
snapped to the nearest real pause in the audio. Natural pauses inside a chapter are kept."""
import json, subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, '.')
from lines import LINES
from line_times import LT
SR = 44100; GAP_CHAPTER = 0.8; LEAD = 0.5; PAUSE_EXTRA = 0.6
SRC = sys.argv[1] if len(sys.argv) > 1 else 'el'

def load(path):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'])
    return np.frombuffer(raw, dtype=np.float32).copy()

def env_db(a):
    win = int(0.01 * SR); n = len(a) // win
    rms = np.sqrt(np.mean(a[:n * win].reshape(n, win) ** 2, axis=1) + 1e-12)
    return 20 * np.log10(rms + 1e-9)

def quietest_near(db, t, span=0.35):
    i0 = max(0, int((t - span) * 100)); i1 = min(len(db) - 1, int((t + span) * 100))
    seg = db[i0:i1 + 1]
    # pick centre of the longest run within 3 dB of the minimum
    m = seg.min(); ok = seg < m + 3
    best = (0, i0); j = 0
    while j < len(seg):
        if ok[j]:
            k = j
            while k < len(seg) and ok[k]: k += 1
            if k - j > best[0]: best = (k - j, i0 + (j + k) // 2)
            j = k
        else: j += 1
    return best[1] / 100

def speech_span(seg, thresh=0.01):
    nz = np.where(np.abs(seg) > thresh)[0]
    if len(nz) == 0: return 0, len(seg)
    return max(0, nz[0] - int(0.02 * SR)), min(len(seg), nz[-1] + int(0.06 * SR))

chapters = []
for c, t, p in LINES:
    if not chapters or chapters[-1][0] != c: chapters.append([c, []])
    chapters[-1][1].append((t, p))

pieces = [np.zeros(int(LEAD * SR), np.float32)]; meta = []; t = LEAD; idx = 0
for c, lines in chapters:
    a = load(os.path.join(SRC, f'{c}.mp3')); db = env_db(a); lt = LT[c]
    assert len(lt) == len(lines), (c, len(lt), len(lines))
    cuts = [0.0] + [quietest_near(db, (lt[k][1] + lt[k + 1][0]) / 2) for k in range(len(lines) - 1)] + [len(a) / SR]
    for k, (text, pause) in enumerate(lines):
        seg = a[int(cuts[k] * SR):int(cuts[k + 1] * SR)]
        if k == 0 or k == len(lines) - 1:  # trim chapter edges only
            s0, s1 = speech_span(seg)
            seg = seg[s0 if k == 0 else 0: s1 if k == len(lines) - 1 else len(seg)]
        on0, on1 = speech_span(seg)
        idx += 1
        meta.append({'i': idx, 'chapter': c, 'text': text, 'start': round(t + on0 / SR, 3), 'dur': round((on1 - on0) / SR, 3)})
        pieces.append(seg); t += len(seg) / SR
        g = (GAP_CHAPTER if k == len(lines) - 1 else 0) + (PAUSE_EXTRA if pause else 0)
        if g: pieces.append(np.zeros(int(g * SR), np.float32)); t += g
pieces.append(np.zeros(int(1.5 * SR), np.float32))
audio = np.concatenate(pieces)
sf.write('vo_raw.wav', audio, SR)
subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-i', 'vo_raw.wav', '-af', 'loudnorm=I=-15:TP=-1.5:LRA=11', '-ar', str(SR), 'vo.wav'])
total = round(len(audio) / SR, 3)
json.dump({'sr': SR, 'total': total, 'lines': meta}, open('vo_timing.json', 'w'), indent=1)
print('lines', len(meta), 'total', total)
