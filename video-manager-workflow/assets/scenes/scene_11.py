import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from style import *

SCENE = 11


def draw(img, t):
    headline(img, "The manager stitches the final cut", t, accent_words=("stitches",))
    n = 12
    bar_w = W - 2 * MARGIN
    ftw = bar_w // n            # final tile width (joined)
    stw, sgap = 56, (bar_w - 56 * n) / (n - 1)   # spread tile width and gap
    top, th = 860, 130
    joined = prog(t, 0.95, 0.15)
    for i in range(n):
        p = prog(t, 0.08 + 0.02 * i, 0.55)
        sx = MARGIN + i * (stw + sgap)
        fx = MARGIN + i * ftw
        sy = top + ((i % 3) - 1) * 110
        x = sx + (fx - sx) * p
        y = sy + (top - sy) * p
        w = stw + (ftw - stw) * p
        a = min(1.0, prog(t, 0.0 + 0.02 * i, 0.3))
        x0, y0 = int(x), int(y)
        out = ACCENT if p > 0.99 else LINE
        rect(img, (x0, y0, int(x + w), y0 + th), fill=CARD, outline=out, radius=14, width=3, alpha=a)
        text(img, (int(x + w / 2), y0 + th // 2), str(i + 1), mono(30, True), fill=INK, alpha=a, anchor="mm")
    p = prog(t, 1.0, 0.4)
    text(img, (MARGIN, top + th + 80), "final.mp4", mono(44, True), fill=INK, alpha=p)
    text(img, (W - MARGIN, top + th + 80), "0:30", mono(44, True), fill=ACCENT, alpha=p, anchor="ra")
    chrome(img, SCENE, t)


if __name__ == "__main__":
    render(SCENE, draw)
