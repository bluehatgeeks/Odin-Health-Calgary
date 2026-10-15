"""Build /workspace/pages/trt-or-fix-causes-first/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *

SLUG = "trt-or-fix-causes-first"
TITLE = "TRT or Fix the Causes of Low T First? | Odin Health Labs"
DESC = "Should you start TRT or fix the causes of low testosterone first? The trade-offs, TRAVERSE findings, reversible causes and how to decide with a physician."
OG_ALT = "Odin Health Labs: should you start TRT or fix the causes of low testosterone first? A step-by-step guide for men in Canada and the USA"
assert len(TITLE) <= 60 and len(DESC) <= 160, (len(TITLE), len(DESC))

FAQ = [
  ("Can I start TRT without fixing the causes first?",
  "That is a decision to make with the full picture in front of you. The Endocrine Society\u2019s 2018 guideline recommends confirming low testosterone with repeated morning tests and then looking for the cause. Some causes change what is safe or sensible, such as untreated severe sleep apnea or plans to have children. Some men work on causes and discuss TRT at the same time, and we help you work out which order suits you."),
  ("Will TRT affect my fertility?",
  "It can. TRT lowers the brain\u2019s LH and FSH signals to the testes, which can reduce sperm production while you take it. Recovery after stopping varies and isn\u2019t certain. If you may want children in the near term, say so before anything starts, because the Endocrine Society guideline advises against starting testosterone therapy in that situation."),
  ("Is TRT safe for my heart?",
  "In the TRAVERSE trial (NEJM, 2023), testosterone gel was non-inferior to placebo for major cardiovascular events in men with hypogonadism who had existing or a high risk of cardiovascular disease. A higher incidence of atrial fibrillation, pulmonary embolism and acute kidney injury was seen in the testosterone group, and testosterone products can raise blood pressure. Whether it suits you depends on your own history, and we go through it with you."),
  ("Can lifestyle changes raise testosterone enough to avoid TRT?",
  "Sometimes they help. It depends on what is behind the low result: sleep, weight, alcohol, a medication or sleep apnea can all play a part, while some causes aren\u2019t lifestyle-related at all. We help you work on the causes that can be changed and recheck your levels afterwards, so you can see where you stand."),
  ("How long should I work on the causes before considering TRT?",
  "There isn\u2019t one right answer. It depends on your symptoms, how low your results are and what the cause turns out to be. We help you set a review date and a recheck, so the decision doesn\u2019t drift."),
  ("How does Odin Health Labs work with my doctor?",
  'Odin Health Labs is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. A free call helps you work out where to start and what to ask. We review your labs with you, build your plan and track your progress, and we can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

# ---------- 1 · HERO: a path from labs splits into causes / TRT, two dots travel, routes meet at the physician ----------
def hero_fork():
    dA, pA = path(('M', 44, 160), ('L', 170, 160), ('C', 230, 160, 240, 70, 300, 70), ('C', 380, 70, 380, 160, 430, 160))
    dB, pB = path(('M', 44, 160), ('L', 170, 160), ('C', 230, 160, 240, 250, 300, 250), ('C', 380, 250, 380, 160, 430, 160))
    s = ['<defs><radialGradient id="hf-g" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.16"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="230" ry="140" fill="url(#hf-g)"/>']
    s.append('<path d="%s" fill="none" stroke="rgba(255,255,255,0.18)" stroke-width="4" stroke-linecap="round"/>' % dB)
    s.append('<path d="%s" fill="none" stroke="rgba(196,255,73,0.2)" stroke-width="4" stroke-linecap="round"/>' % dA)
    s.append(dr(dA, 0.2, 2.0, LIME, 4))
    s.append(dr(dB, 0.6, 2.0, 'rgba(255,255,255,0.7)', 3, ' stroke-dasharray="1 2"'.replace(' stroke-dasharray="1 2"', '')))
    s.append(dot('hf-a', 7, LIME, True)); s.append(dot('hf-b', 6, WHITE))
    G.travel('hf-a', pA, 6, 70, 9, rest=pA[16]); G.travel('hf-b', pB, 6, 70, 9, rest=pB[16])
    s.append('<circle class="hf-arr fx" cx="430" cy="160" r="26" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(node(44, 160, 24, 'labs', 0.1, LIME, fill='#142e14'))
    s.append(node(300, 70, 24, 'leaf', 0.9, LIME))
    s.append(node(300, 250, 24, 'pills', 1.1, WHITE, dashed=True))
    s.append(node(430, 160, 26, 'heart', 1.4, LIME, fill='#142e14'))
    return '\n'.join(s)

# ---------- 2 · LOOP: brain -> testes signal; testosterone returns; TRT adds from outside and the signal fades ----------
def loop():
    dT, pT = path(('M', 150, 78), ('C', 220, 10, 340, 10, 410, 78))
    dB, pB = path(('M', 410, 106), ('C', 340, 176, 220, 176, 150, 106))
    dX, pX = path(('M', 280, 190), ('L', 280, 156), ('C', 230, 156, 190, 134, 152, 108))
    s = ['<path d="%s" fill="none" stroke="rgba(196,255,73,0.2)" stroke-width="3.5" stroke-linecap="round"/>' % dT, dr(dT, 0.4, 1.4, LIME, 3.5)]
    s.append('<path d="%s" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/>' % dB)
    s.append('<path d="M280 190V160" stroke="rgba(255,255,255,0.25)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/>')
    s.append('<g class="lp-sigw">' + ''.join(dot('lp-s%d' % i, 6, LIME) for i in range(3)) + '</g>')
    s.append('<g class="lp-tw">' + ''.join(dot('lp-t%d' % i, 5, WHITE) for i in range(3)) + '</g>')
    s.append('<g class="lp-xw">' + ''.join(dot('lp-x%d' % i, 6, LIME, True) for i in range(2)) + '</g>')
    for i in range(3):
        G.travel('lp-s%d' % i, pT, 4, 96, 3.6, delay='%ss' % f(-i * 1.2), rest=pT[5 + i * 3])
        G.travel('lp-t%d' % i, pB, 4, 96, 4.5, delay='%ss' % f(-i * 1.5), rest=pB[5 + i * 3])
    for i in range(2):
        G.travel('lp-x%d' % i, pX, 4, 96, 3.4, delay='%ss' % f(-i * 1.7), rest=pX[3 + i * 6])
    s.append(node(110, 92, 36, 'brain', 0.1, LIME, fill='#142e14', isz=38))
    s.append(node(450, 92, 36, 'gland', 0.25, WHITE, fill='#142e14', isz=36))
    s.append(node(280, 218, 26, 'pills', 0.5, LIME, isz=28))
    return '\n'.join(s)

# ---------- 3 · ORBIT: four check points around you, a pulse circles and lights each ----------
def orbit():
    s = ['<circle cx="280" cy="120" r="92" fill="none" stroke="rgba(196,255,73,0.18)" stroke-width="3"/>']
    s.append('<circle class="dr" pathLength="1" style="--d:0.2;--dur:1.8s" cx="280" cy="120" r="92" fill="none" stroke="#c4ff49" stroke-width="3" stroke-linecap="round" transform="rotate(-90 280 120)"/>')
    pts = [(280, 28, 'drop', LIME), (372, 120, 'labs', WHITE), (280, 212, 'heart', LIME), (188, 120, 'tube', WHITE)]
    s.append('<g class="mo-spin"><circle cx="280" cy="28" r="7" fill="#fff"/><circle cx="280" cy="28" r="12" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="2"/></g>')
    for k, (x, y, ic, col) in enumerate(pts):
        s.append('<circle class="mo-lit fx" style="--k:%d" cx="%d" cy="%d" r="27" fill="none" stroke="#fff" stroke-width="3.2"/>' % (k, x, y))
        s.append(node(x, y, 24, ic, 0.4 + k * 0.15, col, fill='#142e14' if col == LIME else DARK, isz=26))
    s.append(node(280, 120, 34, 'you', 0.1, WHITE, fill='#142e14', isz=34))
    return '\n'.join(s)

# ---------- 4 · SCALE: a balance sways gently; a heart on one pan, three small marks on the other ----------
def scale():
    s = ['<path d="M280 62V212" stroke="rgba(255,255,255,0.35)" stroke-width="6" stroke-linecap="round"/><path d="M215 218h130" stroke="rgba(255,255,255,0.35)" stroke-width="6" stroke-linecap="round"/>']
    s.append('<g class="sc-beam"><path d="M130 62H430" stroke="#c4ff49" stroke-width="5" stroke-linecap="round"/>')
    s.append('<path d="M130 62L86 152M130 62L174 152" stroke="rgba(255,255,255,0.45)" stroke-width="2.4"/><path d="M80 152H180Q130 196 80 152Z" fill="#142e14" stroke="#c4ff49" stroke-width="3" stroke-linejoin="round"/>')
    s.append('<path d="M430 62L366 152M430 62L494 152" stroke="rgba(255,255,255,0.45)" stroke-width="2.4"/><path d="M360 152H500Q430 198 360 152Z" fill="#142e14" stroke="rgba(255,255,255,0.7)" stroke-width="3" stroke-linejoin="round"/>')
    s.append(node(130, 120, 24, 'heart', 0.4, LIME, fill='#0f240f'))
    for i, ic in enumerate(('pulse', 'drop', 'labs')):
        s.append(node(396 + i * 34, 130, 15, ic, 0.6 + i * 0.12, WHITE, fill='#0f240f', isz=18))
    s.append('</g>')
    s.append('<circle cx="280" cy="62" r="10" fill="#0f240f" stroke="#c4ff49" stroke-width="3.4"/>')
    return '\n'.join(s)

# ---------- 5 · MIXER: eight sliders, knobs move at their own pace ----------
def mixer():
    names = ['sleep', 'body', 'wine', 'pills', 'wind', 'stress', 'food', 'doc']
    s = []
    for i, n in enumerate(names):
        x = 48 + i * 66
        s.append('<path d="M%d 26V168" stroke="rgba(255,255,255,0.18)" stroke-width="6" stroke-linecap="round"/>' % x)
        s.append(dr('M%d 26V168' % x, 0.1 + i * 0.07, 0.9, 'rgba(196,255,73,0.45)', 2))
        for yy in (47, 97, 147):
            s.append('<path d="M%d %dh8" stroke="rgba(255,255,255,0.25)" stroke-width="2" stroke-linecap="round"/>' % (x + 12, yy))
        col = LIME if i % 2 == 0 else WHITE
        s.append('<g class="pop t" style="--d:%s"><rect class="mx-k" style="--k:%d;--a:%d;--p:%ss" x="%d" y="90" width="30" height="16" rx="8" fill="%s"/></g>' % (0.4 + i * 0.08, i, 22 + (i * 7) % 24, f(4 + (i * 5) % 7 * 0.5), x - 15, col))
        s.append(node(x, 207, 17, n, 0.5 + i * 0.07, col, isz=19))
    return '\n'.join(s)

# ---------- 6 · FLOW: six numbered steps, a dot walks the chart and the return loop, each node lights on arrival ----------
def flow():
    X = [50, 150, 260, 370, 480, 590]; Y = 100
    icons = ['doc', 'tube', None, 'leaf', 'calendar', 'chat']
    dM, pM = path(('M', 50, 100), ('L', 590, 100))
    dR, pR = path(('M', 590, 124), ('L', 590, 225), ('L', 150, 225), ('L', 150, 130))
    dN, _ = path(('M', 260, 126), ('L', 260, 160))
    dN2, _ = path(('M', 260, 196), ('L', 260, 225))
    s = ['<path d="%s" fill="none" stroke="rgba(196,255,73,0.2)" stroke-width="4" stroke-linecap="round"/>' % dM, dr(dM, 0.2, 1.8, LIME, 4)]
    s.append('<path d="%s" fill="none" stroke="rgba(255,255,255,0.28)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/>' % dR)
    s.append('<path d="M150 124l-6 10h12z" fill="#fff" fill-opacity="0.7"/>')
    s.append('<path d="%s" fill="none" stroke="rgba(255,255,255,0.28)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/><path d="%s" fill="none" stroke="rgba(255,255,255,0.28)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 7"/>' % (dN, dN2))
    s.append('<text x="270" y="150" font-size="13" fill="#fff" fill-opacity="0.8">No</text><text x="296" y="92" font-size="13" fill="#c4ff49">Yes</text>')
    full, pf = path(('M', 50, 100), ('L', 590, 100), ('L', 590, 225), ('L', 150, 225), ('L', 150, 100))
    total = 540 + 125 + 440 + 125
    a, b, dur = 4, 94, 12
    s.append(dot('fl-d', 7, WHITE, True))
    G.travel('fl-d', pf, a, b, dur, rest=(150, 100), rest_opacity=0)
    s[-1] = s[-1].replace('class="fl-d"', 'class="fl-d fx"')
    for k, x in enumerate(X):
        pct = a + (b - a) * (x - 50) / total
        dl = pct / 100 * dur - dur
        s.append('<circle class="fl-lit fx" style="--dl:%ss" cx="%d" cy="%d" r="30" fill="none" stroke="#fff" stroke-width="3.2"/>' % (f(dl), x, Y))
        if icons[k]:
            s.append(node(x, Y, 24, icons[k], 0.5 + k * 0.15, LIME if k % 2 == 0 else WHITE, fill='#142e14' if k % 2 == 0 else DARK, isz=26))
        else:
            s.append('<g class="pop t" style="--d:%s"><path d="M260 70L292 100L260 130L228 100Z" fill="#142e14" stroke="#c4ff49" stroke-width="2.6" stroke-linejoin="round"/>%s</g>' % (0.5 + k * 0.15, ico('question', 260, 100, 24, LIME, 1.8)))
        s.append('<g class="pop t" style="--d:%s"><circle cx="%d" cy="44" r="12" fill="none" stroke="rgba(196,255,73,0.6)" stroke-width="2"/><text x="%d" y="49" text-anchor="middle" font-size="13" fill="#c4ff49">%d</text></g>' % (0.6 + k * 0.15, x, x, k + 1))
    s.append(node(260, 178, 18, 'doc', 1.4, WHITE, dashed=True, isz=20))
    return '\n'.join(s)

# ---------- 7 · CALL + CHECKLIST ----------
def call():
    s = ['<g class="pop t" style="--d:0.1"><rect x="30" y="24" width="240" height="160" rx="18" fill="#0f240f" stroke="rgba(255,255,255,0.6)" stroke-width="2.6"/></g>']
    for k, cx in enumerate((105, 195)):
        col = LIME if k == 0 else WHITE
        s.append('<g class="pop t" style="--d:%s"><circle cx="%d" cy="82" r="20" fill="none" stroke="%s" stroke-width="3"/><path d="M%d 140c0-22 14-34 30-34s30 12 30 34" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/></g>' % (0.3 + k * 0.15, cx, col, cx - 30, col))
        s.append('<rect class="cc-sp" style="--k:%d" x="%d" y="154" width="60" height="6" rx="3" fill="%s"/>' % (k, cx - 30, col))
    s.append('<circle class="cc-live" cx="250" cy="44" r="5" fill="#c4ff49"/>')
    s.append('<g class="pop t" style="--d:0.2"><rect x="300" y="24" width="230" height="160" rx="18" fill="#142e14" stroke="rgba(196,255,73,0.45)" stroke-width="2.6"/></g>')
    for k in range(4):
        y = 62 + k * 34
        s.append('<g class="cc-row" style="--k:%d"><circle cx="332" cy="%d" r="10" fill="none" stroke="#c4ff49" stroke-width="2.4"/><g class="cc-tick t" style="--k:%d"><path d="M327 %dl4 4 7-8" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></g><path d="M354 %dH%d" stroke="rgba(255,255,255,0.6)" stroke-width="4" stroke-linecap="round"/></g>' % (k, y, k, y, y, 490 - (k * 17) % 40))
    return '\n'.join(s)

# ---------- 8 · COMPASS ----------
COMPASS = '''<circle cx="180" cy="100" r="76" fill="rgba(196,255,73,0.05)" stroke="rgba(196,255,73,0.25)" stroke-width="3"/>
<circle class="dr" pathLength="1" style="--d:0.1;--dur:1.6s" cx="180" cy="100" r="76" fill="none" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round" transform="rotate(-90 180 100)"/>
<circle cx="180" cy="100" r="58" fill="none" stroke="rgba(255,255,255,0.14)" stroke-width="2"/>
<path d="M180 30v10M180 160v10M110 100h10M240 100h10" stroke="rgba(255,255,255,0.5)" stroke-width="3" stroke-linecap="round"/>
<path d="M130.5 50.5l5 5M229.5 50.5l-5 5M130.5 149.5l5-5M229.5 149.5l-5-5" stroke="rgba(255,255,255,0.25)" stroke-width="2.4" stroke-linecap="round"/>
<circle class="cp-star" cx="180" cy="16" r="4.5" fill="#c4ff49"/>
<g class="cp-needle"><path d="M180 44L168 100H192Z" fill="#c4ff49"/><path d="M180 156L168 100H192Z" fill="rgba(255,255,255,0.45)"/><circle cx="180" cy="100" r="5" fill="#0f240f" stroke="#fff" stroke-width="2"/></g>'''

# ---------- FAQ motif: a magnifier drifts over a question mark ----------
FAQMOTIF = '''<path class="dr" pathLength="1" style="--d:0.2;--dur:1.1s" d="M46 36c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="58" cy="64" r="3" fill="#fff"/>
<g class="fq-mag"><circle cx="58" cy="46" r="30" fill="rgba(196,255,73,0.07)" stroke="#c4ff49" stroke-width="3.6"/><path d="M80 68L100 90" stroke="#c4ff49" stroke-width="5" stroke-linecap="round"/></g>'''

def step_icons():
    return {
     "{{STEP1}}": '<rect x="9" y="5" width="30" height="38" rx="5"/><g class="hi-bl" style="--k:0"><path d="M16 16h16" stroke="#fff"/></g><g class="hi-bl" style="--k:1"><path d="M16 24h16" stroke="#fff"/></g><g class="hi-bl" style="--k:2"><path d="M16 32h9" stroke="#fff"/></g>',
     "{{STEP2}}": '<path d="M13 7v26a4.5 4.5 0 0 0 9 0V7"/><path d="M26 7v26a4.5 4.5 0 0 0 9 0V7"/><g class="hi-gr" style="--k:0"><rect x="15.5" y="21" width="4" height="14" fill="#c4ff49" stroke="none"/></g><g class="hi-gr" style="--k:1"><rect x="28.5" y="24" width="4" height="11" fill="#fff" stroke="none"/></g>',
     "{{STEP3}}": '<path d="M24 5l16 16-16 16L8 21z"/><g class="hi-pu" style="--k:0"><path d="M18 21l4.5 4.5L31 16" stroke="#fff"/></g><path d="M24 37v7"/>',
     "{{STEP4}}": '<g class="hi-sw" style="--k:0"><path d="M24 42V16"/><path d="M24 28c-9 0-13-5-13-13 9 0 13 5 13 13z" fill="rgba(196,255,73,0.2)"/><path d="M24 22c7 0 11-4 11-11-7 0-11 4-11 11z" fill="rgba(255,255,255,0.15)" stroke="#fff"/></g>',
     "{{STEP5}}": '<rect x="6" y="9" width="36" height="33" rx="6"/><path d="M6 19h36M16 5v8M32 5v8"/><g class="hi-pu" style="--k:0"><circle cx="24" cy="31" r="4.2" fill="#c4ff49" stroke="none"/></g><circle cx="14" cy="31" r="2" fill="#fff" stroke="none"/><circle cx="34" cy="31" r="2" fill="#fff" stroke="none"/>',
     "{{STEP6}}": '<g class="hi-bl" style="--k:0"><path d="M6 8h22a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H16l-6 5v-5H6a2 2 0 0 1-2-2V10a2 2 0 0 1 2-2z"/></g><g class="hi-bl" style="--k:3"><path d="M20 26h20a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-4v5l-6-5H20a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2z" stroke="#fff"/></g>',
    }

HUB = hub(G, [(110, 50, 'labs'), (110, 150, 'coach'), (450, 50, 'caps'), (450, 150, 'tube')])
slots = {"{{HERO}}": hero_fork(), "{{LOOP}}": loop(), "{{ORBIT}}": orbit(), "{{SCALE}}": scale(), "{{MIXER}}": mixer(), "{{FLOW}}": flow(),
         "{{CALL}}": call(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB, "{{FAQMOTIF}}": FAQMOTIF, "{{COMPASS}}": COMPASS}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Starting testosterone replacement therapy (TRT) versus addressing the causes of low testosterone first",
      "TRT or fix the causes first", "Should I start TRT or fix the causes of low testosterone first?", slots, G)
