import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 4
COLS = [("Worker 1", "scenes 1-4"), ("Worker 2", "scenes 5-8"), ("Worker 3", "scenes 9-12")]


def draw(img, t):
    headline(img, "12 scenes, split across 3 workers", t, accent_words=("12", "3"))
    gap = 24
    cw = (W - 2 * MARGIN - 2 * gap) // 3
    for i, (title, sub) in enumerate(COLS):
        x0 = MARGIN + i * (cw + gap)
        box = (x0, 800, x0 + cw, 1100)
        dy, p = card(img, box, t, 0.1 * i, 0.5)
        cx = x0 + cw // 2
        circle(img, (cx, 890 + dy), 28, fill=None, outline=ACCENT, width=4, alpha=p)
        text(img, (cx, 890 + dy), str(i + 1), font(32, "bold"), fill=ACCENT, alpha=p, anchor="mm")
        text(img, (cx, 975 + dy), title, font(36, "bold"), fill=INK, alpha=p, anchor="mm")
        text(img, (cx, 1035 + dy), sub, font(30, "medium"), fill=MUTED, alpha=p, anchor="mm")
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
