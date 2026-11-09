import json, os, re, shutil, importlib, sys
from frame import Sc, js
PROJ=os.path.abspath("../project")
SFXDIR=os.path.abspath("../.claude/skills/media-use/audio/assets/sfx")
T=json.load(open("vo_timing.json")); LINES=T["lines"]; TOTAL=round(T["total"],3)
SC={}
for m in ("scenes1","scenes2","scenes3","scenes4","scenes5"):
    try: SC.update(importlib.import_module(m).SC)
    except ModuleNotFoundError: pass
CH_ORDER=[]; 
for l in LINES:
    if l["chapter"] not in CH_ORDER: CH_ORDER.append(l["chapter"])
ch_start={}
for c in CH_ORDER:
    first=[l for l in LINES if l["chapter"]==c][0]
    ch_start[c]=0.0 if c==CH_ORDER[0] else round(first["start"]-0.35,3)
ch_end={c:(ch_start[CH_ORDER[i+1]] if i+1<len(CH_ORDER) else TOTAL) for i,c in enumerate(CH_ORDER)}

os.makedirs(f"{PROJ}/compositions",exist_ok=True); os.makedirs(f"{PROJ}/assets/sfx",exist_ok=True)
shutil.copy("vo.wav",f"{PROJ}/assets/vo.wav")
all_sfx=[]
for c in CH_ORDER:
    ls=[l for l in LINES if l["chapter"]==c]
    cs,ce=ch_start[c],ch_end[c]
    starts=[cs]+[round(l["start"]-0.25,3) for l in ls[1:]]
    html_scenes=[]; tws=[]
    for k,l in enumerate(ls):
        st=starts[k]; en=starts[k+1] if k+1<len(starts) else ce
        d=round(en-st,3); v=round(l["start"]-st,3)
        s=Sc(l["i"],d,v,l["dur"])
        f=SC.get(l["i"])
        if f: f(s)
        else:
            s.bg("#FFFFFF"); from props import text; s.add(text(s.id("ph"),960,500,f"Scene {l['i']}",80))
        # auto blink
        for cid,e in s.chars:
            from rig import EXPR
            if d>3.2 and min(s.swaps.get(cid,[99]))>1.9 and not EXPR[e][5]:
                s.ft(f"#{cid}-face-{e}-eyes",{"scaleY":1,"transformOrigin":"50% 50%"},{"scaleY":0.1,"repeat":1,"yoyo":True},1.55,0.07,"none")
        loc=round(st-cs,3)
        html_scenes.append(f'<div id="s{l["i"]}" class="clip scene" data-start="{loc}" data-duration="{d}" data-track-index="{k%2}"><div id="s{l["i"]}-cam" class="cam"><svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">{"".join(s.parts)}</svg></div></div>')
        first={}
        for (kind,sel,a,b,at) in s.tw:
            if kind=="ft": first[sel]=min(first.get(sel,1e9),at)
        for (kind,sel,a,b,at) in s.tw:
            tt=round(loc+at,3)
            if tt>=loc+d: continue
            if kind=="ft":
                bb=dict(b)
                if at>first[sel]: bb["immediateRender"]=False
                tws.append(f'tl.fromTo("{sel}",{js(a)},{js(bb)},{tt});')
            else: tws.append(f'tl.set("{sel}",{js(a)},{tt});')
        for (name,at,vol) in s.sfxs: all_sfx.append((name,round(st+at,3),vol))
    comp=f'''<template>
<style>
#root{{position:absolute;inset:0;overflow:hidden;background:#FAF7F2}}
#root .scene{{position:absolute;inset:0}}
#root .cam{{position:absolute;inset:0;will-change:transform}}
#root svg{{position:absolute;left:0;top:0;overflow:visible}}
#root text{{font-family:Nunito,sans-serif}}
</style>
<div id="root" data-composition-id="{c}" data-width="1920" data-height="1080">
{chr(10).join(html_scenes)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tws)}
window.__timelines["{c}"] = tl;
</script>
</template>'''
    open(f"{PROJ}/compositions/{c}.html","w").write(comp)

# ---------------- captions
AMBERW={"hi","steps","temperament","liking","gap","sociometer","mirror","secure","base","attempt","warm"}
REDW={"kilometres","shy","risk","rejection","verdict","loop","sensitivity","reject"}
groups=[]
for l in LINES:
    words=l["text"].split()
    lens=[len(w)+1 for w in words]; tot=sum(lens); t=l["start"]; times=[]
    for w,n in zip(words,lens):
        dd=l["dur"]*n/tot; times.append((w,t,t+dd)); t+=dd
    cur=[]
    for i,(w,a,b) in enumerate(times):
        cur.append((w,a,b))
        if len(cur)>=6 or re.search(r'[.,:;?!]"?$',w) and len(cur)>=3 or i==len(times)-1:
            groups.append(cur); cur=[]
    if cur: groups.append(cur)
cap_html=[]; cap_tw=[]
for gi,gr in enumerate(groups):
    a=round(gr[0][1]-0.05,3); b=round(gr[-1][2]+0.1,3)
    if gi+1<len(groups): b=min(b,round(groups[gi+1][0][1]-0.06,3))
    spans=[]
    for wi,(w,ws,we) in enumerate(gr):
        key=re.sub(r"[^a-z]","",w.lower())
        cls="w"+(" am" if key in AMBERW else " rd" if key in REDW else "")
        spans.append(f'<span id="c{gi}w{wi}" class="{cls}">{w.replace("&","&amp;")}</span>')
        cap_tw.append(f'tl.fromTo("#c{gi}w{wi}",{{opacity:0.35}},{{opacity:1,duration:0.08,ease:"none"}},{round(ws,3)});')
    cap_html.append(f'<div id="cg{gi}" class="clip cg" data-start="{a}" data-duration="{round(b-a,3)}" data-track-index="0"><div class="line">{" ".join(spans)}</div></div>')
cap=f'''<template>
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
open(f"{PROJ}/compositions/captions.html","w").write(cap)

# ---------------- index
hosts=[]
for i,c in enumerate(CH_ORDER):
    hosts.append(f'<div id="{c}" data-composition-id="{c}" data-composition-src="compositions/{c}.html" data-start="{ch_start[c]}" data-duration="{round(ch_end[c]-ch_start[c],3)}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080" style="z-index:1"></div>')
hosts.append(f'<div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{TOTAL}" data-track-index="2" data-track-kind="captions" data-width="1920" data-height="1080" style="z-index:5"></div>')
aud=[f'<audio id="vo" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-volume="1" src="assets/vo.wav"></audio>']
used=set()
for j,(name,at,vol) in enumerate(sorted(all_sfx,key=lambda x:x[1])):
    src=f"{SFXDIR}/{name}.mp3"
    if not os.path.exists(src): continue
    shutil.copy(src,f"{PROJ}/assets/sfx/{name}.mp3"); used.add(name)
    import subprocess
    dur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",src]).decode().strip())
    aud.append(f'<audio id="fx{j}" class="clip" data-start="{at}" data-duration="{round(dur,3)}" data-track-index="{4+j%3}" data-volume="{vol}" src="assets/sfx/{name}.mp3"></audio>')
idx=f'''<!doctype html>
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
open(f"{PROJ}/index.html","w").write(idx)
print("chapters",{c:(ch_start[c],ch_end[c]) for c in CH_ORDER}); print("scenes built",len(SC),"sfx",len(all_sfx),"caption groups",len(groups))
