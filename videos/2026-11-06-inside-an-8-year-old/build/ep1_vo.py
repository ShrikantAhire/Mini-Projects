"""Generate the Episode 1 voiceover with Kokoro (voice am_fenrir).

Reads the VO blocks from ep1-script.md, makes one clip per sentence, joins them
with pauses, and writes ep1-voiceover.mp3 plus ep1-vo-timing.json (start/end of
every sentence and section, for syncing the animation later).
Usage: python ep1_vo.py <kokoro-model.onnx> <voices.bin> <out_dir>
"""
import json, re, subprocess, sys, os
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "ep1-script.md")
VOICE, SPEED = "am_fenrir", 0.95
GAP_SENT, GAP_PARA, GAP_SECT = 0.35, 0.7, 1.3

# Spoken forms, so the TTS reads numbers and titles the way a narrator would.
SAY = [
    (r"\bMs\. ", "Miz "),
    (r"8-Year-Old", "eight-year-old"),
    (r"\b1980\b", "nineteen eighty"), (r"\b2006\b", "two thousand six"),
    (r"\b1950\b", "nineteen fifty"),
    (r"\bTV\b", "T.V."),
    (r"\bAva\b", "Aiva"),  # Kokoro reads Ava as "AH-va"
]

def spoken(t):
    for a, b in SAY:
        t = re.sub(a, b, t)
    return t

def sections():
    md = open(SCRIPT, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^## \[(\d+:\d+)\] (.+?)\n(.*?)(?=^## |\Z)", md, re.S | re.M):
        body = m.group(3)
        if "**VO:**" not in body:
            continue
        vo = body.split("**VO:**", 1)[1].split("**VISUAL:**", 1)[0].strip()
        paras = [p.strip() for p in re.split(r"\n\s*\n", vo) if p.strip()]
        lines = [[l.strip() for l in p.splitlines() if l.strip()] for p in paras]
        out.append({"time": m.group(1), "title": m.group(2).strip(), "paras": lines})
    return out

def main(model, voices, out_dir):
    k = Kokoro(model, voices)
    audio, timing, t, sr = [], [], 0.0, 24000
    secs = sections()
    for si, sec in enumerate(secs):
        st = {"section": sec["title"], "script_time": sec["time"], "start": round(t, 2), "lines": []}
        for pi, para in enumerate(sec["paras"]):
            for li, line in enumerate(para):
                s, sr = k.create(spoken(line), voice=VOICE, speed=SPEED, lang="en-us")
                audio.append(s)
                st["lines"].append({"text": line, "start": round(t, 2), "end": round(t + len(s) / sr, 2)})
                t += len(s) / sr
                last = li == len(para) - 1
                gap = GAP_SENT if not last else (GAP_PARA if pi < len(sec["paras"]) - 1 else (GAP_SECT if si < len(secs) - 1 else 0.8))
                audio.append(np.zeros(int(sr * gap), dtype=s.dtype)); t += gap
        st["end"] = round(t, 2)
        timing.append(st)
        print(f'{sec["title"]:<28} {st["start"]:7.1f}s -> {st["end"]:7.1f}s')
    wav = os.path.join(out_dir, "ep1-voiceover.wav")
    sf.write(wav, np.concatenate(audio), sr)
    subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-i", wav, "-af", "loudnorm=I=-16:TP=-1.5",
                           "-ar", "44100", "-b:a", "128k", os.path.join(out_dir, "ep1-voiceover.mp3")])
    json.dump(timing, open(os.path.join(out_dir, "ep1-vo-timing.json"), "w"), indent=1)
    print(f"Total {t/60:.0f}:{t%60:04.1f}")

if __name__ == "__main__":
    main(*sys.argv[1:4])
