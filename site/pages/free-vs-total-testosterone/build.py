"""Build /workspace/pages/free-vs-total-testosterone/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match. build() output is minified at the end (HighLevel save limit)."""
import sys, os, math, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "free-vs-total-testosterone"
TITLE = "Free vs Total Testosterone and SHBG | Odin Health Lab"
DESC = "Free vs total testosterone: how SHBG and albumin bind T, normal free T levels, calculated vs dialysis tests and what men in Canada and the USA can do."
OG_ALT = "Odin Health Lab: free vs total testosterone in men, SHBG, albumin, calculated free T and units"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 155, (len(TITLE), len(DESC))

common.ICONS.update({
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "calc": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8"/><path d="M8 12h.01M12 12h.01M16 12h.01M8 16h.01M12 16h.01M16 16h.01"/>',
 "clamp": '<path d="M6 6v6a6 6 0 0 0 12 0V6"/><circle cx="12" cy="12" r="2.4"/>',
 "swap": '<path d="M4 8h14l-3-3"/><path d="M20 16H6l3 3"/>',
 "up": '<path d="M12 19V5"/><path d="M6 11l6-6 6 6"/>',
 "down": '<path d="M12 5v14"/><path d="M6 13l6 6 6-6"/>',
 "filter": '<path d="M4 5h16l-6 8v6l-4-2v-4z"/>',
})

