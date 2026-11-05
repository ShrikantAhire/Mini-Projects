import props as P
from rig import INK, AMBER, RED, PAPER
from scenes1 import kids_group, park_om, CAPS
from scenes2 import research_card
SC={}
def scene(n):
    def deco(f): SC[n]=f; return f
    return deco

# ---------------- SELF-ACCEPTANCE
@scene(63)
def _(s):
    s.bg()
    s.add(f'<g id="{s.id("c1")}"><circle cx="600" cy="400" r="230" fill="#FFF4E0" stroke="{INK}" stroke-width="7"/>'+P.text(s.id("c1a"),600,385,"How I",60,INK)+P.text(s.id("c1b"),600,455,"see me",60,INK)+'</g>')
    s.add(f'<g id="{s.id("c2")}"><circle cx="1320" cy="400" r="230" fill="#FFF4E0" stroke="{INK}" stroke-width="7"/>'+P.text(s.id("c2a"),1320,385,"How accepted",54,INK)+P.text(s.id("c2b"),1320,455,"I feel",60,INK)+'</g>')
    s.add(P.chain(s.id("ch"),960,400))
    s.char("om",960,860,0.6,"om",("thinking",),("think",),look=(0,-6))
    s.pop("c1",s.at(0.35)); s.pop("c2",s.at(0.7)); s.pop("ch",s.at(0.85)); s.sfx("click-soft",s.at(0.85),0.3)

@scene(64)
def _(s): research_card(s,"Mark Leary and colleagues, 1995","Sociometer theory")

def gauge_scene(s,val,om_expr=("neutral",),om_pose=("stand",),gx=1300,label="Am I accepted?"):
    s.bg()
    s.char("om",600,860,1.1,"om",om_expr,om_pose,look=(8,0))
    s.add(P.gauge(s.id("g"),gx,560,260,s.id("nd"),label,val,48))

@scene(65)
def _(s):
    gauge_scene(s,0.5)
    s.pop("g",s.at(0.2))
    s.ft("nd",{"rotation":-30,"svgOrigin":"0 0"},{"rotation":20,"repeat":5,"yoyo":True},s.at(0.4),0.5,"sine.inOut")

@scene(66)
def _(s):
    gauge_scene(s,0.5)
    s.add(f'<path id="{s.id("a1")}" d="M1000 330 A330 330 0 0 1 1600 330" fill="none" stroke="{AMBER}" stroke-width="12" stroke-linecap="round"/><path id="{s.id("a2")}" d="M1600 700 A330 330 0 0 1 1000 700" fill="none" stroke="{AMBER}" stroke-width="12" stroke-linecap="round"/>')
    s.add(f'<path id="{s.id("h1")}" d="M1570 300 L1604 334 L1560 350" fill="none" stroke="{AMBER}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path id="{s.id("h2")}" d="M1030 730 L996 696 L1040 680" fill="none" stroke="{AMBER}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>')
    s.draw("a1",s.at(0.1),0.6,1100); s.draw("a2",s.at(0.35),0.6,1100); s.fadein("h1",s.at(0.1)+0.55,0.1); s.fadein("h2",s.at(0.35)+0.55,0.1)

@scene(67)
def _(s):
    s.bg()
    s.char("om",520,860,1.0,"om",("neutral","happy"),("stand","highfive"),look=(8,0))
    s.char("kid",760,860,1.0,"kid",("happy",),("stand","highfive"),cap=CAPS[2],flip=True)
    s.add(P.gauge(s.id("g"),1400,560,240,s.id("nd"),"Am I accepted?",0.5,44))
    t=s.at(0.15); s.pose("om","stand","highfive",t); s.pose("kid","stand","highfive",t)
    s.add(f'<g id="{s.id("spark")}"><path d="M640 330 l12 -40 l12 40 l40 12 l-40 12 l-12 40 l-12 -40 l-40 -12 Z" fill="#FFD43B" stroke="{INK}" stroke-width="4"/></g>')
    s.pop("spark",t+0.2,0.3); s.sfx("click",t+0.2,0.35); s.face("om","neutral","happy",t+0.25)
    s.ft("nd",{"rotation":0,"svgOrigin":"0 0"},{"rotation":-90+180*0.88},t+0.3,0.9,"back.out(1.6)")

