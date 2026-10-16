"""Build /workspace/pages/low-testosterone-labs-to-ask-for/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *

SLUG = "low-testosterone-labs-to-ask-for"
TITLE = "Low Testosterone Labs: What to Ask For | Odin Health Labs"
DESC = "What labs should you ask for besides total testosterone? Free T, SHBG, LH, FSH, estradiol, prolactin, hematocrit, PSA, thyroid, A1c and what each shows."
OG_ALT = "Odin Health Labs: which labs to ask for besides total testosterone, for men in Canada and the USA"
assert len(TITLE) <= 60 and len(DESC) <= 160, (len(TITLE), len(DESC))

FAQ = [
 ("What is the first test to ask for?",
  "A total testosterone test on an early-morning, fasting blood sample. The Endocrine Society guideline (2018) advises repeating a low result on a second morning before drawing conclusions, because levels vary through the day and from day to day."),
  ("Do I need free testosterone as well as total?",
  "Sometimes. The Endocrine Society guideline advises measuring free testosterone when total testosterone is near the lower limit of normal or when something that alters SHBG may be present, such as a change in body weight or a thyroid or liver condition. We walk you through whether it adds anything in your case."),
  ("Why check LH and FSH?",
  "They show where in the system a low testosterone result may be coming from: the testes themselves, or the signal from the brain and pituitary gland. They also show how active your own production is, which matters if you may want children."),
  ("Should I get a PSA test?",
  "It depends on your age, family history and preferences, and we help you decide whether it fits. If testosterone therapy is ever being considered, PSA is usually part of the baseline conversation for men of an age where it is appropriate."),
  ("Do reference ranges differ between labs?",
  "Yes. Ranges depend on the assay, the equipment and the group of people used to set them, so the same result can be flagged differently at two labs. That is why the range printed on your own report is the one that counts, and we read it with you alongside your symptoms and any repeat result."),
 ("How does Odin Health Labs work with my doctor?",
  'Odin Health Labs is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. A free call helps you work out which labs to ask for and what to do with the results. We review your labs with you, build your plan and track your progress, and we can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

# ---------- 1 · HERO: a tube rack; liquid levels breathe, a drop falls into each tube in turn ----------
def hero_rack():
    xs = [100, 170, 240, 310, 380]; tops = [150, 118, 164, 134, 156]
    caps = [LIME, WHITE, '#9db39d', LIME, WHITE]
    s = ['<defs><radialGradient id="rk-g" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.15"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="170" rx="225" ry="135" fill="url(#rk-g)"/>']
    for i, x in enumerate(xs):
        col = LIME if i % 2 == 0 else WHITE
        s.append('<g class="pop t" style="--d:%s"><g class="rk-liq t" style="--k:%d"><path d="M%d %d H%d V214 a15 15 0 0 1 -30 0 Z" fill="%s" fill-opacity="0.55"/></g>'
                 '<path d="M%d 90 V214 a18 18 0 0 0 36 0 V90" fill="none" stroke="rgba(255,255,255,0.75)" stroke-width="3" stroke-linecap="round"/>'
                 '<path d="M%d 90H%d" stroke="rgba(255,255,255,0.75)" stroke-width="3" stroke-linecap="round"/><rect x="%d" y="74" width="40" height="14" rx="5" fill="%s"/></g>'
                 % (0.15 + i * 0.1, i, x - 15, tops[i], x + 15, col, x - 18, x - 24, x + 24, x - 20, caps[i]))
    s.append('<g class="pop t" style="--d:0.7"><rect x="52" y="218" width="376" height="28" rx="12" fill="#142e14" stroke="rgba(196,255,73,0.5)" stroke-width="2.6"/>' + ''.join('<circle cx="%d" cy="232" r="4" fill="rgba(196,255,73,0.5)"/>' % x for x in xs) + '</g>')
    for i, x in enumerate(xs):
        s.append('<circle class="rk-d fx" style="--k:%d;--h:%d" cx="%d" cy="40" r="6" fill="#c4ff49"/>' % (i, tops[i] - 40, x))
    s.append(dr('M60 280H420', 1.0, 1.2, 'rgba(196,255,73,0.35)', 2.4))
    return '\n'.join(s)

# ---------- 2 · TIMING: a sun rides an arc, the morning window is highlighted; first tube, then the repeat ----------
def timing():
    d, pts = path(('M', 60, 170), ('C', 150, -10, 410, -10, 500, 170), n=42)
    morn = 'M' + ' L'.join('%s %s' % (f(x), f(y)) for x, y in pts[:15])
    s = ['<path d="M30 170H530" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round"/>']
    s.append('<path d="%s" fill="none" stroke="rgba(255,255,255,0.18)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 8"/>' % d)
    s.append(dr(morn, 0.3, 1.4, LIME, 5))
    s.append('<g class="tm-sun">' + '<circle r="11" fill="#c4ff49"/><circle r="19" fill="none" stroke="#c4ff49" stroke-opacity="0.45" stroke-width="2.4"/></g>')
    G.travel('tm-sun', pts, 3, 97, 12, rest=pts[9], fade=2.5)
    s.append(dr('M150 222H190', 0.9, 0.7, WHITE, 3))
    s.append('<path d="M190 222l-8-6v12z" fill="#fff"/>')
    for k, x in enumerate((110, 240)):
        s.append('<circle class="tm-lit fx" style="--k:%d" cx="%d" cy="222" r="30" fill="none" stroke="#fff" stroke-width="3"/>' % (k, x))
        s.append(node(x, 222, 26, 'tube', 0.6 + k * 0.25, LIME if k == 0 else WHITE, isz=28))
    s.append(node(480, 222, 18, 'calendar', 1.1, WHITE, dashed=True, isz=20))
    return '\n'.join(s)

# ---------- 3 · BOUND vs FREE: carriers hold testosterone; free dots drift between them ----------
def bound():
    s = []
    for k, x in enumerate((110, 280, 450)):
        s.append('<g class="pop t" style="--d:%s"><g class="bd-car" style="--k:%d"><circle cx="%d" cy="120" r="46" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.65)" stroke-width="2.8" stroke-dasharray="4 5"/><path d="M%d 104a22 22 0 0 0 44 0" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="3" stroke-linecap="round"/><circle class="bd-b t" style="--k:%d" cx="%d" cy="116" r="9" fill="#c4ff49"/></g></g>' % (0.1 + k * 0.15, k, x, x - 22, k, x))
    for k, (x, y, dx, dy) in enumerate(((195, 52, 16, 10), (365, 196, -14, -10), (195, 196, 12, -12), (365, 52, -16, 12), (280, 30, 18, 6))):
        s.append('<g class="pop t" style="--d:%s"><g class="bd-f" style="--k:%d;--dx:%dpx;--dy:%dpx"><circle cx="%d" cy="%d" r="7" fill="#c4ff49"/><circle cx="%d" cy="%d" r="12" fill="none" stroke="#c4ff49" stroke-opacity="0.35" stroke-width="2"/></g></g>' % (0.5 + k * 0.1, k, dx, dy, x, y, x, y))
    return '\n'.join(s)

# ---------- 4 · RELAY: brain -> pituitary -> testes, pulses run along it; feedback loop; prolactin above, estradiol beside ----------
def relay():
    dM, pM = path(('M', 80, 120), ('L', 400, 120))
    dF, pF = path(('M', 400, 154), ('C', 340, 232, 140, 232, 80, 154))
    s = ['<path d="M114 120H200M260 120H366" stroke="rgba(196,255,73,0.22)" stroke-width="4" stroke-linecap="round"/>']
    s.append(dr('M114 120H200M260 120H366', 0.3, 1.2, LIME, 4))
    s.append('<path d="M230 54V90M434 120H492" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/>')
    s.append('<path d="%s" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/>' % dF)
    for i in range(3):
        s.append(dot('rl-p%d' % i, 6, LIME)); G.travel('rl-p%d' % i, pM[:], 3, 90, 5, delay='%ss' % f(-i * 1.67), rest=(130 + i * 100, 120))
    for i in range(3):
        s.append(dot('rl-f%d' % i, 5, WHITE)); G.travel('rl-f%d' % i, pF, 4, 96, 6, delay='%ss' % f(-i * 2), rest=pF[4 + i * 4])
    s.append('<circle class="rl-lit fx" cx="230" cy="36" r="24" fill="none" stroke="#fff" stroke-width="3"/>')
    s.append(node(80, 120, 34, 'brain', 0.1, LIME, fill='#142e14', isz=36))
    s.append(node(230, 120, 30, 'gland', 0.3, WHITE, isz=32))
    s.append(node(400, 120, 34, 'drop', 0.5, LIME, fill='#142e14', isz=34))
    s.append(node(230, 36, 18, 'pulse', 0.7, WHITE, dashed=True, isz=20))
    s.append(node(510, 120, 18, 'flame', 0.8, WHITE, dashed=True, isz=20))
    return '\n'.join(s)

# ---------- 5 · PIPE: red blood cells flow along a tube; shield, document and heart appear below ----------
def pipe():
    s = ['<g class="pop t" style="--d:0.05"><rect x="40" y="36" width="480" height="68" rx="34" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.4)" stroke-width="2.8"/></g>']
    for i in range(7):
        s.append('<g class="pp-c%d fx"><circle r="12" fill="rgba(196,255,73,0.3)" stroke="#c4ff49" stroke-width="2.4"/><circle r="4.5" fill="none" stroke="#c4ff49" stroke-opacity="0.7" stroke-width="2"/></g>' % i)
        G.travel('pp-c%d' % i, [(70, 70), (490, 70)], 3, 97, 9, delay='%ss' % f(-i * 9 / 7), rest=(84 + i * 60, 70), fade=2.5)
    s[-7:] = [x.replace(' fx"', '"') for x in s[-7:]]
    s.append(dr('M206 160H254M306 160H354', 0.8, 0.9, 'rgba(255,255,255,0.45)', 2.6))
    for k, (x, ic) in enumerate(((180, 'shield'), (280, 'doc'), (380, 'heart'))):
        s.append(node(x, 160, 26, ic, 0.6 + k * 0.25, LIME if k != 1 else WHITE, isz=28))
    return '\n'.join(s)

# ---------- 6 · DASHBOARD: six tiles, each with a dial whose needle sweeps ----------
def dash():
    ic = ['flame', 'drop', 'heart', 'sun', 'labs', 'doc']
    s = []
    for k in range(6):
        x = 20 + (k % 3) * 175; y = 14 + (k // 3) * 118
        cx, cy = x + 112, y + 74
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="%d" width="165" height="104" rx="16" fill="rgba(255,255,255,0.03)" stroke="rgba(196,255,73,0.25)" stroke-width="1.6"/>' % (0.1 + k * 0.1, x, y))
        s.append('<circle cx="%d" cy="%d" r="19" fill="#0f240f" stroke="%s" stroke-width="2.4"/>%s' % (x + 34, y + 34, LIME if k % 2 == 0 else 'rgba(255,255,255,0.75)', ico(ic[k], x + 34, y + 34, 22, LIME if k % 2 == 0 else WHITE, 1.7)))
        s.append('<path d="M%d %d A36 36 0 0 1 %d %d" fill="none" stroke="rgba(255,255,255,0.28)" stroke-width="5" stroke-linecap="round"/><path d="M%d %d A36 36 0 0 1 %d %d" fill="none" stroke="rgba(196,255,73,0.6)" stroke-width="5" stroke-linecap="round"/>' % (cx - 36, cy, cx + 36, cy, cx - 36, cy, cx, cy - 36))
        s.append('<g class="ds-n" style="--k:%d;--p:%ss;--r:%ddeg;transform-origin:%dpx %dpx"><path d="M%d %dL%d %d" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/></g><circle cx="%d" cy="%d" r="5" fill="#fff"/></g>' % (k, f(3.2 + (k * 7 % 5) * 0.6), (k * 23 % 40) - 20, cx, cy, cx, cy, cx, cy - 30, cx, cy))
    return '\n'.join(s)

# ---------- 7 · FORM: a pen walks down a lab request, ticking each box ----------
def form():
    s = ['<g class="pop t" style="--d:0.05"><rect x="150" y="8" width="260" height="214" rx="16" fill="#142e14" stroke="rgba(196,255,73,0.45)" stroke-width="2.6"/></g>']
    s.append(dr('M176 32H300', 0.3, 0.8, LIME, 5))
    a, b, dur = 4, 92, 9
    for k in range(6):
        y = 66 + k * 26
        dl = (a + (b - a) * k / 5) / 100 * dur - dur
        s.append('<g class="pop t" style="--d:%s"><rect x="176" y="%d" width="18" height="18" rx="5" fill="none" stroke="#c4ff49" stroke-width="2.4"/><path d="M%d %dh%d" stroke="rgba(255,255,255,0.55)" stroke-width="4" stroke-linecap="round"/></g>' % (0.4 + k * 0.08, y - 9, 206, y, 120 - (k * 23) % 50))
        s.append('<g class="fm-tick t" style="--dl:%ss"><path d="M180 %dl4 4 8-9" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></g>' % (f(dl), y))
    s.append('<g class="fm-pen"><path d="M0 0l-5-13 9-6 6 12z" fill="#c4ff49"/><path d="M-5-13l9-6" stroke="#0f240f" stroke-width="2"/></g>')
    G.travel('fm-pen', [(200, 66), (200, 66 + 5 * 26)], a, b, dur, rest=(200, 196))
    s[-2] = s[-2]
    return '\n'.join(s)

# ---------- 8 · RULERS: three labs, three normal bands in different places, one fixed result marker ----------
def rulers():
    s = []
    bands = [(190, 170), (330, 150), (240, 150)]
    for k, (bx, bw) in enumerate(bands):
        y = 62 + k * 56
        s.append('<path d="M60 %d H500" stroke="rgba(255,255,255,0.25)" stroke-width="3" stroke-linecap="round"/><text x="60" y="%d" font-size="13" fill="#fff" fill-opacity="0.8">Lab %s</text>' % (y, y - 20, 'ABC'[k]))
        s.append(dr('M60 %dV%d M500 %dV%d' % (y - 9, y + 9, y - 9, y + 9), 0.1 + k * 0.1, 0.6, 'rgba(255,255,255,0.4)', 2.4))
        s.append('<g class="pop t" style="--d:%s"><rect class="rg-b" style="--k:%d;--p:%ss" x="%d" y="%d" width="%d" height="22" rx="11" fill="rgba(196,255,73,0.3)" stroke="#c4ff49" stroke-width="2.4"/></g>' % (0.3 + k * 0.15, k, f(5 + k * 1.3), bx, y - 11, bw))
    s.append('<path d="M300 26V190" stroke="rgba(255,255,255,0.7)" stroke-width="2.4" stroke-dasharray="3 6" stroke-linecap="round"/>')
    s.append('<g class="pop t" style="--d:0.9"><path d="M300 12l9 10-9 10-9-10z" fill="#fff"/></g>')
    return '\n'.join(s)

# ---------- final: the sun rises beside a tube and a calendar ----------
SUNRISE = '''<defs><clipPath id="sr-c"><rect x="0" y="0" width="360" height="150"/></clipPath><radialGradient id="sr-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.35"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs>
<g clip-path="url(#sr-c)"><g class="sr-sun"><circle cx="180" cy="150" r="90" fill="url(#sr-g)"/><g class="sr-rays"><path class="sr-ray" style="--k:0" d="M180 86v-14" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round" transform="rotate(-75 180 150)"/><path class="sr-ray" style="--k:1" d="M180 86v-14" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round" transform="rotate(-50 180 150)"/><path class="sr-ray" style="--k:2" d="M180 86v-14" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round" transform="rotate(-25 180 150)"/><path class="sr-ray" style="--k:3" d="M180 86v-14" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round" transform="rotate(0 180 150)"/><path class="sr-ray" style="--k:4" d="M180 86v-14" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round" transform="rotate(25 180 150)"/><path class="sr-ray" style="--k:5" d="M180 86v-14" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round" transform="rotate(50 180 150)"/><path class="sr-ray" style="--k:6" d="M180 86v-14" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round" transform="rotate(75 180 150)"/></g><circle class="sr-ring fx" style="--k:0" cx="180" cy="150" r="52" fill="none" stroke="#c4ff49" stroke-width="2.4"/><circle class="sr-ring fx" style="--k:1" cx="180" cy="150" r="52" fill="none" stroke="#c4ff49" stroke-width="2.4"/><circle class="sr-ring fx" style="--k:2" cx="180" cy="150" r="52" fill="none" stroke="#c4ff49" stroke-width="2.4"/><circle cx="180" cy="150" r="46" fill="#c4ff49"/></g></g>
<path d="M20 150H340" stroke="rgba(255,255,255,0.45)" stroke-width="3" stroke-linecap="round"/>
<path class="dr" pathLength="1" style="--d:0.2;--dur:1.2s" d="M40 170H320" stroke="rgba(196,255,73,0.3)" stroke-width="2.4" stroke-linecap="round" fill="none"/>'''
SUNRISE += node(66, 110, 26, 'tube', 0.4, LIME, isz=28) + node(294, 110, 26, 'calendar', 0.55, WHITE, isz=28)

# ---------- FAQ motif: a test tube with rising bubbles beside a question mark ----------
FAQMOTIF = '''<path d="M18 12V68a10 10 0 0 0 20 0V12" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round"/><path d="M12 12H44" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round"/><path d="M20 42H36V68a8 8 0 0 1-16 0Z" fill="#c4ff49" fill-opacity="0.45"/>
<circle class="fq-b" style="--k:0" cx="26" cy="60" r="2.8" fill="#fff"/><circle class="fq-b" style="--k:1" cx="31" cy="58" r="2.2" fill="#fff"/><circle class="fq-b" style="--k:2" cx="24" cy="56" r="1.8" fill="#fff"/>
<path class="dr" pathLength="1" style="--d:0.2;--dur:1.1s" d="M64 36c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="76" cy="64" r="3" fill="#fff"/>'''

def step_icons():
    return {
     "{{STEP1}}": '<g class="hi-pu" style="--k:0"><circle cx="24" cy="24" r="8" fill="rgba(196,255,73,0.25)"/></g><path d="M24 6v6M24 36v6M6 24h6M36 24h6M11 11l4 4M33 33l4 4M11 37l4-4M33 15l4-4"/>',
     "{{STEP2}}": '<path d="M13 7v26a4.5 4.5 0 0 0 9 0V7"/><path d="M26 7v26a4.5 4.5 0 0 0 9 0V7"/><g class="hi-gr" style="--k:0"><rect x="15.5" y="21" width="4" height="14" fill="#c4ff49" stroke="none"/></g><g class="hi-gr" style="--k:1"><rect x="28.5" y="24" width="4" height="11" fill="#fff" stroke="none"/></g>',
     "{{STEP3}}": '<circle cx="9" cy="24" r="4"/><path d="M13 24h8l6-14h8M21 24h14M21 24l6 14h8" stroke-opacity="0.7"/><g class="hi-bl" style="--k:0"><circle cx="39" cy="10" r="3.4" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="39" cy="24" r="3.4" fill="#fff" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="39" cy="38" r="3.4" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP4}}": '<path d="M24 5l15 6v11c0 10-6 17-15 21-9-4-15-11-15-21V11z"/><g class="hi-pu" style="--k:0"><path d="M17 24l5 5 9-10" stroke="#fff"/></g>',
    }

HUB = hub(G, [(110, 50, 'labs'), (110, 150, 'coach'), (450, 50, 'caps'), (450, 150, 'scale'), (280, 32, 'heart'), (280, 170, 'drop')])
slots = {"{{HERO}}": hero_rack(), "{{TIMING}}": timing(), "{{BOUND}}": bound(), "{{RELAY}}": relay(), "{{PIPE}}": pipe(), "{{DASH}}": dash(),
         "{{FORM}}": form(), "{{RULERS}}": rulers(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB, "{{FAQMOTIF}}": FAQMOTIF, "{{SUNRISE}}": SUNRISE}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Which blood tests to ask for besides total testosterone when low testosterone is suspected",
      "Low testosterone labs to ask for", "What labs should I ask for besides total testosterone?", slots, G)
