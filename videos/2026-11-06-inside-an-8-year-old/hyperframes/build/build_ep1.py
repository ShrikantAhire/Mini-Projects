"""Build the Episode 1 HyperFrames project from ep1-vo-timing.json and scenes_a/b."""
import json, os, re, shutil, subprocess, importlib
from frame import Sc, js
from rig import EXPR
HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", "project"))
REPO = "/home/user/Mini-Projects/videos/2026-11-06-inside-an-8-year-old"
SFXDIR = "/tmp/claude-0/-home-user-Mini-Projects/cfcad8a0-fce0-5fdb-a25c-c2f339edee7f/scratchpad/hf/.claude/skills/media-use/audio/assets/sfx"
TIM = json.load(open(f"{REPO}/voiceover/ep1-vo-timing.json"))
SC = {}
for m in ("scenes_a", "scenes_b"): SC.update(importlib.import_module(m).SC)
SLUG = {"COLD OPEN": "coldopen", "THE FEELINGS METER": "meter", "PHOTO DAY": "photo", "THE TEST": "test", "HOME": "home",
        "WHAT SCIENCE SAYS": "science", "FOR PARENTS AND TEACHERS": "parents", "CLIFFHANGER": "cliff"}
LINES = []; i = 0
for sec in TIM:
    for l in sec["lines"]:
        i += 1; LINES.append(dict(i=i, chapter=SLUG[sec["section"]], text=l["text"], start=l["start"], dur=round(l["end"] - l["start"], 3)))
