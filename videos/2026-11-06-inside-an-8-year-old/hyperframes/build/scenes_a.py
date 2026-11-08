import props as P
from rig import INK, AMBER, RED, PAPER, GREEN
from epc import *

def flashback(s, label):
    s.add('<rect x="0" y="0" width="1920" height="1080" fill="#C9A66B" opacity="0.2"/>')
    s.add(P.tag(s.id("fbt"), 220, 110, label, "#FFF4E0", "#7D6A4A", 44))

# ================= COLD OPEN
@scene(1)
def _(s):
    s.home()
    s.add(P.tag(s.id("day"), 960, 150, "TUESDAY", "#FFFFFF", INK, 56))
    s.add(P.text(s.id("eight"), 1240, 560, "8", 300, AMBER, stroke=INK, sw=10))
    s.add(P.balloons(s.id("bl"), 400, 700))
    leo(s, 960, 860, 1.25, ("grin",), ("celebrate",))
    s.rise("leo", 0.05, 80); s.pop("day", 0.2); s.pop("eight", s.at(0.45)); s.sfx("pop", s.at(0.45), 0.25)

@scene(2)
def _(s):
    s.bathroom()
    s.add(P.mirror(s.id("mir"), 1500, 470, 360, 560))
    s.add('<g opacity="0.75">'); leo(s, 1500, 760, 0.62, ("happy",), name="refl", flip=True); s.add('</g>')
    s.set("refl", {"opacity": 0}, 0)
    leo(s, 300, 860, 1.05, ("happy",), ("stand",), WALK, look=(8, 0))
    s.walk("leo", s.at(0.15), s.vd * 0.45, 0, 870)
    s.fadein("refl", s.at(0.55), 0.3)
    s.add(P.bubble(s.id("q"), 900, 250, 380, 120, "Older?", 60, tail=(1080, 430), thought=True))
    s.pop("q", s.at(0.7))
    s.sfx("whoosh-short", s.at(0.15), 0.2)

@scene(3)
def _(s):
    s.bathroom()
    s.add(P.mirror(s.id("mir"), 960, 520, 720, 900))
    leo(s, 960, 1213, 2.6, ("neutral", "grin"))
    s.add(P.arrow(s.id("a1"), 1460, 160, 1110, 250, RED, 10))
    s.add(P.tag(s.id("t1"), 1560, 110, "same hair", "#FFFFFF", INK, 44))
    s.add(P.arrow(s.id("a2"), 1460, 820, 1030, 600, RED, 10))
    s.add(P.tag(s.id("t2"), 1560, 850, "same gap", "#FFFFFF", INK, 44))
    t1 = s.atw("same hair"); t2 = s.atw("same gap")
    s.pop("t1", t1); s.fadein("a1", t1 + 0.1)
    s.face("leo", "neutral", "grin", t2 - 0.2)
    s.pop("t2", t2); s.fadein("a2", t2 + 0.1)

@scene(4)
def _(s):
    s.bathroom()
    s.add(f'<circle id="{s.id("glow")}" cx="960" cy="500" r="260" fill="{AMBER}" opacity="0"/>')
    leo(s, 960, 980, 1.7, ("neutral", "thinking"), look=(0, -4))
    s.push(0, s.d, 1.18, 960, 500)
    t = s.atw("inside his head")
    s.ft("glow", {"opacity": 0, "scale": 0.6, "transformOrigin": "50% 50%"}, {"opacity": 0.35, "scale": 1}, t, 0.8, "power2.out")
    s.face("leo", "neutral", "thinking", s.atw("something had changed"))
    s.sfx("sparkle", t, 0.25)

@scene(5)
def _(s):
    s.bg("#FFF8EE")
    s.add(f'<circle id="{s.id("glow")}" cx="960" cy="330" r="180" fill="{AMBER}" opacity="0.3"/>')
    leo(s, 960, 660, 0.95, ("happy",))
    s.add(P.titlecard(s.id("ti"), "Inside an 8-Year-Old's Mind", None, 820))
    s.rise("ti", 0.15, 40); s.pop("leo", 0.05); s.sfx("riser", 0.0, 0.2)

