import props as P
from rig import INK, AMBER, RED, PAPER
from scenes1 import kids_group, park_om, CAPS
from scenes2 import research_card
SC={}
def scene(n):
    def deco(f): SC[n]=f; return f
    return deco

# ---------------- LIKING GAP
@scene(40)
def _(s): research_card(s,"Erica Boothby and colleagues, 2018","Conversations between strangers")

def cafe_pair(s,ea=("happy",),eb=("happy",)):
    s.cafe(); s.add(P.table(s.id("tbl"),960,860,420)); s.add(P.cup(s.id("c1"),890,660),P.cup(s.id("c2"),1030,660))
    s.char("a",640,860,1.0,"adult",ea,("stand",),look=(7,0))
    s.char("b",1280,860,1.0,"adult",eb,("stand",),cap="#7048E8",flip=True,look=(7,0))

@scene(41)
def _(s):
    cafe_pair(s)
    s.add(P.bubble(s.id("ba"),760,260,180,110,"...",60,tail=(660,400)))
    s.add(P.bubble(s.id("bb"),1160,260,180,110,"...",60,tail=(1260,400)))
    s.add(P.bubble(s.id("q"),960,180,1300,120,"“How much did the other person like you?”",50,fill="#FFF4E0"))
    for k in range(3):
        s.pop("ba",0.2+k*0.9,0.3) if k==0 else s.ft("ba",{"opacity":0},{"opacity":1},0.2+k*0.9,0.15,"none")
        s.ft("ba",{"opacity":1},{"opacity":0},0.6+k*0.9,0.15,"none")
        s.ft("bb",{"opacity":0},{"opacity":1},0.65+k*0.9,0.15,"none")
        s.ft("bb",{"opacity":1},{"opacity":0},1.05+k*0.9,0.15,"none")
    s.rise("q",s.at(0.5))

def two_gauges(s,v1,v2,l1="How much I liked them",l2="How much they liked me",y=330,x1=640,x2=1280,r=170):
    s.add(P.gauge(s.id("g1"),x1,y,r,s.id("n1"),l1,v1,36))
    s.add(P.gauge(s.id("g2"),x2,y,r,s.id("n2"),l2,v2,36))

@scene(42)
def _(s):
    cafe_pair(s,("happy","worried"),("happy",))
    two_gauges(s,0.8,0.5)
    s.pop("g1",s.at(0.05)); s.pop("g2",s.at(0.15))
    s.ft("n1",{"rotation":-90,"svgOrigin":"0 0"},{"rotation":-90+180*0.8},s.at(0.2),0.8,"power3.out")
    s.ft("n2",{"rotation":-90,"svgOrigin":"0 0"},{"rotation":-90+180*0.5},s.at(0.3),0.8,"power3.out")
    s.add(P.text(s.id("v1"),905,320,"8/10",56,INK)); s.add(P.text(s.id("v2"),1545,320,"5/10",56,RED))
    s.fadein("v1",s.at(0.45)); s.fadein("v2",s.at(0.5)); s.face("a","happy","worried",s.at(0.5))

@scene(43)
def _(s):
    cafe_pair(s,("worried",),("happy",))
    two_gauges(s,0.8,0.5)
    s.add(P.text(s.id("v1"),905,320,"8/10",56,INK)); s.add(P.text(s.id("v2"),1545,320,"5/10",56,RED))
    s.add(f'<rect id="{s.id("gapbar")}" x="700" y="40" width="520" height="80" rx="40" fill="{RED}" stroke="{INK}" stroke-width="6"/>')
    s.add(P.text(s.id("lg"),960,98,"THE LIKING GAP",54,"#FFFFFF"))
    t=s.at(0.45)
    s.ft("gapbar",{"scaleX":0,"transformOrigin":"50% 50%"},{"scaleX":1},t,0.35,"expo.out"); s.fadein("lg",t+0.15,0.2)
    s.punch(t,1.06,960,300); s.sfx("impact-bass-1",t,0.3)

@scene(44)
def _(s): research_card(s,"Wolf, Nafe & Tomasello, 2021","Children aged 4 to 11")

