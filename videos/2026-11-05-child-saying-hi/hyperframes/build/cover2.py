import sys
sys.path.insert(0,'.')
from rig import stick, INK, AMBER, RED, PAPER
import props as P
W,H=1080,1920
s=[]
s.append(f'<rect width="{W}" height="{H}" fill="#FAF7F2"/>')
# badge + series label
s.append(f'<rect x="80" y="280" width="260" height="96" rx="48" fill="{AMBER}" stroke="{INK}" stroke-width="6"/>')
s.append(P.text("b",210,348,"PART 2",56,"#FFFFFF",stroke=INK,sw=6))
s.append(P.text("sl",370,346,"A Shy Kid's Mind",48,"#5C5C5C",weight=800,anchor="start"))
# headline
s.append(P.text("h1",540,520,"Kids think",118,INK))
s.append(P.text("h2",540,650,"they're",118,INK))
s.append(P.text("h3",540,800,"LESS LIKED",150,RED,stroke=INK,sw=9))
# gauges
s.append(P.gauge("g1",300,1020,170,"n1","",0.8))
s.append(P.gauge("g2",780,1020,170,"n2","",0.5))
s.append(P.text("l1",300,1090,"I like them",44,INK,weight=800))
s.append(P.text("l2",780,1090,"They like me",44,INK,weight=800))
s.append(P.text("v1",300,1155,"8/10",64,INK))
s.append(P.text("v2",780,1155,"5/10",64,RED,stroke=INK,sw=4))
# kids
s.append(stick("a",300,1530,0.85,"om",("worried",),("clasp",),look=(8,0)))
s.append(stick("b",780,1530,0.85,"kid",("happy",),("wave",),cap="#7048E8",flip=True,look=(8,0)))
s.append(f'<line x1="0" y1="1532" x2="{W}" y2="1532" stroke="#CFC6B6" stroke-width="5"/>')
# sub line
s.append(P.text("sub",540,1630,"It starts at age 5",70,AMBER,stroke=INK,sw=6))
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(s)}</svg>'
html=f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Nunito:wght@800;900&display=block" rel="stylesheet"><style>html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden}} text{{font-family:Nunito,sans-serif}}</style></head><body>{svg}</body></html>'
open('../covers/cover2.html','w').write(html)
