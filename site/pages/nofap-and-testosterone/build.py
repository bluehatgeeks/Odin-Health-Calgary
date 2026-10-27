"""Build /workspace/pages/nofap-and-testosterone/page.html (self-contained; paste into a GHL custom-code element when approved).
Template: /testosterone-and-hair-loss (same pipeline). Every number is from /workspace/research-nofap/SOURCES.md (checked Oct 21 2026).
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ). Output is minified at the end (HighLevel save limit)."""
import sys, os, math, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "nofap-and-testosterone"
TITLE = "NoFap and Testosterone: The Day 7 Myth | Odin Health Lab"
DESC = "Testosterone peaking after seven days of NoFap comes from a 28-man study retracted in 2021. What it found, and what ejaculation means for the prostate."
OG_ALT = "Odin Health Lab: does NoFap raise testosterone, the retracted day 7 study, and ejaculation frequency and prostate cancer"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 155, (len(TITLE), len(DESC))

common.ICONS.update({
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "pause": '<circle cx="12" cy="12" r="9"/><path d="M10 8.5v7M14 8.5v7"/>',
 "stamp": '<path d="M5 20h14"/><path d="M7 16h10v-3a2 2 0 0 0-2-2h-1V8a2 2 0 1 0-4 0v3H9a2 2 0 0 0-2 2z"/>',
})

