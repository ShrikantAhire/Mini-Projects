import sys; sys.path.insert(0, '/tmp/claude-0/-home-user-Mini-Projects/cfcad8a0-fce0-5fdb-a25c-c2f339edee7f/scratchpad/hf/ep1/build')
from rig import stick, INK, AMBER, RED, GREEN, PAPER
import props as P
NOC = f'<circle cx="80" cy="-130" r="58" fill="none" stroke="{RED}" stroke-width="7"/>'
OUT = '/tmp/claude-0/-home-user-Mini-Projects/cfcad8a0-fce0-5fdb-a25c-c2f339edee7f/scratchpad/thumb-ep1/'
def page(body, bg):
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@800;900&display=block" rel="stylesheet">
<style>html,body{{margin:0;padding:0;width:1280px;height:720px;overflow:hidden;background:{bg}}} text{{font-family:'Nunito',sans-serif}}</style></head><body>
<svg width="1280" height="720" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg"><rect width="1920" height="1080" fill="{bg}"/>{body}</svg></body></html>'''
def big(t, x, y, size, fill, sw=14, anchor="middle"):
    return f'<text x="{x}" y="{y}" font-family="Nunito" font-weight="900" font-size="{size}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" paint-order="stroke" stroke-linejoin="round" text-anchor="{anchor}">{t}</text>'

# A: Only 7?
b = '<rect y="900" width="1920" height="180" fill="#C5D5E2"/>'
b += f'<g transform="translate(1500 640) rotate(6)">{P.paper("gp",0,0,"",GREEN,1.5).replace(NOC,"")}<text x="0" y="40" font-family="Nunito" font-weight="900" font-size="190" fill="{GREEN}" stroke="{INK}" stroke-width="8" paint-order="stroke" text-anchor="middle">10/10</text></g>'
b += f'<circle cx="1660" cy="330" r="70" fill="#FFD43B" opacity="0.0"/>'
b += stick('leo', 430, 1290, 2.9, 'leo', ('panicked',), ('stand',), meter=0.12, meter_r=46, look=(14, -4))
b += f'<g transform="translate(900 660) rotate(-10)">{P.paper("sp",0,0,"",RED,0.85).replace(NOC,"")}<text x="0" y="40" font-family="Nunito" font-weight="900" font-size="120" fill="{RED}" stroke="{INK}" stroke-width="6" paint-order="stroke" text-anchor="middle">7/10</text></g>'
b += big('ONLY 7?', 1240, 210, 210, AMBER)
open(OUT + 'a.html', 'w').write(page(b, '#DDE7EF'))

# B: Not enough? (meter close-up)
b = '<rect y="0" width="1920" height="1080" fill="#FFF4E0"/>'
for i, t in enumerate(["Not the tallest", "Not the fastest", "Not the best at spelling", "Not the best at drawing"]):
    y = 330 + i * 120
    b += f'<text x="1180" y="{y}" font-family="Nunito" font-weight="800" font-size="64" fill="#B8A88F">{t}</text><line x1="1170" y1="{y-22}" x2="{1190+len(t)*33}" y2="{y-22}" stroke="{RED}" stroke-width="9" stroke-linecap="round" opacity="0.8"/>'
b += stick('leo', 600, 1560, 3.4, 'leo', ('sad',), ('stand',), meter=0.06, meter_r=56)
b += P.arrow('ar', 1000, 760, 860, 1000, RED, 22)
b += big('NOT ENOUGH?', 1270, 170, 140, "#FFFFFF", 16)
open(OUT + 'b.html', 'w').write(page(b, '#FFF4E0'))

# C: No seat?
b = '<rect y="0" width="1920" height="1080" fill="#FBF3E4"/><rect y="880" width="1920" height="200" fill="#E8D8BC"/>'
for nm, x, cap, girl, hair, shirt in (("e", 980, "#E03131", 0, None, None), ("a", 1180, None, 1, "#E8B04A", "#B2F2BB"), ("m", 1380, "#1C7ED6", 0, None, None), ("n", 1580, "#2F9E44", 0, None, None)):
    if girl: b += stick(nm, x, 900, 0.95, 'girl', ('grin',), hair=hair, shirt=shirt)
    else: b += stick(nm, x, 900, 1.0 if nm != "m" else 1.12, 'kid', ('grin',), cap=cap, flip=(x > 1300))
b += P.lunch_table('t', 1280, 900, 900)
b += f'<g transform="translate(1280 380) rotate(-5) scale(1.25)">{P.napkin("nap",0,0)}</g>'
b += stick('leo', 420, 1330, 2.2, 'leo', ('shocked',), ('carry',), meter=0.05, meter_r=46, look=(12, 0), extra=P.tray('tr', 0, -150))
b += big('NO SEAT?', 470, 170, 170, AMBER)
open(OUT + 'c.html', 'w').write(page(b, '#FBF3E4'))
print('ok')
