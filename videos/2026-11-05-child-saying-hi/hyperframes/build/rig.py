# Stickman rig: SVG markup generators. Feet at (0,0), y up is negative.
INK="#1A1A1A"; PAPER="#FAF7F2"; AMBER="#F08C00"; RED="#E03131"; BLUE="#1C3D5A"; GREEN="#2F9E44"; SKY="#74C0FC"; BLUSH="#F4A7B9"
SW=7
BEHIND_MARK='<!--bm-->'

KID=dict(hip=(0,-112), sh=(0,-205), head=(0,-282), r=74)
ADULT_SX, ADULT_SY = 1.2, 1.55

ARMS={
 "stand":   ((-52,-140),(-58,-100),(52,-140),(58,-100)),
 "behind":  ((-46,-150),(-16,-128),(46,-150),(16,-128)),
 "clasp":   ((-56,-140),(-9,-162),(56,-140),(9,-162)),
 "wave":    ((-52,-140),(-58,-100),(80,-205),(96,-265)),
 "point":   ((-52,-140),(-58,-100),(95,-182),(152,-196)),
 "pointup": ((-52,-140),(-58,-100),(95,-215),(150,-250)),
 "pointL":  ((-95,-182),(-152,-196),(52,-140),(58,-100)),
 "crossed": ((-50,-142),(32,-160),(50,-142),(-32,-152)),
 "celebrate":((-80,-210),(-96,-272),(80,-210),(96,-272)),
 "handout": ((-52,-140),(-58,-100),(86,-162),(132,-172)),
 "reach":   ((-52,-140),(-58,-100),(92,-192),(152,-216)),
 "shrug":   ((-82,-160),(-98,-202),(82,-160),(98,-202)),
 "holdsign":((-62,-150),(-36,-186),(62,-150),(36,-186)),
 "highfive":((-52,-140),(-58,-100),(80,-215),(92,-278)),
 "highfiveL":((-80,-215),(-92,-278),(52,-140),(58,-100)),
 "think":   ((-52,-140),(-58,-100),(70,-162),(24,-214)),
 "lunch":   ((-56,-140),(-22,-132),(56,-140),(22,-132)),
 "hug":     ((-70,-170),(-118,-150),(70,-170),(118,-150)),
 "throw":   ((-52,-140),(-58,-100),(70,-225),(120,-250)),
 "catch":   ((-70,-180),(-30,-205),(70,-180),(30,-205)),
 "wipe":    ((-52,-140),(-58,-100),(90,-200),(140,-230)),
 "carry":   ((-60,-150),(-30,-160),(60,-150),(30,-160)),
}
LEGS={
 "stand": ((-14,-56),(-26,0),(14,-56),(26,0)),
 "knees": ((-3,-56),(-30,0),(3,-56),(30,0)),
 "walkA": ((-24,-58),(-46,0),(14,-54),(22,0)),
 "walkB": ((-14,-54),(-22,0),(24,-58),(46,0)),
 "run":   ((-34,-50),(-62,-14),(30,-62),(58,0)),
}

def _pt(p,adult):
    return (p[0]*ADULT_SX, p[1]*ADULT_SY) if adult else p

def _arm(o,e,h,adult,hand=True):
    e=_pt(e,adult); h=_pt(h,adult)
    s=f'<path d="M{o[0]:.1f} {o[1]:.1f} L{e[0]:.1f} {e[1]:.1f} L{h[0]:.1f} {h[1]:.1f}" fill="none"/>'
    if hand: s+=f'<circle cx="{h[0]:.1f}" cy="{h[1]:.1f}" r="11" fill="{PAPER}" stroke-width="5"/>'
    return s

def _legs(name,adult):
    hip=_pt(KID["hip"],adult)
    (kL,fL,kR,fR)=[_pt(p,adult) for p in LEGS[name]]
    s=f'<path d="M{hip[0]:.1f} {hip[1]:.1f} L{kL[0]:.1f} {kL[1]:.1f} L{fL[0]:.1f} {fL[1]:.1f}" fill="none"/>'
    s+=f'<path d="M{hip[0]:.1f} {hip[1]:.1f} L{kR[0]:.1f} {kR[1]:.1f} L{fR[0]:.1f} {fR[1]:.1f}" fill="none"/>'
    s+=f'<path d="M{fL[0]:.1f} {fL[1]:.1f} l-18 2 M{fR[0]:.1f} {fR[1]:.1f} l18 2" fill="none"/>'
    return s