FAQ = [
 ("Does NoFap raise testosterone?",
  "Not in any lasting way that research has shown. The popular claim that testosterone peaks after seven days without ejaculating comes from one study of 28 men, published in 2003 and retracted by the journal on December 10, 2021. Even in that study, levels did not keep rising: after the peak on the seventh day, the authors saw no regular change with longer abstinence."),
 ("Does masturbation lower testosterone?",
  "The study most often quoted on this does not show a drop. In the 2003 study of 28 men, testosterone changed very little from the second to the fifth day after ejaculating, then peaked on the seventh day. That study has since been retracted, so it should not be used as proof either way. If you are worried about low testosterone, two early-morning blood tests tell you far more than counting days."),
 ("Does testosterone really peak on day 7 without ejaculating?",
  "That is what one 2003 study reported: in 28 volunteers, serum testosterone reached 145.7 percent of baseline on the seventh day of abstinence. The journal retracted the paper on December 10, 2021 because it significantly overlapped an earlier Chinese-language paper by the same lead author. The result has not become a reason to plan your sex life around a calendar."),
 ("Was the day 7 testosterone study fake?",
  "The retraction notice does not say that. It gives one reason: the 2003 English paper significantly overlapped a 2002 paper published in Chinese by the lead author. Two of the four authors agreed to the retraction, and the editor could not reach the other two. The notice does not question the data, but a retracted paper is no longer part of the reliable record."),
 ("Is ejaculating often linked to lower prostate cancer risk?",
  "In one large study, yes. Among 31,925 US men in the Health Professionals Follow-up Study, followed from 1992 to 2010, men who reported 21 or more ejaculations a month had about a 20 percent lower risk of prostate cancer than men who reported 4 to 7 (hazard ratio 0.81 for frequency at ages 20 to 29, and 0.78 at ages 40 to 49). The link was driven by lower-risk cancers. The study is observational, so it shows a link, not proof that ejaculating more prevents cancer."),
 ("How does Odin Health Lab work with my doctor?",
  'Odin Health Lab is an andropause and low testosterone telehealth service for men in Canada and the USA. We work alongside your own doctor: we go through your symptoms, sleep, weight, stress, medications and any lab results with you, help you decide which tests to ask your doctor for (such as two early-morning total testosterone tests, and PSA when it fits your age and history), and build your plan. We can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]

SRC = [
 ("source_jiang_2003", "Jiang M, Xin J, Zou Q, Shen JW. A research on the relationship between ejaculation and serum testosterone level in men. <em>J Zhejiang Univ Sci</em> 2003;4(2):236&ndash;240 (retracted).", "https://pubmed.ncbi.nlm.nih.gov/12659241/", "pubmed.ncbi.nlm.nih.gov/12659241"),
 ("source_jiang_retraction", "Retraction Note to: A research on the relationship between ejaculation and serum testosterone level in men. <em>J Zhejiang Univ Sci A</em>, published December 10, 2021.", "https://doi.org/10.1631/jzus.2003.r236", "doi.org/10.1631/jzus.2003.r236"),
 ("source_rider_2016", "Rider JR, Wilson KM, Sinnott JA, et al. Ejaculation Frequency and Risk of Prostate Cancer: Updated Results with an Additional Decade of Follow-up. <em>Eur Urol</em> 2016;70(6):974&ndash;982.", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5040619/", "pmc.ncbi.nlm.nih.gov/articles/PMC5040619"),
]
def src_html():
    return '\n'.join('<li>%s <a href="%s" target="_blank" rel="noopener noreferrer" data-cta="%s">%s</a></li>' % (t, u, c, l) for c, t, u, l in SRC)

G = Gen()

def txt(x, y, s, size=13, fill='#fff', op=0.85, anchor='middle', extra=''):
    a = '' if anchor == 'middle' else ' text-anchor="%s"' % anchor
    return '<text x="%s" y="%s" font-size="%s" fill="%s" fill-opacity="%s"%s%s>%s</text>' % (f(x), f(y), size, fill, op, a, extra, s)

def box(x, y, w, h, hot=False, rx=12):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="1.8"/>' % (f(x), f(y), f(w), f(h), rx,
        'rgba(196,255,73,0.08)' if hot else 'rgba(255,255,255,0.04)', '#c4ff49' if hot else 'rgba(255,255,255,0.35)')

def solid(x, y, w, h, hot=False, rx=12):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="1.8"/>' % (f(x), f(y), f(w), f(h), rx,
        '#173617' if hot else '#142e14', '#c4ff49' if hot else 'rgba(255,255,255,0.45)')

# ---------- hero: day 1 to 9 calendar, the reported day 7 peak, and a RETRACTED stamp ----------
def hero():
    s = ['<defs><radialGradient id="nf-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.14"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="225" ry="140" fill="url(#nf-g)"/>']
    s.append(txt(240, 26, 'The day 7 claim, as the 2003 study reported it', 13, '#c4ff49', 0.9))
    base = 214
    ys = [base, base - 4, base + 2, base - 3, base + 1, base - 2, base - 92, base - 6, base + 2]
    xs = [60 + i * 45 for i in range(9)]
    s.append('<path d="M40 %dH440" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-dasharray="3 6"/>' % base)
    s.append(txt(444, base - 6, 'Baseline', 11, '#fff', 0.6, 'end'))
    for i, x in enumerate(xs):
        s.append('<rect x="%s" y="238" width="34" height="30" rx="7" fill="%s" stroke="%s" stroke-width="1.6"/>' % (f(x - 17), '#173617' if i == 6 else 'rgba(255,255,255,0.04)', '#c4ff49' if i == 6 else 'rgba(255,255,255,0.3)'))
        s.append(txt(x, 258, str(i + 1), 12, '#c4ff49' if i == 6 else '#fff', 0.9))
    s.append(txt(240, 290, 'Abstinence, counted day by day', 11.5, '#fff', 0.75))
    segs = [('M', xs[0], ys[0])] + [('L', xs[i], ys[i]) for i in range(1, 9)]
    d, pts = path(*segs)
    s.append('<path d="%s" stroke="rgba(196,255,73,0.35)" stroke-width="2.6" fill="none" stroke-linejoin="round"/>' % d)
    s.append(dot('nf-d fx', 6, LIME, ring=True)); G.travel('nf-d', pts, 5, 80, 7, rest=pts[-1], rest_opacity=0, fade=4)
    s.append('<g class="nf-pk"><circle cx="%s" cy="%s" r="7" fill="#c4ff49"/></g>' % (f(xs[6]), f(ys[6])))
    s.append(txt(xs[6], ys[6] - 16, '145.7 percent of baseline', 11.5, '#c4ff49', 0.95))
    s.append('<g class="nf-st"><g transform="rotate(-10 120 92)"><rect x="52" y="70" width="136" height="42" rx="8" fill="#0f240f" stroke="#c4ff49" stroke-width="3"/>%s%s</g></g>'
             % (txt(120, 92, 'RETRACTED', 15, '#c4ff49', 1, 'middle', ' font-weight="800" letter-spacing="2"'), txt(120, 106, 'December 10, 2021', 10.5, '#fff', 0.85)))
    s.append(txt(240, 314, '28 men; the journal retracted the paper', 11.5, '#fff', 0.7))
    return '\n'.join(s)

# ---------- the study: what 28 men showed, three phases lighting in turn ----------
def study_fig():
    s = [txt(16, 24, 'What the 2003 study reported in 28 volunteers', 13, '#c4ff49', 0.95, 'start')]
    rows = (('Days 2 to 5', 'Testosterone changed very little', False, 'pause'),
            ('Day 7', 'A clear peak at 145.7 percent of baseline', True, 'gauge'),
            ('After the peak', 'No regular change with longer abstinence', False, 'calendar'))
    for k, (a, b, hot, ic) in enumerate(rows):
        y = 40 + k * 64
        s.append('<g class="st-r" style="--k:%d">%s%s%s%s</g>' % (k, box(16, y, 528, 54, hot, 12), ico(ic, 44, y + 27, 22, LIME, 2),
                 txt(70, y + 23, a, 13, '#c4ff49' if hot else '#fff', 0.95, 'start'), txt(70, y + 42, b, 12, '#fff', 0.85, 'start')))
    return '\n'.join(s)

# ---------- retraction timeline: 2002 Chinese paper -> 2003 English paper -> 2021 retraction ----------
def retract_fig():
    s = []
    pts3 = ((90, 'calendar', '2002', 'Paper in Chinese', 'Lead author, Acta Physiologica Sinica'), (280, 'list', '2003', 'Paper in English', 'J Zhejiang Univ Sci, 28 men'), (470, 'stamp', '2021', 'Retracted', 'December 10: overlap with 2002'))
    s.append('<path d="M90 70H470" stroke="rgba(255,255,255,0.18)" stroke-width="3" stroke-dasharray="3 7"/>')
    d, pts = path(('M', 90, 70), ('L', 470, 70))
    s.append(dot('rt-d fx', 6, LIME, ring=True)); G.travel('rt-d', pts, 5, 85, 8, rest=pts[-1], rest_opacity=0, fade=4)
    for k, (x, ic, yr, a, b) in enumerate(pts3):
        hot = k == 2
        s.append(node(x, 70, 28, ic, 0.2 + k * 0.2, LIME if hot else WHITE, fill='#173617' if hot else '#142e14', isz=26))
        s.append('<g class="rt-l" style="--k:%d">%s%s%s</g>' % (k, txt(x, 128, yr, 15, '#c4ff49', 0.95, 'middle', ' font-weight="800"'), txt(x, 150, a, 12.5, '#fff', 0.92), txt(x, 168, b, 11, '#fff', 0.7)))
    s.append(txt(280, 204, 'The notice gives overlap as the reason; it does not question the data', 11.5, '#fff', 0.72))
    return '\n'.join(s)

# ---------- prostate: hazard ratio bars, 4 to 7 a month vs 21 or more ----------
def prostate_fig():
    s = [txt(16, 24, 'Prostate cancer risk vs men reporting 4 to 7 a month', 13, '#c4ff49', 0.95, 'start')]
    groups = (('Frequency at ages 20 to 29', 0.81), ('Frequency at ages 40 to 49', 0.78))
    sc = 300
    for g, (lab, hr) in enumerate(groups):
        y = 54 + g * 84
        s.append(txt(16, y, lab, 12.5, '#fff', 0.92, 'start'))
        for k, (name, v, hot) in enumerate((('4 to 7 a month', 1.0, False), ('21 or more', hr, True))):
            yy = y + 12 + k * 26
            s.append(txt(150, yy + 13, name, 11.5, '#c4ff49' if hot else '#fff', 0.88, 'end'))
            s.append('<path d="M162 %dH462" stroke="rgba(255,255,255,0.08)" stroke-width="16" stroke-linecap="round"/>' % (yy + 9))
            s.append('<g class="pr-b" style="--k:%d"><rect x="162" y="%d" width="%s" height="16" rx="8" fill="%s" fill-opacity="%s"/></g>' % (g * 2 + k, yy + 1, f(v * sc), '#c4ff49' if hot else '#fff', 0.85 if hot else 0.4))
            s.append(txt(172 + v * sc, yy + 14, ('%.2f' % v), 12, '#c4ff49' if hot else '#fff', 0.95, 'start'))
    s.append(txt(16, 238, '31,925 US men, 1992 to 2010; hazard ratio, lower means fewer cancers found', 11, '#fff', 0.7, 'start'))
    return '\n'.join(s)

# ---------- what moves testosterone: four levers light in turn ----------
def levers_fig():
    s = []
    rows = (('sleep', 'Sleep', 'Short nights lower daytime testosterone'), ('scale', 'Body fat', 'Losing extra weight raises it'),
            ('wine', 'Alcohol', 'Heavy drinking drags it down'), ('tube', 'Labs', 'Two early-morning tests show your real level'))
    for k, (ic, a, b) in enumerate(rows):
        x = 16 + (k % 2) * 272
        y = 14 + (k // 2) * 76
        s.append('<g class="lv-r" style="--k:%d">%s%s%s%s</g>' % (k, box(x, y, 256, 64, k == 3, 12), ico(ic, x + 30, y + 32, 22, LIME, 2),
                 txt(x + 56, y + 27, a, 13, '#c4ff49' if k == 3 else '#fff', 0.95, 'start'), txt(x + 56, y + 46, b, 11.5, '#fff', 0.85, 'start')))
    return '\n'.join(s)

# ---------- help: history + labs + goals -> telehealth assessment -> plan ----------
def help_fig():
    s = []
    for i, (y, ic, lab) in enumerate(((44, 'chat', 'Your symptoms'), (115, 'tube', 'Your labs'), (186, 'sleep', 'Your habits'))):
        s.append(node(40, y, 22, ic, 0.1 + i * 0.1, LIME if i != 1 else WHITE, isz=22) + txt(70, y + 4, lab, 12.5, '#fff', 0.9, 'start'))
        d, pts = path(('M', 170, y), ('C', 208, y, 214, 115, 244, 115), n=6)
        s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % d)
        s.append(dot('hp-a%d fx' % i, 5, WHITE)); G.travel('hp-a%d' % i, pts, 6 + i * 10, 40 + i * 10, 7, rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(276, 115, 30, 'video', 0.4, LIME, fill='#173617', isz=28) + txt(276, 168, 'Telehealth assessment', 12, '#fff', 0.88))
    d, pts = path(('M', 308, 115), ('L', 372, 115))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % d)
    s.append(dot('hp-b fx', 5, LIME)); G.travel('hp-b', pts, 50, 72, 7, rest=pts[0], rest_opacity=0, fade=3)
    s.append('<g class="pop t" style="--d:0.5"><rect x="376" y="22" width="168" height="186" rx="14" fill="#142e14" stroke="rgba(255,255,255,0.55)" stroke-width="2"/></g>')
    s.append(txt(460, 46, 'Your plan', 13, '#c4ff49', 0.95))
    for k, (ic, lab) in enumerate((('gauge', 'Hormones'), ('tube', 'Labs'), ('sleep', 'Sleep'), ('train', 'Training'))):
        y = 76 + k * 34
        s.append('<g class="hp-r" style="--k:%d">%s%s</g>' % (k, ico(ic, 402, y, 18, LIME, 2), txt(420, y + 4, lab, 12.5, '#fff', 0.92, 'start')))
    return '\n'.join(s)

