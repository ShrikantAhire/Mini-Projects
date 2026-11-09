from rig import INK,PAPER,AMBER,RED,BLUE,GREEN,SKY
GROUND=860
def g(id,inner,x=0,y=0,s=1,extra=""):
    return f'<g transform="translate({x} {y}) scale({s})"><g id="{id}" {extra}>{inner}</g></g>'
ST=f'stroke="{INK}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
def text(id,x,y,t,size=64,fill=INK,weight=900,anchor="middle",stroke=None,sw=0,extra=""):
    st=f' stroke="{stroke}" stroke-width="{sw}" paint-order="stroke" stroke-linejoin="round"' if stroke else ''
    t=t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f'<text id="{id}" x="{x}" y="{y}" font-family="Nunito" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{st} {extra}>{t}</text>'
def ground(color="#E8E2D6",line="#CFC6B6"):
    return f'<rect x="0" y="{GROUND}" width="1920" height="{1080-GROUND}" fill="{color}"/><line x1="0" y1="{GROUND}" x2="1920" y2="{GROUND}" stroke="{line}" stroke-width="4"/>'
def tree(x,y=GROUND,s=1):
    return f'<g transform="translate({x} {y}) scale({s})" {ST}><path d="M0 0 L0 -200" fill="none" stroke-width="12"/><circle cx="0" cy="-280" r="110" fill="#8FCB8F"/></g>'
def bench(id,x,y=GROUND,s=1):
    return g(id,f'<g {ST} fill="#B08968"><rect x="-110" y="-150" width="220" height="24" rx="6"/><rect x="-110" y="-96" width="220" height="24" rx="6"/><line x1="-80" y1="-72" x2="-80" y2="0"/><line x1="80" y1="-72" x2="80" y2="0"/><line x1="-80" y1="-126" x2="-80" y2="-96"/><line x1="80" y1="-126" x2="80" y2="-96"/></g>',x,y,s)
def ball(id,x,y,r=26,fill="#FFD43B"):
    return g(id,f'<circle cx="0" cy="0" r="{r}" fill="{fill}" {ST} stroke-width="6"/><path d="M{-r*0.7} {-r*0.3} Q0 {r*0.4} {r*0.7} {-r*0.3}" fill="none" stroke="{INK}" stroke-width="4"/>',x,y)
def footprints(prefix,x0,x1,y,n=10):
    out=""
    for i in range(n):
        x=x0+(x1-x0)*i/(n-1); dy=-10 if i%2 else 10
        out+=g(f"{prefix}{i}",f'<ellipse cx="0" cy="{dy}" rx="16" ry="9" fill="#A8A29E"/>',round(x,1),y)
    return out
def tape(id,x0,x1,y,h0,h1,label,label_id=None,fill=RED,txt_size=64):
    def tp(x): t=(x-x0)/(x1-x0); return y-(h0+(h1-h0)*t)/2
    def bt(x): t=(x-x0)/(x1-x0); return y+(h0+(h1-h0)*t)/2
    s=f'<path d="M{x0} {tp(x0):.1f} L{x1} {tp(x1):.1f} L{x1} {bt(x1):.1f} L{x0} {bt(x0):.1f} Z" fill="{fill}" {ST} stroke-width="6"/>'
    x=x0+24; k=0
    while x<x1-6:
        hh=(h0+(h1-h0)*(x-x0)/(x1-x0))*(0.24 if k%5==0 else 0.13)
        s+=f'<line x1="{x:.1f}" y1="{tp(x)+4:.1f}" x2="{x:.1f}" y2="{tp(x)+4+hh:.1f}" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round"/>'
        x+=26; k+=1
    lx=x0+(x1-x0)*0.35
    s+=text(label_id or id+"-lbl",lx,(tp(lx)+bt(lx))/2+txt_size*0.36,label,txt_size,"#FFFFFF",stroke=INK,sw=6)
    return g(id,s)
