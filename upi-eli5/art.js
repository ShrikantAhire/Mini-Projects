// Original cast and props for "UPI Explained Like You're 5". Flat 2D, round heads, thick outline.
// Everything is drawn in code from these functions; nothing is traced or copied.
import { TAU, lerp, clamp, mulberry32, hash01, rrect } from './lib/motion.js';

export const C = {
  ink: '#262a33',        // outline + type
  paper: '#eef0f3',
  sky: '#cfd6df', skyDusk: '#b9c2ce',
  bldA: '#9aa6b5', bldB: '#87939f', bldC: '#aab3bf', win: '#6f7b89', winLit: '#e9dcb0',
  road: '#5d6670', curb: '#c4c9cf',
  wood: '#a87a52', woodDark: '#7d5838',
  banana: '#e6c24f', bananaDark: '#b8952f',
  red: '#d6282f',        // the one accent: story lines, stamps, the QR frame
  white: '#ffffff',
  noteA: '#a9b8a2', noteB: '#c9a8b0',   // generic notes, not real currency art
  phone: '#2e333c', screen: '#f7f8fa',
  grey: '#7c8592',
};

// ------------------------------------------------------------------ helpers
export function line(ctx, pts, w, color, cap = 'round') {
  ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]);
  for (let i = 1; i < pts.length; i++) ctx.lineTo(pts[i][0], pts[i][1]);
  ctx.lineWidth = w; ctx.strokeStyle = color; ctx.lineCap = cap; ctx.lineJoin = 'round'; ctx.stroke();
}
export function shape(ctx, fill, lw = 5) {
  ctx.fillStyle = fill; ctx.fill();
  if (lw) { ctx.lineWidth = lw; ctx.strokeStyle = C.ink; ctx.lineJoin = 'round'; ctx.stroke(); }
}
export function circle(ctx, x, y, r, fill, lw = 5) { ctx.beginPath(); ctx.arc(x, y, r, 0, TAU); shape(ctx, fill, lw); }
export function ell(ctx, x, y, rx, ry, fill, lw = 5, rot = 0) { ctx.beginPath(); ctx.ellipse(x, y, rx, ry, rot, 0, TAU); shape(ctx, fill, lw); }
// limb: outlined thick stroke
export function limb(ctx, pts, w, color) { line(ctx, pts, w + 10, C.ink); line(ctx, pts, w, color); }

// ------------------------------------------------------------------ cast
export const CAST = {
  raju: {   // banana seller
    skin: '#c48a5c', hair: '#1f1d1c', top: '#4f8580', topDark: '#3d6b67', pants: '#d8d2c4', shoe: '#5a4636',
    hairStyle: 'short', mustache: true, extra: 'gamcha', build: 1.06,
  },
  arjun: {  // office customer
    skin: '#dca57a', hair: '#2b2220', top: '#a9c4dc', topDark: '#87a6c2', pants: '#4a505a', shoe: '#22252b',
    hairStyle: 'side', tie: '#2f3d5c', build: 0.98,
  },
  meena: {  // the didi customer
    skin: '#b47a50', hair: '#1c1a1a', top: '#8a5876', topDark: '#6d4460', pants: '#8a5876', shoe: '#6b4a3a',
    hairStyle: 'bun', saree: true, bindi: true, build: 0.95,
  },
};

