"""Build /trt-clinic-calgary (t2-1028): local landing page for 'TRT Calgary' / 'testosterone replacement therapy Calgary' / 'testosterone clinic Calgary'.
Edit page.body.html, page.css or this file; then: python3 build.py. FAQ HTML and FAQPage JSON-LD come from ONE list.
Facts reused from already-sourced pages only: Alberta Drug Benefit List + clinic fee (Alex, 2026-10-23) from /trt-cost-canada-vs-usa,
APL ranges from /testosterone-calculator (lab1028). No address, hours or in-person claims (unverified)."""
import sys, os, math, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "trt-clinic-calgary"
TITLE = "TRT Calgary: Online Testosterone Clinic | Odin Health Lab"
DESC = "TRT clinic for Calgary and Alberta men, by telehealth: low-T assessment, APL lab ranges explained, costs in Alberta and a written plan. Free call."
OG_ALT = "Odin Health Lab: TRT and low testosterone care by telehealth for men in Calgary and Alberta"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 158, (len(TITLE), len(DESC))
H1 = "TRT clinic in Calgary: low testosterone care by telehealth"

common.ICONS.update({
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "pin": '<path d="M12 21s-6-6.2-6-11a6 6 0 0 1 12 0c0 4.8-6 11-6 11z"/><circle cx="12" cy="10" r="2.2"/>',
 "coin": '<circle cx="12" cy="12" r="9"/><path d="M14.5 9.5c-.5-1-1.5-1.5-2.5-1.5-1.4 0-2.5.8-2.5 2s1 1.6 2.5 2 2.5.8 2.5 2-1.1 2-2.5 2c-1 0-2-.5-2.5-1.5M12 6.5V8M12 16v1.5"/>',
})

