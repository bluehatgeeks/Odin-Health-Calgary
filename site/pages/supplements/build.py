"""Build /workspace/pages/supplements/page.html (self-contained, paste into the GHL custom-code block).
Edit page.body.html (markup), page.css (graphics CSS), the lists below, or ../_shared/*; then run: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ) so they always match."""
import sys, os, math, re, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from common import *

SLUG = "supplements"
# Verbatim from /workspace/homepage/seo-meta.md (title is 63 chars: see NOTES.md, SEO flag 1)
TITLE = "Supplements & Herbology for Energy and Drive | Odin Health Labs"
DESC = "Why most supplement stacks fail, and how a structured, evidence-informed plan differs. Supplements and herbs for low energy, drive and recovery."
OG_ALT = "Odin Health Labs: structured supplement and herbology protocols for men, Canada and USA"
assert len(DESC) <= 160

FAQ = [
  ("What can a supplement and herbology plan do for me?",
  "A structured plan supports energy, drive, sleep and recovery. It is built around your history, labs and goals, with clear dosing, quality sourcing, timing and regular check-ins, and it sits alongside the food, sleep and training habits that shape how you feel."),
  ("Which supplements will you recommend?",
  "Your plan is personal. Anything we suggest depends on your history, diet, medications and conditions, and we ask about those first. We start with food, sleep and training, then add one layer at a time with a reason for each."),
  ("How do you check supplements against my medications?",
  "Tell us everything you take, prescription and over-the-counter. We check each product against your list before it goes into your plan and add them one at a time. You can also share your plan with your doctor or pharmacist."),
  ("Do I need blood tests first?",
  "Not to start a conversation. If blood tests would help, we walk you through which ones to ask about and what the results mean for your plan."),
  ("How quickly will I notice a difference?",
  "People respond differently, so part of your plan is agreeing how you\u2019ll judge whether something is worth continuing. We review it with you at every check-in and keep what is worth keeping."),
 ("Is it fully online, and where do you work with men?",
  'Yes. Odin Health Labs is telehealth only and serves men across Canada and the USA. Everything happens by secure video, phone and message, so there are no clinic visits. See our <a href="%s/">low testosterone and andropause overview</a> for how the service works, or read our <a href="%s/privacy">Privacy Policy</a> for how we protect your information.' % (SITE, SITE)),
]

GEN_STATIC, GEN_MOTION = [], []

# ---------- 1 · HERO: items fall out of a jumble and sort into a six-compartment organiser ----------
def hero_tray():
    cxs = [116, 240, 364]; cys = [212, 268]
    cells = [(cxs[c], cys[r]) for r in range(2) for c in range(3)]
    s = ['<defs><radialGradient id="sp-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.3"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs>',
         '<ellipse cx="240" cy="190" rx="220" ry="110" fill="url(#sp-g)" opacity="0.5"/>',
         '<rect x="40" y="172" width="400" height="128" rx="20" fill="#0f240f" stroke="rgba(196,255,73,0.55)" stroke-width="3"/>']
    for i, (cx, cy) in enumerate(cells):
        s.append('<rect x="%d" y="%d" width="112" height="44" rx="12" fill="rgba(196,255,73,0.05)" stroke="rgba(196,255,73,0.28)" stroke-width="2"/>' % (cx - 56, cy - 22))
        s.append('<rect class="sp-flash" style="--k:%d" x="%d" y="%d" width="112" height="44" rx="12" fill="none" stroke="#c4ff49" stroke-width="3.5"/>' % (i, cx - 56, cy - 22))
    shapes = [
      '<g transform="rotate(-28)"><path d="M0 -10H-14A10 10 0 0 0 -14 10H0Z" fill="#c4ff49"/><path d="M0 -10H14A10 10 0 0 1 14 10H0Z" fill="#fff" fill-opacity="0.9"/><rect x="-24" y="-10" width="48" height="20" rx="10" fill="none" stroke="#0f240f" stroke-width="2"/></g>',
      '<circle r="14" fill="#fff" fill-opacity="0.92"/><path d="M-14 0H14" stroke="#0f240f" stroke-width="2.4"/>',
      '<g transform="rotate(-20) translate(-24 0)"><path d="M0 0C12-16 36-16 48 0C36 16 12 16 0 0Z" fill="#c4ff49" fill-opacity="0.9"/><path d="M4 0H42" stroke="#0f240f" stroke-width="2" stroke-linecap="round"/></g>',
      '<g transform="rotate(32)"><path d="M0 -10H-14A10 10 0 0 0 -14 10H0Z" fill="#fff" fill-opacity="0.9"/><path d="M0 -10H14A10 10 0 0 1 14 10H0Z" fill="#c4ff49"/></g>',
      '<path d="M0 -17C10 -5 15 2 15 8A15 15 0 0 1 -15 8C-15 2 -10 -5 0 -17Z" fill="#c4ff49" fill-opacity="0.9"/><path d="M-6 6a7 7 0 0 0 5 5" stroke="#0f240f" stroke-width="2.2" fill="none" stroke-linecap="round"/>',
      '<rect x="-17" y="-11" width="34" height="22" rx="11" fill="#fff" fill-opacity="0.92"/><path d="M0 -11V11" stroke="#0f240f" stroke-width="2.4"/>',
    ]
    starts = [(-70, -120, -50), (60, -140, 40), (-30, -110, -30), (90, -150, 60), (-90, -170, 25), (30, -120, -60)]
    for i, (cx, cy) in enumerate(cells):
        fx, fy, fr = starts[i]
        s.append('<g transform="translate(%d %d)"><g class="sp-item" style="--k:%d;--fx:%dpx;--fy:%dpx;--fr:%ddeg">%s</g></g>' % (cx, cy, i, fx, fy - (cy - 212), fr, shapes[i]))
    return "\n".join(s)