@scene(6)
def _(s):
    s.school()
    days = ["MON", "TUE", "WED", "THU", "FRI"]
    for i, d in enumerate(days):
        s.add(P.tag(s.id(f"d{i}"), 420 + i * 270, 200, d, "#FFFFFF" if i not in (2, 3, 4) else "#FFF4E0", INK, 52))
        s.pop(f"d{i}", s.at(0.05) + i * 0.15, 0.35)
    s.add(P.tag(s.id("ep"), 960, 330, "3 episodes, 1 week", AMBER, INK, 46))
    s.pop("ep", s.at(0.02))
    leo(s, 240, 860, 1.0, ("happy",), ("stand",), WALK, look=(8, 0))
    s.walk("leo", s.at(0.2), s.vd * 0.6, 0, 1400)
    s.add(P.text(s.id("eye"), 1560, 420, "the way he sees it", 52, INK))
    s.fadein("eye", s.atw("we'll see it"))

@scene(7)
def _(s):
    s.home()
    s.add(f'<g id="{s.id("g1")}">'); mom(s, 560, 860, 1.0, ("happy",)); dad(s, 1360, 860, 1.0, ("happy",)); leo(s, 960, 860, 0.9, ("grin",), ("celebrate",)); s.add(P.tag(s.id("l1"), 960, 160, "Parents", "#FFFFFF", INK, 56)); s.add('</g>')
    s.add(f'<g id="{s.id("g2")}" opacity="0"><rect x="0" y="0" width="1920" height="1080" fill="#F3EFE6"/>{P.ground("#D9CBB4","#C2B096")}{P.blackboard(s.id("bb"),960,300)}')
    carter(s, 360, 860, 1.05, ("happy",), ("point",))
    for i, x in enumerate([760, 960, 1160, 1360, 1560]):
        kid(s, f"k{i}", x, 860, 0.62, ("happy",), cap=["#E03131", "#1C7ED6", "#2F9E44", "#7048E8", "#0CA678"][i], girl=(i % 2 == 1), hair=["#8B5E3C", "#E8B04A", "#5C3D2E"][i % 3])
    s.add(P.tag(s.id("l2"), 960, 110, "Teachers", "#FFFFFF", INK, 56)); s.add('</g>')
    s.add(f'<g id="{s.id("g3")}" opacity="0"><rect x="0" y="0" width="1920" height="1080" fill="#EEF1F5"/>{P.ground("#D3D9E1","#B4BDC9")}')
    s.char("adult", 960, 860, 1.3, "adult", ("happy",), ("stand",))
    s.add(f'<circle cx="960" cy="560" r="76" fill="{AMBER}" opacity="0.25"/>')
    leo(s, 960, 620, 0.32, ("happy",), name="mini")
    s.add(P.tag(s.id("l3"), 960, 160, "You, at eight", "#FFFFFF", INK, 56)); s.add('</g>')
    t2 = s.atw("If you teach"); t3 = s.atw("And if you were")
    s.fadeout("g1", t2 - 0.2, 0.3); s.fadein("g2", t2 - 0.2, 0.3)
    s.fadeout("g2", t3 - 0.2, 0.3); s.fadein("g3", t3 - 0.2, 0.3)
    s.pop("mini", t3 + 0.6)
    s.sfx("whoosh-short", t2 - 0.2, 0.18); s.sfx("whoosh-short", t3 - 0.2, 0.18)

@scene(8)
def _(s):
    s.bg("#FFF8EE")
    s.add(P.text(s.id("ep"), 960, 330, "EPISODE 1", 70, "#7D7263", weight=800))
    s.add(P.text(s.id("ti"), 960, 470, "Am I Good Enough?", 120, AMBER, stroke=INK, sw=8))
    leo(s, 960, 920, 0.75, ("worried",))
    s.rise("ep", 0.05); s.pop("ti", 0.2, 0.5); s.sfx("impact-bass-1", 0.2, 0.25)

# ================= THE FEELINGS METER
@scene(9)
def _(s):
    s.home()
    leo(s, 760, 980, 1.9, ("happy",), meter=0.5, meter_r=46)
    t = s.atw("a feelings meter")
    s.pop("#" + s.id("leo") + "-meter", t, 0.5)
    s.set("#" + s.id("leo") + "-meter", {"opacity": 0}, 0)
    s.add(P.arrow(s.id("ar"), 1180, 600, 870, 690, RED, 10))
    s.add(P.tag(s.id("lb"), 1330, 545, "Feelings meter", "#FFFFFF", INK, 52))
    tc = s.atw("right here")
    s.pop("lb", t + 0.3); s.fadein("ar", tc)
    s.sfx("pop", t, 0.25)

