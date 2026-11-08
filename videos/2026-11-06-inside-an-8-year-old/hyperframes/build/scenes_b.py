import props as P
from rig import INK, AMBER, RED, PAPER, GREEN
from epc import *


# ================= HOME
def dinner(s, leo_expr=("neutral",), meter=0.25):
    s.home()
    s.add(P.table(s.id("tb"), 960, 860, 640))
    s.add(P.cup(s.id("c1"), 860, 660)); s.add(P.cup(s.id("c2"), 1080, 660))
    mom(s, 480, 860, 1.0, ("happy",))
    leo(s, 1420, 860, 0.95, leo_expr, meter=meter, flip=True)

@scene(38)
def _(s):
    dinner(s)
    say(s, "b", 640, 250, 520, 130, "How was school?", 56, (560, 420), at=s.atw("How was"))

@scene(39)
def _(s):
    dinner(s, ("tight",))
    say(s, "b", 1320, 280, 260, 120, "Fine.", 60, (1400, 450), at=0.15)

def bath(s, leo_expr=("neutral",), mom_expr=("happy",)):
    s.bathroom()
    leo(s, 960, 770, 1.0, leo_expr, ("stand",), meter=None)
    s.add(P.bathtub(s.id("tub"), 960, 860))
    mom(s, 1560, 860, 1.05, mom_expr, flip=True)

@scene(40)
def _(s):
    bath(s, ("neutral", "worried"))
    t = s.atw("he asks")
    s.face("leo", "neutral", "worried", t - 0.3)
    say(s, "b", 640, 260, 500, 130, "Mom, am I short?", 54, (900, 470), at=t)

@scene(41)
def _(s):
    bath(s, ("worried",), ("grin",))
    s.add(P.heart(s.id("h"), 1560, 330, 0.9, RED)); s.pop("h", 0.1)
    say(s, "b", 1060, 200, 800, 130, "You're perfect, sweetheart.", 50, (1500, 380), at=s.atw("You're perfect"))

@scene(42)
def _(s):
    bath(s, ("eyeroll",), ("happy",))
    thought(s, "t", 560, 280, 560, 200, "Moms have to\nsay that.", 46, (880, 520), at=s.atw("Moms have"))

def bedtime(s, leo_expr=("sad",), meter=0.25):
    s.bedroom(True)
    s.add(P.bed(s.id("bed"), 960, 860))
    s.add(f'<g transform="translate(820 640) rotate(-90)">'); leo(s, 0, 0, 0.75, leo_expr, meter=meter); s.add('</g>')
    s.add(P.blanket(s.id("bl"), 960, 860))

@scene(43)
def _(s):
    bedtime(s, ("sad",))
    items = [("Shortest", "Shortest"), ("7 out of 10", "Seven out"), ("No cartwheel", "No cartwheel"), ("Horses that look like dogs", "Horses that")]
    for i, (txt, key) in enumerate(items):
        x, y = [(560, 200), (1080, 160), (640, 360), (1180, 330)][i]
        s.add(P.tag(s.id(f"i{i}"), x, y, txt, "#FFFFFF", RED if i == 0 else INK, 46))
        s.pop(f"i{i}", s.atw(key))
        s.ft(f"i{i}", {"y": 0}, {"y": -14, "repeat": 3, "yoyo": True}, s.atw(key) + 0.5, 1.0, "sine.inOut")

@scene(44)
def _(s):
    bedtime(s, ("thinking",))
    thought(s, "t", 900, 260, 520, 220, "Best at...?", 60, (760, 470), at=0.15)

@scene(45)
def _(s):
    bedtime(s, ("thinking", "happy"), 0.25)
    s.add(f'<g id="{s.id("mem")}"><ellipse cx="1060" cy="300" rx="520" ry="240" fill="#FFF4E0" stroke="{INK}" stroke-width="6"/>')
    mason(s, 1240, 420, 0.62, ("grin",), ("celebrate",), name="m2")
    leo(s, 880, 420, 0.6, ("grin",), ("shrug",), name="l2")
    s.add('</g>')
    s.pop("mem", s.atw("he remembers"))
    s.add(P.tag(s.id("best"), 1060, 490, "Best at making Mason laugh", AMBER, INK, 44))
    t = s.atw("Nobody makes")
    s.pop("best", t)
    s.face("leo", "thinking", "happy", s.atw("he remembers"))
    s.needle("leo", 0.25, 0.4, t, 0.9)
    s.ft("m2", {"rotation": -6, "svgOrigin": "0 0"}, {"rotation": 6, "repeat": 5, "yoyo": True}, s.atw("he remembers") + 0.4, 0.2, "sine.inOut")
    s.sfx("sparkle", t, 0.25)

