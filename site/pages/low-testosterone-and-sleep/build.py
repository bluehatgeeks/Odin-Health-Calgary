"""Build /workspace/pages/low-testosterone-and-sleep/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match. build() output is minified at the end (HighLevel save limit)."""
import sys, os, math, re, json, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "low-testosterone-and-sleep"
TITLE = "Low Testosterone, Insomnia and Poor Sleep | Odin Health Lab"
DESC = "Can low testosterone cause insomnia or poor sleep? What studies show on sleep, sleep apnea and testosterone, if TRT helps sleep, and what men can do."
OG_ALT = "Odin Health Lab: low testosterone and insomnia, how sleep affects testosterone in men, sleep apnea, shift work and morning testing"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 155, (len(TITLE), len(DESC))

common.ICONS.update({
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "bed": '<path d="M3 18V7"/><path d="M3 14h18v4"/><path d="M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.8"/>',
 "cup": '<path d="M5 9h11v5a5 5 0 0 1-10 0z"/><path d="M16 10h1.5a2.5 2.5 0 0 1 0 5H16"/><path d="M8 3c0 1.5 1 1.5 1 3M12 3c0 1.5 1 1.5 1 3"/>',
 "screen": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 "split": '<path d="M4 7c4 0 8 2 16 6"/><path d="M4 7h7c2 0 2 10 4 10h5"/>',
})