// pose: { arms:[[shoulderAngle, elbowBend],[..]] in radians (0 = straight down), mouth 0..1, expr, blink 0..1,
//         look:-1..1, lean, hold:'phone'|'note'|null (right hand), holdL }
// x,y = point between the feet. s = scale (1 => ~560px tall)
export function person(ctx, who, x, y, s = 1, pose = {}) {
  const P = CAST[who];
  const { arms = [[0.15, 0.2], [0.15, 0.2]], mouth = 0, expr = 'neutral', blink = 0, look = 0, lean = 0, bob = 0, face = 0 } = pose;
  ctx.save();
  ctx.translate(x, y - bob * s); ctx.scale(s * P.build, s); ctx.rotate(lean);
  // proportions (local units, feet at 0)
  const legH = 150, torsoH = 175, shoulderW = 70, hipW = 58, headR = 92;
  const hipY = -legH, shY = hipY - torsoH, neckY = shY + 4, headY = shY - headR + 22;
  // legs
  if (P.saree) {
    ctx.beginPath(); ctx.moveTo(-hipW - 4, hipY - 10); ctx.lineTo(-hipW - 18, -6); ctx.lineTo(hipW + 18, -6); ctx.lineTo(hipW + 4, hipY - 10); ctx.closePath();
    shape(ctx, P.top);
    line(ctx, [[-hipW - 16, -22], [hipW + 16, -22]], 7, C.banana);
    ell(ctx, -26, -2, 26, 12, P.shoe, 5); ell(ctx, 26, -2, 26, 12, P.shoe, 5);
  } else {
    for (const sx of [-1, 1]) {
      ctx.beginPath(); rrect(ctx, sx > 0 ? 6 : -50, hipY - 6, 44, legH, 14); shape(ctx, P.pants);
      ell(ctx, sx * 30, -4, 32, 14, P.shoe, 5);
    }
  }
  // back arm (left) drawn behind torso
  const armPts = (side, [a, bend]) => {
    const sx = side * shoulderW * 0.86, sy = shY + 20, L1 = 92, L2 = 86;
    const ang = side * a;                       // outward is positive
    const ex = sx + Math.sin(ang) * L1, ey = sy + Math.cos(ang) * L1;
    const ang2 = ang + side * bend * -1;        // bend forward/up
    const hx = ex + Math.sin(ang2) * L2, hy = ey + Math.cos(ang2) * L2;
    return [[sx, sy], [ex, ey], [hx, hy]];
  };
  const L = armPts(-1, arms[0]), R = armPts(1, arms[1]);
  limb(ctx, L, 34, P.topDark); circle(ctx, L[2][0], L[2][1], 17, P.skin, 5);
  // torso
  ctx.beginPath();
  ctx.moveTo(-shoulderW, shY + 18); ctx.quadraticCurveTo(-shoulderW, shY, -shoulderW + 22, shY);
  ctx.lineTo(shoulderW - 22, shY); ctx.quadraticCurveTo(shoulderW, shY, shoulderW, shY + 18);
  ctx.lineTo(hipW + 4, hipY + 8); ctx.lineTo(-hipW - 4, hipY + 8); ctx.closePath();
  shape(ctx, P.top);
  if (P.tie) {
    ctx.beginPath(); ctx.moveTo(-8, shY + 6); ctx.lineTo(8, shY + 6); ctx.lineTo(14, shY + 110); ctx.lineTo(0, shY + 130); ctx.lineTo(-14, shY + 110); ctx.closePath(); shape(ctx, P.tie, 4);
    line(ctx, [[-30, shY + 2], [0, shY + 22], [30, shY + 2]], 5, C.ink);
  }
  if (P.saree) {   // pallu across the chest
    ctx.beginPath(); ctx.moveTo(-shoulderW + 6, shY + 4); ctx.lineTo(-shoulderW + 40, shY); ctx.lineTo(hipW + 4, hipY + 4); ctx.lineTo(hipW - 30, hipY + 8); ctx.closePath();
    shape(ctx, P.topDark, 4);
    line(ctx, [[-shoulderW + 40, shY + 2], [hipW + 2, hipY + 2]], 6, C.banana);
  }
  if (P.extra === 'gamcha') {   // towel over the shoulder
    ctx.beginPath(); ctx.moveTo(shoulderW - 44, shY - 4); ctx.lineTo(shoulderW + 2, shY + 6); ctx.lineTo(shoulderW - 6, shY + 96); ctx.lineTo(shoulderW - 34, shY + 90); ctx.closePath();
    shape(ctx, '#d9b25a', 4);
    for (let i = 0; i < 3; i++) line(ctx, [[shoulderW - 40 + i * 2, shY + 22 + i * 24], [shoulderW - 2 - i * 2, shY + 28 + i * 24]], 3, '#a9853a');
  }
  // neck + head
  ctx.beginPath(); rrect(ctx, -18, neckY - 30, 36, 34, 8); shape(ctx, P.skin, 5);
  drawHead(ctx, P, 0, headY, headR, { mouth, expr, blink, look, face });
  // front arm (right)
  limb(ctx, R, 34, P.top); circle(ctx, R[2][0], R[2][1], 17, P.skin, 5);
  ctx.restore();
  // world position of right hand (for props)
  const rx = x + R[2][0] * s * P.build, ry = y - bob * s + R[2][1] * s;
  const lx = x + L[2][0] * s * P.build, ly = y - bob * s + L[2][1] * s;
  return { rhand: [rx, ry], lhand: [lx, ly], head: [x, y - bob * s + headY * s], headR: headR * s };
}