@scene(46)
def _(s):
    bedtime(s, ("relieved",), 0.4)
    s.add(P.tag(s.id("best"), 1060, 300, "Best at making Mason laugh", AMBER, INK, 40))
    s.fadeout("best", s.atw("He falls"), 0.6)
    for i in range(3):
        s.add(P.text(s.id(f"z{i}"), 860 + i * 70, 470 - i * 60, "z", 50 + i * 14, "#DDF0FF"))
        s.ft(f"z{i}", {"opacity": 0, "y": 20}, {"opacity": 1, "y": 0}, s.atw("He falls") + i * 0.3, 0.5, "power2.out")

@scene(47)
def _(s):
    s.bg("#FFF8EE")
    panels = [("At bedtime", "at bedtime", 380), ("In the car", "in the car", 960), ("Not at dinner", "never at", 1540)]
    for i, (lab, key, x) in enumerate(panels):
        s.add(f'<g id="{s.id(f"p{i}")}"><rect x="{x-270}" y="200" width="540" height="420" rx="26" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>')
        if i == 0:
            s.add(f'<rect x="{x-270}" y="200" width="540" height="420" rx="26" fill="#2B3555"/>')
            s.add(P.g(s.id("bdw"), P.bed(s.id("bd"), 0, 0), x, 590, 0.45))
        elif i == 1:
            s.add(P.g(s.id("carw"), P.car(s.id("car"), 0, 0), x, 590, 0.8))
        else:
            s.add(P.g(s.id("tbw"), P.table(s.id("tb"), 0, 0, 340), x, 590, 1))
            s.add(P.xmark(s.id("x"), x, 380, 1.4))
        s.add(P.text(s.id(f"l{i}"), x, 690, lab, 48, INK))
        s.add('</g>')
        s.pop(f"p{i}", s.atw(key) - 0.2)
    s.add(P.text(s.id("sq"), 960, 130, "The question comes sideways", 60, INK))
    s.rise("sq", s.atw("The question"))
    t = s.atw("And the answer")
    s.fadeout("p0", t - 0.2); s.fadeout("p1", t - 0.2); s.fadeout("p2", t - 0.2); s.fadeout("sq", t - 0.2)
    mom(s, 600, 960, 0.85, ("happy",)); leo(s, 1300, 960, 0.8, ("tight",), meter=0.4, flip=True)
    s.set("mom", {"opacity": 0}, 0); s.set("leo", {"opacity": 0}, 0)
    s.fadein("mom", t); s.fadein("leo", t)
    s.add(P.bubble(s.id("yp"), 860, 430, 400, 110, "You're perfect!", 46, tail=(660, 560)))
    tb = s.atw("often doesn't")
    s.pop("yp", t + 0.6)
    s.ft("yp", {"x": 0, "y": 0, "rotation": 0}, {"x": 330, "y": -260, "rotation": 30, "opacity": 0}, tb, 0.8, "power2.in")
    s.add(P.tag(s.id("dl"), 1300, 300, "doesn't land", "#FFFFFF", RED, 44)); s.pop("dl", tb + 0.4)

@scene(48)
def _(s):
    s.bg("#FFF8EE")
    s.add(P.text(s.id("w"), 960, 470, "Why? Coming up.", 90, AMBER, stroke=INK, sw=7))
    s.pop("w", 0.1); s.sfx("whoosh-short", 0.1, 0.2)

# ================= WHAT SCIENCE SAYS
@scene(49)
def _(s):
    s.headroom()
    leo(s, 560, 960, 1.15, ("neutral",), meter=0.4)
    s.add(P.stamp(s.id("st"), 1250, 420, "NORMAL", GREEN, 110))
    s.pop("st", s.atw("completely normal"), 0.5); s.sfx("impact-bass-1", s.atw("completely normal"), 0.2)
    s.add(P.tag(s.id("dc"), 1250, 640, "studied for decades", "#FFFFFF", INK, 44)); s.pop("dc", s.atw("studied"))

@scene(50)
def _(s): s.research("Diane Ruble and colleagues, 1980", "How children judge their own work")