def bubble(id,x,y,w,h,txt,size=56,tail=(0,0),fill="#FFFFFF",txtfill=INK,thought=False,txt_id=None):
    """x,y = centre. tail = point the tail goes to (absolute)."""
    s=""
    if thought:
        s+=f'<g {ST} stroke-width="6" fill="{fill}">'
        for i,(fx,fy) in enumerate([(-w*0.32,-h*0.18),(0,-h*0.3),(w*0.32,-h*0.18),(w*0.36,h*0.16),(0,h*0.26),(-w*0.36,h*0.16)]):
            s+=f'<ellipse cx="{fx:.0f}" cy="{fy:.0f}" rx="{w*0.3:.0f}" ry="{h*0.38:.0f}"/>'
        s+='</g>'
        s+=f'<rect x="{-w*0.42:.0f}" y="{-h*0.36:.0f}" width="{w*0.84:.0f}" height="{h*0.72:.0f}" fill="{fill}"/>'
        tx,ty=tail[0]-x,tail[1]-y
        for i,f in enumerate([0.55,0.75,0.9]):
            s+=f'<circle cx="{tx*f:.0f}" cy="{ty*f:.0f}" r="{14-i*4}" fill="{fill}" {ST} stroke-width="5"/>'
    else:
        tx,ty=tail[0]-x,tail[1]-y
        s+=f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="{min(h/2,44)}" fill="{fill}" {ST} stroke-width="6"/>'
        if tail!=(0,0):
            bx=max(-w/2+50,min(w/2-50,tx*0.3)); by=h/2 if ty>0 else -h/2
            s+=f'<path d="M{bx-26:.0f} {by:.0f} L{tx:.0f} {ty:.0f} L{bx+26:.0f} {by:.0f}" fill="{fill}" {ST} stroke-width="6"/><line x1="{bx-22:.0f}" y1="{by:.0f}" x2="{bx+22:.0f}" y2="{by:.0f}" stroke="{fill}" stroke-width="9"/>'
    lines=txt.split("\n")
    for i,l in enumerate(lines):
        yy=(i-(len(lines)-1)/2)*size*1.12+size*0.35
        s+=text((txt_id or id+"-t")+(f"{i}" if i else ""),0,round(yy,1),l,size,txtfill)
    return g(id,s,x,y)
def card(id,x,y,l1,l2="",w=820,h=200):
    w=max(w,int(len(l1)*31+260),int(len(l2)*22+260))
    s=f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="22" fill="#FFFFFF" {ST} stroke-width="6"/>'
    s+=f'<g transform="translate({-w/2+80} 0)" {ST} stroke-width="5"><rect x="-38" y="-52" width="76" height="104" rx="8" fill="#F1E9DF"/><rect x="-18" y="-62" width="36" height="20" rx="5" fill="#B0B8C1"/><line x1="-22" y1="-14" x2="22" y2="-14"/><line x1="-22" y1="6" x2="22" y2="6"/><line x1="-22" y1="26" x2="10" y2="26"/></g>'
    tx=-w/2+150
    if l2:
        s+=text(id+"-a",tx,-10,l1,54,INK,anchor="start")+text(id+"-b",tx,52,l2,40,"#5C5C5C",weight=800,anchor="start")
    else:
        s+=text(id+"-a",tx,18,l1,54,INK,anchor="start")
    return g(id,s,x,y)
def gauge(id,x,y,r,needle_id,label="",val=0.5,label_size=40):
    s=f'<defs><linearGradient id="{id}-gr" x1="0" x2="1"><stop offset="0" stop-color="{RED}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient></defs>'
    s+=f'<path d="M{-r} 0 A{r} {r} 0 0 1 {r} 0 Z" fill="#FFFFFF" {ST} stroke-width="6"/>'
    s+=f'<path d="M{-r*0.82} 0 A{r*0.82} {r*0.82} 0 0 1 {r*0.82} 0" fill="none" stroke="url(#{id}-gr)" stroke-width="{r*0.16}"/>'
    ang=-90+180*val
    s+=f'<g id="{needle_id}" transform="rotate({ang-0:.1f})"><line x1="0" y1="0" x2="0" y2="{-r*0.72}" stroke="{INK}" stroke-width="7" stroke-linecap="round"/></g><circle cx="0" cy="0" r="10" fill="{INK}"/>'
    if label: s+=text(id+"-l",0,label_size*1.2,label,label_size,INK,weight=800)
    return g(id,s,x,y)
