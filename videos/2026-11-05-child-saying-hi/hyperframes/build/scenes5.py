import props as P
from rig import INK, AMBER, RED, PAPER
from scenes1 import kids_group, park_om, CAPS
SC={}
def scene(n):
    def deco(f): SC[n]=f; return f
    return deco
ITEMS=[("Drop the label"),("Small steps"),("Attempt > outcome")]

# ---------------- WHAT PARENTS CAN DO
@scene(78)
def _(s):
    s.bg()
    s.add(P.text(s.id("h"),960,150,"3 things for parents",72,INK))
    for i,t in enumerate(ITEMS):
        s.add(P.numcard(s.id(f"c{i}"),960,320+i*200,i+1,t,900))
        s.slidein(f"c{i}",s.at(0.2)+i*0.2,-260); s.sfx("whoosh-short",s.at(0.2)+i*0.2,0.15)
    s.rise("h",0.1)

def num_header(s,i):
    s.add(P.numcard(s.id("hdr"),960,140,i+1,ITEMS[i],900))

@scene(79)
def _(s):
    s.bg(); num_header(s,0)
    s.char("om",960,860,1.1,"om",("sad",),("clasp",))
    s.add(P.label(s.id("shy"),960,500,"SHY",size=40))
    s.ft("hdr",{"rotationX":90,"opacity":0,"transformOrigin":"50% 50%"},{"rotationX":0,"opacity":1},0.1,0.5,"back.out(1.4)")

@scene(80)
def _(s):
    s.bg(); num_header(s,0)
    s.char("om",960,860,1.1,"om",("sad",),("clasp",))
    s.add(P.label(s.id("shy"),960,500,"SHY",size=40))
    s.ft("shy",{"scale":1,"transformOrigin":"50% 50%"},{"scale":2.2},s.at(0.3),s.vd*0.6,"power2.inOut")
    s.ft("om",{"scale":1,"transformOrigin":"50% 100%"},{"scale":0.8},s.at(0.3),s.vd*0.6,"power2.inOut")

@scene(81)
def _(s):
    s.party()
    s.char("om",1000,860,0.95,"om",("sad","relieved"),("clasp",))
    s.char("mom",700,860,1.0,"mom",("happy",),("stand","reach"),look=(8,0))
    s.add(P.label(s.id("shy"),1000,590,"SHY",size=46))
    s.add(P.bubble(s.id("bb"),1200,300,700,130,"Likes to watch first",58,fill="#FFF4E0",tail=(1060,520)))
    t=s.at(0.15); s.pose("mom","stand","reach",t)
    s.ft("shy",{"x":0,"y":0,"rotation":0,"opacity":1},{"x":-160,"y":-180,"rotation":-40,"opacity":0},t+0.3,0.6,"power2.in")
    s.face("om","sad","relieved",t+0.6); s.pop("bb",t+0.7,origin="0% 100%"); s.sfx("pop",t+0.7,0.25)

@scene(82)
def _(s):
    s.bg(); num_header(s,1)
    s.char("om",960,860,1.0,"om",("neutral",),("stand",))
    s.add(P.footprints(s.id("fp"),700,1220,830,6))
    s.ft("hdr",{"rotationX":90,"opacity":0,"transformOrigin":"50% 50%"},{"rotationX":0,"opacity":1},0.1,0.5,"back.out(1.4)")
    for i in range(6): s.pop(f"fp{i}",s.at(0.4)+i*0.1,0.2)

@scene(83)
def _(s):
    s.home(); s.add(P.sofa(s.id("so"),1180))
    s.char("om",620,860,0.9,"om",("embarrassed",),("clasp",),look=(8,0))
    s.char("dad",1250,860,1.0,"dad",("grin",),("stand",),cap="#F08C00",flip=True)
    s.add(P.tag(s.id("nk"),1250,600,"NEW KID",fill="#FFFFFF",size=40))
    s.pop("nk",s.at(0.35)); s.sfx("pop",s.at(0.35),0.2)