@scene(51)
def _(s):
    s.classroom()
    kid(s, "yk", 760, 860, 0.72, ("grin",), ("celebrate",), cap="#FFD43B")
    s.add(P.paper(s.id("p"), 1100, 520, "", INK, 0.55)); s.pop("p", 0.1)
    s.add(P.tag(s.id("age"), 380, 150, "Younger kids", "#FFFFFF", INK, 48)); s.pop("age", 0.1)
    say(s, "b", 1300, 280, 380, 130, "I did it!", 60, (880, 420), at=s.atw("I did it"))

@scene(52)
def _(s):
    s.classroom()
    s.add(P.tag(s.id("age"), 1560, 150, "From about 7 or 8", "#FFFFFF", INK, 48)); s.pop("age", s.atw("From around"))
    for i, (x, sc) in enumerate([(420, 0.8), (1500, 0.8)]):
        kid(s, f"o{i}", x, 860, sc, ("happy",), cap=["#7048E8", "#2F9E44"][i], girl=(i == 1), hair="#E8B04A")
        s.add(P.paper(s.id(f"pp{i}"), x + (110 if i == 0 else -110), 600, "", INK, 0.3))
    leo(s, 960, 860, 0.9, ("thinking",), meter=0.4, look=(-8, 0))
    t = s.atw("looking at the kids")
    s.add(P.arrow(s.id("a0"), 880, 470, 600, 540, RED, 8)); s.add(P.arrow(s.id("a1"), 1040, 470, 1320, 540, RED, 8))
    s.fadein("a0", t); s.fadein("a1", t + 0.4)

@scene(53)
def _(s):
    s.headroom()
    leo(s, 560, 960, 1.15, ("sad",), ("carry",), meter=0.3)
    s.add(P.tag(s.id("a"), 1250, 360, "Not worse at spelling", "#FFFFFF", INK, 50)); s.pop("a", 0.1)
    s.add(P.stamp(s.id("b"), 1250, 560, "COMPARING", RED, 80)); s.pop("b", s.atw("He started"))
    s.sfx("impact-bass-1", s.atw("He started"), 0.2)

@scene(54)
def _(s): s.research("Susan Harter", "How children see themselves")

@scene(55)
def _(s):
    s.yard()
    kid(s, "k5", 760, 860, 0.7, ("neutral", "grin"), ("stand", "celebrate"), cap="#FFD43B")
    s.add(P.tag(s.id("age"), 760, 220, "Age 5", "#FFFFFF", INK, 52)); s.pop("age", 0.1)
    say(s, "q", 1300, 300, 560, 130, "Fastest runner?", 56, (1300, 470), at=0.2)
    t = s.atw("big, confident")
    s.face("k5", "neutral", "grin", t - 0.3); s.pose("k5", "stand", "celebrate", t - 0.3)
    s.add(P.text(s.id("yes"), 1060, 420, "YES!", 120, AMBER, stroke=INK, sw=8)); s.pop("yes", t)
    s.sfx("pop", t, 0.25)

@scene(56)
def _(s):
    s.bg("#FFF8EE")
    areas = [("School", "school"), ("Sports", "sports"), ("Looks", "looks"), ("Friends", "friends")]
    for i, (w, key) in enumerate(areas):
        x = 330 + i * 420
        s.add(P.areabox(s.id(f"a{i}"), x, 330, w, 340, 240))
        s.pop(f"a{i}", s.atw(key))
    s.add(P.tag(s.id("re"), 960, 110, "A more realistic picture", "#FFFFFF", INK, 48)); s.pop("re", s.atw("more realistic"))
    marks = [0.3, 0.6, 0.45, 0.8]
    for i, m in enumerate(marks):
        x = 330 + i * 420
        s.add(f'<line x1="{x-130}" y1="400" x2="{x+130}" y2="400" stroke="#CED4DA" stroke-width="10" stroke-linecap="round"/>')
        s.add(P.g(s.id(f"m{i}"), f'<circle cx="0" cy="0" r="20" fill="{AMBER}" stroke="{INK}" stroke-width="5"/>', x - 130 + 260 * m, 400))
        s.pop(f"m{i}", s.atw(areas[i][1]) + 0.3)
    leo(s, 560, 960, 0.8, ("thinking", "sad"), meter=0.45)
    t = s.atw("self-esteem dips")
    hud(s, 0.6, 0.35, t + 0.3, 1400, 790, 150, "Self-esteem")
    s.face("leo", "thinking", "sad", t + 0.3); s.needle("leo", 0.45, 0.3, t + 0.3, 0.8)

