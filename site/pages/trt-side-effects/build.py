"""Build /workspace/pages/trt-side-effects/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match. build() output is minified at the end (HighLevel save limit).
The shared templates already carry the Safari-motion fix (@media all + var reduce = false); /workspace/safari-fix/apply_fix.py is run on the output as a guard."""
import sys, os, math, re, subprocess, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "trt-side-effects"
TITLE = "TRT Side Effects: Full List and Lab Tests | Odin Health Labs"
DESC = "TRT side effects in men: hematocrit, acne, PSA, estradiol, fertility, sleep apnea, fluid retention and heart risk, with the lab checks and limits used."
OG_ALT = "Odin Health Labs: TRT side effects in men, the full list with hematocrit, PSA, estradiol, fertility and heart risk, and the lab checks and limits used"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 155, (len(TITLE), len(DESC))

common.ICONS.update({
 "coin": '<circle cx="12" cy="12" r="9"/><path d="M14.5 9.5c-.5-1-1.5-1.5-2.5-1.5-1.4 0-2.5.8-2.5 2s1 1.6 2.5 2 2.5.8 2.5 2-1.1 2-2.5 2c-1 0-2-.5-2.5-1.5M12 6.5V8M12 16v1.5"/>',  # same as /trt-cost-canada-vs-usa (related_trtcost card + hub node)
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "swap": '<path d="M4 8h14l-3-3"/><path d="M20 16H6l3 3"/>',
 "up": '<path d="M12 19V5"/><path d="M6 11l6-6 6 6"/>',
 "down": '<path d="M12 5v14"/><path d="M6 13l6 6 6-6"/>',
 "sperm": '<circle cx="8" cy="15" r="3.5"/><path d="M10.6 12.6c1.6-1.8 2.6-4.6 5.2-5.4 2.2-.7 3.4.6 5.2-.8"/>',
 "hair": '<path d="M6 13a6 6 0 0 1 12 0v1.5a6 6 0 0 1-12 0z"/><path d="M6.5 10.5C8 6.5 10 5.5 12 5.5s4 1 5.5 5"/><path d="M9 6.5l1 2M15 6.5l-1 2"/>',
})