# ---------- 2 · WHY STACKS FALL SHORT: crossing pathways clash on the left, tidy lanes on the right ----------
def clash():
    s = ['<path d="M280 24V226" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="3 8" stroke-linecap="round"/>']
    s.append('<path d="M30 60L250 190" stroke="rgba(157,179,157,0.4)" stroke-width="4" stroke-linecap="round"/><path d="M30 190L250 60" stroke="rgba(157,179,157,0.4)" stroke-width="4" stroke-linecap="round"/>')
    s.append('<circle cx="30" cy="60" r="9" fill="#142e14" stroke="#9db39d" stroke-width="2.4"/><circle cx="30" cy="190" r="9" fill="#142e14" stroke="#9db39d" stroke-width="2.4"/><circle cx="250" cy="60" r="9" fill="#142e14" stroke="#9db39d" stroke-width="2.4"/><circle cx="250" cy="190" r="9" fill="#142e14" stroke="#9db39d" stroke-width="2.4"/>')
    s.append('<circle class="cl-a" cx="30" cy="60" r="7" fill="#9db39d"/><circle class="cl-b" cx="30" cy="190" r="7" fill="#fff"/>')
    s.append('<circle class="cl-burst" cx="140" cy="125" r="16" fill="none" stroke="#fff" stroke-width="2.5"/>')
    sp = ""
    for k in range(8):
        a = k * 45; x0 = 140 + 10 * math.cos(math.radians(a)); y0 = 125 + 10 * math.sin(math.radians(a)); x1 = 140 + 22 * math.cos(math.radians(a)); y1 = 125 + 22 * math.sin(math.radians(a))
        sp += "M%.1f %.1fL%.1f %.1f" % (x0, y0, x1, y1)
    s.append('<path class="cl-sparks" d="%s" stroke="#fff" stroke-width="2.4" stroke-linecap="round" fill="none"/>' % sp)
    for k, y in enumerate((70, 125, 180)):
        s.append('<path d="M310 %dH510" stroke="rgba(196,255,73,0.2)" stroke-width="4" stroke-linecap="round"/>' % y)
        s.append('<path class="dr" pathLength="1" style="--d:%.2f" d="M310 %dH510" stroke="#c4ff49" stroke-width="4" stroke-linecap="round" fill="none"/>' % (0.1 + k * 0.2, y))
        s.append('<circle cx="310" cy="%d" r="9" fill="#142e14" stroke="#c4ff49" stroke-width="2.4"/>' % y)
        s.append('<g class="cl-end t" style="--k:%d"><circle cx="510" cy="%d" r="11" fill="#0f240f" stroke="#c4ff49" stroke-width="2.6"/><path d="M505 %dl3.6 3.6L516 %d" fill="none" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></g>' % (k, y, y, y - 4))
        s.append('<circle class="cl-dot" style="--k:%d" cx="310" cy="%d" r="6" fill="#c4ff49"/>' % (k, y))
    return "\n".join(s)

