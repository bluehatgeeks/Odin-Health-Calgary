"""Build /workspace/pages/testosterone-calculator/page.html (self-contained; paste into a GHL custom-code element when approved).
Tool page: unit converter (ng/dL <-> nmol/L, pg/mL <-> pmol/L) + Vermeulen free-T calculator.
Edit page.body.html (markup), page.css (graphics + tool CSS), calc-core.js (math, shared with test-calc.js), calc-ui.js (tool behaviour),
this file (copy, FAQ, SVG generators, no-JS default results); then: python3 build.py"""
import sys, os, math, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "testosterone-calculator"
TITLE = "ISSAM Calculator: Free and Bioavailable Testosterone"  # calc1027: brand suffix dropped ('| Odin Health Lab' = 70 chars / ~623px, truncates); was issam1026 '... | Odin Labs', before that 'Testosterone Calculator: Free T and Units | Odin Health Lab'
DESC = "Free ISSAM calculator: free and bioavailable testosterone from total T, SHBG and albumin (Vermeulen), plus a testosterone ng/dL to nmol/L converter."
OG_ALT = "Odin Health Lab testosterone calculator: ng/dL to nmol/L converter and free testosterone calculator"
assert len(TITLE) <= 65 and 140 <= len(DESC) <= 155, (len(TITLE), len(DESC))

common.ICONS.update({
 "calc": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8"/><path d="M8 12h.01M12 12h.01M16 12h.01M8 16h.01M12 16h.01M16 16h.01"/>',
 "clamp": '<path d="M6 6v6a6 6 0 0 0 12 0V6"/><circle cx="12" cy="12" r="2.4"/>',
 "swap": '<path d="M4 8h14l-3-3"/><path d="M20 16H6l3 3"/>',
 "coin": '<circle cx="12" cy="12" r="9"/><path d="M14.5 9.5c-.5-1-1.5-1.5-2.5-1.5-1.4 0-2.5.8-2.5 2s1 1.6 2.5 2 2.5.8 2.5 2-1.1 2-2.5 2c-1 0-2-.5-2.5-1.5M12 6.5V8M12 16v1.5"/>',
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
})

