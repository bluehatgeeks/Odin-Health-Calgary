"""Build /workspace/pages/functional-health/page.html (self-contained, paste into the GHL custom-code block).
Edit page.template.part1/2/3.html (CSS, motion CSS, body+JS) or the lists below, then run: python3 build.py
FAQ HTML and FAQPage JSON-LD are generated from ONE list (FAQ) so they always match."""
import json, html, math, re, os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://odinhealthlab.ca"
PAGE_URL = SITE + "/functional-health"
ASSESS = SITE + "/owen-lowt"
OG_IMG = "https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/og-home.png"
LOGO = "https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/zJaxLUStVkljpkn9qddd/media/69feb24f-b3d0-45e6-b747-20dc1d2eb84d.svg+xml"

TITLE = "Functional Health for Men: Root Causes | Odin Health Labs"  # = GHL head title + seo-meta.md (iklinks 2026-10-19)
DESC = ("Functional health for men in Canada and the USA: find out why energy, drive, "
        "sleep and mood dropped, from sleep and stress to labs and your plan.")
assert len(TITLE) <= 60, len(TITLE)
assert len(DESC) <= 160, len(DESC)

FAQ = [
 ("What is functional health, and is it medical care?",
  "Functional health is how we describe our root-cause approach. We look at your sleep, stress, nutrition, training, weight and history together to understand why your energy, drive and mood dropped, and we build your plan around what we find. It works alongside your medical care: we can share your plan with your doctor and help you bring your results to appointments."),
 ("How is this different from a regular doctor\u2019s visit?",
  "We spend our time on the day-to-day picture: your routine, stress load, sleep, training and what you\u2019ve already tried. We then turn it into a plan and check in on it with you. It sits alongside your family doctor, and we can share your plan with them."),
 ("Do I need blood tests?",
  "Not necessarily at the start. The free assessment and your first call come first. If blood tests are worth doing, we\u2019ll explain which ones to ask about and help you understand the results."),
 ("What if I take medication?",
  "Tell us what you take on your first call and we factor it into your plan. We can also help you prepare questions to raise with your doctor about how it fits."),
 ("How quickly will I feel a difference?",
  "It depends on what is driving your symptoms. Part of your first call is agreeing on what to track so you can see for yourself whether the plan is working."),
 ("Is it fully online, and where do you work with men?",
  'Yes. Odin Health Labs is telehealth only and serves men across Canada and the USA. Everything happens by secure video or phone, so there are no clinic visits. See our <a href="%s/">low testosterone and andropause overview</a> for how the service works, or read our <a href="%s/privacy">Privacy Policy</a> for how we protect your information.' % (SITE, SITE)),
]

def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))