@scene(57)
def _(s):
    s.headroom()
    s.add(P.listboard(s.id("lst"), 960, 450, ["Not the tallest", "Not the fastest", "Not the best at spelling", "Not the best at drawing"], 820, 50, "Leo's list"))
    s.pop("lst", 0.05, 0.35)

@scene(58)
def _(s):
    s.yard()
    s.add(f'<g stroke="{INK}" stroke-width="7" stroke-linejoin="round"><rect x="760" y="760" width="300" height="100" fill="#FFD8A8"/><rect x="1060" y="660" width="300" height="200" fill="#FFC078"/><rect x="1360" y="560" width="300" height="300" fill="{AMBER}"/></g>')
    leo(s, 560, 860, 0.85, ("neutral", "happy"), meter=0.3)
    s.add(P.tag(s.id("g"), 960, 150, "Not all bad news", "#FFFFFF", GREEN, 52)); s.pop("g", 0.1)
    t1 = s.atw("a real step forward")
    s.ft("leo", {"x": 0, "y": 0}, {"x": 360 / 0.85, "y": -100 / 0.85}, t1, 0.8, "power2.out")
    s.face("leo", "neutral", "happy", t1); s.needle("leo", 0.3, 0.45, t1, 0.7)
    t2 = s.atw("what they want")
    s.add(P.tag(s.id("b"), 1500, 420, "get better at", AMBER, INK, 44)); s.pop("b", t2)
    t3 = s.atw("nobody warns")
    s.add(P.warning(s.id("w"), 360, 360, "")); s.pop("w", t3)

@scene(59)
def _(s):
    s.bathroom()
    s.add(P.mirror(s.id("m"), 1300, 470, 340, 520))
    maya(s, 760, 860, 1.0, ("worried",), ("think",), look=(8, 0))
    s.add(P.tag(s.id("age"), 760, 170, "Earlier than you think", "#FFFFFF", RED, 46)); s.pop("age", s.atw("earlier"))

@scene(60)
def _(s): s.research("Hayley Dohnt & Marika Tiggemann, 2006", "Girls aged 5 to 8, Australia")

@scene(61)
def _(s):
    s.yard()
    for i, (x, hair, shirt) in enumerate([(560, "#8B5E3C", "#F783AC"), (960, "#E8B04A", "#B2F2BB"), (1360, "#5C3D2E", "#A5D8FF")]):
        kid(s, f"g{i}", x, 860, 0.72, ("worried",), girl=True, hair=hair, shirt=shirt)
    s.add(P.tag(s.id("age"), 960, 180, "By age 6", "#FFFFFF", INK, 56)); s.pop("age", s.atw("By age six"))
    s.add(P.tag(s.id("w"), 960, 300, "“I want a thinner body”", "#FFFFFF", RED, 44)); s.pop("w", s.atw("already wanted"))

@scene(62)
def _(s):
    s.yard()
    s.add(P.tv(s.id("tv"), 520, 340)); s.add(P.magazine(s.id("mg"), 860, 340))
    s.add(P.xmark(s.id("x1"), 520, 330, 1.6)); s.add(P.xmark(s.id("x2"), 860, 340, 1.6))
    s.pop("tv", 0.1); s.pop("mg", 0.2)
    t = s.atw("wasn't TV")
    s.pop("x1", t + 0.3); s.pop("x2", t + 0.5)
    t2 = s.atw("what they thought")
    for i, (x, hair, shirt) in enumerate([(1200, "#8B5E3C", "#F783AC"), (1450, "#E8B04A", "#B2F2BB"), (1700, "#5C3D2E", "#A5D8FF")]):
        kid(s, f"g{i}", x, 860, 0.62, ("worried",), girl=True, hair=hair, shirt=shirt, look=((-8, 0) if i else (8, 0)))
        s.add(P.bubble(s.id(f"b{i}"), x, 300, 170, 120, "?", 70, tail=(x + (60 if i < 2 else -60), 520), thought=True))
        s.pop(f"b{i}", t2 + i * 0.25)
    s.add(P.tag(s.id("o"), 1450, 120, "Other girls", "#FFFFFF", INK, 48)); s.pop("o", t2 + 0.8)

