import props as P
from rig import INK, AMBER, RED, PAPER
from scenes1 import kids_group, park_om, CAPS
SC={}
def scene(n):
    def deco(f): SC[n]=f; return f
    return deco

# ---------------- INSIDE OM'S HEAD
@scene(19)
def _(s):
    s.bg("#EEF4F8")
    s.char("om",960,1250,2.4,"om",("worried",),("clasp",),look=(0,0))
    t=max(s.d-0.75,0.5)
    s.cam(t,0.7,{"scale":1,"opacity":1,"transformOrigin":"960px 560px"},{"scale":3.2,"opacity":0},"power3.in")
    s.sfx("whoosh",t+0.2,0.3)

def head_bubbles(s,n_visible,om_expr=("thinking",)):
    s.headroom()
    s.char("om",300,860,0.95,"om",om_expr,("think",),look=(8,-6))
    specs=[("b1",1000,230,760,170,"Will they let me play?"),
           ("b2",1330,470,760,170,"If I say something wrong,\nwill they laugh?"),
           ("b3",900,700,700,150,"Could I be their friend?")]
    for i,(nm,x,y,w,h,t) in enumerate(specs[:n_visible]):
        s.add(P.bubble(s.id(nm),x,y,w,h,t,54 if "\n" not in t else 46,tail=(430,500),thought=True))
    return specs

@scene(20)
def _(s):
    head_bubbles(s,1)
    s.cam(0,0.4,{"scale":1.2,"opacity":0,"transformOrigin":"960px 540px"},{"scale":1,"opacity":1},"power3.out")
    s.pop("b1",s.at(0.05),origin="0% 100%"); s.sfx("pop",s.at(0.05),0.25)

@scene(21)
def _(s):
    head_bubbles(s,2,("embarrassed",))
    for i,(x,y) in enumerate([(1800,370),(1830,560),(960,520)]):
        s.add(f'<g id="{s.id("lf"+str(i))}" transform="translate({x} {y})"><circle r="34" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/><path d="M-16 4 Q0 26 16 4 Z" fill="{INK}"/><circle cx="-11" cy="-8" r="4" fill="{INK}"/><circle cx="11" cy="-8" r="4" fill="{INK}"/></g>')
    s.pop("b2",s.at(0.05),origin="0% 100%"); s.sfx("pop",s.at(0.05),0.25)
    for i in range(3): s.pop("lf"+str(i),s.at(0.55)+i*0.1)

@scene(22)
def _(s):
    head_bubbles(s,3,("worried",))
    s.pop("b3",s.at(0.05),origin="0% 100%"); s.sfx("pop",s.at(0.05),0.25)

@scene(23)
def _(s):
    head_bubbles(s,3,("worried","sad"))
    s.add(f'<g id="{s.id("big")}"><g transform="translate(1080 470)"><ellipse cx="0" cy="0" rx="560" ry="200" fill="#C9CED3" stroke="{INK}" stroke-width="6"/><ellipse cx="-300" cy="-80" rx="200" ry="120" fill="#C9CED3"/><ellipse cx="260" cy="-90" rx="220" ry="120" fill="#C9CED3"/></g>'+P.text(s.id("bt"),1080,500,"Am I good enough?",92,INK)+'</g>')
    t=s.at(0.5)
    for i,nm in enumerate(("b1","b2","b3")):
        s.ft(nm,{"y":0,"opacity":1},{"y":-500,"opacity":0},t-0.4+i*0.08,0.6,"power3.in")
    s.ft("big",{"y":500,"opacity":0},{"y":0,"opacity":1},t,0.9,"expo.out")
    s.face("om","worried","sad",t+0.3)
    s.push(t,s.d-t,1.08,1080,470)

@scene(24)
def _(s):
    s.bg()
    s.char("ad",560,860,1.0,"adult",("happy",),("stand","wave"))
    s.pose("ad","stand","wave",s.at(0.1))
    s.add(P.stopwatch(s.id("sw"),1250,430)); s.add(P.text(s.id("lbl"),1250,640,"2 seconds",64,INK))
    s.pop("sw",s.at(0.2)); s.rise("lbl",s.at(0.55)); s.sfx("pop",s.at(0.2),0.25)

@scene(25)
def _(s):
    s.bg()
    s.char("om",560,860,1.0,"om",("panicked",),("clasp",))
    s.add(P.warning(s.id("wr"),1250,440,"RISK"))
    s.pop("wr",s.at(0.3),0.4,ease="back.out(2)"); s.shake("om",s.at(0.4),5,6)
    s.sfx("impact-bass-1",s.at(0.3),0.3)

