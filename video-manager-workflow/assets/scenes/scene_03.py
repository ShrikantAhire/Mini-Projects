import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 3
ROWS = [("project/", 0, ACCENT), ("brief.md", 1, INK), ("status/", 1, INK), ("assets/", 1, INK), ("clips/", 1, INK)]


def draw(img, t):
    headline(img, "Then it sets up a shared folder", t, accent_words=("shared", "folder"))
    box = (MARGIN, 700, W - MARGIN, 1200)
    dy, p = card(img, box, t, 0.0, 0.4)
    for i, (name, lvl, col) in enumerate(ROWS):
        q = prog(t, 0.3 + 0.17 * i, 0.3)
        x = box[0] + 56 + lvl * 64
        y = box[1] + 50 + i * 86 + int(16 * (1 - q))
        if lvl:
            line(img, [(box[0] + 74, y - 14), (box[0] + 74, y + 28), (x - 14, y + 28)], fill=LINE, width=3, alpha=q)
        text(img, (x, y), name, mono(44, lvl == 0), fill=col, alpha=q)
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