BROWS={
 "neutral": "M-44 -40 L-12 -42 M12 -42 L44 -40",
 "raised":  "M-44 -50 Q-28 -58 -12 -52 M12 -52 Q28 -58 44 -50",
 "high":    "M-44 -58 Q-28 -68 -12 -60 M12 -60 Q28 -68 44 -58",
 "worried": "M-46 -36 L-12 -52 M12 -52 L46 -36",
 "think":   "M-44 -40 L-12 -42 M12 -54 Q28 -62 44 -54",
 "smug":    "M-44 -44 L-12 -38 M12 -38 L44 -44",
}
MOUTHS={
 "flat":  '<path d="M-14 38 L14 38" fill="none"/>',
 "small": '<path d="M-12 36 Q0 45 12 36" fill="none"/>',
 "smile": '<path d="M-22 30 Q0 52 22 30" fill="none"/>',
 "grin":  f'<path d="M-28 28 Q0 66 28 28 Z" fill="{INK}"/>',
 "wobble":'<path d="M-24 40 q6 -8 12 0 t12 0 t12 0 t12 0" fill="none"/>',
 "frown": '<path d="M-18 46 Q0 30 18 46" fill="none"/>',
 "O":     f'<ellipse cx="0" cy="42" rx="10" ry="13" fill="{INK}"/>',
 "smirk": '<path d="M-16 38 Q8 46 22 30" fill="none"/>',
}
EXPR={
 # brows, pupil r, pupil dy, mouth, extras, closed
 "neutral":("neutral",7,0,"small",[],False),
 "happy":("raised",7,0,"smile",[],False),
 "grin":("raised",7,0,"grin",[],False),
 "worried":("worried",5,0,"wobble",[],False),
 "panicked":("worried",4,0,"wobble",["sweat"],False),
 "embarrassed":("worried",6,2,"small",["blush"],False),
 "sad":("worried",6,6,"frown",[],False),
 "shocked":("high",4,0,"O",[],False),
 "thinking":("think",7,-6,"flat",[],False),
 "relieved":("neutral",7,0,"smile",["puff"],True),
 "confused":("think",6,0,"flat",["q"],False),
 "smug":("smug",7,0,"smirk",[],False),
 "mock":("smug",7,0,"grin",[],False),
}

def face(expr,look=(0,0),fid=""):
    b,pr,pdy,m,ex,closed=EXPR[expr]
    dx,dy=look
    s=f'<g id="{fid}">'
    if closed:
        s+='<path d="M-42 -4 Q-27 -16 -12 -4 M12 -4 Q27 -16 42 -4" fill="none" stroke-width="5"/>'
    else:
        s+=f'<g id="{fid}-eyes"><circle cx="-27" cy="-6" r="21" fill="#FFFFFF" stroke-width="5"/><circle cx="27" cy="-6" r="21" fill="#FFFFFF" stroke-width="5"/>'
        s+=f'<circle cx="{-27+dx:.1f}" cy="{-6+dy+pdy:.1f}" r="{pr}" fill="{INK}" stroke="none"/><circle cx="{27+dx:.1f}" cy="{-6+dy+pdy:.1f}" r="{pr}" fill="{INK}" stroke="none"/></g>'
    s+=f'<path d="{BROWS[b]}" fill="none" stroke-width="6"/>'
    s+=MOUTHS[m]
    if "sweat" in ex: s+=f'<path d="M78 -62 q-14 24 0 31 q14 -7 0 -31 Z" fill="{SKY}" stroke-width="4"/>'
    if "blush" in ex: s+=f'<ellipse cx="-44" cy="20" rx="14" ry="8" fill="{BLUSH}" stroke="none"/><ellipse cx="44" cy="20" rx="14" ry="8" fill="{BLUSH}" stroke="none"/>'
    if "q" in ex: s+=f'<text x="70" y="-70" font-size="64" font-weight="900" fill="{INK}" stroke="none" font-family="Nunito">?</text>'
    if "puff" in ex: s+=f'<path d="M30 46 q14 -4 22 4 M34 56 q14 0 20 8" fill="none" stroke-width="4"/>'
    s+='</g>'
    return s