FAQ = [
 ("How do I convert testosterone from ng/dL to nmol/L?",
  "Divide ng/dL by 28.84. To go the other way, multiply nmol/L by 28.84. The factor comes from the molecular weight of testosterone, 288.4 grams per mole (PubChem). For example, 300 ng/dL is about 10.4 nmol/L, 500 ng/dL is about 17.3 nmol/L, and 15 nmol/L is about 433 ng/dL. For free testosterone, multiply pg/mL by 3.467 to get pmol/L, so 64 pg/mL is about 222 pmol/L, which the Endocrine Society rounds to 220."),
 ("What is a normal testosterone level in nmol/L in Canada?",
  "Each lab sets its own range. Alberta Precision Laboratories lists 8.0 to 35.0 nmol/L for men 18 and over, and the LifeLabs reference laboratory in British Columbia lists 8.4 to 28.8 nmol/L for men over 18. The Endocrine Society harmonized range for healthy, non-obese men aged 19 to 39 is 9.2 to 31.8 nmol/L (264 to 916 ng/dL), and the Canadian Urological Association treats a total T below 10 nmol/L as a reasonable threshold for low T, alongside symptoms. Compare your result with the range printed on your own report first."),
 ("How is free testosterone calculated?",
  "Most labs calculate it from total testosterone, SHBG and albumin with the Vermeulen equation (1999), which matched equilibrium dialysis closely in the original study. The equation uses fixed binding strengths for SHBG and albumin and solves for the unbound part. In the worked example published with the ISSAM calculator, total T 10 nmol/L, SHBG 40 nmol/L and albumin 4.3 g/dL give a free T of about 174 pmol/L, 1.74 percent of the total. Albumin of 4.3 g/dL (43 g/L) is the default when no albumin result is available."),
 ("What is a normal free testosterone level in pmol/L?",
  "There is no single harmonized range: the Endocrine Society notes that labs set their own limits and results depend on the method. The European Male Ageing Study (New England Journal of Medicine, 2010) used a free T below 220 pmol/L (64 pg/mL), with total T below 11 nmol/L and at least three sexual symptoms, to define late-onset hypogonadism. The LifeLabs reference laboratory in British Columbia lists a calculated free T range of 115 to 577 pmol/L for men. Check the unit and the method on your report before you compare."),
 ("Why do Canadian and US labs use different testosterone units?",
  "Canada moved health care lab reporting to SI units, which count molecules in moles per litre, in the early 1980s, so total testosterone is reported in nmol/L and free T in pmol/L. The United States kept conventional mass units, so its reports show ng/dL and pg/mL. It is the same hormone measured with a different ruler: 1 nmol/L equals 28.84 ng/dL. We line up results from both countries in one unit when we review your labs with you."),
 ("How do I read free testosterone on a LifeLabs report?",
  "LifeLabs reports free testosterone in pmol/L as a calculated value: total testosterone and SHBG are measured by immunoassay, and free and bioavailable testosterone are calculated from those results. The LifeLabs reference laboratory in British Columbia lists 115 to 577 pmol/L for calculated free T in men, and 8.4 to 28.8 nmol/L for total testosterone in men over 18. To check the number, enter the total T, SHBG and albumin from your report in the free testosterone calculator on this page. If your report has no albumin, the calculator uses 43 g/L."),
 ("Dynacare testosterone results: what do the units and ranges mean?",
  "Dynacare reports total testosterone in nmol/L and free testosterone in pmol/L. Its Ontario test directory lists 7.6 to 31.4 nmol/L for total testosterone in males 15 and over. Free T is calculated with the Vermeulen equation, which Dynacare adopted in 2014 in place of a direct analog test, and the male ranges are 160 to 699 pmol/L at ages 18 to 49 and 155 to 558 pmol/L at 50 and over. Check which age band your report printed before you compare."),
 ("What are the Alberta Precision Laboratories (APL) testosterone ranges in Alberta?",
  "Alberta Precision Laboratories, the public lab system in Alberta, lists 8.0 to 35.0 nmol/L for total testosterone and 175 to 700 pmol/L for calculated free testosterone in males 18 and over. APL calculates free T from total testosterone, SHBG and albumin. Its test directory notes that testosterone is highest in the morning, with values up to 25 percent lower later in the day, and suggests collecting between 07:00 and 10:00."),
 ("How does Odin Health Lab work with my doctor?",
  'Odin Health Lab is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We work alongside your own doctor: we go through your symptoms and lab results with you, put results from Canadian and US labs into one unit, check how your free T was measured or calculated, help you prepare questions for your next appointment, build your nutrition, training, sleep and stress plan, and track your progress with follow-up check-ins and repeat labs. We can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()
F28, P3 = 28.84, 3.467

def txt(x, y, s, size=13, fill='#fff', op=0.85, anchor='middle', extra=''):
    a = '' if anchor == 'middle' else ' text-anchor="%s"' % anchor  # middle is inherited from .mg-svg (page.css)
    return '<text x="%s" y="%s" font-size="%s" fill="%s" fill-opacity="%s"%s%s>%s</text>' % (f(x), f(y), size, fill, op, a, extra, s)

def clamp(x, y, cls='', k=0, sc=1.0, col=LIME):
    return ('<g transform="translate(%s %s) scale(%s)"><g class="%s" style="--k:%d"><path d="M-17 -16V0a17 17 0 0 0 34 0V-16" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>'
            '<circle cx="0" cy="-1" r="7.5" fill="#fff"/></g></g>') % (f(x), f(y), sc, cls, k, col)

def albumin(x, y, cls='', k=0, dot=True):
    return ('<g transform="translate(%s %s)"><g class="%s" style="--k:%d"><ellipse rx="27" ry="18" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.7)" stroke-width="2" stroke-dasharray="4 4"/>'
            '%s</g></g>') % (f(x), f(y), cls, k, '<circle cx="8" cy="-4" r="7" fill="#fff" fill-opacity="0.9"/>' if dot else '')

def fx(x, d):
    return '{:,.{}f}'.format(x, d)

# ---------- Vermeulen (mirror of calc-core.js; test-calc.js checks both agree) ----------
def vermeulen(tt, shbg, alb):
    T, S, N = tt * 1e-9, shbg * 1e-9, 1 + 3.6e4 * alb / 69000
    a, b = N * 1e9, N + 1e9 * (S - T)
    ft = (-b + math.sqrt(b * b + 4 * a * T)) / (2 * a)
    return dict(pmol=ft * 1e12, pg=ft * 1e12 / P3, pct=100 * ft / T, bat=ft * N * 1e9, batNg=ft * N * 1e9 * F28, alb=(N - 1) * ft * 1e9)

def where(v, lo, hi):
    return 'below' if v < lo else ('above' if v > hi else 'inside')

def total_html(n):  # mirror of totalHTML() in calc-ui.js (no-JS default result)
    es, apl, ll = where(n, 9.2, 31.8), where(n, 8.0, 35.0), where(n, 8.4, 28.8)
    if apl == ll: labs = ('inside both' if apl == 'inside' else apl + ' both') + ' typical Canadian lab ranges (Alberta Precision Labs 8.0 to 35.0, LifeLabs 8.4 to 28.8 nmol/L)'
    else: labs = apl + ' the Alberta Precision Labs range (8.0 to 35.0) and ' + ll + ' the LifeLabs range (8.4 to 28.8 nmol/L)'
    aua = 300 / F28
    lc = 'inside' if apl == 'inside' and ll == 'inside' else ('below' if 'below' in (apl, ll) else 'above')
    return ('<p class="rs-head"><b>%s nmol/L = %s ng/dL</b></p><ul class="rs-list">' % (fx(n, 1), fx(n * F28, 0)) +
            '<li class="rs-%s">%s the Endocrine Society harmonized range (9.2 to 31.8 nmol/L, 264 to 916 ng/dL)</li>' % (es, es.capitalize()) +
            '<li class="rs-%s">%s the American Urological Association low-T cut-off (300 ng/dL, about 10.4 nmol/L)</li>' % (('below', 'Under') if n < aua else ('inside', 'At or above')) +
            '<li class="rs-%s">%s the Canadian Urological Association threshold (10 nmol/L)</li>' % (('below', 'Under') if n < 10 else ('inside', 'At or above')) +
            '<li class="rs-%s">%s</li></ul>' % (lc, labs[0].upper() + labs[1:]))

def free_html(p):
    ll = where(p, 115, 577)
    return ('<li class="rs-%s">%s the 220 pmol/L (64 pg/mL) free T cut-off used by the European Male Ageing Study</li>' % (('below', 'Below') if p < 220 else ('inside', 'At or above')) +
            '<li class="rs-%s">%s the LifeLabs calculated free T range for men (115 to 577 pmol/L)</li>' % (ll, ll.capitalize()))

def fc_html(n, s, a):
    r = vermeulen(n, s, a)
    return ('<div class="fc-big"><span class="fc-k">Free testosterone</span><span class="fc-v"><b>%s</b> pmol/L</span><span class="fc-v2">%s pg/mL</span></div>' % (fx(r['pmol'], 0), fx(r['pg'], 1)) +
            '<dl class="fc-dl"><div><dt>Percent free</dt><dd>%s</dd></div><div><dt>Bioavailable T</dt><dd>%s nmol/L (%s ng/dL)</dd></div><div><dt>Total T used</dt><dd>%s nmol/L (%s ng/dL)</dd></div></dl>'
            % (fx(r['pct'], 2), fx(r['bat'], 1), fx(r['batNg'], 0), fx(n, 1), fx(n * F28, 0)) +
            '<ul class="rs-list">' + free_html(r['pmol']) + '</ul>'), r

def fc_bar(n, r):
    fr = max(r['pmol'] / 1e3 / n * 100, 3); al = r['alb'] / n * 100; sb = max(100 - fr - al, 0)
    return '<span class="b1" style="width:%.1f%%"></span><span class="b2" style="width:%.1f%%"></span><span class="b3" style="width:%.1f%%"></span>' % (sb, al, fr)

# ---------- hero: two readouts cycling through conversion pairs ----------
def hero():
    s = ['<defs><radialGradient id="tc-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.14"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="150" rx="225" ry="135" fill="url(#tc-g)"/>']
    for x, lab, col, cls in ((24, 'nmol/L', LIME, 'a'), (276, 'ng/dL', WHITE, 'b')):
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="40" width="180" height="134" rx="16" fill="#142e14" stroke="%s" stroke-width="2.4"/></g>' % (0.1 if cls == 'a' else 0.25, x, LIME if cls == 'a' else 'rgba(255,255,255,0.7)'))
        s.append(txt(x + 90, 68, lab, 14, col, 0.95))
        vals = ('10.4', '15.0', '20.0') if cls == 'a' else ('300', '433', '577')
        for k, v in enumerate(vals):
            s.append('<g class="hv-n hv-n%d%s">%s</g>' % (k, ' fx' if k else '', txt(x + 90, 122, v, 34, '#c4ff49' if cls == 'a' else '#fff', 0.97)))
        s.append('<rect x="%d" y="144" width="150" height="8" rx="4" fill="rgba(255,255,255,0.12)"/>' % (x + 15))
        s.append('<rect class="hv-bar" x="%d" y="144" width="150" height="8" rx="4" fill="%s"/>' % (x + 15, LIME if cls == 'a' else 'rgba(255,255,255,0.75)'))
    s.append('<g class="hv-chip"><rect x="208" y="92" width="64" height="30" rx="15" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/></g>')
    s.append(txt(240, 112, '&#215; 28.84', 12, '#c4ff49', 0.95))
    for i, (y, a, b, col) in enumerate(((80, 204, 276, LIME), (140, 276, 204, WHITE))):
        pd, pts = path(('M', a, y), ('L', b, y))
        s.append('<path d="%s" stroke="rgba(196,255,73,0.25)" stroke-width="2" stroke-dasharray="2 6"/>' % pd)
        s.append(dot('hv-p%d fx' % i, 5, col)); G.travel('hv-p%d' % i, pts, 8, 40, 3, delay='%ss' % f(-i * 1.5), rest=pts[0], rest_opacity=0, fade=4)
    s.append('<g class="pop t" style="--d:0.4"><rect x="24" y="196" width="432" height="62" rx="14" fill="rgba(255,255,255,0.04)" stroke="rgba(196,255,73,0.45)" stroke-width="1.6"/></g>')
    s.append(txt(44, 222, 'Free T', 12, '#fff', 0.7, 'start')); s.append(txt(44, 245, '100 pg/mL', 17, '#fff', 0.95, 'start'))
    s.append('<g class="hv-sw">%s</g>' % ico('swap', 240, 232, 22, LIME, 2))
    s.append(txt(436, 222, '&#215; 3.467', 12, '#c4ff49', 0.85, 'end')); s.append(txt(436, 245, '347 pmol/L', 17, '#c4ff49', 0.97, 'end'))
    s.append(txt(240, 296, 'Same result, two units', 13, '#fff', 0.85))
    return '\n'.join(s)

# ---------- meter inside the converter (pin moved by calc-ui.js) ----------
MX = lambda v: 70 + 460 * v / 40
def meter(n0):
    s = ['<path d="M70 52H530" stroke="rgba(255,255,255,0.35)" stroke-width="3" stroke-linecap="round"/>']
    s.append('<g class="mt-band"><rect x="%s" y="40" width="%s" height="24" rx="8" fill="#c4ff49" fill-opacity="0.22" stroke="#c4ff49" stroke-width="1.6"/></g>' % (f(MX(9.2)), f(MX(31.8) - MX(9.2))))
    s.append(txt((MX(9.2) + MX(31.8)) / 2 + 30, 56, 'Harmonized range', 11, '#fff', 0.8))
    s.append('<path d="M%s 34V72" stroke="#c4ff49" stroke-width="2" stroke-dasharray="4 3"/>' % f(MX(300 / F28)))
    for v in range(0, 41, 10):
        s.append('<path d="M%s 64V70" stroke="#fff" stroke-opacity="0.5" stroke-width="2"/>' % f(MX(v)))
        s.append(txt(MX(v), 90, str(v), 11, '#c4ff49', 0.9))
    for g in (300, 600, 900):
        s.append(txt(MX(g / F28), 112, str(g), 11, '#fff', 0.8))
    s.append(txt(8, 90, 'nmol/L', 11, '#c4ff49', 0.9, 'start')); s.append(txt(8, 112, 'ng/dL', 11, '#fff', 0.8, 'start'))
    x0 = 460 * min(n0, 40) / 40
    s.append('<g id="mt-pin" class="mt-pin" style="transform:translateX(%spx)"><path d="M70 26V74" stroke="#fff" stroke-width="2"/>'
             '<circle class="mt-ring fx" cx="70" cy="52" r="13" fill="none" stroke="#c4ff49" stroke-width="2"/><circle cx="70" cy="52" r="7" fill="#c4ff49" stroke="#0f240f" stroke-width="2"/>'
             '<text id="mt-val" x="70" y="18" font-size="13" fill="#fff">%s</text></g>' % (f(x0), fx(n0, 1)))
    return '\n'.join(s)

# ---------- ranges: three reference bars + cut-off zone ----------
RX = lambda v: 150 + 380 * v / 40
def ranges():
    s = [txt(10, 32, 'nmol/L', 11, '#c4ff49', 0.9, 'start'), '<path d="M150 40H530" stroke="rgba(255,255,255,0.35)" stroke-width="3" stroke-linecap="round"/>']
    for v in range(0, 41, 10):
        s.append('<path d="M%s 34V46" stroke="#fff" stroke-opacity="0.5" stroke-width="2"/>' % f(RX(v))); s.append(txt(RX(v), 26, str(v), 11, '#c4ff49', 0.9))
    s.append('<g class="rg-cz"><rect x="%s" y="48" width="%s" height="124" rx="4" fill="#c4ff49" fill-opacity="0.16"/></g>' % (f(RX(10)), f(RX(11) - RX(10))))
    rows = [('Endocrine Society', 9.2, 31.8, LIME, 'rgba(196,255,73,0.3)'), ('Alberta Precision', 8.0, 35.0, 'rgba(255,255,255,0.75)', 'rgba(255,255,255,0.1)'), ('LifeLabs (BC)', 8.4, 28.8, 'rgba(255,255,255,0.75)', 'rgba(255,255,255,0.1)')]
    for k, (lab, lo, hi, st, fl) in enumerate(rows):
        y = 70 + k * 40
        s.append(txt(10, y + 4, lab, 11, '#fff', 0.85, 'start'))
        s.append('<g class="rg-bar" style="--k:%d"><rect x="%s" y="%d" width="%s" height="18" rx="6" fill="%s" stroke="%s" stroke-width="1.6"/></g>' % (k, f(RX(lo)), y - 9, f(RX(hi) - RX(lo)), fl, st))
        s.append(txt(RX(hi) + 6, y + 4, '%s to %s' % (lo, hi), 11, '#c4ff49' if k == 0 else '#fff', 0.9, 'start'))
    s.append(txt(RX(10.5), 192, 'Low-T cut-offs: 10 to 11 nmol/L', 11, '#c4ff49', 0.95))
    s.append(txt(10, 236, 'ng/dL', 11, '#fff', 0.8, 'start')); s.append('<path d="M150 214H530" stroke="rgba(255,255,255,0.25)" stroke-width="2"/>')
    for g in (300, 600, 900):
        s.append('<path d="M%s 209V219" stroke="#fff" stroke-opacity="0.5" stroke-width="2"/>' % f(RX(g / F28))); s.append(txt(RX(g / F28), 236, str(g), 11, '#fff', 0.8))
    pd, pts = path(('M', 160, 40), ('L', 520, 40))
    s.append(dot('rg-d fx', 6, LIME, ring=True)); G.travel('rg-d', pts, 8, 80, 9, rest=pts[0], rest_opacity=0, fade=4, ease='ease-in-out')
    return '\n'.join(s)

# ---------- why units: Canadian vs US report ----------
def why():
    s = []
    cards = [(30, 'Canada', 'SI units', '15.0', 'nmol/L', LIME), (330, 'USA', 'Conventional units', '433', 'ng/dL', WHITE)]
    for k, (x, a, b, v, u, col) in enumerate(cards):
        s.append('<g class="wy-card" style="--k:%d"><rect x="%d" y="34" width="200" height="140" rx="14" fill="#142e14" stroke="%s" stroke-width="2"/></g>' % (k, x, LIME if k == 0 else 'rgba(255,255,255,0.65)'))
        s.append(txt(x + 18, 60, a, 14, '#c4ff49' if k == 0 else '#fff', 0.95, 'start')); s.append(txt(x + 182, 60, b, 11, '#fff', 0.7, 'end'))
        s.append(txt(x + 18, 86, 'Testosterone, total', 11, '#fff', 0.75, 'start'))
        s.append(txt(x + 18, 124, v, 30, '#c4ff49' if k == 0 else '#fff', 0.97, 'start')); s.append(txt(x + 182, 124, u, 14, '#fff', 0.85, 'end'))
        for j in range(2):
            s.append('<path d="M%d %dH%d" stroke="rgba(255,255,255,0.3)" stroke-width="4" stroke-linecap="round"/>' % (x + 18, 146 + j * 12, x + 150 - j * 40))
    s.append('<g class="wy-chip"><rect x="242" y="90" width="76" height="32" rx="16" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/></g>')
    s.append(txt(280, 111, '&#215; 28.84', 12, '#c4ff49', 0.95))
    for i, (y, a, b, col) in enumerate(((76, 232, 328, LIME), (138, 328, 232, WHITE))):
        pd, pts = path(('M', a, y), ('C', (a + b) / 2, y + (-14 if i == 0 else 14), (a + b) / 2, y + (-14 if i == 0 else 14), b, y), n=6)
        s.append('<path d="%s" stroke="rgba(196,255,73,0.22)" stroke-width="2" stroke-dasharray="2 6" fill="none"/>' % pd)
        s.append(dot('wy-p%d fx' % i, 5, col)); G.travel('wy-p%d' % i, pts, 6, 44, 6, delay='%ss' % f(-i * 3), rest=pts[0], rest_opacity=0, fade=4)
    s.append(txt(280, 204, 'Same hormone, different ruler: 288.4 g per mole', 12, '#fff', 0.8))
    return '\n'.join(s)

# ---------- how: three pools with hops between albumin and free ----------
def how():
    s = [txt(100, 30, 'SHBG: tight', 12, '#c4ff49', 0.95), txt(280, 30, 'Free', 12, '#c4ff49', 0.95), txt(450, 30, 'Albumin: loose', 12, '#fff', 0.85)]
    for k, (x, y) in enumerate(((70, 90), (130, 120), (80, 170), (140, 186))):
        s.append(clamp(x, y, 'hw-cl', k, 0.9))
    for k, (x, y) in enumerate(((420, 86), (480, 130), (420, 176))):
        s.append(albumin(x, y, 'hw-al', k, dot=(k != 1)))
    s.append('<g class="hw-fr"><circle cx="270" cy="110" r="7" fill="#c4ff49"/><circle cx="296" cy="146" r="7" fill="#c4ff49"/><circle class="hw-ring fx" cx="270" cy="110" r="12" fill="none" stroke="#c4ff49" stroke-width="2"/></g>')
    s.append(dr('M190 118H236M236 118l-7-5M236 118l-7 5', 0.3, 0.8, 'rgba(196,255,73,0.55)', 2))
    s.append(dr('M236 136H190M190 136l7-5M190 136l7 5', 0.4, 0.8, 'rgba(196,255,73,0.25)', 2))
    s.append(dr('M326 118H384M384 118l-7-5M384 118l-7 5', 0.5, 0.8, 'rgba(255,255,255,0.6)', 2))
    s.append(dr('M384 136H326M326 136l7-5M326 136l7 5', 0.6, 0.8, 'rgba(255,255,255,0.6)', 2))
    loops = [((300, 120), (360, 90), (420, 100), (470, 126)), ((470, 134), (420, 170), (350, 170), (300, 140))]
    for i, (a, b, c, d) in enumerate(loops):
        pd, pts = path(('M', a[0], a[1]), ('C', b[0], b[1], c[0], c[1], d[0], d[1]), n=7)
        s.append(dot('hw-h%d fx' % i, 6, WHITE)); G.travel('hw-h%d' % i, pts, 10 + i * 45, 40 + i * 45, 6, rest=pts[0], rest_opacity=0, fade=3)
    s.append(txt(100, 222, 'K = 1,000,000,000 L/mol', 11, '#fff', 0.75)); s.append(txt(450, 222, 'K = 36,000 L/mol', 11, '#fff', 0.75))
    s.append(txt(280, 222, 'Free + albumin = bioavailable', 11, '#c4ff49', 0.9))
    return '\n'.join(s)

# ---------- help: two reports -> telehealth review -> one trend + plan ----------
def help_fig():
    s = []
    for k, (y, a, b, col) in enumerate(((30, 'Canada', '15.0 nmol/L', LIME), (120, 'USA', '433 ng/dL', WHITE))):
        s.append('<g class="pop t" style="--d:%s"><rect x="20" y="%d" width="150" height="70" rx="12" fill="#142e14" stroke="%s" stroke-width="2"/></g>' % (0.1 + k * 0.15, y, LIME if k == 0 else 'rgba(255,255,255,0.6)'))
        s.append(txt(36, y + 26, a, 12, '#c4ff49' if k == 0 else '#fff', 0.95, 'start')); s.append(txt(36, y + 52, b, 15, '#fff', 0.95, 'start'))
        pd, pts = path(('M', 170, y + 35), ('C', 210, y + 35, 220, 100, 252, 100), n=6)
        s.append('<path d="%s" stroke="rgba(196,255,73,0.22)" stroke-width="2" stroke-dasharray="2 6" fill="none"/>' % pd)
        s.append(dot('hp-in%d fx' % k, 5, col)); G.travel('hp-in%d' % k, pts, 6 + k * 20, 34 + k * 20, 7, rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(280, 100, 28, 'coach', 0.3, LIME, fill='#173617', isz=28)); s.append(txt(280, 150, 'Telehealth review', 12, '#fff', 0.85))
    s.append('<path d="M308 100H372" stroke="rgba(196,255,73,0.22)" stroke-width="2" stroke-dasharray="2 6"/>')
    s.append('<g class="pop t" style="--d:0.45"><rect x="376" y="24" width="164" height="120" rx="12" fill="rgba(255,255,255,0.04)" stroke="rgba(196,255,73,0.45)" stroke-width="1.6"/></g>')
    s.append('<path d="M392 126H526M392 126V40" stroke="rgba(255,255,255,0.35)" stroke-width="1.6"/>')
    s.append(dr('M396 112L426 104L456 96L486 82L520 70', 0.6, 1.4, LIME, 3))
    s.append(txt(458, 162, 'One unit, one trend', 12, '#c4ff49', 0.95))
    for k, ic in enumerate(('food', 'train', 'sleep', 'stress')):
        x = 398 + k * 40
        s.append('<g class="hp-i" style="--k:%d"><circle cx="%d" cy="200" r="16" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/>%s</g>' % (k, x, ico(ic, x, 200, 17, LIME, 1.8)))
    s.append(txt(372, 205, 'Your written plan', 12, '#fff', 0.8, 'end'))
    return '\n'.join(s)

def final():
    s = ['<defs><radialGradient id="fn-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.3"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><circle cx="180" cy="140" r="96" fill="url(#fn-g)"/>']
    cx, cy, r = 180, 160, 84
    s.append('<path d="M%d %dA%d %d 0 0 1 %d %d" stroke="rgba(196,255,73,0.45)" stroke-width="8" stroke-linecap="round" fill="none"/>' % (cx - r, cy, r, r, cx + r, cy))
    for v in range(0, 41, 10):
        a = math.pi + v / 40 * math.pi
        s.append('<path d="M%s %sL%s %s" stroke="#fff" stroke-opacity="0.6" stroke-width="2" stroke-linecap="round"/>' % (f(cx + (r - 14) * math.cos(a)), f(cy + (r - 14) * math.sin(a)), f(cx + (r - 6) * math.cos(a)), f(cy + (r - 6) * math.sin(a))))
    s.append('<g class="fn-nd"><path d="M%d %dV%d" stroke="#c4ff49" stroke-width="4" stroke-linecap="round"/></g>' % (cx, cy, cy - r + 22))
    s.append('<circle cx="%d" cy="%d" r="8" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/>' % (cx, cy))
    s.append(txt(cx, cy + 30, 'nmol/L and ng/dL', 11, '#fff', 0.75))
    s.append(node(312, 60, 20, 'check', 0.4, LIME, fill='#142e14', isz=22))
    s.append(node(48, 60, 20, 'calc', 0.3, WHITE, isz=22))
    return '\n'.join(s)

# ---------- lab1028: Canadian lab report -> calculator ----------
LR_ROWS = (('Testosterone, total', '15.0', 'nmol/L'), ('SHBG', '30', 'nmol/L'), ('Albumin', '43', 'g/L'), ('Free T, calculated', '326', 'pmol/L'))
def labrep():
    s = ['<g class="pop t" style="--d:0.1"><rect x="24" y="18" width="270" height="206" rx="14" fill="#142e14" stroke="rgba(255,255,255,0.65)" stroke-width="2"/></g>']
    s.append(txt(44, 44, 'Lab report', 13, '#c4ff49', 0.95, 'start'))
    s.append('<path d="M200 40H274M226 50H274" stroke="rgba(255,255,255,0.25)" stroke-width="4" stroke-linecap="round"/>')
    s.append(txt(44, 72, 'Test', 10, '#fff', 0.6, 'start')); s.append(txt(206, 72, 'Result', 10, '#fff', 0.6, 'end')); s.append(txt(252, 72, 'Units', 10, '#fff', 0.6))
    s.append('<g class="lr-hl"><rect x="32" y="82" width="254" height="28" rx="8" fill="#c4ff49" fill-opacity="0.13" stroke="#c4ff49" stroke-opacity="0.5" stroke-width="1.4"/></g>')
    for k, (a, v, u) in enumerate(LR_ROWS):
        y = 101 + k * 32
        s.append(txt(44, y, a, 12, '#fff', 0.88, 'start')); s.append(txt(206, y, v, 14, '#fff', 0.97, 'end'))
        s.append('<g class="lr-u" style="--k:%d"><rect x="222" y="%d" width="60" height="22" rx="11" fill="#0f240f" stroke="#c4ff49" stroke-width="1.6"/></g>' % (k, y - 15))
        s.append(txt(252, y, u, 11, '#c4ff49', 0.97))
    s.append('<path d="M300 124H366" stroke="rgba(196,255,73,0.22)" stroke-width="2" stroke-dasharray="2 6"/>')
    s.append(dr('M300 124H364M364 124l-8-6M364 124l-8 6', 0.45, 0.8, LIME, 2.4))
    s.append('<g class="pop t" style="--d:0.3"><rect x="376" y="30" width="164" height="184" rx="14" fill="rgba(255,255,255,0.04)" stroke="rgba(196,255,73,0.45)" stroke-width="1.6"/></g>')
    s.append(ico('calc', 398, 54, 18, LIME, 1.8)); s.append(txt(416, 59, 'Calculator', 12, '#fff', 0.9, 'start'))
    for k, (lab, v) in enumerate((('Total T', '15.0'), ('SHBG', '30'), ('Albumin', '43'))):
        y = 76 + k * 30
        s.append('<rect x="392" y="%d" width="132" height="22" rx="6" fill="#0f240f" stroke="rgba(255,255,255,0.3)" stroke-width="1.4"/>' % y)
        s.append(txt(400, y + 15, lab, 10, '#fff', 0.7, 'start')); s.append(txt(516, y + 15, v, 12, '#fff', 0.95, 'end'))
        pd, pts = path(('M', 212, 101 + k * 32), ('C', 320, 101 + k * 32, 330, y + 11, 392, y + 11), n=8)
        s.append(dot('lr-p%d fx' % k, 5, LIME if k == 0 else WHITE)); G.travel('lr-p%d' % k, pts, 4, 16, 12, delay='%ss' % f(k * 3), rest=pts[0], rest_opacity=0, fade=2, ease='ease-in-out')
    s.append('<g class="lr-out"><rect x="392" y="170" width="132" height="32" rx="8" fill="#173617" stroke="#c4ff49" stroke-width="2"/></g>')
    s.append(txt(400, 190, 'Free T', 10, '#fff', 0.75, 'start')); s.append(txt(516, 191, '326 pmol/L', 13, '#c4ff49', 0.97, 'end'))
    s.append(txt(280, 246, 'Unit, method, then the range printed by your lab', 12, '#fff', 0.8))
    return '\n'.join(s)

FAQMOTIF = '''<g class="fq-cl"><rect x="12" y="22" width="34" height="46" rx="6" stroke="#c4ff49" stroke-width="3.4"/><path d="M19 32h20" stroke="#c4ff49" stroke-width="3" stroke-linecap="round"/><g class="fq-k" style="--k:0"><circle cx="21" cy="46" r="2.6" fill="#fff"/></g><g class="fq-k" style="--k:1"><circle cx="29" cy="46" r="2.6" fill="#fff"/></g><g class="fq-k" style="--k:2"><circle cx="37" cy="56" r="2.6" fill="#fff"/></g></g>
<path class="dr" pathLength="1" style="--d:0.25;--dur:1.1s" d="M70 36c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82" cy="64" r="3" fill="#fff"/>
<g class="fq-fr" style="--k:0"><circle cx="104" cy="22" r="5" fill="#c4ff49"/></g><g class="fq-fr" style="--k:1"><circle cx="56" cy="16" r="4" fill="#c4ff49"/></g>'''

def hub_nodes():
    return [(90, 52, 'clamp'), (470, 52, 'tube'), (90, 150, 'coin'), (470, 150, 'compass')]

N0, S0, A0 = 15.0, 30.0, 43.0
fc_out, r0 = fc_html(N0, S0, A0)
calcjs = open(os.path.join(HERE, "calc-core.js"), encoding="utf-8").read().strip() + "\n" + open(os.path.join(HERE, "calc-ui.js"), encoding="utf-8").read().strip()
HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{METER}}": meter(N0), "{{CVOUT}}": total_html(N0),
         "{{CVOUTF}}": '<p class="rs-head"><b>%s pmol/L = %s pg/mL</b></p><ul class="rs-list">%s</ul>' % (fx(300, 0), fx(300 / P3, 1), free_html(300)),
         "{{FCOUT}}": fc_out, "{{FCBAR}}": fc_bar(N0, r0), "{{RANGES}}": ranges(), "{{LABREP}}": labrep(), "{{WHY}}": why(), "{{HOW}}": how(), "{{HELP}}": help_fig(),
         "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB, "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final(), "{{CALCJS}}": calcjs}
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Testosterone unit conversion (ng/dL, nmol/L, pg/mL, pmol/L) and calculated free testosterone",
      "Testosterone calculator", "ISSAM calculator: free and bioavailable testosterone, plus ng/dL to nmol/L conversion", slots, G, published="2026-10-18", modified="2026-10-28")