# ---------- 3 · STRUCTURED PLAN: four layers, built from the bottom, lit in order; a marker climbs ----------
def layers():
    s = ['<path d="M404 236V80" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-dasharray="2 7" stroke-linecap="round"/>']
    spec = [("food", 300, 216, False), ("sleep", 250, 164, False), ("caps", 200, 112, False), ("leaf", 150, 60, True)]
    for k, (nm, w, y, dashed) in enumerate(spec):
        x = 220 - w / 2
        da = ' stroke-dasharray="6 6"' if dashed else ''
        s.append('<g class="pop t" style="--d:%.2f"><rect x="%.0f" y="%d" width="%d" height="40" rx="11" fill="%s" stroke="%s" stroke-width="2.6"%s/>%s<path d="M%.0f %dH%.0f" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round"/>'
                 '<rect class="ly-lit t" style="--k:%d" x="%.0f" y="%d" width="%d" height="40" rx="11" fill="rgba(196,255,73,0.22)" stroke="#c4ff49" stroke-width="3.5"/></g>'
                 % (0.15 * k, x, y, w, "rgba(196,255,73,0.08)" if not dashed else "transparent", "#c4ff49" if not dashed else "rgba(255,255,255,0.7)", da,
                    ico(nm, x + 28, y + 20, 24, "#c4ff49" if not dashed else "#fff", 1.8), x + 58, y + 20, x + w - 24, k, x, y, w))
    s.append('<g class="ly-mark"><circle r="8" fill="#fff"/><circle r="13" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="2"/></g>')
    return "\n".join(s)

# ---------- 4 · HERBOLOGY: a sprig draws up, leaves sway, pollen drifts ----------
def sprig():
    s = ['<defs><radialGradient id="sb-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.28"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs>',
         '<ellipse cx="220" cy="130" rx="150" ry="120" fill="url(#sb-g)" opacity="0.6"/>',
         '<path d="M150 266Q220 250 290 266" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2.5" stroke-dasharray="2 7" stroke-linecap="round"/>',
         '<path d="M220 264C220 222 210 184 220 142C230 102 214 82 220 54" fill="none" stroke="rgba(196,255,73,0.2)" stroke-width="6" stroke-linecap="round"/>',
         '<path class="dr" pathLength="1" style="--d:0.1;--dur:1.8s" d="M220 264C220 222 210 184 220 142C230 102 214 82 220 54" fill="none" stroke="#c4ff49" stroke-width="5" stroke-linecap="round"/>']
    leaf = '<path d="M0 0C14-16 42-16 56 0C42 16 14 16 0 0Z" fill="rgba(196,255,73,0.18)" stroke="#c4ff49" stroke-width="2.6" stroke-linejoin="round"/><path d="M5 0H48" stroke="rgba(255,255,255,0.55)" stroke-width="2" stroke-linecap="round"/>'
    pts = [(220, 222, -24), (219, 192, 204), (221, 156, -34), (218, 126, 214), (220, 92, -42), (219, 66, 226)]
    for k, (x, y, a) in enumerate(pts):
        s.append('<g transform="translate(%d %d) rotate(%d)"><g class="pop t" style="--d:%.2f"><g class="sb-leaf" style="--k:%d">%s</g></g></g>' % (x, y, a, 0.8 + k * 0.18, k, leaf))
    s.append('<g transform="translate(220 54) rotate(-90)"><g class="pop t" style="--d:2"><g class="sb-leaf" style="--k:6"><path d="M0 0C10-12 30-12 40 0C30 12 10 12 0 0Z" fill="#c4ff49" fill-opacity="0.85"/></g></g></g>')
    for k, (x, y) in enumerate(((150, 150), (300, 120), (188, 90), (270, 190), (330, 170))):
        s.append('<circle class="sb-pol" style="--k:%d" cx="%d" cy="%d" r="2.8" fill="#c4ff49"/>' % (k, x, y))
    return "\n".join(s)