FAQ = [
 ("What is the difference between free and total testosterone?",
  "Total testosterone is all the testosterone in your blood: the part held tightly by SHBG, the part held loosely by albumin, and a small unbound part. Free testosterone is that unbound part, only 2 to 4 percent of the total according to the Endocrine Society (2018). Free plus albumin-bound testosterone is called bioavailable testosterone. Total T is still the first test. Free T helps when SHBG is unusual or total T sits near the lower limit. We read both with you and explain what they mean for your symptoms."),
 ("What is a normal free testosterone level for men?",
  "Each lab sets its own range, because the Endocrine Society notes that no harmonized free T range exists yet and results depend on the method used. The cut-off researchers use most comes from the European Male Ageing Study (NEJM, 2010): free T below 220 pmol/L (64 pg/mL), with total T below 11 nmol/L and at least three sexual symptoms, defined late-onset hypogonadism. Men in that study with normal total and free T averaged 326 pmol/L. Check the unit and the method printed on your report before you compare numbers."),
 ("What is SHBG and why does it matter?",
  "Sex hormone-binding globulin is the protein that holds most of your testosterone tightly. High SHBG, which comes with aging, liver disease, an overactive thyroid and some anticonvulsants, can make total T look normal while free T is low. Low SHBG, which comes with obesity, diabetes and an underactive thyroid, can make total T look low while free T is normal. In the Massachusetts Male Aging Study, SHBG was about 1.6 percent higher for each year of age. We look at what may be moving your SHBG and build the weight, nutrition, training and sleep plan around it."),
 ("My total testosterone is normal but I have low-T symptoms. What should I check?",
  "Ask for SHBG and a calculated free testosterone from the same fasting, early-morning sample. In a 2016 European Male Ageing Study analysis, men with normal total T but low calculated free T had higher SHBG and more sexual and physical symptoms. The Canadian Urological Association (2021) also points to look-alike conditions such as depression, an underactive thyroid and sleep disorders. We go through your symptoms and labs together and plan the next tests and lifestyle steps with you."),
 ("Which free testosterone test is most accurate?",
  "Equilibrium dialysis is the reference method. A free T calculated from total T, SHBG and albumin was almost identical to dialysis in a 1999 study by Vermeulen and colleagues. Direct analog immunoassays gave values that were only a fraction of the dialysis result, and the Endocrine Society says they are inaccurate and should not be used. If your report says direct or analog, ask for a calculated free T or a dialysis test from a reference lab."),
 ("How does Odin Health Lab work with my doctor?",
  'Odin Health Lab is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We work alongside your own doctor: we go through your symptoms and lab results with you, including total T, SHBG, albumin and free T, help you prepare questions such as which free T method to ask for, build your nutrition, training, sleep and stress plan, and track your progress with follow-up check-ins and repeat labs. We can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

def txt(x, y, s, size=13, fill='#fff', op=0.85, anchor='middle', extra=''):
    a = '' if anchor == 'middle' else ' text-anchor="%s"' % anchor  # middle is inherited from .mg-svg (page.css)
    return '<text x="%s" y="%s" font-size="%s" fill="%s" fill-opacity="%s"%s%s>%s</text>' % (f(x), f(y), size, fill, op, a, extra, s)

def clamp(x, y, cls='', k=0, sc=1.0, col=LIME):
    """SHBG carrier: a U-shaped clamp holding a testosterone dot."""
    return ('<g transform="translate(%s %s) scale(%s)"><g class="%s" style="--k:%d"><path d="M-17 -16V0a17 17 0 0 0 34 0V-16" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>'
            '<circle cx="0" cy="-1" r="7.5" fill="#fff"/></g></g>') % (f(x), f(y), sc, cls, k, col)

def albumin(x, y, cls='', k=0):
    return ('<g transform="translate(%s %s)"><ellipse rx="27" ry="18" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.7)" stroke-width="2" stroke-dasharray="4 4"/>'
            '<g class="%s" style="--k:%d"><circle cx="8" cy="-4" r="7" fill="#fff" fill-opacity="0.9"/></g></g>') % (f(x), f(y), cls, k)

# ---------- hero: most T rides on carriers, a few free molecules glow ----------
def hero():
    s = ['<defs><radialGradient id="ft-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.14"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="225" ry="135" fill="url(#ft-g)"/>']
    s.append(txt(90, 34, 'SHBG: holds tight', 12, '#c4ff49', 0.95)); s.append(txt(240, 34, 'Albumin: loose', 12, '#fff', 0.85)); s.append(txt(392, 34, 'Free', 12, '#c4ff49', 0.95))
    for k, (x, y) in enumerate(((90, 90), (60, 170), (120, 245), (150, 160))):
        s.append(clamp(x, y, 'hr-cl', k))
    for k, (x, y) in enumerate(((240, 100), (220, 190), (270, 255))):
        s.append(albumin(x, y, 'hr-al', k))
    s.append('<path d="M330 60V280" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="3 7"/>')
    loops = [((360, 110), (440, 80), (450, 160), (380, 170)), ((410, 230), (350, 250), (360, 190), (430, 200))]
    for i, (a, b, c, d) in enumerate(loops):
        pd, pts = path(('M', a[0], a[1]), ('C', b[0], b[1], c[0], c[1], d[0], d[1]), ('C', a[0] - 10, d[1] - 10, a[0] - 30, a[1] + 30, a[0], a[1]), n=6)
        s.append(dot('hr-f%d fx' % i, 7, LIME, ring=True)); G.travel('hr-f%d' % i, pts, 4, 92, 9, delay='%ss' % f(-i * 4), rest=pts[0], rest_opacity=0, fade=3)
    s.append('<g class="hr-fs"><circle cx="400" cy="130" r="7" fill="#c4ff49"/><circle class="hr-ring fx" cx="400" cy="130" r="12" fill="none" stroke="#c4ff49" stroke-width="2"/></g>')
    s.append(txt(240, 304, 'Only a small share of testosterone travels free', 13, '#fff', 0.85))
    return '\n'.join(s)

# ---------- split: SHBG-bound / albumin-bound / free, with bioavailable + total brackets ----------
def split():
    s = []
    segs = [(40, 300, 'rgba(196,255,73,0.22)', '#c4ff49', 'SHBG-bound (tight)'), (300, 498, 'rgba(255,255,255,0.12)', 'rgba(255,255,255,0.7)', 'Albumin-bound (loose)')]
    for k, (x1, x2, fill, st, lab) in enumerate(segs):
        s.append('<g class="sp-seg" style="--k:%d"><rect x="%d" y="100" width="%d" height="48" rx="8" fill="%s" stroke="%s" stroke-width="2"/></g>' % (k, x1, x2 - x1 - 4, fill, st))
        s.append(txt((x1 + x2) / 2 - 2, 129, lab, 13, '#c4ff49' if k == 0 else '#fff', 0.92))
    s.append('<g class="sp-free"><rect x="500" y="100" width="20" height="48" rx="6" fill="#c4ff49"/></g>')
    s.append('<path d="M510 96V52" stroke="#c4ff49" stroke-width="1.6" stroke-dasharray="3 4"/>')
    s.append(txt(520, 42, 'Free: 2 to 4 percent', 13, '#c4ff49', 0.95, 'end'))
    s.append(dr('M300 88V80H520V88', 0.4, 0.9, 'rgba(255,255,255,0.75)', 2))
    s.append(txt(400, 70, 'Bioavailable', 12, '#fff', 0.85))
    s.append(dr('M40 160V170H520V160', 0.6, 1.1, LIME, 2))
    s.append(txt(280, 194, 'Total testosterone = all three', 13, '#c4ff49', 0.95))
    for i in range(2):
        pd, pts = path(('M', 510, 112 + i * 18), ('C', 520 + i * 8, 90, 530, 70, 540, 58 + i * 14), n=5)
        s.append(dot('sp-p%d fx' % i, 4, LIME)); G.travel('sp-p%d' % i, pts, 10, 60, 5, delay='%ss' % f(-i * 2.5), rest=pts[0], rest_opacity=0, fade=4)
    s.append(txt(280, 222, 'Albumin lets go easily in tissue; SHBG holds on', 11, '#fff', 0.65))
    return '\n'.join(s)

# ---------- SHBG drivers: lowers vs raises, needle swings ----------
def shbg():
    s = []
    cx, cy, r = 280, 170, 70
    s.append('<path d="M%d %dA%d %d 0 0 1 %d %d" stroke="rgba(255,255,255,0.3)" stroke-width="10" stroke-linecap="round" fill="none"/>' % (cx - r, cy, r, r, cx + r, cy))
    s.append('<path d="M%d %dA%d %d 0 0 1 %d %d" stroke="#c4ff49" stroke-opacity="0.8" stroke-width="10" stroke-linecap="round" fill="none"/>' % (cx - 18, cy - r + 2, r, r, cx + 18, cy - r + 2))
    s.append('<g class="sb-nd"><path d="M%d %dV%d" stroke="#c4ff49" stroke-width="4" stroke-linecap="round"/></g>' % (cx, cy, cy - r + 16))
    s.append('<circle cx="%d" cy="%d" r="8" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/>' % (cx, cy))
    s.append(txt(cx, cy + 30, 'SHBG', 15, '#c4ff49', 0.95)); s.append(txt(cx - r, cy + 30, 'Low', 11, '#fff', 0.7)); s.append(txt(cx + r, cy + 30, 'High', 11, '#fff', 0.7))
    s.append(txt(110, 30, 'Lowers SHBG', 13, '#fff', 0.9)); s.append(txt(450, 30, 'Raises SHBG', 13, '#c4ff49', 0.95))
    lo = ['Obesity', 'Diabetes', 'Underactive thyroid', 'Steroid medicines']
    hi = ['Aging', 'Liver disease', 'Overactive thyroid', 'Some anticonvulsants']
    for k, lab in enumerate(lo):
        y = 52 + k * 46
        s.append('<g class="sb-it" style="--k:%d"><rect x="20" y="%d" width="180" height="36" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.35)" stroke-width="1.5"/>%s%s</g>' % (k, y, ico('down', 40, y + 18, 18, WHITE, 2.2), txt(56, y + 23, lab, 12, '#fff', 0.9, 'start')))
    for k, lab in enumerate(hi):
        y = 52 + k * 46
        s.append('<g class="sb-it" style="--k:%d"><rect x="360" y="%d" width="180" height="36" rx="10" fill="rgba(196,255,73,0.06)" stroke="rgba(196,255,73,0.5)" stroke-width="1.5"/>%s%s</g>' % (k + 4, y, ico('up', 380, y + 18, 18, LIME, 2.2), txt(396, y + 23, lab, 12, '#fff', 0.9, 'start')))
    return '\n'.join(s)

# ---------- calculator: total T + SHBG + albumin -> calculated free T ----------
def calc():
    s = []
    ins = [('Total T', 'tube'), ('SHBG', 'clamp'), ('Albumin', 'drop')]
    for k, (lab, ic) in enumerate(ins):
        y = 30 + k * 66
        s.append('<g class="pop t" style="--d:%s"><rect x="24" y="%d" width="140" height="46" rx="12" fill="#0f240f" stroke="%s" stroke-width="2"/></g>' % (0.1 + k * 0.12, y, LIME if k != 1 else 'rgba(255,255,255,0.7)'))
        s.append(ico(ic, 50, y + 23, 22, LIME, 1.8)); s.append(txt(70, y + 28, lab, 13, '#fff', 0.92, 'start'))
        pd, pts = path(('M', 164, y + 23), ('C', 200, y + 23, 210, 120, 246, 120), n=6)
        s.append('<path d="%s" stroke="rgba(196,255,73,0.25)" stroke-width="2.2" stroke-dasharray="2 6" fill="none"/>' % pd)
        s.append(dot('cc-i%d fx' % k, 5, WHITE if k == 1 else LIME)); G.travel('cc-i%d' % k, pts, 4 + k * 8, 30 + k * 8, 7, rest=pts[0], rest_opacity=0, fade=3)
    s.append('<rect x="246" y="52" width="116" height="140" rx="16" fill="#142e14" stroke="#c4ff49" stroke-width="2.4"/>')
    s.append('<rect x="260" y="66" width="88" height="34" rx="6" fill="#0f240f" stroke="rgba(196,255,73,0.5)" stroke-width="1.4"/>')
    s.append('<g class="cc-scr">%s</g>' % txt(304, 89, 'Free T', 13, '#c4ff49', 0.95))
    for i in range(3):
        for j in range(3):
            s.append('<rect class="cc-key" style="--k:%d" x="%d" y="%d" width="22" height="18" rx="4" fill="#fff" fill-opacity="0.35"/>' % (i * 3 + j, 263 + j * 30, 112 + i * 24))
    pd, pts = path(('M', 362, 122), ('L', 410, 122))
    s.append('<path d="M362 122H410" stroke="rgba(196,255,73,0.3)" stroke-width="2.4" stroke-dasharray="2 6"/>')
    s.append(dot('cc-o fx', 6, LIME, ring=True)); G.travel('cc-o', pts, 46, 62, 7, rest=pts[-1], rest_opacity=0, fade=3)
    s.append('<g class="cc-out"><rect x="410" y="94" width="130" height="56" rx="14" fill="rgba(196,255,73,0.12)" stroke="#c4ff49" stroke-width="2.4"/></g>')
    s.append(txt(475, 118, 'Free T', 14, '#c4ff49', 0.95)); s.append(txt(475, 138, 'calculated', 11, '#fff', 0.75))
    s.append(txt(280, 228, 'An accurate total T, SHBG and albumin go in', 12, '#fff', 0.75))
    return '\n'.join(s)

# ---------- methods: dialysis membrane + three method rows ----------
def methods():
    s = ['<rect x="30" y="20" width="440" height="128" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.25)" stroke-width="1.6"/>']
    s.append('<g class="me-mb"><path d="M270 24V144" stroke="#c4ff49" stroke-width="3" stroke-dasharray="6 6"/></g>')
    s.append(clamp(80, 70, 'me-cl', 0, 0.8)); s.append(clamp(150, 118, 'me-cl', 1, 0.8)); s.append(albumin(200, 60, 'hr-al', 1))
    s.append(txt(150, 140, 'Bound: stays behind', 11, '#fff', 0.7)); s.append(txt(370, 140, 'Only free T crosses', 11, '#c4ff49', 0.9))
    for i in range(3):
        y = 52 + i * 30
        pd, pts = path(('M', 220, y), ('C', 250, y - 8, 290, y + 8, 330 + i * 30, y), n=5)
        s.append(dot('me-p%d fx' % i, 5, LIME)); G.travel('me-p%d' % i, pts, 6, 50, 7.5, delay='%ss' % f(-i * 2.5), rest=pts[-1], rest_opacity=0, fade=4)
    s.append(txt(490, 60, 'Dialysis', 12, '#c4ff49', 0.95, 'start')); s.append(txt(490, 78, 'membrane', 11, '#fff', 0.7, 'start'))
    rows = [('check', 'Equilibrium dialysis: the reference method', LIME), ('check', 'Calculated (Vermeulen): a close match', LIME), ('x', 'Direct analog test: inaccurate, avoid', WHITE)]
    for k, (ic, lab, col) in enumerate(rows):
        y = 176 + k * 28
        mark = ('<circle cx="46" cy="%d" r="10" fill="#c4ff49"/><path d="M41 %dl3.5 3.5 7-8" fill="none" stroke="#0f240f" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>' % (y, y)) if ic == 'check' else \
               ('<circle cx="46" cy="%d" r="10" fill="none" stroke="#fff" stroke-opacity="0.75" stroke-width="2"/><path d="M42 %dl8 8M50 %dl-8 8" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>' % (y, y - 4, y - 4))
        s.append('<g class="me-row" style="--k:%d">%s%s</g>' % (k, mark, txt(66, y + 5, lab, 13, '#c4ff49' if k < 2 else '#fff', 0.92, 'start')))
    return '\n'.join(s)

# ---------- units dial: nmol/L inner, ng/dL outer ----------
def units():
    s = []
    cx, cy, r = 160, 170, 120
    ang = lambda v: math.pi + v / 35 * math.pi
    s.append('<path d="M%d %dA%d %d 0 0 1 %d %d" stroke="rgba(255,255,255,0.35)" stroke-width="2.4" fill="none"/>' % (cx - r, cy, r, r, cx + r, cy))
    s.append('<path d="M%d %dA%d %d 0 0 1 %d %d" stroke="rgba(196,255,73,0.35)" stroke-width="8" fill="none"/>' % (cx - r + 18, cy, r - 18, r - 18, cx + r - 18, cy))
    for v in range(0, 36, 5):
        a = ang(v)
        s.append('<path d="M%s %sL%s %s" stroke="#fff" stroke-opacity="0.6" stroke-width="2" stroke-linecap="round"/>' % (f(cx + (r - 8) * math.cos(a)), f(cy + (r - 8) * math.sin(a)), f(cx + r * math.cos(a)), f(cy + r * math.sin(a))))
    for v in (0, 10, 20, 30):
        a = ang(v)
        s.append(txt(cx + (r - 40) * math.cos(a), cy + (r - 40) * math.sin(a) + 4, str(v), 12, '#c4ff49', 0.95))
        s.append(txt(cx + (r + 18) * math.cos(a), cy + (r + 18) * math.sin(a) + 4, str(int(round(v * 28.84))), 12, '#fff', 0.85))
    s.append('<g class="un-nd"><path d="M%d %dV%d" stroke="#c4ff49" stroke-width="4" stroke-linecap="round"/></g>' % (cx, cy, cy - r + 26))
    s.append('<circle cx="%d" cy="%d" r="8" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/>' % (cx, cy))
    s.append(txt(cx, cy + 26, 'nmol/L inside, ng/dL outside', 11, '#fff', 0.75))
    pairs = [('9.2 nmol/L', '264 ng/dL'), ('11 nmol/L', '320 ng/dL'), ('220 pmol/L', '64 pg/mL')]
    for k, (a, b) in enumerate(pairs):
        y = 30 + k * 62
        s.append('<g class="un-pr" style="--k:%d"><rect x="330" y="%d" width="210" height="48" rx="12" fill="rgba(255,255,255,0.04)" stroke="rgba(196,255,73,0.45)" stroke-width="1.6"/>%s%s%s</g>'
                 % (k, y, txt(352, y + 30, a, 13, '#c4ff49', 0.95, 'start'), ico('swap', 444, y + 24, 18, WHITE, 2), txt(530, y + 30, b, 13, '#fff', 0.9, 'end')))
    s.append(txt(435, 224, 'Total T: x 28.8 = ng/dL', 12, '#fff', 0.8)); s.append(txt(435, 244, 'Free T: pg/mL x 3.47 = pmol/L', 12, '#c4ff49', 0.9))
    return '\n'.join(s)

# ---------- normal ranges: harmonized total T band, free T cut-off, lab limits vary ----------
def normal():
    s = []
    X = lambda v, mx: 40 + 480 * v / mx
    s.append(txt(40, 34, 'Total testosterone, ng/dL', 12, '#fff', 0.85, 'start'))
    s.append('<path d="M40 70H520" stroke="rgba(255,255,255,0.35)" stroke-width="3" stroke-linecap="round"/>')
    s.append('<g class="nr-band"><rect x="%s" y="58" width="%s" height="24" rx="8" fill="#c4ff49" fill-opacity="0.3" stroke="#c4ff49" stroke-width="1.6"/></g>' % (f(X(264, 1000)), f(X(916, 1000) - X(264, 1000))))
    s.append(txt(X(264, 1000), 100, '264', 12, '#c4ff49', 0.95)); s.append(txt(X(916, 1000), 100, '916', 12, '#c4ff49', 0.95))
    s.append(txt((X(264, 1000) + X(916, 1000)) / 2, 50, 'Harmonized range, men 19 to 39', 11, '#fff', 0.75))
    s.append(txt(40, 140, 'Free testosterone, pmol/L', 12, '#fff', 0.85, 'start'))
    s.append('<path d="M40 176H520" stroke="rgba(255,255,255,0.35)" stroke-width="3" stroke-linecap="round"/>')
    s.append('<g class="nr-fz"><rect x="%s" y="164" width="60" height="24" rx="8" fill="#fff" fill-opacity="0.12"/></g>' % f(X(220, 500) - 30))
    s.append('<path d="M%s 156V196" stroke="#c4ff49" stroke-width="2.4" stroke-dasharray="4 4"/>' % f(X(220, 500)))
    s.append(txt(X(220, 500), 214, '220 cut-off (EMAS)', 12, '#c4ff49', 0.95))
    s.append('<path d="M%s 166V186" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' % f(X(326, 500)))
    s.append(txt(X(326, 500) + 6, 156, '326 average', 12, '#fff', 0.85, 'start'))
    s.append(txt(470, 234, 'Lab limits vary', 11, '#fff', 0.65))
    pd, pts = path(('M', 60, 176), ('L', 500, 176))
    s.append(dot('nr-d fx', 6, LIME, ring=True)); G.travel('nr-d', pts, 8, 80, 9, rest=pts[0], rest_opacity=0, fade=4, ease='ease-in-out')
    return '\n'.join(s)

# ---------- EMAS quadrants: normal total / low free stands out ----------
def quad():
    s = []
    s.append(txt(225, 30, 'Free T normal', 12, '#fff', 0.85)); s.append(txt(385, 30, 'Free T low', 12, '#c4ff49', 0.95))
    s.append(txt(138, 95, 'Total T', 12, '#fff', 0.85, 'end')); s.append(txt(138, 111, 'normal', 12, '#fff', 0.85, 'end'))
    s.append(txt(138, 195, 'Total T', 12, '#fff', 0.85, 'end')); s.append(txt(138, 211, 'low', 12, '#fff', 0.85, 'end'))
    cells = [(150, 44, '2,641 men', 'Reference group', False), (310, 44, '277 men', 'More symptoms, higher SHBG', True),
             (150, 144, '96 men', 'Lower SHBG, few features', False), (310, 144, '320 men', 'Low on both', False)]
    for k, (x, y, n, lab, hot) in enumerate(cells):
        s.append('<g class="qd-c" style="--k:%d"><rect x="%d" y="%d" width="150" height="90" rx="12" fill="%s" stroke="%s" stroke-width="%s"/></g>' % (k, x, y, 'rgba(196,255,73,0.14)' if hot else 'rgba(255,255,255,0.04)', '#c4ff49' if hot else 'rgba(255,255,255,0.3)', '2.6' if hot else '1.6'))
        s.append(txt(x + 75, y + 40, n, 16, '#c4ff49' if hot else '#fff', 0.95)); s.append(txt(x + 75, y + 62, lab, 10.5, '#fff', 0.8))
    s.append('<rect class="qd-ring fx" x="306" y="40" width="158" height="98" rx="15" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(txt(507, 82, 'Normal', 11, '#c4ff49', 0.9)); s.append(txt(507, 97, 'total T', 11, '#c4ff49', 0.9)); s.append(txt(507, 112, 'can hide it', 11, '#c4ff49', 0.9))
    return '\n'.join(s)

# ---------- when: decision branches ----------
def when():
    s = [node(70, 125, 30, 'tube', 0.1, LIME, fill='#142e14', isz=28)]
    s.append(txt(70, 178, 'Two morning', 11, '#fff', 0.8)); s.append(txt(70, 192, 'total T tests', 11, '#fff', 0.8))
    ends = [(46, 'Under 150 ng/dL', 'Free T rarely needed', WHITE), (125, '200 to 400 ng/dL', 'Add free T and SHBG', LIME), (204, 'SHBG-changing condition', 'Add free T and SHBG', LIME)]
    for k, (y, a, b, col) in enumerate(ends):
        pd, pts = path(('M', 100, 125), ('C', 180, 125, 220, y, 310, y), n=7)
        s.append('<path d="%s" stroke="%s" stroke-width="2.2" stroke-dasharray="2 6" fill="none"/>' % (pd, 'rgba(255,255,255,0.25)' if col == WHITE else 'rgba(196,255,73,0.35)'))
        s.append(dot('wh-p%d fx' % k, 5, col)); G.travel('wh-p%d' % k, pts, 4 + k * 30, 22 + k * 30, 9, rest=pts[-1], rest_opacity=0, fade=3)
        s.append('<g class="wh-t" style="--k:%d"><rect x="312" y="%d" width="228" height="56" rx="12" fill="%s" stroke="%s" stroke-width="1.8"/>%s%s</g>'
                 % (k, y - 28, 'rgba(196,255,73,0.08)' if col == LIME else 'rgba(255,255,255,0.04)', '#c4ff49' if col == LIME else 'rgba(255,255,255,0.35)', txt(328, y - 5, a, 13, '#c4ff49' if col == LIME else '#fff', 0.95, 'start'), txt(328, y + 15, b, 12, '#fff', 0.8, 'start')))
    return '\n'.join(s)

# ---------- help: lab report rows highlighted, plan out ----------
def help_fig():
    s = ['<g class="pop t" style="--d:0.1"><rect x="30" y="24" width="170" height="200" rx="14" fill="#142e14" stroke="rgba(255,255,255,0.6)" stroke-width="2"/></g>']
    s.append(txt(115, 50, 'Your labs', 12, '#c4ff49', 0.95))
    s.append('<g class="hp-hl"><rect x="40" y="64" width="150" height="30" rx="7" fill="#c4ff49" fill-opacity="0.22"/></g>')
    for k, lab in enumerate(('Total T', 'SHBG', 'Albumin', 'Free T')):
        y = 84 + k * 36
        s.append(txt(52, y, lab, 12, '#fff', 0.9, 'start'))
        s.append('<path d="M120 %dH%d" stroke="rgba(255,255,255,0.45)" stroke-width="4" stroke-linecap="round"/>' % (y - 4, 150 + (k * 9) % 30))
    for i, (a, b, cls, col) in enumerate([((200, 120), (252, 120), 'hp-in', WHITE), ((308, 120), (410, 120), 'hp-out', LIME)]):
        pd, pts = path(('M', a[0], a[1]), ('L', b[0], b[1]))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % pd)
        s.append(dot('%s fx' % cls, 5, col)); G.travel(cls, pts, 8, 46, 6, delay='%ss' % f(-i * 3), rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(280, 120, 28, 'coach', 0.3, LIME, fill='#173617', isz=28)); s.append(txt(280, 170, 'Telehealth review', 12, '#fff', 0.85))
    s.append(node(460, 100, 28, 'doc', 0.5, LIME, fill='#142e14', isz=28)); s.append(txt(460, 150, 'Your plan', 13, '#c4ff49', 0.95))
    for k, ic in enumerate(('food', 'train', 'sleep', 'stress')):
        x = 400 + k * 40
        s.append('<g class="hp-i" style="--k:%d"><circle cx="%d" cy="196" r="16" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/>%s</g>' % (k, x, ico(ic, x, 196, 17, LIME, 1.8)))
    return '\n'.join(s)

def final():
    s = ['<defs><radialGradient id="fn-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.3"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><circle cx="180" cy="110" r="90" fill="url(#fn-g)"/>']
    s.append('<g transform="translate(180 130)"><g class="fn-la"><path d="M-30 -30V0a30 30 0 0 0 30 30" fill="none" stroke="#c4ff49" stroke-width="5" stroke-linecap="round"/></g><g class="fn-ra"><path d="M30 -30V0a30 30 0 0 1 -30 30" fill="none" stroke="#c4ff49" stroke-width="5" stroke-linecap="round"/></g></g>')
    s.append('<g class="fn-dot"><circle cx="180" cy="128" r="12" fill="#fff"/><circle class="hr-ring fx" cx="180" cy="128" r="18" fill="none" stroke="#fff" stroke-width="2"/></g>')
    s.append(node(300, 60, 20, 'check', 0.4, LIME, fill='#142e14', isz=22))
    s.append(node(60, 60, 20, 'calc', 0.3, WHITE, isz=22))
    return '\n'.join(s)

FAQMOTIF = '''<g class="fq-cl"><path d="M14 40v16a14 14 0 0 0 28 0V40" stroke="#c4ff49" stroke-width="4" stroke-linecap="round"/><circle cx="28" cy="56" r="6" fill="#fff"/></g>
<path class="dr" pathLength="1" style="--d:0.25;--dur:1.1s" d="M70 36c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82" cy="64" r="3" fill="#fff"/>
<g class="fq-fr" style="--k:0"><circle cx="104" cy="22" r="5" fill="#c4ff49"/></g><g class="fq-fr" style="--k:1"><circle cx="50" cy="20" r="4" fill="#c4ff49"/></g>'''

def step_icons():
    return {
     "{{STEP1}}": '<path d="M8 12h32a2 2 0 0 1 2 2v18a2 2 0 0 1-2 2H22l-8 6v-6H8a2 2 0 0 1-2-2V14a2 2 0 0 1 2-2z"/><g class="hi-bl" style="--k:0"><circle cx="16" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="24" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="32" cy="23" r="2" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M12 6h10"/><path d="M14 6v26a3 3 0 0 0 6 0V6"/><path d="M14 20h6"/><g class="hi-gr" style="--k:0"><path d="M30 40V30M36 40V22M42 40V34" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<rect x="10" y="6" width="28" height="36" rx="4"/><path d="M16 14h16"/><g class="hi-bl" style="--k:0"><circle cx="18" cy="26" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="24" cy="26" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="30" cy="34" r="2" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP4}}": '<path d="M6 40h36"/><path d="M8 34l9-8 7 5 14-14"/><g class="hi-ck" style="--k:0"><path d="M30 8l4 4 8-9" stroke="#c4ff49"/></g>',
    }

def hub_nodes():
    icons = ['tube', 'list', 'compass', 'calendar', 'scale', 'sleep', 'gauge', 'coach', 'labs']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)
        out.append((round(280 + 230 * math.cos(a)), round(100 + 68 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{SPLIT}}": split(), "{{SHBG}}": shbg(), "{{CALC}}": calc(), "{{METHODS}}": methods(), "{{UNITS}}": units(),
         "{{NORMAL}}": normal(), "{{QUAD}}": quad(), "{{WHEN}}": when(), "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB,
         "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Free vs total testosterone in men: SHBG, albumin, calculated free testosterone and units",
      "Free vs total testosterone", "What is the difference between free and total testosterone?", slots, G, published="2026-10-16")

# ---- minify for HighLevel (keeps page.full.html): strip CSS comments, line indentation and blank lines outside <script> ----
p = os.path.join(HERE, "page.html")
full = open(p, encoding="utf-8").read()
open(os.path.join(HERE, "page.full.html"), "w", encoding="utf-8").write(full)
def mini(src):
    parts = re.split(r'(<script\b[\s\S]*?</script>)', src)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part); continue
        def css(m):
            c = re.sub(r'/\*[\s\S]*?\*/', '', m.group(0))
            c = re.sub(r'\n\s+', '\n', c); c = re.sub(r'\n{2,}', '\n', c)
            return c
        part = re.sub(r'<style\b[\s\S]*?</style>', css, part)
        part = re.sub(r'\n[ \t]+', '\n', part); part = re.sub(r'\n{2,}', '\n', part)
        out.append(part)
    return ''.join(out)
m = mini(full)
# page-local extra compaction (HighLevel save limit): drop unused icon symbols, tighten CSS punctuation inside <style>
used = set(re.findall(r'#pi-([\w-]+)', m))
m = re.sub(r'<symbol id="pi-([\w-]+)" viewBox="0 0 24 24">[\s\S]*?</symbol>', lambda x: x.group(0) if x.group(1) in used else '', m)
def tight(mm):
    c = mm.group(0)
    c = re.sub(r'\s*([{};])\s*', r'\1', c); c = re.sub(r':\s+', ':', c); c = re.sub(r',\s+', ',', c)
    return c
m = re.sub(r'(?<=<style>)[\s\S]*?(?=</style>)', tight, m)
open(p, "w", encoding="utf-8").write(m)
print("minified", len(full.encode()), "->", len(m.encode()), "bytes")