# ---- add WebApplication JSON-LD (the tool itself) next to the Article node ----
p = os.path.join(HERE, "page.html")
full = open(p, encoding="utf-8").read()
m = re.search(r'(<script type="application/ld\+json">\n)([\s\S]*?)(\n</script>)', full)
ld = json.loads(m.group(2).replace("<\\/", "</"))
url = SITE + "/" + SLUG
ld["@graph"].insert(4, {"@type": "WebApplication", "@id": url + "#app", "name": "Testosterone unit converter and free testosterone calculator", "url": url,
    "description": "Converts total testosterone between ng/dL and nmol/L and free testosterone between pg/mL and pmol/L as you type, and calculates free and bioavailable testosterone from total testosterone, SHBG and albumin with the Vermeulen equation.",
    "applicationCategory": "HealthApplication", "operatingSystem": "Any", "browserRequirements": "Requires JavaScript", "inLanguage": "en", "isAccessibleForFree": True,
    "offers": {"@type": "Offer", "price": "0", "priceCurrency": "CAD"}, "publisher": {"@id": SITE + "/#organization"}, "isPartOf": {"@id": url + "#webpage"},
    "featureList": ["Total testosterone ng/dL to nmol/L and nmol/L to ng/dL", "Free testosterone pg/mL to pmol/L and pmol/L to pg/mL",
                    "Calculated free testosterone, percent free and bioavailable testosterone (Vermeulen 1999)", "Plain-words comparison with Endocrine Society, AUA, CUA and Canadian lab reference ranges"]})