def final():
    s = ['<defs><radialGradient id="fn-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.3"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><circle cx="180" cy="105" r="92" fill="url(#fn-g)"/>']
    s.append('<circle class="fn-ring fx" cx="180" cy="104" r="56" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append('<g class="fn-sh"><path d="M180 48l46 17v34c0 30-20 48-46 56-26-8-46-26-46-56V65z" fill="#142e14" stroke="#c4ff49" stroke-width="4" stroke-linejoin="round"/></g>')
    s.append(dr('M160 104l14 14 28-30', 0.4, 0.9, '#fff', 5))
    s.append(node(56, 70, 20, 'calendar', 0.3, WHITE, isz=22)); s.append(node(304, 70, 20, 'tube', 0.4, LIME, fill='#142e14', isz=22))
    return '\n'.join(s)

FAQMOTIF = '''<g class="fq-dp"><circle cx="28" cy="50" r="10" stroke="#c4ff49" stroke-width="4"/><path d="M28 30v5M28 65v5M8 50h5M43 50h5M14 36l3.5 3.5M38.5 60.5l3.5 3.5M14 64l3.5-3.5M38.5 39.5l3.5-3.5" stroke="#c4ff49" stroke-width="3" stroke-linecap="round"/></g>
<path class="dr" pathLength="1" style="--d:0.25;--dur:1.1s" d="M70 36c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82" cy="64" r="3" fill="#fff"/>
<g class="fq-fr" style="--k:0"><circle cx="104" cy="22" r="5" fill="#c4ff49"/></g><g class="fq-fr" style="--k:1"><circle cx="54" cy="20" r="4" fill="#c4ff49"/></g>'''

def step_icons():
    return {
     "{{STEP1}}": '<path d="M8 12h32a2 2 0 0 1 2 2v18a2 2 0 0 1-2 2H22l-8 6v-6H8a2 2 0 0 1-2-2V14a2 2 0 0 1 2-2z"/><g class="hi-bl" style="--k:0"><circle cx="16" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="24" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="32" cy="23" r="2" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M12 6h10"/><path d="M14 6v26a3 3 0 0 0 6 0V6"/><path d="M14 20h6"/><g class="hi-gr" style="--k:0"><path d="M30 40V30M36 40V22M42 40V34" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<path d="M8 38C8 22 18 12 40 10c0 22-10 30-26 30"/><g class="hi-sw" style="--k:0"><path d="M8 38c6-9 12-15 20-19" stroke="#c4ff49"/></g>',
     "{{STEP4}}": '<path d="M6 40h36"/><path d="M8 34l9-8 7 5 14-14"/><g class="hi-ck" style="--k:0"><path d="M30 8l4 4 8-9" stroke="#c4ff49"/></g>',
    }

def hub_nodes():
    icons = ['leaf', 'sleep', 'list', 'tube', 'drop', 'gauge']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)
        out.append((round(280 + 220 * math.cos(a)), round(100 + 66 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{STUDY}}": study_fig(), "{{RETRACT}}": retract_fig(), "{{PROSTATE}}": prostate_fig(), "{{LEVERS}}": levers_fig(),
         "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(), "{{SRC}}": src_html(), "{{HUB}}": HUB,
         "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "NoFap, masturbation and testosterone in men: the retracted day 7 study and ejaculation frequency and prostate cancer",
      "Does NoFap raise testosterone?", "Does NoFap raise testosterone? What the day 7 study really showed", slots, G, published="2026-10-21")

# ---- minify for HighLevel (same as /testosterone-and-hair-loss) ----
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
used = set(re.findall(r'#pi-([\w-]+)', m))
m = re.sub(r'<symbol id="pi-([\w-]+)" viewBox="0 0 24 24">[\s\S]*?</symbol>', lambda x: x.group(0) if x.group(1) in used else '', m)
def tight(mm):
    c = mm.group(0)
    c = re.sub(r'\s*([{};])\s*', r'\1', c); c = re.sub(r':\s+', ':', c); c = re.sub(r',\s+', ',', c)
    return c
m = re.sub(r'(?<=<style>)[\s\S]*?(?=</style>)', tight, m)
open(p, "w", encoding="utf-8").write(m)
print(subprocess.run([sys.executable, "/workspace/safari-fix/apply_fix.py", p], capture_output=True, text=True).stdout.strip())
print("minified", len(full.encode()), "->", len(open(p, encoding="utf-8").read().encode()), "bytes")
