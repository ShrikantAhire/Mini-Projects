import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 2
BARS = [0.85, 0.6, 0.92, 0.7, 0.45]


def draw(img, t):
    headline(img, "Step 1: the manager writes a brief", t, accent_words=("brief",))
    box = (MARGIN, 700, W - MARGIN, 1260)
    dy, p = card(img, box, t, 0.1, 0.5)
    x0, y0 = box[0] + 48, box[1] + dy + 44
    text(img, (x0, y0), "brief.md", mono(40, True), fill=ACCENT, alpha=p)
    line(img, [(box[0] + 48, y0 + 80), (box[2] - 48, y0 + 80)], fill=LINE, width=3, alpha=p)
    full = box[2] - box[0] - 96
    for i, frac in enumerate(BARS):
        by = y0 + 130 + i * 78
        rect(img, (x0, by, x0 + full, by + 28), fill=(40, 44, 53), radius=14, alpha=p)
        # typing fill: staggered, each row fills over 0.2 s, all done by 1.3 s
        q = prog(t, 0.5 + 0.17 * i, 0.3)
        w = int(full * frac * q)
        if w > 28:
            rect(img, (x0, by, x0 + w, by + 28), fill=MUTED, radius=14)
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