@scene(45)
def _(s):
    s.bg()
    s.char("k4",960,860,0.75,"kid",("grin",),("celebrate",),cap="#FFD43B")
    two_gauges(s,0.9,0.9,"I like them","They like me",330,560,1360,160)
    s.add(P.text(s.id("tag"),960,150,"Age 4: no gap",72,AMBER,stroke=INK,sw=7))
    s.pop("g1",s.at(0.05)); s.pop("g2",s.at(0.1)); s.rise("tag",s.at(0.25))
    s.ft("n1",{"rotation":-90,"svgOrigin":"0 0"},{"rotation":72},s.at(0.15),0.7,"power3.out")
    s.ft("n2",{"rotation":-90,"svgOrigin":"0 0"},{"rotation":72},s.at(0.2),0.7,"power3.out")

def age_scene(s,marker_from,marker_to,needle_from,needle_to,label,expr,kid_scale):
    s.bg()
    two_gauges(s,0.9,needle_from,"I like them","They like me",290,640,1280,150)
    s.add(P.timeline_axis(s.id("ax"),520,1560,640,[("4",560),("5",700),("11",1500)]))
    s.add(f'<g transform="translate(0 0)"><g id="{s.id("mk")}"><path d="M{marker_from} 600 l-26 -40 l52 0 Z" fill="{AMBER}" stroke="{INK}" stroke-width="5"/></g></g>')
    s.char("kid",300,860,kid_scale,"kid",expr,("clasp",),cap="#FFD43B",look=(8,0))
    s.add(f'<g id="{s.id("wh")}">')
    s.char("w1",1620,860,0.55,"kid",("smug",),("stand",),cap=CAPS[1],flip=True); s.char("w2",1720,860,0.55,"kid",("smug",),("stand",),cap=CAPS[3],flip=True)
    s.add('</g>')
    s.add(P.text(s.id("lb"),1040,830,label,60,INK))
    return s

@scene(46)
def _(s):
    age_scene(s,560,700,0.9,0.68,"Age 5: the gap starts",("worried",),0.6)
    s.ft("mk",{"x":0},{"x":140},s.at(0.05),0.6,"power2.inOut")
    s.ft("n2",{"rotation":72,"svgOrigin":"0 0"},{"rotation":-90+180*0.68},s.at(0.2),0.7,"power2.inOut")
    s.rise("lb",s.at(0.25)); s.fadein("wh",s.at(0.55))

@scene(47)
def _(s):
    age_scene(s,700,1500,0.68,0.42,"Age 11: a wider gap",("sad",),0.85)
    s.ft("mk",{"x":0},{"x":800},s.at(0.05),1.2,"power2.inOut")
    s.ft("n2",{"rotation":-90+180*0.68,"svgOrigin":"0 0"},{"rotation":-90+180*0.42},s.at(0.1),1.1,"power2.inOut")
    s.rise("lb",s.at(0.4))

@scene(48)
def _(s):
    s.park(bench=430)
    kids_group(s,[1250,1420,1590],sc=0.7,poses=["wave","wave","celebrate"],exprs=("happy",))
    s.char("om",600,860,1.0,"om",("worried",),("clasp",),look=(8,0))
    s.add(P.bubble(s.id("tb"),1250,470,760,330,"They won't let me in",64,tail=(680,520),thought=True))
    s.pop("tb",s.at(0.05),origin="0% 100%")
    s.ft("tb",{"opacity":1},{"opacity":0.18},s.at(0.65),0.6,"power2.inOut")

@scene(49)
def _(s):
    s.bg()
    s.char("om",700,860,1.1,"om",("confused",),("stand",))
    s.add(f'<path id="{s.id("loopar")}" d="M760 470 C 1000 300, 1060 650, 820 640" fill="none" stroke="{AMBER}" stroke-width="12" stroke-linecap="round"/><path id="{s.id("ah")}" d="M850 610 L815 642 L860 660" fill="none" stroke="{AMBER}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>')
    s.add(P.text(s.id("t"),1380,420,"Guess ≠ fact",96,INK))
    s.draw("loopar",s.at(0.15),0.7,800); s.fadein("ah",s.at(0.15)+0.6,0.15); s.rise("t",s.at(0.5))

