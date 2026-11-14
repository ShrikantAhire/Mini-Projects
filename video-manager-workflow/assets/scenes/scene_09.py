import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 9


def draw(img, t):
    headline(img, "Pass: next batch starts. Fail: redo it.", t, accent_words=("Pass", "Fail"))
    top, bot = 760, 1160
    gap = 40
    cw = (W - 2 * MARGIN - gap) // 2
    specs = [("Approved", "Next batch starts", GREEN, "check", 0.1),
             ("Redo", "Fix, then resubmit", ACCENT, "x", 0.25)]
    for i, (title, sub, col, kind, st) in enumerate(specs):
        x0 = MARGIN + i * (cw + gap)
        x1 = x0 + cw
        dy, p = card(img, (x0, top, x1, bot), t, st, 0.55, outline=col)
        cx, cy = (x0 + x1) // 2, top + 130 + dy
        circle(img, (cx, cy), 70, fill=None, outline=col, width=6, alpha=p)
        if kind == "check":
            line(img, [(cx - 30, cy + 2), (cx - 8, cy + 26), (cx + 32, cy - 24)], fill=col, width=12, alpha=p)
        else:
            line(img, [(cx - 28, cy - 28), (cx + 28, cy + 28)], fill=col, width=12, alpha=p)
            line(img, [(cx + 28, cy - 28), (cx - 28, cy + 28)], fill=col, width=12, alpha=p)
        text(img, (cx, top + 280 + dy), title, font(52, "bold"), fill=INK, alpha=p, anchor="mm")
        text(img, (cx, top + 340 + dy), sub, font(32, "medium"), fill=MUTED, alpha=p, anchor="mm")
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
