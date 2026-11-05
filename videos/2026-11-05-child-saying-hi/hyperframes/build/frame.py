import json
from rig import stick, baby, INK, PAPER, AMBER, RED
import props as P
BGC="#FAF7F2"
def js(o): return json.dumps(o)
class Sc:
    def __init__(s,n,d,v,vd):
        s.n=n; s.d=d; s.v=v; s.vd=vd; s.parts=[]; s.tw=[]; s.sfxs=[]; s.chars=[]; s.swaps={}
    def id(s,name): return f"s{s.n}-{name}"
    def at(s,frac): return round(s.v+frac*s.vd,3)
    def add(s,*svg): s.parts.extend(svg)
    # ---- characters
    def char(s,name,x,y,sc=1.0,kind="kid",exprs=("neutral",),poses=("stand",),legs=("stand",),**kw):
        cid=s.id(name); s.chars.append((cid,exprs[0]))
        s.add(stick(cid,x,y,sc,kind,exprs,poses,legs,**kw)); return name
    def baby(s,name,x,y,sc=1.0,expr="happy",look=(0,0)):
        s.add(baby(s.id(name),x,y,sc,expr,look)); return name
    # ---- tweens
    def ft(s,name,frm,to,at,dur=0.5,ease="power3.out"):
        sel=name if name.startswith("#") else "#"+s.id(name)
        t=dict(to); t["duration"]=dur; t["ease"]=ease
        s.tw.append(("ft",sel,frm,t,at))
    def set(s,name,props,at):
        sel=name if name.startswith("#") else "#"+s.id(name)
        s.tw.append(("set",sel,props,None,at))
    def pop(s,name,at,dur=0.45,origin="50% 50%",ease="back.out(1.7)"):
        s.ft(name,{"scale":0,"opacity":0,"transformOrigin":origin},{"scale":1,"opacity":1},at,dur,ease)
    def fadein(s,name,at,dur=0.4): s.ft(name,{"opacity":0},{"opacity":1},at,dur,"power2.out")
    def fadeout(s,name,at,dur=0.25): s.ft(name,{"opacity":1},{"opacity":0},at,dur,"power2.in")
    def rise(s,name,at,dy=50,dur=0.55): s.ft(name,{"y":dy,"opacity":0},{"y":0,"opacity":1},at,dur,"expo.out")
    def slidein(s,name,at,dx=-300,dur=0.6): s.ft(name,{"x":dx,"opacity":0},{"x":0,"opacity":1},at,dur,"expo.out")
    def shake(s,name,at,n=5,amp=8,dur=0.06):
        s.ft(name,{"x":-amp},{"x":amp,"repeat":n,"yoyo":True},at,dur,"sine.inOut")
        s.ft(name,{"x":amp},{"x":0},at+dur*(n+1),0.05,"none")
    def move(s,name,at,dur,frm,to,ease="power2.inOut"): s.ft(name,frm,to,at,dur,ease)
    def swap(s,cid,a,b,at,kind="f"):
        s.ft(f"#{cid}-{kind}-{a}",{"opacity":1},{"opacity":0},at,0.12,"none")
        s.ft(f"#{cid}-{kind}-{b}",{"opacity":0},{"opacity":1},at,0.12,"none")
        if kind=="f": s.swaps.setdefault(cid,[]).append(at)
    def face(s,name,a,b,at): s.swap(s.id(name),a,b,at,"f")
    def pose(s,name,a,b,at): s.swap(s.id(name),a,b,at,"arms")
    def legs(s,name,a,b,at): s.swap(s.id(name),a,b,at,"legs")
    def walk(s,name,at,dur,x0,x1,step=0.24,bob=True):
        """name's outer group translated in local units: pass deltas x0->x1 (screen px / scale handled by caller)."""
        s.ft(name,{"x":x0},{"x":x1},at,dur,"none")
        cid=s.id(name); t=at; k=0
        while t<at+dur-0.05:
            a,b=("walkA","walkB") if k%2==0 else ("walkB","walkA")
            s.set(f"#{cid}-legs-{a}",{"opacity":1},t); s.set(f"#{cid}-legs-{b}",{"opacity":0},t)
            t+=step; k+=1
        s.set(f"#{cid}-legs-walkA",{"opacity":0},at+dur); s.set(f"#{cid}-legs-walkB",{"opacity":0},at+dur)
        s.set(f"#{cid}-legs-stand",{"opacity":0},at); s.set(f"#{cid}-legs-stand",{"opacity":1},at+dur)
    def shakehead(s,name,at,n=3):
        s.ft(name+"-head",{"rotation":-9,"transformOrigin":"50% 100%"},{"rotation":9,"repeat":n,"yoyo":True},at,0.16,"sine.inOut")
        s.ft(name+"-head",{"rotation":9},{"rotation":0},at+0.16*(n+1),0.12,"power2.out")
    def nod(s,name,at):
        s.ft(name+"-head",{"rotation":0,"transformOrigin":"50% 100%"},{"rotation":6,"repeat":1,"yoyo":True},at,0.18,"sine.inOut")
    def cam(s,at,dur,frm,to,ease="power2.inOut"):
        s.tw.append(("ft",f"#s{s.n}-cam",frm,dict(to,duration=dur,ease=ease),at))
    def push(s,at,dur,scale=1.1,ox=960,oy=540):
        s.cam(at,dur,{"scale":1,"transformOrigin":f"{ox}px {oy}px"},{"scale":scale},"power1.inOut")
    def punch(s,at,scale=1.08,ox=960,oy=540):
        s.cam(at,0.12,{"scale":1,"transformOrigin":f"{ox}px {oy}px"},{"scale":scale},"power3.out")
        s.cam(at+0.12,0.4,{"scale":scale},{"scale":1},"power2.out")
    def draw(s,name,at,dur=0.6,length=3000):
        s.ft(name,{"strokeDasharray":length,"strokeDashoffset":length},{"strokeDashoffset":0},at,dur,"power2.inOut")
    def sfx(s,name,at,vol=0.35): s.sfxs.append((name,at,vol))
    # ---- backgrounds
    def bg(s,color=BGC): s.add(f'<rect x="0" y="0" width="1920" height="1080" fill="{color}"/>')
    def park(s,tree=True,bench=None,ground_col="#DCE8D2"):
        s.bg("#EEF4F8"); s.add(P.ground(ground_col,"#B9CDAA"))
        if tree: s.add(P.tree(1720,860,0.9))
        if bench is not None: s.add(P.bench(s.id("bench"),bench))
    def party(s):
        s.bg("#FCE4EA"); s.add(P.ground("#F2C9D3","#E0A8B6"))
        s.add(P.balloons(s.id("bl1"),220,520),P.balloons(s.id("bl2"),1700,500))
        s.add('<path d="M0 90 Q240 150 480 90 T960 90 T1440 90 T1920 90" fill="none" stroke="#E03131" stroke-width="5"/>')
        for i,x in enumerate(range(60,1920,120)):
            col=["#F08C00","#E03131","#0CA678","#1C7ED6"][i%4]
            s.add(f'<path d="M{x} {100+ (8 if i%2 else 0)} l24 0 l-12 34 Z" fill="{col}"/>')
    def classroom(s):
        s.bg("#F3EFE6"); s.add(P.ground("#D9CBB4","#C2B096")); s.add(P.blackboard(s.id("bb"),960,260))
    def home(s):
        s.bg("#FFF6EA"); s.add(P.ground("#E7D3B8","#CDB495")); s.add(P.window(s.id("win"),1600,330))
    def cafe(s):
        s.bg("#F6EFE6"); s.add(P.ground("#E2D2BE","#C9B49B"))
    def corridor(s):
        s.bg("#EAF0F2"); s.add(P.ground("#CBD5DB","#AAB7BF"))
        s.add('<line x1="0" y1="560" x2="1920" y2="560" stroke="#C7D2D8" stroke-width="6"/>')
    def nursery(s):
        s.bg("#F7F0FA"); s.add(P.ground("#E6D9EE","#CDB9DA")); s.add('<ellipse cx="960" cy="900" rx="760" ry="70" fill="#D8C4E6"/>')
    def kitchen(s):
        s.bg("#F4F7F5"); s.add(P.ground("#DDE3DF","#BFC9C3"))
    def office(s):
        s.bg("#EEF1F5"); s.add(P.ground("#D3D9E1","#B4BDC9"))
    def headroom(s):
        s.bg("#FFF8EE")
        s.add('<rect x="70" y="50" width="1780" height="800" rx="320" fill="#FFFFFF" stroke="#E6B980" stroke-width="8" stroke-dasharray="26 22"/>')