@scene(84)
def _(s):
    s.home(); s.add(P.sofa(s.id("so"),1180))
    s.char("om",620,860,0.9,"om",("happy",),("handout",),look=(8,0))
    s.char("dad",1250,860,1.0,"dad",("grin",),("stand",),cap="#F08C00",flip=True)
    s.add(f'<g id="{s.id("bb")}"><rect x="420" y="130" width="900" height="300" rx="40" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/><path d="M560 430 L600 500 L640 430" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/><line x1="566" y1="430" x2="634" y2="430" stroke="#FFFFFF" stroke-width="9"/></g>')
    for i,l in enumerate(("Hi, I'm Om.","I like playing ball.","Can I play too?")):
        s.add(P.text(s.id(f"l{i}"),870,215+i*85,l,62,INK))
        s.fadein(f"l{i}",s.at([0.0,0.3,0.65][i]),0.25)
    s.pop("bb",0.05,0.3,origin="20% 100%")

@scene(85)
def _(s):
    s.home()
    s.add(P.text(s.id("h"),960,150,"10x at home = 1x at the park",68,INK))
    s.char("om",500,860,0.9,"om",("happy","grin"),("handout","celebrate"))
    for i in range(10):
        x=760+(i%5)*55+(i//5)*330; 
        if i%5==4: s.add(f'<line id="{s.id("tl"+str(i))}" x1="{x-235}" y1="470" x2="{x+15}" y2="370" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>')
        else: s.add(f'<line id="{s.id("tl"+str(i))}" x1="{x}" y1="340" x2="{x}" y2="500" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>')
        s.fadein("tl"+str(i),s.at(0.1)+i*0.14,0.08); s.sfx("key-press",s.at(0.1)+i*0.14,0.12)
    s.add(P.arrow(s.id("ar"),1280,620,1500,620,AMBER,12)); s.add(P.tree(1620,720,0.45))
    s.draw("ar",s.at(0.65),0.4,400); s.rise("h",s.at(0.6))
    s.face("om","happy","grin",s.at(0.7)); s.pose("om","handout","celebrate",s.at(0.7))

@scene(86)
def _(s):
    s.bg()
    s.add(P.text(s.id("h"),960,130,"One friend, then the group",68,INK))
    s.add(f'<g id="{s.id("p1")}"><rect x="60" y="200" width="880" height="620" rx="30" fill="#FFF6EA" stroke="{INK}" stroke-width="6"/>')
    s.add(f'<g transform="translate(0 0)">'); s.char("om1",360,780,0.7,"om",("happy",),("throw",)); s.char("f1",640,780,0.7,"kid",("happy",),("catch",),cap=CAPS[2],flip=True); s.add('</g>')
    s.add(P.ball(s.id("b1"),500,470,22)); s.add('</g>')
    s.add(f'<g id="{s.id("p2")}"><rect x="980" y="200" width="880" height="620" rx="30" fill="#EEF4F8" stroke="{INK}" stroke-width="6"/>')
    s.char("om2",1160,780,0.6,"om",("happy",),("wave",)); s.char("f2",1300,780,0.6,"kid",("happy",),("wave",),cap=CAPS[2])
    for j,x in enumerate((1480,1600,1720)): s.char(f"g{j}",x,780,0.6,"kid",("happy",),(("celebrate","wave","stand")[j],),cap=CAPS[(j+3)%5],flip=True)
    s.add('</g>')
    s.rise("h",0.1); s.fadein("p1",0.2)
    s.ft("b1",{"y":0},{"y":-60,"repeat":5,"yoyo":True},0.4,0.4,"sine.inOut")
    s.slidein("p2",s.at(0.42),300); s.sfx("whoosh-short",s.at(0.42),0.2)

@scene(87)
def _(s):
    s.bg(); num_header(s,2)
    s.char("om",960,860,1.0,"om",("neutral",),("stand",))
    s.ft("hdr",{"rotationX":90,"opacity":0,"transformOrigin":"50% 50%"},{"rotationX":0,"opacity":1},0.1,0.5,"back.out(1.4)")

@scene(88)
def _(s):
    s.park(bench=None)
    kids_group(s,[1550,1680,1800],sc=0.6,poses=["crossed","stand","stand"],exprs=("neutral",),opacity=0.8)
    s.char("mom",560,860,1.0,"mom",("happy",),("stand","highfive"),look=(8,0))
    s.char("om",1250,860,0.9,"om",("sad","happy"),("clasp","highfiveL"),("stand","walkA","walkB"),flip=True)
    s.walk("om",s.at(0.02),s.vd*0.35,0,(1250-800)/0.9,0.24)
    s.add(P.bubble(s.id("bb"),980,220,960,140,"You talked to them yourself. I loved that.",48,fill="#FFF4E0",tail=(640,330)))
    t=s.at(0.5); s.pose("mom","stand","highfive",t); s.pose("om","clasp","highfiveL",t); s.face("om","sad","happy",t+0.1)
    s.add(f'<g id="{s.id("spark")}"><path d="M700 330 l12 -40 l12 40 l40 12 l-40 12 l-12 40 l-12 -40 l-40 -12 Z" fill="#FFD43B" stroke="{INK}" stroke-width="4"/></g>')
    s.pop("spark",t+0.15,0.3); s.sfx("click",t+0.15,0.35); s.pop("bb",s.at(0.55),origin="30% 100%")

@scene(89)
def _(s):
    s.bg()
    s.char("om",600,860,1.1,"om",("relieved",),("stand",))
    s.add(P.gauge(s.id("g"),1350,560,240,s.id("nd"),"My worth",0.78,44))
    s.add(P.bubble(s.id("no"),1500,250,180,110,"No",64))
    s.ft("no",{"x":0,"y":0},{"x":-760,"y":120},s.at(0.15),0.5,"power2.in")
    s.ft("no",{"x":-760,"y":120,"rotation":0},{"x":-500,"y":-160,"rotation":40,"opacity":0},s.at(0.15)+0.5,0.6,"power2.out")
    s.sfx("pop",s.at(0.15)+0.5,0.25)

@scene(90)
def _(s):
    s.office(); s.add(P.door(s.id("door"),1450))
    s.char("nb",1450,860,1.0,"adult",("happy",),("wave",),cap="#0CA678",flip=True)
    s.char("mom",900,860,1.0,"mom",("happy",),("wave",),look=(8,0))
    s.char("dad",1130,860,1.0,"dad",("grin",),("handout",),look=(8,0))
    s.char("om",420,860,0.8,"om",("thinking",),("clasp",),look=(8,0))
    s.nod("dad",s.at(0.4)); s.sfx("notification",0.15,0.15)

@scene(91)
def _(s):
    s.kitchen(); s.add(P.counter_kitchen(s.id("ct"),760))
    s.char("dad",760,860,1.0,"dad",("neutral","embarrassed","grin"),("stand","handout"),look=(8,0))
    s.char("om",1450,860,0.85,"om",("thinking",),("clasp",),flip=True,look=(8,0))
    s.add(f'<g id="{s.id("cupg")}">'+P.cup(s.id("cup"),940,580)+'</g>')
    s.add(f'<path id="{s.id("spill")}" d="M960 580 q60 10 120 0 q30 -6 40 4" fill="none" stroke="#8B5E3C" stroke-width="12" stroke-linecap="round"/>')
    s.add(P.bubble(s.id("bb"),760,250,560,130,"Oops, that's okay",58,tail=(760,380)))
    t=s.at(0.15)
    s.ft("cupg",{"rotation":0,"svgOrigin":"960 580"},{"rotation":80},t,0.3,"power2.in"); s.draw("spill",t+0.25,0.4,200)
    s.face("dad","neutral","embarrassed",t+0.3); s.face("dad","embarrassed","grin",s.at(0.55)); s.pop("bb",s.at(0.55))

@scene(92)
def _(s):
    s.kitchen(); s.add(P.counter_kitchen(s.id("ct"),760))
    s.char("dad",760,860,1.0,"dad",("grin",),("celebrate",),look=(8,0))
    s.char("om",1350,860,0.85,"om",("thinking","grin"),("clasp","celebrate"),flip=True)
    t=s.at(0.35); s.face("om","thinking","grin",t); s.pose("om","clasp","celebrate",t)
    s.ft("om",{"y":0},{"y":-30,"repeat":1,"yoyo":True},t,0.2,"power2.out")

@scene(93)
def _(s):
    s.office(); s.add(P.plant(s.id("pl"),1700))
    s.char("co",1350,860,1.0,"adult",("happy",),("stand",),cap="#7048E8",flip=True)
    s.char("mom",620,860,1.0,"mom",("neutral",),("stand",),look=(8,0))
    s.char("om",820,860,0.8,"om",("neutral",),("clasp",),look=(8,0))
    s.add(f'<g id="{s.id("info")}"><rect x="360" y="90" width="1200" height="200" rx="30" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>'+P.text(s.id("i1"),960,175,"If the fear is intense,",62,INK)+P.text(s.id("i2"),960,250,"talk to a child psychologist",62,AMBER,stroke=INK,sw=6)+'</g>')
    s.cam(0,0.6,{"opacity":0},{"opacity":1},"power2.out"); s.rise("info",s.at(0.6))

# ---------------- CLOSE
def close_park(s,tape=True):
    s.park(bench=430)
    s.add(f'<g id="{s.id("kidsg")}">'); kids_group(s,[1300,1400,1500,1600,1700],sc=0.5,opacity=0.9); s.add('</g>')
    if tape: s.add(P.tape(s.id("tape"),700,1760,800,90,26,"10 km",txt_size=66))

@scene(94)
def _(s):
    close_park(s)
    s.char("om",600,860,1.0,"om",("worried",),("behind",),("knees",),look=(7,0))
    s.ft("kidsg",{"x":120,"scale":0.55,"transformOrigin":"1500px 860px"},{"x":120,"scale":0.55},0,0.1,"none")
    s.cam(0,0.4,{"opacity":0},{"opacity":1},"power2.out"); s.sfx("whoosh",0,0.2)

@scene(95)
def _(s):
    s.park(bench=430)
    s.add(P.tape(s.id("tape"),700,1760,800,90,26,"10 km",txt_size=66))
    s.add(f'<g id="{s.id("kidsg")}">')
    for i,x in enumerate((1300,1430,1560,1690,1820)):
        s.char(f"k{i}",x,860,0.9,"kid",("neutral",),("stand",),cap=CAPS[i],flip=True)
    s.add('</g>')
    s.char("om",600,860,1.0,"om",("worried",),("clasp",),("stand","walkA","walkB"),look=(7,0))
    s.add(P.footprints(s.id("fp"),660,940,840,5))
    s.add(P.text(s.id("st"),1140,560,"10 steps",80,AMBER,stroke=INK,sw=7))
    t=s.at(0.05)
    s.walk("om",t,s.vd*0.9,0,380,0.28); s.shake("om-head",t+0.6,6,3)
    for i in range(5): s.pop(f"fp{i}",t+0.3+i*0.35,0.2)
    s.ft("kidsg",{"x":60,"scale":0.3,"transformOrigin":"1560px 860px"},{"x":0,"scale":1},t,s.vd,"power2.inOut")
    s.ft("tape",{"opacity":1,"scaleX":1,"transformOrigin":"0% 50%"},{"opacity":0,"scaleX":0.3},t,s.vd*0.7,"power2.inOut")
    s.rise("st",t+s.vd*0.6)

def close_final(s,om_expr=("happy",),om_pose=("wave",)):
    s.park(bench=430)
    kids_group(s,[1300,1440,1580,1700,1820],sc=0.55*2,prefix="k")
    s.char("om",980,860,1.0,"om",om_expr,om_pose,look=(8,0))

@scene(96)
def _(s):
    s.park(bench=430)
    for i,x in enumerate((1300,1430,1560,1690,1820)):
        s.char(f"k{i}",x,860,0.9,"kid",("neutral","happy"),("stand",),cap=CAPS[i],flip=True)
    s.char("om",980,860,1.0,"om",("worried","happy"),("clasp","wave"),look=(8,0))
    s.add(P.bubble(s.id("bb"),1040,280,700,140,"Hi. I'm Om. Can I play too?",54,tail=(1000,470)))
    s.pose("om","clasp","wave",s.at(0.0)); s.pop("bb",s.at(0.02),origin="0% 100%")
    s.face("om","worried","happy",s.at(0.7))
    for i in range(5): s.face(f"k{i}","neutral","happy",s.at(0.6)+i*0.05)
    s.push(s.at(0.0),s.d,1.06,1100,600)

@scene(97)
def _(s):
    s.park(bench=430)
    for i,x in enumerate((1300,1430,1560,1690,1820)):
        s.char(f"k{i}",x,860,0.9,"kid",("happy",),(("throw" if i==0 else "stand"),),cap=CAPS[i],flip=True)
    s.char("om",980,860,1.0,"om",("happy","grin"),("wave","catch"),look=(8,-4))
    s.add(P.ball(s.id("ball"),1240,630,30))
    t=s.at(0.25)
    s.ft("ball",{"x":0},{"x":-260},t,0.7,"none"); s.ft("ball",{"y":0},{"y":-160},t,0.35,"power2.out")
    s.ft("ball",{"y":-160},{"y":90},t+0.35,0.35,"power2.in")
    s.pose("om","wave","catch",t+0.45); s.face("om","happy","grin",t+0.7); s.sfx("whoosh-short",t,0.2); s.sfx("click-soft",t+0.7,0.35)

@scene(98)
def _(s):
    s.park(bench=430)
    for i,x in enumerate((1180,1360,1540,1720)):
        s.char(f"k{i}",x,860,0.9,"kid",("grin",),(("celebrate","wave","celebrate","throw")[i],),("run" if i%2 else "stand",),cap=CAPS[i],flip=i%2==0)
    s.char("om",960,860,1.0,"om",("grin",),("celebrate",))
    s.add(P.ball(s.id("ball"),1080,420,30))
    s.ft("ball",{"y":0},{"y":-120,"repeat":3,"yoyo":True},0.3,0.45,"sine.inOut")
    s.cam(0.2,s.d-0.2,{"scale":1.12,"y":60,"transformOrigin":"1300px 700px"},{"scale":0.94,"y":-30},"power2.inOut")
    s.sfx("riser",max(0,s.at(0.0)-0.8),0.18)

@scene(99)
def _(s):
    s.bg()
    s.add(P.share_icon(s.id("sh"),960,360,)); s.add(P.text(s.id("t"),960,620,"Send this to a parent",80,INK))
    s.pop("sh",s.at(0.1)); s.rise("t",s.at(0.3)); s.sfx("pop",s.at(0.1),0.2)

@scene(100)
def _(s):
    s.bg()
    s.char("om",360,860,1.0,"om",("happy",),("wave",))
    s.add(P.comment_icon(s.id("cm"),1100,380)); s.add(P.text(s.id("t"),1100,640,"Tell me in the comments",72,INK))
    s.pop("cm",s.at(0.2)); s.rise("t",s.at(0.4)); s.sfx("pop",s.at(0.2),0.2)
    s.ft("om-arms-wave",{"rotation":-6,"transformOrigin":"50% 100%"},{"rotation":6,"repeat":5,"yoyo":True},s.at(0.3),0.3,"sine.inOut")