@scene(26)
def _(s):
    s.bg("#2B2D42"); s.add(P.ground("#3A3D57","#4A4E6E"))
    s.add(P.spotlight(s.id("spot"),620))
    s.char("om",620,860,1.0,"om",("worried",),("clasp",),look=(8,0))
    for j,x in enumerate((1250,1450,1650)):
        s.char(f"k{j}",x,860,0.75,"kid",("neutral",),("holdsign",),cap=CAPS[j],flip=True)
        s.add(f'<g transform="translate({x} 735)"><g id="{s.id("cd"+str(j))}"><rect x="-48" y="-58" width="96" height="116" rx="10" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/><text x="0" y="20" text-anchor="middle" font-family="Nunito" font-size="58" font-weight="900" fill="{INK}">?</text></g></g>')
    s.add(P.text(s.id("yn"),960,170,"YES / NO ?",96,"#FFFFFF"))
    s.fadein("spot",0.1,0.5); s.rise("yn",s.at(0.6))
    for j in range(3):
        s.ft("cd"+str(j),{"scaleX":1,"transformOrigin":"50% 50%"},{"scaleX":0.08,"repeat":3,"yoyo":True},s.at(0.3)+j*0.15,0.35,"sine.inOut")

@scene(27)
def _(s):
    s.park(bench=None)
    s.char("om",600,860,1.0,"om",("neutral","worried"),("clasp",),look=(8,0))
    s.char("kid",1350,860,0.95,"kid",("neutral",),("stand",),cap=CAPS[0],flip=True)
    s.add(P.bubble(s.id("no"),1150,360,240,150,"No",80,tail=(1330,470)))
    s.pop("no",s.at(0.15)); s.face("om","neutral","worried",s.at(0.4))
    s.add(P.text(s.id("full"),1150,180,"“The game is full right now”",52,"#8A8A8A",weight=800))
    s.fadein("full",s.at(0.35))

@scene(28)
def _(s):
    s.park(bench=None)
    s.char("om",600,860,1.1,"om",("shocked","sad"),("clasp",),look=(8,0))
    s.add(P.bubble(s.id("no"),1050,330,240,150,"No",80,tail=(760,400)))
    s.add(P.bubble(s.id("nw"),1150,330,720,170,"We don't want you",70,tail=(780,480),fill=RED,txtfill="#FFFFFF"))
    s.ft("no",{"x":250,"opacity":1},{"x":0,"opacity":1},0,0.4,"power3.out")
    t=s.at(0.15)
    s.ft("no",{"opacity":1,"scale":1,"transformOrigin":"50% 50%"},{"opacity":0,"scale":0.6},t,0.15,"power2.in")
    s.ft("nw",{"opacity":0,"scale":0.6,"transformOrigin":"0% 100%"},{"opacity":1,"scale":1},t+0.08,0.3,"back.out(1.6)")
    s.face("om","shocked","sad",t+0.9); s.punch(t+0.1,1.05,760,450); s.sfx("glitch-1",t,0.35)

@scene(29)
def _(s):
    s.bg()
    s.char("om",300,860,1.0,"om",("thinking",),("think",),look=(8,-4))
    s.add(P.scale_balance(s.id("sc"),1100,860))
    t=s.at(0.35)
    s.ft("sc-beam",{"rotation":0,"svgOrigin":"0 -300"},{"rotation":12},t,0.8,"back.out(1.4)")
    s.sfx("impact-bass-2",t+0.25,0.3)

@scene(30)
def _(s):
    s.park(bench=430)
    s.add('<g>'); kids_group(s,[1300,1400,1500,1600,1700],sc=0.5,opacity=0.85); s.add('</g>')
    s.char("om",600,860,1.0,"om",("worried","sad"),("clasp",),("stand","walkA","walkB"),look=(7,0))
    s.add(P.footprints(s.id("fp"),650,760,840,2))
    t=s.at(0.05); s.walk("om",t,0.6,0,140,0.2)
    s.pop("fp0",t+0.2,0.2); s.pop("fp1",t+0.45,0.2)
    t2=s.at(0.62); s.walk("om",t2,0.8,140,-30,0.25); s.face("om","worried","sad",t2)

# ---------------- TEMPERAMENT
@scene(31)
def _(s):
    s.bg()
    s.char("om",480,860,1.0,"om",("sad","relieved"),("clasp",))
    s.add(P.stamp(s.id("st"),1250,430,"SOMETHING WRONG?",RED,74))
    s.add(f'<line id="{s.id("strike")}" x1="820" y1="430" x2="1680" y2="430" stroke="{INK}" stroke-width="14" stroke-linecap="round"/>')
    s.pop("st",0.2,0.4,ease="back.out(2)"); s.sfx("pop",0.2,0.3)
    s.draw("strike",s.at(0.55),0.4,900); s.face("om","sad","relieved",s.at(0.7))

def research_card(s,l1,l2,bg="plain"):
    s.bg("#F6F1EA")
    s.add(P.text(s.id("bgq"),960,300,"THE RESEARCH",44,"#7D7263",weight=800))
    s.add(P.card(s.id("card"),960,470,l1,l2,980,230))
    s.ft("card",{"x":-400,"opacity":0},{"x":0,"opacity":1},0.15,0.6,"expo.out")
    s.sfx("whoosh-short",0.15,0.25)

@scene(32)
def _(s): research_card(s,"Jerome Kagan, Harvard","Kagan, Reznick & Snidman, 1988")

