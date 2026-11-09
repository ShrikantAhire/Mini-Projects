import json, os, re, shutil, subprocess, importlib, sys
from frame import Sc, js
SPEC=os.environ.get('SPEC','shorts_spec'); OUTDIR=os.environ.get('OUTDIR','shorts')
SHORTS=importlib.import_module(SPEC).SHORTS
SFXDIR=os.path.abspath("../.claude/skills/media-use/audio/assets/sfx")
SC={}
for m in ("scenes1","scenes2","scenes3","scenes4","scenes5"): SC.update(importlib.import_module(m).SC)
LEAD=0.3; TAIL=float(os.environ.get('TAIL','1.2'))
WIN_TOP=600; SCALE=0.6; WIN_H=int(1080*SCALE); LEFT=int((1080-1920*SCALE)/2)
AMBERW={"hi","steps","temperament","liking","gap","sociometer","mirror","secure","base","attempt","warm","loop"}
REDW={"kilometers","shy","risk","rejection","verdict","sensitivity","reject"}
only=sys.argv[1:] or list(SHORTS)
for name in only:
    sp=SHORTS[name]; P=os.path.abspath(f"../{OUTDIR}/{name}")
    os.makedirs(f"{P}/compositions",exist_ok=True); os.makedirs(f"{P}/assets/sfx",exist_ok=True)
    for f in ("package.json","hyperframes.json","meta.json"):
        if os.path.exists(f"../project/{f}") and not os.path.exists(f"{P}/{f}"): shutil.copy(f"../project/{f}",f"{P}/{f}")
    shutil.copy("../project/assets/gsap.min.js",f"{P}/assets/gsap.min.js")
    src=f"el/{name}.wav" if os.path.exists(f"el/{name}.wav") else f"el/{name}.mp3"
    if os.path.exists(src):
        subprocess.check_call(["ffmpeg","-v","error","-y","-i",src,"-af",f"adelay={int(LEAD*1000)}:all=1,loudnorm=I=-14:TP=-1.5:LRA=11","-ar","44100","-ac","1",f"{P}/assets/vo.wav"])
        audio_ok=True
    else:
        subprocess.check_call(["ffmpeg","-v","error","-y","-f","lavfi","-i","anullsrc=r=44100:cl=mono","-t",str(sp["dur"]+LEAD),f"{P}/assets/vo.wav"])
        audio_ok=False
    TOTAL=round(sp["dur"]+LEAD+TAIL,3)
    segs=sp["segs"]; starts=[0.0]+[round(LEAD+s[1]-0.15,3) for s in segs[1:]]
    html=[]; tws=[]; sfx=[]
    for k,(text,a,b,sid) in enumerate(segs):
        st=starts[k]; en=starts[k+1] if k+1<len(segs) else TOTAL
        d=round(en-st,3); v=round(LEAD+a-st,3); vd=round(b-a,3)
        s=Sc(sid,d,v,vd); SC[sid](s)
        first={}
        for (kind,sel,x,y,at) in s.tw:
            if kind=="ft": first[sel]=min(first.get(sel,1e9),at)
        for (kind,sel,x,y,at) in s.tw:
            tt=round(st+at,3)
            if tt>=st+d: continue
            if kind=="ft":
                yy=dict(y)
                if at>first[sel]: yy["immediateRender"]=False
                tws.append(f'tl.fromTo("{sel}",{js(x)},{js(yy)},{tt});')
            else: tws.append(f'tl.set("{sel}",{js(x)},{tt});')
        for (n,at,vol) in s.sfxs: sfx.append((n,round(st+at,3),vol))
        html.append(f'<div id="s{sid}" class="clip scene" data-start="{st}" data-duration="{d}" data-track-index="{k%2}"><div class="fit"><div id="s{sid}-cam" class="cam"><svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">{"".join(s.parts)}</svg></div></div></div>')
    comp=f'''<template>
<style>
#root{{position:absolute;inset:0;overflow:hidden;background:#FAF7F2}}
#root .scene{{position:absolute;left:0;top:{WIN_TOP}px;width:1080px;height:{WIN_H}px;overflow:hidden}}
#root .fit{{position:absolute;left:{LEFT}px;top:0;width:1920px;height:1080px;transform:scale({SCALE});transform-origin:0 0}}
#root .cam{{position:absolute;inset:0}}
#root svg{{position:absolute;left:0;top:0;overflow:visible}}
#root .hdr{{position:absolute;left:60px;right:60px;top:250px;text-align:center;font-family:Nunito,sans-serif;font-weight:900;font-size:70px;line-height:1.1;color:#1A1A1A}}
#root .hdr .l2{{color:#F08C00;-webkit-text-stroke:8px #1A1A1A;paint-order:stroke fill}}
</style>
<div id="root" data-composition-id="scenes" data-width="1080" data-height="1920">
<div id="hdr" class="hdr"><div>{sp["title"][0]}</div><div class="l2">{sp["title"][1]}</div></div>
{chr(10).join(html)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
tl.fromTo("#hdr",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.5,ease:"expo.out"}},0.1);
{chr(10).join(tws)}
window.__timelines["scenes"] = tl;
</script>
</template>'''
    open(f"{P}/compositions/scenes.html","w").write(comp)
    # captions: 2-4 word groups, centred under the scene window
    groups=[]
    for (text,a,b,sid) in segs:
        words=text.split(); lens=[len(w)+1 for w in words]; tot=sum(lens); t=LEAD+a; times=[]
        for w,n in zip(words,lens):
            dd=(b-a)*n/tot; times.append((w,t,t+dd)); t+=dd
        cur=[]
        for i,(w,x,y) in enumerate(times):
            cur.append((w,x,y))
            if len(cur)>=4 or (re.search(r'[.,:;?!]"?$',w) and len(cur)>=2) or i==len(times)-1: groups.append(cur); cur=[]
    ch=[]; ct=[]
    for gi,gr in enumerate(groups):
        a=round(gr[0][1]-0.05,3); b=round(gr[-1][2]+0.1,3)
        if gi+1<len(groups): b=min(b,round(groups[gi+1][0][1]-0.06,3))
        sp_=[]
        for wi,(w,ws,we) in enumerate(gr):
            key=re.sub(r"[^a-z]","",w.lower())
            cls="w"+(" am" if key in AMBERW else " rd" if key in REDW else "")
            sp_.append(f'<span id="c{gi}w{wi}" class="{cls}">{w.replace("&","&amp;")}</span>')
            ct.append(f'tl.fromTo("#c{gi}w{wi}",{{opacity:0.35}},{{opacity:1,duration:0.08,ease:"none"}},{round(ws,3)});')
        ch.append(f'<div id="cg{gi}" class="clip cg" data-start="{a}" data-duration="{round(b-a,3)}" data-track-index="0"><div class="line">{" ".join(sp_)}</div></div>')
    cap=f'''<template>
<style>
#root{{position:absolute;inset:0;pointer-events:none}}
#root .cg{{position:absolute;left:0;right:0;top:{WIN_TOP+WIN_H+70}px;text-align:center}}
#root .line{{display:inline-block;font-family:Nunito,sans-serif;font-weight:800;font-size:76px;line-height:1.15;color:#1A1A1A;-webkit-text-stroke:10px #FAF7F2;paint-order:stroke fill;max-width:900px}}
#root .am{{color:#F08C00;-webkit-text-stroke:10px #1A1A1A}}
#root .rd{{color:#E03131}}
</style>
<div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
{chr(10).join(ch)}
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(ct)}
window.__timelines["captions"] = tl;
</script>
</template>'''
    open(f"{P}/compositions/captions.html","w").write(cap)
    aud=[f'<audio id="vo" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-volume="1" src="assets/vo.wav"></audio>']
    for j,(n,at,vol) in enumerate(sorted(sfx,key=lambda x:x[1])):
        f=f"{SFXDIR}/{n}.mp3"
        if not os.path.exists(f): continue
        shutil.copy(f,f"{P}/assets/sfx/{n}.mp3")
        du=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).decode())
        aud.append(f'<audio id="fx{j}" class="clip" data-start="{at}" data-duration="{round(du,3)}" data-track-index="{4+j%3}" data-volume="{vol}" src="assets/sfx/{n}.mp3"></audio>')
    idx=f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" />
<script src="assets/gsap.min.js"></script>
<style>*{{margin:0;padding:0;box-sizing:border-box}} html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#FAF7F2}} #bgfill{{position:absolute;inset:0;background:#FAF7F2}}</style>
</head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
<div id="bgfill"></div>
<div id="scenes" data-composition-id="scenes" data-composition-src="compositions/scenes.html" data-start="0" data-duration="{TOTAL}" data-track-index="1" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index:1"></div>
<div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{TOTAL}" data-track-index="2" data-track-kind="captions" data-width="1080" data-height="1920" style="z-index:5"></div>
{chr(10).join(aud)}
</div>
<script>const tl = gsap.timeline({{ paused: true }}); window.__timelines["main"] = tl;</script>
</body></html>'''
    open(f"{P}/index.html","w").write(idx)
    print(name,"total",TOTAL,"segments",len(segs),"audio" if audio_ok else "PLACEHOLDER audio")