FAQ = [
 ("What are the most common side effects of TRT?",
  "A rise in red blood cells (hematocrit) is the most frequent side effect in testosterone trials, according to the Endocrine Society&rsquo;s 2018 guideline. Acne and oily skin, breast tenderness, a small rise in PSA and lower sperm production are also linked to testosterone. Breast enlargement, male pattern balding and new or worse sleep apnea are uncommon. Each form adds its own, such as injection-site pain, skin irritation from patches or gel rubbing off onto a partner. Regular labs catch most of these early, and we track them with you."),
 ("Does TRT raise hematocrit, and when is it too high?",
  "Yes. Testosterone raises hemoglobin and hematocrit, more in older men and at higher doses. The Endocrine Society advises checking hematocrit before starting, at three to six months and then yearly, taking extra care if it starts above 48 percent, and pausing treatment if it passes 54 percent until it settles, then restarting at a lower dose. In a 2022 study of men on testosterone, those whose hematocrit reached 52 percent or more had more heart attacks, strokes and blood clots in the first year. We follow your hematocrit with you at every check-in."),
 ("Does TRT shrink your testicles or affect fertility?",
  'It can. Testosterone from outside the body switches off the LH and FSH signals that drive the testes, so they make less of their own testosterone and fewer sperm. In a 1981 study, testicular volume fell by about 16 to 19 percent after four months of injections and returned to normal after they stopped. In a World Health Organization trial, 65 percent of healthy men on weekly injections had no sperm by six months. If you may want children, plan that before you start. See our <a href="%s/trt-and-fertility">TRT and fertility guide</a>.' % SITE),
 ("Does TRT cause hair loss or acne?",
  "Acne and oily skin have a clear link with testosterone. Hair loss is less certain: the Endocrine Society lists male pattern balding as an uncommon side effect with weak evidence, mostly in men with a family tendency toward it. If acne or thinning shows up, your levels, the dose, its timing and the form you use are worth reviewing, and we go through them with you."),
 ("Is TRT bad for your heart or prostate?",
  "In the TRAVERSE trial of 5,246 men aged 45 to 80 with heart disease or high heart risk, a heart attack, stroke or cardiovascular death occurred in 7.0 percent of men on testosterone gel and 7.3 percent on placebo. Atrial fibrillation, acute kidney injury and pulmonary embolism were more common with testosterone, and the FDA added a blood pressure warning in 2025. High-grade prostate cancer occurred in 0.19 versus 0.12 percent, not a significant difference. Testosterone does raise PSA a little and can speed up an existing prostate cancer, so PSA is checked before starting and during the first year."),
 ("What labs are checked on TRT, and how often?",
  "The Endocrine Society&rsquo;s 2018 plan checks hematocrit before starting, at three to six months and then yearly, and testosterone at three to six months, aiming for the middle of the normal range; with cypionate or enanthate injections, the level is measured midway between doses and the dose adjusted if it is above 600 or below 350 ng/dL. Men 55 to 69, or 40 to 69 at higher risk, who choose prostate monitoring have PSA checked before starting and at three to twelve months, with a closer prostate work-up if PSA rises more than 1.4 ng/mL within the first year or is confirmed above 4.0. The Canadian Urological Association&rsquo;s 2021 guideline monitors at baseline, three months, six months and then yearly. We add estradiol, lipids and blood pressure, and go through every result with you."),
 ("Can TRT cause water retention, swelling or mood swings?",
  "It can. The Endocrine Society&rsquo;s 2018 guideline notes that testosterone can cause fluid retention and swelling (edema) and can make swelling from heart failure or other conditions worse, and in 2025 the FDA added a class-wide warning about blood pressure increases. Swings in mood or libido are listed as a side effect of injections, where levels peak after each dose and fall before the next. Steadier dosing, a different form and checking levels midway between injections help, and we track weight, swelling and blood pressure with you at check-ins."),
 ("How does Odin Health Labs work with my doctor?",
  'Odin Health Labs is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We work alongside your own doctor: we go through your symptoms, history and lab results with you, help you prepare questions about TRT side effects and monitoring, build your nutrition, training, sleep and stress plan, and track hematocrit, PSA, estradiol, lipids and blood pressure with you at follow-up check-ins, using the Endocrine Society&rsquo;s monitoring plan as the checklist. We can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

def txt(x, y, s, size=13, fill='#fff', op=0.85, anchor='middle', extra=''):
    a = '' if anchor == 'middle' else ' text-anchor="%s"' % anchor  # middle is inherited from .mg-svg (page.css)
    return '<text x="%s" y="%s" font-size="%s" fill="%s" fill-opacity="%s"%s%s>%s</text>' % (f(x), f(y), size, fill, op, a, extra, s)

def chip(x, y, w, h, cls, k, lines, hot=False, size=11.5):
    s = '<g class="%s" style="--k:%d"><rect x="%s" y="%s" width="%s" height="%s" rx="11" fill="%s" stroke="%s" stroke-width="1.6"/>' % (
        cls, k, f(x), f(y), f(w), f(h), 'rgba(196,255,73,0.1)' if hot else 'rgba(255,255,255,0.04)', '#c4ff49' if hot else 'rgba(255,255,255,0.35)')
    n = len(lines); y0 = y + h / 2 - (n - 1) * 8 + 4
    for i, l in enumerate(lines):
        s += txt(x + w / 2, y0 + i * 16, l, size, '#c4ff49' if (hot and i == 0) else '#fff', 0.92)
    return s + '</g>'

# ---------- hero: a radar sweep lights each thing that gets checked on TRT ----------
def hero():
    cx, cy = 240, 160
    s = ['<defs><radialGradient id="se-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.14"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="225" ry="140" fill="url(#se-g)"/>']
    for r in (58, 98):
        s.append('<circle cx="240" cy="160" r="%d" fill="none" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="3 7"/>' % r)
    s.append('<g class="hr-sw"><path d="M240 160L150.9 70.9A126 126 0 0 1 240 34Z" fill="#c4ff49" fill-opacity="0.13"/><path d="M240 160V34" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/></g>')
    labs = [('Hematocrit', 'drop'), ('Skin and acne', 'mood'), ('PSA', 'gland'), ('Sperm count', 'sperm'), ('Estradiol', 'swap'), ('Blood pressure', 'heart'), ('Sleep apnea', 'sleep')]
    for i, (lab, ic) in enumerate(labs):
        a = math.radians(-90 + i * 360 / 7)
        x, y = cx + 178 * math.cos(a), cy + 104 * math.sin(a)
        ly = y - 30 if y < cy - 5 else y + 38
        s.append('<g class="hr-s" style="--k:%d"><circle cx="%s" cy="%s" r="22" fill="#0f240f" stroke="%s" stroke-width="2.4"/>%s</g>%s'
                 % (i, f(x), f(y), LIME if i % 2 == 0 else 'rgba(255,255,255,0.75)', ico(ic, x, y, 22, LIME if i % 2 == 0 else WHITE, 1.8), txt(x, ly, lab, 12, '#fff', 0.88)))
    s.append(node(240, 160, 32, 'tube', 0.1, LIME, fill='#142e14', isz=32))
    return '\n'.join(s)

# ---------- full list: a clipboard checklist, a highlight bar steps down the rows and each tick pops as it passes ----------
def checklist():
    s = ['<path d="M78 125H150" stroke="rgba(255,255,255,0.16)" stroke-width="2.4" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>']
    s.append('<g class="pop t" style="--d:0.1"><rect x="150" y="18" width="270" height="220" rx="16" fill="#142e14" stroke="rgba(255,255,255,0.5)" stroke-width="2.4"/><rect x="245" y="8" width="80" height="22" rx="8" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/></g>')
    rows = [('Hematocrit', '54 percent'), ('PSA rise', '+1.4 ng/mL'), ('PSA level', '4.0 ng/mL'), ('Testosterone', '350 to 600'), ('Estradiol', 'if breast signs'), ('Blood pressure', 'each check-in')]
    s.append('<g class="fl-hl"><rect x="162" y="44" width="246" height="28" rx="8" fill="#c4ff49" fill-opacity="0.14"/></g>')
    for k, (lab, lim) in enumerate(rows):
        y = 58 + k * 30
        s.append('<rect x="170" y="%d" width="16" height="16" rx="4" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="1.8"/>' % (y - 8))
        s.append('<g class="fl-tk" style="--k:%d"><path d="M173 %dl3.5 3.5 7-8" stroke="#c4ff49" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/></g>' % (k, y))
        s.append(txt(196, y + 5, lab, 13, '#fff', 0.92, anchor='start'))
        s.append(txt(398, y + 5, lim, 12, '#c4ff49', 0.95, anchor='end'))
    d, pts = path(('M', 78, 125), ('L', 150, 125), n=4)
    s.append(dot('fl-p', 5, LIME)); G.travel('fl-p', pts, 10, 50, 4.5, rest=pts[-1], rest_opacity=0)
    s.append(node(60, 125, 26, 'tube', 0.2, LIME, fill='#142e14', isz=28))
    s.append(node(486, 125, 26, 'shield', 0.4, WHITE, isz=28))
    s.append('<path d="M420 125H458" stroke="rgba(196,255,73,0.35)" stroke-width="2.4" stroke-dasharray="2 7" stroke-linecap="round" fill="none"/>')
    s.append(txt(60, 172, 'Labs in', 12, '#fff', 0.8)); s.append(txt(486, 172, 'Caught early', 12, '#c4ff49', 0.9))
    return '\n'.join(s)

# ---------- tiers: clear link / uncommon / depends on the form ----------
def tiers():
    s = []
    cols = [('Clear link', ['Higher hematocrit', 'Acne, oily skin', 'PSA rise', 'Lower sperm count'], True),
            ('Uncommon, weak link', ['Breast swelling', 'Balding (family trait)', 'Worse sleep apnea'], False),
            ('Depends on the form', ['Shots: mood, libido swings', 'Gel: transfer by touch', 'Patch: skin reactions'], False)]
    k = 0
    for c, (head, items, hot) in enumerate(cols):
        x = 16 + c * 180
        s.append('<g class="ti-h" style="--k:%d"><rect x="%d" y="16" width="168" height="40" rx="12" fill="%s" stroke="%s" stroke-width="2"/></g>' % (c, x, 'rgba(196,255,73,0.14)' if hot else '#142e14', '#c4ff49' if hot else 'rgba(255,255,255,0.5)'))
        s.append(txt(x + 84, 41, head, 13, '#c4ff49' if hot else '#fff', 0.95))
        for j, it in enumerate(items):
            y = 70 + j * 38
            s.append('<g class="ti-p" style="--k:%d"><rect x="%d" y="%d" width="156" height="30" rx="15" fill="rgba(255,255,255,0.05)" stroke="%s" stroke-width="1.5"/>%s</g>' % (k, x + 6, y, 'rgba(196,255,73,0.55)' if hot else 'rgba(255,255,255,0.3)', txt(x + 84, y + 20, it, 11.5, '#fff', 0.92)))
            k += 1
    s.append(txt(280, 238, 'Most frequent in trials: a rise in hematocrit (Endocrine Society)', 12, '#c4ff49', 0.9))
    return '\n'.join(s)

# ---------- hematocrit: cells stream through a vessel, the level rises toward the 48 and 54 lines ----------
def hct():
    s = ['<defs><clipPath id="hc-clip"><rect x="22" y="62" width="316" height="92" rx="40"/></clipPath></defs>']
    s.append('<rect x="20" y="60" width="320" height="96" rx="42" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.45)" stroke-width="2.4"/>')
    s.append('<g clip-path="url(#hc-clip)">')
    for k in range(10):
        y = 84 + (k * 37) % 48
        s.append('<g class="hc-c" style="--k:%d;--x:%dpx"><ellipse cx="0" cy="%d" rx="13" ry="8" fill="#fff" fill-opacity="0.82"/></g>' % (k, 30 + k * 31, y))
    for k in range(6):
        y = 76 + (k * 29) % 64
        s.append('<g class="hc-x" style="--k:%d;--x:%dpx"><ellipse cx="0" cy="%d" rx="11" ry="7" fill="#c4ff49" fill-opacity="0.8"/></g>' % (k, 46 + k * 52, y))
    s.append('</g>')
    s.append(txt(180, 44, 'Testosterone raises red cell count', 12, '#fff', 0.85))
    s.append(txt(180, 186, 'More red cells = thicker blood', 12, '#fff', 0.75))
    # tube: 40 at y=214, 60 at y=34 (9 px per point)
    Y = lambda v: 214 - (v - 40) * 9
    s.append(txt(400, 22, 'Hematocrit', 12, '#c4ff49', 0.95))
    s.append('<rect x="380" y="32" width="40" height="186" rx="18" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.55)" stroke-width="2.2"/>')
    s.append('<g class="hc-lv"><rect x="384" y="%s" width="32" height="%s" rx="10" fill="#c4ff49" fill-opacity="0.55"/></g>' % (f(Y(52)), f(214 - Y(52))))
    for v, lab, sub, col in ((54, '54 percent', 'pause and recheck', LIME), (48, '48 percent', 'start with caution', WHITE)):
        s.append('<path d="M372 %sH430" stroke="%s" stroke-width="2.2" stroke-dasharray="4 4"/>' % (f(Y(v)), col))
        s.append('<g class="hc-th" style="--k:%d">%s%s</g>' % (0 if v == 54 else 1, txt(438, Y(v) - 2, lab, 13, '#c4ff49' if col == LIME else '#fff', 0.95, 'start'), txt(438, Y(v) + 14, sub, 11, '#fff', 0.75, 'start')))
    return '\n'.join(s)

# ---------- skin, hair, breasts: three tiles + testosterone converting to estradiol ----------
def skin():
    s = []
    tiles = [('mood', 'Acne, oily skin', 'Clear link', True), ('hair', 'Balding', 'Uncommon, family trait', False), ('gland', 'Breast tenderness', 'Swelling is uncommon', False)]
    for k, (ic, a, b, hot) in enumerate(tiles):
        y = 18 + k * 66
        s.append('<g class="sk-t" style="--k:%d"><rect x="16" y="%d" width="210" height="54" rx="12" fill="%s" stroke="%s" stroke-width="1.8"/>%s%s%s</g>'
                 % (k, y, 'rgba(196,255,73,0.08)' if hot else 'rgba(255,255,255,0.04)', '#c4ff49' if hot else 'rgba(255,255,255,0.35)', ico(ic, 42, y + 27, 24, LIME if hot else WHITE, 1.8), txt(64, y + 23, a, 13, '#c4ff49' if hot else '#fff', 0.95, 'start'), txt(64, y + 41, b, 11, '#fff', 0.75, 'start')))
    s.append(txt(290, 70, 'Testosterone', 12, '#c4ff49', 0.95))
    s.append('<path d="M250 96H330M398 96H470" stroke="rgba(255,255,255,0.2)" stroke-width="2.2" stroke-dasharray="2 6"/>')
    s.append('<g class="sk-gt"><rect x="332" y="70" width="64" height="52" rx="12" fill="#142e14" stroke="#c4ff49" stroke-width="2.2"/></g>')
    s.append(txt(364, 101, 'Converts', 11, '#fff', 0.9)); s.append(txt(364, 60, 'Aromatase', 11, '#fff', 0.7))
    d, pts = path(('M', 252, 96), ('L', 330, 96)); s.append(dot('sk-a fx', 7, LIME, ring=True)); G.travel('sk-a', pts, 4, 40, 6, rest=pts[-1], rest_opacity=0, fade=3)
    d, pts = path(('M', 398, 96), ('L', 472, 96)); s.append(dot('sk-b fx', 7, WHITE, ring=True)); G.travel('sk-b', pts, 50, 84, 6, rest=pts[-1], rest_opacity=0, fade=3)
    s.append('<g class="sk-e"><circle cx="502" cy="96" r="26" fill="#0f240f" stroke="rgba(255,255,255,0.8)" stroke-width="2.4"/></g>')
    s.append(txt(502, 101, 'E2', 15, '#fff', 0.95)); s.append(txt(502, 140, 'Estradiol', 12, '#fff', 0.85))
    s.append(txt(392, 180, 'In a 2023 trial, shots raised estradiol', 11.5, '#fff', 0.8)); s.append(txt(392, 198, 'and nasal gel did not', 11.5, '#c4ff49', 0.9))
    return '\n'.join(s)

# ---------- fertility: outside T quiets the pituitary signal, testes shrink, sperm fade ----------
def fert():
    s = [node(150, 50, 26, 'brain', 0.1, LIME, fill='#142e14', isz=28)]
    s.append(txt(116, 55, 'Pituitary', 11.5, '#fff', 0.8, 'end'))
    s.append('<path d="M150 78V156" stroke="rgba(255,255,255,0.14)" stroke-width="3"/>')
    s.append('<g class="fe-sg"><path d="M150 78V156" stroke="#c4ff49" stroke-width="3" stroke-dasharray="6 6"/></g>')
    s.append(txt(162, 122, 'LH + FSH', 12, '#c4ff49', 0.95, 'start'))
    s.append('<g class="fe-ts"><ellipse cx="128" cy="192" rx="20" ry="25" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.75)" stroke-width="2.2"/><ellipse cx="172" cy="192" rx="20" ry="25" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.75)" stroke-width="2.2"/></g>')
    s.append(txt(150, 236, 'Testes', 11.5, '#fff', 0.8))
    for k in range(3):
        x, y = 206 + k * 6, 170 + k * 16
        s.append('<g class="fe-sp" style="--k:%d"><circle cx="%d" cy="%d" r="3.6" fill="#c4ff49"/><path d="M%s %sq7 -5 14 0t14 0" fill="none" stroke="#c4ff49" stroke-width="1.6" stroke-linecap="round"/></g>' % (k, x, y, f(x + 3), f(y)))
    s.append(node(420, 50, 24, 'drop', 0.3, WHITE, isz=24)); s.append(txt(420, 92, 'Outside testosterone', 11.5, '#fff', 0.85))
    d, pts = path(('M', 394, 50), ('C', 330, 14, 240, 14, 180, 42), n=8)
    s.append('<path d="%s" stroke="rgba(255,255,255,0.22)" stroke-width="2.2" stroke-dasharray="2 6" fill="none"/>' % d)
    for i in range(2):
        s.append(dot('fe-d%d fx' % i, 5, WHITE)); G.travel('fe-d%d' % i, pts, 6, 40, 6, delay='%ss' % f(-i * 3), rest=pts[-1], rest_opacity=0, fade=3)
    s.append(chip(262, 116, 282, 50, 'fe-c', 0, ['Testes 16 to 19 percent smaller', 'after four months of shots (1981)'], True))
    s.append(chip(262, 178, 282, 50, 'fe-c', 1, ['65 percent had no sperm', 'by six months (WHO trial, 1990)'], False))
    return '\n'.join(s)

# ---------- heart: scrolling ECG strip, TRAVERSE bars, three flagged events ----------
def heart():
    s = ['<defs><clipPath id="ht-clip"><rect x="20" y="16" width="520" height="84" rx="12"/></clipPath></defs>']
    s.append('<rect x="20" y="16" width="520" height="84" rx="12" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.25)" stroke-width="1.6"/>')
    y0, d = 62, ['M20 62']
    for i in range(5):
        x = 20 + i * 130
        d.append('H%d l8 -8 l8 8 l8 10 l8 -36 l8 46 l8 -12 l6 0' % (x + 40))
        d.append('H%d' % (x + 130))
    s.append('<g clip-path="url(#ht-clip)"><g class="ht-ecg"><path d="%s" fill="none" stroke="#c4ff49" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/></g></g>' % ' '.join(d))
    for k, (lab, v, col) in enumerate((('Testosterone gel', 7.0, LIME), ('Placebo gel', 7.3, WHITE))):
        y = 140 + k * 52
        s.append(txt(24, y - 8, lab, 12, '#fff', 0.85, 'start'))
        w = v / 8 * 270
        s.append('<g class="ht-b" style="--k:%d"><rect x="24" y="%d" width="%s" height="22" rx="7" fill="%s" fill-opacity="%s"/></g>' % (k, y, f(w), col, 0.75 if col == LIME else 0.4))
        s.append(txt(32 + w, y + 16, '%.1f percent' % v, 12, '#c4ff49' if col == LIME else '#fff', 0.95, 'start'))
    s.append(txt(445, 118, 'Higher with testosterone', 11.5, '#c4ff49', 0.9))
    for k, lab in enumerate(('Atrial fibrillation', 'Acute kidney injury', 'Pulmonary embolism')):
        y = 128 + k * 36
        s.append('<g class="ht-c" style="--k:%d"><rect x="350" y="%d" width="190" height="28" rx="9" fill="rgba(255,255,255,0.04)" stroke="rgba(196,255,73,0.5)" stroke-width="1.5"/>%s%s</g>' % (k, y, ico('up', 368, y + 14, 16, LIME, 2.2), txt(384, y + 19, lab, 12, '#fff', 0.92, 'start')))
    return '\n'.join(s)

# ---------- prostate: PSA line rises a little, two check lines ----------
def psa():
    s = []
    Y = lambda v: 180 - v * 35
    s.append('<path d="M50 20V180H330" stroke="rgba(255,255,255,0.4)" stroke-width="2" fill="none"/>')
    s.append(txt(30, 26, 'PSA', 11, '#fff', 0.75))
    for k, (v, lab) in enumerate(((4.0, '4.0 ng/mL: check'), (0.92 + 1.4, '+1.4 in year 1: check'))):
        s.append('<g class="ps-th" style="--k:%d"><path d="M50 %sH330" stroke="%s" stroke-width="2" stroke-dasharray="5 5"/>%s</g>' % (k, f(Y(v)), '#c4ff49' if k == 0 else '#fff', txt(338, Y(v) + 4, lab, 12, '#c4ff49' if k == 0 else '#fff', 0.92, 'start')))
    d, pts = path(('M', 50, Y(0.92)), ('C', 110, Y(0.95), 150, Y(1.25), 200, Y(1.3)), ('C', 250, Y(1.35), 290, Y(1.36), 330, Y(1.36)), n=8)
    s.append(dr(d, 0.3, 1.2, LIME, 3.2))
    s.append(txt(196, Y(1.3) - 14, 'Average rise 0.3 to 0.44 ng/mL', 11.5, '#fff', 0.8))
    s.append(dot('ps-d fx', 6, LIME, ring=True)); G.travel('ps-d', pts, 6, 80, 8, rest=pts[-1], rest_opacity=0, fade=4, ease='ease-in-out')
    for x, lab in ((50, 'Start'), (190, '3 to 12 mo'), (330, 'Year 1 on')):
        s.append(txt(x, 200, lab, 11, '#fff', 0.75))
    s.append('<g class="ps-ch"><rect x="40" y="218" width="480" height="34" rx="12" fill="rgba(196,255,73,0.08)" stroke="rgba(196,255,73,0.55)" stroke-width="1.6"/></g>')
    s.append(txt(280, 240, 'TRAVERSE: high-grade cancer 0.19 vs 0.12 percent, not significant', 12, '#fff', 0.92))
    return '\n'.join(s)

# ---------- sleep apnea breathing wave + blood pressure gauge ----------
def sleepbp():
    s = ['<rect x="16" y="14" width="276" height="180" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.22)" stroke-width="1.5"/>',
         '<rect x="306" y="14" width="238" height="180" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.22)" stroke-width="1.5"/>']
    s.append(ico('sleep', 44, 44, 24, LIME, 1.8)); s.append(txt(64, 50, 'Sleep apnea', 13, '#c4ff49', 0.95, 'start'))
    s.append('<g class="sb-ps"><rect x="128" y="84" width="50" height="52" rx="10" fill="#fff" fill-opacity="0.08"/></g>')
    wv = 'M36 110C46 86 56 86 66 110S86 134 96 110S116 86 126 110H180C190 86 200 86 210 110S230 134 240 110S260 86 270 110'
    s.append(f'<path d="{wv}" fill="none" stroke="#c4ff49" stroke-opacity="0.32" stroke-width="3" stroke-linecap="round"/>')
    s.append(f'<path class="sb-wv" pathLength="1" d="{wv}" fill="none" stroke="#c4ff49" stroke-width="3" stroke-linecap="round"/>')
    s.append(txt(153, 152, 'pause', 11, '#fff', 0.7))
    s.append(txt(154, 180, 'Treat severe apnea before TRT', 12, '#fff', 0.88))
    cx, cy, r = 425, 140, 70
    s.append(txt(425, 42, 'Blood pressure', 13, '#c4ff49', 0.95))
    s.append('<path d="M%d %dA%d %d 0 0 1 %d %d" stroke="rgba(255,255,255,0.3)" stroke-width="10" stroke-linecap="round" fill="none"/>' % (cx - r, cy, r, r, cx + r, cy))
    s.append('<path d="M%s %sA%d %d 0 0 1 %d %d" stroke="#c4ff49" stroke-opacity="0.75" stroke-width="10" stroke-linecap="round" fill="none"/>' % (f(cx + r * math.cos(math.radians(-50))), f(cy + r * math.sin(math.radians(-50))), r, r, cx + r, cy))
    s.append('<g class="sb-nd"><path d="M%d %dV%d" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g>' % (cx, cy, cy - r + 14))
    s.append('<circle cx="%d" cy="%d" r="8" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/>' % (cx, cy))
    s.append(txt(425, 178, 'Rises across all products (FDA)', 11.5, '#fff', 0.85))
    return '\n'.join(s)

# ---------- monitoring: a dot walks the schedule, each checkpoint's tests light ----------
def monitor():
    s = ['<path d="M70 62H490" stroke="rgba(255,255,255,0.18)" stroke-width="4" stroke-linecap="round"/>']
    s.append(dr('M70 62H490', 0.2, 1.4, LIME, 4))
    cols = [('Before', ['Testosterone x2', 'Hematocrit', 'PSA + prostate exam', 'Estradiol, lipids']),
            ('3 to 6 mo', ['Testosterone', 'Hematocrit', 'Symptoms review']),
            ('By year 1', ['PSA + prostate exam', 'Blood pressure', 'Side effects check']),
            ('Every year', ['Testosterone', 'Hematocrit', 'PSA per screening'])]
    for j, (head, items) in enumerate(cols):
        x = 70 + j * 140
        s.append(txt(x, 34, head, 13, '#c4ff49', 0.95))
        s.append('<g class="mo-n" style="--k:%d"><circle cx="%d" cy="62" r="11" fill="#0f240f" stroke="#c4ff49" stroke-width="3"/></g>' % (j, x))
        for i, it in enumerate(items):
            y = 90 + i * 34
            s.append('<g class="mo-c" style="--k:%d"><rect x="%d" y="%d" width="128" height="26" rx="8" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.3)" stroke-width="1.4"/>%s</g>' % (j, x - 64, y, txt(x, y + 17, it, 11, '#fff', 0.92)))
    d, pts = path(('M', 70, 62), ('L', 490, 62))
    s.append(dot('mo-d fx', 7, LIME, ring=True)); G.travel('mo-d', pts, 5, 85, 8.5, rest=pts[-1], rest_opacity=0, fade=4)
    return '\n'.join(s)

# ---------- manage: a dial points at each adjustment in turn ----------
def manage():
    cx, cy = 120, 110
    s = ['<circle cx="120" cy="110" r="66" fill="#142e14" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>',
         '<circle cx="120" cy="110" r="48" fill="none" stroke="rgba(196,255,73,0.3)" stroke-width="6" stroke-dasharray="2 9"/>']
    s.append('<g class="mn-pt"><path d="M120 110H178" stroke="#c4ff49" stroke-width="5" stroke-linecap="round"/><circle cx="178" cy="110" r="5" fill="#c4ff49"/></g>')
    s.append('<circle cx="120" cy="110" r="16" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/>')
    tiles = [('down', 'Lower the dose or change the interval'), ('swap', 'Switch the form: shot, gel or nasal'), ('clock', 'Pause until hematocrit settles'), ('drop', 'Donate blood (phlebotomy)')]
    for k, (ic, lab) in enumerate(tiles):
        y = 20 + k * 50
        s.append('<g class="mn-t" style="--k:%d"><rect x="222" y="%d" width="322" height="40" rx="12" fill="rgba(255,255,255,0.04)" stroke="rgba(196,255,73,0.5)" stroke-width="1.6"/>%s%s</g>' % (k, y, ico(ic, 244, y + 20, 20, LIME, 2), txt(264, y + 25, lab, 12.5, '#fff', 0.92, 'start')))
    return '\n'.join(s)

# ---------- help: monitoring panel with sparklines -> telehealth review -> plan ----------
def help_fig():
    s = ['<g class="pop t" style="--d:0.1"><rect x="24" y="18" width="276" height="196" rx="14" fill="#142e14" stroke="rgba(255,255,255,0.55)" stroke-width="2"/></g>']
    s.append(txt(162, 42, 'Your monitoring', 12, '#c4ff49', 0.95))
    rows = [('Hematocrit', 'M0 10L20 8L40 6L60 5L80 6L100 6'), ('PSA', 'M0 9L20 9L40 8L60 7L80 7L100 7'), ('Estradiol', 'M0 8L20 4L40 9L60 6L80 7L100 6'),
            ('Lipids', 'M0 5L20 6L40 6L60 7L80 6L100 6'), ('Blood pressure', 'M0 9L20 7L40 8L60 6L80 7L100 6')]
    for k, (lab, sp) in enumerate(rows):
        y = 64 + k * 32
        s.append(txt(40, y + 4, lab, 12, '#fff', 0.9, 'start'))
        dd = re.sub(r'([ML])(\d+) (\d+)', lambda m: '%s%d %d' % (m.group(1), 148 + int(m.group(2)), y - 8 + int(m.group(3)) * 1.4), sp)
        s.append(dr(dd, 0.3 + k * 0.12, 0.9, 'rgba(255,255,255,0.75)', 2.2))
        s.append('<circle class="hp-s" style="--k:%d" cx="276" cy="%d" r="6" fill="#c4ff49"/>' % (k, y))
    for i, (a, b, cls, col) in enumerate([((300, 116), (390, 116), 'hp-a', WHITE), ((448, 116), (484, 116), 'hp-b', LIME)]):
        d, pts = path(('M', a[0], a[1]), ('L', b[0], b[1]))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % d)
        s.append(dot('%s fx' % cls, 5, col)); G.travel(cls, pts, 8 + i * 40, 40 + i * 40, 6, rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(420, 116, 28, 'coach', 0.3, LIME, fill='#173617', isz=28)); s.append(txt(420, 172, 'Telehealth review', 12, '#fff', 0.85))
    s.append(node(510, 116, 24, 'doc', 0.5, LIME, fill='#142e14', isz=24)); s.append(txt(510, 156, 'Plan', 12, '#c4ff49', 0.95))
    return '\n'.join(s)

def final():
    s = ['<defs><radialGradient id="fn-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.3"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><circle cx="180" cy="105" r="92" fill="url(#fn-g)"/>']
    s.append('<circle class="fn-ring fx" cx="180" cy="104" r="56" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append('<g class="fn-sh"><path d="M180 48l46 17v34c0 30-20 48-46 56-26-8-46-26-46-56V65z" fill="#142e14" stroke="#c4ff49" stroke-width="4" stroke-linejoin="round"/></g>')
    s.append(dr('M160 104l14 14 28-30', 0.4, 0.9, '#fff', 5))
    s.append(node(56, 70, 20, 'tube', 0.3, WHITE, isz=22)); s.append(node(304, 70, 20, 'pulse', 0.4, LIME, fill='#142e14', isz=22))
    return '\n'.join(s)

FAQMOTIF = '''<g class="fq-dp"><path d="M28 30c9 11 14 18 14 25a14 14 0 0 1-28 0c0-7 5-14 14-25z" stroke="#c4ff49" stroke-width="4" stroke-linejoin="round"/></g>
<path class="dr" pathLength="1" style="--d:0.25;--dur:1.1s" d="M70 36c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82" cy="64" r="3" fill="#fff"/>
<g class="fq-fr" style="--k:0"><circle cx="104" cy="22" r="5" fill="#c4ff49"/></g><g class="fq-fr" style="--k:1"><circle cx="50" cy="20" r="4" fill="#c4ff49"/></g>'''

def step_icons():
    return {
     "{{STEP1}}": '<path d="M8 12h32a2 2 0 0 1 2 2v18a2 2 0 0 1-2 2H22l-8 6v-6H8a2 2 0 0 1-2-2V14a2 2 0 0 1 2-2z"/><g class="hi-bl" style="--k:0"><circle cx="16" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="24" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="32" cy="23" r="2" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M12 6h10"/><path d="M14 6v26a3 3 0 0 0 6 0V6"/><path d="M14 20h6"/><g class="hi-gr" style="--k:0"><path d="M30 40V30M36 40V22M42 40V34" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<path d="M8 38C8 22 18 12 40 10c0 22-10 30-26 30"/><g class="hi-sw" style="--k:0"><path d="M8 38c6-9 12-15 20-19" stroke="#c4ff49"/></g>',
     "{{STEP4}}": '<path d="M6 40h36"/><path d="M8 34l9-8 7 5 14-14"/><g class="hi-ck" style="--k:0"><path d="M30 8l4 4 8-9" stroke="#c4ff49"/></g>',
    }

def hub_nodes():
    icons = ['sperm', 'scale', 'tube', 'link', 'sleep', 'list', 'compass', 'coach', 'labs', 'coin']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)
        out.append((round(280 + 230 * math.cos(a)), round(100 + 68 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{CHECKLIST}}": checklist(), "{{TIERS}}": tiers(), "{{HCT}}": hct(), "{{SKIN}}": skin(), "{{FERT}}": fert(), "{{HEART}}": heart(), "{{PSA}}": psa(),
         "{{SLEEPBP}}": sleepbp(), "{{MONITOR}}": monitor(), "{{MANAGE}}": manage(), "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB,
         "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "TRT side effects in men: the full list, hematocrit, PSA, estradiol, fertility, heart risk and monitoring",
      "TRT side effects", "TRT side effects: the full list, and what gets monitored", slots, G, published="2026-10-16", modified="2026-10-21")

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
# 2026-10-21 deepen (size budget, GHL save fails ~170 KB): compact JSON-LD, drop HTML comments outside scripts,
# join SVG element lines, and drop CSS rules whose class selectors match nothing on this page (page-local, static check)
def ld_compact(mm):
    return mm.group(1) + json.dumps(json.loads(mm.group(2)), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + mm.group(3)
m = re.sub(r'(<script type="application/ld\+json">\s*)([\s\S]*?)(\s*</script>)', ld_compact, m)
_parts = re.split(r'(<script\b[\s\S]*?</script>)', m)
m = ''.join(pp if i % 2 else re.sub(r'<!--[\s\S]*?-->\n?', '', pp) for i, pp in enumerate(_parts))
m = re.sub(r'<svg\b[\s\S]*?</svg>', lambda x: re.sub(r'>\n<', '><', x.group(0)), m)
_body = re.sub(r'<style>[\s\S]*?</style>', '', m)
_cls = set(w for c in re.findall(r'class="([^"]*)"', _body) for w in c.split())
_js = set(re.findall(r'[\w-]+', ' '.join(re.findall(r'<script(?![^>]*ld\+json)[^>]*>([\s\S]*?)</script>', m))))
def _purge(css):
    def rule(r):
        sel = r.group(1)
        if not sel.lstrip().startswith(('.', 'html', 'body')) or '.pg' not in sel and '.js-reveal' not in sel: return r.group(0)
        live = any(all(t in _cls or t in _js for t in re.findall(r'\.([A-Za-z][\w-]*)', part)) for part in sel.split(','))
        return r.group(0) if live else ''
    return re.sub(r'([^{}@]+)\{([^{}]*)\}', rule, css)
m = re.sub(r'(?<=<style>)[\s\S]*?(?=</style>)', lambda x: _purge(x.group(0)), m)
_parts = re.split(r'(<script\b[\s\S]*?</script>|<style>[\s\S]*?</style>)', m)
_blk = r'(?:/?(?:li|ul|ol|tr|td|th|thead|tbody|table|caption|div|section|p|figure|figcaption|h[1-6]|details|summary|main|nav|svg|g|defs|symbol|path|circle|rect|text|ellipse)\b)'
m = ''.join(pp if i % 2 else re.sub(r'>\n(?=<' + _blk + ')', '>', pp) for i, pp in enumerate(_parts))
open(p, "w", encoding="utf-8").write(m)
# Safari-motion guard (templates already fixed; this is a no-op unless something regressed)
print(subprocess.run([sys.executable, "/workspace/safari-fix/apply_fix.py", p], capture_output=True, text=True).stdout.strip())
print("minified", len(full.encode()), "->", len(open(p, encoding="utf-8").read().encode()), "bytes")