@scene(33)
def _(s):
    s.nursery()
    s.char("mom",200,860,0.9,"mom",("happy",))
    s.add(f'<g transform="translate(1560 860)"><rect id="{s.id("toy")}" x="-50" y="-100" width="100" height="100" rx="10" fill="{AMBER}" stroke="{INK}" stroke-width="6"/></g>')
    s.baby("b1",420,770,1.3,"happy",(8,0)); s.baby("b2",420,930,1.3,"thinking",(-8,0))
    s.ft("b1",{"x":0},{"x":900},s.at(0.1),s.vd*0.6,"power1.inOut")
    s.ft("b2-head",{"rotation":0,"svgOrigin":"78 -70"},{"rotation":-12},s.at(0.2),0.4,"power2.out")
    s.ft("b2-head",{"rotation":-12},{"rotation":0},s.at(0.6),0.4,"power2.out")
    s.ft("b2",{"x":0},{"x":260},s.at(0.65),s.d-s.at(0.65),"power1.inOut")

@scene(34)
def _(s):
    s.nursery()
    s.add(f'<g transform="translate(1560 860)"><rect x="-50" y="-100" width="100" height="100" rx="10" fill="{AMBER}" stroke="{INK}" stroke-width="6"/></g>')
    s.baby("b1",1380,770,1.3,"happy"); s.baby("b2",680,930,1.3,"thinking",(8,-4))
    s.add(P.text(s.id("t1"),960,250,"Look first,",96,INK)); s.add(P.text(s.id("t2"),960,370,"then join",96,AMBER,stroke=INK,sw=7))
    s.add(P.text(s.id("bi"),960,130,"Behavioural inhibition",52,"#6B6B6B",weight=800))
    s.fadein("bi",s.at(0.1)); s.rise("t1",s.at(0.6)); s.rise("t2",s.at(0.8))

@scene(35)
def _(s):
    s.nursery()
    s.baby("b2",820,920,1.15,"happy",(4,0))
    s.add(P.stamp(s.id("st"),960,360,"TEMPERAMENT",AMBER,96,rot=-4))
    s.pop("st",s.at(0.15),0.4,ease="back.out(2)"); s.sfx("pop",s.at(0.15),0.3)

@scene(36)
def _(s): research_card(s,"Thomas & Chess, 1977","“Slow to warm up”")

@scene(37)
def _(s):
    s.park(bench=None)
    kids_group(s,[1250,1400,1550],sc=0.6,poses=["celebrate","throw","wave"])
    s.char("tod",420,860,0.7,"kid",("thinking","happy"),("clasp",),("stand","walkA","walkB"),cap="#F783AC",look=(8,0))
    s.add(f'<circle id="{s.id("ring")}" cx="420" cy="500" r="46" fill="none" stroke="{AMBER}" stroke-width="12" transform="rotate(-90 420 500)"/>')
    s.add(f'<circle cx="420" cy="500" r="46" fill="none" stroke="#E5DED3" stroke-width="12" opacity="0.6"/>')
    s.draw("ring",s.at(0.05),s.vd*0.5,290)
    t=s.at(0.6); s.face("tod","thinking","happy",t)
    s.walk("tod",t,s.d-t-0.1,0,(1080-420)/0.7,0.22)
    s.fadeout("ring",t)

@scene(38)
def _(s):
    s.park(bench=None)
    kids_group(s,[1250,1400,1550],sc=0.75,poses=["celebrate","wave","stand"])
    s.char("kid",500,860,0.55,"kid",("relieved","happy"),("clasp","wave"),("stand","walkA","walkB"),cap="#F783AC")
    seg=s.vd/4
    for i,sc in enumerate((0.7,0.85,1.0)):
        a=[1,0.7/0.55,0.85/0.55,1/0.55][i]; b=[0.7/0.55,0.85/0.55,1/0.55][i]
        s.ft("kid",{"scale":a,"transformOrigin":"50% 100%"},{"scale":b},s.v+seg*i,seg*0.8,"back.out(1.4)")
    t=s.v+seg*3; s.face("kid","relieved","happy",t); s.pose("kid","clasp","wave",t+0.3)
    s.walk("kid",t,seg,0,(1050-500)/1.0,0.24)

@scene(39)
def _(s):
    s.bg()
    s.char("om",700,860,1.15,"om",("thinking",),("reach",),look=(8,-4))
    s.add(f'<g transform="translate(870 580)"><g id="{s.id("hm")}"><line x1="0" y1="40" x2="0" y2="110" stroke="{INK}" stroke-width="10" stroke-linecap="round"/><circle cx="0" cy="0" r="56" fill="#BCC7D1" stroke="#7D8A96" stroke-width="12"/></g></g>')
    s.add(P.text(s.id("q"),1400,420,"What am I like?",80,INK))
    s.pop("hm",s.at(0.3)); s.rise("q",s.at(0.6))
    s.push(s.at(0.2),s.d-s.at(0.2),1.08,900,500)