FAQ = [
 ("Does low testosterone cause insomnia?",
  "Not on its own, as far as the research shows. In a 2008 study of 1,312 men aged 65 and older, men with lower testosterone slept less efficiently, woke more often in the night and had less deep sleep, but most of that link was explained by body fat. In a 2015 study of 1,274 men over 65, insomnia complaints and taking a long time to fall asleep were not linked with testosterone at all. A 2024 US health-records study found testosterone deficiency was more common in men with insomnia, which shows the two travel together, not which causes which. The better-proven direction runs the other way: short, broken sleep lowers testosterone. So we start with your sleep, your weight and the signs of sleep apnea, alongside two morning labs."),
 ("Will testosterone therapy help me sleep?",
  "The evidence is mixed, and it is not a proven fix for insomnia. In a Japanese trial of 48 men with low testosterone and sleep problems but no sleep apnea (the EARTH study, 2018), a year of testosterone therapy improved sleep-disturbance scores compared with no treatment. But in 17 healthy men over 60, short-term high-dose testosterone cut sleep by about an hour and made breathing during sleep worse (2003), and in 67 men with obesity and severe sleep apnea, testosterone worsened night-time oxygen drops early in treatment, an effect that faded by the end of the trial (2012). The Endocrine Society advises against starting testosterone therapy while severe sleep apnea is untreated. That is why checking for apnea and fixing the sleep itself come first; we build that plan with you and track it with repeat labs."),
 ("Does poor sleep lower testosterone?",
  "It can. In a University of Chicago study published in JAMA in 2011, 10 healthy young men spent about a week in bed only five hours a night. Their daytime testosterone fell from an average of 18.4 to 16.5 nmol/L, a drop of 10 to 15 percent, and their sense of vigour fell night by night. In older men, a 2007 study in the journal Sleep found that men who slept less at night had lower morning testosterone. The Canadian Urological Association (2021) notes that a structured sleep program may offset the effect of limited sleep. We build that sleep plan with you and re-check your labs to see the change."),
 ("Can sleep apnea cause low testosterone?",
  "Sleep apnea and low testosterone often show up together, and extra body weight is the main link. A 2014 review in the Asian Journal of Andrology found that obstructive sleep apnea had no direct effect on testosterone once age and weight were accounted for, while weight loss raised testosterone in proportion to the weight lost. A 2019 meta-analysis of 12 studies with 388 men found CPAP on its own did not significantly change testosterone. Loud snoring, gasping at night and daytime sleepiness are worth a sleep study, and the Endocrine Society advises against starting testosterone therapy while severe sleep apnea is untreated. We help you map those signs and build the weight, training and sleep plan."),
 ("Can low testosterone cause poor sleep?",
  "The link can run both ways. The same 2014 review notes that low testosterone may affect overall sleep quality. And many symptoms blamed on low T, such as low energy, lower sex drive, poor concentration and daytime sleepiness, can also come from sleep loss alone, as the JAMA study authors point out. That overlap is why we look at your sleep and your labs together before deciding what is driving your symptoms."),
 ("I work nights. When should I get my testosterone tested?",
  'Guidelines ask for an early-morning, fasting draw because testosterone peaks in the morning. In a 2005 study of seven young men, testosterone rose during sleep and fell while awake, and it rose during daytime sleep much as it did at night. So for shift workers, the timing of your main sleep matters for reading the result: tell whoever orders your labs about your rotation and test on a stable stretch. In a 2020 study of 2,571 men at an andrology clinic, shift workers with shift work sleep disorder had lower testosterone and more low-T symptoms. See our <a href="%s/shift">shift work page</a>.' % SITE),
 ("How much sleep should men aim for?",
  "The US National Heart, Lung, and Blood Institute says adults need 7 to 9 hours a night. Its tips: keep the same bed and wake times every day, use the hour before bed for quiet time away from bright screens, avoid heavy meals and alcohol close to bedtime, keep caffeine and nicotine away from the evening, get outside and be active during the day, and keep your bedroom quiet, cool and dark. We turn those into a routine that fits your work and family week."),
 ("How does Odin Health Lab work with my doctor?",
  'Odin Health Lab is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We work alongside your own doctor: we go through your sleep, symptoms and lab results with you, build your sleep, training, nutrition and stress plan, and track your progress with follow-up check-ins and repeat labs. If your answers point to sleep apnea, we flag it so you can raise a sleep study with your doctor. We can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

def txt(x, y, s, size=13, fill='#fff', op=0.85, anchor='middle', extra=''):
    return '<text x="%s" y="%s" font-size="%s" fill="%s" fill-opacity="%s" text-anchor="%s"%s>%s</text>' % (f(x), f(y), size, fill, op, anchor, extra, s)

def stars(pts, cls='sl-st'):
    return ''.join('<g class="%s" style="--k:%d"><path d="M%s %sv8M%s %sh8" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/></g>' % (cls, k, f(x), f(y - 4), f(x - 4), f(y)) for k, (x, y) in enumerate(pts))

def hero():
    s = ['<defs><radialGradient id="sl-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.14"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="170" rx="220" ry="130" fill="url(#sl-g)"/>']
    s.append('<rect x="40" y="70" width="200" height="180" rx="14" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.18)" stroke-width="1.6"/>')
    s.append(txt(140, 96, 'Asleep', 13, '#c4ff49', 0.95)); s.append(txt(340, 96, 'Awake', 13, '#fff', 0.8))
    s.append('<path d="M40 250H440" stroke="rgba(255,255,255,0.3)" stroke-width="2"/>')
    d, pts = path(('M', 40, 232), ('C', 120, 226, 180, 120, 240, 120), ('C', 300, 120, 380, 196, 440, 214), n=18)
    s.append('<path d="%s" stroke="rgba(255,255,255,0.12)" stroke-width="2.4" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>' % d)
    s.append(dr(d, 0.25, 1.8, LIME, 3))
    s.append(dot('hr-o fx', 6, LIME, ring=True)); G.travel('hr-o', pts, 4, 90, 10, rest=pts[0], rest_opacity=0, fade=2)
    s.append('<circle class="hr-ring fx" cx="240" cy="120" r="16" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append('<g class="hr-moon">%s</g>' % ico('sleep', 78, 40, 34, LIME, 1.8))
    s.append('<g class="hr-sun">%s</g>' % ico('sun', 404, 40, 34, WHITE, 1.8))
    s.append(stars(((130, 34), (176, 52), (210, 28))))
    s.append(txt(240, 286, 'Testosterone climbs in sleep, drifts down awake', 13, '#fff', 0.85))
    return '\n'.join(s)

def insomnia():
    """Two-way loop: poor sleep -> lower T (lime arc) and lower T -> poorer sleep (white arc), extra weight pulsing at the centre;
    below, one night (11 p.m. to 7 a.m.) broken by wake-ups that blink in turn."""
    s = []
    A, B, C = (90, 100), (470, 100), (280, 100)
    d1, p1 = path(('M', 122, 86), ('C', 190, 18, 370, 18, 438, 86), n=18)
    d2, p2 = path(('M', 438, 114), ('C', 370, 182, 190, 182, 122, 114), n=18)
    s.append('<path d="%s" stroke="rgba(196,255,73,0.18)" stroke-width="3" fill="none" stroke-linecap="round"/>' % d1)
    s.append(dr(d1, 0.3, 1.2, LIME, 3))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.22)" stroke-width="2.4" stroke-dasharray="4 7" fill="none" stroke-linecap="round"/>' % d2)
    s.append('<path d="M430 74l10 12-15 3" stroke="#c4ff49" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append('<path d="M130 126l-10-12 15-3" stroke="#fff" stroke-opacity="0.6" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(dot('in-a fx', 5.5, LIME, ring=True)); G.travel('in-a', p1, 4, 46, 8, rest=p1[-1], rest_opacity=0, fade=3)
    s.append(dot('in-b fx', 4.5, WHITE)); G.travel('in-b', p2, 54, 92, 8, rest=p2[-1], rest_opacity=0, fade=3)
    s.append(txt(280, 30, 'Short, broken sleep lowers T', 12, '#c4ff49', 0.95))
    s.append(txt(280, 178, 'Low T: poorer sleep (link mostly via weight)', 12, '#fff', 0.75))
    s.append('<circle class="in-ring fx" cx="280" cy="100" r="30" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(node(280, 100, 24, 'scale', 0.5, WHITE, dashed=True, isz=24))
    s.append(node(A[0], A[1], 30, 'sleep', 0.2, LIME, fill='#142e14', isz=30)); s.append(txt(A[0], A[1] + 50, 'Poor sleep', 13, '#c4ff49', 0.95))
    s.append(node(B[0], B[1], 30, 'gauge', 0.35, WHITE, isz=30)); s.append(txt(B[0], B[1] + 50, 'Lower T', 13))
    # one night, fragmented
    y = 214
    s.append('<path d="M60 %dH500" stroke="rgba(255,255,255,0.18)" stroke-width="14" stroke-linecap="round"/>' % y)
    segs = [(60, 150), (166, 262), (280, 360), (378, 500)]
    for k, (x1, x2) in enumerate(segs):
        s.append('<rect class="in-sl" style="--k:%d" x="%d" y="%d" width="%d" height="14" rx="7" fill="#c4ff49" fill-opacity="0.7"/>' % (k, x1, y - 7, x2 - x1))
    for k, x in enumerate((158, 271, 369)):
        s.append('<g class="in-wk" style="--k:%d"><circle cx="%d" cy="%d" r="9" fill="#0f240f" stroke="#fff" stroke-width="2"/><path d="M%d %dv-4" stroke="#fff" stroke-width="2" stroke-linecap="round"/></g>' % (k, x, y, x, y + 2))
    s.append(txt(60, 246, '11 p.m.', 11, '#fff', 0.65, 'start')); s.append(txt(500, 246, '7 a.m.', 11, '#fff', 0.65, 'end'))
    s.append(txt(280, 250, 'Wake-ups break up the night', 12, '#fff', 0.85))
    return '\n'.join(s)

def overnight():
    s = []
    s.append(txt(40, 34, 'Testosterone', 12, '#c4ff49', 0.95, 'start'))
    d, pts = path(('M', 40, 120), ('C', 120, 118, 150, 70, 230, 60), ('C', 330, 50, 420, 46, 520, 44), n=16)
    s.append(dr(d, 0.2, 1.6, LIME, 3))
    s.append(dot('ov-o fx', 5, LIME, ring=True)); G.travel('ov-o', pts, 6, 86, 9, rest=pts[-1], rest_opacity=0, fade=3)
    # hypnogram: stepped sleep stages with REM blocks
    hyp = 'M40 150H70V200H110V230H150V180H190V158H230V200H270V226H300V170H340V156H390V196H430V168H470V154H520'
    s.append('<path d="M40 248H520" stroke="rgba(255,255,255,0.25)" stroke-width="1.6"/>')
    s.append(dr(hyp, 0.4, 2.0, 'rgba(255,255,255,0.7)', 2.2))
    for k, (x1, x2) in enumerate(((190, 230), (340, 390), (470, 520))):
        s.append('<rect class="ov-rem" style="--k:%d" x="%d" y="150" width="%d" height="12" rx="4" fill="#c4ff49" fill-opacity="0.75"/>' % (k, x1, x2 - x1))
    s.append(txt(40, 272, 'Sleep stages (lime = REM)', 12, '#fff', 0.75, 'start'))
    s.append('<g class="ov-scan"><path d="M40 30V250" stroke="#c4ff49" stroke-opacity="0.5" stroke-width="1.6" stroke-dasharray="3 5"/></g>')
    s.append(txt(520, 272, 'The rise needs 3+ hours of sleep', 12, '#c4ff49', 0.9, 'end'))
    return '\n'.join(s)

def shortsleep():
    s = []
    base = 220; scale = 8.2  # px per nmol/L
    for k, (x, v, lab, col, sub) in enumerate(((150, 18.4, 'Rested', LIME, '10 h in bed'), (330, 16.5, 'Short sleep', WHITE, '5 h in bed'))):
        h = v * scale
        s.append('<g class="ss-bar" style="--k:%d"><rect x="%d" y="%s" width="80" height="%s" rx="10" fill="%s" fill-opacity="%s"/></g>' % (k, x - 40, f(base - h), f(h), col, '0.85' if k == 0 else '0.55'))
        s.append(txt(x, base - h - 12, '%s' % v, 16, '#c4ff49' if k == 0 else '#fff', 0.95))
        s.append(txt(x, base + 22, lab, 13, '#c4ff49' if k == 0 else '#fff', 0.9))
        s.append(txt(x, base + 40, sub, 11, '#fff', 0.65))
    s.append('<path d="M60 220H420" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>')
    s.append(txt(240, 30, 'Daytime testosterone, nmol/L', 12, '#fff', 0.75))
    # vigour battery
    s.append('<rect x="452" y="70" width="64" height="120" rx="10" fill="none" stroke="#fff" stroke-opacity="0.7" stroke-width="2.4"/><rect x="472" y="60" width="24" height="10" rx="3" fill="#fff" fill-opacity="0.7"/>')
    s.append('<rect class="ss-vig" x="460" y="78" width="48" height="104" rx="6" fill="#c4ff49" fill-opacity="0.85"/>')
    s.append(txt(484, 214, 'Vigour', 12, '#c4ff49', 0.95)); s.append(txt(484, 232, 'falls night', 11, '#fff', 0.65)); s.append(txt(484, 246, 'by night', 11, '#fff', 0.65))
    d, pts = path(('M', 240, 120), ('L', 290, 120))
    s.append('<path d="M240 120H290" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-dasharray="2 5"/>')
    s.append(dot('ss-p fx', 4.5, WHITE)); G.travel('ss-p', pts, 10, 70, 4, rest=pts[-1], rest_opacity=0, fade=3)
    return '\n'.join(s)

def apnea():
    s = []
    tri = [(110, 70, 'wind', 'Sleep apnea'), (450, 70, 'scale', 'Extra weight'), (280, 190, 'gauge', 'Lower T')]
    edges = [(1, 0), (1, 2), (0, 2)]
    for k, (a, b) in enumerate(edges):
        A, B = tri[a], tri[b]
        d, pts = path(('M', A[0], A[1]), ('L', B[0], B[1]))
        dashed = (a, b) == (0, 2)
        s.append('<path d="%s" stroke="%s" stroke-width="2.2" stroke-dasharray="%s" fill="none"/>' % (d, 'rgba(255,255,255,0.18)' if dashed else 'rgba(196,255,73,0.35)', '3 7' if dashed else '2 6'))
        s.append(dot('ap-p%d fx' % k, 5, WHITE if dashed else LIME))
        G.travel('ap-p%d' % k, pts, 8, 60, 6, delay='%ss' % f(-k * 2), rest=pts[0], rest_opacity=0, fade=3)
    for i, (x, y, ic, lab) in enumerate(tri):
        s.append(node(x, y, 30, ic, 0.15 + i * 0.12, LIME if i == 1 else WHITE, fill='#142e14' if i == 1 else DARK, isz=30))
        s.append(txt(x, y + (50 if i < 2 else 50), lab, 13, '#c4ff49' if i == 1 else '#fff', 0.9))
    s.append('<circle class="ap-ring fx" cx="450" cy="70" r="38" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    # breathing wave with a pause
    wave = 'M40 268c10-14 20-14 30 0s20 14 30 0 20-14 30 0H190c10-18 20-18 30 0s20 14 30 0 20-14 30 0'
    s.append('<g class="ap-wave">%s</g>' % dr(wave, 0.5, 1.6, 'rgba(255,255,255,0.75)', 2.4))
    s.append('<g class="ap-pause"><rect x="134" y="256" width="52" height="24" rx="8" fill="none" stroke="#c4ff49" stroke-width="1.6" stroke-dasharray="3 4"/></g>')
    s.append(txt(160, 300, 'Breathing pauses', 11, '#c4ff49', 0.9))
    s.append(txt(450, 280, 'Weight is the main link', 13, '#c4ff49', 0.95))
    return '\n'.join(s)

def shiftfig():
    s = []
    cx, cy, r = 120, 135, 82
    s.append('<circle cx="%d" cy="%d" r="%d" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>' % (cx, cy, r))
    for h in range(0, 24, 3):
        a = -math.pi / 2 + h / 24 * 2 * math.pi
        s.append('<path d="M%s %sL%s %s" stroke="rgba(255,255,255,0.4)" stroke-width="2" stroke-linecap="round"/>' % (f(cx + (r - 8) * math.cos(a)), f(cy + (r - 8) * math.sin(a)), f(cx + r * math.cos(a)), f(cy + r * math.sin(a))))
    def arc(h1, h2, rr):
        a1 = -math.pi / 2 + h1 / 24 * 2 * math.pi; a2 = -math.pi / 2 + h2 / 24 * 2 * math.pi
        return 'M%s %sA%d %d 0 0 1 %s %s' % (f(cx + rr * math.cos(a1)), f(cy + rr * math.sin(a1)), rr, rr, f(cx + rr * math.cos(a2)), f(cy + rr * math.sin(a2)))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.35)" stroke-width="9" stroke-linecap="round" fill="none"/>' % arc(23, 31, r - 22))
    s.append('<path class="sh-arc" d="%s" stroke="#c4ff49" stroke-width="9" stroke-linecap="round" fill="none"/>' % arc(7, 15, r - 22))
    s.append('<g class="sh-hand"><path d="M%d %dV%d" stroke="#c4ff49" stroke-width="3" stroke-linecap="round"/></g>' % (cx, cy, cy - r + 14))
    s.append('<circle cx="%d" cy="%d" r="6" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/>' % (cx, cy))
    s.append(ico('sun', cx, cy + r + 22, 22, WHITE, 1.8)); s.append(ico('sleep', cx, cy - r - 20, 22, LIME, 1.8))
    lanes = [(70, 'Night sleep', 50, 'sh-a', WHITE), (180, 'Day sleep', 210, 'sh-b', LIME)]
    for k, (y, lab, x0, cls, col) in enumerate(lanes):
        s.append(txt(260, y - 30, lab, 12, '#c4ff49' if k else '#fff', 0.9, 'start'))
        s.append('<path d="M260 %dH530" stroke="rgba(255,255,255,0.25)" stroke-width="1.6"/>' % (y + 20))
        bx = 260 + (0 if k == 0 else 90)
        s.append('<rect x="%d" y="%d" width="120" height="44" rx="8" fill="%s"/>' % (bx, y - 24, 'rgba(255,255,255,0.07)' if k == 0 else 'rgba(196,255,73,0.1)'))
        d, pts = path(('M', bx - 20, y + 12), ('C', bx + 30, y + 12, bx + 60, y - 18, bx + 120, y - 18), ('C', bx + 150, y - 18, bx + 180, y + 4, bx + 200, y + 8), n=12)
        s.append(dr(d, 0.3 + k * 0.3, 1.4, col, 2.6))
        s.append(dot('%s fx' % cls, 4.5, col)); G.travel(cls, pts, 8, 72, 8, delay='%ss' % f(-k * 3), rest=pts[-1], rest_opacity=0, fade=3)
    s.append(txt(395, 250, 'T follows your sleep, day or night', 13, '#c4ff49', 0.95))
    return '\n'.join(s)

def testing():
    s = []
    s.append('<path d="M30 200H300" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>')
    s.append('<g class="ts-sun"><circle cx="110" cy="176" r="26" fill="#c4ff49" fill-opacity="0.85"/></g>')
    s.append('<rect x="30" y="201" width="270" height="60" fill="#0f240f"/>')
    for k, x in enumerate((60, 160)):
        s.append('<g class="ts-ray" style="--k:%d"><path d="M%d 150l-10-14M%d 150l10-14" stroke="#c4ff49" stroke-width="2" stroke-linecap="round"/></g>' % (k, x, x + 40))
    cx, cy, r = 380, 120, 70
    s.append('<circle cx="%d" cy="%d" r="%d" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.45)" stroke-width="2.2"/>' % (cx, cy, r))
    a1, a2 = -math.pi / 2 + 7 / 12 * 2 * math.pi, -math.pi / 2 + 11 / 12 * 2 * math.pi
    s.append('<path class="ts-win" d="M%s %sA%d %d 0 0 1 %s %s" stroke="#c4ff49" stroke-width="8" stroke-linecap="round" fill="none"/>' % (f(cx + (r - 12) * math.cos(a1)), f(cy + (r - 12) * math.sin(a1)), r - 12, r - 12, f(cx + (r - 12) * math.cos(a2)), f(cy + (r - 12) * math.sin(a2))))
    for h in range(12):
        a = -math.pi / 2 + h / 12 * 2 * math.pi
        s.append('<circle cx="%s" cy="%s" r="2" fill="#fff" fill-opacity="0.6"/>' % (f(cx + (r - 26) * math.cos(a)), f(cy + (r - 26) * math.sin(a))))
    s.append('<g class="ts-hand"><path d="M%d %dV%d" stroke="#fff" stroke-width="3" stroke-linecap="round"/></g>' % (cx, cy, cy - 44))
    s.append('<circle cx="%d" cy="%d" r="5" fill="#c4ff49"/>' % (cx, cy))
    s.append(txt(cx, cy + r + 26, '7 to 11 a.m. window', 12, '#c4ff49', 0.95))
    s.append('<rect x="490" y="60" width="30" height="120" rx="15" fill="none" stroke="#fff" stroke-opacity="0.75" stroke-width="2.4"/>')
    s.append('<rect class="ts-fill" x="496" y="100" width="18" height="74" rx="9" fill="#c4ff49" fill-opacity="0.85"/>')
    s.append(txt(505, 206, 'Fasting', 12, '#fff', 0.85)); s.append(txt(505, 222, 'x2', 12, '#c4ff49', 0.95))
    s.append(txt(165, 240, 'After a normal night', 13, '#fff', 0.85))
    return '\n'.join(s)

def habits():
    s = []
    items = [('clock', 'Same wake time'), ('bed', '7 to 9 hours'), ('sun', 'Daylight + activity'),
             ('cup', 'Caffeine early'), ('wine', 'No alcohol late'), ('screen', 'Dark, cool room')]
    for k, (ic, lab) in enumerate(items):
        col, row = k % 2, k // 2
        x, y = 50 + col * 260, 40 + row * 74
        s.append('<g class="hb-row" style="--k:%d"><rect x="%d" y="%d" width="230" height="56" rx="12" fill="rgba(255,255,255,0.04)" stroke="rgba(196,255,73,0.35)" stroke-width="1.6"/>%s%s'
                 '<g class="hb-ck"><circle cx="%d" cy="%d" r="11" fill="#c4ff49"/><path d="M%d %dl4 4 8-9" fill="none" stroke="#0f240f" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></g></g>'
                 % (k, x, y, ico(ic, x + 30, y + 28, 24, LIME, 1.8), txt(x + 56, y + 33, lab, 13, '#fff', 0.9, 'start'), x + 204, y + 28, x + 198, y + 28))
    return '\n'.join(s)

def help_fig():
    s = ['<g class="pop t" style="--d:0.1"><rect x="230" y="26" width="100" height="168" rx="16" fill="#142e14" stroke="#c4ff49" stroke-width="2.2"/><path d="M268 36h24" stroke="rgba(255,255,255,0.5)" stroke-width="3" stroke-linecap="round"/></g>']
    s.append(node(280, 76, 22, 'coach', 0.25, LIME, fill='#173617', isz=24))
    for k, h in enumerate((22, 34, 28, 46, 52)):
        x = 248 + k * 16
        s.append('<g class="hp-bar" style="--k:%d"><rect x="%d" y="%d" width="10" height="%d" rx="3" fill="%s"/></g>' % (k, x, 176 - h, h, LIME if k > 2 else '#fff'))
    s.append(txt(280, 214, 'Sleep log', 12, '#fff', 0.8))
    for i, (a, b, cls, col) in enumerate([((90, 110), (226, 110), 'hp-in', WHITE), ((334, 110), (470, 110), 'hp-out', LIME)]):
        d, pts = path(('M', a[0], a[1]), ('L', b[0], b[1]))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % d)
        s.append(dot('%s fx' % cls, 5, col)); G.travel(cls, pts, 8, 48, 6, delay='%ss' % f(-i * 3), rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(60, 110, 26, 'tube', 0.45, WHITE, isz=26)); s.append(txt(60, 160, 'Labs', 13))
    s.append(node(500, 110, 26, 'doc', 0.55, LIME, fill='#142e14', isz=26)); s.append(txt(500, 160, 'Your plan', 13, '#c4ff49', 0.95))
    for k, ic in enumerate(('sleep', 'train', 'food', 'stress')):
        x = 60 + k * 50 if k < 2 else 410 + (k - 2) * 50
        s.append('<g class="hp-i" style="--k:%d"><circle cx="%d" cy="226" r="18" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/>%s</g>' % (k, x + 20, ico(ic, x + 20, 226, 18, LIME, 1.8)))
    return '\n'.join(s)

def final():
    s = ['<path d="M30 150H330" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>']
    s.append('<g class="fn-moon">%s</g>' % ico('sleep', 120, 80, 40, LIME, 1.8))
    s.append('<g class="fn-sun"><circle cx="240" cy="132" r="24" fill="#c4ff49" fill-opacity="0.85"/></g>')
    s.append('<rect x="30" y="151" width="300" height="60" fill="#0f240f"/>')
    s.append(stars(((60, 50), (180, 40), (300, 62)), 'fn-st'))
    s.append(node(180, 178, 18, 'check', 0.3, LIME, fill='#142e14', isz=20))
    return '\n'.join(s)

FAQMOTIF = '''<g class="fq-moon">%s</g>
<path class="dr" pathLength="1" style="--d:0.25;--dur:1.1s" d="M74 38c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="86" cy="66" r="3" fill="#fff"/>
<g class="fq-z" style="--k:0"><path d="M100 14h8l-8 9h8" stroke="#c4ff49" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></g>
<g class="fq-z" style="--k:1"><path d="M110 30h6l-6 7h6" stroke="#c4ff49" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>''' % ico('sleep', 36, 50, 52, LIME, 2.2)

def step_icons():
    return {
     "{{STEP1}}": '<path d="M8 12h32a2 2 0 0 1 2 2v18a2 2 0 0 1-2 2H22l-8 6v-6H8a2 2 0 0 1-2-2V14a2 2 0 0 1 2-2z"/><g class="hi-bl" style="--k:0"><circle cx="16" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="24" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="32" cy="23" r="2" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M12 6h10"/><path d="M14 6v26a3 3 0 0 0 6 0V6"/><path d="M14 20h6"/><g class="hi-gr" style="--k:0"><path d="M30 40V30M36 40V22M42 40V34" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<path d="M30 10a12 12 0 1 0 10 18A10 10 0 0 1 30 10z"/><g class="hi-sl" style="--k:0"><path d="M6 42h14" stroke="#c4ff49"/><circle cx="13" cy="42" r="3" stroke="#c4ff49"/></g>',
     "{{STEP4}}": '<path d="M6 40h36"/><path d="M8 34l9-8 7 5 14-14"/><g class="hi-ck" style="--k:0"><path d="M30 8l4 4 8-9" stroke="#c4ff49"/></g>',
    }

def hub_nodes():
    icons = ['list', 'compass', 'tube', 'calendar', 'clock', 'scale', 'coach', 'caps']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)
        out.append((round(280 + 230 * math.cos(a)), round(100 + 68 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{INSOMNIA}}": insomnia(), "{{OVERNIGHT}}": overnight(), "{{SHORT}}": shortsleep(), "{{APNEA}}": apnea(), "{{SHIFT}}": shiftfig(),
         "{{TESTING}}": testing(), "{{HABITS}}": habits(), "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB,
         "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Low testosterone, insomnia and poor sleep in men: how sleep and testosterone affect each other",
      "Low testosterone and sleep", "Can low testosterone cause insomnia, and how does sleep affect T?", slots, G, published="2026-10-16", modified="2026-10-22")

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
# 2026-10-22 sleep deepen: same page-local compaction as /trt-side-effects (2026-10-21) to stay under the GHL save limit
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
# Safari-motion guard (no-op unless something regressed)
print(subprocess.run([sys.executable, "/workspace/safari-fix/apply_fix.py", p], capture_output=True, text=True).stdout.strip())
print("minified", len(full.encode()), "->", len(open(p, encoding="utf-8").read().encode()), "bytes")
