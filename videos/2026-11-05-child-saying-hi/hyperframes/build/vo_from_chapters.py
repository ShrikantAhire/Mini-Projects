"""Build vo.wav + vo_timing.json from one MP3 per chapter (el/<chapter>.mp3).
Each chapter is split into its script lines at the longest pauses, then re-joined
with consistent gaps, so every scene keeps its own start time."""
import json, re, subprocess, sys, os
import numpy as np, soundfile as sf
sys.path.insert(0, '.')
from lines import LINES
SR = 44100; GAP_LINE = 0.45; GAP_CHAPTER = 0.7; LEAD = 0.6; PAUSE_EXTRA = 0.6
SRC = sys.argv[1] if len(sys.argv) > 1 else 'el'

def load(path):
    raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'])
    return np.frombuffer(raw, dtype=np.float32).copy()

def silences(a, thresh_db=-38, min_len=0.18):
    win = int(0.01 * SR); n = len(a) // win
    rms = np.sqrt(np.mean(a[:n * win].reshape(n, win) ** 2, axis=1) + 1e-12)
    db = 20 * np.log10(rms + 1e-9); quiet = db < thresh_db
    out = []; i = 0
    while i < n:
        if quiet[i]:
            j = i
            while j < n and quiet[j]: j += 1
            if (j - i) * 0.01 >= min_len: out.append((i * 0.01, j * 0.01))
            i = j
        else: i += 1
    return out

chapters = []
for c, t, p in LINES:
    if not chapters or chapters[-1][0] != c: chapters.append([c, []])
    chapters[-1][1].append((t, p))

pieces = []; meta = []; t = LEAD; idx = 0
pieces.append(np.zeros(int(LEAD * SR), np.float32))
for ci, (c, lines) in enumerate(chapters):
    a = load(os.path.join(SRC, f'{c}.mp3'))
    sil = [s for s in silences(a) if s[0] > 0.05 and s[1] < len(a) / SR - 0.05]
    need = len(lines) - 1
    if len(sil) < need:
        sys.exit(f'{c}: found {len(sil)} pauses, need {need}')
    # dynamic programming: pick `need` pauses so line lengths match the text lengths
    # and the chosen pauses are long ones
    nz = np.where(np.abs(a) > 0.01)[0]; a0, a1 = nz[0] / SR, nz[-1] / SR + 0.05
    chars = np.array([len(x[0]) for x in lines], float)
    rate = (a1 - a0 - sum(s[1] - s[0] for s in sil) * 0.3) / chars.sum()
    exp = chars * rate
    m = len(sil); INF = 1e18
    mids = [(x[0] + x[1]) / 2 for x in sil]; lens = [x[1] - x[0] for x in sil]
    def lc(k, st, en):
        d = en - st; return ((d - exp[k]) / max(exp[k], 0.8)) ** 2
    dp = [[INF] * m for _ in range(need)]; bp = [[-1] * m for _ in range(need)]
    for j in range(m):
        dp[0][j] = lc(0, a0, sil[j][0]) - 0.8 * lens[j]
    for k in range(1, need):
        for j in range(m):
            for i in range(j):
                if dp[k - 1][i] >= INF: continue
                v = dp[k - 1][i] + lc(k, sil[i][1], sil[j][0]) - 0.8 * lens[j]
                if v < dp[k][j]: dp[k][j] = v; bp[k][j] = i
    best = INF; bj = -1
    for j in range(m):
        if dp[need - 1][j] >= INF: continue
        v = dp[need - 1][j] + lc(need, sil[j][1], a1)
        if v < best: best = v; bj = j
    chosen = []; k = need - 1; j = bj
    while k >= 0: chosen.append(sil[j]); j = bp[k][j]; k -= 1
    chosen.sort()
    # trim leading/trailing silence of the chapter
    bounds = [a0] + [x for s in chosen for x in (s[0] + 0.04, s[1] - 0.04)] + [a1]
    for k, (text, pause) in enumerate(lines):
        s0, s1 = bounds[2 * k], bounds[2 * k + 1]
        seg = a[int(s0 * SR):int(s1 * SR)]
        idx += 1
        meta.append({'i': idx, 'chapter': c, 'text': text, 'start': round(t, 3), 'dur': round(len(seg) / SR, 3)})
        pieces.append(seg); t += len(seg) / SR
        last_in_ch = k == len(lines) - 1
        g = (GAP_CHAPTER if last_in_ch else GAP_LINE) + (PAUSE_EXTRA if pause else 0)
        pieces.append(np.zeros(int(g * SR), np.float32)); t += g
pieces.append(np.zeros(int(1.0 * SR), np.float32))
audio = np.concatenate(pieces)
sf.write('vo_raw.wav', audio, SR)
subprocess.check_call(['ffmpeg', '-v', 'error', '-y', '-i', 'vo_raw.wav', '-af', 'loudnorm=I=-15:TP=-1.5:LRA=11', '-ar', str(SR), 'vo.wav'])
total = round(len(audio) / SR, 3)
json.dump({'sr': SR, 'total': total, 'lines': meta}, open('vo_timing.json', 'w'), indent=1)
print('lines', len(meta), 'total', total)