@scene(63)
def _(s):
    s.classroom()
    maya(s, 700, 860, 1.0, ("embarrassed",))
    say(s, "b", 1160, 280, 620, 150, "Rabbit teeth!", 80, (900, 430), at=s.atw("one joke"))
    s.add(P.tv(s.id("tv"), 1560, 650)); s.ft("tv", {"scale": 1, "transformOrigin": "50% 50%"}, {"scale": 0.5}, s.atw("than anything"), 0.6)

@scene(64)
def _(s): s.research("Erik Erikson, 1950", "Childhood and Society")

@scene(65)
def _(s):
    s.bg("#FFF8EE")
    s.add(P.text(s.id("q"), 960, 520, "?", 360, AMBER, stroke=INK, sw=10))
    s.add(P.tag(s.id("age"), 960, 140, "Ages 6 to 12", "#FFFFFF", INK, 52)); s.pop("age", s.atw("six and twelve"))
    s.pop("q", 0.1)
    t = s.atw("Am I capable")
    s.fadeout("q", t - 0.2)
    s.add(P.text(s.id("ac"), 960, 500, "Am I capable?", 120, AMBER, stroke=INK, sw=8)); s.pop("ac", t)
    s.sfx("impact-bass-1", t, 0.2)

def paths(s):
    s.yard()
    s.add(P.signpost(s.id("sp"), 960, 860, "Yes, I can", "Not good enough"))

@scene(66)
def _(s):
    paths(s)
    leo(s, 560, 860, 0.85, ("happy", "grin"), ("stand", "celebrate"), WALK, meter=0.45)
    s.walk("leo", 0.2, s.vd * 0.5, 0, -260)
    t = s.atw("build a feeling")
    s.face("leo", "happy", "grin", t); s.pose("leo", "stand", "celebrate", t); s.needle("leo", 0.45, 0.85, t, 0.8)
    s.sfx("sparkle", t, 0.2)

@scene(67)
def _(s):
    paths(s)
    kid(s, "k", 1360, 860, 0.85, ("neutral", "sad"), cap="#7048E8", legs=WALK)
    s.walk("k", 0.2, s.vd * 0.5, 0, 260)
    s.face("k", "neutral", "sad", s.atw("start to believe"))

@scene(68)
def _(s):
    s.headroom()
    leo(s, 960, 1150, 2.6, ("neutral",), meter=0.35, meter_r=46)
    s.push(0, s.d, 1.2, 960, 760)
    s.add(P.tag(s.id("t"), 960, 130, "Right now", AMBER, INK, 56)); s.pop("t", s.atw("right now"))

# ================= FOR PARENTS AND TEACHERS
def tipcard(s, n, txt):
    s.add(P.numcard(s.id("nc"), 960, 130, n, txt, 1100))
    s.ft("nc", {"y": -200}, {"y": 0}, 0.05, 0.5, "expo.out")

@scene(69)
def _(s):
    s.home()
    mom(s, 560, 860, 1.0, ("happy",)); dad(s, 1360, 860, 1.0, ("happy",), flip=True); leo(s, 960, 860, 0.85, ("neutral",), meter=0.35)
    s.add(P.tag(s.id("t"), 960, 130, "3 things to start tonight", AMBER, INK, 56)); s.pop("t", s.atw("Here are"))
    for i in range(3):
        s.add(f'<g transform="translate({760+i*200} 330)"><g id="{s.id(f"n{i}")}"><circle r="56" fill="#FFFFFF" stroke="{INK}" stroke-width="6"/>{P.text(s.id(f"nt{i}"),0,24,str(i+1),70,INK)}</g></g>')
        s.pop(f"n{i}", s.atw("three things") + i * 0.2)

@scene(70)
def _(s):
    s.home()
    tipcard(s, 1, "Compare with last month")
    leo(s, 420, 900, 1.0, ("neutral", "grin"), meter=0.35)
    s.add(P.paper(s.id("p1"), 860, 560, "5/10", INK, 0.8, "Last month"))
    s.add(P.paper(s.id("p2"), 1360, 560, "7/10", GREEN, 0.8, "This week"))
    s.pop("p1", s.atw("Last month")); s.pop("p2", s.atw("This week"))
    s.add(P.arrow(s.id("ar"), 1000, 760, 1220, 700, GREEN, 12)); s.fadein("ar", s.atw("This week") + 0.3)
    s.add(P.brain(s.id("br"), 1720, 650, 0.9)); s.pop("br", s.atw("brain growing"))
    t = s.atw("actually win")
    s.face("leo", "neutral", "grin", t - 0.5); s.needle("leo", 0.35, 0.8, t - 0.5, 1.0)
    s.sfx("sparkle", t - 0.5, 0.2)

