import props as P
from rig import INK, AMBER, RED, PAPER
CAPS=["#E03131","#1C7ED6","#2F9E44","#7048E8","#0CA678"]
SC={}
def scene(n):
    def deco(f): SC[n]=f; return f
    return deco

def kids_group(s,xs,y=860,sc=0.6,prefix="k",exprs=("happy",),poses=None,opacity=1,flips=None,look=(0,0)):
    names=[]
    for i,x in enumerate(xs):
        pz=(poses[i],) if poses else (("celebrate","throw","stand","wave","catch")[i%5],)
        names.append(s.char(f"{prefix}{i}",x,y,sc,"kid",exprs,pz,("run",) if i%2==0 else ("stand",),cap=CAPS[i%5],opacity=opacity,flip=(flips[i] if flips else i%2==1),look=look))
    return names

def park_om(s,expr=("worried",),om_x=600,kids_far=True,bench=430,pose=("behind",)):
    s.park(bench=bench)
    s.add('<g id="%s">'%s.id("kidsg"))
    kids_group(s,[1300,1400,1500,1600,1700] if kids_far else [1150,1300,1450,1600,1750],sc=0.5,opacity=0.85)
    s.add('</g>')
    s.char("om",om_x,860,1.0,"om",expr,pose,("knees",),look=(7,0))

# ---------------- HOOK
@scene(1)
def _(s):
    s.park(bench=None)
    kids_group(s,[700,920,1140,1360,1580],sc=0.85)
    s.add(P.ball(s.id("ball"),800,560,30))
    for i in range(5): s.rise(f"k{i}",0.05+i*0.08,40)
    # ball bounces between kids
    pts=[(800,560),(1030,470),(1250,560),(1470,470),(1250,560)]
    t=0.4
    for a,b in zip(pts,pts[1:]):
        s.move("ball",t,0.55,{"x":a[0]-800,"y":a[1]-560},{"x":b[0]-800,"y":b[1]-560},"sine.inOut"); t+=0.6
    s.cam(0,s.d,{"x":0},{"x":-60},"none")
    s.sfx("pop",0.45,0.18)

@scene(2)
def _(s):
    park_om(s)
    s.add(P.tag(s.id("tag"),600,380,"Om, 6"))
    s.cam(0,0.9,{"x":500},{"x":0},"power3.out")
    s.pop("tag",s.at(0.35))

@scene(3)
def _(s):
    park_om(s)
    s.add(P.bubble(s.id("bub"),900,300,320,190,"Hi",90,tail=(660,520),thought=True))
    s.pop("bub",s.at(0.55),origin="0% 100%")
    s.ft("bub",{"rotation":-3,"transformOrigin":"50% 50%"},{"rotation":3,"repeat":3,"yoyo":True},s.at(0.55)+0.45,0.35,"sine.inOut")
    s.sfx("pop",s.at(0.55))

@scene(4)
def _(s):
    park_om(s)
    s.add(P.bubble(s.id("bub"),900,300,320,190,"Hi",90,tail=(660,520),thought=True))
    s.add(P.footprints(s.id("fp"),720,1240,830,10))
    s.add(P.text(s.id("lbl"),980,760,"10 steps",64,AMBER,stroke=INK,sw=6))
    for i in range(10): s.pop(f"fp{i}",s.at(0.05)+i*0.12,0.25)
    s.rise("lbl",s.at(0.7))

@scene(5)
def _(s):
    park_om(s,expr=("worried","panicked"))
    s.add(P.tape(s.id("tape"),700,1760,800,90,26,"10 km",txt_size=66))
    t=s.at(0.25)
    s.ft("tape",{"scaleX":0.05,"opacity":0,"transformOrigin":"0% 50%"},{"scaleX":1,"opacity":1},t,1.1,"power2.inOut")
    s.ft("kidsg",{"x":0,"scale":1,"transformOrigin":"1500px 860px"},{"x":120,"scale":0.55},t,1.1,"power2.inOut")
    s.face("om","worried","panicked",t+0.4)
    s.push(t,s.d-t,1.12,600,560)
    s.sfx("whoosh",t)

# ---------------- RELATE
def party_mom_om(s,om_expr=("worried",),mom_expr=("happy",),mom_pose=("stand",),om_x=845):
    s.party()
    kids_group(s,[1350,1500,1650],sc=0.55,opacity=0.8)
    s.char("om",om_x,860,0.85,"om",om_expr,("clasp",),("knees",),look=(8,0))
    s.char("mom",760,860,1.0,"mom",mom_expr,mom_pose,look=(6,0))