ldj = json.dumps(ld, ensure_ascii=False, indent=2).replace("</", "<\\/")
full = full[:m.start(2)] + ldj + full[m.end(2):]
open(p, "w", encoding="utf-8").write(full)

# ---- calc1027: no in-body <title> on this page (the GHL SEO panel sets the one <head> title; og/twitter/meta desc/canonical stay in-body) ----
full, ntitle = re.subn(r'<title>[^<]*</title>\n', '', full, count=1)
assert ntitle == 1 and '<title' not in full, ntitle

# ---- minify for HighLevel (keeps page.full.html): strip CSS comments, line indentation and blank lines outside <script> ----
open(os.path.join(HERE, "page.full.html"), "w", encoding="utf-8").write(full)
def mini(src):
    parts = re.split(r'(<script\b[\s\S]*?</script>)', src)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part); continue
        def css(mm):
            c = re.sub(r'/\*[\s\S]*?\*/', '', mm.group(0))
            c = re.sub(r'\n\s+', '\n', c); c = re.sub(r'\n{2,}', '\n', c)
            return c
        part = re.sub(r'<style\b[\s\S]*?</style>', css, part)
        part = re.sub(r'\n[ \t]+', '\n', part); part = re.sub(r'\n{2,}', '\n', part)
        out.append(part)
    return ''.join(out)
mm = mini(full)
used = set(re.findall(r'#pi-([\w-]+)', mm))
mm = re.sub(r'<symbol id="pi-([\w-]+)" viewBox="0 0 24 24">[\s\S]*?</symbol>', lambda x: x.group(0) if x.group(1) in used else '', mm)
def tight(x):
    c = x.group(0)
    c = re.sub(r'\s*([{};])\s*', r'\1', c); c = re.sub(r':\s+', ':', c); c = re.sub(r',\s+', ',', c)
    return c
mm = re.sub(r'(?<=<style>)[\s\S]*?(?=</style>)', tight, mm)
# compact the page's own tool script (indentation only; code untouched)
mm = re.sub(r'(<script>\n/\*CORE\*/[\s\S]*?</script>)', lambda x: re.sub(r'\n[ \t]+', '\n', x.group(1)), mm)
open(p, "w", encoding="utf-8").write(mm)
print("minified", len(full.encode()), "->", len(mm.encode()), "bytes")