@scene(71)
def _(s):
    s.home()
    tipcard(s, 2, "Be specific")
    mom(s, 420, 900, 1.0, ("happy",)); leo(s, 1300, 900, 1.0, ("tight", "grin"), meter=0.4, flip=True)
    t1 = s.atw("\"You're perfect\"")
    s.add(P.bubble(s.id("b1"), 800, 420, 420, 110, "You're perfect", 50, tail=(560, 560)))
    s.pop("b1", t1)
    s.ft("b1", {"x": 0, "y": 0, "rotation": 0}, {"x": 160, "y": -260, "rotation": -25, "opacity": 0}, t1 + 1.6, 0.7, "power2.in")
    s.add(P.tag(s.id("x"), 1280, 300, "slides right off", "#FFFFFF", RED, 40)); s.pop("x", t1 + 1.6)
    s.fadeout("x", s.atw("\"You kept") - 0.2)
    t2 = s.atw("\"You kept")
    s.add(P.bubble(s.id("b2"), 820, 420, 660, 110, "You kept practicing", 50, tail=(560, 560)))
    s.pop("b2", t2)
    t3 = s.atw("sticks")
    s.ft("b2", {"x": 0, "y": 0}, {"x": 330, "y": 40}, t3, 0.6, "power2.inOut")
    s.add(f'<circle id="{s.id("gl")}" cx="1300" cy="620" r="150" fill="{AMBER}" opacity="0"/>')
    s.ft("gl", {"opacity": 0}, {"opacity": 0.35}, t3 + 0.5, 0.5, "power2.out")
    s.face("leo", "tight", "grin", t3 + 0.5); s.needle("leo", 0.4, 0.8, t3 + 0.5, 0.9)
    s.sfx("chime", t3 + 0.5, 0.2)

@scene(72)
def _(s):
    s.classroom()
    tipcard(s, 3, "No body jokes")
    maya(s, 1400, 860, 1.0, ("embarrassed", "happy"))
    s.add(P.bubble(s.id("b"), 760, 380, 520, 120, "Rabbit teeth!", 60, tail=(1250, 500)))
    s.pop("b", 0.3)
    s.add(P.xmark(s.id("x"), 760, 380, 2.4)); s.pop("x", s.atw("no jokes") + 0.4)
    for i, w in enumerate(["height", "teeth", "weight", "hair"]):
        s.add(P.tag(s.id(f"w{i}"), 340 + i * 280, 640, w, "#FFFFFF", INK, 44)); s.pop(f"w{i}", s.atw(w, -0.1))
    t = s.atw("At this age")
    s.face("maya", "embarrassed", "happy", t)
    s.add(P.tag(s.id("l"), 760, 800, "A joke can last longer than the laugh", "#FFF4E0", INK, 38)); s.pop("l", t + 0.5)

@scene(73)
def _(s):
    s.photo_room()
    s.add(P.tag(s.id("t"), 960, 120, "For teachers", AMBER, INK, 56)); s.pop("t", 0.05)
    hs = [0.78, 0.84, 0.9, 0.96, 1.02, 1.08]
    caps = ["#E03131", "#1C7ED6", "#2F9E44", "#7048E8", "#0CA678", "#F08C00"]
    xs = [460 + i * 200 for i in range(6)]
    new = [3, 0, 5, 1, 4, 2]
    months = ["Jan", "Mar", "Apr", "Jul", "Sep", "Nov"]
    for i in range(6):
        kid(s, f"k{i}", xs[i], 860, hs[i] * 0.8, ("neutral",), cap=caps[i], girl=(i % 2 == 0), hair=["#8B5E3C", "#E8B04A", "#5C3D2E"][i % 3])
    s.add(P.tag(s.id("rk"), 960, 260, "Ranking", "#FFFFFF", RED, 52)); s.pop("rk", s.atw("into a ranking"))
    s.add(P.paper(s.id("p"), 1700, 520, "6/10", RED, 0.45)); s.pop("p", s.atw("reading scores"))
    t = s.atw("Lining up by birthday")
    s.fadeout("rk", t - 0.2); s.fadeout("p", t - 0.2)
    for i in range(6):
        sc = hs[i] * 0.8
        s.ft(f"k{i}", {"x": 0}, {"x": (xs[new[i]] - xs[i]) / sc}, t, 1.2, "power2.inOut")
        s.add(P.tag(s.id(f"mo{i}"), xs[new[i]], 920, months[new[i]], "#FFFFFF", INK, 34)); s.pop(f"mo{i}", t + 1.3 + i * 0.08)
    s.add(P.tag(s.id("bd"), 960, 260, "By birthday month", "#FFFFFF", GREEN, 52)); s.pop("bd", t + 1.2)

