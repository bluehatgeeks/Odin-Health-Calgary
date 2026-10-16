"""Build /workspace/pages/low-testosterone-age-or-weight/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *

SLUG = "low-testosterone-age-or-weight"
TITLE = "Low T: Aging or Weight, Sleep and Stress? | Odin Health Labs"
DESC = "Is low testosterone from aging or from weight, sleep and stress? What studies show, which labs tell them apart, and what you can change. Canada and USA."
OG_ALT = "Odin Health Labs: is low testosterone from aging, or from weight, sleep and stress? Guidance for men in Canada and the USA"
assert len(TITLE) <= 60 and len(DESC) <= 160, (len(TITLE), len(DESC))

FAQ = [
 ("Does testosterone naturally drop with age?",
  "On average, yes, but slowly. In the Massachusetts Male Aging Study, total testosterone fell about 1.6 percent a year in men followed for 7 to 10 years from ages 40 to 70, and bioavailable testosterone fell 2 to 3 percent a year. The Baltimore Longitudinal Study of Aging measured an average drop of 0.124 nmol/L a year in 890 healthy men. Declines differ a lot from man to man, and in the Massachusetts study the authors suggested that new health problems may speed the fall. We look at your numbers and your habits together, so you know how much of your picture is the slow slope of age and how much is something you can change."),
 ("Can losing weight raise my testosterone?",
  "Often, yes. A 2013 meta-analysis of 24 studies found that total testosterone rose by about 2.9 nmol/L on average after low-calorie diets and about 8.7 nmol/L after bariatric surgery, with larger rises in men who lost more weight. In the European Male Ageing Study, weight loss tracked with a rise in testosterone and weight gain with a fall. The AUA guideline advises counselling every man with low testosterone on weight loss and physical activity. We build a nutrition and training plan around your life and re-check your labs to see the change."),
 ("How much can poor sleep lower testosterone?",
  "In a University of Chicago study of 10 healthy men with an average age of 24, about a week of five-hour bedtimes lowered daytime testosterone from an average of 18.4 to 16.5 nmol/L, with the biggest gap between 2 and 10 PM. The Canadian Urological Association guideline sums up persistent sleep restriction as lowering testosterone by roughly 10 to 15 percent and notes that a structured sleep program may offset it. It is a small study in young men, and it shows the direction of the effect, not your exact number. We set up a sleep plan that fits your schedule, including night and rotating shifts."),
 ("Can stress lower testosterone?",
  "Sustained stress can. A 2026 review in the Journal of Clinical Endocrinology &amp; Metabolism pulled together military, endurance-athlete and competition studies and concluded that testosterone suppression under sustained stress is commonly a reversible, brain-driven adaptation rather than testicular failure. Severe energy deficit, disrupted sleep and uncontrollable psychological stress turn down the brain&rsquo;s LH signal and often raise SHBG, which lowers free testosterone. The same review found that heavy resistance training did not suppress baseline testosterone when energy intake was sufficient. We build stress, recovery and fueling habits you can keep."),
 ("Which labs show whether it is age or lifestyle?",
  'The AUA guideline defines low testosterone as total testosterone under 300 ng/dL on two early-morning measurements together with symptoms, and recommends measuring LH in every man with a low result. In the European Male Ageing Study, low testosterone with low or normal LH was far more common (11.8 percent of men) than low testosterone with high LH (2.0 percent), and obesity was strongly linked to the low-or-normal-LH pattern. SHBG and free testosterone add context, because obesity lowers SHBG and total testosterone together. We walk you through each result. See our <a href="%s/low-testosterone-labs-to-ask-for">lab guide</a>.' % SITE),
 ("How does Odin Health Labs work with my doctor?",
  'Odin Health Labs is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We review your labs with you, work out which levers matter most, build your plan and track your progress. We can share your plan and results with your own doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

# ---------- 1 · HERO: four drivers feed one gauge; the needle sways ----------
def hero_conv():
    s = ['<defs><radialGradient id="ag-g" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.16"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="228" ry="148" fill="url(#ag-g)"/>']
    nodes = [(66, 60, 'calendar', LIME), (414, 60, 'scale', WHITE), (66, 260, 'sleep', WHITE), (414, 260, 'stress', LIME)]
    for i, (x, y, ic, col) in enumerate(nodes):
        d, pts = path(('M', x, y), ('L', 240, 168))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>' % d)
        s.append(dr(d, 0.5 + i * 0.12, 1.0, 'rgba(196,255,73,0.45)', 2.4))
    s.append('<g class="pop t" style="--d:0.3"><path d="M160 196A80 80 0 0 1 320 196" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="12" stroke-linecap="round"/></g>')
    s.append(dr('M160 196A80 80 0 0 1 320 196', 0.5, 1.2, LIME, 5))
    s.append('<path d="M160 196h14M306 196h14M240 116v12" stroke="rgba(255,255,255,0.4)" stroke-width="2.4" stroke-linecap="round"/>')
    s.append('<path class="hv-nd" d="M240 196V132" stroke="#fff" stroke-width="4.4" stroke-linecap="round" fill="none"/>')
    s.append('<circle cx="240" cy="196" r="9" fill="#142e14" stroke="#c4ff49" stroke-width="3"/>')
    for i, (x, y, ic, col) in enumerate(nodes):
        d, pts = path(('M', x, y), ('L', 232, 176))
        s.append(dot('hv-p%d fx' % i, 5.5, LIME if i % 2 == 0 else WHITE))
        G.travel('hv-p%d' % i, pts, 8, 80, 8, delay='%ss' % f(-i * 2), rest=pts[0], rest_opacity=0, fade=3)
    for i, (x, y, ic, col) in enumerate(nodes):
        s.append(node(x, y, 30, ic, 0.1 + i * 0.12, col, fill='#142e14' if col == LIME else DARK, isz=32))
    return '\n'.join(s)

# ---------- 2 · AGE: a gentle slope, a man-to-man band, a dot riding it ----------
def age():
    dA, pA = path(('M', 70, 70), ('C', 190, 78, 330, 98, 500, 126), n=24)
    band = 'M70 52C190 56 330 70 500 92L500 168C330 134 190 104 70 92Z'
    s = ['<path d="M50 200H540M50 30V200" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round" fill="none"/>']
    s.append('<g class="pop t" style="--d:0.2"><path class="ag-band" d="%s" fill="rgba(196,255,73,0.1)" stroke="rgba(196,255,73,0.28)" stroke-width="1.6" stroke-linejoin="round"/></g>' % band)
    for x, lab in ((70, '40s'), (195, '50s'), (320, '60s'), (445, '70s')):
        s.append('<path d="M%d 200v8" stroke="rgba(255,255,255,0.45)" stroke-width="2.4" stroke-linecap="round"/><text x="%d" y="228" font-size="13" fill="#fff" fill-opacity="0.75" text-anchor="middle">%s</text>' % (x, x, lab))
    s.append(dr(dA, 0.4, 1.8, LIME, 4.6))
    s.append(dot('ag-p', 7, LIME, ring=True)); G.travel('ag-p', pA, 6, 94, 11, rest=pA[len(pA) // 2], fade=2.5)
    s.append(node(70, 70, 17, 'calendar', 0.1, LIME, isz=18))
    return '\n'.join(s)

# ---------- 3 · WEIGHT: three descending steps, a ball rolls down, the drops shrink ----------
def weight():
    s = ['<path d="M30 214H530" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round"/>']
    steps = [(52, 192, 118, 1.0, 'BMI under 25'), (206, 192, 152, 0.74, 'BMI 25 to 30'), (360, 192, 186, 0.5, 'BMI 30 and over')]
    for k, (x, w, top, sc, lab) in enumerate(steps):
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="%d" width="148" height="%d" rx="12" fill="%s" stroke="%s" stroke-width="2.4"/></g>' % (0.1 + k * 0.16, x, top, 214 - top, '#142e14' if k % 2 == 0 else '#173617', 'rgba(196,255,73,0.65)' if k == 0 else 'rgba(255,255,255,0.5)'))
        s.append('<g class="pop t" style="--d:%s"><g class="wt-dr" style="--k:%d;--sc:%s">%s</g></g>' % (0.3 + k * 0.16, k, sc, ico('drop', x + 74, top - 52, 36, LIME if k == 0 else WHITE, 1.9)))
        s.append('<text x="%d" y="240" font-size="13" fill="#fff" fill-opacity="0.8" text-anchor="middle">%s</text>' % (x + 74, lab))
    s.append(dr('M60 214H500', 0.2, 1.2, 'rgba(196,255,73,0.25)', 2.4))
    pts = [(82, 84), (160, 84), (176, 90), (230, 106), (330, 106), (346, 112), (384, 148), (500, 148)]
    # ball rolls on the step tops: 118-top, 152-top, 186-top, with a drop between steps
    pts = [(70, 102), (190, 102), (200, 110), (214, 136), (330, 136), (350, 144), (366, 170), (490, 170)]
    s.append(dot('wt-p', 8, LIME, ring=True)); G.travel('wt-p', pts, 6, 94, 10, rest=pts[0], fade=2.5)
    return '\n'.join(s)

# ---------- 4 · LOSS: two bars drawn to scale (+2.87 and +8.73 nmol/L), they rise, hold, reset ----------
def loss():
    s = ['<path d="M60 196H520M60 30V196" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round" fill="none"/>']
    unit = 11.0
    for k, (x, val, lab, ic) in enumerate(((150, 2.87, 'Low-calorie diet', 'food'), (324, 8.73, 'Bariatric surgery', 'scale'))):
        h = val * unit
        top = 196 - h
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="30" width="86" height="166" rx="14" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.28)" stroke-width="2"/>'
                 '<rect class="ls-bar" style="--s:1;--k:%d" x="%d" y="%s" width="86" height="%s" rx="14" fill="%s" fill-opacity="%s"/></g>' % (0.1 + k * 0.15, x, k, x, f(top), f(h), LIME if k else 'rgba(255,255,255,0.8)', '0.85' if k else '0.5'))
        s.append('<text x="%d" y="%s" font-size="17" fill="#fff" text-anchor="middle">+%s</text>' % (x + 43, f(top - 12), ('%.2f' % val)))
        s.append('<text x="%d" y="220" font-size="13" fill="#fff" fill-opacity="0.8" text-anchor="middle">%s</text>' % (x + 43, lab))
        s.append('<g class="ls-up" style="--k:%d"><path d="M%d %s v-14M%d %s l-6 8M%d %s l6 8" stroke="#fff" stroke-width="3" stroke-linecap="round" fill="none"/></g>' % (k, x + 43, f(top - 34), x + 43, f(top - 48), x + 43, f(top - 48)))
    s.append('<text x="280" y="244" font-size="12" fill="#fff" fill-opacity="0.65" text-anchor="middle">Average rise in total testosterone, nmol/L</text>')
    return '\n'.join(s)

# ---------- 5 · SLEEP: two daytime curves, the gap opens in the afternoon and evening; a moon with stars ----------
def sleep():
    top = path(('M', 70, 90), ('C', 180, 80, 280, 96, 360, 112), ('C', 420, 124, 470, 136, 510, 146), n=22)
    low = path(('M', 70, 100), ('C', 180, 102, 280, 128, 360, 154), ('C', 420, 172, 470, 186, 510, 194), n=22)
    s = ['<path d="M50 214H540M50 30V214" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round" fill="none"/>']
    s.append('<rect class="sl-win fx" x="300" y="46" width="210" height="168" rx="12" fill="rgba(196,255,73,0.08)" stroke="rgba(196,255,73,0.3)" stroke-width="1.6" stroke-dasharray="4 6"/>')
    for x, lab in ((70, '8 AM'), (300, '2 PM'), (510, '10 PM')):
        s.append('<path d="M%d 214v8" stroke="rgba(255,255,255,0.45)" stroke-width="2.4" stroke-linecap="round"/><text x="%d" y="240" font-size="13" fill="#fff" fill-opacity="0.75" text-anchor="middle">%s</text>' % (x, x, lab))
    s.append(dr(low[0], 0.5, 1.6, 'rgba(255,255,255,0.8)', 3.4))
    s.append(dr(top[0], 0.3, 1.6, LIME, 4.4))
    s.append(dot('sl-p0', 7, LIME, ring=True)); G.travel('sl-p0', top[1], 6, 88, 9, rest=top[1][-1], fade=2.5)
    s.append(dot('sl-p1', 6, WHITE)); G.travel('sl-p1', low[1], 6, 88, 9, delay='-1.2s', rest=low[1][-1], fade=2.5)
    s.append('<g class="sl-st" style="--k:0"><path d="M440 56v10M435 61h10" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/></g><g class="sl-st" style="--k:1"><path d="M498 44v8M494 48h8" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/></g>')
    s.append(node(86, 46, 18, 'sleep', 0.1, LIME, isz=20))
    return '\n'.join(s)

# ---------- 6 · STRESS: load waveform shakes on top; the brain-to-testes signal below dims and recovers ----------
def stress():
    zz = 'M110 60' + ''.join('l%d %d' % (14, -22 if i % 2 == 0 else 22) for i in range(22))
    s = ['<g class="pop t" style="--d:0.1"><path d="M40 60H100" stroke="rgba(255,255,255,0.25)" stroke-width="2.4" stroke-linecap="round"/></g>']
    s.append('<g class="st-zz">' + dr(zz, 0.3, 1.6, 'rgba(255,255,255,0.8)', 3.2) + '</g>')
    s.append(node(60, 60, 22, 'stress', 0.1, LIME, isz=24))
    d, pts = path(('M', 102, 174), ('L', 458, 174))
    s.append('<g class="st-sig"><path d="%s" stroke="rgba(196,255,73,0.35)" stroke-width="3" stroke-dasharray="3 8" stroke-linecap="round" fill="none"/></g>' % d)
    s.append(dr(d, 0.6, 1.2, 'rgba(196,255,73,0.6)', 3))
    for k in range(3):
        s.append(dot('st-d%d%s' % (k, ' fx' if k else ''), 6, LIME))
        G.travel('st-d%d' % k, pts, 8, 92, 6, delay='%ss' % f(-k * 2), rest=pts[0] if k else pts[len(pts)//2], fade=3, rest_opacity=1 if k == 0 else 0)
    s.append(node(60, 174, 30, 'brain', 0.2, LIME, fill='#142e14', isz=34))
    s.append(node(500, 174, 30, 'gland', 0.5, WHITE, isz=32))
    s.append('<text x="280" y="214" font-size="13" fill="#fff" fill-opacity="0.75" text-anchor="middle">LH signal from the brain to the testes</text>')
    return '\n'.join(s)

# ---------- 7 · PATTERN: a result forks by LH; dots take each branch in turn ----------
def pattern():
    up = path(('M', 112, 130), ('C', 190, 130, 220, 62, 330, 62), ('L', 410, 62), n=20)
    dn = path(('M', 112, 130), ('C', 190, 130, 220, 198, 330, 198), ('L', 410, 198), n=20)
    s = ['<circle class="fk-ring fx" cx="112" cy="130" r="30" fill="none" stroke="#c4ff49" stroke-width="2"/>']
    for d in (up[0], dn[0]):
        s.append('<path d="%s" stroke="rgba(255,255,255,0.14)" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>' % d)
    s.append(dr(up[0], 0.5, 1.3, 'rgba(255,255,255,0.7)', 3.2)); s.append(dr(dn[0], 0.6, 1.3, LIME, 3.6))
    s.append(dot('fk-a', 6.5, WHITE, ring=True)); G.travel('fk-a', up[1], 6, 46, 10, rest=up[1][-1], fade=2.5, rest_opacity=1)
    s.append(dot('fk-b', 6.5, LIME, ring=True)); G.travel('fk-b', dn[1], 56, 96, 10, rest=dn[1][-1], fade=2.5, rest_opacity=1)
    s.append(node(76, 130, 30, 'tube', 0.1, LIME, fill='#142e14', isz=32))
    s.append(node(444, 62, 30, 'gland', 0.6, WHITE, isz=32))
    s.append(node(444, 198, 30, 'brain', 0.75, LIME, fill='#142e14', isz=34))
    s.append('<text x="444" y="108" font-size="13" fill="#fff" fill-opacity="0.85" text-anchor="middle">LH high</text>')
    s.append('<text x="444" y="244" font-size="13" fill="#c4ff49" fill-opacity="0.95" text-anchor="middle">LH low or normal</text>')
    s.append('<text x="76" y="176" font-size="13" fill="#fff" fill-opacity="0.85" text-anchor="middle">Low T result</text>')
    return '\n'.join(s)

# ---------- final: a sunrise over the horizon, rays turn, nodes on either side ----------
SUNRISE = '''<defs><clipPath id="sr-c"><rect x="0" y="0" width="360" height="150"/></clipPath></defs>
<g clip-path="url(#sr-c)"><g class="sr-sun"><g class="sr-rays"><path d="M238.0 150.0L256.0 150.0M230.2 121.0L245.8 112.0M209.0 99.8L218.0 84.2M180.0 92.0L180.0 74.0M151.0 99.8L142.0 84.2M129.8 121.0L114.2 112.0M122.0 150.0L104.0 150.0M129.8 179.0L114.2 188.0M151.0 200.2L142.0 215.8M180.0 208.0L180.0 226.0M209.0 200.2L218.0 215.8M230.2 179.0L245.8 188.0" stroke="#c4ff49" stroke-opacity="0.75" stroke-width="3.4" stroke-linecap="round"/></g>
<circle cx="180" cy="150" r="46" fill="#c4ff49" fill-opacity="0.88"/></g></g>
<path d="M30 150H330" stroke="rgba(255,255,255,0.55)" stroke-width="3.4" stroke-linecap="round"/>
<path class="dr" pathLength="1" style="--d:0.3;--dur:1.2s" d="M70 168H290" fill="none" stroke="rgba(196,255,73,0.3)" stroke-width="2.4" stroke-linecap="round"/>
<path class="sr-sp" style="--k:0" d="M96 40v12M90 46h12" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path class="sr-sp" style="--k:1" d="M270 34v10M265 39h10" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/>'''
SUNRISE += node(50, 112, 24, 'sleep', 0.4, WHITE, isz=26) + node(310, 112, 24, 'train', 0.55, LIME, isz=26)

FAQMOTIF = '''<g class="fq-mn"><path d="M44 24a28 28 0 1 0 24 44a22 22 0 0 1-24-44z" fill="#c4ff49" fill-opacity="0.85"/></g>
<path class="fq-st" style="--k:0" d="M20 22v10M15 27h10" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/><path class="fq-st" style="--k:1" d="M62 14v8M58 18h8" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/>
<path class="dr" pathLength="1" style="--d:0.2;--dur:1.1s" d="M86 38c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="98" cy="66" r="3" fill="#fff"/>'''

def step_icons():
    return {
     "{{STEP1}}": '<path d="M18 6v22a6 6 0 0 0 12 0V6"/><path d="M14 6h20"/><g class="hi-gr" style="--k:0"><rect x="20.5" y="22" width="7" height="12" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:0"><circle cx="38" cy="30" r="2.8" fill="#fff" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="10" cy="22" r="2.8" fill="#fff" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M34 30A15 15 0 1 1 18 8a12 12 0 0 0 16 22z"/><g class="hi-bl" style="--k:0"><path d="M36 10v8M32 14h8" stroke="#c4ff49"/></g><g class="hi-bl" style="--k:1"><circle cx="8" cy="40" r="2.4" fill="#fff" stroke="none"/></g>',
     "{{STEP3}}": '<path d="M12 42V10"/><g class="hi-sw" style="--k:0"><path d="M12 10h22l6 6-6 6H12z" fill="rgba(196,255,73,0.22)"/></g><path d="M8 42h12"/>',
     "{{STEP4}}": '<path d="M5 28h9l4-10 8 20 4-10h13"/><g class="hi-ck" style="--k:0"><path d="M30 12l5 5 9-11" stroke="#fff"/></g>',
    }

<<<<<<< HEAD
HUB = hub(G, [(110, 52, 'tube'), (110, 148, 'scale'), (450, 52, 'coach'), (450, 148, 'labs'), (230, 28, 'caps'), (330, 172, 'drop'), (330, 28, 'flame')])
=======
HUB = hub(G, [(110, 52, 'tube'), (110, 148, 'scale'), (450, 52, 'coach'), (450, 148, 'labs'), (230, 28, 'caps'), (330, 172, 'drop')])
>>>>>>> origin/master
slots = {"{{HERO}}": hero_conv(), "{{AGE}}": age(), "{{WEIGHT}}": weight(), "{{LOSS}}": loss(), "{{SLEEP}}": sleep(), "{{STRESS}}": stress(),
         "{{PATTERN}}": pattern(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB, "{{FAQMOTIF}}": FAQMOTIF, "{{SUNRISE}}": SUNRISE}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Low testosterone in men: age-related decline versus weight, sleep and stress",
      "Low T: age or weight", "Is my low testosterone from aging or from weight, sleep and stress?", slots, G)