FAQ = [
 ("Is there a TRT clinic in Calgary that works by telehealth?",
  "Yes. Odin Health Lab is a low testosterone and andropause telehealth service built in Calgary for men in Calgary, across Alberta and elsewhere in Canada and the USA. Calls are by video or phone, so you do not need to travel to an office. We go through your symptoms and history, plan the right morning labs, explain your results and build a written sleep, weight, stress and nutrition plan with you."),
 ("How much does TRT cost in Calgary?",
  'Most TRT clinics charge about $100 to $300 a month for visits and monitoring, and the medication is extra. On Alberta&rsquo;s drug list generic testosterone cypionate is a regular benefit at $34.88 CAD for a 10 mL vial, about $15 a month at 100 mg a week before the pharmacy&rsquo;s dispensing fee. Gels are not a benefit on the list. See the full breakdown in <a href="%s/trt-cost-canada-vs-usa#alberta">TRT cost in Canada vs the USA</a>.' % SITE),
 ("What testosterone level is low on an Alberta lab report?",
  'Alberta Precision Laboratories lists an adult male range of 8.0 to 35.0 nmol/L for total testosterone and notes results can be up to a quarter lower later in the day, so a morning draw between 7 and 10 a.m. is suggested. APL calculates free testosterone from total T, SHBG and albumin, with an adult male range of 175 to 700 pmol/L. Our <a href="%s/testosterone-calculator">testosterone calculator</a> converts and explains your numbers.' % SITE),
 ("Do I need to live in Calgary to work with Odin Health Lab?",
  "No. Everything happens by telehealth, so men anywhere in Alberta, the rest of Canada and the USA can book. Calgary is where we are built, and we know how Alberta lab reports and the Alberta drug list work."),
 ("What should I bring to the first call?",
  'A list of your symptoms and when they started, your medications and supplements, and any recent lab results, such as total testosterone, SHBG, hematocrit or PSA. If you have not had labs yet, we help you plan which ones to ask for. See <a href="%s/low-testosterone-labs-to-ask-for">low testosterone labs to ask for</a>.' % SITE),
 ("How does Odin Health Lab work with my doctor?",
  'We work alongside your own doctor. We go through your symptoms, history and lab results with you, help you decide which tests to ask your doctor for, prepare your questions about TRT and its costs, and build your sleep, weight, stress and nutrition plan. We can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]

G = Gen()

def txt(x, y, s, size=13, fill='#fff', op=0.85, anchor='middle', extra=''):
    return '<text x="%s" y="%s" font-size="%s" fill="%s" fill-opacity="%s" text-anchor="%s"%s>%s</text>' % (f(x), f(y), size, fill, op, anchor, extra, s)

def box(x, y, w, h, hot=False, rx=12):
    return '<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, w, h, rx, '#142e14' if hot else DARK, LIME if hot else 'rgba(255,255,255,0.35)')

def hero():
    """A loop: Calgary pin -> video call -> morning labs -> written plan; a dot rides it, a ring pulses on the call."""
    s = ['<defs><radialGradient id="yc-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.16"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="210" ry="130" fill="url(#yc-g)"/>']
    nodes = [(70, 100, 'pin', 'Calgary + Alberta'), (240, 70, 'video', 'Free call'), (410, 100, 'tube', 'Morning labs'), (240, 230, 'list', 'Written plan')]
    d, pts = path(('M', 70, 100), ('C', 140, 40, 200, 40, 240, 70), ('C', 290, 40, 360, 40, 410, 100), ('C', 400, 170, 300, 220, 240, 230), ('C', 180, 220, 80, 170, 70, 100), n=16)
    s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>' % d)
    s.append(dr(d, 0.25, 1.8, 'rgba(196,255,73,0.5)', 2.4))
    s.append(dot('yc-o fx', 6, LIME, ring=True)); G.travel('yc-o', pts, 4, 92, 11, rest=pts[0], rest_opacity=0, fade=2)
    for i, (x, y, ic, lab) in enumerate(nodes):
        s.append(node(x, y, 28 if i != 1 else 30, ic, 0.15 + i * 0.12, LIME if i in (1, 3) else WHITE, fill='#142e14' if i in (1, 3) else DARK, isz=30 if i != 1 else 32))
        s.append(txt(x, y + 48, lab, 13, '#c4ff49' if i in (1, 3) else '#fff', 0.9))
    s.append('<circle class="wc-ring fx" cx="240" cy="70" r="38" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    return '\n'.join(s)

def how():
    s = []
    cols = [('Talk', 'video', ['Video or phone call', 'symptoms, sleep, weight', 'medications, goals']),
            ('Test', 'tube', ['Two morning labs', 'free T and SHBG', 'when borderline']),
            ('Plan', 'list', ['Written plan', 'check-ins, repeat labs', 'TRT questions ready'])]
    for k, (head, ic, lines) in enumerate(cols):
        x = 16 + k * 180
        g = [box(x, 16, 168, 152, k == 0, 14), '<rect x="%d" y="16" width="168" height="38" rx="14" fill="rgba(196,255,73,0.12)"/>' % x,
             ico(ic, x + 22, 35, 18, LIME, 2), txt(x + 38, 40, head, 12.5, '#c4ff49', 0.95, 'start')]
        for i, l in enumerate(lines):
            g.append(txt(x + 84, 84 + i * 28, l, 11.5, '#fff', 0.9))
        s.append('<g class="pv-p" style="--k:%d">%s</g>' % (k, ''.join(g)))
    s.append('<g class="pv-n">%s%s</g>' % (box(60, 182, 440, 34, True, 12), txt(280, 204, 'All by telehealth, anywhere in Alberta', 12, '#fff', 0.92)))
    return '\n'.join(s)

def labs():
    """APL total T range bar (8.0-35.0 nmol/L on a 0-40 scale) and free T bar (175-700 pmol/L on 0-800), stretching in."""
    s = []
    for k, (y, lab, lo, hi, mx, a, b, hot) in enumerate(((50, 'Total testosterone, APL adult male range (nmol/L)', 8.0, 35.0, 40, '8.0', '35.0', True),
                                                       (120, 'Free testosterone, calculated by APL (pmol/L)', 175, 700, 800, '175', '700', False))):
        X = lambda v: 40 + v * 480 / mx
        s.append(txt(40, y - 14, lab, 12.5, '#c4ff49' if hot else '#fff', 0.95, 'start'))
        s.append('<path d="M40 %dH520" stroke="rgba(255,255,255,0.14)" stroke-width="14" stroke-linecap="round"/>' % (y + 6))
        s.append('<g class="cf-b" style="--k:%d"><rect x="%s" y="%d" width="%s" height="14" rx="7" fill="%s" fill-opacity="%s"/></g>' % (k, f(X(lo)), y - 1, f(X(hi) - X(lo)), LIME if hot else WHITE, 0.8 if hot else 0.6))
        s.append(txt(X(lo), y + 32, a, 11.5, '#fff', 0.9) + txt(X(hi), y + 32, b, 11.5, '#fff', 0.9))
    for k, (ic, lab) in enumerate((('sun', 'Draw 7 to 10 a.m.'), ('calendar', 'Repeat to confirm'), ('link', 'Same lab each time'))):
        x = 40 + k * 164
        s.append('<g class="cf-t" style="--k:%d"><rect x="%d" y="186" width="152" height="30" rx="15" fill="rgba(255,255,255,0.05)" stroke="rgba(196,255,73,0.55)" stroke-width="1.6"/>%s%s</g>' % (k, x, ico(ic, x + 20, 201, 16, LIME, 2), txt(x + 34, 206, lab, 12, '#fff', 0.92, 'start')))
    return '\n'.join(s)

def cost():
    X = lambda v: 40 + v * 480 / 350
    s = []
    for k, (y, lab, lo, hi, a, b, hot) in enumerate(((50, 'Clinic fee per month, medication not included', 100, 300, '$100', '$300', True),
                                                       (120, 'With generic cypionate on Alberta&rsquo;s list (about $15 CAD a month)', 115, 315, '$115', '$315', False))):
        s.append(txt(40, y - 14, lab, 12.5, '#c4ff49' if hot else '#fff', 0.95, 'start'))
        s.append('<path d="M40 %dH520" stroke="rgba(255,255,255,0.14)" stroke-width="14" stroke-linecap="round"/>' % (y + 6))
        s.append('<g class="cf-b" style="--k:%d"><rect x="%s" y="%d" width="%s" height="14" rx="7" fill="%s" fill-opacity="%s"/></g>' % (k, f(X(lo)), y - 1, f(X(hi) - X(lo)), LIME if hot else WHITE, 0.8 if hot else 0.6))
        s.append(txt(X(lo), y + 32, a, 11.5, '#fff', 0.9) + txt(X(hi), y + 32, b, 11.5, '#fff', 0.9))
    for k, (ic, lab) in enumerate((('calendar', 'Visit frequency'), ('pills', 'Extra medication'), ('leaf', 'Supplement support'))):
        x = 40 + k * 164
        s.append('<g class="cf-t" style="--k:%d"><rect x="%d" y="186" width="152" height="30" rx="15" fill="rgba(255,255,255,0.05)" stroke="rgba(196,255,73,0.55)" stroke-width="1.6"/>%s%s</g>' % (k, x, ico(ic, x + 20, 201, 16, LIME, 2), txt(x + 34, 206, lab, 12, '#fff', 0.92, 'start')))
    return '\n'.join(s)

def final():
    s = ['<defs><radialGradient id="fn-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.3"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><circle cx="180" cy="105" r="92" fill="url(#fn-g)"/>']
    s.append('<circle class="fn-ring fx" cx="180" cy="104" r="56" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append('<g class="fn-sh"><path d="M180 48l46 17v34c0 30-20 48-46 56-26-8-46-26-46-56V65z" fill="#142e14" stroke="#c4ff49" stroke-width="4" stroke-linejoin="round"/></g>')
    s.append(dr('M160 104l14 14 28-30', 0.4, 0.9, '#fff', 5))
    s.append(node(56, 70, 20, 'pin', 0.3, WHITE, isz=22)); s.append(node(304, 70, 20, 'video', 0.4, LIME, fill='#142e14', isz=22))
    return '\n'.join(s)

FAQMOTIF = '''<g class="fq-dp"><circle cx="28" cy="50" r="18" stroke="#c4ff49" stroke-width="4"/><path d="M28 40v12l7 5" stroke="#c4ff49" stroke-width="3" stroke-linecap="round"/></g>
<path class="dr" pathLength="1" style="--d:0.25;--dur:1.1s" d="M70 36c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82" cy="64" r="3" fill="#fff"/>
<g class="fq-fr" style="--k:0"><circle cx="104" cy="22" r="5" fill="#c4ff49"/></g><g class="fq-fr" style="--k:1"><circle cx="50" cy="20" r="4" fill="#c4ff49"/></g>'''

AUTHOR = {"@type": "Person", "@id": SITE + "/#alexander-tretjakov", "name": "Alexander Tretjakov", "jobTitle": "Founder",
          "worksFor": {"@id": SITE + "/#organization"}}
def ld_extra(ld):
    g = ld["@graph"]
    g.append(AUTHOR)
    for x in g:
        if x["@type"] == "WebPage":
            x["about"] = {"@type": "MedicalCondition", "name": "Low testosterone (male hypogonadism, andropause)"}
            x["spatialCoverage"] = {"@type": "City", "name": "Calgary", "containedInPlace": {"@type": "AdministrativeArea", "name": "Alberta"}}

slots = {"{{HERO}}": hero(), "{{HOW}}": how(), "{{LABS}}": labs(), "{{COST}}": cost(), "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "TRT and low testosterone care by telehealth for men in Calgary and Alberta",
      "TRT clinic Calgary", H1, slots, G, published="2026-10-28", modified="2026-10-28", author={"@id": SITE + "/#alexander-tretjakov"}, ld_extra=ld_extra)
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
