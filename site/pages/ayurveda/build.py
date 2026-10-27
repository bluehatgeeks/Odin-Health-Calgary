"""Build /workspace/pages/ayurveda/page.html (self-contained; paste into the GHL custom-code "Main Content" element).
Edit page.body.html (markup), page.css (graphics CSS), this file (FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match.
Same architecture as /health-coaching and /supplements: common.assemble() + base_head/base_motion/base_loader/base_tail."""
import sys, os, re, math, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *          # Gen, path, dr, node, dot, f, LIME/WHITE/DARK + common.* (assemble, jsonld, faq_html, ci, ico, SITE, ICONS)
import common

SLUG = "ayurveda"
# Verbatim from /workspace/homepage/seo-meta.md
TITLE = "Ayurveda for Energy, Sleep and Stress | Odin Health Lab"
DESC = "Ayurveda uses your constitution to guide diet, daily rhythm and herbs. See how it can support energy, sleep and stress, including for men with low-T symptoms."
OG_ALT = "Odin Health Lab: Ayurveda online for energy, sleep and stress, for men in Canada and the USA"
assert len(TITLE) <= 60 and len(DESC) <= 160, (len(TITLE), len(DESC))

common.ICONS.update({
 "bowl": '<path d="M3 11h18a9 9 0 0 1-18 0z"/><path d="M8 7c0-1.5 1-2 1-3.5M12 7c0-1.5 1-2 1-3.5M16 7c0-1.5 1-2 1-3.5"/>',
 "moon": '<path d="M21 13.5A8.5 8.5 0 1 1 10.5 3a7 7 0 0 0 10.5 10.5z"/>',
 "lotus": '<path d="M12 20c-4 0-8-2-9-6 3 0 6 1 9 4 3-3 6-4 9-4-1 4-5 6-9 6z"/><path d="M12 18c-2-2-3-5-3-8 1-2 2-4 3-6 1 2 2 4 3 6 0 3-1 6-3 8z"/>',
 "breath": '<path d="M3 9h10a3 3 0 1 0-3-3"/><path d="M3 13h15a3 3 0 1 1-3 3"/><path d="M3 17h6"/>',
})
SAGE = '#9db39d'
G = Gen()

FAQ = [
 ("What is Ayurveda, and what is a dosha?",
  "Ayurveda is a traditional system of health from India. It describes three doshas, Vata, Pitta and Kapha, as a way of naming patterns in how a person runs: movement and change, heat and drive, steadiness and structure. Everyone has all three in their own mix. That mix is your constitution, and it guides the food, daily rhythm, herbs and movement in your plan."),
 ("Can Ayurveda help men with low-T symptoms like low energy and poor sleep?",
  'Ayurveda works on the daily habits that shape how you feel: sleep, stress, food, movement and routine. Men with low testosterone symptoms often describe low energy, poor sleep and low drive, and these habits are part of that picture. We build a plan around your constitution and adjust it at every check-in. To find out whether low testosterone is part of your picture, see <a href="%s/low-testosterone-labs-to-ask-for">which blood tests to ask for</a>.' % SITE),
 ("Which herbs might be in my plan?",
  'Herbs are one option among four pillars, and we suggest them only where they fit you. Ashwagandha, for example, is a traditional Ayurvedic herb that many men ask about. We point you to products from suppliers that test for quality and purity, because some imported Ayurvedic products have been found to contain heavy metals. In Canada, licensed natural health products carry an eight-digit NPN on the label. See our <a href="%s/supplements">supplements and herbology</a> page for how we build a plan.' % SITE),
 ("How does Ayurveda work with my doctor and my medications?",
  "Ayurveda works alongside your medical care. Some herbs, including ashwagandha, can interact with medications such as those for thyroid, blood pressure or diabetes, and with sedatives, so we check your medication list before suggesting any herb and ask you to confirm with your doctor or pharmacist. We can share your plan with your doctor if you choose, and we factor in anything they change."),
 ("What happens in the first Ayurvedic session?",
  "A private video or phone call about your energy, sleep, digestion, stress, routine, any medications and what you have already tried. We look at your constitution and your current state, then agree the first one or two changes and what you will track, so you can see for yourself how the plan is working."),
 ("Is it fully online, and where do you work with men?",
  'Yes. Odin Health Lab is telehealth only and serves men across Canada and the USA. Sessions happen by secure video, phone and message, so there are no clinic visits. See our <a href="%s/">low testosterone and andropause overview</a> for how the service works, or read our <a href="%s/privacy">Privacy Policy</a> for how we protect your information.' % (SITE, SITE)),
]