@scene(10)
def _(s):
    s.home()
    leo(s, 760, 980, 1.9, ("happy", "sad"), meter=0.5, meter_r=46)
    tu = s.atw("feels good"); td = s.atw("feels small")
    s.needle("leo", 0.5, 0.92, tu, 0.8)
    s.add(P.tag(s.id("up"), 1450, 400, "feels good", GREEN, "#FFFFFF", 52)); s.pop("up", tu)
    s.needle("leo", 0.92, 0.12, td, 0.8)
    s.face("leo", "happy", "sad", td)
    s.fadeout("up", td - 0.1)
    s.add(P.tag(s.id("dn"), 1450, 640, "feels small", RED, "#FFFFFF", 52)); s.pop("dn", td + 0.1)
    s.ft("leo", {"scale": 1}, {"scale": 0.92, "transformOrigin": "50% 100%"}, td, 0.6, "power2.out")

@scene(11)
def _(s):
    s.kitchen()
    s.add(P.table(s.id("tb"), 960, 860, 700))
    s.add(P.pancakes(s.id("pc"), 960, 640))
    s.add(P.bday_card(s.id("cd"), 1240, 560, "Love, Grandma"))
    mom(s, 360, 860, 1.0, ("happy",), ("celebrate",)); dad(s, 1600, 860, 1.0, ("happy",), ("celebrate",), flip=True)
    leo(s, 700, 860, 1.1, ("grin",), ("celebrate",), meter=0.6)
    s.pop("pc", 0.1); s.pop("cd", s.atw("a card"))
    s.add(P.text(s.id("n1"), 470, 330, "♪", 80, AMBER, stroke=INK, sw=4)); s.add(P.text(s.id("n2"), 1500, 330, "♪", 80, AMBER, stroke=INK, sw=4))
    s.rise("n1", 0.3); s.rise("n2", 0.5)
    s.ft("pc-flame", {"scaleY": 0.8, "transformOrigin": "50% 100%"}, {"scaleY": 1.15, "repeat": 9, "yoyo": True}, 0, 0.25, "sine.inOut")
    s.needle("leo", 0.6, 0.93, s.atw("nearly full"), 0.9)
    s.sfx("sparkle", s.atw("nearly full"), 0.25)

@scene(12)
def _(s):
    s.home()
    leo(s, 960, 1150, 2.6, ("grin",), meter=0.93, meter_r=46)
    s.push(0, s.vd * 0.5, 1.1, 960, 760)
    t = s.atw("move a lot")
    for k, v in enumerate([0.5, 0.85, 0.3, 0.75]):
        prev = [0.93, 0.5, 0.85, 0.3][k]
        s.needle("leo", prev, v, t + k * 0.28, 0.25, "power2.inOut")
    s.add(P.tag(s.id("k"), 960, 150, "Keep an eye on it", "#FFFFFF", INK, 56)); s.pop("k", 0.1)

# ================= PHOTO DAY
@scene(13)
def _(s):
    s.photo_room()
    s.add(P.camera(s.id("cam"), 1500, 860))
    s.add(P.tag(s.id("t"), 860, 380, "CLASS PHOTO DAY", AMBER, INK, 72))
    s.pop("t", 0.1); s.rise("cam", 0.05, 120); s.sfx("click", 0.6, 0.3)

HEIGHTS = [("ethan", 1.08), ("ava", 0.98), ("leo", 0.86), ("mason", 1.16), ("maya", 0.92), ("noah", 1.02)]
def lineup_cast(s, order_x, y=860, sc=0.9, exprs=None, meter=None):
    exprs = exprs or {}
    for nm, h in HEIGHTS:
        x = order_x[nm]
        e = exprs.get(nm, ("happy",))
        if nm == "leo": leo(s, x, y, sc * 0.94, e, meter=meter)
        elif nm == "mason": mason(s, x, y, sc, e)
        elif nm == "maya": maya(s, x, y, sc * 0.98, e)
        elif nm == "ava": ava(s, x, y, sc * 1.02, e)
        elif nm == "ethan": ethan(s, x, y, sc, e)
        else: noah(s, x, y, sc, e)

