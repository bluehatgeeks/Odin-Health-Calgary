"""Build /workspace/pages/when-to-get-checked-for-low-t/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "when-to-get-checked-for-low-t"
TITLE = "When to Get Checked for Low T | Odin Health Lab"
DESC = "When low-T symptoms warrant testing: two morning labs, what temporarily lowers T, free T when borderline, and next steps in Canada and the USA."
OG_ALT = "Odin Health Lab: when to get checked for low testosterone, symptom clusters, two morning labs and next steps"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 158, (len(TITLE), len(DESC))

common.ICONS.update({
 "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "split": '<path d="M4 7c4 0 8 2 16 6"/><path d="M4 7h7c2 0 2 10 4 10h5"/>',
 "pin": '<path d="M12 21s-6-6.2-6-11a6 6 0 0 1 12 0c0 4.8-6 11-6 11z"/><circle cx="12" cy="10" r="2.2"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/>',
})

FAQ = [
 ("When is it worth getting checked for low testosterone?",
  "Testing is most useful when sexual symptoms (lower sex drive, fewer morning erections or erectile dysfunction) show up together with fatigue, less muscle or more belly fat, or low mood and poor focus. In the European Male Ageing Study of 3,369 men aged 40 to 79, the three sexual symptoms had the clearest link with low testosterone. The Endocrine Society (2018) and the Canadian Urological Association (2021) both diagnose low T from symptoms plus consistently low lab results, not from a single vague complaint."),
 ("Is vague tiredness alone a reason to test?",
  "Tiredness on its own is a weak signal. The American Urological Association notes that symptoms linked to low testosterone are very non-specific and can come from chronic fatigue, chronic stress or a depressed state. The Canadian Urological Association recommends ruling out overlapping conditions such as depression, an underactive thyroid and sleep disorders. Isolated fatigue is still worth looking into, but a symptom cluster that includes sexual changes is a clearer cue to check testosterone."),
 ("Why two early-morning tests instead of one?",
  "Testosterone peaks in the morning and food lowers it, and levels swing from day to day. The Endocrine Society recommends fasting morning total testosterone as the first test and a repeat to confirm; in that guideline, about three in ten men whose first result looked low had a normal result on repeat. The American Urological Association uses a total testosterone below 300 ng/dL on two early-morning tests. The Canadian Urological Association recommends a morning draw between 7 and 11 a.m. and suggests below 10 nmol/L as a reasonable threshold."),
 ("What can temporarily lower testosterone?",
  "The Endocrine Society and the Canadian Urological Association list causes that suppress testosterone and should be checked alongside the labs: acute illness, opioids and glucocorticoids, nutritional deficiency, obesity, diabetes, sleep apnea and short or broken sleep. Extreme exercise and extreme dieting are also on the Canadian list. Sorting those out matters because a low result during illness or a short stretch of bad sleep may not reflect your usual baseline."),
 ("What happens after the labs?",
  'When total testosterone is borderline, or when something may change SHBG (the protein that carries testosterone), the Endocrine Society recommends checking free testosterone. LH helps classify whether the issue is in the testes (high LH) or the brain&rsquo;s signal (low or normal LH). We go through your symptoms and results with you by telehealth, then build a sleep, training, nutrition and stress plan with follow-up check-ins and repeat labs. See <a href="%s/low-testosterone-labs-to-ask-for">which labs to ask for</a>.' % SITE),
 ("How does Odin Health Lab work with my doctor?",
  'Odin Health Lab is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We work alongside your own doctor: we go through your symptoms and lab results with you, build your sleep, training, nutrition and stress plan, and track your progress with follow-up check-ins and repeat labs. We can share your symptom list, plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

def txt(x, y, s, size=13, fill='#fff', op=0.85, anchor='middle', extra=''):
    return '<text x="%s" y="%s" font-size="%s" fill="%s" fill-opacity="%s" text-anchor="%s"%s>%s</text>' % (f(x), f(y), size, fill, op, anchor, extra, s)

def hero():
    s = ['<defs><radialGradient id="wc-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.16"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="210" ry="130" fill="url(#wc-g)"/>']
    nodes = [(70, 100, 'list', 'Symptoms'), (240, 70, 'compass', 'Worth a check'), (410, 100, 'tube', 'Morning labs'), (240, 230, 'check', 'Confirmed')]
    d, pts = path(('M', 70, 100), ('C', 140, 40, 200, 40, 240, 70), ('C', 290, 40, 360, 40, 410, 100), ('C', 400, 170, 300, 220, 240, 230), ('C', 180, 220, 80, 170, 70, 100), n=16)
    s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>' % d)
    s.append(dr(d, 0.25, 1.8, 'rgba(196,255,73,0.5)', 2.4))
    s.append(dot('wc-o fx', 6, LIME, ring=True)); G.travel('wc-o', pts, 4, 92, 11, rest=pts[0], rest_opacity=0, fade=2)
    for i, (x, y, ic, lab) in enumerate(nodes):
        s.append(node(x, y, 28 if i != 1 else 30, ic, 0.15 + i * 0.12, LIME if i in (1, 3) else WHITE, fill='#142e14' if i in (1, 3) else DARK, isz=30 if i != 1 else 32))
        s.append(txt(x, y + 48, lab, 13, '#c4ff49' if i in (1, 3) else '#fff', 0.9))
    s.append('<circle class="wc-ring fx" cx="240" cy="70" r="38" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    return '\n'.join(s)

def clusters():
    s = []
    groups = [
      (90, 120, 'heart', 'Sexual', LIME, True),
      (240, 70, 'batt', 'Energy + body', WHITE, True),
      (390, 120, 'brain', 'Mood + focus', WHITE, True),
      (240, 210, 'sleep', 'Tiredness alone', 'rgba(255,255,255,0.55)', False),
    ]
    for k, (x, y, ic, lab, col, strong) in enumerate(groups):
        cls = 'cl-g' if strong else 'cl-w'
        s.append('<g class="%s" style="--k:%d"><circle cx="%d" cy="%d" r="46" fill="%s" stroke="%s" stroke-width="2.2"%s/>%s%s</g>'
                 % (cls, k if strong else 0, x, y,
                    'rgba(196,255,73,0.12)' if strong else 'rgba(255,255,255,0.03)',
                    col if strong else 'rgba(255,255,255,0.35)',
                    '' if strong else ' stroke-dasharray="4 5"',
                    ico(ic, x, y - 6, 24, LIME if strong and k == 0 else WHITE, 1.8),
                    txt(x, y + 22, lab, 12, '#c4ff49' if strong and k == 0 else '#fff', 0.9)))
    for i, (x, y) in enumerate(((90, 120), (240, 70), (390, 120))):
        d, pts = path(('M', x, y), ('L', 240, 150))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="2 6" fill="none"/>' % d)
        s.append(dot('cl-p%d fx' % i, 4.5, LIME if i == 0 else WHITE))
        G.travel('cl-p%d' % i, pts, 12, 55, 7, delay='%ss' % f(-i * 2.2), rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(240, 150, 18, 'check', 0.5, LIME, fill='#142e14', isz=20))
    s.append(txt(240, 268, 'Clusters beat a single vague symptom', 13, '#c4ff49', 0.95))
    return '\n'.join(s)

def twotests():
    s = []
    d, pts = path(('M', 60, 130), ('L', 500, 130))
    s.append('<path d="M60 130H500" stroke="rgba(255,255,255,0.14)" stroke-width="2.4" stroke-dasharray="2 8" stroke-linecap="round"/>')
    s.append(dr(d, 0.3, 1.5, 'rgba(196,255,73,0.55)', 2.4))
    s.append(dot('tt-p fx', 6, LIME, ring=True)); G.travel('tt-p', pts, 6, 85, 9, rest=pts[-1], rest_opacity=0, fade=3, ease='ease-in-out')
    items = [(90, 'sun', 'Fasting AM', WHITE), (220, 'tube', 'Test 1', LIME), (350, 'tube', 'Test 2', LIME), (480, 'check', 'Confirmed', LIME)]
    for i, (x, ic, lab, col) in enumerate(items):
        s.append(node(x, 130, 28, ic, 0.15 + i * 0.12, col, fill='#142e14' if col == LIME else DARK, isz=30))
        s.append(txt(x, 186, lab, 13, '#c4ff49' if i == 3 else '#fff', 0.9))
    for k, x in enumerate((220, 350)):
        s.append('<g class="tt-sun" style="--k:%d">%s</g>' % (k, ico('sun', x, 58, 24, LIME, 1.8)))
    for x, sym in ((155, '+'), (285, '+'), (415, '=')):
        s.append(txt(x, 138, sym, 22, '#fff', 0.7))
    s.append('<g class="tt-chip"><rect x="160" y="214" width="240" height="36" rx="10" fill="rgba(196,255,73,0.1)" stroke="#c4ff49" stroke-width="1.6"/>%s</g>'
             % txt(280, 237, 'About 3 in 10 first lows normalize', 13, '#c4ff49', 0.95))
    s.append('<circle class="tt-ring fx" cx="480" cy="130" r="36" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    return '\n'.join(s)

def temporary():
    s = []
    causes = [(70, 70, 'pulse', 'Illness'), (200, 50, 'pills', 'Opioids'), (340, 50, 'sleep', 'Short sleep'),
              (470, 70, 'scale', 'Weight'), (140, 200, 'train', 'Overtraining'), (400, 200, 'food', 'Crash diet')]
    for k, (x, y, ic, lab) in enumerate(causes):
        s.append('<g class="tm-c" style="--k:%d"><circle cx="%d" cy="%d" r="36" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.45)" stroke-width="1.8"/>%s%s</g>'
                 % (k, x, y, ico(ic, x, y - 6, 22, LIME if k % 2 == 0 else WHITE, 1.8), txt(x, y + 22, lab, 12, '#fff', 0.85)))
        d, pts = path(('M', x, y), ('L', 280, 130))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.1)" stroke-width="1.6" stroke-dasharray="2 6" fill="none"/>' % d)
        s.append(dot('tm-p%d fx' % k, 4, WHITE if k % 2 else LIME))
        G.travel('tm-p%d' % k, pts, 8, 48, 8, delay='%ss' % f(-k * 1.4), rest=pts[0], rest_opacity=0, fade=3)
    s.append('<rect x="248" y="70" width="64" height="120" rx="12" fill="none" stroke="#fff" stroke-opacity="0.7" stroke-width="2.4"/>')
    s.append('<rect class="tm-m" x="255" y="78" width="50" height="104" rx="8" fill="#c4ff49" fill-opacity="0.85"/>')
    s.append(txt(280, 214, 'T level', 12, '#c4ff49', 0.95))
    s.append(txt(280, 248, 'Causes can dip the reading', 13, '#fff', 0.75))
    return '\n'.join(s)

def borderline():
    s = []
    s.append('<rect x="40" y="40" width="140" height="160" rx="14" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.35)" stroke-width="1.8"/>')
    s.append(txt(110, 70, 'Total T', 14, '#fff', 0.9))
    s.append('<path d="M70 100H150" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>')
    s.append('<path class="bd-line" d="M70 130H150" stroke="#c4ff49" stroke-width="2.4" stroke-dasharray="4 4"/>')
    s.append(txt(110, 118, 'Borderline', 11, '#c4ff49', 0.95))
    s.append('<g class="bd-dot"><circle cx="110" cy="148" r="8" fill="#c4ff49"/></g>')
    s.append(txt(110, 180, 'Near cut-off', 12, '#fff', 0.75))
    d, pts = path(('M', 180, 120), ('L', 250, 120))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.2)" stroke-width="2.2" stroke-dasharray="2 6" fill="none"/>' % d)
    s.append(dot('bd-p fx', 5, LIME)); G.travel('bd-p', pts, 10, 70, 5, rest=pts[-1], rest_opacity=0, fade=3)
    for k, (x, ic, lab) in enumerate(((300, 'drop', 'Free T'), (400, 'link', 'SHBG'), (500, 'gland', 'LH'))):
        s.append('<g class="bd-b" style="--k:%d"><circle cx="%d" cy="120" r="34" fill="#142e14" stroke="#c4ff49" stroke-width="2"/>%s%s</g>'
                 % (k, x, ico(ic, x, 112, 22, LIME, 1.8), txt(x, 168, lab, 13, '#c4ff49', 0.95)))
    s.append(txt(400, 210, 'Explain a borderline result and the cause', 13, '#fff', 0.75))
    return '\n'.join(s)

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

def final():
    s = ['<circle cx="180" cy="110" r="64" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>']
    s.append('<circle cx="180" cy="110" r="40" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>')
    s.append('<g class="fn-nd"><path d="M180 50 L188 110 L180 170 L172 110 Z" fill="#c4ff49" fill-opacity="0.9"/><circle cx="180" cy="110" r="8" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/></g>')
    s.append(node(300, 110, 28, 'check', 0.3, LIME, fill='#142e14', isz=30))
    d, pts = path(('M', 248, 110), ('L', 272, 110))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-dasharray="2 5" fill="none"/>' % d)
    s.append(dot('fn-p fx', 5, LIME)); G.travel('fn-p', pts, 20, 70, 4, rest=pts[-1], rest_opacity=0, fade=2)
    s.append(txt(180, 198, 'Clear next step', 13, '#fff', 0.8))
    return '\n'.join(s)

FAQMOTIF = '''<circle cx="36" cy="48" r="28" stroke="#fff" stroke-width="3" fill="none"/>
<path class="fq-nd" d="M36 24 L40 48 L36 72 L32 48 Z" fill="#c4ff49"/>
<circle cx="36" cy="48" r="5" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/>
<path class="dr" pathLength="1" style="--d:0.25;--dur:1.1s" d="M74 38c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="86" cy="66" r="3" fill="#fff"/>
<path class="fq-st" style="--k:0" d="M106 18v10M101 23h10" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/>'''

def step_icons():
    return {
     "{{STEP1}}": '<path d="M14 8h22a2 2 0 0 1 2 2v30a2 2 0 0 1-2 2H14a2 2 0 0 1-2-2V10a2 2 0 0 1 2-2z"/><path d="M20 18h12M20 26h12M20 34h8"/><g class="hi-bl" style="--k:0"><circle cx="16" cy="18" r="1.8" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="16" cy="26" r="1.8" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="16" cy="34" r="1.8" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M19 6h10"/><path d="M21 6v26a3 3 0 0 0 6 0V6"/><path d="M21 20h6"/><g class="hi-gr" style="--k:0"><path d="M33 40V30M38 40V24M43 40V34" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<g class="hi-sl" style="--k:0"><path d="M10 20v10M6 22v6M38 20v10M42 22v6M10 25h28" stroke="#c4ff49"/></g><path d="M18 40c4-6 8-6 12 0"/><path d="M24 8a5 5 0 1 0 5 5"/>',
     "{{STEP4}}": '<path d="M6 36h8l5-12 7 16 5-10h11"/><g class="hi-ck" style="--k:0"><path d="M30 10l5 5 9-11" stroke="#c4ff49"/></g>',
    }

def hub_nodes():
    icons = ['list', 'split', 'tube', 'calendar', 'scale', 'link', 'flame', 'drop', 'coach', 'caps', 'body']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)
        out.append((round(280 + 240 * math.cos(a)), round(100 + 70 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{CLUSTERS}}": clusters(), "{{TWOTESTS}}": twotests(), "{{TEMP}}": temporary(),
         "{{BORDER}}": borderline(), "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB,
         "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "When to get checked for low testosterone in men",
      "When to get checked for low T", "When should you get checked for low testosterone?", slots, G, published="2026-10-16")
