# Shared Episode 1 helpers: cast, meter HUD, scene registry.
import props as P
from rig import INK, AMBER, RED, PAPER, GREEN, BLUE
SC = {}
def scene(n):
    def deco(f): SC[n] = f; return f
    return deco

MASON_CAP = "#1C7ED6"; ETHAN_CAP = "#E03131"; NOAH_CAP = "#2F9E44"
WALK = ("stand", "walkA", "walkB")

def leo(s, x, y=860, sc=1.0, exprs=("neutral",), poses=("stand",), legs=("stand",), meter=None, name="leo", **kw):
    return s.char(name, x, y, sc, "leo", exprs, poses, legs, meter=meter, **kw)
def mason(s, x, y=860, sc=1.0, exprs=("happy",), poses=("stand",), legs=("stand",), name="mason", **kw):
    return s.char(name, x, y, sc * 1.16, "kid", exprs, poses, legs, cap=MASON_CAP, **kw)
def maya(s, x, y=860, sc=1.0, exprs=("neutral",), poses=("stand",), legs=("stand",), name="maya", **kw):
    return s.char(name, x, y, sc, "girl", exprs, poses, legs, hair="#8B5E3C", shirt="#F783AC", **kw)
def ava(s, x, y=860, sc=1.0, exprs=("happy",), poses=("stand",), legs=("stand",), name="ava", **kw):
    return s.char(name, x, y, sc, "girl", exprs, poses, legs, hair="#E8B04A", shirt="#B2F2BB", **kw)
def ethan(s, x, y=860, sc=1.0, exprs=("happy",), poses=("stand",), legs=("stand",), name="ethan", **kw):
    return s.char(name, x, y, sc * 1.08, "kid", exprs, poses, legs, cap=ETHAN_CAP, **kw)
def noah(s, x, y=860, sc=1.0, exprs=("happy",), poses=("stand",), legs=("stand",), name="noah", **kw):
    return s.char(name, x, y, sc * 1.04, "kid", exprs, poses, legs, cap=NOAH_CAP, **kw)
def kid(s, name, x, y=860, sc=1.0, exprs=("happy",), poses=("stand",), cap="#7048E8", girl=False, hair="#5C3D2E", shirt="#A5D8FF", **kw):
    if girl: return s.char(name, x, y, sc, "girl", exprs, poses, hair=hair, shirt=shirt, **kw)
    return s.char(name, x, y, sc, "kid", exprs, poses, cap=cap, **kw)
def carter(s, x, y=860, sc=1.0, exprs=("happy",), poses=("stand",), legs=("stand",), name="carter", **kw):
    return s.char(name, x, y, sc, "teacher", exprs, poses, legs, **kw)
def mom(s, x, y=860, sc=1.0, exprs=("happy",), poses=("stand",), name="mom", **kw):
    return s.char(name, x, y, sc, "mom", exprs, poses, **kw)
def dad(s, x, y=860, sc=1.0, exprs=("happy",), poses=("stand",), name="dad", **kw):
    return s.char(name, x, y, sc, "dad", exprs, poses, **kw)

def hud(s, v0, v1, at, x=1600, y=330, r=150, label="Leo's meter", dur=0.9, name="hud"):
    """Large feelings meter in screen space, needle moves v0 -> v1 at `at`."""
    s.add(P.gauge(s.id(name), x, y, r, s.id(name + "n"), label, v0, 38))
    s.pop(name, max(0.05, at - 0.5), 0.4)
    if v1 != v0:
        s.ft(name + "n", {"rotation": -90 + 180 * v0, "svgOrigin": "0 0"}, {"rotation": -90 + 180 * v1}, at, dur, "power3.out")

def thought(s, name, x, y, w, h, txt, size=50, tail=(0, 0), at=0.1):
    s.add(P.bubble(s.id(name), x, y, w, h, txt, size, tail=tail, thought=True))
    s.pop(name, at)

def say(s, name, x, y, w, h, txt, size=50, tail=(0, 0), at=0.1, fill="#FFFFFF"):
    s.add(P.bubble(s.id(name), x, y, w, h, txt, size, tail=tail, fill=fill))
    s.pop(name, at)

def sepia(s):
    s.add('<rect x="0" y="0" width="1920" height="1080" fill="#C9A66B" opacity="0.18"/>')
    s.add(P.text(s.id("fb"), 160, 110, "LAST YEAR", 46, "#7D6A4A", anchor="start"))