@scene(74)
def _(s):
    s.bg("#EEF4F8"); s.add(P.ground("#DCE8D2", "#B9CDAA"))
    s.add(P.tag(s.id("t"), 960, 110, "If you're eight and watching", AMBER, INK, 50)); s.pop("t", 0.05)
    leo(s, 960, 860, 0.9, ("sad", "happy"), meter=0.35)
    s.add(P.listboard(s.id("lst"), 960, 330, ["Not the tallest", "Not the fastest"], 560, 40, None)); s.pop("lst", 0.3)
    t = s.atw("doesn't mean")
    s.ft("lst", {"opacity": 1}, {"opacity": 0.2}, t + 0.6, 0.8, "power2.out")
    s.face("leo", "sad", "happy", t + 0.6); s.needle("leo", 0.35, 0.55, t + 0.6, 0.8)
    te = s.atw("Everyone has")
    for i, (x, girl) in enumerate([(420, True), (1500, False)]):
        kid(s, f"k{i}", x, 860, 0.8, ("neutral",), cap="#7048E8", girl=girl, hair="#E8B04A")
        s.add(P.listboard(s.id(f"l{i}"), x, 400, ["Not the best at...", "Not the..."], 400, 34, None))
        s.set(f"k{i}", {"opacity": 0}, 0); s.fadein(f"k{i}", te); s.pop(f"l{i}", te + 0.2)
    tg = s.atw("Even grown-ups")
    s.char("ad", 1760, 860, 0.85, "adult", ("neutral",)); s.set("ad", {"opacity": 0}, 0); s.fadein("ad", tg)

# ================= CLIFFHANGER
@scene(75)
def _(s):
    s.lunchroom()
    s.add(P.lunch_table(s.id("t1"), 1460, 860, 600))
    leo(s, 200, 860, 0.9, ("happy",), ("carry",), WALK, meter=0.45, extra=P.tray(s.id("tray"), 0, -150))
    s.walk("leo", 0.1, s.vd * 0.85, 0, 1000)
    s.add(P.tag(s.id("fr"), 300, 150, "FRIDAY", "#FFFFFF", INK, 52)); s.pop("fr", 0.05)

@scene(76)
def _(s):
    s.lunchroom()
    s.add(P.lunch_table(s.id("t1"), 1460, 860, 600))
    leo(s, 1100, 860, 0.9, ("happy", "shocked"), ("carry",), meter=0.45, extra=P.tray(s.id("tray"), 0, -150))
    s.face("leo", "happy", "shocked", 0.2)
    s.add(f'<rect id="{s.id("sp")}" x="1380" y="520" width="220" height="140" rx="16" fill="none" stroke="{RED}" stroke-width="8" stroke-dasharray="20 14"/>')
    s.fadein("sp", 0.2); s.sfx("whoosh-short", 0.2, 0.2)

@scene(77)
def _(s):
    s.lunchroom()
    for nm, x, f in (("ethan", 640, False), ("ava", 860, False), ("mason", 1080, True), ("noah", 1300, True)):
        {"ethan": ethan, "ava": ava, "mason": mason, "noah": noah}[nm](s, x, 860, 0.72, ("grin",), flip=f)
    s.add(P.lunch_table(s.id("t2"), 960, 860, 1000))
    t = s.atw("They're laughing")
    for nm in ("ethan", "ava", "mason", "noah"):
        s.ft(nm, {"rotation": -4, "svgOrigin": "0 0"}, {"rotation": 4, "repeat": 5, "yoyo": True}, t, 0.18, "sine.inOut")
    tc = s.atw("The Club")
    s.add(P.napkin(s.id("nap"), 960, 330)); s.pop("nap", tc, 0.5)
    s.sfx("impact-bass-1", tc, 0.25)
    s.cam(0, s.d, {"scale": 1.0, "transformOrigin": "960px 540px"}, {"scale": 1.08}, "none")