function drawHead(ctx, P, hx, hy, r, { mouth, expr, blink, look, face }) {
  ctx.save(); ctx.translate(hx, hy);
  // hair behind
  if (P.hairStyle === 'bun') circle(ctx, 0, -r * 0.92, r * 0.38, P.hair, 5);
  circle(ctx, 0, 0, r, P.skin, 6);
  // ears
  ell(ctx, -r * 0.98, r * 0.08, 13, 18, P.skin, 5); ell(ctx, r * 0.98, r * 0.08, 13, 18, P.skin, 5);
  circle(ctx, 0, 0, r, P.skin, 0);
  ctx.beginPath(); ctx.arc(0, 0, r, 0, TAU); ctx.lineWidth = 6; ctx.strokeStyle = C.ink; ctx.stroke();
  // hair front
  ctx.save(); ctx.beginPath(); ctx.arc(0, 0, r - 3, 0, TAU); ctx.clip();
  ctx.fillStyle = P.hair;
  if (P.hairStyle === 'short') {
    ctx.beginPath(); ctx.moveTo(-r, -r * 0.05); ctx.quadraticCurveTo(-r * 0.9, -r * 1.2, 0, -r * 1.05); ctx.quadraticCurveTo(r * 0.95, -r * 1.15, r, -r * 0.1);
    ctx.quadraticCurveTo(r * 0.7, -r * 0.5, r * 0.2, -r * 0.55); ctx.quadraticCurveTo(-r * 0.4, -r * 0.6, -r * 0.75, -r * 0.25); ctx.closePath(); ctx.fill();
  } else if (P.hairStyle === 'side') {
    ctx.beginPath(); ctx.moveTo(-r, 0); ctx.quadraticCurveTo(-r, -r * 1.15, r * 0.1, -r * 1.05); ctx.quadraticCurveTo(r * 1.05, -r * 0.95, r, -r * 0.05);
    ctx.quadraticCurveTo(r * 0.85, -r * 0.55, r * 0.35, -r * 0.62); ctx.quadraticCurveTo(-r * 0.15, -r * 0.5, -r * 0.55, -r * 0.62); ctx.quadraticCurveTo(-r * 0.8, -r * 0.35, -r * 0.82, 0); ctx.closePath(); ctx.fill();
  } else if (P.hairStyle === 'bun') {
    ctx.beginPath(); ctx.moveTo(-r, r * 0.2); ctx.quadraticCurveTo(-r, -r * 1.1, 0, -r * 1.02); ctx.quadraticCurveTo(r, -r * 1.1, r, r * 0.2);
    ctx.quadraticCurveTo(r * 0.8, -r * 0.4, r * 0.05, -r * 0.62); ctx.quadraticCurveTo(-r * 0.8, -r * 0.4, -r, r * 0.2); ctx.closePath(); ctx.fill();
  }
  ctx.restore();
  ctx.beginPath(); ctx.arc(0, 0, r, 0, TAU); ctx.lineWidth = 6; ctx.strokeStyle = C.ink; ctx.stroke();
  const fx = face * r * 0.12;
  // eyes
  const ey = -r * 0.02, ex = r * 0.36;
  const shock = expr === 'shock';
  for (const sx of [-1, 1]) {
    const rx = shock ? 19 : 16, ry = (shock ? 23 : 19) * (1 - blink * 0.92);
    ell(ctx, fx + sx * ex, ey, rx, Math.max(ry, 1.5), C.white, 4);
    if (blink < 0.6) circle(ctx, fx + sx * ex + look * 6, ey + 2, shock ? 6 : 8, C.ink, 0);
  }
  // brows
  const brow = { neutral: [0, 0], smile: [-4, 0.05], worried: [-2, -0.35], shock: [-16, 0], smug: [2, 0.3], annoyed: [4, 0.4] }[expr] || [0, 0];
  for (const sx of [-1, 1]) {
    const cx = fx + sx * ex, cy = ey - 36 + brow[0];
    const a = sx * brow[1];
    line(ctx, [[cx - 20 * Math.cos(a), cy - 20 * Math.sin(a) * -1], [cx + 20 * Math.cos(a), cy + 20 * Math.sin(a) * -1]], 8, P.hair);
  }
  // nose
  line(ctx, [[fx + 2, r * 0.12], [fx + 9, r * 0.27], [fx - 1, r * 0.29]], 4, C.ink);
  // mustache
  const my = r * 0.42;
  // mouth
  ctx.save(); ctx.translate(fx, my + (P.mustache ? 14 : 4));
  const open = clamp(mouth);
  if (open > 0.06) {
    ell(ctx, 0, 4, 18 + open * 6, 6 + open * 18, '#5a2a2a', 4);
  } else if (expr === 'smile' || expr === 'smug') {
    ctx.beginPath(); ctx.moveTo(-26, -2); ctx.quadraticCurveTo(0, expr === 'smug' ? 14 : 24, 26, -6); ctx.lineWidth = 5; ctx.strokeStyle = C.ink; ctx.lineCap = 'round'; ctx.stroke();
  } else if (shock) {
    ell(ctx, 0, 6, 14, 18, '#5a2a2a', 4);
  } else if (expr === 'worried' || expr === 'annoyed') {
    ctx.beginPath(); ctx.moveTo(-20, 8); ctx.quadraticCurveTo(0, -6, 20, 8); ctx.lineWidth = 5; ctx.strokeStyle = C.ink; ctx.lineCap = 'round'; ctx.stroke();
  } else {
    line(ctx, [[-16, 2], [16, 2]], 5, C.ink);
  }
  ctx.restore();
  if (P.mustache) {
    ctx.beginPath(); ctx.moveTo(fx - 40, my + 8); ctx.quadraticCurveTo(fx - 22, my - 12, fx, my - 2); ctx.quadraticCurveTo(fx + 22, my - 12, fx + 40, my + 8); ctx.quadraticCurveTo(fx + 18, my + 4, fx, my + 6); ctx.quadraticCurveTo(fx - 18, my + 4, fx - 40, my + 8);
    ctx.fillStyle = P.hair; ctx.fill();
  }
  if (P.bindi) circle(ctx, fx, ey - 52, 6, C.red, 0);
  // cheeks
  ctx.globalAlpha = 0.18; circle(ctx, fx - r * 0.55, r * 0.3, 14, C.red, 0); circle(ctx, fx + r * 0.55, r * 0.3, 14, C.red, 0); ctx.globalAlpha = 1;
  ctx.restore();
}