def stick(cid,x,y,s=1.0,kind="kid",exprs=("neutral",),poses=("stand",),legs=("stand",),look=(0,0),cap=None,flip=False,opacity=1,extra="",gray=False):
    """kind: om, kid, adult, adult_om, mom, dad, teacher, researcher, baby"""
    adult = kind in ("adult","adult_om","mom","dad","teacher","researcher","counsellor","guest")
    ink = "#6B7280" if gray else INK
    sh=_pt(KID["sh"],adult); hip=_pt(KID["hip"],adult)
    hc=(0,sh[1]-18-(56 if adult else 74)) if adult else KID["head"]
    hr=56 if adult else 74
    fs=-1 if flip else 1
    out=f'<g transform="translate({x:.1f} {y:.1f}) scale({s*fs:.3f} {s:.3f})" opacity="{opacity}"><g id="{cid}" stroke="{ink}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round">'
    # legs (variants)
    for i,l in enumerate(legs):
        out+=f'<g id="{cid}-legs-{l}" opacity="{1 if i==0 else 0}">{_legs(l,adult)}</g>'
    out+=BEHIND_MARK
    # body/clothes
    if kind=="mom":
        out+=f'<path d="M{-36} {sh[1]} L{36} {sh[1]} L{80} {-95} L{-80} {-95} Z" fill="{BLUE}"/>'
    else:
        out+=f'<path d="M{hip[0]} {hip[1]} L{sh[0]} {sh[1]}" fill="none"/>'
    if kind=="om":
        out+=(f'<path d="M-38 -207 L38 -207 L62 -170 L46 -160 L40 -172 L42 -106 L-42 -106 L-40 -172 L-46 -160 L-62 -170 Z" fill="{"#9AA3AC" if gray else AMBER}"/>')
    if kind=="dad":
        out+=f'<path d="M-44 {sh[1]-2} L44 {sh[1]-2} L74 {sh[1]+48} L56 {sh[1]+60} L50 {sh[1]+44} L50 {hip[1]+4} L-50 {hip[1]+4} L-50 {sh[1]+44} L-56 {sh[1]+60} L-74 {sh[1]+48} Z" fill="{GREEN}"/>'
    if kind=="adult_om":
        out+=f'<path d="M0 {sh[1]+4} L-12 {sh[1]+24} L0 {sh[1]+110} L12 {sh[1]+24} Z" fill="{AMBER}" stroke-width="5"/>'
    if kind=="teacher":
        out+=f'<rect x="20" y="{sh[1]+50}" width="60" height="78" rx="6" fill="#FFFFFF" stroke-width="5"/><line x1="32" y1="{sh[1]+72}" x2="68" y2="{sh[1]+72}" stroke-width="4"/><line x1="32" y1="{sh[1]+90}" x2="68" y2="{sh[1]+90}" stroke-width="4"/>'
    if kind=="researcher":
        out+=f'<path d="M-40 {sh[1]} L40 {sh[1]} L52 {hip[1]+40} L-52 {hip[1]+40} Z" fill="#FFFFFF" stroke-width="5"/>'
    # arms
    ao = (-48,-165) if kind=="om" else ((0,sh[1]+12))
    for i,p in enumerate(poses):
        (eL,hL,eR,hR)=ARMS[p]
        oL = ao if kind!="om" else (-48,-165); oR = ao if kind!="om" else (48,-165)
        if kind!="om": oL=oR=(0,sh[1]+12)
        grp=f'<g id="{cid}-arms-{p}" opacity="{1 if i==0 else 0}">{_arm(oL,eL,hL,adult,hand=p!="behind")}{_arm(oR,eR,hR,adult,hand=p!="behind")}</g>'
        if p=="behind": out=out.replace(BEHIND_MARK,grp+BEHIND_MARK)
        else: out+=grp
    # neck + head
    out+=f'<g id="{cid}-head"><line x1="0" y1="{sh[1]}" x2="0" y2="{hc[1]+hr}"/>'
    out+=f'<circle cx="{hc[0]}" cy="{hc[1]}" r="{hr}" fill="{"#D7DCE0" if gray else PAPER}"/>'
    if kind=="om":
        out+=f'<path d="M-18 {hc[1]-hr+2} L-30 {hc[1]-hr-36} M0 {hc[1]-hr} L4 {hc[1]-hr-42} M18 {hc[1]-hr+2} L36 {hc[1]-hr-34}" fill="none"/>'
    if kind=="mom":
        out+=f'<circle cx="{-hr+4}" cy="{hc[1]-hr+16}" r="22" fill="{INK}"/>'
    if cap:
        out+=f'<path d="M{-hr} {hc[1]-8} A{hr} {hr} 0 0 1 {hr} {hc[1]-8} Z" fill="{cap}"/><path d="M{hr-10} {hc[1]-8} L{hr+34} {hc[1]-4}" fill="none" stroke-width="9"/>'
    sc=hr/74
    out+=f'<g transform="translate({hc[0]} {hc[1]}) scale({sc:.3f})">'
    for i,e in enumerate(exprs):
        out+=f'<g id="{cid}-f-{e}" opacity="{1 if i==0 else 0}">{face(e,look,fid=cid+"-face-"+e)}</g>'
    if kind=="dad":
        out+=f'<circle cx="-27" cy="-6" r="27" fill="none" stroke-width="5"/><circle cx="27" cy="-6" r="27" fill="none" stroke-width="5"/><line x1="-1" y1="-6" x2="1" y2="-6" stroke-width="5"/>'
    out+='</g></g>'
    out+=extra
    out+='</g></g>'
    return out

def baby(cid,x,y,s=1.0,expr="happy",look=(0,0)):
    out=f'<g transform="translate({x} {y}) scale({s})"><g id="{cid}" stroke="{INK}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round">'
    out+='<path d="M-60 -40 L40 -40" fill="none"/><path d="M-60 -40 L-80 0 M-40 -40 L-30 0 M20 -40 L10 0 M40 -40 L60 0" fill="none"/>'
    out+=f'<g id="{cid}-head"><circle cx="78" cy="-70" r="46" fill="{PAPER}"/><g transform="translate(78 -70) scale(0.62)">{face(expr,look,fid=cid+"-face")}</g></g>'
    out+='</g></g>'
    return out