# ---------------- REJECTION LOOP
@scene(50)
def _(s):
    s.bg()
    s.char("om",480,860,1.0,"om",("worried",),("clasp",),look=(8,-4))
    s.add(P.bubble(s.id("tb"),1150,380,760,300,"They'll reject me",66,tail=(560,520),thought=True))
    s.add(P.bubble(s.id("stone"),1150,380,760,300,"They'll reject me",66,tail=(560,520),thought=True,fill="#9AA0A6",txtfill="#FFFFFF"))
    s.pop("tb",0.15,origin="0% 100%")
    s.set("stone",{"opacity":0},0); s.ft("stone",{"opacity":0},{"opacity":1},s.at(0.55),0.25,"power2.in")
    s.ft("stone",{"y":-20},{"y":0},s.at(0.55)+0.2,0.2,"bounce.out"); s.sfx("impact-bass-2",s.at(0.55)+0.2,0.3)

@scene(51)
def _(s): research_card(s,"Geraldine Downey, Columbia University","Rejection sensitivity")

@scene(52)
def _(s):
    s.park(bench=None)
    s.char("om",420,860,1.0,"om",("panicked",),("clasp",),look=(8,0))
    s.add(P.radar(s.id("rd"),420,470))
    s.char("k1",1150,860,0.8,"kid",("neutral","shocked"),("stand",),cap=CAPS[1])
    s.char("k2",1500,860,0.8,"kid",("neutral",),("stand",),cap=CAPS[2])
    for k,t in enumerate((s.at(0.1),s.at(0.4),s.at(0.7))):
        s.ft("rd",{"scale":0.6,"opacity":1,"transformOrigin":"50% 100%"},{"scale":1.3,"opacity":0},t,0.6,"power2.out")
        s.sfx("ping",t,0.12)
    s.face("k1","neutral","shocked",s.at(0.4))
    s.ft("k2",{"scaleX":1,"transformOrigin":"50% 50%"},{"scaleX":-1},s.at(0.7),0.2,"power2.inOut")

@scene(53)
def _(s): research_card(s,"Downey and colleagues, 1998","Children in grades 5 to 7")

@scene(54)
def _(s):
    s.corridor(); s.add(P.door(s.id("door"),1550))
    s.char("st",450,860,1.0,"kid",("happy",),("handout",),("stand","walkA","walkB"),cap=CAPS[1])
    s.add(f'<g transform="translate(450 860) scale(1)"><g id="{s.id("inv")}"><rect x="120" y="-200" width="70" height="50" rx="6" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><path d="M120 -200 L155 -175 L190 -200" fill="none" stroke="{INK}" stroke-width="4"/></g></g>')
    s.walk("st",s.at(0.1),s.vd*0.85,0,820,0.26)
    s.ft("inv",{"x":0},{"x":820},s.at(0.1),s.vd*0.85,"none")

@scene(55)
def _(s):
    s.corridor(); s.add(P.door(s.id("door"),1550))
    s.char("rs",700,860,1.0,"researcher",("neutral",),("stand","shrug"))
    s.char("st",1250,860,1.0,"kid",("happy","shocked"),("handout",),cap=CAPS[1],flip=True)
    s.add(P.text(s.id("q"),1250,430,"?",140,INK))
    s.pose("rs","stand","shrug",s.at(0.3)); s.face("st","happy","shocked",s.at(0.4))
    s.ft("q",{"y":40,"opacity":0},{"y":-30,"opacity":1},s.at(0.45),0.8,"power2.out")