@scene(6)
def _(s):
    party_mom_om(s)
    s.cam(0,0.6,{"clipPath":"inset(0% 0% 0% 100%)"},{"clipPath":"inset(0% 0% 0% 0%)"},"power3.inOut")
    s.sfx("whoosh",0.0)

@scene(7)
def _(s):
    party_mom_om(s)
    s.ft("om",{"x":0},{"x":40},s.at(0.4),0.4,"power2.out")
    s.ft("om",{"x":40},{"x":0},s.at(0.4)+1.0,0.3,"power2.in")

@scene(8)
def _(s):
    party_mom_om(s,mom_pose=("stand","pointup"))
    s.add(P.bubble(s.id("bub"),1120,250,420,150,"Go play!",72,tail=(800,330)))
    s.pose("mom","stand","pointup",s.at(0.2))
    s.pop("bub",s.at(0.25),origin="0% 100%"); s.sfx("pop",s.at(0.25))

@scene(9)
def _(s):
    party_mom_om(s,mom_pose=("pointup",))
    s.add(P.bubble(s.id("bub"),1120,250,420,150,"Go play!",72,tail=(800,330)))
    s.shakehead("om",s.at(0.2),4)

@scene(10)
def _(s):
    party_mom_om(s,om_expr=("worried","sad"),mom_expr=("happy","embarrassed"))
    s.char("guest",1180,860,1.0,"adult",("neutral",),flip=True)
    s.add(P.label(s.id("shy"),880,560,"SHY",size=50))
    s.face("mom","happy","embarrassed",s.at(0.3))
    t=s.at(0.75)
    s.ft("shy",{"x":-500,"y":-300,"rotation":-60,"opacity":0},{"x":0,"y":0,"rotation":0,"opacity":1},t,0.35,"power3.in")
    s.face("om","worried","sad",t+0.35)
    s.punch(t+0.35,1.05,880,560); s.sfx("pop",t+0.35,0.4)

@scene(11)
def _(s):
    park_om(s,expr=("neutral",))
    s.cam(0,0.5,{"opacity":0},{"opacity":1},"power2.out")

@scene(12)
def _(s):
    park_om(s,expr=("thinking",))
    s.add(P.arrow(s.id("arr"),1000,250,700,430,AMBER,12))
    s.add(P.text(s.id("you"),1160,250,"You?",96,AMBER,stroke=INK,sw=7))
    s.draw("arr",s.at(0.2),0.5,800); s.pop("you",s.at(0.35))

@scene(13)
def _(s):
    s.classroom()
    groups=[(380,["#E03131","#1C7ED6","#2F9E44"]),(960,["#7048E8","#0CA678","#F08C00"]),(1540,["#1C7ED6","#E03131","#0CA678"])]
    for gi,(gx,cols) in enumerate(groups):
        for j,c in enumerate(cols):
            s.char(f"g{gi}{j}",gx-90+j*90,860,0.5,"kid",("happy",),(("wave","stand","celebrate")[j],),cap=c,flip=j==2)
        s.add(f'<ellipse id="{s.id("c"+str(gi))}" cx="{gx}" cy="760" rx="190" ry="150" fill="none" stroke="{AMBER}" stroke-width="8"/>')
        s.draw(f"c{gi}",s.at(0.35)+gi*0.25,0.6,1200)
    s.char("om",160,860,0.6,"om",("sad",),("clasp",),look=(6,0))

@scene(14)
def _(s):
    s.classroom()
    s.char("om",520,860,0.85,"om",("sad",),("lunch",),("stand",),look=(0,6))
    s.add(P.lunchbox(s.id("lb"),520,770))
    inner=f'<g transform="translate(1250 360)">'
    s.add(P.bubble(s.id("tb"),1250,360,820,440,"",10,tail=(600,520),thought=True))
    s.add(f'<g id="{s.id("mini")}">')
    s.char("mo",1060,500,0.42,"om",("happy",),("wave",))
    for j in range(3): s.char(f"mk{j}",1330+j*80,500,0.42,"kid",("neutral",),("stand",),cap=["#E03131","#1C7ED6","#2F9E44"][j],flip=True)
    s.add('</g>')
    s.add(P.xmark(s.id("x"),1250,360,1.3))
    s.pop("tb",s.at(0.15),origin="0% 100%"); s.fadein("mini",s.at(0.25))
    s.pop("x",s.at(0.72)); s.sfx("pop",s.at(0.72),0.3)

