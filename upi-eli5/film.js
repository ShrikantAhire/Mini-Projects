// UPI Explained Like You're 5: pure function of time. window.seek(t) paints frame t.
// Scenes are timed in SECONDS against the placed VO (vo_timeline.json); docs/shotlist.md is the plan.
import * as M from './lib/motion.js';
import { C, person, cart, qr, phone, note, bank, tick, city, line, circle, bananaBunch } from './art.js';

const { W, H, E, prog, lerp, clamp, spring, SPRING, wobble, font, text, fill, rrect, mulberry32, hash01, noise1 } = M;
const DISPLAY = 'Display', UI = 'UI';
const GROUND = 820;
const B = (t) => (t - 0.00212) / 0.599996;   // seconds -> beats on the measured grid (beats.json)

// ------------------------------------------------------------------ data loaded in init
let VO = [], LIP = null, CAPS = [];
const CAPTEXT = {
  n1: ['This man sells bananas in Mumbai.', 'He takes digital payments all day,', 'with no card machine and no fees.'],
  n2: ['So how did a country that ran on cash', 'get here?'],
  n3: ['In 2016, India paid for', 'almost everything in cash.'],
  c1: ['Bhaiya, change for ₹500?'],
  v1: ['“Sir, I sell bananas. I don\'t run a bank.”'],
  n4: ['Card machines cost money,', 'and banks take a cut,', 'so small shops said no.'],
  n5: ['That April, India\'s banks launched UPI.', 'Any bank to any bank, by phone,', 'in seconds, for free.'],
  n6: ['Hardly anyone used it.', 'Then, on 8 November,', 'India cancelled its ₹500 and ₹1,000 notes', 'overnight.'],
  n7: ['About 86% of India\'s cash', 'stopped being money.'],
  c2: ['“So how do I pay now?”'],
  v2: ['“Scan the code, didi.”'],
  n8: ['Suddenly, people had no choice.', 'And a QR code costs nothing to print.'],
  n9: ['Today, UPI handles more than', '20 billion payments a month.', 'And most of them start', 'with a sticker like this one.'],
};
const line_ = (k) => VO.find((r) => r.key === k) || { start: 0, end: 0 };
const mouthOf = (t, keys) => {
  if (!LIP) return 0;
  for (const k of keys) { const r = line_(k); if (t >= r.start && t <= r.end) {
    const v = LIP.env[Math.min(LIP.env.length - 1, Math.floor(t * LIP.fps))] || 0;
    return v * (0.75 + 0.25 * Math.abs(Math.sin(t * 23)));
  } }
  return 0;
};

