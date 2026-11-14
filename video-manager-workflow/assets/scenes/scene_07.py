import math
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 7


def draw(img, t):
    headline(img, "After each batch, it stops and waits", t, accent_words=("stops",))
    cx, cy, r = W // 2, 930, 170
    p = prog(t, 0.1, 0.6)
    # slow subtle pulse on the outline ring
    pulse = 0.5 + 0.5 * math.sin(t * 2 * math.pi / 2.5)
    circle(img, (cx, cy), r + 18 + int(10 * pulse), fill=None, outline=ACCENT, width=3,
           alpha=p * (0.15 + 0.2 * (1 - pulse)))
    circle(img, (cx, cy), r, fill=CARD, outline=ACCENT, width=6, alpha=p)
    bw, bh = 38, 130
    for dx in (-35, 35):
        x = cx + dx
        rect(img, (x - bw // 2, cy - bh // 2, x + bw // 2, cy + bh // 2), fill=INK, radius=8, alpha=p)
    text(img, (cx, cy + r + 40), "Worker 2", font(40, "semibold"), fill=MUTED, alpha=prog(t, 0.3, 0.5), anchor="ma")
    text(img, (cx, cy + r + 110), "Waiting for review", font(56, "bold"), fill=INK,
         alpha=prog(t, 0.4, 0.5), anchor="ma")
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