def scale_balance(id,x,y,left="Hi",right="Rejection"):
    s=f'<g {ST}><line x1="0" y1="0" x2="0" y2="-300"/><line x1="-80" y1="0" x2="80" y2="0"/></g>'
    s+=f'<g id="{id}-beam"><g {ST}><line x1="-260" y1="-300" x2="260" y2="-300"/><line x1="-240" y1="-300" x2="-240" y2="-200"/><line x1="240" y1="-300" x2="240" y2="-200"/><path d="M-320 -200 Q-240 -150 -160 -200 Z" fill="#E9E2D6"/><path d="M160 -200 Q240 -150 320 -200 Z" fill="#E9E2D6"/></g>'
    s+=text(id+"-lt",-240,-215,left,54,AMBER,stroke=INK,sw=6)
    s+=f'<path d="M160 -205 Q170 -300 240 -310 Q320 -300 320 -205 Z" fill="#8C8C8C" {ST} stroke-width="6"/>'+text(id+"-rt",240,-238,right,40,"#FFFFFF",stroke=INK,sw=5)
    s+='</g>'
    return g(id,s,x,y)
def mirror(id,x,y,w=300,h=520,fog_id=None):
    s=f'<g {ST}><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="{w*0.42}" fill="#7D8A96"/><rect x="{-w/2+22}" y="{-h/2+22}" width="{w-44}" height="{h-44}" rx="{w*0.36}" fill="#BCC7D1" stroke-width="5"/></g>'
    return g(id,s,x,y)
def stopwatch(id,x,y):
    s=f'<g {ST}><rect x="-14" y="-118" width="28" height="22" rx="4" fill="#B0B8C1"/><circle cx="0" cy="0" r="96" fill="#FFFFFF"/><line x1="0" y1="0" x2="40" y2="-50"/></g>'+text(id+"-t",0,60,"0:02",44,INK)
    return g(id,s,x,y)
def warning(id,x,y,word="RISK"):
    s=f'<path d="M0 -130 L130 100 L-130 100 Z" fill="{RED}" {ST} stroke-width="8"/>'+text(id+"-t",0,70,word,56,"#FFFFFF")+f'<text x="0" y="12" font-family="Nunito" font-size="110" font-weight="900" fill="#FFFFFF" text-anchor="middle">!</text>'
    return g(id,s,x,y)
def label(id,x,y,word,w=None,size=54,fill=RED,rot=-6):
    w=w or len(word)*size*0.72+40
    s=f'<g transform="rotate({rot})"><rect x="{-w/2}" y="{-size*0.75}" width="{w}" height="{size*1.5}" rx="12" fill="{fill}" {ST} stroke-width="5"/>'+text(id+"-t",0,size*0.36,word,size,"#FFFFFF")+'</g>'
    return g(id,s,x,y)
def house(id,x,y,glow=False):
    s=""
    if glow: s+=f'<circle id="{id}-glow" cx="0" cy="-150" r="260" fill="{AMBER}" opacity="0.22"/>'
    s+=f'<g {ST}><rect x="-150" y="-220" width="300" height="220" fill="#FFF4E0"/><path d="M-185 -210 L0 -360 L185 -210 Z" fill="{AMBER}"/><rect x="-40" y="-120" width="80" height="120" fill="#B08968"/><rect x="60" y="-180" width="60" height="60" fill="#BFE3FF"/></g>'
    return g(id,s,x,y)
def balloons(id,x,y):
    s=f'<g {ST} stroke-width="5"><path d="M0 0 Q-20 -80 -40 -170 M0 0 Q10 -90 30 -200 M0 0 Q30 -60 90 -150" fill="none" stroke-width="3"/><ellipse cx="-40" cy="-220" rx="46" ry="56" fill="{RED}"/><ellipse cx="30" cy="-250" rx="44" ry="54" fill="{AMBER}"/><ellipse cx="94" cy="-196" rx="40" ry="50" fill="#0CA678"/></g>'
    return g(id,s,x,y)
def table(id,x,y=GROUND,w=360):
    s=f'<g {ST}><rect x="{-w/2}" y="-200" width="{w}" height="22" rx="6" fill="#B08968"/><line x1="{-w/2+30}" y1="-178" x2="{-w/2+30}" y2="0"/><line x1="{w/2-30}" y1="-178" x2="{w/2-30}" y2="0"/></g>'
    return g(id,s,x,y)