# ---------- 5 · MEDICATIONS: a scan bar checks each row of a list; one row gets a closer look ----------
def scan():
    s = ['<defs><linearGradient id="sc-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ff49" stop-opacity="0"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0.4"/></linearGradient></defs>',
         '<rect class="pop t" style="--d:0" x="70" y="30" width="260" height="200" rx="18" fill="#0f240f" stroke="rgba(196,255,73,0.5)" stroke-width="2.6"/>']
    rows = [("caps", 70, 0), ("leaf", 110, 1), ("bottle", 150, 0), ("doc", 190, 0)]
    times = [0.9, 2.1, 3.3, 4.4]
    for k, (nm, y, q) in enumerate(rows):
        s.append('<g class="pop" style="--d:%.2f"><circle cx="104" cy="%d" r="15" fill="#142e14" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>%s<path d="M134 %dH%d" stroke="rgba(255,255,255,0.4)" stroke-width="4" stroke-linecap="round"/><path d="M134 %dH%d" stroke="rgba(255,255,255,0.18)" stroke-width="3" stroke-linecap="round"/></g>' % (0.15 + k * 0.1, y, ico(nm, 104, y, 18, "#fff", 1.7), y - 4, 250 - k * 14, y + 6, 214 - k * 12))
        if q:
            s.append('<g class="sc-mark t sc-m%d"><circle cx="300" cy="%d" r="13" fill="#0f240f" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 3"/><path d="M296 %dc0-3 2-4.5 4-4.5s4 1.5 4 3.5c0 2-2 2.5-3 3.5-.6.6-1 1.2-1 2.5" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="300" cy="%d" r="1.4" fill="#fff"/></g>' % (k, y, y - 3, y + 8))
        else:
            s.append('<g class="sc-mark t sc-m%d"><circle cx="300" cy="%d" r="13" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/><path d="M294 %dl4.5 4.5L307 %d" fill="none" stroke="#c4ff49" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></g>' % (k, y, y, y - 4))
    s.append('<g class="sc-bar"><rect x="70" y="30" width="260" height="22" fill="url(#sc-g)"/><path d="M70 52H330" stroke="#c4ff49" stroke-width="3" stroke-linecap="round"/></g>')
    s.append('<path d="M330 130H356" stroke="rgba(255,255,255,0.35)" stroke-width="2" stroke-dasharray="2 6" stroke-linecap="round"/>')
    s.append('<g class="pop t" style="--d:0.5"><circle class="sc-ring" cx="390" cy="130" r="34" fill="none" stroke="#c4ff49" stroke-width="2"/><circle cx="390" cy="130" r="34" fill="#0f240f" stroke="#c4ff49" stroke-width="2.6"/>%s</g>' % ico("shield", 390, 130, 36, "#c4ff49", 1.6))
    return "\n".join(s)

# ---------- 6 · QUALITY: three seals, each stamped in turn ----------
def stamps():
    s = []
    for k, (nm, x) in enumerate((("labs", 110), ("doc", 280), ("caps", 450))):
        s.append('<g class="pop t" style="--d:%.2f"><circle class="qs-orb" cx="%d" cy="100" r="62" fill="none" stroke="rgba(196,255,73,0.3)" stroke-width="2" stroke-dasharray="3 9" stroke-linecap="round"/><circle cx="%d" cy="100" r="46" fill="#0f240f" stroke="#c4ff49" stroke-width="2.8"/>%s</g>' % (0.1 + k * 0.15, x, x, ico(nm, x, 100, 40, "#c4ff49", 1.5)))
        s.append('<circle class="qs-ring t" style="--k:%d" cx="%d" cy="134" r="15" fill="none" stroke="#c4ff49" stroke-width="2"/>' % (k, x + 36))
        s.append('<g class="qs-stamp t" style="--k:%d"><circle cx="%d" cy="134" r="15" fill="#c4ff49"/><path d="M%d 134l4.5 4.5L%d 129" fill="none" stroke="#0f240f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>' % (k, x + 36, x + 30, x + 43))
    return "\n".join(s)

