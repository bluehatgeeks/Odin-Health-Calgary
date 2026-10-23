"""Build /workspace/pages/weight-loss-drugs-and-testosterone/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *

SLUG = "weight-loss-drugs-and-testosterone"
TITLE = "Tirzepatide, Semaglutide and Testosterone | Odin Health Labs"
DESC = "Does tirzepatide (Mounjaro, Zepbound) or semaglutide (Ozempic, Wegovy) affect testosterone levels in men? SURMOUNT, STEP and Saxenda (liraglutide) studies."
OG_ALT = "Odin Health Labs: do tirzepatide and semaglutide raise or lower testosterone in men? What the SURMOUNT, STEP and other trials found, for men in Canada and the USA"
assert len(TITLE) <= 60 and len(DESC) <= 160, (len(TITLE), len(DESC))

FAQ = [
 ("Do GLP-1 drugs like semaglutide and tirzepatide raise or lower testosterone in men?",
  "In men with overweight or obesity, the research points up. A 2026 meta-analysis in Andrology (8 studies, 375 men) found that GLP-1 drugs significantly raised total and calculated free testosterone along with LH and FSH. A 2025 Andrology meta-analysis (7 studies, 680 men) and a 2026 Journal of Sexual Medicine review (10 studies, 639 men) also found higher total testosterone. A chart review of 110 men presented at ENDO 2025 saw average total testosterone climb from 322 to 380 ng/dL on semaglutide, dulaglutide or tirzepatide. Most studies are small, short and in men with obesity or diabetes, so we measure your own numbers before and during treatment and track the change with you."),
 ("Does tirzepatide affect testosterone levels?",
  "In men with obesity, tirzepatide (Mounjaro, Zepbound) appears to raise testosterone levels, mostly alongside the weight lost, but the big SURMOUNT trials did not measure it. Testosterone is not among the registered outcomes of SURMOUNT-1 (2,539 adults without diabetes, a 72-week trial), which reported average weight loss of 15.0 to 20.9 percent across the three doses. In a two-month controlled pilot of 83 men with obesity and low testosterone (La Vignera and colleagues, 2025), the tirzepatide group had higher total, free and bioavailable testosterone, LH and FSH than men on diet and walking alone or on testosterone gel, and lower estradiol. A 2026 review of incretin drugs including tirzepatide reported average total testosterone rises of 2.5 to 5.2 nmol/L. We check your total and free testosterone, SHBG and LH before and during treatment."),
 ("Does semaglutide (Ozempic, Wegovy) lower testosterone?",
  "Measured testosterone went up, not down, in the controlled studies so far. In a 24-week randomized trial of 25 men with type 2 diabetes, obesity and low testosterone (Gregori&ccaron; and colleagues, 2025), semaglutide 1 mg raised median total testosterone from 6.1 to 7.8 nmol/L and left LH and FSH unchanged, while testosterone injections in the comparison group lowered sperm counts. The STEP 1 trial (1,961 adults) did not measure testosterone. A US health-records study of 3,094 men aged 18 to 50 on semaglutide found more new records of testosterone deficiency (1.53 versus 0.80 percent) and erectile dysfunction than in matched men, an association that does not show the drug caused it. Free testosterone can lag when SHBG rises, so we read total, free and SHBG together."),
 ("Are there male-specific considerations with Saxenda (liraglutide) for weight management?",
  "Yes. In men, the questions are what Saxenda does to testosterone, LH, FSH and sperm, and the small studies so far point up. In a randomized 16-week trial of 30 men with obesity and low testosterone (Jensterle and colleagues, 2019), liraglutide 3.0 mg daily raised total testosterone by 2.6 nmol/L (5.9 on testosterone gel), raised LH and FSH, and took off 7.9 kg. In a four-month study of 110 men aged 18 to 35 with metabolic hypogonadism (La Vignera and colleagues, 2023), men on liraglutide 3 mg daily had higher total testosterone, SHBG, LH and FSH than men on gonadotropins or testosterone gel, with better sperm parameters and erectile function. The SCALE trial behind the 3.0 mg dose (3,731 adults) was 78.5 percent women and did not report testosterone. We check your total and free testosterone, SHBG and LH before you start and as the weight comes off."),
 ("Is the testosterone rise from the drug itself or from the weight loss?",
  "Researchers read it two ways, and both agree on the direction. The 2026 Corona meta-analysis found that the testosterone rises were independent of the weight lost, which suggests a direct effect on the hypothalamus-pituitary-testis axis. A 2026 systematic review of incretin therapies (La Vignera and Condorelli) reported rises of 2.5 to 5.2 nmol/L and concluded they were largely mediated by weight loss and better insulin sensitivity. A 2025 Andrology meta-analysis found that larger percent weight loss went with a larger testosterone rise. Either way, the practical step is the same: check your baseline, then re-check as the weight comes off."),
 ("Can fast weight loss on a GLP-1 drug cost me muscle?",
  "Some of the weight lost is lean mass, and you can plan for it. In a body-composition substudy of SURMOUNT-1 (160 adults, 73 percent women), tirzepatide cut body weight by 21.3 percent, fat mass by 33.9 percent and lean mass by 10.9 percent over a 72-week trial, and about three-quarters of the weight lost was fat and one quarter was lean mass. A 2025 joint advisory from four US obesity and nutrition societies lists muscle and bone loss among the challenges of GLP-1 treatment and recommends resistance training and an appropriate diet to preserve muscle and bone. We build your protein, strength-training, sleep and fueling plan and track how your body responds."),
 ("Why can my total testosterone rise while free testosterone barely moves?",
  "SHBG, the protein that carries testosterone in the blood, tends to rise as weight falls, and that pulls free testosterone down relative to total. In the 2026 Journal of Sexual Medicine review, free testosterone changes were inconsistent and often offset by rising SHBG. In the ENDO 2025 chart review, the authors stressed that free testosterone should be measured in men with obesity because SHBG moves with weight loss. We read total testosterone, free testosterone and SHBG together, so you see the whole picture."),
 ("Which labs should I get before and during GLP-1 treatment?",
  'A useful panel covers total and free testosterone, SHBG, LH, FSH and estradiol, along with metabolic markers such as A1c. LH and FSH show whether the brain&rsquo;s signal to the testes is staying on, and SHBG explains gaps between total and free testosterone. Many men repeat the panel after meaningful weight change. Our <a href="%s/low-testosterone-labs-to-ask-for">lab guide</a> explains each result in plain language, and we review your numbers with you.' % SITE),
 ("How does Odin Health Labs work with my doctor?",
  'Odin Health Labs is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We work alongside whoever prescribes your GLP-1 medication: we review your labs with you, build your muscle-protection, sleep and nutrition plan, and track your progress. We can share your plan and results with your own doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()
def drb(d, delay, dur, stroke, sw):
    return dr(d, delay, dur, stroke, sw).replace('stroke-linecap="round"', 'stroke-linecap="butt"')

# ---------- 1 · HERO: a balance beam tips as weight falls and testosterone rises; three supports feed the pivot ----------
def hero_conv():
    s = ['<defs><radialGradient id="wl-g" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.16"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="228" ry="148" fill="url(#wl-g)"/>']
    sup = [(96, 288, 'labs', WHITE), (240, 294, 'food', LIME), (384, 288, 'train', WHITE)]
    for i, (x, y, ic, col) in enumerate(sup):
        d, pts = path(('M', x, y - 24), ('L', 240, 246))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>' % d)
        s.append(dr(d, 0.5 + i * 0.12, 1.0, 'rgba(196,255,73,0.45)', 2.4))
        s.append(dot('hw-p%d fx' % i, 5, LIME if i % 2 else WHITE))
        G.travel('hw-p%d' % i, pts, 8, 80, 7, delay='%ss' % f(-i * 2.3), rest=pts[0], rest_opacity=0, fade=3)
    s.append('<g class="pop t" style="--d:0.2"><path d="M240 200L216 244H264Z" fill="#142e14" stroke="#c4ff49" stroke-width="3" stroke-linejoin="round"/></g>')
    beam = ['<path d="M60 196H420" stroke="#fff" stroke-width="5" stroke-linecap="round"/>', '<path d="M100 196V168M380 196V168" stroke="rgba(255,255,255,0.5)" stroke-width="2.4" stroke-linecap="round"/>']
    beam.append(node(100, 138, 30, 'scale', 0.3, WHITE, isz=32))
    beam.append(node(380, 138, 30, 'drop', 0.42, LIME, fill='#142e14', isz=32))
    s.append('<g class="hw-bm">' + ''.join(beam) + '</g>')
    s.append('<circle cx="240" cy="196" r="9" fill="#142e14" stroke="#c4ff49" stroke-width="3"/>')
    s.append('<text x="100" y="86" font-size="14" fill="#fff" fill-opacity="0.85" text-anchor="middle">Weight</text><text x="380" y="86" font-size="14" fill="#c4ff49" fill-opacity="0.95" text-anchor="middle">Testosterone</text>')
    for i, (x, y, ic, col) in enumerate(sup):
        s.append(node(x, y, 22, ic, 0.5 + i * 0.12, col, fill='#142e14' if col == LIME else DARK, isz=24))
    return '\n'.join(s)

# ---------- 2 · RESEARCH: men included in each review, bars drawn to scale ----------
def research():
    rows = [('Orra 2025', 219, 'Bioavailable T up'), ('Corona 2026', 375, 'Total + free T up'), ('Deameh 2026', 639, 'Total T up'), ('Salvio 2025', 680, 'Total T up')]
    scale = 320 / 680.0
    s = ['<path d="M150 20V220" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round"/>']
    for k, (lab, n, res) in enumerate(rows):
        y = 28 + k * 50
        w = n * scale
        s.append('<g class="pop t" style="--d:%s"><rect x="150" y="%d" width="%s" height="34" rx="9" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.22)" stroke-width="1.6"/></g>' % (0.1 + k * 0.12, y, f(w)))
        s.append('<rect class="rs-bar" style="--k:%d" x="150" y="%d" width="%s" height="34" rx="9" fill="%s" fill-opacity="%s"/>' % (k, y, f(w), LIME if k % 2 else 'rgba(255,255,255,0.8)', '0.85' if k % 2 else '0.5'))
        s.append('<text x="138" y="%d" font-size="15" fill="#fff" text-anchor="end">%s</text>' % (y + 22, lab))
        s.append('<text x="%s" y="%d" font-size="15" fill="#fff" fill-opacity="0.95">%d men</text>' % (f(150 + w + 10), y + 22, n))
        s.append('<g class="rs-up" style="--k:%d"><path d="M164 %d v-12M164 %d l-5 7M164 %d l5 7" transform="translate(0 0)" stroke="%s" stroke-width="2.6" stroke-linecap="round" fill="none"/></g>' % (k, y + 26, y + 14, y + 14, '#0f240f' if k % 2 else '#fff'))
    return '\n'.join(s)

# ---------- 2b · TRIALS: a lens checks the two big trials (testosterone not measured), then four smaller studies light up ----------
def trials():
    s = []
    big = [(150, 'SURMOUNT-1', 'tirzepatide'), (410, 'STEP 1', 'semaglutide')]
    for i, (x, lab, drug) in enumerate(big):
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="34" width="200" height="72" rx="14" fill="#142e14" stroke="rgba(255,255,255,0.45)" stroke-width="2"/></g>' % (f(0.1 + i * 0.12), x - 100))
        s.append('<text x="%d" y="60" font-size="15" fill="#fff" text-anchor="middle">%s</text><text x="%d" y="80" font-size="12" fill="#fff" fill-opacity="0.7" text-anchor="middle">%s</text>' % (x - 24, lab, x - 24, drug))
        s.append('<g class="tr-q" style="--k:%d"><circle cx="%d" cy="70" r="17" fill="none" stroke="#c4ff49" stroke-opacity="0.8" stroke-width="2" stroke-dasharray="4 4"/><text x="%d" y="76" font-size="16" fill="#c4ff49" text-anchor="middle">T?</text></g>' % (i, x + 62, x + 62))
    s.append('<text x="280" y="128" font-size="12" fill="#fff" fill-opacity="0.75" text-anchor="middle">Big weight-loss trials: testosterone not measured</text>')
    small = [(80, 'Tirzepatide', 'T up', True), (213, 'Semaglutide', 'T up', True), (347, 'Liraglutide', 'T up', True), (480, 'Dulaglutide', 'No change', False)]
    for k, (x, lab, res, up) in enumerate(small):
        s.append('<g class="tr-hit" style="--k:%d"><circle cx="%d" cy="178" r="22" fill="%s" stroke="%s" stroke-width="2.4"/></g>' % (k, x, '#142e14' if up else DARK, LIME if up else 'rgba(255,255,255,0.7)'))
        if up:
            s.append('<g class="tr-ar" style="--k:%d"><path d="M%d 188v-20M%d 168l-6 7M%d 168l6 7" stroke="#c4ff49" stroke-width="2.6" stroke-linecap="round" fill="none"/></g>' % (k, x, x, x))
        else:
            s.append('<path d="M%d 174h14M%d 182h14" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>' % (x - 7, x - 7))
        s.append('<text x="%d" y="220" font-size="12" fill="#fff" fill-opacity="0.9" text-anchor="middle">%s</text><text x="%d" y="236" font-size="12" fill="%s" text-anchor="middle">%s</text>' % (x, lab, x, '#c4ff49' if up else '#fff', res))
    d, pts = path(('M', 212, 70), ('L', 472, 70), ('C', 520, 110, 520, 150, 480, 178), ('L', 80, 178), n=10)
    s.append('<path d="M212 70H472" stroke="rgba(255,255,255,0.12)" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>')
    s.append('<path d="M80 178H480" stroke="rgba(196,255,73,0.18)" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>')
    s.append('<g class="tr-lens fx"><circle r="13" fill="rgba(196,255,73,0.12)" stroke="#fff" stroke-width="2.4"/><path d="M9 9l9 9" stroke="#fff" stroke-width="3" stroke-linecap="round"/></g>')
    G.travel('tr-lens', pts, 4, 92, 12, rest=pts[-1], rest_opacity=0, fade=3, ease='ease-in-out')
    return '\n'.join(s)

# ---------- 3 · WHY: two routes (weight loss, a possible direct signal) merge into one rising result ----------
def why():
    a = path(('M', 100, 70), ('C', 220, 70, 280, 118, 410, 122), n=22)
    b = path(('M', 100, 180), ('C', 220, 180, 280, 130, 410, 126), n=22)
    c = path(('M', 410, 124), ('L', 468, 124), n=4)
    s = ['<circle class="wy-ring fx" cx="500" cy="124" r="32" fill="none" stroke="#c4ff49" stroke-width="2"/>']
    s.append('<path d="%s" stroke="rgba(255,255,255,0.14)" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>' % a[0])
    s.append('<path d="%s" stroke="rgba(196,255,73,0.2)" stroke-width="3" stroke-dasharray="6 8" stroke-linecap="round" fill="none"/>' % b[0])
    s.append(dr(a[0], 0.4, 1.4, 'rgba(255,255,255,0.75)', 3.2)); s.append(dr(b[0], 0.55, 1.4, LIME, 3.2))
    s.append(dr(c[0], 1.4, 0.5, LIME, 3.6))
    s.append(dot('wy-a', 6.5, WHITE, ring=True)); G.travel('wy-a', a[1] + c[1], 6, 46, 9, rest=c[1][-1], fade=2.5)
    s.append(dot('wy-b', 6.5, LIME, ring=True)); G.travel('wy-b', b[1] + c[1], 52, 94, 9, rest=c[1][-1], fade=2.5)
    s.append('<circle cx="410" cy="124" r="6" fill="#142e14" stroke="#c4ff49" stroke-width="2.4"/>')
    s.append(node(70, 70, 30, 'scale', 0.1, WHITE, isz=32))
    s.append(node(70, 180, 30, 'brain', 0.25, LIME, fill='#142e14', isz=34))
    s.append(node(500, 124, 30, 'drop', 0.7, LIME, fill='#142e14', isz=32))
    s.append('<text x="70" y="124" font-size="14" fill="#fff" fill-opacity="0.85" text-anchor="middle">Weight loss</text>')
    s.append('<text x="70" y="234" font-size="14" fill="#c4ff49" fill-opacity="0.95" text-anchor="middle">Direct signal</text>')
    s.append('<text x="500" y="176" font-size="14" fill="#fff" fill-opacity="0.85" text-anchor="middle">Higher T</text>')
    return '\n'.join(s)

# ---------- 4 · NUMBERS: a ruler in ng/dL, a ball hops from the 322 average to the 380 average ----------
def numbers():
    X = lambda v: 40 + (v - 200) / 250.0 * 480
    y0 = 150
    s = ['<g class="pop t" style="--d:0.1"><rect x="40" y="%d" width="%s" height="60" fill="rgba(255,255,255,0.05)"/><rect x="%s" y="%d" width="%s" height="60" fill="rgba(196,255,73,0.08)"/></g>' % (y0 - 30, f(X(300) - 40), f(X(300)), y0 - 30, f(520 - X(300)))]
    s.append('<path d="M40 150H520" stroke="rgba(255,255,255,0.35)" stroke-width="3" stroke-linecap="round"/>')
    for v in (200, 250, 300, 350, 400, 450):
        s.append('<path d="M%s %d v10" stroke="rgba(255,255,255,0.5)" stroke-width="2.4" stroke-linecap="round"/><text x="%s" y="%d" font-size="13" fill="#fff" fill-opacity="0.75" text-anchor="middle">%d</text>' % (f(X(v)), y0 + 4, f(X(v)), y0 + 38, v))
    s.append('<path d="M%s 84V%d" stroke="#c4ff49" stroke-width="2.4" stroke-dasharray="4 5" stroke-linecap="round"/>' % (f(X(300)), y0 + 6))
    s.append('<text x="%s" y="76" font-size="14" fill="#c4ff49" text-anchor="middle">300</text>' % f(X(300)))
    x1, x2 = X(322), X(380)
    s.append('<circle cx="%s" cy="%d" r="7" fill="#142e14" stroke="#fff" stroke-width="2.4"/>' % (f(x1), y0))
    s.append('<circle cx="%s" cy="%d" r="7" fill="#142e14" stroke="#c4ff49" stroke-width="2.4"/>' % (f(x2), y0))
    s.append('<text x="%s" y="%d" font-size="16" fill="#fff" text-anchor="middle">322</text><text x="%s" y="%d" font-size="16" fill="#c4ff49" text-anchor="middle">380</text>' % (f(x1), y0 - 40, f(x2), y0 - 40))
    hop, pts = path(('M', x1, y0), ('C', x1 + 20, y0 - 62, x2 - 20, y0 - 62, x2, y0), n=18)
    s.append(dr(hop, 0.5, 1.4, 'rgba(196,255,73,0.5)', 2.4))
    s.append(dot('nm-p', 8, LIME, ring=True)); G.travel('nm-p', pts, 8, 58, 8, rest=pts[-1], fade=2.5)
    s.append('<text x="280" y="232" font-size="13" fill="#fff" fill-opacity="0.7" text-anchor="middle">Average total testosterone, ng/dL</text>')
    s.append(node(500, 60, 20, 'drop', 0.5, LIME, fill='#142e14', isz=22))
    return '\n'.join(s)

# ---------- 5 · MUSCLE: a ring split into the share of weight lost as fat and as lean mass ----------
def muscle():
    cx, cy, r = 280, 118, 70
    s = ['<circle cx="%d" cy="%d" r="%d" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="26"/>' % (cx, cy, r)]
    fat = 'M%d %dA%d %d 0 1 1 %d %d' % (cx, cy - r, r, r, cx - r, cy)
    lean = 'M%d %dA%d %d 0 0 1 %d %d' % (cx - r, cy, r, r, cx, cy - r)
    s.append(drb(fat, 0.3, 1.5, LIME, 26))
    s.append('<g class="ms-lean">' + drb(lean, 0.9, 0.8, 'rgba(255,255,255,0.88)', 26) + '</g>')
    s.append(node(cx, cy, 30, 'train', 0.6, WHITE, fill='#142e14', isz=32))
    s.append('<path d="M%d %dL%d %d" stroke="rgba(255,255,255,0.35)" stroke-width="2" stroke-linecap="round"/>' % (cx - 56, cy - 56, 226, 52))
    s.append('<text x="222" y="40" font-size="15" fill="#fff" text-anchor="end">About 25 percent lean mass</text>')
    s.append('<path d="M%d %dL%d %d" stroke="rgba(196,255,73,0.5)" stroke-width="2" stroke-linecap="round"/>' % (cx + 62, cy + 40, 380, cy + 76))
    s.append('<text x="386" y="%d" font-size="15" fill="#c4ff49" text-anchor="start">About 75 percent fat</text>' % (cy + 82))
    s.append('<text x="280" y="236" font-size="13" fill="#fff" fill-opacity="0.7" text-anchor="middle">Share of weight lost on tirzepatide (SURMOUNT-1 DXA substudy)</text>')
    return '\n'.join(s)

# ---------- 6 · LABS: total testosterone grows, SHBG holds some of it, free stays the readable slice ----------
def labs():
    s = []
    def row(y, n, free_idx, extra_from, label, base_d):
        out = ['<text x="30" y="%d" font-size="14" fill="#fff" fill-opacity="0.85">%s</text>' % (y - 28, label)]
        for i in range(n):
            x = 50 + i * 40
            is_free = i in free_idx
            cls = 'sb-x' if (extra_from is not None and i >= extra_from) else ''
            out.append('<g class="pop t" style="--d:%s"><g class="%s" style="--k:%d"><circle cx="%d" cy="%d" r="13" fill="%s" fill-opacity="%s" stroke="%s" stroke-width="2.2"/></g></g>' % (f(base_d + i * 0.06), cls, i - (extra_from or 0), x, y, LIME if is_free else '#fff', '0.9' if is_free else '0.28', LIME if is_free else 'rgba(255,255,255,0.7)'))
        return '\n'.join(out)
    s.append(row(70, 8, {1}, None, 'Before: total testosterone', 0.1))
    s.append(row(170, 10, {1}, 8, 'During weight loss: total testosterone', 0.3))
    s.append('<path d="M336 70L474 108M436 170L486 138" stroke="rgba(255,255,255,0.25)" stroke-width="2.4" stroke-dasharray="2 7" stroke-linecap="round" fill="none"/>')
    s.append(node(500, 122, 24, 'link', 0.5, WHITE, isz=26))
    s.append('<text x="500" y="166" font-size="13" fill="#fff" fill-opacity="0.85" text-anchor="middle">SHBG</text>')
    s.append('<text x="30" y="226" font-size="13" fill="#fff" fill-opacity="0.7">Bright dots: free, usable testosterone</text>')
    return '\n'.join(s)

# ---------- final: four rising steps, a ball climbs them, a flag waves at the top ----------
def final():
    s = ['<path d="M24 170H336" stroke="rgba(255,255,255,0.55)" stroke-width="3.4" stroke-linecap="round"/>']
    for k in range(4):
        x = 40 + k * 70; h = (k + 1) * 28
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="%d" width="64" height="%d" rx="8" fill="%s" stroke="%s" stroke-width="2.4"/></g>' % (0.1 + k * 0.12, x, 170 - h, h, '#142e14' if k % 2 == 0 else '#173617', LIME if k == 3 else 'rgba(255,255,255,0.5)'))
    # ball rides the step tops with small hops
    tops = [(72, 170 - 28 - 10), (142, 170 - 56 - 10), (212, 170 - 84 - 10), (282, 170 - 112 - 10)]
    sg = [('M', tops[0][0], tops[0][1])]
    for i in range(1, 4):
        px, py = tops[i - 1]; qx, qy = tops[i]
        sg.append(('C', px + 24, py - 30, qx - 24, qy - 30, qx, qy))
    d, p = path(*sg, n=10)
    s.append(dot('fn-p', 8, LIME, ring=True)); G.travel('fn-p', p, 8, 82, 8, rest=p[-1], fade=3)
    s.append('<path d="M282 58V20" stroke="#fff" stroke-width="3" stroke-linecap="round"/><g class="fn-fl"><path d="M282 20h26l-6 8 6 8h-26z" fill="#c4ff49" fill-opacity="0.9"/></g>')
    s.append(node(48, 110, 22, 'labs', 0.4, WHITE, isz=24))
    s.append(node(140, 62, 20, 'train', 0.5, LIME, fill='#142e14', isz=22))
    return '\n'.join(s)

FAQMOTIF = '''<g class="fq-dr"><path d="M30 20c9 12 15 20 15 28a15 15 0 0 1-30 0c0-8 6-16 15-28z" fill="#c4ff49" fill-opacity="0.85"/></g>
<path class="dr" pathLength="1" style="--d:0.2;--dur:1.1s" d="M70 38c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82" cy="66" r="3" fill="#fff"/>
<path class="fq-st" style="--k:0" d="M104 20v10M99 25h10" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/>'''

def step_icons():
    return {
     "{{STEP1}}": '<path d="M18 6v22a6 6 0 0 0 12 0V6"/><path d="M14 6h20"/><g class="hi-gr" style="--k:0"><rect x="20.5" y="22" width="7" height="12" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:0"><circle cx="38" cy="30" r="2.8" fill="#fff" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="10" cy="22" r="2.8" fill="#fff" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M14 24h20"/><g class="hi-pu" style="--k:0"><path d="M10 14v20M5 19v10" stroke="#c4ff49"/></g><g class="hi-pu" style="--k:1"><path d="M38 14v20M43 19v10" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<path d="M5 28h9l4-10 8 20 4-10h13"/><g class="hi-ck" style="--k:0"><path d="M30 12l5 5 9-11" stroke="#fff"/></g>',
     "{{STEP4}}": '<path d="M12 42V10"/><g class="hi-sw" style="--k:0"><path d="M12 10h22l6 6-6 6H12z" fill="rgba(196,255,73,0.22)"/></g><path d="M8 42h12"/>',
    }

HUB = hub(G, [(110, 52, 'tube'), (110, 148, 'scale'), (450, 52, 'drop'), (450, 148, 'coach'), (230, 28, 'caps'), (330, 172, 'labs'), (330, 28, 'shield')])
slots = {"{{HERO}}": hero_conv(), "{{RESEARCH}}": research(), "{{TRIALS}}": trials(), "{{WHY}}": why(), "{{NUMBERS}}": numbers(), "{{MUSCLE}}": muscle(), "{{LABS}}": labs(),
         "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB, "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Tirzepatide, semaglutide and other GLP-1 drugs and testosterone in men",
      "GLP-1 drugs and testosterone", "Do GLP-1 drugs like tirzepatide and semaglutide raise or lower testosterone in men?", slots, G, modified="2026-10-23")