@scene(56)
def _(s):
    s.corridor()
    s.add('<line x1="960" y1="40" x2="960" y2="860" stroke="#1A1A1A" stroke-width="6"/>')
    s.char("a",480,860,1.0,"kid",("sad",),("clasp",),cap=CAPS[1])
    s.char("b",1440,860,1.0,"kid",("neutral","panicked"),("clasp",),cap=CAPS[0])
    s.add(P.gauge(s.id("g1"),480,260,140,s.id("n1"),"Upset",0.35,38))
    s.add(P.gauge(s.id("g2"),1440,260,140,s.id("n2"),"Upset",0.9,38))
    s.ft("n1",{"rotation":-90,"svgOrigin":"0 0"},{"rotation":-90+180*0.35},s.at(0.3),0.6,"power2.out")
    s.ft("n2",{"rotation":-90,"svgOrigin":"0 0"},{"rotation":-90+180*0.9},s.at(0.45),0.7,"power2.out")
    s.face("b","neutral","panicked",s.at(0.45)); s.shake("b",s.at(0.5),6,6)

@scene(57)
def _(s):
    s.classroom()
    s.char("te",420,860,1.0,"teacher",("thinking",),("stand",),look=(8,-4))
    s.add(P.calendar(s.id("cal"),1050,560)); s.add(P.chart(s.id("ch"),1500,560))
    s.add(P.text(s.id("t"),1050,760,"1 year later",58,INK))
    for k in range(5): s.ft("cal",{"scaleY":1,"transformOrigin":"50% 0%"},{"scaleY":0.2,"repeat":1,"yoyo":True},s.at(0.1)+k*0.25,0.1,"none")
    s.rise("t",s.at(0.35)); s.draw("ch-line",s.at(0.55),0.8,400)

LOOP_TXT=("They'll reject me","I hang back","They don't invite me","See? I knew it.")
def loop_scene(s,filled,om_scale=0.5,om_expr=("worried",)):
    s.bg()
    s.add(P.loop(s.id("lp"),960,450,300,[LOOP_TXT[i] if i<filled else "" for i in range(4)],[s.id(f"n{i}") for i in range(4)]))
    s.char("om",960,640,om_scale,"om",om_expr,("crossed",))
    return s

@scene(58)
def _(s):
    loop_scene(s,0)
    for i in range(4): s.pop(f"n{i}",0.25+i*0.12,0.35)
    s.ft("lp",{"rotation":-90,"opacity":0,"svgOrigin":"960 450"},{"rotation":0,"opacity":1},0.05,0.6,"expo.out")
    s.sfx("whoosh-short",0.05,0.25)

@scene(59)
def _(s):
    loop_scene(s,2)
    s.fadein("n0-t",s.at(0.1)); s.fadein("n1-t",s.at(0.55)); s.sfx("pop",s.at(0.1),0.2); s.sfx("pop",s.at(0.55),0.2)
    s.shake("om",s.at(0.6),3,4)

@scene(60)
def _(s):
    loop_scene(s,3)
    s.fadein("n2-t",s.at(0.2)); s.sfx("pop",s.at(0.2),0.2)

@scene(61)
def _(s):
    loop_scene(s,4,0.5,("worried","sad"))
    s.fadein("n3-t",s.at(0.15)); s.sfx("pop",s.at(0.15),0.2)
    s.add(f'<g id="{s.id("dot")}"><circle cx="960" cy="150" r="20" fill="{RED}" stroke="{INK}" stroke-width="5"/></g>')
    s.ft("dot",{"rotation":0,"svgOrigin":"960 450"},{"rotation":720},s.at(0.3),s.d-s.at(0.3),"none")
    s.ft("om",{"scale":1,"transformOrigin":"50% 100%"},{"scale":0.72},s.at(0.3),s.d-s.at(0.3),"power1.in")
    s.face("om","worried","sad",s.at(0.4)); s.sfx("whoosh",s.at(0.3),0.2)

@scene(62)
def _(s):
    s.bg()
    s.char("om",900,860,1.2,"om",("sad",),("holdsign",),look=(0,6))
    s.add(f'<g id="{s.id("sign")}"><rect x="780" y="430" width="240" height="150" rx="14" fill="{RED}" stroke="{INK}" stroke-width="7"/>'+P.text(s.id("no"),900,535,"NO",96,"#FFFFFF")+'</g>')
    s.pop("sign",s.at(0.35),0.35,ease="back.out(2)"); s.sfx("impact-bass-1",s.at(0.35),0.3)
    s.push(s.at(0.35),s.d-s.at(0.35),1.1,900,520)
