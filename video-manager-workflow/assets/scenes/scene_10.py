import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 10


def draw(img, t):
    headline(img, "Mistakes get caught after 2 scenes, not 12", t, accent_words=("2", "scenes,"))
    gap = 10
    n = 12
    tw = (W - 2 * MARGIN - gap * (n - 1)) // n
    top, th = 800, 190
    for i in range(n):
        x0 = MARGIN + i * (tw + gap)
        x1 = x0 + tw
        if i < 2:
            st = 0.1 + 0.15 * i
            dy, p = card(img, (x0, top, x1, top + th), t, st, 0.5, fill=CARD, outline=GREEN)
            cx, cy = (x0 + x1) // 2, top + th // 2 + dy
            line(img, [(cx - 15, cy), (cx - 4, cy + 13), (cx + 17, cy - 14)], fill=GREEN, width=7, alpha=p)
        else:
            st = 0.2 + 0.03 * i
            p = prog(t, st, 0.5)
            dy = int(40 * (1 - p))
            rect(img, (x0, top + dy, x1, top + th + dy), fill=CARD, outline=LINE, radius=28, alpha=0.45 * p)
        text(img, ((x0 + x1) // 2, top + th + 36 + int(40 * (1 - prog(t, 0.3, 0.5)))), str(i + 1),
             mono(30, True), fill=INK if i < 2 else MUTED, alpha=prog(t, 0.3, 0.5) * (1 if i < 2 else 0.5), anchor="mm")
    p = prog(t, 0.5, 0.5)
    text(img, (MARGIN, top + th + 130), "2 checked", font(44, "bold"), fill=GREEN, alpha=p)
    text(img, (MARGIN, top + th + 195), "10 not built yet, nothing to redo", font(36, "medium"), fill=MUTED, alpha=p)
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