@scene(68)
def _(s):
    s.park(bench=None)
    s.char("om",380,860,1.0,"om",("worried",),("clasp",),look=(8,0))
    s.add(P.gauge(s.id("g"),380,300,110,s.id("nd"),"",0.18))
    s.char("k1",950,860,0.85,"kid",("neutral",),("stand",),cap=CAPS[0])
    s.char("k2",1300,860,0.85,"kid",("neutral",),("stand",),cap=CAPS[1],flip=True)
    s.char("k3",1650,860,0.85,"kid",("neutral",),("crossed",),cap=CAPS[3])
    for i,x in enumerate((950,1300,1650)):
        s.add(P.tag(s.id(f"t{i}"),x,(470,420,470)[i],"Rejection?",RED,"#FFFFFF",34))
        s.pop(f"t{i}",s.at(0.3+i*0.2)); s.sfx("pop",s.at(0.3+i*0.2),0.18)

@scene(69)
def _(s):
    s.park(bench=None)
    s.add(P.text(s.id("ok"),960,170,"I'm okay as I am",80,AMBER,stroke=INK,sw=7))
    kids_group(s,[700,820],sc=0.8,prefix="g1",poses=["crossed","stand"],exprs=("neutral",),flips=[True,True])
    kids_group(s,[1500,1620],sc=0.8,prefix="g2",poses=["wave","celebrate"],exprs=("happy",),flips=[True,True])
    s.add(f'<circle id="{s.id("glow")}" cx="380" cy="620" r="210" fill="{AMBER}" opacity="0.2"/>')
    s.char("om",380,860,1.0,"om",("neutral","happy"),("stand","shrug"),("stand","walkA","walkB"),look=(8,0))
    s.add(P.bubble(s.id("no"),760,400,180,110,"No",64,tail=(740,560)))
    s.rise("ok",0.2); s.pop("no",s.at(0.2))
    s.pose("om","stand","shrug",s.at(0.42)); s.face("om","neutral","happy",s.at(0.45))
    s.fadeout("no",s.at(0.5)); s.fadeout("glow",s.at(0.55))
    s.walk("om",s.at(0.58),s.d-s.at(0.58)-0.2,0,960,0.24)

@scene(70)
def _(s):
    s.bg()
    s.char("om",460,860,1.0,"om",("shocked",),("clasp",),look=(8,0))
    s.add(P.bubble(s.id("no"),1100,320,200,120,"No",70,tail=(560,500)))
    s.add(f'<g transform="translate(1300 600)"><rect x="-140" y="40" width="280" height="50" rx="10" fill="#8B5E3C" stroke="{INK}" stroke-width="6"/></g>')
    s.add(f'<g id="{s.id("gv")}">'+P.gavel(s.id("gvl"),1300,450)+'</g>')
    s.add(P.stamp(s.id("ver"),1300,300,"VERDICT",RED,96,rot=-6))
    t=s.at(0.45)
    s.pop("no",s.at(0.05)); s.ft("no",{"opacity":1},{"opacity":0},t-0.2,0.15,"none")
    s.ft("gv",{"rotation":-50,"svgOrigin":"1300 650"},{"rotation":0},t,0.18,"power4.in")
    s.pop("ver",t+0.18,0.3,ease="back.out(2.5)"); s.punch(t+0.18,1.07,1300,500); s.sfx("impact-bass-2",t+0.18,0.4)

@scene(71)
def _(s):
    s.bg()
    s.add(P.mirror(s.id("m"),960,470,320,560))
    s.pop("m",s.at(0.1),0.5); s.sfx("whoosh-short",s.at(0.1),0.2)

def mirror_kids(s,mock):
    out=""
    for j,x in enumerate((900,1020)):
        e="mock" if mock else "happy"
        s.char(f"mk{j}{'m' if mock else 'h'}",x,640,0.4,"kid",(e,),("stand",),cap=CAPS[j])
    return out

@scene(72)
def _(s):
    s.park(bench=None)
    s.char("om",420,860,1.0,"om",("worried",),("clasp",),look=(8,0))
    s.add(P.mirror(s.id("m"),960,520,320,560))
    s.add(f'<g id="{s.id("refl")}">'); s.char("ro",960,700,0.55,"om",("worried",),("clasp",),flip=True,look=(8,0)); s.add('</g>')
    kids_group(s,[1450,1600,1750],sc=0.75,poses=["wave","stand","celebrate"],exprs=("happy",))
    s.fadein("refl",s.at(0.35),0.6)

