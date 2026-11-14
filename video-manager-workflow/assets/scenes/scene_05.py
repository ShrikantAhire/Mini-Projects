import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 5
TILE, GAP, BGAP = 190, 20, 68
X0 = (W - (4 * TILE + 2 * GAP + BGAP)) // 2
TOP = 780


def tile_x(i):
    return X0 + i * (TILE + GAP) + (BGAP - GAP if i >= 2 else 0)


def draw(img, t):
    headline(img, "Each worker builds in batches of 2", t, accent_words=("batches",))
    for i in range(4):
        s = 0.15 + 0.1 * i
        batch_a = i < 2
        col = ACCENT if batch_a else MUTED
        x = tile_x(i)
        dy, p = card(img, (x, TOP, x + TILE, TOP + 250), t, start=s, outline=col)
        text(img, (x + TILE // 2, TOP + 125 + dy), f"{i + 5:02d}", font(72, "bold"),
             fill=INK, alpha=p, anchor="mm")
        text(img, (x + TILE // 2, TOP + 200 + dy), "scene", mono(30), fill=MUTED, alpha=p, anchor="mm")
    for b, label in enumerate(("Batch A", "Batch B")):
        p = prog(t, 0.6 + 0.15 * b, 0.5)
        col = ACCENT if b == 0 else MUTED
        xa, xb = tile_x(2 * b), tile_x(2 * b + 1) + TILE
        y = TOP + 250 + 36
        line(img, [(xa, y - 20), (xa, y), (xb, y), (xb, y - 20)], fill=col, width=6, alpha=p)
        text(img, ((xa + xb) // 2, y + 28), label, font(44, "semibold"), fill=col if b == 0 else INK,
             alpha=p, anchor="ma")
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