@scene(14)
def _(s):
    s.photo_room()
    start = {"ethan": 560, "ava": 760, "leo": 960, "mason": 1160, "maya": 1360, "noah": 1560}
    end = {"leo": 560, "maya": 760, "ava": 960, "noah": 1160, "ethan": 1360, "mason": 1560}
    lineup_cast(s, start, sc=0.85)
    carter(s, 200, 860, 1.05, ("happy",), ("pointL",), flip=True)
    t = s.atw("lines everyone")
    for nm in start:
        dx = (end[nm] - start[nm])
        scale = {"leo": 0.85 * 0.94, "mason": 0.85 * 1.16, "maya": 0.85 * 0.98, "ava": 0.85 * 1.02, "ethan": 0.85 * 1.08, "noah": 0.85 * 1.04}[nm]
        s.ft(nm, {"x": 0}, {"x": dx / scale}, t + 0.2, 1.2, "power2.inOut")
    s.add(P.arrow(s.id("ar"), 520, 260, 1600, 180, INK, 8))
    s.add(P.text(s.id("sh"), 560, 330, "shortest", 44, RED)); s.add(P.text(s.id("tl"), 1560, 250, "tallest", 44, INK))
    s.fadein("ar", t + 1.4); s.fadein("sh", t + 1.5); s.fadein("tl", t + 1.5)

def photo_rows(s, leo_expr=("happy",), meter=0.85, maya_expr=("tight",)):
    s.photo_room()
    for i, x in enumerate([700, 900, 1100, 1300]):
        kid(s, f"b{i}", x, 700, 0.85, ("happy",), cap=["#7048E8", "#0CA678", "#E8590C", "#1C7ED6"][i], girl=(i == 1))
    mason(s, 1500, 700, 0.85, ("happy",))
    leo(s, 560, 900, 0.82, leo_expr, meter=meter)
    for i, x in enumerate([760, 960, 1160, 1360]):
        if i == 1: maya(s, x, 900, 0.86, maya_expr)
        else: kid(s, f"f{i}", x, 900, 0.88, ("happy",), cap=["#E03131", "#2F9E44", "#F08C00", "#7048E8"][i], girl=(i == 3), hair="#E8B04A")

@scene(15)
def _(s):
    photo_rows(s, ("happy", "embarrassed"), 0.85, ("neutral",))
    s.push(0, s.d, 1.35, 600, 650)
    t = s.atw("very end")
    s.add(P.arrow(s.id("ar"), 440, 400, 530, 520, RED, 10)); s.fadein("ar", t)
    s.add(P.tag(s.id("e"), 440, 350, "end of the row", "#FFFFFF", RED, 40)); s.pop("e", t)
    s.face("leo", "happy", "embarrassed", s.atw("knows exactly"))
    s.needle("leo", 0.85, 0.72, s.atw("knows exactly"), 0.8)

@scene(16)
def _(s):
    photo_rows(s, ("neutral",), 0.72, ("neutral",))
    s.cam(0, s.vd * 0.4, {"scale": 1.4, "transformOrigin": "1500px 450px"}, {"scale": 1.4}, "none")
    s.add(P.tag(s.id("m"), 1500, 210, "Mason", "#FFFFFF", INK, 48)); s.pop("m", s.atw("is Mason"))
    s.add(P.arrow(s.id("up"), 1700, 700, 1700, 330, GREEN, 12)); s.fadein("up", s.atw("grew over"))
    s.add(P.tag(s.id("ld"), 560, 430, "Leo didn't", "#FFFFFF", RED, 44))
    t = s.atw("Leo didn't")
    s.cam(t - 0.3, 0.7, {"scale": 1.4, "transformOrigin": "1500px 450px"}, {"scale": 1.0}, "power2.inOut")
    s.pop("ld", t + 0.3)

@scene(17)
def _(s):
    s.photo_room()
    s.add(P.camera(s.id("cam"), 1250, 860))
    s.char("ph", 1500, 860, 1.05, "adult", ("grin",), ("wave",), cap="#495057", flip=True)
    say(s, "b", 900, 260, 620, 130, "Big smiles, everybody!", 54, (1450, 470), at=0.25)