def blackboard(id,x,y):
    s=f'<g {ST}><rect x="-300" y="-170" width="600" height="340" rx="10" fill="#2F4F3E" stroke="#8B5E3C" stroke-width="16"/></g><path d="M-220 -80 q30 -30 60 0 t60 0 M-220 0 L80 0 M-220 70 L-20 70" fill="none" stroke="#E8F0E8" stroke-width="5" stroke-linecap="round" opacity="0.8"/>'
    return g(id,s,x,y)
def desk(id,x,y=GROUND):
    s=f'<g {ST}><rect x="-110" y="-150" width="220" height="20" rx="5" fill="#C9A27A"/><line x1="-90" y1="-130" x2="-90" y2="0"/><line x1="90" y1="-130" x2="90" y2="0"/></g>'
    return g(id,s,x,y)
def door(id,x,y=GROUND):
    s=f'<g {ST}><rect x="-90" y="-400" width="180" height="400" fill="#C9A27A"/><circle cx="55" cy="-200" r="10" fill="{INK}"/></g>'
    return g(id,s,x,y)
def sofa(id,x,y=GROUND,w=520):
    s=f'<g {ST}><rect x="{-w/2}" y="-230" width="{w}" height="120" rx="30" fill="#E07A5F"/><rect x="{-w/2-30}" y="-160" width="{w+60}" height="110" rx="26" fill="#E07A5F"/><line x1="{-w/2}" y1="-50" x2="{-w/2}" y2="0"/><line x1="{w/2}" y1="-50" x2="{w/2}" y2="0"/></g>'
    return g(id,s,x,y)
def window(id,x,y):
    s=f'<g {ST}><rect x="-130" y="-110" width="260" height="220" fill="#DDF0FF"/><line x1="0" y1="-110" x2="0" y2="110"/><line x1="-130" y1="0" x2="130" y2="0"/></g>'
    return g(id,s,x,y)
def heart(id,x,y,s=1,fill=AMBER):
    return g(id,f'<path d="M0 30 C-70 -20 -50 -90 0 -55 C50 -90 70 -20 0 30 Z" fill="{fill}" {ST} stroke-width="6"/>',x,y,s)