// ------------------------------------------------------------------ props
// QR code: seeded modules with three finder squares; red frame is the story accent
export function qr(ctx, x, y, size, { frame = true, glow = 0, label = true } = {}) {
  const n = 21, m = size / (n + 4);
  ctx.save(); ctx.translate(x - size / 2, y - size / 2);
  if (glow > 0) { ctx.shadowColor = C.red; ctx.shadowBlur = 40 * glow; }
  ctx.beginPath(); rrect(ctx, 0, 0, size, size * (label ? 1.18 : 1), size * 0.06); ctx.fillStyle = C.white; ctx.fill();
  ctx.shadowBlur = 0;
  if (frame) { ctx.lineWidth = Math.max(3, size * 0.035); ctx.strokeStyle = C.red; ctx.stroke(); }
  ctx.fillStyle = C.ink;
  const rnd = mulberry32(77);
  const finder = (i, j) => (i < 7 && j < 7) || (i >= n - 7 && j < 7) || (i < 7 && j >= n - 7);
  for (let j = 0; j < n; j++) for (let i = 0; i < n; i++) {
    const r = rnd();
    if (finder(i, j)) continue;
    if (r > 0.52) ctx.fillRect((i + 2) * m, (j + 2) * m, m + 0.5, m + 0.5);
  }
  for (const [i, j] of [[0, 0], [n - 7, 0], [0, n - 7]]) {
    ctx.fillRect((i + 2) * m, (j + 2) * m, 7 * m, 7 * m);
    ctx.fillStyle = C.white; ctx.fillRect((i + 3) * m, (j + 3) * m, 5 * m, 5 * m);
    ctx.fillStyle = C.ink; ctx.fillRect((i + 4) * m, (j + 4) * m, 3 * m, 3 * m);
  }
  if (label) {
    ctx.fillStyle = C.red; ctx.font = `800 ${Math.round(size * 0.1)}px UI`; ctx.textAlign = 'center';
    ctx.fillText('SCAN & PAY', size / 2, size * 1.11);
  }
  ctx.restore();
}