@scene(78)
def _(s):
    s.lunchroom()
    for nm, x, f in (("ethan", 640, False), ("ava", 860, False), ("mason", 1080, True), ("noah", 1300, True)):
        {"ethan": ethan, "ava": ava, "mason": mason, "noah": noah}[nm](s, x, 860, 0.72, ("happy",), flip=f)
    s.add(P.lunch_table(s.id("t2"), 960, 860, 1000))
    for i, x in enumerate([640, 860, 1080, 1300]):
        s.add(f'<g transform="translate({x} 360)"><g id="{s.id(f"c{i}")}"><circle r="44" fill="{RED}" stroke="{INK}" stroke-width="6"/>{P.text(s.id(f"ct{i}"),0,20,str(i+1),56,"#FFFFFF")}</g></g>')
        s.pop(f"c{i}", s.atw("four seats") + i * 0.25)
    s.add(P.tag(s.id("full"), 960, 170, "All taken", "#FFFFFF", RED, 56)); s.pop("full", s.atw("all four"))
    s.sfx("error", s.atw("all four"), 0.2)

@scene(79)
def _(s):
    s.lunchroom()
    mason(s, 1180, 860, 0.85, ("happy", "worried"), flip=True, look=(-8, 0))
    ethan(s, 1460, 860, 0.8, ("happy",), flip=True)
    leo(s, 480, 860, 0.95, ("shocked", "sad"), ("carry",), meter=0.45, look=(8, 0), extra=P.tray(s.id("tray"), 0, -150))
    s.add(P.lunch_table(s.id("t2"), 1280, 860, 700))
    t = s.atw("sees Leo")
    s.face("mason", "happy", "worried", t)
    s.add(f'<line id="{s.id("eye")}" x1="560" y1="560" x2="1100" y2="560" stroke="{AMBER}" stroke-width="6" stroke-dasharray="14 12"/>')
    s.fadein("eye", t + 0.2)
    tf = s.atw("For a second")
    s.face("leo", "shocked", "sad", tf)
    s.add('<rect id="%s" x="0" y="0" width="1920" height="1080" fill="#1A1A1A" opacity="0"/>' % s.id("dim"))
    s.ft("dim", {"opacity": 0}, {"opacity": 0.25}, tf, 0.6, "power2.out")
    s.push(tf, s.d - tf, 1.12, 820, 560)

@scene(80)
def _(s):
    s.lunchroom()
    leo(s, 620, 980, 1.5, ("sad",), ("carry",), meter=0.45, extra=P.tray(s.id("tray"), 0, -150))
    hud(s, 0.45, 0.04, s.at(0.3), 1400, 480, 230)
    s.needle("leo", 0.45, 0.04, s.at(0.3), 1.0)
    s.add(P.tag(s.id("lw"), 1400, 760, "Lowest all week", "#FFFFFF", RED, 48)); s.pop("lw", s.at(0.6))
    s.sfx("impact-bass-2", s.at(0.3), 0.3)

@scene(81)
def _(s):
    s.bg("#FFF8EE")
    s.add(P.text(s.id("nx"), 960, 200, "NEXT WEEK", 60, "#7D7263", weight=800))
    s.add(P.text(s.id("ep"), 960, 330, "Episode 2: The Club", 100, AMBER, stroke=INK, sw=8))
    s.add(P.napkin(s.id("nap"), 960, 620))
    s.rise("nx", 0.05); s.pop("ep", 0.2, 0.5); s.pop("nap", s.atw("What Leo does"))
    s.sfx("riser", 0.0, 0.2)

@scene(82)
def _(s):
    s.bg("#FFF8EE")
    leo(s, 620, 900, 1.1, ("grin",), ("wave",))
    s.add(P.subscribe(s.id("sub"), 1300, 520)); s.pop("sub", s.atw("subscribe"))
    s.add(P.text(s.id("t"), 1300, 340, "A Leo in your house?", 60, INK)); s.rise("t", 0.1)
    s.ft("sub", {"scale": 1, "transformOrigin": "50% 50%"}, {"scale": 1.08, "repeat": 3, "yoyo": True}, s.atw("subscribe") + 0.6, 0.35, "sine.inOut")
    s.sfx("click", s.atw("subscribe") + 0.3, 0.25)