@scene(18)
def _(s):
    photo_rows(s, ("happy",), 0.72, ("tight",))
    s.push(0, s.vd * 0.3, 1.2, 560, 700)
    b = [("Shortest.", "Shortest"), ("End of the row.", "End of the row"), ("Front, where everyone can see.", "Front, where")]
    s.add(P.bubble(s.id("tb"), 900, 330, 780, 300, "", 40, tail=(640, 500), thought=True))
    s.pop("tb", s.atw("a small voice"))
    for i, (txt, key) in enumerate(b):
        s.add(P.text(s.id(f"w{i}"), 900, 270 + i * 62, txt, 40 if i < 2 else 36, RED if i == 0 else INK))
        s.pop(f"w{i}", s.atw(key))
    s.needle("leo", 0.72, 0.6, s.atw("Shortest"), 0.6)

@scene(19)
def _(s):
    photo_rows(s, ("happy",), 0.6, ("tight",))
    s.push(0, s.vd * 0.6, 1.5, 900, 640)
    s.add(P.arrow(s.id("ar"), 1160, 330, 990, 470, RED, 10)); s.fadein("ar", s.atw("Maya"))
    s.add(P.tag(s.id("m"), 1200, 290, "Maya", "#FFFFFF", INK, 44)); s.pop("m", s.atw("Maya"))

@scene(20)
def _(s):
    s.photo_room()
    maya(s, 960, 1250, 2.4, ("tight", "worried"))
    s.add(P.arrow(s.id("a1"), 1280, 600, 1060, 650, RED, 9)); s.add(P.arrow(s.id("a2"), 640, 600, 860, 650, RED, 9))
    s.fadein("a1", s.atw("tight") - 0.2); s.fadein("a2", s.atw("tight") - 0.2)

@scene(21)
def _(s):
    s.classroom(); flashback(s, "LAST WEEK")
    maya(s, 760, 860, 0.95, ("happy", "embarrassed"))
    kid(s, "boy", 1200, 860, 1.0, ("mock",), ("pointL",), cap="#E8590C")
    for i, x in enumerate([1450, 1620, 1780]):
        kid(s, f"k{i}", x, 860, 0.75, ("neutral", "mock"), cap=["#7048E8", "#2F9E44", "#1C7ED6"][i], flip=True)
    say(s, "b", 1220, 300, 560, 120, "Rabbit teeth!", 60, (1180, 470), at=s.atw("said her"))
    tl = s.atw("Everyone laughed")
    s.face("maya", "happy", "embarrassed", s.atw("said her") + 0.3)
    for i in range(3): s.face(f"k{i}", "neutral", "mock", tl + i * 0.08)
    s.sfx("glitch-1", tl, 0.12)
    s.add(P.stopwatch(s.id("sw"), 1580, 260)); s.pop("sw", s.atw("over in two"))
    s.fadeout("b", s.atw("For them"))

@scene(22)
def _(s):
    s.bathroom()
    for i, (x, sc) in enumerate([(500, 0.8), (960, 1.0), (1420, 0.8)]):
        s.add(P.mirror(s.id(f"m{i}"), x, 480, 300 * sc, 460 * sc))
        s.pop(f"m{i}", s.at(0.05) + i * 0.3)
    maya(s, 960, 980, 1.05, ("worried",), ("think",))
    s.add(P.tag(s.id("t"), 960, 150, "Not over for Maya", "#FFFFFF", RED, 48)); s.pop("t", 0.1)

@scene(23)
def _(s):
    s.photo_room()
    s.add(P.camera(s.id("cam"), 1250, 860))
    s.char("ph", 1500, 860, 1.05, "adult", ("grin",), ("point",), cap="#495057", flip=True)
    maya(s, 400, 860, 0.95, ("tight",))
    say(s, "b", 860, 250, 900, 130, "Come on, show me those teeth!", 48, (1450, 470), at=0.15)

@scene(24)
def _(s):
    s.photo_room()
    maya(s, 960, 1250, 2.0, ("tight",))
    s.shakehead("#" + s.id("maya"), 0.2, 3)

@scene(25)
def _(s):
    photo_rows(s, ("happy",), 0.55, ("tight",))
    s.add(P.flash(s.id("fl")))
    s.ft("fl", {"opacity": 0.95}, {"opacity": 0}, 0.05, 0.5, "power2.out")
    s.sfx("click", 0.05, 0.45)

# ================= THE TEST
def flatpaper(s, name, x):
    s.add(P.g(s.id(name), f'<rect x="-60" y="-12" width="120" height="16" rx="3" fill="#FFFFFF" stroke="{INK}" stroke-width="4"/>', x, 704))