export function bananaBunch(ctx, x, y, s = 1, rot = 0) {
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s, s);
  // 4 fat curved fingers fanning from a stem
  for (let i = 3; i >= 0; i--) {
    ctx.save(); ctx.rotate(-0.5 + i * 0.32);
    ctx.beginPath(); ctx.moveTo(0, 0);
    ctx.bezierCurveTo(34, -10, 70, 10, 84, 52);
    ctx.bezierCurveTo(88, 62, 80, 66, 74, 58);
    ctx.bezierCurveTo(60, 30, 34, 18, 0, 18); ctx.closePath();
    shape(ctx, C.banana, 4);
    line(ctx, [[80, 54], [86, 62]], 6, C.bananaDark);
    ctx.restore();
  }
  ctx.beginPath(); rrect(ctx, -16, -4, 22, 26, 5); shape(ctx, C.bananaDark, 4);
  ctx.restore();
}

export function cart(ctx, x, y, s = 1, { qrGlow = 0, showQR = true, sign = true } = {}) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  // wheels
  for (const wx of [-150, 150]) { circle(ctx, wx, -50, 50, C.woodDark, 6); circle(ctx, wx, -50, 12, C.ink, 0); for (let k = 0; k < 6; k++) line(ctx, [[wx, -50], [wx + Math.cos(k) * 44, -50 + Math.sin(k) * 44]], 4, C.ink); }
  // bed
  ctx.beginPath(); rrect(ctx, -230, -190, 460, 90, 10); shape(ctx, C.wood, 6);
  for (let i = 0; i < 4; i++) line(ctx, [[-225, -170 + i * 20], [225, -170 + i * 20]], 2, C.woodDark);
  // handle
  line(ctx, [[-230, -150], [-330, -120]], 16, C.ink); line(ctx, [[-230, -150], [-330, -120]], 8, C.woodDark);
  // bananas on top
  const rnd = mulberry32(5);
  for (let i = 0; i < 6; i++) bananaBunch(ctx, -200 + i * 72, -205 - (i % 2) * 14, 0.95, -0.25 + (rnd() - 0.5) * 0.4);
  // canopy poles + roof
  line(ctx, [[-215, -190], [-215, -560]], 10, C.ink); line(ctx, [[215, -190], [215, -560]], 10, C.ink);
  ctx.beginPath(); ctx.moveTo(-260, -550); ctx.lineTo(260, -550); ctx.lineTo(230, -610); ctx.lineTo(-230, -610); ctx.closePath(); shape(ctx, '#c9b98f', 6);
  for (let i = -3; i <= 3; i++) line(ctx, [[i * 70, -608], [i * 76, -552]], 3, '#a89772');
  if (sign) { ctx.beginPath(); rrect(ctx, -110, -602, 220, 44, 8); shape(ctx, C.white, 4); ctx.fillStyle = C.ink; ctx.font = '800 26px UI'; ctx.textAlign = 'center'; ctx.fillText('RAJU FRUITS', 0, -571); }
  if (showQR) qr(ctx, 150, -330, 110, { glow: qrGlow });
  ctx.restore();
}

export function phone(ctx, x, y, s = 1, rot = 0, draw) {
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s, s);
  ctx.beginPath(); rrect(ctx, -60, -110, 120, 220, 18); shape(ctx, C.phone, 5);
  ctx.beginPath(); rrect(ctx, -50, -96, 100, 192, 10); ctx.fillStyle = C.screen; ctx.fill();
  if (draw) { ctx.save(); ctx.beginPath(); rrect(ctx, -50, -96, 100, 192, 10); ctx.clip(); draw(ctx); ctx.restore(); }
  ctx.restore();
}

export function tick(ctx, x, y, r, p = 1) {   // drawn check mark in a red disc
  circle(ctx, x, y, r * Math.min(1, p * 1.4), C.red, 0);
  if (p > 0.4) {
    const k = clamp((p - 0.4) / 0.6);
    const a = [x - r * 0.45, y], b = [x - r * 0.1, y + r * 0.35], c = [x + r * 0.5, y - r * 0.35];
    const pts = k < 0.4 ? [a, [lerp(a[0], b[0], k / 0.4), lerp(a[1], b[1], k / 0.4)]] : [a, b, [lerp(b[0], c[0], (k - 0.4) / 0.6), lerp(b[1], c[1], (k - 0.4) / 0.6)]];
    line(ctx, pts, r * 0.22, C.white);
  }
}

