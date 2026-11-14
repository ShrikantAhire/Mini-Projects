import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 6
LINES = [
    [("{", INK)],
    [('  "worker": ', MUTED), ("2", INK), (",", MUTED)],
    [('  "scene": ', MUTED), ("6", INK), (",", MUTED)],
    [('  "state": ', MUTED), ('"done"', GREEN)],
    [("}", INK)],
]


def draw(img, t):
    headline(img, "After every scene, it logs its status", t, accent_words=("logs",))
    box = (MARGIN, 760, W - MARGIN, 1260)
    dy, p = card(img, box, t, start=0.1)
    f = mono(46, True)
    text(img, (MARGIN + 44, 760 + 40 + dy), "status/worker-2.json", mono(28), fill=MUTED, alpha=p)
    line(img, [(MARGIN + 44, 760 + 100 + dy), (W - MARGIN - 44, 760 + 100 + dy)], fill=LINE, width=2, alpha=p)
    for i, parts in enumerate(LINES):
        a = prog(t, 0.2 + 0.08 * i, 0.4)
        x = MARGIN + 44
        y = 760 + 135 + i * 62 + dy
        for s, c in parts:
            text(img, (x, y), s, f, fill=c, alpha=a * p)
            x += f.getlength(s)
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