def class_desks(s, papers=True, leo_expr=("neutral",), meter=0.55, look=(0, 0)):
    s.classroom()
    s.add(P.desk(s.id("d1"), 560, 860)); s.add(P.desk(s.id("d2"), 960, 860)); s.add(P.desk(s.id("d3"), 1360, 860))
    mason(s, 560, 860, 0.8, ("happy",))
    leo(s, 960, 860, 0.84, leo_expr, meter=meter, look=look)
    kid(s, "girl", 1360, 860, 0.84, ("happy",), girl=True, hair="#5C3D2E", shirt="#FFD8A8")

@scene(26)
def _(s):
    class_desks(s, meter=0.55)
    carter(s, 160, 860, 1.05, ("happy",), ("handout",), WALK)
    s.walk("carter", 0.1, s.vd * 0.8, 0, 1100)
    for i, x in enumerate([560, 960, 1360]):
        flatpaper(s, f"p{i}", x)
        s.ft(f"p{i}", {"y": -500, "opacity": 0, "rotation": -30}, {"y": 0, "opacity": 1, "rotation": 0}, s.at(0.3) + i * 0.3, 0.5, "power2.out")
    s.sfx("whoosh-short", s.at(0.3), 0.2)

@scene(27)
def _(s):
    s.classroom()
    leo(s, 560, 980, 1.5, ("neutral",), ("carry",), meter=0.55)
    s.add(P.paper(s.id("p"), 1250, 540, "7/10", INK, 1.2))
    s.pop("p", 0.05); s.sfx("pop", 0.1, 0.2)

@scene(28)
def _(s):
    s.classroom(); flashback(s, "LAST YEAR")
    leo(s, 620, 860, 0.85, ("happy", "grin"), ("carry", "celebrate"))
    s.add(P.paper(s.id("p"), 1000, 560, "7/10", INK, 0.6))
    t = s.atw("Seven! Nice")
    say(s, "b", 1300, 280, 460, 130, "Seven! Nice.", 60, (760, 450), at=t)
    s.face("leo", "happy", "grin", t); s.pose("leo", "carry", "celebrate", t)
    s.sfx("chime", t, 0.25)

@scene(29)
def _(s):
    class_desks(s, leo_expr=("neutral", "thinking"), meter=0.55, look=(0, 0))
    for i, x in enumerate([560, 960, 1360]):
        flatpaper(s, f"p{i}", x)
    s.add(P.tag(s.id("ty"), 960, 140, "THIS YEAR", "#FFFFFF", INK, 48)); s.pop("ty", 0.1)
    t = s.atw("he looks at Mason")
    s.face("leo", "neutral", "thinking", s.atw("Before he even"))
    s.fadeout("ty", t - 0.4)
    s.cam(t - 0.3, 0.9, {"x": 0, "scale": 1, "transformOrigin": "960px 600px"}, {"x": 200, "scale": 1.3}, "power2.inOut")
    s.add(P.arrow(s.id("ar"), 900, 420, 640, 520, RED, 9)); s.fadein("ar", t)

@scene(30)
def _(s):
    s.classroom()
    mason(s, 560, 980, 1.3, ("grin",), ("celebrate",))
    s.add(P.paper(s.id("p"), 1250, 540, "10/10", GREEN, 1.2))
    s.pop("p", 0.05); s.sfx("sparkle", 0.1, 0.25)

@scene(31)
def _(s):
    s.classroom()
    kid(s, "girl", 560, 980, 1.3, ("happy",), ("celebrate",), girl=True, hair="#5C3D2E", shirt="#FFD8A8")
    s.add(P.paper(s.id("p"), 1250, 540, "9/10", GREEN, 1.2))
    s.pop("p", s.atw("Nine") - 0.15); s.sfx("pop", s.atw("Nine"), 0.2)

@scene(32)
def _(s):
    s.classroom()
    leo(s, 560, 980, 1.5, ("neutral", "sad"), ("carry",), meter=0.55)
    s.add(P.paper(s.id("p"), 1250, 540, "", INK, 1.2))
    s.add(P.text(s.id("sv"), 1346, 400, "7", 120, INK))
    t = s.atw("feels smaller")
    s.ft("sv", {"scale": 1, "transformOrigin": "50% 50%"}, {"scale": 0.35}, t, 0.9, "power2.inOut")
    s.face("leo", "neutral", "sad", s.atw("looks different"))
    s.sfx("whoosh-short", t, 0.18)