// ------------------------------------------------------------------ motion helpers
const sp = (t, t0, cfg = SPRING.bouncy) => spring(t - t0, cfg);
const ez = (t, a, b, f = E.inOutCubic) => f(prog(t, a, b));
const blinkAt = (t, times) => { for (const b of times) { const d = Math.abs(t - b); if (d < 0.09) return 1 - d / 0.09; } return 0; };
function zoomAt(ctx, s, cx, cy, tx = cx, ty = cy) { ctx.translate(tx, ty); ctx.scale(s, s); ctx.translate(-cx, -cy); }
const logZ = (a, b, p) => a * (b / a) ** p;
function outlined(ctx, str, x, y, size, color = C.white, stroke = C.ink, align = 'left', lw = 0.07) {
  ctx.font = font(size, 400, DISPLAY); ctx.textAlign = align; ctx.lineJoin = 'round';
  ctx.lineWidth = size * lw * 2; ctx.strokeStyle = stroke; ctx.strokeText(str, x, y);
  ctx.fillStyle = color; ctx.fillText(str, x, y);
}
function pill(ctx, str, x, y, size, bg = C.red, fg = C.white, align = 'center', pad = 0.42) {
  ctx.font = font(size, 800, UI); const w = ctx.measureText(str).width, h = size * 1.5;
  const x0 = align === 'center' ? x - w / 2 - size * pad : x;
  rrect(ctx, x0, y - h * 0.72, w + size * pad * 2, h, size * 0.25); ctx.fillStyle = bg; ctx.fill();
  ctx.lineWidth = 5; ctx.strokeStyle = C.ink; ctx.stroke();
  ctx.fillStyle = fg; ctx.textAlign = 'left'; ctx.fillText(str, x0 + size * pad, y);
  return w + size * pad * 2;
}
function stamp(ctx, str, x, y, size, rot, k) {
  if (k <= 0) return;
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); const s = lerp(1.8, 1, clamp(k)); ctx.scale(s, s); ctx.globalAlpha = clamp(k * 3);
  ctx.font = font(size, 400, DISPLAY); const w = ctx.measureText(str).width;
  rrect(ctx, -w / 2 - size * 0.25, -size * 0.92, w + size * 0.5, size * 1.12, 10);
  ctx.lineWidth = size * 0.08; ctx.strokeStyle = C.red; ctx.stroke();
  ctx.fillStyle = C.red; ctx.textAlign = 'center'; ctx.fillText(str, 0, 0);
  ctx.restore();
}
function paperBg(ctx, tone = C.paper) {
  fill(ctx, tone);
  ctx.fillStyle = 'rgba(38,42,51,.05)';
  for (let x = 0; x < W; x += 60) ctx.fillRect(x, 0, 2, H);
  for (let y = 0; y < H; y += 60) ctx.fillRect(0, y, W, 2);
}
function darkBg(ctx) {
  const g = ctx.createRadialGradient(W / 2, H * 0.45, 100, W / 2, H * 0.5, W * 0.75);
  g.addColorStop(0, '#3a4150'); g.addColorStop(1, '#1b1f27'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
}
function stringArc(ctx, a, b, k, lift = 120, w = 6, dash = null) {
  if (k <= 0) return;
  const mx = (a[0] + b[0]) / 2, my = Math.min(a[1], b[1]) - lift;
  ctx.beginPath();
  const N = 40, n = Math.max(2, Math.round(N * clamp(k)));
  for (let i = 0; i <= n; i++) {
    const s = (i / N);
    const x = (1 - s) ** 2 * a[0] + 2 * (1 - s) * s * mx + s * s * b[0];
    const y = (1 - s) ** 2 * a[1] + 2 * (1 - s) * s * my + s * s * b[1];
    i ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
  }
  ctx.setLineDash(dash || []); ctx.lineWidth = w; ctx.strokeStyle = C.red; ctx.lineCap = 'round'; ctx.stroke(); ctx.setLineDash([]);
  circle(ctx, a[0], a[1], w * 1.4, C.red, 0);
}
const arcPt = (a, b, s, lift = 120) => {
  const mx = (a[0] + b[0]) / 2, my = Math.min(a[1], b[1]) - lift;
  return [(1 - s) ** 2 * a[0] + 2 * (1 - s) * s * mx + s * s * b[0], (1 - s) ** 2 * a[1] + 2 * (1 - s) * s * my + s * s * b[1]];
};

// The cart world: Raju behind his cart on a Mumbai street. Reused by several shots.
function street(ctx, t, { tint = 0, raju = {}, pan = 0, qrGlow = 0, cartX = 1180, sign = true } = {}) {
  city(ctx, W, H, GROUND, { tint: 0, pan: pan + t * 6 });
  const rp = { expr: 'smile', blink: blinkAt(t, [2.2, 6.1, 11.8, 16.3, 21.5, 27.9, 33.2, 44.2, 50.6, 56.7]), ...raju };
  const R = person(ctx, 'raju', cartX - 70, GROUND + 70, 0.95, rp);
  cart(ctx, cartX, GROUND + 140, 1.0, { qrGlow, sign });
  if (tint > 0) { ctx.fillStyle = `rgba(150,128,98,${0.42 * tint})`; ctx.fillRect(0, 0, W, H); }
  return { R, qrPos: [cartX + 150, GROUND + 140 - 330] };
}

// ------------------------------------------------------------------ S1 hook (0 - 7.5)
function s1(ctx, t) {
  ctx.save();
  const z = logZ(1.18, 1.3, ez(t, 0, 7.4, E.inOutSine));
  zoomAt(ctx, z, 1180, 600, 1240, 600);
  const scanning = t > 3.7 && t < 6.6;
  const { qrPos } = street(ctx, t, { qrGlow: scanning ? 0.6 + 0.4 * Math.sin(t * 9) : 0, raju: { expr: t > 4.9 ? 'smug' : 'smile', look: t > 3.8 && t < 6 ? 1 : 0 } });
  // phone scans the sticker
  const kin = sp(t, 3.6, SPRING.snappy), kout = ez(t, 6.4, 6.9, E.inCubic);
  if (kin > 0 && kout < 1) {
    const px = lerp(1900, qrPos[0] + 300, kin) + kout * 700, py = lerp(1250, qrPos[1] + 60, kin) + kout * 400;
    circle(ctx, px + 12, py + 112, 40, CASTskin('arjun'), 5);
    phone(ctx, px, py, 1.25, -0.18, (c) => {
      if (t < 4.85) { // scan frame
        const k = (t * 1.6) % 1; c.strokeStyle = C.red; c.lineWidth = 4;
        c.strokeRect(-34, -50, 68, 68); line(c, [[-34, -50 + k * 68], [34, -50 + k * 68]], 3, C.red);
        c.fillStyle = C.ink; c.font = font(15, 700, UI); c.textAlign = 'center'; c.fillText('Scanning…', 0, 52);
      } else {
        tick(c, 0, -14, 34, ez(t, 4.85, 5.25, E.outBack));
        c.fillStyle = C.ink; c.font = font(17, 800, UI); c.textAlign = 'center'; c.fillText('₹40 PAID', 0, 52);
        c.font = font(12, 600, UI); c.fillStyle = C.grey; c.fillText('to Raju Fruits', 0, 72);
      }
    });
  }
  ctx.restore();
  // title (screen space): already landing on frame 0
  const ex = ez(t, 2.9, 3.4, E.inBack);
  if (ex < 1) {
    const k = sp(t, -0.12, SPRING.bouncy), dy = -ex * 700;
    ctx.save(); ctx.translate(150, 470 + dy); const s = lerp(1.25, 1, clamp(k)); ctx.scale(s, s);
    outlined(ctx, 'UPI', 0, 0, 340);
    ctx.restore();
    const k2 = sp(t, 0.35, SPRING.snappy);
    if (k2 > 0) { ctx.save(); ctx.translate(lerp(-900, 0, clamp(k2)), dy); pill(ctx, "EXPLAINED LIKE YOU'RE 5", 158, 572, 46, C.red, C.white, 'left'); ctx.restore(); }
  }
}
const CASTskin = (w) => ({ raju: '#c48a5c', arjun: '#dca57a', meena: '#b47a50' }[w]);

// ------------------------------------------------------------------ S2 how did we get here (7.5 - 10.4)
function s2(ctx, t) {
  const lt = t - 7.5;
  ctx.save();
  const z = logZ(1.3, 0.8, ez(lt, 0, 0.9, E.outCubic));
  zoomAt(ctx, z, 1180, 560, 1180 + (1 - z) * 900, 560);
  const { qrPos } = street(ctx, t, { raju: { expr: 'smile' } });
  // pile of cash on the pavement, left
  const pile = [-260 + 300, GROUND + 120];
  const rnd = mulberry32(11);
  for (let i = 0; i < 14; i++) {
    const k = sp(lt, 0.5 + i * 0.05, SPRING.bouncy);
    if (k <= 0) continue;
    const fly = ez(t, 9.75, 10.4, E.inCubic);
    const x = pile[0] + (rnd() - 0.5) * 300, y = pile[1] - i * 10 - rnd() * 20;
    note(ctx, x, y - (1 - k) * 200 - fly * (900 + i * 60), 0.9, (rnd() - 0.5) * 0.6 + fly * (i % 2 ? 2 : -2), i % 3 ? 500 : 1000);
  }
  ctx.restore();
  // red question string (screen space) from sticker to pile
  const Z = z, map = ([x, y]) => [(x - 1180) * Z + 1180 + (1 - Z) * 900, (y - 560) * Z + 560];
  const a = map(qrPos), b = map([pile[0] + 40, pile[1] - 120]);
  const k = ez(lt, 1.0, 1.8, E.outCubic) * (1 - ez(t, 9.9, 10.3));
  if (k > 0) {
    stringArc(ctx, a, b, k, 260, 7, [18, 14]);
    if (k > 0.5) { const m = arcPt(a, b, 0.5, 260); const kk = sp(t, 8.9, SPRING.bouncy); circle(ctx, m[0], m[1], 56 * kk, C.red, 5); ctx.save(); ctx.globalAlpha = clamp(kk); outlined(ctx, '?', m[0], m[1] + 34, 96 * kk, C.white, C.ink, 'center', 0); ctx.restore(); }
  }
}

// ------------------------------------------------------------------ S3 2016, everything in cash (10.4 - 14.95)
function s3(ctx, t) {
  const lt = t - 10.4;
  ctx.save(); zoomAt(ctx, logZ(1.0, 1.06, ez(lt, 0, 4.5, E.inOutSine)), 960, 600);
  const { R } = street(ctx, t, { tint: 1, raju: { expr: 'smile', arms: [[0.15, 0.2], [0.55, 1.3]] }, cartX: 1300 });
  const A = person(ctx, 'arjun', 430, GROUND + 150, 0.95, { expr: 'smile', arms: [[0.15, 0.2], [0.65, 1.2]], face: 0.6, look: 1, blink: blinkAt(t, [12.9]) });
  ctx.fillStyle = 'rgba(150,128,98,.25)'; ctx.fillRect(-100, -100, W + 200, H + 200);
  // notes travel from Arjun to Raju three times
  const items = [['Chai', '₹10', 11.2], ['Rickshaw', '₹40', 12.3], ['Rent', '₹8,000', 13.4]];
  items.forEach(([lab, val, t0], i) => {
    const p = ez(t, t0, t0 + 0.75, E.inOutCubic);
    if (t > t0 && t < t0 + 0.8) { const pt = arcPt(A.rhand, R.rhand, p, 220); note(ctx, pt[0], pt[1], 0.55, p * 6, 500); }
    if (t > t0 - 0.2) stringArc(ctx, A.rhand, R.rhand, ez(t, t0 - 0.2, t0 + 0.5, E.outCubic) * (1 - ez(t, t0 + 0.9, t0 + 1.1)), 220, 5, [12, 12]);
  });
  ctx.restore();
  // receipt list, top right
  items.forEach(([lab, val, t0], i) => {
    const k = sp(t, t0 + 0.6, SPRING.snappy); if (k <= 0) return;
    ctx.save(); ctx.translate(lerp(W + 400, 1430, clamp(k)), 150 + i * 92);
    rrect(ctx, 0, -50, 380, 74, 12); ctx.fillStyle = C.white; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = C.ink; ctx.stroke();
    ctx.fillStyle = C.ink; ctx.font = font(36, 700, UI); ctx.textAlign = 'left'; ctx.fillText(lab, 24, 0);
    ctx.textAlign = 'right'; ctx.fillStyle = C.red; ctx.font = font(36, 800, UI); ctx.fillText(val + ' cash', 356, 0);
    ctx.restore();
  });
  stamp(ctx, '2016', 330, 260, 190, -0.08, sp(t, 10.55, SPRING.bouncy));
}

// ------------------------------------------------------------------ S4 skit: change for 500? (14.95 - 19.95)
function s4(ctx, t) {
  const lt = t - 14.95;
  ctx.save(); zoomAt(ctx, logZ(1.42, 1.5, ez(lt, 0, 5, E.inOutSine)), 1000, 520, 960, 500);
  const shrug = sp(t, 17.15, SPRING.wobbly) * (1 - ez(t, 19.4, 19.9));
  const { R } = street(ctx, t, { raju: { expr: t > 16.8 ? 'annoyed' : 'neutral', mouth: mouthOf(t, ['v1']), arms: [[lerp(0.15, 1.15, shrug), lerp(0.2, 1.9, shrug)], [lerp(0.15, 1.15, shrug), lerp(0.2, 1.9, shrug)]], look: -1, face: -0.5, bob: shrug * 6 }, cartX: 1260 });
  const offer = sp(t, 15.05, SPRING.snappy);
  const A = person(ctx, 'arjun', 690, GROUND + 140, 0.95, { expr: t > 17.4 ? 'shock' : 'smile', mouth: mouthOf(t, ['c1']), arms: [[0.15, 0.2], [lerp(0.15, 1.2, offer), lerp(0.2, 0.5, offer)]], face: 0.7, look: 1, blink: blinkAt(t, [18.6]) });
  if (offer > 0) note(ctx, A.rhand[0] + 50, A.rhand[1] - 10, 0.55, -0.15 + 0.05 * wobble(t - 15.3, 3, 4), 500);
  ctx.restore();
}

// ------------------------------------------------------------------ S5 why shops said no (19.95 - 24.8)
function s5(ctx, t) {
  paperBg(ctx);
  ctx.fillStyle = 'rgba(38,42,51,.08)'; ctx.fillRect(0, 860, W, H - 860);
  line(ctx, [[0, 860], [W, 860]], 5, C.ink);
  ctx.save(); zoomAt(ctx, logZ(1.22, 1.3, ez(t, 19.95, 24.8, E.inOutSine)), 960, 640, 960, 610);
  // 1 card machine
  const k1 = sp(t, 20.15, SPRING.bouncy);
  if (k1 > 0) {
    ctx.save(); ctx.translate(420, 860 - (1 - clamp(k1)) * 300); ctx.scale(k1, k1);
    rrect(ctx, -90, -330, 180, 300, 26); ctx.fillStyle = '#3b414c'; ctx.fill(); ctx.lineWidth = 6; ctx.strokeStyle = C.ink; ctx.stroke();
    rrect(ctx, -66, -300, 132, 90, 10); ctx.fillStyle = '#c9d6c2'; ctx.fill();
    for (let r = 0; r < 3; r++) for (let c = 0; c < 3; c++) { rrect(ctx, -60 + c * 44, -190 + r * 44, 32, 30, 6); ctx.fillStyle = '#d9dde3'; ctx.fill(); }
    rrect(ctx, -40, -380, 80, 60, 6); ctx.fillStyle = C.white; ctx.fill(); ctx.stroke();
    ctx.restore();
    const kt = sp(t, 20.9, SPRING.bouncy);
    if (kt > 0) { ctx.save(); ctx.translate(300, 420); ctx.rotate(-0.08 + 0.1 * wobble(t - 20.9, 2, 3)); ctx.scale(kt, kt); pill(ctx, 'COSTS MONEY', 0, 0, 34, C.white, C.ink, 'left'); ctx.restore(); }
  }
  // 2 bank takes a cut
  const k2 = sp(t, 21.75, SPRING.bouncy);
  if (k2 > 0) {
    ctx.save(); ctx.translate(0, (1 - clamp(k2)) * 300); bank(ctx, 1000, 860, 1.35 * clamp(k2) + 0.0001, 'BANK'); ctx.restore();
    // coin with a slice cut out
    const cx = 1000, cy = 380, r = 70, cut = ez(t, 22.6, 23.0, E.outCubic);
    circle(ctx, cx - 230, cy + 30, r, '#e3c35c', 6);
    ctx.fillStyle = C.ink; ctx.font = font(64, 400, DISPLAY); ctx.textAlign = 'center'; ctx.fillText('₹', cx - 230, cy + 54);
    if (cut > 0) {
      const ang = -0.5, sx = cx - 230 + cut * 210, sy = cy + 30 - cut * 140;
      ctx.beginPath(); ctx.moveTo(cx - 230, cy + 30); ctx.arc(cx - 230, cy + 30, r + 4, ang - 0.35, ang + 0.35); ctx.closePath(); ctx.fillStyle = C.paper; ctx.fill();
      ctx.beginPath(); ctx.moveTo(sx, sy); ctx.arc(sx, sy, r, ang - 0.35, ang + 0.35); ctx.closePath(); ctx.fillStyle = '#e3c35c'; ctx.fill(); ctx.lineWidth = 5; ctx.strokeStyle = C.ink; ctx.stroke();
      stringArc(ctx, [cx - 150, cy - 30], [cx + 60, cy - 10], cut, 90, 7);
      if (cut > 0.8) { ctx.save(); ctx.translate(cx + 110, cy - 80); ctx.rotate(-0.08); const kk = sp(t, 23.0, SPRING.bouncy); ctx.scale(kk, kk); pill(ctx, 'TAKES A CUT', 0, 0, 34, C.red, C.white, 'left'); ctx.restore(); }
    }
  }
  // 3 Raju: cash only
  const k3 = sp(t, 23.25, SPRING.bouncy);
  if (k3 > 0) {
    ctx.save(); ctx.translate(0, (1 - clamp(k3)) * 500);
    const shake = Math.sin(t * 14) * ez(t, 23.6, 23.8) * (1 - ez(t, 24.3, 24.6));
    person(ctx, 'raju', 1470, 860, 0.85, { expr: 'annoyed', face: shake, look: shake, blink: blinkAt(t, [24.2]) });
    ctx.save(); ctx.translate(1470, 400); ctx.rotate(-0.06); pill(ctx, 'CASH ONLY', 0, 0, 52, C.white, C.red); ctx.restore();
    ctx.restore();
  }
  ctx.restore();
}

// ------------------------------------------------------------------ S6 web of banks -> UPI (24.8 - 31.6)
function s6(ctx, t) {
  const lt = t - 24.8;
  city(ctx, W, H, GROUND + 60, { pan: 400 + t * 4 });
  ctx.fillStyle = 'rgba(22,26,34,.66)'; ctx.fillRect(0, 0, W, H);
  ctx.save(); zoomAt(ctx, logZ(1.0, 1.05, ez(lt, 0, 6.8, E.inOutSine)), 960, 600);
  const P = [960, 610];
  const banks = [[330, 620], [600, 930], [1590, 620], [1320, 930]];
  const order = [0, 2, 1, 3], lineT = [26.9, 27.45, 28.0, 28.55];
  // strings first (behind)
  order.forEach((bi, j) => {
    const b = banks[bi], k = ez(t, lineT[j], lineT[j] + 0.45, E.outCubic);
    stringArc(ctx, [b[0], b[1] - 250], [P[0] + (b[0] < 960 ? -120 : 120), P[1] - 40], k, 80, 7);
    // money pulses after all lines are drawn
    if (t > 29.0) for (let q = 0; q < 2; q++) { const s = ((t - 29.0) * 0.8 + q * 0.5 + j * 0.13) % 1; const pt = arcPt([b[0], b[1] - 250], [P[0] + (b[0] < 960 ? -120 : 120), P[1] - 40], s, 80); circle(ctx, pt[0], pt[1], 13, '#e3c35c', 4); }
  });
  banks.forEach((b, i) => { const k = sp(t, 25.2 + i * 0.12, SPRING.bouncy); if (k > 0) bank(ctx, b[0], b[1], 0.95 * k + 0.0001, ['BANK A', 'BANK B', 'BANK C', 'BANK D'][i]); });
  const kp = sp(t, 25.05, SPRING.bouncy);
  if (kp > 0) phone(ctx, P[0], P[1] + (1 - kp) * 300, 2.3 * Math.max(0.01, kp), 0, (c) => {
    c.fillStyle = C.ink; c.font = font(46, 400, DISPLAY); c.textAlign = 'center'; c.fillText('UPI', 0, -30);
    c.font = font(9, 700, UI); c.fillStyle = C.grey; c.fillText('ANY BANK → ANY BANK', 0, -6);
    const kk = ez(t, 29.3, 29.8, E.outBack); if (kk > 0) tick(c, 0, 40, 24, kk);
  });
  ctx.restore();
  // header + stamp
  const kh = sp(t, 24.95, SPRING.snappy);
  if (kh > 0) { ctx.save(); ctx.globalAlpha = clamp(kh); ctx.translate(0, (1 - clamp(kh)) * -80); outlined(ctx, 'APRIL 2016', 960, 170, 110, C.white, C.ink, 'center'); ctx.restore(); }
  stamp(ctx, '₹0 FEE', 1560, 300, 100, 0.1, sp(t, 30.25, SPRING.bouncy));
  const ks = sp(t, 29.6, SPRING.snappy);
  if (ks > 0) { ctx.save(); ctx.translate(lerp(-500, 0, clamp(ks)), 0); pill(ctx, 'IN SECONDS', 150, 300, 44, C.white, C.ink, 'left'); ctx.restore(); }
}

// ------------------------------------------------------------------ S7 nobody cared, then 8 Nov (31.6 - 39.5)
function s7(ctx, t) {
  paperBg(ctx);
  const sh = Math.max(0, 1 - (t - 34.45) / 0.35) * (t > 34.45 ? 1 : 0);
  ctx.save(); ctx.translate(noise1(t * 60, 2) * 22 * sh, noise1(t * 60, 7) * 22 * sh);
  // flat usage chart (first sentence), slides away when the calendar lands
  const away = ez(t, 34.3, 34.8, E.inBack);
  ctx.save(); ctx.translate(0, away * -900);
  const kc = sp(t, 31.75, SPRING.snappy);
  if (kc > 0) {
    const x0 = 360, x1 = 1560, y0 = 780, y1 = 260;
    line(ctx, [[x0, y1], [x0, y0], [x1, y0]], 7, C.ink);
    ctx.fillStyle = C.ink; ctx.font = font(34, 700, UI); ctx.textAlign = 'left'; ctx.fillText('UPI payments, 2016', x0 + 20, y1 + 10);
    const k = ez(t, 32.0, 33.4, E.linear); const pts = [];
    for (let i = 0; i <= 60 * k; i++) { const s = i / 60; pts.push([lerp(x0, x1, s), y0 - 18 - s * 22 - Math.abs(noise1(s * 12, 4)) * 10]); }
    if (pts.length > 1) line(ctx, pts, 9, C.red);
    if (t > 32.8) { const kk = sp(t, 32.8, SPRING.bouncy); ctx.save(); ctx.translate(1200, 600); ctx.scale(kk, kk); pill(ctx, 'BARELY USED', 0, 0, 40, C.white, C.ink); ctx.restore(); }
  }
  ctx.restore();
  // calendar slam
  const kd = clamp(sp(t, 34.1, { stiffness: 420, damping: 22 }));
  if (t > 34.1) {
    const y = lerp(-500, 0, kd);
    ctx.save(); ctx.translate(960, 470 + y); ctx.rotate(-0.04);
    rrect(ctx, -230, -250, 460, 480, 24); ctx.fillStyle = C.white; ctx.fill(); ctx.lineWidth = 7; ctx.strokeStyle = C.ink; ctx.stroke();
    ctx.save(); rrect(ctx, -230, -250, 460, 120, 24); ctx.clip(); ctx.fillStyle = C.red; ctx.fillRect(-230, -250, 460, 120); ctx.restore();
    line(ctx, [[-230, -130], [230, -130]], 7, C.ink);
    for (const rx of [-120, 120]) { ctx.beginPath(); rrect(ctx, rx - 12, -280, 24, 70, 12); ctx.fillStyle = C.grey; ctx.fill(); ctx.stroke(); }
    ctx.fillStyle = C.white; ctx.font = font(80, 400, DISPLAY); ctx.textAlign = 'center'; ctx.fillText('NOV 2016', 0, -160);
    ctx.fillStyle = C.ink; ctx.font = font(300, 400, DISPLAY); ctx.fillText('8', 0, 170);
    ctx.restore();
  }
  // notes cancelled
  [[500, 360, 640, -0.12, 35.5, 36.35], [1000, 1560, 640, 0.1, 35.8, 37.25]].forEach(([v, x, y, r, tin, tx]) => {
    const k = sp(t, tin, SPRING.bouncy); if (k <= 0) return;
    const fall = ez(t, 38.5, 39.3, E.inCubic);
    note(ctx, x, y + (1 - clamp(k)) * 600 + fall * 700, 1.5 * Math.max(0.01, k), r + fall * 0.8, v, { dead: ez(t, tx, tx + 0.45, E.outCubic) });
  });
  const kn = sp(t, 38.6, SPRING.snappy);
  if (kn > 0) { ctx.save(); ctx.translate(960, 1000 + (1 - clamp(kn)) * 200); pill(ctx, 'OVERNIGHT', 0, 0, 46, C.red, C.white); ctx.restore(); }
  ctx.restore();
}

// ------------------------------------------------------------------ S8 86% (39.5 - 43.0)
function s8(ctx, t) {
  darkBg(ctx);
  const k = ez(t, 39.75, 41.5, E.outCubic), n = Math.round(86 * k);
  const kin = sp(t, 39.6, SPRING.bouncy);
  ctx.save(); ctx.translate(560, 640); const s = lerp(0.6, 1, clamp(kin)); ctx.scale(s, s);
  outlined(ctx, n + '%', 0, 0, 380, C.white, '#11141a', 'center', 0.05);
  ctx.fillStyle = '#c9ced6'; ctx.font = font(44, 700, UI); ctx.textAlign = 'center'; ctx.fillText("of India's cash", 0, 90);
  ctx.restore();
  // stack of 10 notes; top ones go dead as the count climbs
  for (let i = 0; i < 10; i++) {
    const ki = sp(t, 39.6 + i * 0.05, SPRING.snappy); if (ki <= 0) continue;
    const dead = clamp((k * 8.6 - (9 - i)) * 1.0);
    note(ctx, 1380 + (i % 2 ? 14 : -10), 880 - i * 62 - (1 - clamp(ki)) * 400, 1.25, (i % 3 - 1) * 0.04, i % 2 ? 500 : 1000, { color: dead > 0.5 ? '#6a6f78' : null });
  }
  // crash line
  const kl = ez(t, 41.3, 42.4, E.inOutCubic);
  if (kl > 0) {
    const pts = [[120, 200], [420, 280], [560, 230], [860, 520], [1000, 460], [1300, 800], [1500, 760], [1820, 1000]];
    const L = pts.length - 1, m = kl * L, i = Math.floor(m), f = m - i;
    const p = pts.slice(0, i + 1); if (i < L) p.push([lerp(pts[i][0], pts[i + 1][0], f), lerp(pts[i][1], pts[i + 1][1], f)]);
    line(ctx, p, 22, '#11141a'); line(ctx, p, 12, C.red);
  }
}

// ------------------------------------------------------------------ S9 skit: scan the code (43.0 - 46.6)
function s9(ctx, t) {
  const lt = t - 43.0;
  ctx.save(); zoomAt(ctx, logZ(1.45, 1.52, ez(lt, 0, 3.6, E.inOutSine)), 1000, 520, 960, 500);
  const point = sp(t, 44.75, SPRING.snappy);
  const { qrPos } = street(ctx, t, { raju: { expr: t > 44.75 ? 'smug' : 'neutral', mouth: mouthOf(t, ['v2']), arms: [[0.15, 0.2], [lerp(0.15, 1.75, point), lerp(0.2, 0.25, point)]], look: point > 0.5 ? 1 : -1, face: point > 0.5 ? 0.4 : -0.5 }, cartX: 1260, qrGlow: point > 0.5 ? 0.7 : 0 });
  const lift = sp(t, 45.45, SPRING.snappy);
  const Mn = person(ctx, 'meena', 700, GROUND + 140, 0.95, { expr: t > 45.6 ? 'smile' : 'worried', mouth: mouthOf(t, ['c2']), arms: [[0.15, 0.2], [lerp(0.15, 0.55, lift), lerp(0.2, 1.9, lift)]], face: 0.7, look: 1, blink: blinkAt(t, [43.9]) });
  if (lift > 0) phone(ctx, Mn.rhand[0] + 10, Mn.rhand[1] - 70, 0.75, 0.15, (c) => { const kk = ez(t, 46.05, 46.35, E.outBack); if (kk > 0) tick(c, 0, -10, 30, kk); else { c.strokeStyle = C.red; c.lineWidth = 4; c.strokeRect(-30, -40, 60, 60); } });
  ctx.restore();
}

// ------------------------------------------------------------------ S10 no choice, stickers everywhere (46.6 - 51.7)
function s10(ctx, t) {
  if (t < 48.75) {   // a crowd lifting phones, ticks popping
    paperBg(ctx);
    const who = ['arjun', 'meena', 'raju'];
    const rnd = mulberry32(21);
    for (let row = 0; row < 2; row++) for (let i = 0; i < 9; i++) {
      const x = 120 + i * 210 + (row ? 105 : 0), y = 700 + row * 300, s = 0.42 + row * 0.08;
      const w = who[(i + row * 2) % 3], t0 = 46.75 + hash01(i + row * 9, 4) * 1.3;
      const k = sp(t, t0, SPRING.bouncy);
      const P = person(ctx, w, x, y, s, { expr: k > 0.5 ? 'smile' : 'worried', arms: [[0.15, 0.2], [lerp(0.15, 0.55, clamp(k)), lerp(0.2, 1.9, clamp(k))]], blink: blinkAt(t, [47.3 + i * 0.1]) });
      if (k > 0) { phone(ctx, P.rhand[0] + 4, P.rhand[1] - 34, 0.32, 0.1); const kt = ez(t, t0 + 0.3, t0 + 0.6, E.outBack); if (kt > 0) tick(ctx, P.rhand[0] + 4, P.rhand[1] - 110, 24, kt); }
    }
    const kh = sp(t, 46.8, SPRING.snappy);
    if (kh > 0) { ctx.save(); ctx.translate(960, 150 + (1 - clamp(kh)) * -200); pill(ctx, 'NO CASH? NO CHOICE.', 0, 0, 52, C.red, C.white); ctx.restore(); }
  } else {           // a street of stalls, a QR sticker lands on each
    ctx.save(); zoomAt(ctx, logZ(1.0, 1.08, ez(t, 48.75, 51.7, E.inOutSine)), 960, 560);
    city(ctx, W, H, GROUND - 40, { pan: 900 });
    const stalls = 6;
    for (let i = 0; i < stalls; i++) {
      const x = 170 + i * 316, y = GROUND + 40 + (i % 2) * 40;
      cart(ctx, x, y, 0.5, { showQR: false, sign: false });
      const k = sp(t, 49.0 + i * 0.28, SPRING.bouncy);
      if (k > 0) { ctx.save(); ctx.translate(x + 75, y - 165); ctx.rotate((1 - clamp(k)) * 1.5); qr(ctx, 0, (1 - clamp(k)) * -400, 66 * Math.max(0.05, k)); ctx.restore(); }
    }
    ctx.restore();
    stamp(ctx, '₹0 TO PRINT', 960, 230, 120, -0.05, sp(t, 50.3, SPRING.bouncy));
  }
}

// ------------------------------------------------------------------ S11 20 billion a month, back to Raju (51.7 - 58.2)
function s11(ctx, t) {
  if (t < 55.85) {
    darkBg(ctx);
    const x0 = 200, x1 = 1720, y0 = 900, y1 = 420;
    line(ctx, [[x0, y0], [x1, y0]], 5, '#8a92a0');
    ctx.fillStyle = '#c9ced6'; ctx.font = font(36, 700, UI); ctx.textAlign = 'left'; ctx.fillText('2016', x0, y0 + 56); ctx.textAlign = 'right'; ctx.fillText('TODAY', x1, y0 + 56);
    const k = ez(t, 52.0, 55.0, E.inOutSine); const pts = [];
    for (let i = 0; i <= 80 * k; i++) { const s = i / 80; pts.push([lerp(x0, x1, s), y0 - (s ** 2.4) * (y0 - y1) - noise1(s * 14, 3) * 14 * s]); }
    if (pts.length > 1) { line(ctx, pts, 22, '#11141a'); line(ctx, pts, 12, C.red); const e = pts[pts.length - 1]; circle(ctx, e[0], e[1], 16, C.red, 5); }
    const n = Math.max(1, Math.round(20 * ez(t, 52.0, 54.6, E.outCubic)));
    const kin = sp(t, 51.8, SPRING.bouncy);
    ctx.save(); ctx.translate(200, 330); const s = lerp(0.7, 1, clamp(kin)); ctx.scale(s, s);
    outlined(ctx, `${n} BILLION+`, 0, 0, 200, C.white, '#11141a', 'left', 0.05);
    ctx.fillStyle = '#c9ced6'; ctx.font = font(48, 700, UI); ctx.textAlign = 'left'; ctx.fillText('UPI payments every month', 6, 80);
    ctx.restore();
  } else {
    const p = ez(t, 56.5, 58.2, E.inCubic);
    const qrp = [1180 + 150, GROUND + 140 - 330];
    const z = logZ(1.0, 9.5, p);
    ctx.save(); zoomAt(ctx, z, qrp[0], qrp[1], lerp(qrp[0], 960, p), lerp(qrp[1], 540, p));
    street(ctx, t, { raju: { expr: 'smile', look: 1, arms: [[0.15, 0.2], [lerp(0.15, 1.7, sp(t, 56.0, SPRING.snappy)), 0.25]] }, qrGlow: 0.7 });
    ctx.restore();
  }
}

// ------------------------------------------------------------------ S12 end card (58.2 - 60)
function s12(ctx, t) {
  paperBg(ctx, C.white);
  const k = sp(t, 58.2, SPRING.bouncy);
  person(ctx, 'raju', 1500, 1120 + (1 - clamp(k)) * 400, 1.12, { expr: 'smile', blink: blinkAt(t, [59.3]), arms: [[0.15, 0.2], [2.5 + 0.22 * Math.sin((t - 58.2) * 11), 0.5]] });
  qr(ctx, 1040, 560, 260 * Math.max(0.01, clamp(sp(t, 58.4, SPRING.bouncy))));
  ctx.save(); ctx.translate(140, 520); const s = lerp(1.3, 1, clamp(k)); ctx.scale(s, s); outlined(ctx, 'UPI', 0, 0, 300); ctx.restore();
  const k2 = sp(t, 58.45, SPRING.snappy);
  if (k2 > 0) { ctx.save(); ctx.translate(lerp(-900, 0, clamp(k2)), 0); pill(ctx, "EXPLAINED LIKE YOU'RE 5", 148, 620, 46, C.red, C.white, 'left'); ctx.restore(); }
}

// ------------------------------------------------------------------ edit
const SHOTS = [
  [0, s1], [7.5, s2], [10.4, s3], [14.95, s4], [19.95, s5], [24.8, s6], [31.6, s7], [39.5, s8], [43.0, s9], [46.6, s10], [51.7, s11], [58.2, s12],
];
// whip pans (both shots on screen) at these cuts; others are hard cuts on the downbeat
const WHIPS = { 14.95: 0.38, 19.95: 0.38, 24.8: 0.4, 43.0: 0.38, 51.7: 0.4 };
function shotAt(t) { let i = 0; while (i + 1 < SHOTS.length && t >= SHOTS[i + 1][0]) i++; return i; }
function drawShot(ctx, i, t) { ctx.save(); SHOTS[i][1](ctx, t); ctx.restore(); }

function captions(ctx, t) {
  for (const r of VO) {
    if (t < r.start - 0.05 || t > r.end + 0.25) continue;
    const parts = CAPTEXT[r.key]; if (!parts) return;
    const tot = parts.reduce((a, p) => a + p.length, 0);
    let acc = 0, cur = parts[parts.length - 1];
    for (const p of parts) { const a = r.start + (acc / tot) * (r.end - r.start); acc += p.length; const b = r.start + (acc / tot) * (r.end - r.start); if (t >= a - 0.05 && t < b) { cur = p; break; } }
    const quote = r.key[0] !== 'n';
    ctx.font = font(quote ? 46 : 44, quote ? 700 : 600, UI);
    const w = ctx.measureText(cur).width;
    rrect(ctx, W / 2 - w / 2 - 28, H - 128, w + 56, 74, 16); ctx.fillStyle = 'rgba(20,22,28,.78)'; ctx.fill();
    ctx.fillStyle = quote ? '#ffd9d9' : C.white; ctx.textAlign = 'center'; ctx.fillText(cur, W / 2, H - 77);
    return;
  }
}

const HITS_S = [
  [0, 'title slam', 'impact'], [0.35, 'subtitle', 'whoosh', { len: 0.3 }], [2.9, 'title out', 'whoosh', { len: 0.35, from: 2400, to: 600 }],
  [3.6, 'phone in', 'whoosh', { len: 0.3 }], [4.85, 'paid', 'bell', { pitch: 'A5' }],
  [7.5, 'pull back', 'whoosh', { len: 0.5, from: 2000, to: 500 }], [8.0, 'cash pile', 'coins'], [8.9, 'question', 'pop', { pitch: 'E5' }], [9.75, 'notes fly', 'whoosh', { len: 0.6 }],
  [10.55, '2016 stamp', 'thud'], [11.2, 'chai', 'tick'], [12.3, 'rickshaw', 'tick'], [13.4, 'rent', 'tick'],
  [14.95, 'whip', 'whoosh', { len: 0.38 }], [15.05, 'note offered', 'pop', { pitch: 'C6' }], [17.15, 'shrug', 'boing', { pitch: 'G4', to: 'C4' }],
  [19.95, 'whip', 'whoosh', { len: 0.38 }], [20.15, 'card machine', 'pop', { pitch: 'A5' }], [21.75, 'bank', 'thud'], [22.6, 'cut', 'coins'], [23.25, 'cash only', 'pop', { pitch: 'D5' }],
  [24.8, 'whip', 'whoosh', { len: 0.4 }], [25.05, 'phone', 'pop', { pitch: 'D6' }], [26.9, 'line 1', 'tok', { pitch: 'D5' }], [27.35, 'line 2', 'tok', { pitch: 'F5' }], [27.8, 'line 3', 'tok', { pitch: 'A5' }], [28.25, 'line 4', 'tok', { pitch: 'C6' }], [28.7, 'line 5', 'tok', { pitch: 'D6' }],
  [29.55, 'in seconds', 'blip', { pitch: 'A6' }], [30.25, 'zero fee', 'thud'],
  [31.6, 'chart', 'click'], [32.8, 'barely used', 'pop', { pitch: 'C5' }], [34.45, 'calendar slam', 'impact'], [36.35, 'X 500', 'thud+click'], [37.25, 'X 1000', 'thud+click'], [38.6, 'overnight', 'whoosh', { len: 0.4 }],
  [39.5, '86 in', 'sub', { len: 0.6 }], [41.3, 'crash', 'riser', { len: 0.4 }],
  [43.0, 'whip', 'whoosh', { len: 0.38 }], [44.75, 'point', 'pop', { pitch: 'G5' }], [46.15, 'paid', 'bell', { pitch: 'D6' }],
  [46.6, 'crowd', 'click'], [47.4, 'ticks', 'blip', { pitch: 'E6' }], [48.0, 'ticks', 'blip', { pitch: 'A6' }], [48.75, 'stalls', 'whoosh', { len: 0.3 }],
  [49.0, 'qr 1', 'pop', { pitch: 'C5' }], [49.56, 'qr 3', 'pop', { pitch: 'E5' }], [50.12, 'qr 5', 'pop', { pitch: 'G5' }], [50.3, 'zero to print', 'thud'],
  [51.7, 'whip', 'whoosh', { len: 0.4 }], [52.0, 'counter', 'riser', { len: 2.6 }], [54.6, '20 billion', 'bell', { pitch: 'A5' }],
  [55.85, 'back to raju', 'click'], [57.4, 'push in', 'swell'], [58.2, 'end card', 'impact'], [58.45, 'subtitle', 'bell', { pitch: 'D6' }],
];
const HITS = HITS_S.map(([s, l, sfx, o]) => [Math.round(B(s) * 1000) / 1000, l, sfx, o].filter((x) => x !== undefined));

M.film({
  fonts: [font(100, 400, DISPLAY), font(40, 800, UI), font(40, 600, UI)],
  hits: HITS,
  samples: 6,
  async init() {
    VO = await fetch('vo_timeline.json').then((r) => r.json());
    LIP = await fetch('lipsync.json').then((r) => r.json());
  },
  draw(ctx, u, t) {
    fill(ctx, C.paper);
    const i = shotAt(t);
    // whip window around a cut: outgoing slides left while incoming slides in from the right
    for (const [tc, d] of Object.entries(WHIPS)) {
      const c = Number(tc);
      if (t >= c - d / 2 && t < c + d / 2) {
        const p = E.inOutCubic((t - (c - d / 2)) / d), a = shotAt(c - 0.001), b = shotAt(c + 0.001);
        const edge = (1 - p) * W;
        ctx.save(); ctx.beginPath(); ctx.rect(0, 0, edge, H); ctx.clip(); ctx.translate(-p * W, 0); drawShot(ctx, a, Math.min(t, c - 0.001)); ctx.restore();
        ctx.save(); ctx.beginPath(); ctx.rect(edge, 0, W - edge, H); ctx.clip(); ctx.translate(edge, 0); drawShot(ctx, b, Math.max(t, c)); ctx.restore();
        line(ctx, [[edge, 0], [edge, H]], 10, C.ink);
        captions(ctx, t);
        return;
      }
    }
    drawShot(ctx, i, t);
    captions(ctx, t);
  },
});