@scene(15)
def _(s):
    s.bg()
    s.char("om",960,860,1.0,"om",("neutral",),("stand",))
    s.char("aom",960,860,1.05,"adult_om",("neutral",),("stand",))
    s.ft("om",{"scale":1,"opacity":1,"transformOrigin":"50% 100%"},{"scale":1.35,"opacity":0},s.at(0.3),0.7,"power2.inOut")
    s.ft("aom",{"scale":0.75,"opacity":0,"transformOrigin":"50% 100%"},{"scale":1,"opacity":1},s.at(0.3)+0.2,0.7,"power3.out")
    s.sfx("whoosh-short",s.at(0.3))

@scene(16)
def _(s):
    s.office()
    third=s.vd/3
    # panel 1: meeting
    s.add(f'<g id="{s.id("p1")}">'); s.add(P.table(s.id("tbl"),960,860,700))
    s.char("a1",620,860,0.9,"adult",("neutral",)); s.char("a2",1300,860,0.9,"adult",("neutral",),flip=True)
    s.char("om1",960,860,0.9,"adult_om",("worried",)); s.add('</g>')
    # panel 2: lobby
    s.add(f'<g id="{s.id("p2")}" opacity="0"><rect x="0" y="0" width="1920" height="860" fill="#F2ECE4"/>'); s.add(P.door(s.id("door"),1300)); s.add(P.door(s.id("door2"),1550))
    s.char("om2",800,860,0.9,"adult_om",("worried",)); s.char("nb",1050,860,0.9,"adult",("neutral",),flip=True); s.add('</g>')
    # panel 3: event
    s.add(f'<g id="{s.id("p3")}" opacity="0"><rect x="0" y="0" width="1920" height="860" fill="#EDE7F6"/>')
    s.char("om3",820,860,0.9,"adult_om",("panicked",)); s.add(P.name_tag(s.id("nt"),1180,420)); s.add('</g>')
    a,b=s.at(0.42),s.at(0.72)
    s.set("p1",{"opacity":0},a); s.set("p2",{"opacity":1},a)
    s.set("p2",{"opacity":0},b); s.set("p3",{"opacity":1},b)
    s.sfx("whoosh-short",a,0.25); s.sfx("whoosh",b,0.2)

@scene(17)
def _(s):
    s.office()
    s.char("aom",600,860,0.95,"adult_om",("thinking",),("think",),look=(6,-4))
    s.add(f'<g id="{s.id("grp")}">')
    for j in range(3): s.char(f"g{j}",1250+j*150,860,0.85,"adult",("happy",),("stand",),flip=j%2==0)
    s.add('</g>')
    s.add(P.bubble(s.id("bub"),900,250,380,170,"",10,tail=(660,380)))
    s.add(f'<path id="{s.id("scr")}" d="M760 250 q20 -30 40 0 t40 0 t40 0 t40 0 t40 0 t40 0" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    s.pop("bub",s.at(0.1)); s.draw("scr",s.at(0.15),1.6,700)
    s.ft("grp",{"x":0,"opacity":1},{"x":500,"opacity":0},s.at(0.55),1.4,"power1.in")
    s.ft("bub",{"scale":1},{"scale":0,"transformOrigin":"0% 100%"},s.at(0.9),0.2,"power3.in")
    s.ft("scr",{"opacity":1},{"opacity":0},s.at(0.9),0.15,"none")
    s.sfx("pop",s.at(0.9),0.25)

@scene(18)
def _(s):
    s.office()
    s.char("aom",960,860,1.2,"adult_om",("grin",),("stand",))
    # chest window
    s.add(f'<g id="{s.id("win")}"><rect x="895" y="520" width="130" height="150" rx="16" fill="#FFF4E0" stroke="{INK}" stroke-width="6"/>')
    s.char("mini",960,660,0.32,"om",("sad",),("clasp",))
    s.add('</g>')
    s.ft("win",{"scaleY":0,"transformOrigin":"50% 0%"},{"scaleY":1},s.at(0.45),0.45,"back.out(1.5)")
    s.push(s.at(0.3),s.d-s.at(0.3),1.15,960,560)