os.makedirs(f"{PROJ}/assets/sfx", exist_ok=True); os.makedirs(f"{PROJ}/compositions", exist_ok=True)
vo = f"{PROJ}/assets/vo.wav"
subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-i", f"{REPO}/voiceover/ep1-voiceover.mp3", "-ar", "48000", vo])
TOTAL = round(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", vo]).decode()), 3)
CH = []
for l in LINES:
    if l["chapter"] not in CH: CH.append(l["chapter"])
cs = {c: (0.0 if k == 0 else round([l for l in LINES if l["chapter"] == c][0]["start"] - 0.35, 3)) for k, c in enumerate(CH)}
ce = {c: (cs[CH[k + 1]] if k + 1 < len(CH) else TOTAL) for k, c in enumerate(CH)}
all_sfx = []; missing = []
for c in CH:
    ls = [l for l in LINES if l["chapter"] == c]
    starts = [cs[c]] + [round(l["start"] - 0.25, 3) for l in ls[1:]]
    html, tws = [], []
    for k, l in enumerate(ls):
        st = starts[k]; en = starts[k + 1] if k + 1 < len(starts) else ce[c]
        d = round(en - st, 3); v = round(l["start"] - st, 3)
        s = Sc(l["i"], d, v, l["dur"], l["text"])
        f = SC.get(l["i"])
        if f: f(s)
        else:
            missing.append(l["i"]); s.bg("#FFFFFF")
        for cid, e in s.chars:
            if d > 3.2 and min(s.swaps.get(cid, [99])) > 1.9 and not EXPR[e][5]:
                s.ft(f"#{cid}-face-{e}-eyes", {"scaleY": 1, "transformOrigin": "50% 50%"}, {"scaleY": 0.1, "repeat": 1, "yoyo": True}, 1.55, 0.07, "none")
        loc = round(st - cs[c], 3)
        html.append(f'<div id="s{l["i"]}" class="clip scene" data-start="{loc}" data-duration="{d}" data-track-index="{k%2}"><div id="s{l["i"]}-cam" class="cam"><svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">{"".join(s.parts)}</svg></div></div>')
        first = {}
        for (kind, sel, a, b, at) in s.tw:
            if kind == "ft": first[sel] = min(first.get(sel, 1e9), at)
        for (kind, sel, a, b, at) in s.tw:
            tt = round(loc + max(0, at), 3)
            if tt >= loc + d: continue
            if kind == "ft":
                bb = dict(b)
                if at > first[sel]: bb["immediateRender"] = False
                tws.append(f'tl.fromTo("{sel}",{js(a)},{js(bb)},{tt});')
            else: tws.append(f'tl.set("{sel}",{js(a)},{tt});')
        for (name, at, vol) in s.sfxs: all_sfx.append((name, round(st + at, 3), vol))
    comp = f'''<template>
<style>
#root{{position:absolute;inset:0;overflow:hidden;background:#FAF7F2}}
#root .scene{{position:absolute;inset:0}}
#root .cam{{position:absolute;inset:0;will-change:transform}}
#root svg{{position:absolute;left:0;top:0;overflow:visible}}
#root text{{font-family:Nunito,sans-serif}}
</style>
<div id="root" data-composition-id="{c}" data-width="1920" data-height="1080">
{chr(10).join(html)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tws)}
window.__timelines["{c}"] = tl;
</script>
</template>'''
    open(f"{PROJ}/compositions/{c}.html", "w").write(comp)

# captions (word timing estimated from character length within each line)
AMBERW = {"meter", "capable", "specific", "birthday", "laugh", "comparing", "normal"}
REDW = {"shortest", "smaller", "short", "rabbit", "club", "drops", "ranking", "list"}
groups = []
for l in LINES:
    words = l["text"].split(); lens = [len(w) + 1 for w in words]; tot = sum(lens); t = l["start"]; times = []
    for w, n in zip(words, lens):
        dd = l["dur"] * n / tot; times.append((w, t, t + dd)); t += dd
    cur = []
    for k, (w, a, b) in enumerate(times):
        cur.append((w, a, b))
        if len(cur) >= 6 or (re.search(r'[.,:;?!]"?$', w) and len(cur) >= 3) or k == len(times) - 1:
            groups.append(cur); cur = []
cap_html, cap_tw = [], []
for gi, gr in enumerate(groups):
    a = round(gr[0][1] - 0.05, 3); b = round(gr[-1][2] + 0.1, 3)
    if gi + 1 < len(groups): b = min(b, round(groups[gi + 1][0][1] - 0.06, 3))
    spans = []
    for wi, (w, ws, we) in enumerate(gr):
        key = re.sub(r"[^a-z]", "", w.lower())
        cls = "w" + (" am" if key in AMBERW else " rd" if key in REDW else "")
        spans.append(f'<span id="c{gi}w{wi}" class="{cls}">{w.replace("&","&amp;")}</span>')
        cap_tw.append(f'tl.fromTo("#c{gi}w{wi}",{{opacity:0.35}},{{opacity:1,duration:0.08,ease:"none"}},{round(ws,3)});')
    cap_html.append(f'<div id="cg{gi}" class="clip cg" data-start="{a}" data-duration="{round(b-a,3)}" data-track-index="0"><div class="line">{" ".join(spans)}</div></div>')
cap = f'''<template>
<style>
#root{{position:absolute;inset:0;pointer-events:none}}
#root .cg{{position:absolute;left:0;right:0;bottom:46px;text-align:center}}
#root .line{{display:inline-block;font-family:Nunito,sans-serif;font-weight:800;font-size:58px;line-height:1.15;color:#1A1A1A;-webkit-text-stroke:10px #FAF7F2;paint-order:stroke fill;max-width:1600px}}
#root .am{{color:#F08C00;-webkit-text-stroke:10px #1A1A1A}}
#root .rd{{color:#E03131;-webkit-text-stroke:10px #FAF7F2}}
</style>
<div id="root" data-composition-id="captions" data-width="1920" data-height="1080">
{chr(10).join(cap_html)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(cap_tw)}
window.__timelines["captions"] = tl;
</script>
</template>'''
open(f"{PROJ}/compositions/captions.html", "w").write(cap)
hosts = [f'<div id="{c}" data-composition-id="{c}" data-composition-src="compositions/{c}.html" data-start="{cs[c]}" data-duration="{round(ce[c]-cs[c],3)}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080" style="z-index:1"></div>' for c in CH]
hosts.append(f'<div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{TOTAL}" data-track-index="2" data-track-kind="captions" data-width="1920" data-height="1080" style="z-index:5"></div>')
aud = [f'<audio id="vo" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-volume="1" src="assets/vo.wav"></audio>']
for j, (name, at, vol) in enumerate(sorted(all_sfx, key=lambda x: x[1])):
    src = f"{SFXDIR}/{name}.mp3"
    if not os.path.exists(src): print("missing sfx", name); continue
    shutil.copy(src, f"{PROJ}/assets/sfx/{name}.mp3")
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src]).decode())
    dur = min(dur, round(TOTAL - at, 3))
    aud.append(f'<audio id="fx{j}" class="clip" data-start="{at}" data-duration="{round(dur,3)}" data-track-index="{4+j%3}" data-volume="{vol}" src="assets/sfx/{name}.mp3"></audio>')
idx = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1920, height=1080" />
<script src="assets/gsap.min.js"></script>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:#FAF7F2}}
#bgfill{{position:absolute;inset:0;background:#FAF7F2}}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
<div id="bgfill"></div>
{chr(10).join(hosts)}
{chr(10).join(aud)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
window.__timelines["main"] = tl;
</script>
</body>
</html>'''
open(f"{PROJ}/index.html", "w").write(idx)
print("total", TOTAL, "chapters", {c: (cs[c], ce[c]) for c in CH})
print("scenes", len(LINES), "missing", missing, "sfx", len(all_sfx), "captions", len(groups))