# ---------- 7 · RELATED: three pages orbit the supplements node ----------
def orbit():
    cx, cy, R = 280, 100, 72
    s = ['<circle class="so-ring t" cx="280" cy="100" r="34" fill="none" stroke="#c4ff49" stroke-width="2"/>',
         '<circle cx="280" cy="100" r="72" fill="none" stroke="rgba(196,255,73,0.22)" stroke-width="2" stroke-dasharray="3 9" stroke-linecap="round"/>']
    s.append('<g class="so-orbit">')
    for k, (nm, a) in enumerate((("coach", 0), ("labs", 120), ("home", 240))):
        x = cx + R * math.sin(math.radians(a)); y = cy - R * math.cos(math.radians(a))
        s.append('<g class="so-sat" style="transform-origin:%.1fpx %.1fpx"><circle cx="%.1f" cy="%.1f" r="25" fill="#0f240f" stroke="rgba(255,255,255,0.75)" stroke-width="2.6"/>%s</g>' % (x, y, x, y, ico(nm, x, y, 28, "#fff", 1.6)))
    s.append('</g>')
    s.append('<g class="pop t" style="--d:0"><circle cx="280" cy="100" r="34" fill="rgba(196,255,73,0.14)" stroke="#c4ff49" stroke-width="3"/>%s</g>' % ico("caps", 280, 100, 36, "#c4ff49", 1.6))
    return "\n".join(s)

# ---------- 8 · FAQ: a capsule opens a little and a question mark rises ----------
FAQMOTIF = '''<circle cx="60" cy="52" r="46" stroke="rgba(196,255,73,0.18)" stroke-width="1.5" stroke-dasharray="2 7" stroke-linecap="round"/>
<g class="fq-q"><path class="dr" pathLength="1" style="--d:0.3;--dur:1.1s" d="M51 22c0-6 4-9 9-9s9 3 9 7.5c0 4-3 5.5-5.5 7.5-2 1.7-3 3-3 6" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/><circle class="fq-qd" cx="60.5" cy="39" r="2.6" fill="#fff"/></g>
<g transform="translate(60 70) rotate(-35)"><g class="fq-half fq-l"><path d="M0 -13H-15A13 13 0 0 0 -15 13H0Z" fill="#c4ff49" fill-opacity="0.9"/></g><g class="fq-half fq-r"><path d="M0 -13H15A13 13 0 0 1 15 13H0Z" fill="#fff" fill-opacity="0.92"/></g></g>
<circle class="fq-sp" style="--k:0" cx="100" cy="40" r="3" fill="#c4ff49"/><circle class="fq-sp" style="--k:1" cx="18" cy="48" r="2.4" fill="#fff"/>'''

# ---------- 9 · FINAL: a written plan; lines and ticks draw in, a pen moves down the list ----------
def plan():
    s = ['<g class="fn-sheet">',
         '<rect x="110" y="24" width="140" height="164" rx="14" fill="#142e14" stroke="#c4ff49" stroke-width="3"/><rect x="150" y="14" width="60" height="22" rx="8" fill="#0f240f" stroke="#fff" stroke-width="2.6"/>']
    for k in range(4):
        y = 68 + k * 30
        s.append('<rect x="126" y="%d" width="18" height="18" rx="5" fill="none" stroke="rgba(196,255,73,0.6)" stroke-width="2.4"/>' % (y - 9))
        s.append('<path class="dr" pathLength="1" style="--d:%.2f" d="M130 %dl3.6 3.6L141 %d" fill="none" stroke="#c4ff49" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>' % (0.4 + k * 0.35, y, y - 4))
        s.append('<path class="dr" pathLength="1" style="--d:%.2f" d="M154 %dH%d" stroke="rgba(255,255,255,0.7)" stroke-width="4" stroke-linecap="round" fill="none"/>' % (0.3 + k * 0.35, y, 232 - [0, 24, 8, 36][k]))
    s.append('</g>')
    s.append('<g class="fn-pen">%s</g>' % ico("pen", 0, 0, 30, "#fff", 1.8))
    return "\n".join(s)

