"""Build /workspace/pages/health-coaching/page.html (self-contained, paste into the GHL custom-code block).
Edit page.body.html (markup), page.css (graphics CSS), the lists below, or ../_shared/*; then run: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ) so they always match."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from common import *

SLUG = "health-coaching"
# Verbatim from /workspace/homepage/seo-meta.md (title is 62 chars: see NOTES.md, compliance/SEO flag 1)
TITLE = "Health Coaching for Men with Low-T Symptoms | Odin Health Lab"
DESC = "One-on-one health coaching for men with fatigue, low drive and belly fat: sleep, stress, training and nutrition steps you can track. Canada and USA."
OG_ALT = "Odin Health Lab: one-on-one health coaching for men with low testosterone symptoms, Canada and USA"
assert len(DESC) <= 160

FAQ = [
  ("Is health coaching medical care?",
  "Coaching is practical, day-to-day support with sleep, stress, training and nutrition habits, and it works alongside your medical care. We can help you prepare questions for appointments, keep track of what you\u2019ve noticed and share your plan with your doctor if you choose."),
  ("What can coaching do for low-T symptoms?",
  "Coaching helps with the habits that are part of how many men feel day to day: sleep, stress, training and eating. Your coach builds a plan around your pattern, helps you track it and adjusts it at every check-in. To find out whether low testosterone is part of your picture, we can walk you through which blood tests are worth asking about."),
  ("How does coaching work with my doctor?",
  "Coaching works alongside your doctor. We can help you prepare for appointments, keep track of what you\u2019ve noticed and share your plan and tracking with your doctor if you choose. We also factor in anything your doctor changes along the way."),
 ("What happens on the first call?",
  "A private video or phone call to go through your symptoms, your routine, your sleep, training and eating, any medications and what you\u2019ve already tried. Together we pick the first one or two steps and agree what you will track, so you can see for yourself whether the plan is working."),
  ("How quickly will I notice a difference?",
  "It depends on what is behind your symptoms and on how the steps fit your life. What you get is a clear plan, a way to track it and regular check-ins to adjust it."),
 ("Is it fully online, and where do you work with men?",
  'Yes. Odin Health Lab is telehealth only and serves men across Canada and the USA. Everything happens by secure video, phone and message, so there are no clinic visits. See our <a href="%s/">low testosterone and andropause overview</a> for how the service works, or read our <a href="%s/privacy">Privacy Policy</a> for how we protect your information.' % (SITE, SITE)),
]

# ---------- 1 · HERO: a staircase of five steps, a dot hops up step by step ----------
def hero_stairs():
    names = ["sleep", "stress", "train", "food", "check"]
    s = ['<defs><linearGradient id="hs-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.16"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0.02"/></linearGradient></defs>']
    s.append('<path d="M20 278H460" stroke="rgba(255,255,255,0.18)" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/>')
    tops, cxs = [], []
    for i in range(5):
        x = 40 + i * 80; top = 232 - i * 34; cx = x + 40
        tops.append(top); cxs.append(cx)
        s.append('<rect x="%d" y="%d" width="80" height="%d" fill="url(#hs-g)"/>' % (x, top, 278 - top))
        s.append('<path d="M%d %d V%d" stroke="rgba(196,255,73,0.18)" stroke-width="2"/>' % (x + 80, top, 278) if i < 4 else '')
    path = "M40 278V232H120V198H200V164H280V130H360V96H440V278"
    s.append('<path d="%s" fill="none" stroke="rgba(196,255,73,0.22)" stroke-width="4" stroke-linejoin="round"/>' % path)
    s.append('<path class="dr" pathLength="1" style="--d:0.1;--dur:2s" d="M40 232H120V198H200V164H280V130H360V96H440" fill="none" stroke="#c4ff49" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
    for i in range(5):
        s.append('<g class="hs-n pop t" style="--d:%.2f;--k:%d"><circle cx="%d" cy="%d" r="19" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/><circle class="hs-lit" cx="%d" cy="%d" r="19" fill="none" stroke="#fff" stroke-width="3.5"/>%s</g>'
                 % (0.5 + i * 0.18, i, cxs[i], tops[i] + 42, cxs[i], tops[i] + 42, ico(names[i], cxs[i], tops[i] + 42, 22, "#c4ff49", 1.8)))
    # flag on the top step
    s.append('<g class="pop t" style="--d:1.6"><path d="M424 96V62" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M424 62h22l-6 8 6 8h-22z" fill="#c4ff49"/></g>')
    # the hopper: outer group moves (x,y linear), inner group does the hop arc
    s.append('<g class="hs-dot"><g class="hs-hop"><circle r="8" fill="#fff"/><circle r="13" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="2"/></g></g>')
    # keyframes for the dot are generated here (positions are data)
    pts = [(cxs[i] - 18, tops[i] - 14) for i in range(5)]
    def tr(p): return "translate(%dpx,%dpx)" % p
    kf = ["0%% { transform: %s; opacity: 0; }" % tr(pts[0]),
          "4%% { transform: %s; opacity: 1; }" % tr(pts[0]),
          "14%% { transform: %s; }" % tr(pts[0]), "20%% { transform: %s; }" % tr(pts[1]),
          "34%% { transform: %s; }" % tr(pts[1]), "40%% { transform: %s; }" % tr(pts[2]),
          "54%% { transform: %s; }" % tr(pts[2]), "60%% { transform: %s; }" % tr(pts[3]),
          "74%% { transform: %s; }" % tr(pts[3]), "80%% { transform: %s; }" % tr(pts[4]),
          "94%% { transform: %s; opacity: 1; }" % tr(pts[4]), "100%% { transform: %s; opacity: 0; }" % tr(pts[4])]
    css_final = ".pg .hs-dot { transform: %s; }\n" % tr(pts[4])
    css_kf = "@keyframes hs-move {\n  %s\n}\n" % "\n  ".join(kf)
    open(os.path.join(HERE, "gen.hero.css"), "w").write(css_final + "/*@motion*/\n" + css_kf)
    return "\n".join(x for x in s if x)

# ---------- 2 · SYMPTOMS: three small scenes (battery, flame, moon) ----------
def symptoms_scene():
    s = []
    for i, x in enumerate((20, 200, 380)):
        s.append('<rect class="pop" style="--d:%.2f" x="%d" y="14" width="160" height="150" rx="18" fill="rgba(255,255,255,0.03)" stroke="rgba(196,255,73,0.22)" stroke-width="1.5"/>' % (0.1 + i * 0.12, x))
    # battery
    s.append('<g class="pop" style="--d:0.3"><rect x="62" y="64" width="74" height="46" rx="9" fill="none" stroke="#fff" stroke-width="3"/><rect x="138" y="76" width="7" height="22" rx="3" fill="#fff"/>'
             '<rect class="sy-chg" x="68" y="70" width="62" height="34" rx="5" fill="#c4ff49" fill-opacity="0.85"/>'
             '<path class="sy-bolt" d="M104 70l-12 20h9l-4 14 14-22h-9z" fill="#0f240f"/></g>')
    s.append('<path class="dr" pathLength="1" style="--d:0.8" d="M60 130h80" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-linecap="round" stroke-dasharray="1 3"/>')
    # flame
    s.append('<g class="pop" style="--d:0.45"><g transform="translate(290 112)"><g class="sy-flame"><path d="M0 -50 C 10 -28 32 -20 32 6 A32 32 0 0 1 -32 6 C -32 -8 -22 -16 -14 -26 C -10 -12 -4 -12 0 -50Z" fill="#c4ff49" fill-opacity="0.2" stroke="#c4ff49" stroke-width="3" stroke-linejoin="round"/>'
             '<path d="M0 -14 C 6 -4 14 0 14 12 A14 14 0 0 1 -14 12 C -14 4 -6 0 0 -14Z" fill="#c4ff49"/></g></g></g>')
    for k, (ex, ey) in enumerate(((278, 72), (300, 66), (318, 78))):
        s.append('<circle class="sy-ember" style="--k:%d" cx="%d" cy="%d" r="2.6" fill="#c4ff49"/>' % (k, ex, ey))
    # moon + stars + z
    s.append('<g class="pop" style="--d:0.6"><path class="sy-moon" d="M498 58 A38 38 0 1 0 520 120 A30 30 0 0 1 498 58Z" fill="rgba(255,255,255,0.1)" stroke="#fff" stroke-width="3" stroke-linejoin="round"/></g>')
    for k, (sx, sy, r) in enumerate(((416, 52, 3.2), (536, 46, 2.6), (545, 96, 2.2))):
        s.append('<circle class="sy-star" style="--k:%d" cx="%d" cy="%d" r="%s" fill="#c4ff49"/>' % (k, sx, sy, r))
    s.append('<g class="sy-z" style="--k:0" fill="none" stroke="#c4ff49" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M528 70h12l-12 14h12"/></g>')
    s.append('<g class="sy-z" style="--k:1" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M548 52h8l-8 10h8"/></g>')
    return "\n".join(s)

# ---------- 3 · PROTOCOL vs generic: scattered tips drift, sequenced steps slide into place ----------
def scatter_seq():
    s = ['<path d="M280 24V226" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="3 8" stroke-linecap="round"/>']
    s.append('<path d="M50 190c40-70 20-120 70-130s90 50 120 20-10-60-40-30" fill="none" stroke="rgba(157,179,157,0.28)" stroke-width="2" stroke-dasharray="2 7" stroke-linecap="round"/>')
    chips = [(44, 40, 70, -8, 14, -10, 6.2), (150, 34, 62, 6, -18, 12, 7.4), (88, 96, 76, 4, 16, 8, 5.6),
             (172, 118, 66, -10, -12, -14, 8.0), (46, 160, 64, 8, 18, -8, 6.8), (138, 176, 74, -4, -16, 10, 7.0)]
    for k, (x, y, w, r, dx, dy, p) in enumerate(chips):
        s.append('<g class="sc-chip" style="--k:%d;--dx:%dpx;--dy:%dpx;--r:%ddeg;--p:%ss"><g transform="translate(%d %d) rotate(%d)"><rect width="%d" height="24" rx="12" fill="#142e14" stroke="#9db39d" stroke-width="2" stroke-dasharray="3 4"/><circle cx="14" cy="12" r="3.4" fill="#9db39d"/></g></g>' % (k, dx, dy, r * 2, p, x, y, r, w))
    # sequenced rows
    for k in range(6):
        y = 34 + k * 31
        w = [150, 120, 138, 110, 128, 100][k]
        s.append('<g class="sc-row" style="--k:%d"><rect x="318" y="%d" width="%d" height="24" rx="12" fill="rgba(196,255,73,0.14)" stroke="#c4ff49" stroke-width="2"/><circle cx="332" cy="%d" r="3.4" fill="#c4ff49"/><path d="M346 %dh%d" stroke="rgba(255,255,255,0.7)" stroke-width="2.4" stroke-linecap="round"/></g>' % (k, y, w, y + 12, y + 12, w - 50))
        s.append('<g class="sc-tick t" style="--k:%d"><circle cx="500" cy="%d" r="10" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/><path d="M495 %dl3.6 3.6L505 %d" fill="none" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></g>' % (k, y + 12, y + 12, y + 9))
    s.append('<path class="dr" pathLength="1" style="--d:0.3" d="M500 24V224" stroke="rgba(196,255,73,0.0)" stroke-width="2"/>')
    return "\n".join(s)

# ---------- 4 · FIVE PILLARS: a habit-tracker grid (5 pillars x 7 days) that fills in across the week ----------
def habit_grid():
    names = ["sleep", "stress", "train", "food", "check"]
    on = ["1111011", "0110110", "1010100", "1101101", "1111110"]
    s = ['<rect class="hb-sweep" x="95" y="12" width="46" height="216" rx="14" fill="rgba(196,255,73,0.10)" stroke="rgba(196,255,73,0.45)" stroke-width="1.5"/>']
    for r in range(5):
        y = 34 + r * 42
        s.append('<g class="pop t" style="--d:%.2f"><circle cx="42" cy="%d" r="19" fill="#0f240f" stroke="rgba(196,255,73,0.6)" stroke-width="2"/>%s</g>' % (0.1 + r * 0.1, y, ico(names[r], 42, y, 22, "#c4ff49", 1.7)))
        s.append('<path d="M72 %dH530" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>' % y)
        for c in range(7):
            x = 118 + c * 60
            s.append('<circle cx="%d" cy="%d" r="12" fill="none" stroke="rgba(255,255,255,0.18)" stroke-width="2"/>' % (x, y))
            if on[r][c] == "1":
                s.append('<g class="hb-dot t" style="--c:%d;--r:%d"><circle cx="%d" cy="%d" r="9" fill="#c4ff49"/><path d="M%d %dl3.2 3.2L%d %d" fill="none" stroke="#0f240f" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></g>' % (c, r, x, y, x - 4, y, x + 5, y - 3.5))
    return "\n".join(s)

# ---------- 5 · WEEKLY CHECK-IN: a dial with a sweeping hand; seven day dots light as it passes ----------
def checkin_dial():
    cx, cy, R = 220, 130, 96
    def p(a, r=R):
        a = math.radians(a); return cx + r * math.sin(a), cy - r * math.cos(a)
    s = ['<defs><linearGradient id="ck-w" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c4ff49" stop-opacity="0"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0.38"/></linearGradient></defs>',
         '<circle cx="220" cy="130" r="112" fill="none" stroke="rgba(196,255,73,0.15)" stroke-width="1.5" stroke-dasharray="2 8" stroke-linecap="round"/>',
         '<circle cx="220" cy="130" r="96" fill="#0f240f" stroke="rgba(196,255,73,0.5)" stroke-width="2.5"/>',
         '<circle cx="220" cy="130" r="66" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>']
    for k in range(28):
        a = k * 360 / 28; x0, y0 = p(a, 90); x1, y1 = p(a, 86 if k % 4 else 82)
        s.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="rgba(255,255,255,%s)" stroke-width="2" stroke-linecap="round"/>' % (x0, y0, x1, y1, 0.3 if k % 4 else 0.5))
    x1, y1 = p(-38, 90)
    s.append('<g class="ck-hand"><path d="M220 130 L%.1f %.1f A90 90 0 0 1 220 40Z" fill="url(#ck-w)"/><path d="M220 130V38" stroke="#c4ff49" stroke-width="3.5" stroke-linecap="round"/></g>' % (x1, y1))
    for k in range(7):
        x, y = p(k * 360 / 7, 66)
        s.append('<g class="ck-dot t" style="--k:%d"><circle cx="%.1f" cy="%.1f" r="9" fill="#142e14" stroke="#c4ff49" stroke-width="2.5"/><circle cx="%.1f" cy="%.1f" r="4" fill="#c4ff49"/></g>' % (k, x, y, x, y))
    s.append('<circle cx="220" cy="130" r="22" fill="#0f240f" stroke="#fff" stroke-width="2.5"/>' + ico("you", 220, 130, 26, "#fff", 1.7))
    # chat bubbles either side
    s.append('<g class="ck-bub t" style="--k:0"><path d="M30 76h74a8 8 0 0 1 8 8v26a8 8 0 0 1-8 8H58l-14 12v-12H30a8 8 0 0 1-8-8V84a8 8 0 0 1 8-8z" fill="#142e14" stroke="#c4ff49" stroke-width="2.4"/><path d="M38 92h50M38 104h30" stroke="rgba(255,255,255,0.6)" stroke-width="3" stroke-linecap="round"/></g>')
    s.append('<g class="ck-bub t" style="--k:1"><path d="M340 142h70a8 8 0 0 1 8 8v26a8 8 0 0 1-8 8h-12v12l-14-12h-44a8 8 0 0 1-8-8v-26a8 8 0 0 1 8-8z" fill="#142e14" stroke="rgba(255,255,255,0.7)" stroke-width="2.4"/><path d="M350 158h50M350 170h32" stroke="rgba(196,255,73,0.8)" stroke-width="3" stroke-linecap="round"/></g>')
    return "\n".join(s)

# ---------- 6 · YOUR PROGRESS, SHARED: a bridge, a shared note crosses it both ways ----------
def bridge():
    s = ['<ellipse cx="280" cy="170" rx="250" ry="60" fill="url(#br-g)" opacity="0.5"/>' ]
    s.insert(0, '<defs><radialGradient id="br-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.18"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs>')
    s.append('<path d="M124 120H436" stroke="rgba(255,255,255,0.22)" stroke-width="3" stroke-linecap="round"/>')
    s.append('<path d="M124 120Q280 20 436 120" fill="none" stroke="rgba(196,255,73,0.2)" stroke-width="4"/>')
    s.append('<path class="dr" pathLength="1" style="--d:0.1;--dur:1.6s" d="M124 120Q280 20 436 120" fill="none" stroke="#c4ff49" stroke-width="4" stroke-linecap="round"/>')
    for i in range(1, 6):
        t = i / 6; x = 124 + 312 * t; y = 120 - 200 * t * (1 - t)
        s.append('<path class="dr" pathLength="1" style="--d:%.2f" d="M%.1f %.1fV120" stroke="rgba(196,255,73,0.35)" stroke-width="2" stroke-linecap="round"/>' % (0.6 + i * 0.1, x, y))
    s.append('<path d="M280 124V146" stroke="rgba(255,255,255,0.35)" stroke-width="2" stroke-dasharray="2 6" stroke-linecap="round"/>')
    s.append('<g class="pop t" style="--d:0.2"><circle class="br-ring" style="--k:0" cx="90" cy="120" r="34" fill="none" stroke="#c4ff49" stroke-width="2"/><circle cx="90" cy="120" r="34" fill="#0f240f" stroke="#c4ff49" stroke-width="2.6"/>%s</g>' % ico("coach", 90, 120, 34, "#c4ff49", 1.6))
    s.append('<g class="pop t" style="--d:0.35"><circle class="br-ring" style="--k:1" cx="470" cy="120" r="34" fill="none" stroke="#fff" stroke-width="2"/><circle cx="470" cy="120" r="34" fill="#0f240f" stroke="rgba(255,255,255,0.75)" stroke-width="2.6" stroke-dasharray="4 5"/>%s</g>' % ico("heart", 470, 120, 34, "#fff", 1.6))
    s.append('<g class="pop t" style="--d:0"><circle cx="280" cy="170" r="26" fill="#0f240f" stroke="#fff" stroke-width="2.6"/>%s</g>' % ico("you", 280, 170, 30, "#fff", 1.6))
    s.append('<g class="br-note"><g transform="translate(-11 -30)"><rect width="22" height="28" rx="4" fill="#142e14" stroke="#c4ff49" stroke-width="2.4"/><path d="M5 8h12M5 14h12M5 20h7" stroke="#fff" stroke-width="2" stroke-linecap="round"/></g></g>')
    # keyframes generated: outbound 0-40%, hold, return 50-90%
    def seg(p0, p1, rev):
        out = []
        n = 8
        for i in range(n + 1):
            t = i / n; tt = (1 - t) if rev else t
            x = 124 + 312 * tt; y = 120 - 200 * tt * (1 - tt)
            out.append("%.1f%% { transform: translate(%.1fpx,%.1fpx); }" % (p0 + (p1 - p0) * t, x, y))
        return out
    # opacity holds
    css = ".pg .br-note { transform: translate(280px,70px); }\n/*@motion*/\n@keyframes br-cross {\n  0% { opacity: 0; transform: translate(124px,120px); }\n  3% { opacity: 1; }\n  " + "\n  ".join(seg(0, 40, False)[1:]) + "\n  44% { opacity: 1; }\n  46% { opacity: 0; transform: translate(436px,120px); }\n  50% { opacity: 0; transform: translate(436px,120px); }\n  53% { opacity: 1; }\n  " + "\n  ".join(seg(50, 90, True)[1:]) + "\n  94% { opacity: 1; }\n  97%, 100% { opacity: 0; transform: translate(124px,120px); }\n}\n"
    open(os.path.join(HERE, "gen.bridge.css"), "w").write(css)
    return "\n".join(s)

# ---------- 7 · RELATED: three puzzle tiles slide together and lock ----------
def puzzle():
    s = ['<circle class="pz-ring" cx="280" cy="95" r="56" fill="none" stroke="#c4ff49" stroke-width="2"/>']
    items = [("labs", 150, "rgba(255,255,255,0.7)", 0), ("coach", 280, "#c4ff49", 1), ("caps", 410, "rgba(255,255,255,0.7)", 2)]
    for ic, x, col, k in items:
        fill = "rgba(196,255,73,0.14)" if k == 1 else "#0f240f"
        s.append('<g class="pz-tile" style="--k:%d"><g class="pop t" style="--d:%.2f"><rect x="%d" y="53" width="84" height="84" rx="20" fill="%s" stroke="%s" stroke-width="2.6"/>%s</g></g>' % (k, 0.1 + k * 0.12, x - 42, fill, "#c4ff49" if k == 1 else "rgba(255,255,255,0.7)", ico(ic, x, 95, 40, "#c4ff49" if k == 1 else "#fff", 1.7)))
    s.append('<circle class="pz-knob" style="--k:0" cx="215" cy="95" r="5" fill="#c4ff49"/><circle class="pz-knob" style="--k:1" cx="345" cy="95" r="5" fill="#c4ff49"/>')
    return "\n".join(s)

# ---------- 8 · FAQ: a speech bubble with a question mark; three typing dots ----------
FAQMOTIF = '''<g class="fq-bub"><path d="M22 14h76a12 12 0 0 1 12 12v32a12 12 0 0 1-12 12H58L40 86V70H22A12 12 0 0 1 10 58V26a12 12 0 0 1 12-12z" fill="rgba(196,255,73,0.07)" stroke="#c4ff49" stroke-width="3.5" stroke-linejoin="round"/>
<path class="dr" pathLength="1" style="--d:0.3;--dur:1.1s" d="M52 34c0-6 4-9 8-9s8 3 8 7c0 4-3 5-5 7-2 1.5-3 3-3 6" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="60" cy="58" r="2.6" fill="#fff"/></g>
<circle class="fq-dot" style="--k:0" cx="76" cy="90" r="3.2" fill="#c4ff49"/><circle class="fq-dot" style="--k:1" cx="88" cy="90" r="3.2" fill="#c4ff49"/><circle class="fq-dot" style="--k:2" cx="100" cy="90" r="3.2" fill="#c4ff49"/>'''

# ---------- 9 · FINAL: a door swings open, light spills out, footsteps lead in ----------
DOOR = '''<defs><linearGradient id="dor-g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.5"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></linearGradient></defs>
<rect x="126" y="28" width="104" height="146" rx="6" fill="#0a1c0a"/>
<g class="dor-light"><rect x="130" y="32" width="96" height="138" rx="4" fill="rgba(196,255,73,0.3)"/><path d="M226 38L350 4V196L226 166Z" fill="url(#dor-g)"/></g>
<path d="M30 176H330" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/>
<rect x="126" y="28" width="104" height="146" rx="6" fill="none" stroke="rgba(196,255,73,0.6)" stroke-width="3.5"/>
<g class="dor-panel"><rect x="130" y="32" width="96" height="138" rx="4" fill="#142e14" stroke="#c4ff49" stroke-width="3"/><rect x="142" y="46" width="30" height="42" rx="4" fill="none" stroke="rgba(196,255,73,0.45)" stroke-width="2"/><rect x="184" y="46" width="30" height="42" rx="4" fill="none" stroke="rgba(196,255,73,0.45)" stroke-width="2"/><circle cx="212" cy="108" r="5" fill="#fff"/></g>
<ellipse class="dor-fp" style="--k:0" cx="50" cy="176" rx="9" ry="4.5" fill="#c4ff49"/><ellipse class="dor-fp" style="--k:1" cx="78" cy="170" rx="9" ry="4.5" fill="#c4ff49"/><ellipse class="dor-fp" style="--k:2" cx="106" cy="176" rx="9" ry="4.5" fill="#c4ff49"/>'''

# ---------- step icons (How it works) ----------
def step_icons():
    return {
     "{{STEP1}}": '<rect x="6" y="8" width="36" height="8" rx="4"/><rect x="6" y="20" width="36" height="8" rx="4"/><rect x="6" y="32" width="36" height="8" rx="4"/><g class="hi-kn t" style="--k:0"><circle cx="16" cy="12" r="4.5" fill="#c4ff49" stroke="none"/></g><g class="hi-kn t" style="--k:1"><circle cx="32" cy="24" r="4.5" fill="#fff" stroke="none"/></g><g class="hi-kn t" style="--k:2"><circle cx="22" cy="36" r="4.5" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<rect x="5" y="9" width="38" height="28" rx="6"/><circle cx="24" cy="21" r="5" stroke="#fff"/><path d="M14 33c1.5-4 5-6 10-6s8.5 2 10 6" stroke="#fff"/><circle class="hi-live" cx="37" cy="14" r="2" fill="#c4ff49" stroke="none"/><path d="M16 42h16" /><path class="hi-wv" style="--k:0" d="M2 18c-1.5 2.5-1.5 6.5 0 9"/><path class="hi-wv" style="--k:1" d="M46 18c1.5 2.5 1.5 6.5 0 9"/>',
     "{{STEP3}}": '<rect x="8" y="6" width="32" height="36" rx="5"/><g class="hi-ck t" style="--k:0"><path d="M14 17l3 3 5-6" stroke="#fff"/></g><path d="M26 17h8" opacity="0.6"/><g class="hi-ck t" style="--k:1"><path d="M14 27l3 3 5-6" stroke="#fff"/></g><path d="M26 27h8" opacity="0.6"/><g class="hi-ck t" style="--k:2"><path d="M14 37l3 3 5-6" stroke="#fff"/></g><path d="M26 37h8" opacity="0.6"/>',
     "{{STEP4}}": '<g class="hi-cyc t"><path d="M38 20a15 15 0 0 0-26-6"/><path d="M12 6v8h8"/><path d="M10 28a15 15 0 0 0 26 6" stroke="#fff"/><path d="M36 42v-8h-8" stroke="#fff"/></g>',
    }

slots = {"{{HERO}}": hero_stairs(), "{{SYMPTOMS}}": symptoms_scene(), "{{SCATTER}}": scatter_seq(), "{{HABITS}}": habit_grid(),
         "{{DIAL}}": checkin_dial(), "{{BRIDGE}}": bridge(), "{{PUZZLE}}": puzzle(), "{{FAQMOTIF}}": FAQMOTIF, "{{DOOR}}": DOOR,
         "{{FAQ}}": faq_html(FAQ)}
slots.update(step_icons())
import re as _re
# {{CI:name:k}} placeholders in page.body.html
body = open(os.path.join(HERE, "page.body.html"), encoding="utf-8").read()
def _ci(m): return ci(m.group(1), int(m.group(2)))
open(os.path.join(HERE, ".body.expanded.html"), "w", encoding="utf-8").write(_re.sub(r"\{\{CI:(\w+):(\d+)\}\}", _ci, body))

ld = jsonld(SLUG, TITLE, DESC, "Health coaching for men with low testosterone (andropause) symptoms", "Health coaching", FAQ)
import shutil, tempfile
# assemble() reads page.body.html; use the expanded copy via a temp page dir view
tmp = os.path.join(HERE, ".tmp"); os.makedirs(tmp, exist_ok=True)
shutil.copy(os.path.join(HERE, ".body.expanded.html"), os.path.join(tmp, "page.body.html"))
css = open(os.path.join(HERE, "page.css"), encoding="utf-8").read()
# generated keyframes (positions are data): split static part and motion part
def gen(name):
    t = open(os.path.join(HERE, name)).read(); a, b = t.split("/*@motion*/\n"); return a, b
static_extra, motion_extra = "", ""
for n in ("gen.hero.css", "gen.bridge.css"):
    a, b = gen(n); static_extra += a; motion_extra += b
open(os.path.join(tmp, "page.css"), "w").write(css.replace("/*@GEN_STATIC*/", static_extra).replace("/*@GEN_MOTION*/", motion_extra))
import common
assemble(tmp, SLUG, TITLE, DESC, OG_ALT, ld, slots)
shutil.copy(os.path.join(tmp, "page.html"), os.path.join(HERE, "page.html"))
shutil.rmtree(tmp); os.remove(os.path.join(HERE, ".body.expanded.html"))
