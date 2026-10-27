"""Build /workspace/pages/trt-and-fertility/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *

SLUG = "trt-and-fertility"
TITLE = "TRT and Fertility: Effects and Options | Odin Health Lab"
DESC = "Does testosterone therapy affect fertility? How TRT lowers sperm production, whether it recovers, and options like hCG and clomiphene. Canada and USA."
OG_ALT = "Odin Health Lab: how testosterone therapy affects fertility and the options for men in Canada and the USA"
assert len(TITLE) <= 60 and len(DESC) <= 160, (len(TITLE), len(DESC))

common.ICONS.update({"pause": '<circle cx="12" cy="12" r="9"/><path d="M10 8.5v7M14 8.5v7"/>'})

FAQ = [
 ("Does testosterone therapy cause infertility?",
  "It can lower fertility while you are on it. Testosterone from outside tells your brain to turn down LH and FSH, the signals your testes need to make sperm, and sperm counts can fall very low, in some men to none. The American Urological Association and Canadian Urological Association guidelines both describe this effect. For many men it eases after stopping, but how quickly varies from man to man. If children are part of your plans, we help you look at options that keep your own production going."),
 ("How long does it take for sperm to come back after stopping?",
  "It varies. In male contraceptive trials of testosterone, about two-thirds of men had sperm back in the ejaculate within six months of stopping, and roughly one in ten took until the second year (AUA guideline). In one study of men who stopped therapy and used hCG and/or a SERM, being older and having been on therapy longer were linked to a lower chance of recovery at six and twelve months. Some men do not return to their earlier level. A semen analysis after stopping shows where you stand, and we track it with you."),
 ("Can I use hCG, clomiphene or similar options instead of testosterone?",
  "For men with low testosterone who want to keep their fertility, the AUA says aromatase inhibitors, hCG, SERMs such as clomiphene, or a combination may be used, and the Canadian guideline lists the same classes as off-label alternatives. They work by raising your own testosterone rather than replacing it. Each has its own trade-offs, response differs from man to man, and they are prescription medicines. We help you compare them against your labs and your timeline."),
 ("Are hCG and enclomiphene available in Canada and the USA?",
  "hCG products are authorized in both countries: Health Canada lists chorionic gonadotropin products such as Pregnyl, and FDA-approved brands include Novarel and Pregnyl. In the USA, hCG has been regulated as a biologic since March 23, 2020, which ended the pharmacy-compounding exemptions for it. Clomiphene is authorized for women in both countries and used off-label in men. Enclomiphene is not an FDA-approved product, and Health Canada&rsquo;s Drug Product Database has no enclomiphene listing. Rules and stock change, so we check what is available to you where you live."),
 ("Do I need a semen analysis before starting treatment?",
  'If you may want children, it is a sensible baseline. The AUA guideline recommends a reproductive health evaluation before treatment for men with low testosterone who are interested in fertility, including a testicular exam, FSH and a semen analysis where indicated. A baseline also makes later results easier to read. We help you arrange the right tests and go through them with you. See our <a href="%s/low-testosterone-labs-to-ask-for">lab guide</a>.' % SITE),
 ("How does Odin Health Lab work with my doctor and fertility specialists?",
  'Odin Health Lab is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We review your labs and semen results with you, map your options around your fertility goals, build your plan and track your progress. We can share your plan and results with your own doctor or a men&rsquo;s fertility specialist if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

def wob(lane, amp, ph, x0=100, x1=400, step=12):
    return [(x, lane + amp * math.sin(x / 18.0 + ph)) for x in range(x0, x1 + 1, step)]

def tad(cls, extra=''):
    return ('<g class="%s"><g class="sm-t"><path d="M-5 0q-6-5-12 0t-12 0t-12 0" fill="none" stroke="#c4ff49" stroke-opacity="0.8" stroke-width="2.4" stroke-linecap="round"/></g>'
            '<circle r="6.5" fill="#c4ff49"/>%s</g>') % (cls, extra)

# ---------- 1 · HERO: swimmers cross a gate that narrows and opens; brain on the left, calendar on the right ----------
def hero_swim():
    s = ['<defs><radialGradient id="sm-g" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.15"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="228" ry="140" fill="url(#sm-g)"/>']
    for y in (136, 160, 184):
        s.append('<path d="M96 %d H404" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/>' % y)
    s.append('<g class="pop t" style="--d:0.35"><g class="sm-gt"><rect x="234" y="36" width="18" height="82" rx="9" fill="#142e14" stroke="rgba(196,255,73,0.6)" stroke-width="2.4"/></g>'
             '<g class="sm-gb"><rect x="234" y="202" width="18" height="82" rx="9" fill="#142e14" stroke="rgba(196,255,73,0.6)" stroke-width="2.4"/></g></g>')
    s.append(dr('M243 24V10M243 296V310', 0.8, 0.5, 'rgba(255,255,255,0.35)', 2.4))
    specs = [(148, 4, 0.0, 0), (160, 5, 1.4, 1), (172, 4, 2.6, 2), (154, 5, 3.9, 3), (166, 4, 5.1, 4)]
    for i, (lane, amp, ph, k) in enumerate(specs):
        s.append(tad('sm%d' % k))
        pts = wob(lane, amp, ph)
        G.travel('sm%d' % k, pts, 3, 95, 10, delay='%ss' % f(-i * 2), rest=pts[3 + i * 4], fade=2.5)
    s.append(node(58, 160, 30, 'brain', 0.1, LIME, fill='#142e14', isz=34))
    s.append(node(430, 160, 30, 'calendar', 0.5, WHITE, isz=32))
    return '\n'.join(s)

# ---------- 2 · MECHANISM: outside testosterone bar rises while four of your own bars fall ----------
def mech():
    s = []
    def bar(x, scale, kind, ic, k, color, delay):
        out = ['<g class="pop t" style="--d:%s"><rect x="%d" y="26" width="36" height="140" rx="12" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.35)" stroke-width="2.4"/>'
               '<rect class="mc-bar mc-%s" style="--s:%s;--k:%d" x="%d" y="26" width="36" height="140" rx="12" fill="%s" fill-opacity="%s"/></g>'
               % (delay, x, kind, scale, k, x, color, '0.9' if kind == 'up' else '0.6')]
        out.append(node(x + 18, 204, 20, ic, delay + 0.2, LIME if kind != 'up' else WHITE, isz=22))
        return ''.join(out)
    s.append(bar(52, 0.9, 'up', 'pills', 0, WHITE, 0.05))
    s.append(dr('M112 96H156', 0.7, 0.7, 'rgba(255,255,255,0.5)', 2.8))
    s.append('<path d="M156 96l-9-6v12z" fill="#fff" fill-opacity="0.8"/>')
    for k, (x, sc, ic) in enumerate(((196, 0.36, 'brain'), (290, 0.42, 'gland'), (384, 0.26, 'drop'), (478, 0.2, 'tube'))):
        s.append(bar(x, sc, 'dn', ic, k, LIME, 0.15 + k * 0.12))
    return '\n'.join(s)

# ---------- 3 · STAGES: four signposts sway; a dot walks the ground line ----------
def stages():
    s = ['<path d="M24 220H536" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round"/>']
    s.append(dr('M24 232H536', 0.4, 1.4, 'rgba(196,255,73,0.25)', 2.4))
    for k, (x, ic) in enumerate(((78, 'clock'), (218, 'calendar'), (358, 'question'), (498, 'check'))):
        col = LIME if k % 2 == 0 else WHITE
        s.append('<g class="pop t" style="--d:%s"><path d="M%d 96V220" stroke="rgba(255,255,255,0.55)" stroke-width="6" stroke-linecap="round"/>'
                 '<g class="sp-b" style="--k:%d"><rect x="%d" y="34" width="108" height="56" rx="14" fill="#142e14" stroke="%s" stroke-width="2.6"/>%s</g></g>'
                 % (0.1 + k * 0.14, x, k, x - 54, 'rgba(196,255,73,0.75)' if col == LIME else 'rgba(255,255,255,0.7)', ico(ic, x, 62, 30, col, 1.7)))
    s.append(dot('sp-w', 6, LIME, ring=True))
    G.travel('sp-w', [(30, 208), (530, 208)], 3, 96, 12, rest=(300, 208), fade=2.5)
    return '\n'.join(s)

# ---------- 4 · RECOVERY: three curves back toward the starting level; dots ride the first two ----------
def recovery():
    dA, pA = path(('M', 60, 200), ('C', 170, 200, 250, 150, 300, 112), ('C', 360, 66, 430, 60, 520, 60), n=22)
    dB, pB = path(('M', 60, 206), ('C', 220, 206, 330, 190, 420, 150), ('C', 460, 132, 495, 112, 520, 104), n=22)
    dC, pC = path(('M', 60, 212), ('C', 180, 212, 280, 204, 360, 190), ('C', 430, 178, 480, 170, 520, 166), n=22)
    s = ['<path d="M50 220H536M50 30V220" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round"/>',
         '<path d="M50 60H536" stroke="rgba(255,255,255,0.28)" stroke-width="2.4" stroke-dasharray="3 8" stroke-linecap="round"/>']
    for x, lab in ((60, 'Stop'), (200, 'Half a year'), (340, 'Year 1'), (500, 'Year 2')):
        s.append('<path d="M%d 220v8" stroke="rgba(255,255,255,0.45)" stroke-width="2.4" stroke-linecap="round"/><text x="%d" y="248" font-size="13" fill="#fff" fill-opacity="0.75" text-anchor="middle">%s</text>' % (x, x, lab))
    s.append(dr(dC, 0.9, 1.4, 'rgba(255,255,255,0.35)', 3.4))
    s.append(dr(dB, 0.6, 1.4, 'rgba(255,255,255,0.8)', 3.4))
    s.append(dr(dA, 0.3, 1.4, LIME, 4.4))
    s.append(dot('rc-p0', 7, LIME, ring=True)); G.travel('rc-p0', pA, 4, 58, 10, rest=pA[-1], fade=2.5)
    s.append(dot('rc-p1', 6, WHITE)); G.travel('rc-p1', pB, 4, 70, 10, delay='-4s', rest=pB[-1], fade=2.5)
    s.append(node(520, 60, 14, 'check', 1.0, LIME, isz=16))
    return '\n'.join(s)

# ---------- 5 · BASELINE: sample -> a microscope field of drifting swimmers -> result sheet ----------
def baseline():
    s = ['<defs><clipPath id="sa-c"><circle cx="280" cy="110" r="70"/></clipPath></defs>']
    s.append(dr('M112 110H208M352 110H448', 0.3, 0.9, 'rgba(255,255,255,0.4)', 2.6))
    s.append('<g class="pop t" style="--d:0.2"><circle cx="280" cy="110" r="72" fill="rgba(196,255,73,0.05)" stroke="rgba(255,255,255,0.7)" stroke-width="3"/></g>')
    s.append('<circle class="sa-lens fx" cx="280" cy="110" r="72" fill="none" stroke="#c4ff49" stroke-width="2.4"/>')
    s.append('<g clip-path="url(#sa-c)"><path d="M210 80H350M210 110H350M210 140H350M250 40V180M280 40V180M310 40V180" stroke="rgba(255,255,255,0.08)" stroke-width="1.6"/>')
    for k, (x, y, dx, dy) in enumerate(((246, 78, 26, 12), (300, 92, -22, 16), (258, 128, 24, -14), (320, 140, -20, -12), (284, 108, 14, 22), (232, 108, 30, -6), (330, 112, -26, 6))):
        s.append('<g class="sa-d" style="--k:%d;--dx:%dpx;--dy:%dpx"><path d="M%d %dq-5-4-10 0t-10 0" fill="none" stroke="#c4ff49" stroke-opacity="0.7" stroke-width="2" stroke-linecap="round"/><circle cx="%d" cy="%d" r="4.2" fill="#c4ff49"/></g>' % (k, dx, dy, x - 4, y, x, y))
    s.append('</g>')
    s.append(node(76, 110, 30, 'tube', 0.1, LIME, fill='#142e14', isz=32))
    s.append(node(484, 110, 30, 'doc', 0.6, WHITE, isz=32))
    s.append(dot('sa-p', 6, WHITE)); G.travel('sa-p', [(112, 110), (448, 110)], 6, 94, 8, rest=(398, 110), fade=2.5)
    s.append(dr('M236 196H324', 1.0, 0.8, 'rgba(255,255,255,0.35)', 2.4))
    return '\n'.join(s)

# ---------- 6 · OPTIONS: four routes on an arc; a dot rides along and each node lights as it passes ----------
def options():
    P = [(70, 190), (150, 10), (410, 10), (490, 190)]
    cub = lambda t: tuple((1-t)**3*P[0][i] + 3*(1-t)**2*t*P[1][i] + 3*(1-t)*t*t*P[2][i] + t**3*P[3][i] for i in (0, 1))
    d, pts = path(('M',) + P[0], ('C',) + P[1] + P[2] + P[3], n=60)
    L = [0.0]
    for i in range(1, len(pts)): L.append(L[-1] + math.hypot(pts[i][0]-pts[i-1][0], pts[i][1]-pts[i-1][1]))
    a, b, dur = 5, 93, 12
    s = ['<path d="%s" fill="none" stroke="rgba(255,255,255,0.18)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 8"/>' % d]
    s.append(dr(d, 0.3, 1.6, 'rgba(196,255,73,0.45)', 3))
    labels = ['hCG', 'SERMs', 'Aromatase inhibitors', 'Causes first']
    icons = ['drop', 'pills', 'scale', 'leaf']
    for k, t in enumerate((0, 1/3, 2/3, 1)):
        x, y = cub(t)
        idx = min(len(pts) - 1, max(0, round(t * (len(pts) - 1))))
        frac = L[idx] / L[-1]
        dl = (a + (b - a) * frac) / 100 * dur - dur
        s.append('<circle class="ar-lit fx" style="--dl:%ss" cx="%s" cy="%s" r="36" fill="none" stroke="#fff" stroke-width="3"/>' % (f(dl), f(x), f(y)))
        s.append(node(x, y, 28, icons[k], 0.4 + k * 0.18, LIME if k % 2 == 0 else WHITE, isz=30))
        s.append('<text x="%s" y="%s" font-size="13" fill="#fff" fill-opacity="0.85" text-anchor="middle">%s</text>' % (f(x), f(y + 50), labels[k]))
    s.append(dot('ar-p', 6, LIME, ring=True)); G.travel('ar-p', pts, a, b, dur, rest=pts[len(pts)//2], fade=2.5)
    return '\n'.join(s)

# ---------- 7 · REGIONS: Canada and USA panels, a scan line lights each row ----------
def regions():
    s = []
    rows = [('hCG', 'auth'), ('Clomiphene', 'off'), ('Enclomiphene', 'none')]
    ys = [92, 144, 196]
    scan_from, scan_to, dur = 70, 214, 8
    for pi, (x0, title) in enumerate(((20, 'Canada'), (292, 'USA'))):
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="14" width="248" height="226" rx="18" fill="rgba(255,255,255,0.03)" stroke="rgba(196,255,73,0.28)" stroke-width="1.8"/>'
                 '<text x="%d" y="46" font-size="17" fill="#c4ff49" text-anchor="middle">%s</text></g>' % (0.05 + pi * 0.15, x0, x0 + 124, title))
        for ri, (name, st) in enumerate(rows):
            y = ys[ri]
            frac = (y - scan_from) / (scan_to - scan_from)
            tpc = 8 + 64 * frac
            dl = tpc / 100 * dur - dur
            s.append('<rect class="rg-hl fx" style="--dl:%ss" x="%d" y="%d" width="224" height="42" rx="12" fill="rgba(196,255,73,0.14)" stroke="rgba(196,255,73,0.5)" stroke-width="1.6"/>' % (f(dl), x0 + 12, y - 21))
            s.append('<g class="pop t" style="--d:%s">' % f(0.3 + ri * 0.12 + pi * 0.1))
            s.append(ico({'hCG': 'drop', 'Clomiphene': 'pills', 'Enclomiphene': 'tube'}[name], x0 + 40, y, 22, LIME if st == 'auth' else 'rgba(255,255,255,0.8)', 1.8))
            s.append('<text x="%d" y="%d" font-size="15" fill="#fff" text-anchor="start">%s</text>' % (x0 + 62, y + 5, name))
            if st == 'auth':
                s.append('<circle cx="%d" cy="%d" r="11" fill="#c4ff49"/><path d="M%d %dl3.4 3.4 6-7" fill="none" stroke="#0f240f" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>' % (x0 + 214, y, x0 + 209, y))
            elif st == 'off':
                s.append('<circle cx="%d" cy="%d" r="11" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3.6 3.6"/><circle cx="%d" cy="%d" r="3" fill="#fff"/>' % (x0 + 214, y, x0 + 214, y))
            else:
                s.append('<circle cx="%d" cy="%d" r="11" fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="2.4"/><path d="M%d %dh10" stroke="rgba(255,255,255,0.6)" stroke-width="2.6" stroke-linecap="round"/>' % (x0 + 214, y, x0 + 209, y))
            s.append('</g>')
    s.append('<g class="rg-scan fx"><path d="M26 %d H534" stroke="#c4ff49" stroke-opacity="0.75" stroke-width="3" stroke-linecap="round"/></g>' % scan_from)
    G.motion.append('/*scan-meta*/')
    return '\n'.join(s)

# ---------- final: a sprout in a pot, leaves sway, sparkles twinkle ----------
SPROUT = '''<path d="M130 156h100l-12 40h-76z" fill="#142e14" stroke="rgba(196,255,73,0.75)" stroke-width="2.6" stroke-linejoin="round"/>
<path d="M118 156H242" stroke="rgba(196,255,73,0.75)" stroke-width="3.4" stroke-linecap="round"/>
<path class="dr" pathLength="1" style="--d:0.2;--dur:1.1s" d="M180 156C180 128 176 104 180 76" fill="none" stroke="#c4ff49" stroke-width="3.6" stroke-linecap="round"/>
<g class="pl-lf" style="--k:0;transform-origin:100% 100%"><path d="M180 124C150 124 136 104 138 90C162 90 178 104 180 124z" fill="#c4ff49" fill-opacity="0.85"/></g>
<g class="pl-lf" style="--k:1;transform-origin:0% 100%"><path d="M180 104C210 104 224 84 222 70C198 70 182 84 180 104z" fill="#fff" fill-opacity="0.8"/></g>
<circle class="pl-bd" cx="180" cy="70" r="7" fill="#c4ff49"/>
<path class="pl-sp" style="--k:0" d="M120 56v14M113 63h14" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path class="pl-sp" style="--k:1" d="M246 40v12M240 46h12" stroke="#c4ff49" stroke-width="2.6" stroke-linecap="round"/>
<path class="pl-sp" style="--k:2" d="M204 22v10M199 27h10" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'''
SPROUT += node(60, 112, 26, 'calendar', 0.4, LIME, isz=28) + node(300, 112, 26, 'heart', 0.55, WHITE, isz=28)

# ---------- FAQ motif ----------
FAQMOTIF = '''<g class="fq-sm"><path d="M32 52q-7-6-14 0t-14 0" fill="none" stroke="#c4ff49" stroke-opacity="0.8" stroke-width="3" stroke-linecap="round"/><circle cx="38" cy="52" r="8" fill="#c4ff49"/></g>
<path class="dr" pathLength="1" style="--d:0.2;--dur:1.1s" d="M66 38c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="78" cy="66" r="3" fill="#fff"/>'''

def step_icons():
    return {
     "{{STEP1}}": '<rect x="8" y="10" width="32" height="30" rx="4"/><path d="M8 19h32M16 6v8M32 6v8"/><g class="hi-pu" style="--k:0"><circle cx="24" cy="29" r="4.2" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M18 6v22a6 6 0 0 0 12 0V6"/><path d="M14 6h20"/><g class="hi-gr" style="--k:0"><rect x="20.5" y="22" width="7" height="12" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:0"><circle cx="38" cy="30" r="2.8" fill="#fff" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="10" cy="22" r="2.8" fill="#fff" stroke="none"/></g>',
     "{{STEP3}}": '<path d="M12 42V10"/><g class="hi-sw" style="--k:0"><path d="M12 10h22l6 6-6 6H12z" fill="rgba(196,255,73,0.22)"/></g><path d="M8 42h12"/>',
     "{{STEP4}}": '<path d="M5 28h9l4-10 8 20 4-10h13"/><g class="hi-ck" style="--k:0"><path d="M30 12l5 5 9-11" stroke="#fff"/></g>',
    }

import common
common.ICONS.update({"hair": '<path d="M6 13a6 6 0 0 1 12 0v1.5a6 6 0 0 1-12 0z"/><path d="M6.5 10.5C8 6.5 10 5.5 12 5.5s4 1 5.5 5"/><path d="M9 6.5l1 2M15 6.5l-1 2"/>'})
HUB = hub(G, [(110, 52, 'labs'), (110, 148, 'coach'), (450, 52, 'scale'), (450, 148, 'caps'), (230, 28, 'tube'), (330, 172, 'sleep'), (230, 172, 'hair'), (330, 28, 'pause')])
slots = {"{{HERO}}": hero_swim(), "{{MECH}}": mech(), "{{STAGES}}": stages(), "{{RECOVERY}}": recovery(), "{{BASELINE}}": baseline(),
         "{{OPTIONS}}": options(), "{{REGIONS}}": regions(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB, "{{FAQMOTIF}}": FAQMOTIF, "{{SPROUT}}": SPROUT}
slots.update(step_icons())
G.motion = [m for m in G.motion if m != '/*scan-meta*/']
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Testosterone therapy and male fertility: effects on sperm production, recovery and options",
      "TRT and fertility", "Does testosterone therapy affect fertility, and what are the options?", slots, G)