# ---------- step icons ----------
def step_icons():
    return {
     "{{STEP1}}": '<rect x="9" y="6" width="30" height="36" rx="5"/><path d="M16 17h16M16 25h16M16 33h9" opacity="0.55"/><g class="hi-pen t"><path d="M26 38l1-4 9-9a2 2 0 0 1 3 3l-9 9z" stroke="#fff" fill="#142e14"/></g>',
     "{{STEP2}}": '<rect x="12" y="14" width="22" height="28" rx="5"/><rect x="16" y="8" width="14" height="6" rx="2"/><path d="M12 26h22" opacity="0.55"/><g class="hi-lens t"><circle cx="30" cy="30" r="7" stroke="#fff" fill="rgba(15,36,15,0.85)"/><path d="M35 35l6 6" stroke="#fff"/></g>',
     "{{STEP3}}": '<path d="M8 40h32" opacity="0.4"/><g class="hi-hop t" style="--k:0"><circle cx="12" cy="30" r="6" fill="#142e14"/><path d="M12 28v4" stroke="#fff"/></g><g class="hi-hop t" style="--k:1"><circle cx="24" cy="30" r="6" fill="#142e14" stroke="#fff"/><path d="M22 28.5l2-1.5v5" stroke="#fff"/></g><g class="hi-hop t" style="--k:2"><circle cx="36" cy="30" r="6" fill="#142e14"/><path d="M33.5 29c0-1.5 1-2 2.5-2s2.5 1 2.5 2c0 2-4 3-4 5h4" stroke="#fff" stroke-width="2"/></g>',
     "{{STEP4}}": '<circle class="hi-halo t" cx="24" cy="24" r="17" opacity="0.5"/><path d="M24 7l14 5v10c0 9-6 14-14 17-8-3-14-8-14-17V12z"/><path d="M17 24l5 5 9-10" stroke="#fff"/>',
    }

slots = {"{{HERO}}": hero_tray(), "{{CLASH}}": clash(), "{{LAYERS}}": layers(), "{{SPRIG}}": sprig(), "{{SCAN}}": scan(),
         "{{STAMPS}}": stamps(), "{{ORBIT}}": orbit(), "{{FAQMOTIF}}": FAQMOTIF, "{{PLAN}}": plan(), "{{FAQ}}": faq_html(FAQ)}
slots.update(step_icons())

body = open(os.path.join(HERE, "page.body.html"), encoding="utf-8").read()
tmp = os.path.join(HERE, ".tmp"); os.makedirs(tmp, exist_ok=True)
open(os.path.join(tmp, "page.body.html"), "w", encoding="utf-8").write(re.sub(r"\{\{CI:(\w+):(\d+)\}\}", lambda m: ci(m.group(1), int(m.group(2))), body))
TIMES = [0.9, 2.1, 3.3, 4.4]
gen = "".join("  @keyframes sc-mk%d { 0%%, %.1f%% { opacity: 0; transform: scale(0.7); } %.1f%%, 88%% { opacity: 1; transform: none; } 94%%, 100%% { opacity: 0; transform: none; } }\n  .js-reveal .pg .sc-m%d { animation: sc-mk%d 6s var(--ease-out) infinite; }\n" % (k, TIMES[k] / 6 * 100 - 0.01, TIMES[k] / 6 * 100 + 3, k, k) for k in range(4))
open(os.path.join(tmp, "page.css"), "w").write(open(os.path.join(HERE, "page.css"), encoding="utf-8").read().replace("/*@GEN_MOTION*/", gen))
ld = jsonld(SLUG, TITLE, DESC, "Supplements and herbology for men with low energy and drive", "Supplements", FAQ)
assemble(tmp, SLUG, TITLE, DESC, OG_ALT, ld, slots)
shutil.copy(os.path.join(tmp, "page.html"), os.path.join(HERE, "page.html"))
shutil.rmtree(tmp)
