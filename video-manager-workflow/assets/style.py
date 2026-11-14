"""Shared render toolkit for every scene. Workers: import this, do not edit it.

Usage in assets/scenes/scene_NN.py:

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from style import *

    def draw(img, t):
        headline(img, "Your headline here", t)
        ...                      # your visual, using card(), text(), prog() etc.
        chrome(img, SCENE, t)    # always last

    SCENE = 5
    if __name__ == "__main__":
        render(SCENE, draw)
"""
import pathlib
import subprocess

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLIPS = ROOT / "clips"

W, H, FPS = 1080, 1920, 30
DUR = 2.5
FRAMES = int(DUR * FPS)  # 75
TOTAL_SCENES = 12
MARGIN = 96
SAFE_BOTTOM = H - 140

BG = (15, 17, 21)
CARD = (28, 31, 38)
LINE = (52, 56, 66)
INK = (242, 239, 233)
MUTED = (140, 146, 158)
ACCENT = (217, 119, 87)
GREEN = (120, 190, 140)

_FONT_DIR = "/usr/share/fonts/opentype/inter/"
_WEIGHTS = {"regular": "Inter-Regular.otf", "medium": "Inter-Medium.otf",
            "semibold": "Inter-SemiBold.otf", "bold": "InterDisplay-Bold.otf"}
_cache = {}


def font(size, weight="semibold"):
    key = ("inter", size, weight)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(_FONT_DIR + _WEIGHTS[weight], size)
    return _cache[key]


def mono(size, bold=False):
    key = ("mono", size, bold)
    if key not in _cache:
        name = "DejaVuSansMono-Bold.ttf" if bold else "DejaVuSansMono.ttf"
        _cache[key] = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/" + name, size)
    return _cache[key]


# ---------- timing ----------
def ease_out(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def prog(t, start=0.0, dur=0.5):
    """Eased 0..1 progress of an animation that starts at `start` seconds and lasts `dur`."""
    return ease_out((t - start) / dur)


# ---------- drawing primitives (all support alpha 0..1) ----------
def _layer(img):
    return Image.new("RGBA", img.size, (0, 0, 0, 0))


def _rgba(color, alpha):
    return (*color[:3], int(255 * max(0.0, min(1.0, alpha))))


def text(img, xy, s, fnt, fill=INK, alpha=1.0, anchor="la"):
    if alpha <= 0:
        return
    lay = _layer(img)
    ImageDraw.Draw(lay).text(xy, s, font=fnt, fill=_rgba(fill, alpha), anchor=anchor)
    img.alpha_composite(lay)


def rect(img, box, fill=CARD, outline=None, radius=28, width=3, alpha=1.0):
    if alpha <= 0:
        return
    lay = _layer(img)
    ImageDraw.Draw(lay).rounded_rectangle(
        box, radius=radius, fill=_rgba(fill, alpha) if fill else None,
        outline=_rgba(outline, alpha) if outline else None, width=width)
    img.alpha_composite(lay)


def circle(img, center, r, fill=CARD, outline=None, width=4, alpha=1.0):
    if alpha <= 0:
        return
    cx, cy = center
    lay = _layer(img)
    ImageDraw.Draw(lay).ellipse((cx - r, cy - r, cx + r, cy + r),
                                fill=_rgba(fill, alpha) if fill else None,
                                outline=_rgba(outline, alpha) if outline else None, width=width)
    img.alpha_composite(lay)


def line(img, pts, fill=LINE, width=4, alpha=1.0):
    if alpha <= 0:
        return
    lay = _layer(img)
    ImageDraw.Draw(lay).line(pts, fill=_rgba(fill, alpha), width=width, joint="curve")
    img.alpha_composite(lay)


def card(img, box, t, start=0.0, dur=0.5, fill=CARD, outline=LINE, radius=28):
    """Rounded card that fades in and rises 40 px. Returns the y offset used, so content can follow it."""
    p = prog(t, start, dur)
    dy = int(40 * (1 - p))
    x0, y0, x1, y1 = box
    rect(img, (x0, y0 + dy, x1, y1 + dy), fill=fill, outline=outline, radius=radius, alpha=p)
    return dy, p


def wrap(s, fnt, max_w):
    words, lines, cur = s.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def headline(img, s, t, start=0.0, y=300, size=96, color=INK, accent_words=()):
    """Left-aligned, wrapped headline that fades and rises in. Words in accent_words are drawn in ACCENT.
    Returns the y coordinate just below the last line."""
    fnt = font(size, "bold")
    lh = int(size * 1.12)
    for i, ln in enumerate(wrap(s, fnt, W - 2 * MARGIN)):
        p = prog(t, start + 0.08 * i, 0.55)
        yy = y + i * lh + int(30 * (1 - p))
        x = MARGIN
        for word in ln.split(" "):
            c = ACCENT if word.strip(".,:!?") in accent_words else color
            text(img, (x, yy), word, fnt, fill=c, alpha=p)
            x += fnt.getlength(word + " ")
    return y + len(wrap(s, fnt, W - 2 * MARGIN)) * lh


def chrome(img, scene_no, t):
    """Scene counter (top right), brand tag (top left) and the 30 s progress bar. Call last in every scene."""
    text(img, (MARGIN, 140), "MANAGER  +  3 WORKERS", mono(28, True), fill=MUTED)
    text(img, (W - MARGIN, 140), f"{scene_no:02d} / {TOTAL_SCENES}", mono(28, True), fill=MUTED, anchor="ra")
    y = SAFE_BOTTOM - 40
    rect(img, (MARGIN, y, W - MARGIN, y + 8), fill=LINE, radius=4)
    frac = ((scene_no - 1) * DUR + t) / (TOTAL_SCENES * DUR)
    x1 = MARGIN + int((W - 2 * MARGIN) * min(1.0, frac))
    if x1 > MARGIN + 8:
        rect(img, (MARGIN, y, x1, y + 8), fill=ACCENT, radius=4)


# ---------- render ----------
def render(scene_no, draw_fn, out=None):
    out = pathlib.Path(out) if out else CLIPS / f"scene_{scene_no:02d}.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264",
           "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), str(out)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(FRAMES):
        img = Image.new("RGBA", (W, H), (*BG, 255))
        draw_fn(img, f / FPS)
        proc.stdin.write(img.convert("RGB").tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError("ffmpeg failed")
    print(f"wrote {out}")
    return out