// generic banknote (not a reproduction of real currency)
export function note(ctx, x, y, s, rot, value, { color, dead = 0 } = {}) {
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s, s);
  const col = color || (value === 1000 ? C.noteB : C.noteA);
  ctx.beginPath(); rrect(ctx, -110, -55, 220, 110, 8); shape(ctx, col, 5);
  ctx.beginPath(); rrect(ctx, -96, -42, 192, 84, 4); ctx.lineWidth = 3; ctx.strokeStyle = 'rgba(38,42,51,.35)'; ctx.stroke();
  circle(ctx, 52, 0, 26, 'rgba(255,255,255,.45)', 3);
  ctx.fillStyle = C.ink; ctx.font = `800 ${value >= 1000 ? 34 : 40}px Display`; ctx.textAlign = 'left'; ctx.fillText('₹' + value, -88, 14);
  if (dead > 0) {
    ctx.globalAlpha = dead; ctx.fillStyle = 'rgba(80,80,80,.55)'; ctx.fillRect(-110, -55, 220, 110); ctx.globalAlpha = 1;
    const k = clamp(dead * 1.5);
    line(ctx, [[-90, -40], [lerp(-90, 90, k), lerp(-40, 40, k)]], 14, C.red);
    if (dead > 0.5) { const k2 = clamp((dead - 0.5) * 2); line(ctx, [[90, -40], [lerp(90, -90, k2), lerp(-40, 40, k2)]], 14, C.red); }
  }
  ctx.restore();
}

export function bank(ctx, x, y, s = 1, label = 'BANK') {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(-120, -200); ctx.lineTo(0, -270); ctx.lineTo(120, -200); ctx.closePath(); shape(ctx, C.paper, 5);
  ctx.beginPath(); rrect(ctx, -120, -200, 240, 26, 3); shape(ctx, C.bldC, 5);
  for (let i = 0; i < 4; i++) { ctx.beginPath(); rrect(ctx, -98 + i * 62, -170, 26, 150, 3); shape(ctx, C.paper, 4); }
  ctx.beginPath(); rrect(ctx, -136, -22, 272, 24, 3); shape(ctx, C.bldC, 5);
  ctx.fillStyle = C.ink; ctx.font = '800 22px UI'; ctx.textAlign = 'center'; ctx.fillText(label, 0, -181);
  ctx.restore();
}

// city backdrop: rows of blocky buildings, deterministic
export function city(ctx, W, H, ground, { tint = 0, pan = 0, seed = 3 } = {}) {
  const sky = ctx.createLinearGradient(0, 0, 0, ground); sky.addColorStop(0, C.sky); sky.addColorStop(1, '#e3e7ec');
  ctx.fillStyle = sky; ctx.fillRect(-W, -H, W * 3, ground + H);
  for (const [row, col, hMin, hMax, par] of [[0, C.bldC, 380, 640, 0.3], [1, C.bldA, 260, 520, 0.6], [2, C.bldB, 180, 380, 1]]) {
    let x = -W - 200 - ((pan * par) % 260);
    let i = Math.floor((pan * par) / 260) * 7 + row * 101;
    while (x < 2 * W + 200) {
      const w = 160 + hash01(i, seed) * 160, h = hMin + hash01(i + 3, seed) * (hMax - hMin);
      ctx.fillStyle = col; ctx.fillRect(x, ground - h, w - 8, h);
      ctx.fillStyle = row === 2 ? C.win : 'rgba(111,123,137,.55)';
      for (let wy = ground - h + 26; wy < ground - 40; wy += 46) for (let wx = x + 18; wx < x + w - 30; wx += 38) {
        if (hash01(wx * 3 + wy, seed) > 0.25) ctx.fillRect(wx, wy, 18, 24);
      }
      if (row === 2 && hash01(i, 9) > 0.6) { ctx.fillStyle = 'rgba(38,42,51,.5)'; ctx.fillRect(x + 10, ground - h - 22, 4, 22); ctx.fillRect(x + 4, ground - h - 22, 20, 3); }
      x += w; i++;
    }
  }
  ctx.fillStyle = C.curb; ctx.fillRect(-W, ground, W * 3, 18);
  ctx.fillStyle = '#b3b8be'; ctx.fillRect(-W, ground + 18, W * 3, H * 2);
  if (tint > 0) { ctx.fillStyle = `rgba(120,108,90,${0.35 * tint})`; ctx.fillRect(-W, -H, W * 3, H * 3); }
}
