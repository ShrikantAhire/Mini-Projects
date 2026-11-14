import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 8
ITEMS = [("Format", 0.5), ("Look", 0.8), ("Words", 1.1)]


def draw(img, t):
    headline(img, "The manager checks the batch against the brief", t, size=88,
             accent_words=("checks",))
    cw = (W - 2 * MARGIN - 40) // 2
    for i, (name, sub) in enumerate((("Brief", "brief.md"), ("Batch", "scenes 5-6"))):
        x = MARGIN + i * (cw + 40)
        dy, p = card(img, (x, 700, x + cw, 880), t, start=0.1 + 0.1 * i,
                     outline=ACCENT if i == 0 else LINE)
        text(img, (x + cw // 2, 765 + dy), name, font(56, "bold"), alpha=p, anchor="mm")
        text(img, (x + cw // 2, 828 + dy), sub, mono(30), fill=MUTED, alpha=p, anchor="mm")
    dy, p = card(img, (MARGIN, 920, W - MARGIN, 1260), t, start=0.25)
    for i, (name, ts) in enumerate(ITEMS):
        y = 950 + i * 100 + dy
        x = MARGIN + 50
        a = prog(t, 0.35 + 0.1 * i, 0.4) * p
        circle(img, (x + 30, y + 30), 30, fill=None, outline=LINE, width=4, alpha=a)
        text(img, (x + 100, y + 30), name, font(52, "semibold"), alpha=a, anchor="lm")
        k = prog(t, ts, 0.3)
        if k > 0:
            circle(img, (x + 30, y + 30), 30, fill=GREEN, outline=None, alpha=k)
            line(img, [(x + 16, y + 31), (x + 26, y + 41), (x + 45, y + 20)], fill=BG, width=7, alpha=k)
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