@scene(33)
def _(s):
    s.classroom()
    leo(s, 620, 980, 1.5, ("sad",), meter=0.55)
    hud(s, 0.55, 0.42, s.at(0.3), 1400, 480, 220)
    s.needle("leo", 0.55, 0.42, s.at(0.3), 0.9)
    s.sfx("impact-bass-2", s.at(0.3), 0.2)

@scene(34)
def _(s):
    s.yard()
    ethan(s, 300, 860, 0.95, ("grin",), ("celebrate",))
    for i, x in enumerate([1080, 1230, 1380]):
        kid(s, f"c{i}", x, 860, 0.75, ("happy", "grin"), ("stand", "celebrate"), cap=["#7048E8", "#0CA678", "#1C7ED6"][i], girl=(i == 1), flip=True)
    leo(s, 1590, 860, 0.85, ("neutral", "sad"), meter=0.42, flip=True)
    s.ft("ethan", {"x": 0, "rotation": 0, "svgOrigin": "0 -200"}, {"x": 490, "rotation": 360}, s.at(0.05), 1.3, "power1.inOut")
    tc = s.atw("everybody claps")
    for i in range(3):
        s.pose(f"c{i}", "stand", "celebrate", tc + i * 0.1); s.face(f"c{i}", "happy", "grin", tc + i * 0.1)
    s.sfx("sparkle", tc, 0.2)
    t = s.atw("Leo can't")
    s.face("leo", "neutral", "sad", t); s.needle("leo", 0.42, 0.36, t, 0.7)

@scene(35)
def _(s):
    s.classroom()
    ava(s, 420, 860, 1.0, ("grin",), ("carry",))
    s.add(P.drawing(s.id("good"), 740, 500, True))
    leo(s, 1500, 860, 1.0, ("neutral", "embarrassed"), ("carry",), meter=0.36, flip=True)
    s.add(P.drawing(s.id("bad"), 1180, 500, False))
    s.pop("good", 0.1)
    t = s.atw("Leo's horses")
    s.pop("bad", t)
    s.add(P.text(s.id("wf"), 1600, 300, "woof?", 50, "#7D7263")); s.fadein("wf", s.atw("like dogs"))
    s.face("leo", "neutral", "embarrassed", t + 0.3); s.needle("leo", 0.36, 0.32, t + 0.3, 0.6)

@scene(36)
def _(s):
    s.headroom()
    leo(s, 400, 960, 1.15, ("sad",), meter=0.32)
    items = ["Not the tallest", "Not the fastest", "Not the best at spelling", "Not the best at drawing"]
    keys = ["not the tallest", "not the fastest", "best at spelling", "best at drawing"]
    s.add(P.listboard(s.id("lst"), 1180, 470, items, 820, 50, "Leo's list"))
    s.pop("lst", s.atw("made a list"))
    for i, k in enumerate(keys):
        t = s.atw(k) - (0.4 if i >= 2 else 0)
        s.set(f"#{s.id('lst')}-r{i}", {"opacity": 0}, 0); s.fadein(f"#{s.id('lst')}-r{i}", t, 0.25)
        s.set(f"#{s.id('lst')}-x{i}", {"opacity": 0}, 0); s.fadein(f"#{s.id('lst')}-x{i}", t + 0.5, 0.15)
        s.sfx("click-soft", t + 0.5, 0.2)
    s.needle("leo", 0.32, 0.25, s.atw("best at drawing"), 0.7)

@scene(37)
def _(s):
    s.yard()
    leo(s, 700, 860, 1.0, ("sad",), meter=0.25)
    s.add(P.listboard(s.id("lst"), 760, 250, ["Not the tallest", "Not the fastest", "Not the best at spelling", "Not the best at drawing"], 720, 38, None))
    s.add(P.text(s.id("q"), 1420, 330, "Nobody knows", 56, "#7D7263"))
    s.fadein("q", s.atw("Nobody even"))
    for i, x0 in enumerate([-200, -350]):
        kid(s, f"w{i}", 200 + i * 160, 860, 0.7, ("happy",), ("stand",), legs=("stand", "walkA", "walkB"), cap=["#7048E8", "#2F9E44"][i])
        s.walk(f"w{i}", s.atw("Nobody even") - 0.5, 2.5, 0, 1700)
