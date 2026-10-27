"""Build /workspace/pages/low-testosterone-symptoms/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "low-testosterone-symptoms"
TITLE = "Low Testosterone Symptoms in Men | Odin Health Lab"
DESC = "Low testosterone symptoms in men: low libido, fewer morning erections, fatigue, belly fat, low mood, what mimics them and how low T is confirmed."
OG_ALT = "Odin Health Lab: low testosterone symptoms in men, the sexual, physical and mood signs of low T and how it is confirmed"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 158, (len(TITLE), len(DESC))

# extra icons used only on this page (merged before icons_svg() runs inside build())
common.ICONS.update({
 "bone": '<path d="M7 17l10-10"/><path d="M5.5 15.5a2.5 2.5 0 1 0 3 3"/><path d="M15.5 5.5a2.5 2.5 0 1 1 3 3"/><path d="M8.5 18.5a2.5 2.5 0 1 1-3-3"/><path d="M18.5 8.5a2.5 2.5 0 1 1-3-3"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/>',
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "split": '<path d="M4 7c4 0 8 2 16 6"/><path d="M4 7h7c2 0 2 10 4 10h5"/>',
})

FAQ = [
 ("What are the most common signs of low testosterone in men?",
  "Guidelines from the Endocrine Society (2018) and the Canadian Urological Association (2021) group the signs of low testosterone into three areas. Sexual: lower sex drive, fewer morning or spontaneous erections and erectile dysfunction. Physical: low energy, less muscle and strength, more body fat (especially around the belly) and lower bone density. Mood and thinking: low mood, irritability, poor concentration and memory, and sleep problems. In the European Male Ageing Study of 3,369 men aged 40 to 79, the three sexual symptoms had the clearest link with low testosterone."),
 ("Can low testosterone cause fatigue and belly fat?",
  "Low testosterone is linked with lower energy, less muscle and more body fat, and the link runs both ways: obesity also lowers testosterone, and the Canadian Urological Association lists it among the causes to address first. Fatigue and weight gain are also common with short or broken sleep, sleep apnea, an underactive thyroid, depression, stress and some medications. That overlap is why symptoms need to be read together with labs, not on their own."),
 ("Can I have low T symptoms with a normal testosterone level?",
  'Yes. The Canadian Urological Association notes that some men have symptoms at testosterone levels above the usual cut-off, and recommends looking for conditions with overlapping symptoms such as depression, an underactive thyroid and sleep disorders. When total testosterone is borderline, or when something may change SHBG (the protein that carries testosterone in the blood), the Endocrine Society recommends checking free testosterone. See <a href="%s/low-testosterone-labs-to-ask-for">which labs to ask for</a>.' % SITE),
 ("How is low testosterone confirmed?",
  "Low testosterone is confirmed when consistent symptoms line up with low results on two separate early-morning total testosterone tests. Testosterone peaks in the morning and food lowers it, so the Endocrine Society recommends fasting morning tests and a repeat to confirm; in that guideline, about three in ten men whose first result looked low had a normal result on repeat. The American Urological Association uses a total testosterone below 300 ng/dL on two early-morning tests, and the Canadian Urological Association recommends a morning draw between 7 and 11 a.m. and suggests below 10 nmol/L as a reasonable threshold. LH, free testosterone, SHBG and other labs then help explain why it is low."),
 ("Is andropause the same as low testosterone?",
  "Andropause, or the &ldquo;male menopause,&rdquo; is a popular term rather than a diagnosis. The NHS points out that testosterone falls gradually with age rather than dropping suddenly, and that many midlife symptoms come from stress, sleep, alcohol, weight or mood rather than hormones. The medical term for low testosterone with symptoms later in life is late-onset hypogonadism, and it is identified from symptoms plus blood tests. We use &ldquo;andropause&rdquo; because it is the word many men search for."),
 ("How does Odin Health Lab work with my doctor?",
  'Odin Health Lab is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We work alongside your own doctor: we go through your symptoms and lab results with you, build your sleep, training, nutrition and stress plan, and track your progress over time. We can share your symptom list, plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

def txt(x, y, s, size=13, fill='#fff', op=0.85, anchor='middle', extra=''):
    return '<text x="%s" y="%s" font-size="%s" fill="%s" fill-opacity="%s" text-anchor="%s"%s>%s</text>' % (f(x), f(y), size, fill, op, anchor, extra, s)

# ---------- 1 · HERO: three symptom clusters on an orbit loop around "you" ----------
def hero():
    s = ['<defs><radialGradient id="lh-g" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.16"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="220" ry="140" fill="url(#lh-g)"/>']
    top, bl, br, mid = (240, 58), (100, 228), (380, 228), (240, 160)
    d, pts = path(('M', top[0], top[1]), ('C', 340, 50, 410, 140, br[0], br[1]), ('C', 340, 290, 140, 290, bl[0], bl[1]), ('C', 70, 140, 140, 50, top[0], top[1]), n=18)
    s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>' % d)
    s.append(dr(d, 0.3, 1.8, 'rgba(196,255,73,0.45)', 2.2))
    s.append(dot('lh-o fx', 6, LIME, ring=True)); G.travel('lh-o', pts, 2, 97, 12, rest=pts[0], rest_opacity=0, fade=2)
    for i, a in enumerate([top, bl, br]):
        d2, p2 = path(('M', a[0], a[1]), ('L', mid[0], mid[1]))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.12)" stroke-width="2" stroke-dasharray="2 7" fill="none"/>' % d2)
        s.append(dot('lh-p%d fx' % i, 4.5, WHITE if i else LIME))
        G.travel('lh-p%d' % i, p2, 10, 45, 6, delay='%ss' % f(-i * 2), rest=a, rest_opacity=0, fade=3)
    s.append('<circle class="lh-ring fx" cx="240" cy="160" r="42" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(node(240, 160, 32, 'you', 0.15, LIME, fill='#142e14', isz=34))
    s.append(node(top[0], top[1], 26, 'heart', 0.3, LIME, fill='#142e14', isz=28))
    s.append(node(bl[0], bl[1], 26, 'batt', 0.45, WHITE, isz=28))
    s.append(node(br[0], br[1], 26, 'brain', 0.6, WHITE, isz=28))
    s.append(txt(290, 50, 'Sexual', 14, '#c4ff49', 0.95, 'start'))
    s.append(txt(100, 278, 'Energy + body', 14))
    s.append(txt(380, 278, 'Mood + focus', 14))
    s.append(txt(240, 214, 'You', 13, '#fff', 0.7))
    return '\n'.join(s)

# ---------- 2 · SEXUAL: falling testosterone line lights three symptom chips in turn ----------
def sexual():
    s = []
    chips = [('sun', 'Morning erections'), ('heart', 'Sexual desire'), ('pulse', 'Erections')]
    for k, (ic, lab) in enumerate(chips):
        y = 48 + k * 58
        s.append('<g class="sx-c" style="--k:%d"><rect x="24" y="%d" width="214" height="44" rx="12" fill="rgba(196,255,73,0.08)" stroke="#c4ff49" stroke-opacity="0.7" stroke-width="1.8"/>%s%s</g>'
                 % (k, y, ico(ic, 50, y + 22, 22, LIME, 1.8), txt(72, y + 27, lab, 14, '#fff', 0.92, 'start')))
        s.append('<path class="dr" pathLength="1" style="--d:%s;--dur:0.6s" d="M238 %d H272" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-dasharray="2 5" fill="none"/>' % (0.3 + k * 0.1, y + 22))
    s.append('<path d="M280 40V214H536" stroke="rgba(255,255,255,0.4)" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    d, pts = path(('M', 292, 64), ('C', 370, 70, 430, 150, 528, 196))
    s.append(dr(d, 0.4, 1.4, LIME, 3))
    s.append(dot('sx-p fx', 6, LIME, ring=True)); G.travel('sx-p', pts, 6, 78, 9, rest=pts[-1], rest_opacity=0, fade=4, ease='ease-in-out')
    s.append(txt(296, 34, 'Testosterone', 12, '#fff', 0.7, 'start'))
    s.append(txt(528, 234, 'Lower T, more of the three', 12, '#c4ff49', 0.95, 'end'))
    return '\n'.join(s)

# ---------- 3 · PHYSICAL: four tiles (battery drains, muscle bar shrinks, waist widens, bone dots fade) ----------
def physical():
    s = []
    xs = [22, 156, 290, 424]
    labels = ['Energy', 'Muscle', 'Belly fat', 'Bone density']
    for i, x in enumerate(xs):
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="26" width="114" height="168" rx="14" fill="rgba(255,255,255,0.04)" stroke="%s" stroke-width="1.8"/></g>' % (0.1 + i * 0.1, x, LIME if i == 0 else 'rgba(255,255,255,0.26)'))
        s.append(txt(x + 57, 222, labels[i], 13))
    # battery
    s.append('<rect x="44" y="92" width="62" height="34" rx="6" fill="none" stroke="#fff" stroke-opacity="0.75" stroke-width="2.4"/><rect x="106" y="102" width="6" height="14" rx="2" fill="#fff" fill-opacity="0.75"/>')
    s.append('<rect class="py-bat" x="49" y="97" width="52" height="24" rx="3" fill="#c4ff49" fill-opacity="0.85"/>')
    s.append(ico('sleep', 79, 58, 22, WHITE, 1.8))
    # muscle
    s.append(ico('train', 213, 58, 28, LIME, 1.9))
    s.append('<rect x="198" y="88" width="30" height="80" rx="6" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.3)" stroke-width="1.5"/>')
    s.append('<rect class="py-mu" x="202" y="92" width="22" height="72" rx="4" fill="#c4ff49" fill-opacity="0.8"/>')
    # belly
    s.append('<path d="M330 66c-8 0-12 6-12 14v80M364 66c8 0 12 6 12 14v80" stroke="rgba(255,255,255,0.45)" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    s.append('<ellipse class="py-bl" cx="347" cy="118" rx="24" ry="22" fill="rgba(196,255,73,0.2)" stroke="#c4ff49" stroke-width="2.2"/>')
    s.append('<circle cx="347" cy="52" r="10" fill="none" stroke="rgba(255,255,255,0.6)" stroke-width="2.2"/>')
    # bone dots
    s.append(ico('bone', 481, 58, 26, WHITE, 1.8))
    k = 0
    for r in range(3):
        for c in range(4):
            s.append('<circle class="py-bn" style="--k:%d" cx="%d" cy="%d" r="5" fill="%s"/>' % (k, 457 + c * 16, 98 + r * 22, LIME if (r + c) % 2 == 0 else '#fff'))
            k += 1
    return '\n'.join(s)

# ---------- 4 · MOOD: brain node, scrolling mood wave, focus dot drifting in a target ----------
def mood():
    period = 80
    wave = 'M120 125 ' + ' '.join('q %d %d %d 0 q %d %d %d 0' % (period / 4, -26 if i % 2 == 0 else -14, period / 2, period / 4, 26 if i % 2 == 0 else 14, period / 2) for i in range(6))
    s = ['<defs><clipPath id="md-clip"><rect x="130" y="70" width="240" height="110" rx="10"/></clipPath></defs>']
    s.append('<rect x="130" y="70" width="240" height="110" rx="10" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.18)" stroke-width="1.6"/>')
    s.append('<g clip-path="url(#md-clip)"><g class="md-wv"><path d="%s" stroke="#c4ff49" stroke-width="3" fill="none" stroke-linecap="round"/></g></g>' % wave)
    s.append(node(70, 125, 30, 'brain', 0.15, LIME, fill='#142e14', isz=32))
    s.append('<circle cx="462" cy="125" r="58" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="2"/><circle cx="462" cy="125" r="36" fill="none" stroke="rgba(255,255,255,0.32)" stroke-width="2"/><circle cx="462" cy="125" r="14" fill="none" stroke="#c4ff49" stroke-width="2.2"/>')
    s.append('<path d="M462 58v14M462 178v14M395 125h14M515 125h14" stroke="rgba(255,255,255,0.4)" stroke-width="2" stroke-linecap="round"/>')
    s.append('<g class="md-dt"><circle cx="462" cy="125" r="6" fill="#fff"/></g>')
    s.append(txt(70, 186, 'Mood', 13))
    s.append(txt(250, 206, 'Low mood, irritability, poor sleep', 13, '#fff', 0.75))
    s.append(txt(462, 214, 'Focus drifts', 13, '#c4ff49', 0.95))
    return '\n'.join(s)

# ---------- 5 · OVERLAP: centre circle with five look-alike causes drifting in and out ----------
def overlap():
    s = ['<circle cx="280" cy="128" r="64" fill="rgba(196,255,73,0.12)" stroke="#c4ff49" stroke-width="2.4"/>']
    s.append(txt(280, 124, 'Low T', 15, '#c4ff49', 1))
    s.append(txt(280, 142, 'symptoms', 13, '#fff', 0.85))
    sats = [(118, 70, 'sleep', 'Sleep apnea'), (118, 190, 'gland', 'Thyroid'), (442, 70, 'mood', 'Low mood'), (442, 190, 'scale', 'Weight'), (280, 236, 'pills', 'Medications')]
    for k, (x, y, ic, lab) in enumerate(sats):
        dx, dy = (280 - x) * 0.18, (128 - y) * 0.18
        s.append('<g class="ov-s" style="--k:%d;--dx:%spx;--dy:%spx"><circle cx="%d" cy="%d" r="%d" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.45)" stroke-width="1.8" stroke-dasharray="4 4"/>%s%s</g>'
                 % (k, f(dx), f(dy), x, y, 30 if k == 4 else 42, ico(ic, x, y - (0 if k == 4 else 8), 22, WHITE if k % 2 else LIME, 1.8), '' if k == 4 else txt(x, y + 22, lab, 12, '#fff', 0.85)))
    s.append(txt(318, 241, 'Medications', 12, '#fff', 0.85, 'start'))
    return '\n'.join(s)

# ---------- 6 · DIAGNOSIS: symptoms + morning test + morning test = confirmed pattern ----------
def diagnosis():
    s = []
    d, pts = path(('M', 70, 120), ('L', 510, 120))
    s.append('<path d="M70 120H510" stroke="rgba(255,255,255,0.14)" stroke-width="2.4" stroke-dasharray="2 8" stroke-linecap="round"/>')
    s.append(dr(d, 0.3, 1.6, 'rgba(196,255,73,0.55)', 2.4))
    s.append(dot('dg-p fx', 6, LIME, ring=True)); G.travel('dg-p', pts, 6, 82, 9, rest=pts[-1], rest_opacity=0, fade=3, ease='ease-in-out')
    items = [(70, 'list', 'Symptoms', WHITE), (220, 'tube', 'Morning test', LIME), (370, 'tube', 'Repeat test', LIME), (510, 'check', 'Confirmed', LIME)]
    for i, (x, ic, lab, col) in enumerate(items):
        s.append(node(x, 120, 28, ic, 0.15 + i * 0.15, col, fill='#142e14' if col == LIME else DARK, isz=30))
        s.append(txt(x, 178, lab, 13, '#c4ff49' if i == 3 else '#fff', 0.9))
    for k, x in enumerate((220, 370)):
        s.append('<g class="dg-sun" style="--k:%d">%s</g>' % (k, ico('sun', x, 58, 24, LIME, 1.8)))
    for x, sym in ((145, '+'), (295, '+'), (442, '=')):
        s.append(txt(x, 128, sym, 22, '#fff', 0.7))
    s.append('<circle class="dg-ring fx" cx="510" cy="120" r="34" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(txt(295, 210, 'Fasting, early morning, on separate days', 12, '#fff', 0.65))
    return '\n'.join(s)

# ---------- 7 · CHECKER figure: clipboard rows tick in sequence ----------
def checker_fig():
    s = ['<g class="pop t" style="--d:0.1"><rect x="110" y="18" width="150" height="176" rx="14" fill="#142e14" stroke="rgba(255,255,255,0.5)" stroke-width="2.4"/><rect x="150" y="8" width="70" height="22" rx="6" fill="#173617" stroke="#c4ff49" stroke-width="2"/></g>']
    for k in range(4):
        y = 52 + k * 34
        s.append('<rect x="128" y="%d" width="20" height="20" rx="5" fill="none" stroke="rgba(255,255,255,0.6)" stroke-width="2"/>' % y)
        s.append('<path d="M160 %dh%d" stroke="rgba(255,255,255,0.4)" stroke-width="3" stroke-linecap="round"/>' % (y + 10, 80 - (k % 2) * 22))
        s.append('<g class="ck-t" style="--k:%d"><path d="M132 %d l5 5 10 -11" stroke="#c4ff49" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>' % (k, y + 10))
    s.append(node(60, 100, 22, 'heart', 0.4, LIME, fill='#142e14', isz=22))
    s.append(node(310, 70, 20, 'batt', 0.5, WHITE, isz=22))
    s.append(node(310, 140, 20, 'brain', 0.6, WHITE, isz=22))
    return '\n'.join(s)

# ---------- 8 · HELP: telehealth screen; labs flow in, plan flows out, coaching icons light in turn ----------
def help_fig():
    s = ['<g class="pop t" style="--d:0.1"><rect x="190" y="30" width="180" height="120" rx="14" fill="#142e14" stroke="#c4ff49" stroke-width="2.2"/><path d="M262 150v14M240 166h80" stroke="rgba(255,255,255,0.5)" stroke-width="2.4" stroke-linecap="round"/></g>']
    s.append(node(250, 90, 24, 'you', 0.25, WHITE, isz=26))
    s.append(node(318, 90, 24, 'coach', 0.35, LIME, fill='#173617', isz=26))
    for k, (x, y) in enumerate(((228, 54), (340, 54))):
        s.append('<g class="hp-b" style="--k:%d"><rect x="%d" y="%d" width="34" height="18" rx="8" fill="%s"/><path d="M%d %dh18" stroke="#0f240f" stroke-width="2" stroke-linecap="round"/></g>' % (k, x - 17, y - 9, LIME if k else '#fff', x - 9, y))
    for i, (a, b, cls, col) in enumerate([((80, 90), (190, 90), 'hp-in', WHITE), ((370, 90), (480, 90), 'hp-out', LIME)]):
        d, pts = path(('M', a[0], a[1]), ('L', b[0], b[1]))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % d)
        s.append(dot('%s fx' % cls, 5, col)); G.travel(cls, pts, 8, 48, 6, delay='%ss' % f(-i * 3), rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(60, 90, 24, 'labs', 0.45, WHITE, isz=26)); s.append(txt(60, 138, 'Labs', 13))
    s.append(node(500, 90, 24, 'doc', 0.55, LIME, fill='#142e14', isz=26)); s.append(txt(500, 138, 'Your plan', 13, '#c4ff49', 0.95))
    for k, (ic, lab) in enumerate((('sleep', 'Sleep'), ('train', 'Training'), ('food', 'Nutrition'), ('stress', 'Stress'))):
        x = 130 + k * 100
        s.append('<g class="hp-i" style="--k:%d"><circle cx="%d" cy="206" r="20" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/>%s</g>' % (k, x, ico(ic, x, 206, 20, LIME, 1.8)))
        s.append(txt(x, 244, lab, 12, '#fff', 0.8))
    return '\n'.join(s)

# ---------- final: an energy line climbs, a dot rides it, a battery fills ----------
def final():
    pts_line = [(24, 160), (80, 150), (120, 128), (170, 136), (220, 98), (262, 108), (300, 64)]
    segs = [('M',) + pts_line[0]] + [('L',) + p for p in pts_line[1:]]
    d, p = path(*segs)
    s = ['<path d="M24 176H336" stroke="rgba(255,255,255,0.45)" stroke-width="3" stroke-linecap="round"/>']
    s.append(dr(d, 0.2, 1.6, LIME, 3.4))
    dense = []
    for i in range(len(pts_line) - 1):
        a, b = pts_line[i], pts_line[i + 1]
        for k in range(4):
            dense.append((a[0] + (b[0] - a[0]) * k / 4, a[1] + (b[1] - a[1]) * k / 4))
    dense.append(pts_line[-1])
    s.append(dot('fn-p', 7, LIME, ring=True)); G.travel('fn-p', dense, 8, 78, 8, rest=dense[-1], fade=3)
    s.append('<rect x="290" y="20" width="50" height="26" rx="6" fill="none" stroke="#fff" stroke-width="2.4"/><rect x="340" y="28" width="5" height="10" rx="2" fill="#fff"/>')
    s.append('<rect class="fn-bt" x="294" y="24" width="42" height="18" rx="3" fill="#c4ff49"/>')
    for i, (x, y, ic) in enumerate(((80, 150, 'sleep'), (170, 136, 'train'), (262, 108, 'food'))):
        s.append(node(x, y + 2, 16, ic, 0.4 + i * 0.12, WHITE if i % 2 else LIME, fill=DARK, isz=16))
    return '\n'.join(s)

FAQMOTIF = '''<rect x="12" y="34" width="44" height="26" rx="6" stroke="#fff" stroke-width="3"/><rect x="56" y="42" width="5" height="10" rx="2" fill="#fff"/>
<g class="fq-bt"><rect x="16" y="38" width="36" height="18" rx="3" fill="#c4ff49"/></g>
<path class="dr" pathLength="1" style="--d:0.2;--dur:1.1s" d="M74 38c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="86" cy="66" r="3" fill="#fff"/>
<path class="fq-st" style="--k:0" d="M106 18v10M101 23h10" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/>'''

def step_icons():
    return {
     "{{STEP1}}": '<path d="M14 8h22a2 2 0 0 1 2 2v30a2 2 0 0 1-2 2H14a2 2 0 0 1-2-2V10a2 2 0 0 1 2-2z"/><path d="M20 18h12M20 26h12M20 34h8"/><g class="hi-bl" style="--k:0"><circle cx="16" cy="18" r="1.8" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="16" cy="26" r="1.8" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="16" cy="34" r="1.8" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M19 6h10"/><path d="M21 6v26a3 3 0 0 0 6 0V6"/><path d="M21 20h6"/><g class="hi-gr" style="--k:0"><path d="M33 40V30M38 40V24M43 40V34" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<g class="hi-sl" style="--k:0"><path d="M10 20v10M6 22v6M38 20v10M42 22v6M10 25h28" stroke="#c4ff49"/></g><path d="M18 40c4-6 8-6 12 0"/><path d="M24 8a5 5 0 1 0 5 5"/>',
     "{{STEP4}}": '<path d="M6 36h8l5-12 7 16 5-10h11"/><g class="hi-ck" style="--k:0"><path d="M30 10l5 5 9-11" stroke="#c4ff49"/></g>',
    }

def hub_nodes():
    icons = ['scale', 'tube', 'link', 'calendar', 'flame', 'drop', 'coach', 'caps', 'body', 'split']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)  # half-step offset: 10 nodes, none stacked at the ends
        out.append((round(280 + 240 * math.cos(a)), round(100 + 70 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{SEXUAL}}": sexual(), "{{PHYSICAL}}": physical(), "{{MOOD}}": mood(), "{{OVERLAP}}": overlap(),
         "{{DIAG}}": diagnosis(), "{{CHECKFIG}}": checker_fig(), "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB,
         "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Low testosterone symptoms in men (late-onset hypogonadism, andropause)",
      "Low testosterone symptoms", "What are the symptoms of low testosterone in men?", slots, G, published="2026-10-16")