# ---------- 1 · HERO: three overlapping dosha circles breathe around you; an outer ring turns ----------
def hero_doshas():
    s = ['<defs><radialGradient id="ay-hg"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.18"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs>',
         '<circle cx="240" cy="160" r="150" fill="url(#ay-hg)"/>',
         '<circle cx="240" cy="160" r="138" fill="none" stroke="rgba(196,255,73,0.16)" stroke-width="2"/>']
    s.append(dr('M240 22a138 138 0 1 1 -0.1 0', 0.2, 2.2, 'rgba(196,255,73,0.55)', 2))
    # orbit: three dots on the ring, the whole group turns slowly
    s.append('<g class="ay-orb">' + ''.join('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (f(240 + 138 * math.cos(a)), f(160 + 138 * math.sin(a)), r, c)
             for a, r, c in ((-math.pi / 2, 6, LIME), (math.pi / 6, 4.5, WHITE), (5 * math.pi / 6, 4.5, SAGE))) + '</g>')
    circ = [(240, 122, LIME, 'wind', 240, 78), (205, 182, WHITE, 'flame', 162, 210), (275, 182, SAGE, 'drop', 318, 210)]
    for k, (cx, cy, col, ic, ix, iy) in enumerate(circ):
        s.append('<g class="pop t" style="--d:%s"><g class="ay-br t" style="--k:%d"><circle cx="%d" cy="%d" r="72" fill="%s" fill-opacity="0.07" stroke="%s" stroke-width="2.6"/></g></g>' % (0.2 + k * 0.15, k, cx, cy, col, col))
    for k, (cx, cy, col, ic, ix, iy) in enumerate(circ):
        s.append(node(ix, iy, 22, ic, 0.6 + k * 0.15, col if col != SAGE else WHITE, isz=24))
    s.append('<circle class="ay-pulse fx" cx="240" cy="162" r="26" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(node(240, 162, 24, 'you', 0.1, LIME, fill='#142e14', isz=28))
    return '\n'.join(s)

# ---------- 2 · WHAT AYURVEDA IS: a three-axis map; three people's mixes take turns, each person lights in sync ----------
def constitution_map():
    cx, cy, R = 150, 128, 92
    ang = [-90, 150, 30]
    P = lambda a, r: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
    s = []
    for g in (0.34, 0.67, 1.0):
        pts = ' '.join('%s,%s' % tuple(f(v) for v in P(a, R * g)) for a in ang)
        s.append('<polygon points="%s" fill="none" stroke="rgba(255,255,255,%s)" stroke-width="1.6" stroke-dasharray="3 6"/>' % (pts, 0.12 if g < 1 else 0.24))
    for k, a in enumerate(ang):
        x, y = P(a, R)
        s.append(dr('M%d %d L%s %s' % (cx, cy, f(x), f(y)), 0.2 + k * 0.1, 0.8, 'rgba(196,255,73,0.45)', 2))
    for k, (a, ic) in enumerate(zip(ang, ('wind', 'flame', 'drop'))):
        x, y = P(a, R + 22)
        s.append('<g class="pop t" style="--d:%s">%s</g>' % (0.5 + k * 0.1, ico(ic, x, y, 22, LIME if k == 0 else WHITE, 1.8)))
    mixes = [(0.92, 0.42, 0.36), (0.40, 0.90, 0.48), (0.36, 0.50, 0.92)]
    cols = [LIME, WHITE, SAGE]
    for k, m in enumerate(mixes):
        pts = [P(a, R * v) for a, v in zip(ang, m)]
        s.append('<g class="ay-mix" style="--k:%d"><polygon points="%s" fill="%s" fill-opacity="0.13" stroke="%s" stroke-width="2.6" stroke-linejoin="round"/>%s</g>'
                 % (k, ' '.join('%s,%s' % (f(x), f(y)) for x, y in pts), cols[k], cols[k], ''.join('<circle cx="%s" cy="%s" r="4" fill="%s"/>' % (f(x), f(y), cols[k]) for x, y in pts)))
    # three people on the right
    for k, x in enumerate((330, 410, 490)):
        s.append('<g class="pop t" style="--d:%s"><circle cx="%d" cy="128" r="28" fill="#0f240f" stroke="%s" stroke-width="2.6"/>%s</g>' % (0.6 + k * 0.12, x, cols[k] if k != 2 else 'rgba(255,255,255,0.6)', ico('you', x, 128, 30, cols[k], 1.6)))
        s.append('<circle class="ay-who" style="--k:%d" cx="%d" cy="128" r="35" fill="none" stroke="%s" stroke-width="2.4"/>' % (k, x, cols[k]))
        s.append('<path class="dr" pathLength="1" style="--d:%s" d="M%d 178h40" stroke="%s" stroke-width="3" stroke-linecap="round" fill="none"/>' % (0.9 + k * 0.1, x - 20, cols[k]))
    return '\n'.join(s)

# ---------- 3 · MEN / LOW-T LINK: four meshed gears (energy, sleep, stress, drive) turn together ----------
def gear_path(cx, cy, r, n, h=7):
    pts = []
    for i in range(n * 4):
        a = 2 * math.pi * i / (n * 4)
        rr = r + h if (i % 4) in (1, 2) else r - h
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return 'M' + ' L'.join('%s %s' % (f(x), f(y)) for x, y in pts) + 'Z'

def gears():
    c0 = (280, 112, 56, 12)
    def at(c, r2, deg):
        d = c[2] + r2 + 4
        return (c[0] + d * math.cos(math.radians(deg)), c[1] + d * math.sin(math.radians(deg)))
    l = at(c0, 40, 160) + (40, 9)
    r = at(c0, 40, -28) + (40, 9)
    d = at(r, 28, 42) + (28, 7)
    spec = [(c0, 'batt', LIME, 0, 'n'), (l, 'sleep', WHITE, 1, 'r'), (r, 'stress', WHITE, 2, 'r'), (d, 'flame', LIME, 3, 'n')]
    s = ['<defs><radialGradient id="ay-gg"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.16"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="280" cy="112" rx="250" ry="100" fill="url(#ay-gg)"/>']
    for (x, y, rr, n), ic, col, k, dirn in spec:
        dur = n * 2.0
        s.append('<g class="pop t" style="--d:%s"><g class="ay-gear ay-gear--%s t" style="--gd:%ss"><path d="%s" fill="#0f240f" stroke="%s" stroke-width="2.6" stroke-linejoin="round"/>'
                 '<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-opacity="0.35" stroke-width="2" stroke-dasharray="3 6"/></g>%s</g>'
                 % (0.15 + k * 0.15, dirn, f(dur), gear_path(x, y, rr, n), col if col == LIME else 'rgba(255,255,255,0.75)', f(x), f(y), f(rr - 14), col, ico(ic, x, y, int(rr * 0.8), col, 1.7)))
    return '\n'.join(s)

# ---------- 4 · PILLARS: four small scenes (steaming bowl, swinging metronome, growing sprig, breathing circle) ----------
def pillars():
    s = []
    for i in range(4):
        s.append('<rect class="pop" style="--d:%s" x="%d" y="10" width="126" height="150" rx="18" fill="rgba(255,255,255,0.03)" stroke="rgba(196,255,73,0.22)" stroke-width="1.5"/>' % (0.08 + i * 0.1, 10 + i * 140))
    # food: bowl + steam
    s.append('<g class="pop t" style="--d:0.3"><path d="M33 96h80a40 40 0 0 1-80 0z" fill="rgba(196,255,73,0.16)" stroke="#c4ff49" stroke-width="3" stroke-linejoin="round"/><path d="M28 96h90" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M58 135h30" stroke="rgba(255,255,255,0.5)" stroke-width="3" stroke-linecap="round"/></g>')
    for k, x in enumerate((55, 73, 91)):
        s.append('<path class="ay-steam" style="--k:%d" d="M%d 82c-6-8 6-12 0-20s6-12 0-20" fill="none" stroke="%s" stroke-width="2.6" stroke-linecap="round"/>' % (k, x, '#fff' if k == 1 else '#c4ff49'))
    # rhythm: metronome
    s.append('<g class="pop t" style="--d:0.4"><path d="M180 140l22-104h12l22 104z" fill="#142e14" stroke="rgba(255,255,255,0.75)" stroke-width="2.6" stroke-linejoin="round"/><path d="M176 140h64" stroke="#fff" stroke-width="3" stroke-linecap="round"/></g>')
    s.append('<g class="ay-arm"><path d="M208 126V46" stroke="#c4ff49" stroke-width="3" stroke-linecap="round"/><rect x="200" y="62" width="16" height="12" rx="3" fill="#c4ff49"/></g><circle cx="208" cy="126" r="4.5" fill="#fff"/>')
    # herbs: sprig grows
    s.append('<path d="M310 142h80" stroke="rgba(255,255,255,0.4)" stroke-width="2.6" stroke-linecap="round"/>')
    s.append(dr('M350 142C350 116 346 90 352 40', 0.4, 1.4, LIME, 3))
    for k, (x, y, rot, flip) in enumerate(((350, 118, -30, 1), (349, 96, 30, -1), (350, 72, -36, 1), (352, 50, 28, -1))):
        s.append('<g class="pop t" style="--d:%s"><g class="ay-leaf" style="--k:%d;transform-origin:%dpx %dpx"><path d="M%d %d c%d -14 %d -18 %d -16 c%d 10 %d 16 %d 16z" fill="rgba(196,255,73,0.25)" stroke="#c4ff49" stroke-width="2.2" stroke-linejoin="round"/></g></g>'
                 % (0.9 + k * 0.15, k, x, y, x, y, 10 * flip, 22 * flip, 28 * flip, -2 * flip, -12 * flip, -28 * flip))
    # breath & movement: breathing circles + wave
    s.append('<circle class="ay-in fx" cx="493" cy="78" r="38" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append('<g class="pop t" style="--d:0.5"><g class="ay-lung t"><circle cx="493" cy="78" r="28" fill="rgba(196,255,73,0.14)" stroke="#c4ff49" stroke-width="3"/></g>%s</g>' % ico('breath', 493, 78, 26, WHITE, 1.8))
    s.append(dr('M447 134c8-8 15-8 23 0s15 8 23 0 15-8 23 0 15 8 23 0', 0.7, 1.2, 'rgba(255,255,255,0.7)', 2.6))
    return '\n'.join(s)

# ---------- 5 · DAILY RHYTHM: sun and moon trade places over a horizon; day markers light as the sun passes ----------
DIAL_T = 18.0
def day_dial():
    cx, cy, R = 220, 196, 150
    s = ['<defs><clipPath id="ay-sky"><rect x="0" y="0" width="440" height="198"/></clipPath>'
         '<linearGradient id="ay-dg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c4ff49" stop-opacity="0"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0.14"/></linearGradient></defs>']
    s.append('<path d="M%d %dA%d %d 0 0 1 %d %dZ" fill="url(#ay-dg)"/>' % (cx - R, cy, R, R, cx + R, cy))
    s.append('<path d="M%d %dA%d %d 0 0 1 %d %d" fill="none" stroke="rgba(255,255,255,0.18)" stroke-width="2.4" stroke-dasharray="2 8" stroke-linecap="round"/>' % (cx - R, cy, R, R, cx + R, cy))
    s.append(dr('M%d %dA%d %d 0 0 1 %d %d' % (cx - R, cy, R, R, cx + R, cy), 0.2, 2.0, 'rgba(196,255,73,0.6)', 2.4))
    for k, (x, y, r) in enumerate(((62, 46, 2.6), (390, 36, 3), (300, 22, 2.2), (120, 90, 2))):
        s.append('<circle class="ay-star" style="--k:%d" cx="%d" cy="%d" r="%s" fill="#c4ff49"/>' % (k, x, y, r))
    # day markers: wake, breakfast, main meal at midday, move, dinner, wind-down
    marks = [(0.08, 'sun'), (0.24, 'bowl'), (0.5, 'food'), (0.68, 'train'), (0.82, 'bowl'), (0.94, 'moon')]
    for k, (fr, ic) in enumerate(marks):
        a = math.pi * (1 - fr)
        x, y = cx + R * math.cos(a), cy - R * math.sin(a)
        s.append('<g class="ay-mk t" style="--dl:%ss"><g class="pop t" style="--d:%s"><circle cx="%s" cy="%s" r="15" fill="#0f240f" stroke="#c4ff49" stroke-width="2.2"/>%s</g></g>'
                 % (f(fr * DIAL_T / 2 - DIAL_T), 0.6 + k * 0.12, f(x), f(y), ico(ic, x, y, 18, LIME if k % 2 == 0 else WHITE, 1.8)))
    # the sky wheel: sun starts at the left horizon, moon opposite; group turns clockwise round (cx, cy)
    s.append('<g clip-path="url(#ay-sky)"><g class="ay-sky"><g transform="translate(%d %d)"><circle r="17" fill="#c4ff49"/><circle r="26" fill="none" stroke="#c4ff49" stroke-opacity="0.4" stroke-width="2.4"/></g>'
             '<g transform="translate(%d %d)"><circle r="16" fill="#0f240f" stroke="#fff" stroke-width="2.6"/>%s</g></g></g>' % (cx - R + 28, cy, cx + R - 28, cy, ico('moon', 0, 0, 20, WHITE, 1.8)))
    s.append('<path d="M30 %dH410" stroke="rgba(255,255,255,0.4)" stroke-width="3" stroke-linecap="round"/>' % (cy + 1))
    s.append('<path d="M70 %dh300" stroke="rgba(255,255,255,0.15)" stroke-width="2" stroke-dasharray="2 9" stroke-linecap="round"/>' % (cy + 26))
    return '\n'.join(s)

# ---------- 6 · RELATED: branches grow from an Ayurveda node; sap pulses run out to each related page ----------
def branches():
    c = (280, 120)
    leaves = [(80, 54, 'labs'), (150, 172, 'coach'), (280, 30, 'home'), (410, 172, 'caps'), (480, 54, 'clock')]
    s = ['<defs><radialGradient id="ay-rg"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.2"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><circle cx="280" cy="120" r="100" fill="url(#ay-rg)"/>']
    s.append('<path d="M280 210V150" stroke="rgba(196,255,73,0.35)" stroke-width="4" stroke-linecap="round"/>')
    for i, (x, y, ic) in enumerate(leaves):
        mx = (c[0] + x) / 2
        d, pts = path(('M', c[0], c[1]), ('C', mx, c[1], mx if y != 30 else 280, y, x, y), n=16)
        s.append('<path d="%s" stroke="rgba(196,255,73,0.18)" stroke-width="3" fill="none" stroke-linecap="round"/>' % d)
        s.append(dr(d, 0.3 + i * 0.1, 1.0, LIME, 2.4))
        s.append(dot('ay-sap%d fx' % i, 4.5, WHITE))
        G.travel('ay-sap%d' % i, pts, 8, 42, 10, delay='%ss' % f(-i * 2), rest=pts[-1], rest_opacity=0)
    s.append('<circle class="ay-pulse fx" cx="280" cy="120" r="34" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(node(280, 120, 30, 'lotus', 0.1, LIME, fill='#142e14', isz=34))
    for i, (x, y, ic) in enumerate(leaves):
        s.append(node(x, y, 24, ic, 0.6 + i * 0.12, WHITE if i % 2 else LIME, isz=26))
    return '\n'.join(s)

# ---------- 7 · FAQ: mortar and pestle; the pestle rocks, herb flecks rise ----------
FAQMOTIF = '''<path d="M14 52h92a46 40 0 0 1-92 0z" fill="rgba(196,255,73,0.08)" stroke="#c4ff49" stroke-width="3.5" stroke-linejoin="round"/>
<path d="M8 52h104" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><path d="M44 94h32" stroke="#c4ff49" stroke-width="3.5" stroke-linecap="round"/>
<g class="fq-pes"><path d="M66 50L92 12" stroke="#fff" stroke-width="7" stroke-linecap="round"/><circle cx="64" cy="52" r="5" fill="#fff"/></g>
<path class="dr" pathLength="1" style="--d:0.3;--dur:1s" d="M30 70c8 6 20 8 30 8" stroke="rgba(196,255,73,0.7)" stroke-width="3" stroke-linecap="round"/>
<circle class="fq-fl" style="--k:0" cx="40" cy="40" r="3" fill="#c4ff49"/><circle class="fq-fl" style="--k:1" cx="52" cy="34" r="2.6" fill="#fff"/><circle class="fq-fl" style="--k:2" cx="30" cy="36" r="2.4" fill="#c4ff49"/>'''

# ---------- 8 · FINAL: a sun rises over the horizon once, rays turn, a dotted path leads to it ----------
SUNRISE = '''<defs><clipPath id="ay-hz"><rect x="0" y="0" width="360" height="146"/></clipPath><radialGradient id="ay-sg"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.35"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs>
<circle cx="180" cy="146" r="110" fill="url(#ay-sg)"/>
<g clip-path="url(#ay-hz)"><g class="ay-rise"><g class="ay-rays">''' + ''.join(
    '<path d="M180 %d V%d" transform="rotate(%d 180 146)" stroke="#c4ff49" stroke-opacity="0.6" stroke-width="3" stroke-linecap="round"/>' % (146 - 62, 146 - 76, a) for a in range(-90, 91, 20)) + '''</g>
<circle cx="180" cy="146" r="46" fill="#c4ff49" fill-opacity="0.9"/><circle cx="180" cy="146" r="54" fill="none" stroke="#c4ff49" stroke-opacity="0.4" stroke-width="2.4"/></g></g>
<path d="M20 146H340" stroke="rgba(255,255,255,0.45)" stroke-width="3" stroke-linecap="round"/>
<path d="M40 186C90 176 130 168 180 150" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2.4" stroke-dasharray="2 9" stroke-linecap="round"/>
<ellipse class="ay-fp" style="--k:0" cx="60" cy="182" rx="8" ry="4" fill="#c4ff49"/><ellipse class="ay-fp" style="--k:1" cx="96" cy="174" rx="8" ry="4" fill="#c4ff49"/><ellipse class="ay-fp" style="--k:2" cx="132" cy="166" rx="8" ry="4" fill="#c4ff49"/>'''

# ---------- How-it-works step icons (48x48) ----------
STEPS = {
 "{{STEP1}}": '<rect x="9" y="5" width="30" height="38" rx="5"/><path d="M18 5h12v5H18z" fill="#0f240f"/><g class="ay-ck t" style="--k:0"><path d="M15 20l3 3 5-6" stroke="#fff"/></g><path d="M27 20h7" opacity="0.6"/><g class="ay-ck t" style="--k:1"><path d="M15 31l3 3 5-6" stroke="#fff"/></g><path d="M27 31h7" opacity="0.6"/>',
 "{{STEP2}}": '<rect x="13" y="4" width="22" height="40" rx="5"/><path d="M21 38h6"/><circle cx="24" cy="18" r="4" stroke="#fff"/><path d="M18 28c1-3 3-4 6-4s5 1 6 4" stroke="#fff"/><path class="ay-wv" style="--k:0" d="M7 17c-2 4-2 10 0 14"/><path class="ay-wv" style="--k:1" d="M41 17c2 4 2 10 0 14"/>',
 "{{STEP3}}": '<path d="M24 42V20" stroke="#fff"/><g class="ay-sp" style="--k:0;transform-origin:24px 30px"><path d="M24 30c-2-6-8-8-14-7 1 6 7 9 14 7z" fill="rgba(196,255,73,0.25)"/></g><g class="ay-sp" style="--k:1;transform-origin:24px 22px"><path d="M24 22c2-6 8-9 14-8-1 6-7 10-14 8z" fill="rgba(196,255,73,0.25)"/></g><path d="M14 42h20"/>',
 "{{STEP4}}": '<g class="ay-cyc t"><path d="M38 20a15 15 0 0 0-26-6"/><path d="M12 6v8h8"/><path d="M10 28a15 15 0 0 0 26 6" stroke="#fff"/><path d="M36 42v-8h-8" stroke="#fff"/></g><circle cx="24" cy="24" r="3" fill="#c4ff49" stroke="none"/>',
}

slots = {"{{HERO}}": hero_doshas(), "{{MAP}}": constitution_map(), "{{GEARS}}": gears(), "{{PILLARS}}": pillars(), "{{DIAL}}": day_dial(),
         "{{BRANCHES}}": branches(), "{{FAQMOTIF}}": FAQMOTIF, "{{SUNRISE}}": SUNRISE, "{{FAQ}}": faq_html(FAQ)}
slots.update(STEPS)

rd = lambda *p: open(os.path.join(*p), encoding="utf-8").read()
body = re.sub(r"\{\{CI:(\w+):(\d+)\}\}", lambda m: ci(m.group(1), int(m.group(2))), rd(HERE, "page.body.html"))
st, mo = G.css()
css = rd(HERE, "page.css").replace("/*@GEN_STATIC*/", st).replace("/*@GEN_MOTION*/", mo)
tmp = os.path.join(HERE, ".tmp"); os.makedirs(tmp, exist_ok=True)
open(os.path.join(tmp, "page.body.html"), "w", encoding="utf-8").write(body)
open(os.path.join(tmp, "page.css"), "w", encoding="utf-8").write(css)
ld = jsonld(SLUG, TITLE, DESC, "Ayurveda for energy, sleep and stress in men, including low testosterone (andropause) symptoms", "Ayurveda", FAQ)
assemble(tmp, SLUG, TITLE, DESC, OG_ALT, ld, slots)
shutil.copy(os.path.join(tmp, "page.html"), os.path.join(HERE, "page.html"))
shutil.rmtree(tmp)

# copy guards (Alex rules): no disclaimer blocks, no illustration captions, doctor mentions only inside the FAQ, no detox/cleanse promises
out = rd(HERE, "page.html")
main = out[out.index('<main'):out.index('</main>')]
nofaq = re.sub(r'<section id="faq"[\s\S]*?</section>', '', main)
txt = re.sub(r'<[^>]+>', ' ', nofaq)
for pat in (r'illustration only', r'class="disclaimer"', r'\b911\b', r'\b988\b', r'physician', r'\bdoctor', r'not a treatment', r'do not practi[cs]e medicine',
            r'5,000', r'\bdetox', r'\bcleans', r'clinical tradition', r'cortisol'):
    assert not re.search(pat, txt, re.I), "copy guard: " + pat
assert not re.search(r'illustration only|class="disclaimer"|\b911\b|\b988\b|\bdetox|\bcleans', main, re.I)
print("copy guards OK")