# ---------------- JSON-LD ----------------
ld = {
 "@context": "https://schema.org",
 "@graph": [
  {"@type": "Organization", "@id": SITE + "/#organization", "name": "Odin Health Labs", "alternateName": "Odin Labs",
   "url": SITE + "/", "logo": LOGO,
   "areaServed": [{"@type": "Country", "name": "Canada"}, {"@type": "Country", "name": "United States"}]},
  {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Odin Health Labs", "inLanguage": "en",
   "publisher": {"@id": SITE + "/#organization"}},
  {"@type": "WebPage", "@id": PAGE_URL + "#webpage", "url": PAGE_URL, "name": TITLE, "description": DESC,
   "inLanguage": "en", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#organization"},
   "about": {"@type": "Thing", "name": "Functional health approach to low testosterone (andropause) symptoms in men"},
   "breadcrumb": {"@id": PAGE_URL + "#breadcrumb"},
   "mainEntity": {"@id": PAGE_URL + "#faq"}},
  {"@type": "BreadcrumbList", "@id": PAGE_URL + "#breadcrumb", "itemListElement": [
     {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
     {"@type": "ListItem", "position": 2, "name": "Functional health", "item": PAGE_URL}]},
  {"@type": "FAQPage", "@id": PAGE_URL + "#faq", "url": PAGE_URL, "inLanguage": "en",
   "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in FAQ]},
 ],
}
ld_json = json.dumps(ld, ensure_ascii=False, indent=2).replace("</", "<\\/")
faq_html = "\n".join(
 '<details class="faq-item">\n<summary><span class="faq-question">%s</span></summary>\n<p class="faq-answer">%s</p>\n</details>' % (html.escape(q, quote=False), a)
 for q, a in FAQ)

# ---------------- icons (24x24 stroke glyphs) ----------------
ICONS = {
 "sleep": '<path d="M21 13.5A8.5 8.5 0 1 1 10.5 3a7 7 0 0 0 10.5 10.5z"/>',
 "stress": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "food": '<path d="M12 21c-4 0-7-3-7-8 0-4 3-6 5-6 1 0 1.5.5 2 .5s1-.5 2-.5c2 0 5 2 5 6 0 5-3 8-7 8z"/><path d="M12 7c0-2 1-3.5 3-4"/>',
 "train": '<path d="M6 7v10"/><path d="M3 9.5v5"/><path d="M18 7v10"/><path d="M21 9.5v5"/><path d="M6 12h12"/>',
 "body": '<path d="M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><path d="M8 9a4 4 0 0 1 8 0"/><path d="M12 9l2-2"/>',
 "labs": '<path d="M9 3h6"/><path d="M10 3v6l-5 9a2 2 0 0 0 1.8 3h10.4a2 2 0 0 0 1.8-3l-5-9V3"/><path d="M8 15h8"/>',
 "heart": '<path d="M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 11c0 5.5-7 10-7 10z"/><path d="M8 12h2l1.5-3 2 5 1.5-2h1.5"/>',
 "doc": '<path d="M7 3h10a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/><path d="M9 8l1.5 1.5L13 7"/><path d="M9 14l1.5 1.5L13 13"/><path d="M15 9h1M15 15h1"/>',
 "coach": '<path d="M9 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/><path d="M3 20c0-4 3-6 6-6s6 2 6 6"/><path d="M17 11a2.5 2.5 0 1 0 0-5"/><path d="M17 14c3 0 4.5 2 4.5 5"/>',
 "caps": '<path d="M10.5 20.5a4.95 4.95 0 0 1-7-7l10-10a4.95 4.95 0 0 1 7 7z"/><path d="M8.5 8.5l7 7"/>',
 "home": '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 "batt": '<path d="M4 8h13a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2z"/><path d="M22 11.5v2"/><path d="M6 11.5v2"/>',
 "flame": '<path d="M12 3c1 3 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 .3 1.2 1 2 2 2 0-3-1-5 1-8z"/>',
 "mood": '<circle cx="12" cy="12" r="9"/><path d="M8.5 15c1 1 2.3 1.5 3.5 1.5s2.5-.5 3.5-1.5"/><path d="M9 10v.01M15 10v.01"/>',
 "drop": '<path d="M12 3c4 5 6.5 8.5 6.5 12a6.5 6.5 0 0 1-13 0C5.5 11.5 8 8 12 3z"/>',
 "you": '<path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"/><path d="M4 21c0-4.5 3.6-7 8-7s8 2.5 8 7"/>',
}
icons_svg = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>'
  + "".join('<symbol id="fi-%s" viewBox="0 0 24 24">%s</symbol>' % (k, v) for k, v in ICONS.items())
  + '</defs></svg>')

def ico(name, cx, cy, size, color, sw=1.8):
    return ('<g fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">'
            '<use href="#fi-%s" x="%.1f" y="%.1f" width="%d" height="%d"/></g>') % (color, sw, name, cx - size / 2, cy - size / 2, size, size)

# ---------------- levers (equalizer) ----------------
lev = []
cols = [70, 175, 280, 385, 490]
names = ["sleep", "stress", "food", "train", "body"]
fs = [0.25, 0.40, 0.20, 0.35, 0.30]
ts = [0.80, 0.55, 0.70, 0.90, 0.60]
ps = [6.5, 7.5, 6.0, 8.0, 7.0]
for i, cx in enumerate(cols):
    v = "--f:%s;--t:%s;--p:%ss;--k:%d" % (fs[i], ts[i], ps[i], i)
    lev.append('<rect x="%d" y="30" width="10" height="120" rx="5" fill="rgba(255,255,255,0.08)"/>' % (cx - 5))
    lev.append('<rect class="lv-bar" x="%d" y="30" width="10" height="120" rx="5" fill="#c4ff49" fill-opacity="0.85" style="%s"/>' % (cx - 5, v))
    lev.append('<circle class="lv-knob" cx="%d" cy="150" r="13" fill="#0f240f" stroke="#fff" stroke-width="3" style="%s"/>' % (cx, v))
    lev.append('<circle cx="%d" cy="196" r="24" fill="#0f240f" stroke="rgba(196,255,73,0.5)" stroke-width="2"/>' % cx)
    lev.append(ico(names[i], cx, 196, 28, "#c4ff49"))
LEVERS = "\n".join(lev)

# ---------------- loop ----------------
CX, CY, R = 220, 150, 100
def pt(a, r=R):
    a = math.radians(a)
    return CX + r * math.sin(a), CY - r * math.cos(a)
loop = ['<circle class="lp-orbit" cx="220" cy="150" r="128" fill="none" stroke="rgba(196,255,73,0.18)" stroke-width="1.5" stroke-dasharray="3 10" stroke-linecap="round"/>',
        '<circle cx="220" cy="150" r="100" fill="none" stroke="rgba(196,255,73,0.1)" stroke-width="2"/>']
for i in range(4):
    a0, a1 = i * 90 + 24, i * 90 + 66
    (x0, y0), (x1, y1) = pt(a0), pt(a1)
    d = "M%.1f %.1f A100 100 0 0 1 %.1f %.1f" % (x0, y0, x1, y1)
    loop.append('<path class="dr" pathLength="1" style="--d:%.2f" d="%s" fill="none" stroke="#c4ff49" stroke-width="3.5" stroke-linecap="round"/>' % (0.2 + i * 0.35, d))
    # arrow head at end, tangent clockwise
    ar = math.radians(a1); tx, ty = math.cos(ar), math.sin(ar); nx, ny = -ty, tx
    bx, by = x1 - 9 * tx, y1 - 9 * ty
    loop.append('<path class="pop t" style="--d:%.2f" d="M%.1f %.1f L%.1f %.1f L%.1f %.1f" fill="none" stroke="#c4ff49" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>' % (0.9 + i * 0.2, bx + 6 * nx, by + 6 * ny, x1, y1, bx - 6 * nx, by - 6 * ny))
loop.append('<g class="lp-dot"><circle cx="220" cy="50" r="6" fill="#fff"/></g>')
loop.append('<circle class="lp-ring t" cx="220" cy="150" r="16" fill="none" stroke="#c4ff49" stroke-width="2"/><circle cx="220" cy="150" r="6" fill="#c4ff49"/>')
for i, nm in enumerate(["sleep", "stress", "body", "drop"]):
    x, y = pt(i * 90)
    loop.append('<g class="lp-n" style="--k:%d"><g class="lp-body"><circle cx="%.1f" cy="%.1f" r="30" fill="#0f240f" stroke="rgba(196,255,73,0.6)" stroke-width="2.2"/><circle class="lp-hi" cx="%.1f" cy="%.1f" r="30" fill="none" stroke="#c4ff49" stroke-width="3.5"/>%s</g></g>' % (i, x, y, x, y, ico(nm, x, y, 34, "#c4ff49", 1.6)))
LOOP = "\n".join(loop)

# ---------------- labs ----------------
LABS = '''<defs>
<clipPath id="vl-clip"><path d="M272 88V114L256 150Q252 168 268 168H292Q308 168 304 150L288 114V88Z"/></clipPath>
<radialGradient id="lb-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.35"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient>
</defs>
<ellipse cx="280" cy="130" rx="240" ry="110" fill="url(#lb-g)" opacity="0.5"/>
<path d="M50 130C110 130 130 60 200 60H400" fill="none" stroke="rgba(196,255,73,0.2)" stroke-width="4" stroke-linecap="round"/>
<path class="dr" pathLength="1" style="--d:0.1" d="M50 130C110 130 130 60 200 60H400" fill="none" stroke="#c4ff49" stroke-width="4" stroke-linecap="round"/>
<path class="pop" style="--d:0.5" d="M50 130C110 130 130 200 200 200H400" fill="none" stroke="rgba(255,255,255,0.6)" stroke-width="3" stroke-dasharray="3 9" stroke-linecap="round"/>
<path d="M280 88V62M280 168V198" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-dasharray="2 6" stroke-linecap="round"/>
<g class="pop t" style="--d:0"><circle cx="40" cy="130" r="11" fill="#142e14" stroke="#fff" stroke-width="2.5"/></g>
<path d="M272 88V114L256 150Q252 168 268 168H292Q308 168 304 150L288 114V88Z" fill="rgba(255,255,255,0.04)"/>
<g clip-path="url(#vl-clip)"><rect class="vl-liq" x="248" y="94" width="64" height="78" fill="#c4ff49" fill-opacity="0.75"/>
<circle class="vl-bub" style="--k:0" cx="274" cy="156" r="2.6" fill="#fff"/><circle class="vl-bub" style="--k:1" cx="288" cy="148" r="2" fill="#fff"/></g>
<path d="M272 88V114L256 150Q252 168 268 168H292Q308 168 304 150L288 114V88" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M266 88H294" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<g class="lb-end t" style="--k:0"><circle cx="440" cy="60" r="28" fill="#0f240f" stroke="#c4ff49" stroke-width="2.5"/>%s</g>
<g class="lb-end t" style="--k:1"><circle cx="440" cy="200" r="28" fill="#0f240f" stroke="rgba(255,255,255,0.7)" stroke-width="2.5" stroke-dasharray="4 5"/>%s</g>
<circle class="pk" style="--k:0" cx="150" cy="60" r="5.5" fill="#c4ff49"/>
<circle class="pk" style="--k:1" cx="150" cy="200" r="5.5" fill="#fff"/>''' % (ico("doc", 440, 60, 30, "#c4ff49"), ico("heart", 440, 200, 30, "#fff"))

# ---------------- related ----------------
REL = '''<path d="M250 95H142M310 95H418" stroke="rgba(196,255,73,0.35)" stroke-width="2.5" stroke-dasharray="3 9" stroke-linecap="round"/>
<g class="pop t" style="--d:0.1"><circle class="rl-cap" style="--k:0" cx="110" cy="95" r="30" fill="none" stroke="#c4ff49" stroke-width="2"/><circle cx="110" cy="95" r="30" fill="#0f240f" stroke="#c4ff49" stroke-width="2.5"/>%s</g>
<g class="pop t" style="--d:0.25"><circle class="rl-cap" style="--k:1" cx="450" cy="95" r="30" fill="none" stroke="#c4ff49" stroke-width="2"/><circle cx="450" cy="95" r="30" fill="#0f240f" stroke="#c4ff49" stroke-width="2.5"/><g class="rl-sway t">%s</g></g>
<circle class="rl-pk-l" cx="250" cy="95" r="4.5" fill="#c4ff49"/><circle class="rl-pk-r" cx="310" cy="95" r="4.5" fill="#fff"/>
<g class="pop t" style="--d:0"><circle cx="280" cy="95" r="36" fill="#0f240f" stroke="#fff" stroke-width="3"/>%s</g>''' % (ico("coach", 110, 95, 34, "#c4ff49", 1.6), ico("caps", 450, 95, 34, "#c4ff49", 1.6), ico("you", 280, 95, 40, "#fff", 1.6))

# ---------------- faq motif ----------------
FAQMOTIF = '''<circle cx="60" cy="50" r="44" stroke="rgba(196,255,73,0.2)" stroke-width="1.5" stroke-dasharray="2 7" stroke-linecap="round"/>
<g class="fq-lens"><circle cx="52" cy="46" r="26" fill="rgba(196,255,73,0.07)" stroke="#c4ff49" stroke-width="5"/><path d="M71 65L92 86" stroke="#c4ff49" stroke-width="7" stroke-linecap="round"/>
<path class="dr" pathLength="1" style="--d:0.3;--dur:1.1s" d="M44 40c0-5 4-8 8-8s8 3 8 7c0 4-3 5-5 7-2 1.5-3 3-3 6" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="52" cy="60" r="2.4" fill="#fff"/></g>
<circle class="fq-sp" style="--k:0" cx="100" cy="22" r="3.2" fill="#c4ff49"/><circle class="fq-sp" style="--k:1" cx="14" cy="30" r="2.6" fill="#fff"/><circle class="fq-sp" style="--k:2" cx="104" cy="58" r="2.4" fill="#9db39d"/>'''

# ---------------- compass ----------------
cp = ['<circle class="cp-halo" style="--k:0" cx="180" cy="100" r="78" fill="none" stroke="#c4ff49" stroke-width="2"/>',
      '<circle class="cp-halo" style="--k:1" cx="180" cy="100" r="78" fill="none" stroke="#c4ff49" stroke-width="2"/>',
      '<circle cx="180" cy="100" r="74" fill="#0f240f" stroke="rgba(196,255,73,0.55)" stroke-width="3"/>',
      '<circle cx="180" cy="100" r="58" fill="none" stroke="rgba(196,255,73,0.15)" stroke-width="1.5" stroke-dasharray="2 7" stroke-linecap="round"/>']
for k in range(12):
    a = k * 30; major = k % 3 == 0
    x0 = 180 + 70 * math.sin(math.radians(a)); y0 = 100 - 70 * math.cos(math.radians(a))
    r2 = 60 if major else 65
    x1 = 180 + r2 * math.sin(math.radians(a)); y1 = 100 - r2 * math.cos(math.radians(a))
    cp.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="%s" stroke-linecap="round"/>' % (x0, y0, x1, y1, "rgba(255,255,255,0.55)" if major else "rgba(255,255,255,0.28)", 3 if major else 2))
cp.append('<circle class="cp-sun" cx="180" cy="23" r="4.5" fill="#c4ff49"/>')
cp.append('<g class="cp-wob"><g class="cp-swing"><path d="M180 40L191 100H169Z" fill="#c4ff49"/><path d="M180 160L191 100H169Z" fill="#fff" fill-opacity="0.85"/><circle cx="180" cy="100" r="6" fill="#0f240f" stroke="#fff" stroke-width="2.5"/></g></g>')
COMPASS = "\n".join(cp)

# ---------------- assemble ----------------
tpl = "".join(open(os.path.join(HERE, "page.template.part%d.html" % i), encoding="utf-8").read() for i in (1, 2, 3))
out = tpl
for k, v in {"{{TITLE}}": html.escape(TITLE, quote=False), "{{DESC}}": html.escape(DESC), "{{SITE}}": SITE, "{{PAGE_URL}}": PAGE_URL,
             "{{ASSESS}}": ASSESS, "{{OG_IMG}}": OG_IMG, "{{JSONLD}}": ld_json, "{{FAQ}}": faq_html, "{{ICONS}}": icons_svg,
             "{{LEVERS}}": LEVERS, "{{LOOP}}": LOOP, "{{LABS}}": LABS, "{{REL}}": REL, "{{FAQMOTIF}}": FAQMOTIF, "{{COMPASS}}": COMPASS}.items():
    out = out.replace(k, v)
assert "{{" not in out, re.findall(r"\{\{\w+\}\}", out)
assert "calgary" not in re.sub(r"Odin-Health-Calgary|odinlabcalgary", "", out, flags=re.I).lower()  # only the repo/CDN names may contain it
open(os.path.join(HERE, "page.html"), "w", encoding="utf-8").write(out)
print(len(out.encode()), "bytes,", out.count("\n") + 1, "lines;", "title", len(TITLE), "desc", len(DESC))
