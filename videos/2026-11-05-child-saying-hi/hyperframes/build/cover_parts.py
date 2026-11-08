import sys
sys.path.insert(0,'.')
from rig import stick, INK, AMBER, RED, PAPER
import props as P
W,H=1080,1920
def frame(n,h1,h2,h3,sub,visual,ground=True):
    s=[f'<rect width="{W}" height="{H}" fill="#FAF7F2"/>']
    s.append(f'<rect x="80" y="280" width="260" height="96" rx="48" fill="{AMBER}" stroke="{INK}" stroke-width="6"/>')
    s.append(P.text("b",210,348,f"PART {n}",56,"#FFFFFF",stroke=INK,sw=6))
    s.append(P.text("sl",370,346,"A Shy Kid's Mind",48,"#5C5C5C",weight=800,anchor="start"))
    s.append(P.text("h1",540,520,h1,118,INK)); s.append(P.text("h2",540,650,h2,118,INK))
    s.append(f'<g>{P.text("h3",540,800,h3,150 if len(h3)<=10 else 128,RED,stroke=INK,sw=9)}</g>')
    s+=visual
    if ground: s.append(f'<line x1="0" y1="1532" x2="{W}" y2="1532" stroke="#CFC6B6" stroke-width="5"/>')
    s.append(P.text("sub",540,1630,sub,66,AMBER,stroke=INK,sw=6))
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(s)}</svg>'
    html=f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Nunito:wght@800;900&display=block" rel="stylesheet"><style>html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden}} text{{font-family:Nunito,sans-serif}}</style></head><body>{svg}</body></html>'
    open(f'../covers/cover{n}.html','w').write(html)

# Part 1: Om by the bench, thinking
v=[P.bench("bn",170,1530,0.8),
   stick("om",330,1530,0.85,"om",("worried",),("clasp",),look=(8,-2)),
   P.bubble("tb",680,1030,470,230,"Am I good\nenough?",62,tail=(400,1250),thought=True)]
for i,x in enumerate((780,860,940,1020)):
    v.append(stick(f"k{i}",x,1530,0.42,"kid",("happy",),(("celebrate","wave","throw","stand")[i],),cap=["#E03131","#1C7ED6","#2F9E44","#7048E8"][i],flip=i%2==1))
frame(1,"What he thinks","before saying",'"HI"',"10 steps feel like 10 km",v)

# Part 3: the rejection loop
v=[P.loop("lp",540,1180,250,("They'll reject me","I hang back","They don't invite me","See? I knew it."),["n0","n1","n2","n3"]),
   stick("om",540,1265,0.34,"om",("sad",),("crossed",))]
frame(3,"When fear","of rejection","COMES TRUE","The loop that keeps kids out",v,ground=False)

# Part 4: three cards
v=[P.numcard("c1",540,960,1,"Drop the label",900),P.numcard("c2",540,1170,2,'Small steps for "hi"',900),P.numcard("c3",540,1380,3,"Praise the attempt",900)]
frame(4,"3 things","to do for a","SHY CHILD","You can start tonight",v,ground=False)

# Part 5: the foggy mirror
v=[stick("om",290,1530,0.85,"om",("worried",),("clasp",),look=(8,0)),
   f'<defs><filter id="fg"><feGaussianBlur stdDeviation="16"/></filter><clipPath id="mc"><rect x="582" y="902" width="296" height="556" rx="120"/></clipPath></defs>',
   f'<g stroke="{INK}" stroke-width="7"><rect x="560" y="880" width="340" height="600" rx="140" fill="#7D8A96"/><rect x="582" y="902" width="296" height="556" rx="120" fill="#BCC7D1" stroke-width="5"/></g><line x1="600" y1="1480" x2="580" y2="1532" stroke="{INK}" stroke-width="7"/><line x1="860" y1="1480" x2="880" y2="1532" stroke="{INK}" stroke-width="7"/>',
   '<g clip-path="url(#mc)">',
   stick("m1",680,1330,0.45,"kid",("mock",),("stand",),cap="#E03131"),
   stick("m2",790,1330,0.45,"kid",("mock",),("stand",),cap="#1C7ED6",flip=True),
   '<g filter="url(#fg)" opacity="0.75" fill="#FFFFFF"><ellipse cx="640" cy="1010" rx="110" ry="80"/><ellipse cx="830" cy="1150" rx="90" ry="90"/><ellipse cx="650" cy="1400" rx="90" ry="60"/></g>',
   '</g>']
frame(5,"Why a smile","can look like","TEASING","How parents clear the fog",v)