@scene(73)
def _(s):
    s.park(bench=None)
    s.char("om",360,860,1.0,"om",("worried",),("clasp",),look=(8,0))
    s.add(P.mirror(s.id("m"),960,520,320,560))
    s.add(f'<g id="{s.id("mk")}">'); mirror_kids(s,True); s.add('</g>')
    s.add(f'<defs><filter id="{s.id("fog")}"><feGaussianBlur stdDeviation="16"/></filter></defs><g id="{s.id("fogg")}" filter="url(#{s.id("fog")})" opacity="0.8"><ellipse cx="900" cy="380" rx="110" ry="80" fill="#FFFFFF"/><ellipse cx="1030" cy="520" rx="100" ry="90" fill="#FFFFFF"/><ellipse cx="910" cy="690" rx="90" ry="60" fill="#FFFFFF"/></g>')
    kids_group(s,[1450,1600,1750],sc=0.75,poses=["wave","stand","celebrate"],exprs=("happy",))
    s.fadein("fogg",s.at(0.1),0.8); s.fadein("mk",s.at(0.4),0.5); s.sfx("glitch-2",s.at(0.6),0.15)

@scene(74)
def _(s):
    s.home()
    s.add(P.mirror(s.id("m"),960,520,320,560))
    s.add(f'<g id="{s.id("mm")}">'); mirror_kids(s,True); s.add('</g>')
    s.add(f'<g id="{s.id("mh")}" opacity="0">'); mirror_kids(s,False); s.add('</g>')
    s.add(f'<defs><filter id="{s.id("fog")}"><feGaussianBlur stdDeviation="16"/></filter></defs><g id="{s.id("fogg")}" filter="url(#{s.id("fog")})" opacity="0.8"><ellipse cx="900" cy="380" rx="110" ry="80" fill="#FFFFFF"/><ellipse cx="1030" cy="520" rx="100" ry="90" fill="#FFFFFF"/><ellipse cx="910" cy="690" rx="90" ry="60" fill="#FFFFFF"/></g>')
    s.char("mom",620,860,1.0,"mom",("happy",),("wipe",),look=(8,0))
    s.char("dad",1300,860,1.0,"dad",("happy",),("wipe",),flip=True,look=(8,0))
    s.add(f'<g id="{s.id("cloth")}"><rect x="830" y="440" width="70" height="50" rx="10" fill="#4DABF7" stroke="{INK}" stroke-width="5"/></g>')
    t=s.at(0.45)
    s.ft("cloth",{"x":0,"y":0},{"x":180,"y":120,"repeat":3,"yoyo":True},s.at(0.05),0.45,"sine.inOut")
    s.ft("fogg",{"opacity":0.8},{"opacity":0},t,0.8,"power2.out")
    s.ft("mm",{"opacity":1},{"opacity":0},t+0.3,0.3,"none"); s.ft("mh",{"opacity":0},{"opacity":1},t+0.3,0.3,"none")

@scene(75)
def _(s): research_card(s,"Carl Rogers","Unconditional positive regard")

@scene(76)
def _(s):
    s.home(); s.add(P.sofa(s.id("so"),960))
    s.char("om",1010,860,0.85,"om",("relieved",),("clasp",))
    s.char("mom",880,860,1.0,"mom",("happy",),("hug",),look=(8,4))
    s.add(P.heart(s.id("ht"),960,230,1.4))
    for i,(w,x) in enumerate((("Marks",560),("Performance",960),("Talkative?",1380))):
        s.add(P.tag(s.id(f"t{i}"),x,420,w))
        s.fadein(f"t{i}",s.at(0.25+i*0.15),0.25)
        s.ft(f"t{i}",{"y":0,"opacity":1},{"y":-140,"opacity":0},s.at(0.7)+i*0.08,0.8,"power2.in")
    s.pop("ht",s.at(0.8),0.5); s.sfx("pop",s.at(0.8),0.25)

@scene(77)
def _(s):
    s.park(bench=None)
    s.add(P.house(s.id("hs"),420,860,glow=True))
    s.add(f'<path id="{s.id("path")}" d="M520 840 Q900 780 1500 840" fill="none" stroke="{AMBER}" stroke-width="8" stroke-dasharray="4 26" stroke-linecap="round"/>')
    s.add(P.text(s.id("sb"),420,330,"Secure base",72,AMBER,stroke=INK,sw=7))
    s.char("om",620,860,0.85,"om",("happy",),("wave",),("stand","walkA","walkB"),look=(8,0))
    s.ft("hs-glow",{"opacity":0.1,"scale":0.9,"transformOrigin":"50% 50%"},{"opacity":0.32,"scale":1.05},0.2,1.2,"sine.inOut")
    s.walk("om",s.at(0.1),s.vd*0.55,0,1000,0.24)
    s.ft("om",{"scaleX":1},{"scaleX":-1},s.at(0.6),0.15,"none")
    s.ft("om",{"scaleX":-1},{"scaleX":1},s.at(0.6)+0.9,0.15,"none")
    s.rise("sb",s.at(0.82))