def arrow(id,x1,y1,x2,y2,color=INK,w=8):
    import math
    a=math.atan2(y2-y1,x2-x1); hl=30
    p1=(x2-hl*math.cos(a-0.5),y2-hl*math.sin(a-0.5)); p2=(x2-hl*math.cos(a+0.5),y2-hl*math.sin(a+0.5))
    return g(id,f'<path d="M{x1} {y1} L{x2} {y2} M{p1[0]:.0f} {p1[1]:.0f} L{x2} {y2} L{p2[0]:.0f} {p2[1]:.0f}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
def numcard(id,x,y,n,txt,w=900):
    s=f'<rect x="{-w/2}" y="-90" width="{w}" height="180" rx="26" fill="#FFFFFF" {ST} stroke-width="6"/><circle cx="{-w/2+100}" cy="0" r="58" fill="{AMBER}" {ST} stroke-width="6"/>'
    s+=text(id+"-n",-w/2+100,24,str(n),70,"#FFFFFF",stroke=INK,sw=5)+text(id+"-t",-w/2+190,22,txt,62,INK,anchor="start")
    return g(id,s,x,y)
def xmark(id,x,y,s=1,color=RED):
    return g(id,f'<path d="M-40 -40 L40 40 M40 -40 L-40 40" stroke="{color}" stroke-width="14" stroke-linecap="round"/>',x,y,s)
def lunchbox(id,x,y):
    return g(id,f'<g {ST} stroke-width="5"><rect x="-50" y="-34" width="100" height="40" rx="8" fill="#4DABF7"/><path d="M-50 -34 L-40 -64 L40 -64 L50 -34" fill="#A5D8FF"/></g>',x,y)
def cup(id,x,y):
    return g(id,f'<g {ST} stroke-width="5"><path d="M-22 -40 L22 -40 L18 0 L-18 0 Z" fill="#FFFFFF"/><path d="M22 -30 q16 4 0 20" fill="none"/></g>',x,y)
def plant(id,x,y=GROUND):
    return g(id,f'<g {ST} stroke-width="5"><path d="M-40 0 L-50 -90 L50 -90 L40 0 Z" fill="#C9805A"/><path d="M0 -90 Q-60 -170 -70 -230 M0 -90 Q10 -190 0 -260 M0 -90 Q60 -170 80 -220" fill="none" stroke="#2F9E44" stroke-width="10"/></g>',x,y)
def calendar(id,x,y,txt="1 year later"):
    s=f'<g {ST} stroke-width="6"><rect x="-130" y="-130" width="260" height="250" rx="16" fill="#FFFFFF"/><rect x="-130" y="-130" width="260" height="60" rx="16" fill="{RED}"/></g>'+text(id+"-t",0,40,"12",110,INK)
    return g(id,s,x,y)
def chart(id,x,y):
    s=f'<g {ST} stroke-width="6"><rect x="-150" y="-110" width="300" height="220" rx="12" fill="#FFFFFF"/></g><path id="{id}-line" d="M-110 -50 L-40 -30 L20 10 L100 60" fill="none" stroke="{RED}" stroke-width="9" stroke-linecap="round"/>'
    return g(id,s,x,y)
def stamp(id,x,y,word,color=RED,size=90,rot=-8):
    w=len(word)*size*0.7+60
    return g(id,f'<g transform="rotate({rot})"><rect x="{-w/2}" y="{-size*0.8}" width="{w}" height="{size*1.6}" rx="14" fill="none" stroke="{color}" stroke-width="10"/>'+text(id+"-t",0,size*0.36,word,size,color)+'</g>',x,y)
def spotlight(id,x,y=GROUND):
    return g(id,f'<path d="M-40 -760 L40 -760 L220 0 L-220 0 Z" fill="#FFF3BF" opacity="0.8"/><ellipse cx="0" cy="0" rx="220" ry="34" fill="#FFE8A1"/>',x,y)
def loop(id,x,y,r=300,nodes=("","","",""),node_ids=None):
    import math
    s=f'<circle cx="0" cy="0" r="{r}" fill="none" stroke="#B0B8C1" stroke-width="10" stroke-dasharray="1 0"/>'
    angs=[-90,0,90,180]
    for i,a in enumerate(angs):
        a2=math.radians(a+45)
        ax,ay=r*math.cos(a2),r*math.sin(a2)
        s+=f'<path d="M{ax:.0f} {ay:.0f} l{-22*math.sin(a2)+18*math.cos(a2):.0f} {22*math.cos(a2)+18*math.sin(a2):.0f}" stroke="{INK}" stroke-width="0"/>'
    for i,a in enumerate(angs):
        ar=math.radians(a); nx,ny=r*math.cos(ar),r*math.sin(ar)
        nid=(node_ids or [f"{id}-n{j}" for j in range(4)])[i]
        s+=f'<g transform="translate({nx:.0f} {ny:.0f})"><g id="{nid}"><rect x="-230" y="-52" width="460" height="104" rx="52" fill="#FFFFFF" {ST} stroke-width="6"/>'+text(nid+"-t",0,16,nodes[i],42,INK)+'</g></g>'
    return g(id,s,x,y)
def gavel(id,x,y):
    return g(id,f'<g {ST}><rect x="-90" y="-50" width="180" height="70" rx="14" fill="#8B5E3C"/><line x1="0" y1="20" x2="0" y2="200" stroke-width="16"/></g>',x,y)
def radar(id,x,y):
    return g(id,f'<g fill="none" stroke="{RED}" stroke-width="6" stroke-linecap="round"><path d="M-30 -20 Q0 -50 30 -20"/><path d="M-55 -40 Q0 -90 55 -40"/><path d="M-80 -60 Q0 -130 80 -60"/></g>',x,y)
def chain(id,x,y):
    return g(id,f'<g {ST} fill="none" stroke-width="10"><ellipse cx="-30" cy="0" rx="50" ry="28"/><ellipse cx="30" cy="0" rx="50" ry="28"/></g>',x,y)
def share_icon(id,x,y):
    return g(id,f'<g {ST} stroke-width="10" fill="none"><path d="M-70 40 Q-60 -60 40 -60"/><path d="M10 -100 L60 -60 L10 -20"/></g>',x,y,2)
def comment_icon(id,x,y):
    return g(id,f'<path d="M-110 -80 H110 Q140 -80 140 -50 V40 Q140 70 110 70 H-30 L-80 120 L-70 70 H-110 Q-140 70 -140 40 V-50 Q-140 -80 -110 -80 Z" fill="#FFFFFF" {ST} stroke-width="8"/><circle cx="-60" cy="-5" r="12" fill="{INK}"/><circle cx="0" cy="-5" r="12" fill="{INK}"/><circle cx="60" cy="-5" r="12" fill="{INK}"/>',x,y)
def timeline_axis(id,x0,x1,y,ticks):
    s=f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
    for lab,xx in ticks:
        s+=f'<line x1="{xx}" y1="{y-18}" x2="{xx}" y2="{y+18}" stroke="{INK}" stroke-width="6"/>'+text(f"{id}-{lab}",xx,y+70,lab,46,INK,weight=800)
    return g(id,s)
def tag(id,x,y,word,fill="#FFFFFF",color=INK,size=44):
    w=len(word)*size*0.62+50
    return g(id,f'<rect x="{-w/2}" y="{-size*0.8}" width="{w}" height="{size*1.6}" rx="{size*0.8}" fill="{fill}" {ST} stroke-width="5"/>'+text(id+"-t",0,size*0.35,word,size,color),x,y)
def counter_kitchen(id,x,y=GROUND):
    return g(id,f'<g {ST}><rect x="-300" y="-260" width="600" height="260" fill="#E9ECEF"/><rect x="-320" y="-280" width="640" height="30" rx="6" fill="#ADB5BD"/></g>',x,y)
def name_tag(id,x,y):
    return g(id,f'<rect x="-120" y="-70" width="240" height="140" rx="14" fill="{RED}" {ST} stroke-width="6"/><rect x="-100" y="-10" width="200" height="66" fill="#FFFFFF"/>'+text(id+"-t",0,-24,"HELLO",44,"#FFFFFF")+text(id+"-t2",0,40,"my name is",28,INK,weight=800),x,y)

def pancakes(id,x,y,candle=True):
    s=f'<g {ST} stroke-width="6"><ellipse cx="0" cy="10" rx="170" ry="34" fill="#FFFFFF"/>'
    for i in range(3): s+=f'<ellipse cx="0" cy="{-14-i*30}" rx="120" ry="30" fill="#E8B04A"/>'
    s+='</g>'
    if candle:
        s+=f'<g {ST} stroke-width="5"><rect x="-10" y="-150" width="20" height="62" fill="#74C0FC"/></g><path id="{id}-flame" d="M0 -186 Q-14 -164 0 -152 Q14 -164 0 -186 Z" fill="{AMBER}" stroke="{RED}" stroke-width="3"/>'
    return g(id,s,x,y)
def bday_card(id,x,y,txt="Happy 8th, Leo!"):
    s=f'<g {ST} stroke-width="6"><path d="M-150 -100 L150 -100 L150 100 L-150 100 Z" fill="#FFF0F6"/><path d="M-150 -100 L0 10 L150 -100" fill="none"/></g>'+heart(id+"-h",0,40,0.5,RED)+text(id+"-t",0,-120,txt,40,INK)
    return g(id,s,x,y)
def camera(id,x,y=GROUND):
    s=f'<g {ST}><line x1="0" y1="-300" x2="-80" y2="0"/><line x1="0" y1="-300" x2="80" y2="0"/><line x1="0" y1="-300" x2="0" y2="0"/><rect x="-90" y="-400" width="180" height="110" rx="14" fill="#495057"/><rect x="-40" y="-430" width="70" height="30" rx="6" fill="#868E96"/><circle cx="0" cy="-345" r="38" fill="#ADB5BD"/><circle cx="0" cy="-345" r="18" fill="#212529"/></g>'
    return g(id,s,x,y)
def flash(id):
    return f'<rect id="{id}" x="0" y="0" width="1920" height="1080" fill="#FFFFFF" opacity="0"/>'
def paper(id,x,y,score,color=INK,s=1,name=""):
    o=f'<g {ST} stroke-width="6"><rect x="-150" y="-200" width="300" height="400" rx="10" fill="#FFFFFF"/></g>'
    for i in range(5): o+=f'<line x1="-110" y1="{-90+i*50}" x2="{90 if i%2 else 60}" y2="{-90+i*50}" stroke="#ADB5BD" stroke-width="8" stroke-linecap="round"/>'
    o+=f'<circle cx="80" cy="-130" r="58" fill="none" stroke="{RED}" stroke-width="7"/>'+text(id+"-sc",80,-112 if len(score)<=4 else -116,score,54 if len(score)<=3 else 40 if len(score)==4 else 34,color)
    if name: o+=text(id+"-nm",0,262,name,44,"#5C5C5C",weight=800)
    return g(id,o,x,y,s)
def tray(id,x,y):
    s=f'<g {ST} stroke-width="6"><rect x="-120" y="-20" width="240" height="34" rx="8" fill="#ADB5BD"/><ellipse cx="-50" cy="-32" rx="40" ry="16" fill="#FFD43B"/><rect x="30" y="-70" width="40" height="52" rx="6" fill="#FFFFFF"/><circle cx="-60" cy="-44" r="14" fill="#2F9E44"/></g>'
    return g(id,s,x,y)
def lunch_table(id,x,y=GROUND,w=760,seats=4):
    s=f'<g {ST}><rect x="{-w/2}" y="-190" width="{w}" height="26" rx="8" fill="#C9A27A"/><line x1="{-w/2+40}" y1="-164" x2="{-w/2+40}" y2="0"/><line x1="{w/2-40}" y1="-164" x2="{w/2-40}" y2="0"/></g>'
    return g(id,s,x,y)
def napkin(id,x,y,l1="THE CLUB",l2="Members only",rot=-4):
    s=f'<g transform="rotate({rot})"><rect x="-220" y="-110" width="440" height="220" rx="8" fill="#FFFFFF" {ST} stroke-width="6"/>'+text(id+"-a",0,-6,l1,76,RED)+text(id+"-b",0,62,l2,44,INK,weight=800)+'</g>'
    return g(id,s,x,y)
def bathtub(id,x,y=GROUND):
    s=f'<g {ST}><path d="M-300 -260 L300 -260 L270 -40 Q260 0 220 0 L-220 0 Q-260 0 -270 -40 Z" fill="#FFFFFF"/><line x1="-220" y1="0" x2="-240" y2="30"/><line x1="220" y1="0" x2="240" y2="30"/></g>'
    for i,(bx,by,r) in enumerate([(-220,-280,40),(-150,-300,50),(-60,-290,36),(140,-290,44),(220,-282,36),(40,-300,30)]):
        s+=f'<circle cx="{bx}" cy="{by}" r="{r}" fill="#E7F5FF" stroke="#74C0FC" stroke-width="4"/>'
    return g(id,s,x,y)
def bed(id,x,y=GROUND):
    s=f'<g {ST}><rect x="-420" y="-200" width="840" height="120" rx="20" fill="#748FFC"/><rect x="-460" y="-330" width="40" height="330" rx="10" fill="#8B5E3C"/><rect x="420" y="-240" width="40" height="240" rx="10" fill="#8B5E3C"/><rect x="-400" y="-250" width="170" height="70" rx="30" fill="#FFFFFF"/></g>'
    return g(id,s,x,y)
def blanket(id,x,y=GROUND):
    return g(id,f'<path d="M-240 -200 Q-200 -270 0 -262 Q260 -270 420 -200 L420 -120 L-240 -120 Z" fill="#91A7FF" {ST}/>',x,y)
def listboard(id,x,y,items,w=760,size=48,title=None):
    h=len(items)*size*1.6+(110 if title else 60)
    s=f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="24" fill="#FFFFFF" {ST} stroke-width="6"/>'
    y0=-h/2+(110 if title else 50)
    if title: s+=text(id+"-ti",0,-h/2+70,title,54,INK)
    for i,it in enumerate(items):
        yy=y0+i*size*1.6+size*0.9
        s+=f'<g id="{id}-r{i}">'+text(f"{id}-i{i}",-w/2+60,yy,it,size,INK,weight=800,anchor="start")+'</g>'
        s+=f'<line id="{id}-x{i}" x1="{-w/2+50}" y1="{yy-size*0.32:.0f}" x2="{-w/2+60+len(it)*size*0.52:.0f}" y2="{yy-size*0.32:.0f}" stroke="{RED}" stroke-width="8" stroke-linecap="round"/>'
    return g(id,s,x,y)
def drawing(id,x,y,good=True):
    s=f'<rect x="-170" y="-130" width="340" height="260" rx="8" fill="#FFFFFF" {ST} stroke-width="6"/>'
    if good:
        s+=f'<g stroke="#8B5E3C" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M-90 10 Q-80 -40 0 -40 Q60 -40 80 -10 L112 -72 L126 -66 L104 -2 Q100 20 80 20 L-80 20 Z" fill="#E8C39E"/><path d="M-70 20 L-80 90 M-40 20 L-34 90 M40 20 L34 90 M70 20 L80 90 M-90 10 Q-130 20 -126 70"/><path d="M118 -70 L112 -92 L126 -78"/></g>'
    else:
        s+=f'<g stroke="#8B5E3C" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="-10" cy="10" rx="80" ry="38" fill="#E8C39E"/><circle cx="84" cy="-20" r="34" fill="#E8C39E"/><path d="M60 -46 L54 -76 L74 -54 M100 -46 L112 -74 L112 -46 M-60 44 L-64 80 M-20 46 L-20 82 M20 46 L22 82 M50 40 L56 78 M-90 0 Q-120 -20 -110 -50"/><path d="M110 -10 q10 6 0 12" /></g>'
    return g(id,s,x,y)
def areabox(id,x,y,word,w=330,h=220,fill="#FFFFFF"):
    return g(id,f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="22" fill="{fill}" {ST} stroke-width="6"/>'+text(id+"-t",0,-h/2+60,word,48,INK),x,y)
def tv(id,x,y):
    return g(id,f'<g {ST}><rect x="-150" y="-110" width="300" height="200" rx="16" fill="#495057"/><rect x="-126" y="-88" width="252" height="156" rx="8" fill="#A5D8FF"/><line x1="-50" y1="90" x2="-80" y2="140"/><line x1="50" y1="90" x2="80" y2="140"/></g>',x,y)
def magazine(id,x,y):
    return g(id,f'<g {ST} stroke-width="6"><rect x="-90" y="-120" width="180" height="240" rx="6" fill="#FFC9C9"/><rect x="-60" y="-80" width="120" height="110" fill="#FFFFFF"/><line x1="-60" y1="60" x2="60" y2="60"/><line x1="-60" y1="88" x2="30" y2="88"/></g>',x,y)
def car(id,x,y=GROUND):
    s=f'<g {ST}><path d="M-300 -60 L-300 -150 Q-290 -170 -260 -170 L-170 -170 L-110 -250 L120 -250 L200 -170 L280 -160 Q310 -155 310 -120 L310 -60 Z" fill="{SKY}"/><path d="M-150 -175 L-100 -232 L0 -232 L0 -175 Z M20 -175 L20 -232 L110 -232 L170 -175 Z" fill="#E7F5FF" stroke-width="5"/><circle cx="-180" cy="-50" r="52" fill="#495057"/><circle cx="190" cy="-50" r="52" fill="#495057"/></g>'
    return g(id,s,x,y)
def signpost(id,x,y,left,right):
    s=f'<g {ST}><line x1="0" y1="0" x2="0" y2="-360" stroke-width="12"/><path d="M-20 -330 L-360 -330 L-400 -290 L-360 -250 L-20 -250 Z" fill="{GREEN}"/><path d="M20 -230 L360 -230 L400 -190 L360 -150 L20 -150 Z" fill="{RED}"/></g>'
    s+=text(id+"-l",-200,-274,left,40,"#FFFFFF")+text(id+"-r",200,-174,right,36,"#FFFFFF")
    return g(id,s,x,y)
def titlecard(id,l1,l2=None,y=470):
    s=text(id+"-a",960,y,l1,110,INK,stroke=PAPER,sw=4)
    if l2: s+=text(id+"-b",960,y+120,l2,64,AMBER,stroke=INK,sw=6)
    return g(id,s)
def subscribe(id,x,y):
    return g(id,f'<rect x="-230" y="-60" width="460" height="120" rx="20" fill="{RED}" {ST} stroke-width="6"/>'+text(id+"-t",0,22,"SUBSCRIBE",60,"#FFFFFF"),x,y)
def brain(id,x,y,s=1):
    return g(id,f'<path d="M-90 20 Q-120 -40 -70 -70 Q-60 -120 0 -110 Q60 -130 80 -80 Q130 -60 110 0 Q120 60 60 70 Q20 100 -20 80 Q-90 90 -90 20 Z" fill="#FFC9DE" {ST} stroke-width="6"/><path d="M-50 -60 Q-20 -40 -40 0 Q-20 30 10 20 M30 -80 Q20 -40 50 -20 Q80 0 60 40" fill="none" {ST} stroke-width="5"/>',x,y,s)
