import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 12


def draw(img, t):
    y = headline(img, "Try this setup in Claude Code", t, accent_words=("Claude", "Code"))
    uw = prog(t, 0.3, 0.6)
    uy = y + 24
    rect(img, (MARGIN, uy, MARGIN + int(420 * uw) + 1, uy + 10), fill=ACCENT, radius=5)
    p = prog(t, 0.6, 0.5)
    text(img, (MARGIN, uy + 90 + int(30 * (1 - p))), "Follow for practical Claude workflows",
         font(40, "medium"), fill=MUTED, alpha=p)
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
