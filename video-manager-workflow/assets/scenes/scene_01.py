import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 1


def draw(img, t):
    headline(img, "This video was made by 4 AI agents", t, accent_words=("4", "AI"))
    mgr = (W // 2, 820)
    workers = [(240, 1140), (540, 1140), (840, 1140)]
    for i, w in enumerate(workers):
        p = prog(t, 0.25 + 0.1 * i, 0.4)
        line(img, [mgr, w], fill=LINE, width=5, alpha=p)
    p = prog(t, 0.0, 0.5)
    circle(img, (mgr[0], mgr[1] + int(30 * (1 - p))), 120, fill=CARD, outline=ACCENT, width=6, alpha=p)
    text(img, (mgr[0], mgr[1] + int(30 * (1 - p))), "Manager", font(38, "bold"), fill=INK, alpha=p, anchor="mm")
    for i, w in enumerate(workers):
        p = prog(t, 0.2 + 0.1 * i, 0.5)
        c = (w[0], w[1] + int(30 * (1 - p)))
        circle(img, c, 85, fill=CARD, outline=MUTED, width=4, alpha=p)
        text(img, c, f"Worker {i + 1}", font(30, "semibold"), fill=INK, alpha=p, anchor="mm")
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
