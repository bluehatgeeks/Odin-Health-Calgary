"""Build /workspace/pages/andropause-vs-menopause/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "andropause-vs-menopause"
TITLE = "Andropause vs Menopause: How They Differ | Odin Health Labs"
DESC = "Andropause vs menopause: why testosterone drifts down slowly in men instead of stopping, who gets low T, how symptoms and labs differ and what men can do."
OG_ALT = "Odin Health Labs: andropause vs menopause, a slow testosterone decline in men compared with the defined end point of menopause"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 158, (len(TITLE), len(DESC))

# extra icons used only on this page (merged before icons_svg() runs inside build())
common.ICONS.update({
 "pin": '<path d="M12 21s-6-6.2-6-11a6 6 0 0 1 12 0c0 4.8-6 11-6 11z"/><circle cx="12" cy="10" r="2.2"/>',
 "phone": '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
 "split": '<path d="M4 7c4 0 8 2 16 6"/><path d="M4 7h7c2 0 2 10 4 10h5"/>',
 "bone": '<path d="M7 17l10-10"/><path d="M5.5 15.5a2.5 2.5 0 1 0 3 3"/><path d="M15.5 5.5a2.5 2.5 0 1 1 3 3"/><path d="M8.5 18.5a2.5 2.5 0 1 1-3-3"/><path d="M18.5 8.5a2.5 2.5 0 1 1-3-3"/>',
 "sliders": '<path d="M4 7h10M18 7h2M4 17h4M12 17h8"/><circle cx="16" cy="7" r="2"/><circle cx="10" cy="17" r="2"/>',
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "users": '<circle cx="8" cy="8" r="3"/><circle cx="16" cy="8" r="3"/><path d="M2.5 20c0-3.5 2.5-5.5 5.5-5.5s5.5 2 5.5 5.5"/><path d="M13.5 15c.8-.4 1.6-.5 2.5-.5 3 0 5.5 2 5.5 5.5"/>',
})

FAQ = [
 ("Is andropause the same as menopause?",
  "No. Menopause is a defined event: the ovaries run out of egg follicles, estrogen falls and periods stop for good, confirmed once there has been no period for twelve months in a row. The average age is 51 in Canada and the USA. Andropause, or the &ldquo;male menopause,&rdquo; is a popular term for something quite different. The NHS describes testosterone falling steadily by about 1 percent a year from around age 30 to 40, with no sudden drop and no end point, and calls the &ldquo;male menopause&rdquo; label misleading. The medical term for symptoms plus low testosterone later in life is late-onset hypogonadism."),
 ("When does andropause start, and do all men get it?",
  "Testosterone starts drifting down slowly from around age 30 to 40, but that decline on its own is unlikely to cause problems, according to the NHS. Not every man develops symptomatic low testosterone. In the European Male Ageing Study of men aged 40 to 79, about 2 in 100 met a strict definition of late-onset hypogonadism (three sexual symptoms plus low total and free testosterone). That rose from about 1 in 1,000 men in their 40s to about 5 in 100 in their 70s, and it was more common with a higher body-mass index and more health conditions. Menopause, by contrast, happens to every woman."),
 ("Can men get hot flashes like women in menopause?",
  "They can, but it is not typical of ordinary aging. The Endocrine Society lists hot flushes and sweats among the signs of testosterone deficiency, in a list it bases on men with severe deficiency. The signs most closely tied to low testosterone in middle-aged and older men are sexual: lower sex drive, fewer morning erections and erectile dysfunction. See <a href=\"%s/low-testosterone-symptoms\">low testosterone symptoms in men</a>." % SITE),
 ("How is andropause diagnosed compared with menopause?",
  "For women aged 45 or over, NICE guidance says menopause is identified from symptoms and periods, usually without blood tests. For men it works the other way round: low testosterone is confirmed only when consistent symptoms line up with low results on two separate fasting, early-morning total testosterone tests. The American Urological Association uses a total testosterone below 300 ng/dL on two early-morning tests, and the Canadian Urological Association suggests below 10 nmol/L as a reasonable threshold. Free testosterone, SHBG and LH help explain borderline results and the cause. See <a href=\"%s/low-testosterone-labs-to-ask-for\">which labs to ask for</a>." % SITE),
 ("What can men do about andropause symptoms?",
  "Start with the things that move testosterone and symptoms. Guidelines name obesity, sleep apnea, acute illness, opioids, glucocorticoids, extreme dieting and extreme exercise as causes to address first, and in the European Male Ageing Study men who lost weight saw their testosterone rise in proportion. Short sleep, stress, heavy drinking and inactivity drive many of the same symptoms. The Endocrine Society suggests against routinely prescribing testosterone to all men 65 or older with low levels, so the first step is a clear picture of your symptoms, labs and habits. See <a href=\"%s/trt-or-fix-causes-first\">TRT or fix the causes first</a>." % SITE),
 ("How does Odin Health Labs work with my doctor?",
  'Odin Health Labs is a telehealth service for men in Canada and the USA with andropause and low testosterone symptoms. We work alongside your own doctor: we go through your symptoms and lab results with you, build your sleep, training, nutrition and stress plan, and track your progress with follow-up check-ins and repeat labs. We can share your symptom list, plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

def txt(x, y, s, size=13, fill='#fff', op=0.85, anchor='middle', extra=''):
    return '<text x="%s" y="%s" font-size="%s" fill="%s" fill-opacity="%s" text-anchor="%s"%s>%s</text>' % (f(x), f(y), size, fill, op, anchor, extra, s)

# ---------- 1 · HERO: two hormone curves, a slow testosterone drift vs a steep estrogen fall at menopause ----------
def hero():
    s = ['<defs><radialGradient id="av-g" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.14"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="250" cy="150" rx="230" ry="140" fill="url(#av-g)"/>']
    s.append('<path d="M60 40V254H450" stroke="rgba(255,255,255,0.4)" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    for age in (30, 40, 50, 60, 70, 80):
        x = 70 + (age - 30) * 7.4
        s.append('<path d="M%s 254v6" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>' % f(x))
        s.append(txt(x, 276, str(age), 12, '#fff', 0.6))
    s.append(txt(255, 300, 'Age', 12, '#fff', 0.6))
    s.append(txt(36, 150, 'Hormone level', 12, '#fff', 0.6, 'middle', ' transform="rotate(-90 36 150)"'))
    s.append('<path d="M225 56V254" stroke="rgba(255,255,255,0.25)" stroke-width="1.6" stroke-dasharray="3 6"/>')
    s.append(txt(225, 48, 'Menopause, average age 51', 12, '#fff', 0.75))
    dm, pm = path(('M', 70, 78), ('L', 196, 82), ('C', 226, 88, 236, 204, 270, 212), ('L', 440, 222))
    da, pa = path(('M', 70, 70), ('C', 200, 92, 330, 126, 440, 150))
    s.append(dr(dm, 0.3, 1.6, 'rgba(255,255,255,0.75)', 3))
    s.append(dr(da, 0.5, 1.6, LIME, 3.4))
    s.append('<circle class="av-ring fx" cx="236" cy="150" r="18" fill="none" stroke="#fff" stroke-width="2"/>')
    s.append(dot('av-m fx', 5.5, WHITE)); G.travel('av-m', pm, 4, 90, 10, rest=pm[-1], rest_opacity=0, fade=3)
    s.append(dot('av-a fx', 6, LIME, ring=True)); G.travel('av-a', pa, 4, 90, 10, delay='-1s', rest=pa[-1], rest_opacity=0, fade=3)
    s.append(txt(440, 176, 'Testosterone (men)', 13, '#c4ff49', 0.95, 'end'))
    s.append(txt(440, 242, 'Estrogen (women)', 13, '#fff', 0.85, 'end'))
    return '\n'.join(s)

# ---------- 2 · TIMING: age ruler; men's lane drifts the whole span, women's lane passes the 45-55 window ----------
def timing():
    X = lambda age: 60 + (age - 30) * 9
    s = ['<defs><linearGradient id="tm-g" x1="0" x2="1"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.95"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0.3"/></linearGradient></defs>']
    s.append('<path d="M60 200H510" stroke="rgba(255,255,255,0.45)" stroke-width="2.2" stroke-linecap="round"/>')
    for age in range(30, 81, 10):
        s.append('<path d="M%d 194v12" stroke="rgba(255,255,255,0.45)" stroke-width="2"/>' % X(age))
        s.append(txt(X(age), 226, str(age), 12, '#fff', 0.65))
    s.append(txt(60, 46, 'Men: testosterone', 13, '#c4ff49', 0.95, 'start'))
    s.append('<g class="pop t" style="--d:0.2"><rect x="60" y="60" width="450" height="18" rx="9" fill="url(#tm-g)"/></g>')
    d, pts = path(('M', 60, 69), ('L', 510, 69))
    s.append(dot('tm-m fx', 7, '#fff', ring=True)); G.travel('tm-m', pts, 3, 93, 16, rest=pts[-1], rest_opacity=0, fade=3)
    s.append(txt(510, 100, 'Slow and steady, about 1 percent a year', 12, '#fff', 0.75, 'end'))
    s.append(txt(60, 132, 'Women: menopause', 13, '#fff', 0.9, 'start'))
    s.append('<rect x="60" y="145" width="%d" height="10" rx="5" fill="rgba(255,255,255,0.55)"/>' % (X(45) - 60))
    s.append('<rect x="%d" y="147" width="%d" height="6" rx="3" fill="rgba(255,255,255,0.14)"/>' % (X(55), 510 - X(55)))
    s.append('<rect class="tm-band" x="%d" y="138" width="%d" height="24" rx="8" fill="rgba(196,255,73,0.22)" stroke="#c4ff49" stroke-width="2"/>' % (X(45), X(55) - X(45)))
    d2, p2 = path(('M', X(45), 150), ('L', X(55), 150))
    s.append(dot('tm-w fx', 6, LIME)); G.travel('tm-w', p2, 30, 50, 8, rest=p2[-1], rest_opacity=0, fade=4)
    s.append('<circle class="tm-mk" cx="%d" cy="150" r="5" fill="#fff"/>' % X(51))
    s.append(txt(X(51), 182, 'Usually 45 to 55, average 51', 12, '#c4ff49', 0.95))
    return '\n'.join(s)

# ---------- 3 · WHO: a 100-dot grid with two lit men + four bars growing by decade (EMAS) ----------
def prevalence():
    s = []
    lit = (37, 82)
    for i in range(100):
        r, c = divmod(i, 10)
        x, y = 34 + c * 18, 40 + r * 18
        if i in lit:
            s.append('<circle class="pv-on" style="--k:%d" cx="%d" cy="%d" r="6" fill="#c4ff49"/>' % (lit.index(i), x, y))
        else:
            s.append('<circle cx="%d" cy="%d" r="5" fill="rgba(255,255,255,0.28)"/>' % (x, y))
    s.append(txt(115, 232, 'About 2 in 100 men aged 40 to 79', 12, '#c4ff49', 0.95))
    s.append('<path d="M266 200H540" stroke="rgba(255,255,255,0.45)" stroke-width="2.2" stroke-linecap="round"/>')
    s.append(txt(403, 26, 'Late-onset hypogonadism by age (EMAS)', 12, '#fff', 0.7))
    bars = [('40s', 3, '1 in 1,000'), ('50s', 18, '6 in 1,000'), ('60s', 94, '3 in 100'), ('70s', 150, '5 in 100')]
    for k, (lab, h, val) in enumerate(bars):
        x = 280 + k * 66
        s.append('<rect class="pv-b" style="--k:%d" x="%d" y="%d" width="40" height="%d" rx="4" fill="%s"/>' % (k, x, 200 - h, h, LIME if k == 3 else 'rgba(196,255,73,0.6)'))
        s.append(txt(x + 20, 220, lab, 12, '#fff', 0.8))
        s.append(txt(x + 20, 238, val, 11, '#c4ff49' if k == 3 else '#fff', 0.85))
    return '\n'.join(s)

# ---------- 4 · HORMONES: ovary follicles fade out vs testes keep sending testosterone (some bound to SHBG) ----------
def biology():
    s = ['<path d="M280 24V214" stroke="rgba(255,255,255,0.16)" stroke-width="2" stroke-dasharray="3 7"/>']
    s.append('<g class="pop t" style="--d:0.1"><circle cx="140" cy="104" r="70" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.45)" stroke-width="2.2"/></g>')
    k = 0
    for ring, (rr, n) in enumerate(((26, 6), (50, 10))):
        for j in range(n):
            a = j * 2 * math.pi / n + ring * 0.3
            s.append('<circle class="bo-f" style="--k:%d" cx="%s" cy="%s" r="%s" fill="%s"/>' % (k, f(140 + rr * math.cos(a)), f(104 + rr * math.sin(a)), 6 if ring else 5, LIME if k % 3 == 0 else '#fff'))
            k += 1
    s.append('<circle cx="140" cy="104" r="7" fill="rgba(255,255,255,0.3)"/>')
    s.append(txt(140, 202, 'Ovaries: follicles run out', 13))
    s.append(txt(140, 230, 'Estrogen falls, periods stop', 12, '#c4ff49', 0.95))
    s.append(node(370, 104, 34, 'gland', 0.2, LIME, fill='#142e14', isz=34))
    for i, (end, cls, col) in enumerate(((500, 'bt-a', LIME), (500, 'bt-b', WHITE))):
        ey = 58 if i == 0 else 150
        d, pts = path(('M', 404, 104), ('C', 440, 104, 450, ey, end, ey))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.18)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % d)
        s.append(dot('%s fx' % cls, 5, col)); G.travel(cls, pts, 6, 50, 5, delay='%ss' % f(-i * 2.5), rest=pts[0], rest_opacity=0, fade=4)
    s.append('<circle class="bt-n" cx="514" cy="58" r="14" fill="#142e14" stroke="#c4ff49" stroke-width="2.2"/>')
    s.append('<rect x="500" y="138" width="34" height="24" rx="7" fill="#0f240f" stroke="rgba(255,255,255,0.6)" stroke-width="2"/>')
    s.append(txt(514, 30, 'Free T', 12, '#c4ff49', 0.95))
    s.append(txt(517, 184, 'SHBG-bound', 12, '#fff', 0.8))
    s.append(txt(400, 202, 'Testes: production continues', 13))
    s.append(txt(400, 230, 'More SHBG with age, less free T', 12, '#c4ff49', 0.95))
    return '\n'.join(s)

# ---------- 5 · SYMPTOMS: Venn of andropause vs menopause; shared symptoms light in turn ----------
def venn():
    s = ['<g class="vn-l"><circle cx="215" cy="145" r="125" fill="rgba(196,255,73,0.08)" stroke="#c4ff49" stroke-width="2.2"/></g>',
         '<g class="vn-r"><circle cx="345" cy="145" r="125" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.6)" stroke-width="2.2"/></g>']
    s.append(txt(150, 76, 'Andropause', 15, '#c4ff49', 1))
    s.append(txt(410, 76, 'Menopause', 15, '#fff', 1))
    for k, (lab, y) in enumerate((('Morning erections', 122), ('Erectile issues', 150), ('Less muscle', 178))):
        s.append(txt(152, y, lab, 11.5, '#fff', 0.85))
    for k, (lab, y) in enumerate((('Period changes', 122), ('Vaginal dryness', 150), ('More UTIs', 178))):
        s.append(txt(408, y, lab, 11.5, '#fff', 0.85))
    shared = ['Low libido', 'Poor sleep', 'Low mood', 'Brain fog', 'Belly weight', 'Hot flushes', 'Bone loss']
    for k, lab in enumerate(shared):
        s.append('<g class="vn-i" style="--k:%d">%s</g>' % (k, txt(280, 84 + k * 22, lab, 11.5, '#c4ff49', 1)))
    s.append(txt(280, 286, 'Shared', 12, '#fff', 0.6))
    return '\n'.join(s)

# ---------- 6 · COMPARE: two columns of rows; a highlight bar steps down both together ----------
def compare_fig():
    s = []
    for c, (x, lab, col) in enumerate(((40, 'Andropause', LIME), (200, 'Menopause', WHITE))):
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="20" width="128" height="172" rx="14" fill="%s" stroke="%s" stroke-width="2"/></g>' % (0.1 + c * 0.12, x, '#142e14' if c == 0 else 'rgba(255,255,255,0.04)', col if c == 0 else 'rgba(255,255,255,0.45)'))
        s.append(txt(x + 64, 44, lab, 13, col, 0.95))
        for r in range(5):
            y = 66 + r * 24
            s.append('<path d="M%d %dh%d" stroke="rgba(255,255,255,0.4)" stroke-width="3" stroke-linecap="round"/>' % (x + 16, y, 96 - (r % 2) * 26))
    s.append('<g class="cp-h"><rect x="34" y="56" width="300" height="20" rx="6" fill="rgba(196,255,73,0.16)" stroke="#c4ff49" stroke-opacity="0.6" stroke-width="1.4"/></g>')
    s.append(node(184, 112, 14, 'split', 0.4, LIME, fill='#0f240f', isz=16))
    return '\n'.join(s)

# ---------- 7 · LABS: men's lane morning tests vs women's lane twelve-month calendar ----------
def labs():
    s = []
    s.append(txt(30, 30, 'Men', 14, '#c4ff49', 1, 'start'))
    d, pts = path(('M', 80, 74), ('L', 500, 74))
    s.append('<path d="M80 74H500" stroke="rgba(255,255,255,0.14)" stroke-width="2.4" stroke-dasharray="2 8" stroke-linecap="round"/>')
    s.append(dr(d, 0.3, 1.4, 'rgba(196,255,73,0.55)', 2.4))
    s.append(dot('lb-p fx', 6, LIME, ring=True)); G.travel('lb-p', pts, 6, 80, 9, rest=pts[-1], rest_opacity=0, fade=3, ease='ease-in-out')
    for i, (x, ic, lab) in enumerate(((80, 'sun', 'Early morning'), (220, 'tube', 'Total T'), (360, 'tube', 'Repeat test'), (500, 'labs', 'Free T, SHBG, LH'))):
        s.append(node(x, 74, 24, ic, 0.15 + i * 0.12, LIME if i else WHITE, fill='#142e14', isz=26))
        s.append(txt(x, 120, lab, 12, '#fff', 0.85))
    s.append(txt(30, 156, 'Women over 45', 14, '#fff', 0.95, 'start'))
    for k in range(12):
        r, c = divmod(k, 6)
        x, y = 40 + c * 22, 170 + r * 22
        s.append('<rect x="%d" y="%d" width="16" height="16" rx="4" fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="1.6"/>' % (x, y))
        s.append('<rect class="lb-c" style="--k:%d" x="%d" y="%d" width="10" height="10" rx="2" fill="#c4ff49"/>' % (k, x + 3, y + 3))
    s.append(txt(100, 232, 'Twelve months, no period', 12, '#fff', 0.8))
    d2, p2 = path(('M', 180, 192), ('L', 300, 192))
    s.append('<path d="M180 192H300" stroke="rgba(255,255,255,0.2)" stroke-width="2.2" stroke-dasharray="2 7"/>')
    s.append(dot('lb-w fx', 5, WHITE)); G.travel('lb-w', p2, 10, 60, 7, rest=p2[-1], rest_opacity=0, fade=4)
    s.append(node(324, 192, 24, 'check', 0.4, LIME, fill='#142e14', isz=26))
    s.append(txt(324, 236, 'Confirmed', 12, '#c4ff49', 0.95))
    s.append('<g opacity="0.5">%s<path d="M436 176l32 32" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/></g>' % ico('tube', 452, 192, 30, WHITE, 1.8))
    s.append(txt(452, 236, 'Usually no blood test', 12, '#fff', 0.75))
    return '\n'.join(s)

# ---------- 8 · LEVERS: four sliders move right in turn; a meter fills ----------
def levers():
    s = []
    for k, (ic, lab) in enumerate((('scale', 'Weight'), ('sleep', 'Sleep'), ('train', 'Training'), ('stress', 'Stress'))):
        y = 48 + k * 50
        s.append(ico(ic, 40, y, 22, LIME if k % 2 == 0 else WHITE, 1.8))
        s.append(txt(62, y + 5, lab, 13, '#fff', 0.9, 'start'))
        s.append('<path d="M150 %dH340" stroke="rgba(255,255,255,0.22)" stroke-width="6" stroke-linecap="round"/>' % y)
        s.append('<rect class="lv-t" style="--k:%d" x="150" y="%d" width="170" height="6" rx="3" fill="#c4ff49" fill-opacity="0.55"/>' % (k, y - 3))
        s.append('<g class="lv-k" style="--k:%d"><circle cx="320" cy="%d" r="11" fill="#0f240f" stroke="#c4ff49" stroke-width="2.6"/></g>' % (k, y))
        d, pts = path(('M', 350, y), ('C', 390, y, 400, 125, 428, 125))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.12)" stroke-width="2" stroke-dasharray="2 7" fill="none"/>' % d)
        s.append(dot('lv-p%d fx' % k, 4, WHITE if k % 2 else LIME)); G.travel('lv-p%d' % k, pts, 10, 50, 8, delay='%ss' % f(-k * 2), rest=pts[0], rest_opacity=0, fade=4)
    s.append('<rect x="440" y="36" width="54" height="178" rx="12" fill="none" stroke="#fff" stroke-opacity="0.7" stroke-width="2.4"/>')
    s.append('<rect class="lv-f" x="447" y="43" width="40" height="164" rx="7" fill="#c4ff49" fill-opacity="0.85"/>')
    s.append(txt(467, 238, 'Energy + drive', 12, '#c4ff49', 0.95))
    return '\n'.join(s)

# ---------- 9 · HELP: Canada + USA pins send pulses to a phone consult; a plan flows out, habits light ----------
def help_fig():
    s = []
    for i, (y, lab) in enumerate(((70, 'Canada'), (190, 'USA'))):
        s.append('<g class="pop t" style="--d:%s"><rect x="24" y="%d" width="124" height="44" rx="12" fill="#142e14" stroke="%s" stroke-width="2"/></g>' % (0.1 + i * 0.12, y - 22, LIME if i == 0 else 'rgba(255,255,255,0.55)'))
        s.append(ico('pin', 48, y, 22, LIME if i == 0 else WHITE, 1.8))
        s.append(txt(70, y + 5, lab, 14, '#fff', 0.92, 'start'))
        d, pts = path(('M', 150, y), ('C', 200, y, 210, 130, 240, 130))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % d)
        s.append(dot('hl-%d fx' % i, 5, LIME if i == 0 else WHITE)); G.travel('hl-%d' % i, pts, 8, 46, 7, delay='%ss' % f(-i * 3.5), rest=pts[0], rest_opacity=0, fade=3)
    s.append('<g class="pop t" style="--d:0.2"><rect x="240" y="30" width="84" height="200" rx="16" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/><path d="M272 214h20" stroke="rgba(255,255,255,0.5)" stroke-width="2.4" stroke-linecap="round"/></g>')
    s.append(node(282, 78, 20, 'you', 0.3, WHITE, isz=22))
    s.append(node(282, 172, 20, 'coach', 0.4, LIME, fill='#173617', isz=22))
    for k, y in enumerate((104, 126)):
        s.append('<g class="hl-b" style="--k:%d"><rect x="%d" y="%d" width="40" height="18" rx="8" fill="%s"/><path d="M%d %dh20" stroke="#0f240f" stroke-width="2" stroke-linecap="round"/></g>' % (k, 252 if k == 0 else 272, y, '#fff' if k == 0 else LIME, 262 if k == 0 else 282, y + 9))
    d, pts = path(('M', 326, 130), ('L', 440, 130))
    s.append('<path d="M326 130H440" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7"/>')
    s.append(dot('hl-o fx', 5, LIME)); G.travel('hl-o', pts, 50, 88, 7, rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(470, 130, 28, 'doc', 0.5, LIME, fill='#142e14', isz=30))
    s.append(txt(470, 84, 'Your plan', 13, '#c4ff49', 0.95))
    for k, (ic, x) in enumerate((('sleep', 420), ('train', 470), ('food', 520))):
        s.append('<g class="hl-i" style="--k:%d"><circle cx="%d" cy="200" r="17" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/>%s</g>' % (k, x, ico(ic, x, 200, 18, LIME, 1.8)))
    return '\n'.join(s)

# ---------- final: a sun rises over the horizon, rays turn, habit icons bob ----------
def final():
    s = ['<defs><clipPath id="fn-clip"><rect x="0" y="0" width="360" height="160"/></clipPath></defs>']
    s.append('<g clip-path="url(#fn-clip)"><g class="fn-sun"><g class="fn-ry">')
    for i in range(12):
        a = i * math.pi / 6
        s.append('<path d="M%s %sL%s %s" stroke="#c4ff49" stroke-opacity="0.7" stroke-width="3" stroke-linecap="round"/>' % (f(180 + 46 * math.cos(a)), f(112 + 46 * math.sin(a)), f(180 + 60 * math.cos(a)), f(112 + 60 * math.sin(a))))
    s.append('</g><circle cx="180" cy="112" r="34" fill="#c4ff49" fill-opacity="0.9"/></g></g>')
    s.append('<path d="M20 160H340" stroke="#fff" stroke-opacity="0.6" stroke-width="3" stroke-linecap="round"/>')
    for k, (x, ic) in enumerate(((60, 'sleep'), (300, 'train'))):
        s.append('<g class="fn-ic" style="--k:%d">%s</g>' % (k, node(x, 136, 16, ic, 0.4 + k * 0.12, WHITE if k else LIME, fill=DARK, isz=16)))
    s.append(txt(180, 190, 'Steady energy, clear plan', 13, '#fff', 0.8))
    return '\n'.join(s)

def faq_motif():
    d, pts = path(('M', 10, 30), ('C', 30, 34, 50, 44, 70, 52))
    G.travel('fq-p', pts, 6, 80, 5, rest=pts[-1], rest_opacity=0, fade=4)
    return ('<path class="dr" pathLength="1" style="--d:0.1;--dur:1s" d="%s" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round"/>' % d
            + '<path class="dr" pathLength="1" style="--d:0.3;--dur:1s" d="M10 62H32C40 62 40 84 48 84H70" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
            + '<g class="fq-p fx"><circle r="4.5" fill="#c4ff49"/></g>'
            + '<path class="dr" pathLength="1" style="--d:0.4;--dur:1.1s" d="M80 38c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="92" cy="66" r="3" fill="#fff"/>'
            + '<path class="fq-st" style="--k:0" d="M110 16v10M105 21h10" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/>')

def step_icons():
    return {
     "{{STEP1}}": '<path d="M8 12h32a2 2 0 0 1 2 2v18a2 2 0 0 1-2 2H22l-8 6v-6H8a2 2 0 0 1-2-2V14a2 2 0 0 1 2-2z"/><g class="hi-bl" style="--k:0"><circle cx="16" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="24" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="32" cy="23" r="2" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M12 6h10"/><path d="M14 6v26a3 3 0 0 0 6 0V6"/><path d="M14 20h6"/><g class="hi-gr" style="--k:0"><path d="M30 40V30M36 40V22M42 40V34" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<path d="M6 14h22M38 14h4M6 34h8M22 34h20"/><g class="hi-sl" style="--k:0"><circle cx="33" cy="14" r="4" stroke="#c4ff49"/></g><g class="hi-sl" style="--k:1"><circle cx="18" cy="34" r="4" stroke="#c4ff49"/></g>',
     "{{STEP4}}": '<path d="M6 40h36"/><path d="M8 34l9-8 7 5 14-14"/><g class="hi-ck" style="--k:0"><path d="M30 8l4 4 8-9" stroke="#c4ff49"/></g>',
    }

def hub_nodes():
    icons = ['list', 'tube', 'calendar', 'scale', 'link', 'flame', 'drop', 'coach', 'caps', 'body']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)  # half-step offset: 10 nodes, none stacked at the ends
        out.append((round(280 + 240 * math.cos(a)), round(100 + 70 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{TIMING}}": timing(), "{{WHO}}": prevalence(), "{{BIO}}": biology(), "{{VENN}}": venn(),
         "{{CMPFIG}}": compare_fig(), "{{LABS}}": labs(), "{{LEVERS}}": levers(), "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(),
         "{{HUB}}": HUB, "{{FAQMOTIF}}": faq_motif(), "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Andropause (late-onset hypogonadism) compared with menopause",
      "Andropause vs menopause", "Andropause vs menopause: what is the difference?", slots, G, published="2026-10-16")
