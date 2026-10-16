"""Build /workspace/pages/privacy/page.html (self-contained; paste into the GHL custom-code element of /privacy when approved).
Legal page: policy text lives verbatim in page.body.html (edit there, conservatively). This file: SEO, JSON-LD, SVG graphics, section icons.
Uses the shared page system (../_shared: base_head/base_motion/base_loader/base_tail, common.py, gfx.py, answer.css) but its own
assemble step, because (a) there is no FAQ (no FAQPage JSON-LD) and (b) the organization's location "Calgary, Alberta, Canada"
must stay in the policy, which the shared assemble() forbids. Run: python3 build.py"""
import sys, os, re, json, html
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "privacy"
TITLE = "Privacy Policy | Odin Health Labs"
DESC = "How Odin Health Labs collects, uses and protects personal and health information for telehealth clients in Canada and the USA, and your privacy rights."
OG_ALT = "Odin Health Labs Privacy Policy: how we protect personal information for telehealth clients in Canada and the USA"
EFFECTIVE, UPDATED = "2026-03-19", "2026-10-15"
EMAIL, PHONE = "office@odinhealthcoaching.com", "+1-587-324-8710"   # both copied from the live policy (Section 14)
assert len(TITLE) <= 60 and len(DESC) <= 160, (len(TITLE), len(DESC))

common.ICONS.update({
 "tag": '<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"/><path d="M8 8h.01"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "eye": '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "toggle": '<rect x="2" y="7" width="20" height="10" rx="5"/><circle cx="16" cy="12" r="3"/>',
 "trash": '<path d="M4 7h16"/><path d="M9 7V4h6v3"/><path d="M6 7l1 13h10l1-13"/><path d="M10 11v6M14 11v6"/>',
 "flag": '<path d="M5 21V4"/><path d="M5 4h12l-2 4 2 4H5"/>',
 "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
 "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
})

G = Gen()

# ---------- hero: shield + lock, data dots flow into the keyhole ----------
def hero():
    s = ['<defs><radialGradient id="pv-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.22"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs>',
         '<circle cx="240" cy="152" r="128" fill="url(#pv-g)"/>',
         '<circle class="hl-orb" cx="240" cy="152" r="104" fill="none" stroke="rgba(196,255,73,0.35)" stroke-width="2" stroke-dasharray="3 11" stroke-linecap="round"/>']
    srcs = [(64, 70, 'doc', (190, 118)), (64, 234, 'calendar', (190, 186)), (416, 70, 'chat', (290, 118)), (416, 234, 'heart', (290, 186))]
    for i, (x, y, ic, (ex, ey)) in enumerate(srcs):
        mx = (x + ex) / 2
        d, pts = path(('M', x, y), ('C', mx, y, mx, ey, ex, ey), ('L', 240, 160))
        s.append('<path d="%s" stroke="rgba(196,255,73,0.16)" stroke-width="3" fill="none" stroke-linecap="round"/>' % d)
        s.append(dr(d, 0.3 + i * 0.12, 1.1, LIME, 2.2))
        s.append(dot('hl-p%d fx' % i, 5.5, WHITE if i % 2 else LIME, ring=True))
        G.travel('hl-p%d' % i, pts, 4, 46, 8, delay='%ss' % f(-i * 2), rest=pts[0], rest_opacity=0)
    # shield
    s.append('<g class="pop t" style="--d:0.05"><path d="M240 70l66 24v54c0 44-28 70-66 82-38-12-66-38-66-82V94z" fill="#142e14" stroke="#c4ff49" stroke-width="3" stroke-linejoin="round"/></g>')
    # lock
    s.append(dr('M218 146v-14a22 22 0 0 1 44 0v14', 0.4, 0.9, WHITE, 4))
    s.append('<g class="pop t" style="--d:0.3"><rect x="206" y="144" width="68" height="54" rx="10" fill="#1d3f1d" stroke="#ffffff" stroke-opacity="0.85" stroke-width="3"/></g>')
    s.append('<circle class="hl-ring fx" cx="240" cy="166" r="13" fill="none" stroke="#c4ff49" stroke-width="2.4"/>')
    s.append('<g class="hl-key"><circle cx="240" cy="164" r="7" fill="#c4ff49"/><path d="M236.5 166h7l2 15h-11z" fill="#c4ff49"/></g>')
    for k, (sx, sy) in enumerate(((176, 66), (312, 60), (326, 214), (156, 220))):
        s.append('<path class="hl-sp" style="--k:%d" d="M%s %sv10M%s %sh10" stroke="#c4ff49" stroke-width="2.2" stroke-linecap="round"/>' % (k, sx, sy - 5, sx - 5, sy))
    for i, (x, y, ic, _) in enumerate(srcs):
        s.append(node(x, y, 26, ic, 0.2 + i * 0.12, WHITE if i % 2 else LIME, isz=26))
    return '\n'.join(s)

# ---------- sharing: you -> Odin -> service providers; "not sold" tag crossed ----------
def share():
    s = []
    hx, hy = 214, 132
    d0, p0 = path(('M', 74, hy), ('L', hx - 34, hy))
    s.append('<path d="%s" stroke="rgba(196,255,73,0.18)" stroke-width="3" fill="none"/>' % d0)
    s.append(dr(d0, 0.2, 0.7, LIME, 2.4))
    s.append(dot('sh-in fx', 6, LIME, ring=True)); G.travel('sh-in', p0, 2, 22, 7, rest=p0[0], rest_opacity=0)
    provs = [(40, 'calendar', 'Booking &amp; CRM'), (98, 'card', 'Payments'), (156, 'mail', 'Email tools'), (214, 'gauge', 'Analytics &amp; ads')]
    for i, (py, ic, lab) in enumerate(provs):
        d, pts = path(('M', hx + 34, hy), ('C', 320, hy, 320, py, 372, py))
        s.append('<path d="%s" stroke="rgba(196,255,73,0.16)" stroke-width="3" fill="none" stroke-linecap="round"/>' % d)
        s.append(dr(d, 0.5 + i * 0.1, 0.9, LIME, 2.2))
        s.append(dot('sh-o%d fx' % i, 5, WHITE))
        G.travel('sh-o%d' % i, pts, 26 + i * 4, 58 + i * 4, 7, rest=pts[-1], rest_opacity=0)
        s.append(node(394, py, 21, ic, 0.6 + i * 0.1, WHITE if i % 2 else LIME, isz=22))
        s.append('<text x="424" y="%s" font-size="15" fill="#ffffff" fill-opacity="0.9" class="pop" style="--d:%s">%s</text>' % (py + 5, f(0.7 + i * 0.1), lab))
    s.append(node(46, hy, 26, 'you', 0.1, WHITE, isz=26))
    s.append('<circle class="sh-ring fx" cx="%s" cy="%s" r="38" fill="none" stroke="#c4ff49" stroke-width="2"/>' % (hx, hy))
    s.append(node(hx, hy, 34, 'shield', 0.25, LIME, fill='#142e14', isz=34))
    s.append('<text x="%s" y="%s" font-size="14" fill="#c4ff49" text-anchor="middle" class="pop" style="--d:0.35">Odin Health Labs</text>' % (hx, hy + 56))
    # not sold
    s.append('<g class="pop t" style="--d:0.8"><circle cx="%s" cy="38" r="20" fill="none" stroke="rgba(255,255,255,0.6)" stroke-width="2.2" stroke-dasharray="4 5"/>%s</g>' % (hx, ico('tag', hx, 38, 20, 'rgba(255,255,255,0.75)', 1.7)))
    s.append('<g class="sh-x"><path d="M%s 24l28 28M%s 24l-28 28" stroke="#ff8a7a" stroke-width="3" stroke-linecap="round"/></g>' % (hx - 14, hx + 14))
    s.append('<text x="%s" y="43" font-size="15" fill="#ffffff" fill-opacity="0.9" class="pop" style="--d:0.9">Not sold</text>' % (hx + 30))
    return '\n'.join(s)

# ---------- section icon chips (48x48), each with ONE looping element ----------
SW = 'fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'
SI = {
 "intro":   '<path d="M12 6h18l8 8v28H12z"/><path d="M30 6v8h8"/><path d="M18 22h12M18 28h8"/><g class="si-a si-pop" style="color:#c4ff49"><path d="M30 31l8 3v4c0 4-3 6-8 7-5-1-8-3-8-7v-4z" fill="#142e14"/><path d="M27 38l2 2 4-4"/></g>',
 "collect": '<rect x="11" y="9" width="26" height="32" rx="3"/><path d="M19 6h10v6H19z"/><path d="M17 20h14M17 27h14M17 34h8"/><g class="si-a si-slide" style="color:#c4ff49"><circle cx="34" cy="20" r="2.6" fill="currentColor" stroke="none"/></g>',
 "use":     '<g class="si-a si-spin"><circle cx="24" cy="24" r="7"/><path d="M24 9v5M24 34v5M9 24h5M34 24h5M13.4 13.4l3.5 3.5M31.1 31.1l3.5 3.5M13.4 34.6l3.5-3.5M31.1 16.9l3.5-3.5"/></g><circle cx="24" cy="24" r="2" fill="#c4ff49" stroke="none"/>',
 "basis":   '<path d="M24 8v32M16 40h16"/><g class="si-a si-tip"><path d="M10 15h28"/><path d="M10 15l-4 10a4.5 4.5 0 0 0 8 0z" style="color:#c4ff49" stroke="#c4ff49"/><path d="M38 15l-4 10a4.5 4.5 0 0 0 8 0z"/></g>',
 "share":   '<circle cx="12" cy="24" r="5"/><circle cx="36" cy="12" r="5"/><circle cx="36" cy="36" r="5"/><path d="M16.5 21.5l15-7M16.5 26.5l15 7"/><g class="si-a si-hop" style="color:#c4ff49"><circle cx="24" cy="18" r="2.6" fill="currentColor" stroke="none"/></g>',
 "cookie":  '<path d="M38 26a14 14 0 1 1-16-16 5 5 0 0 0 7 6 5 5 0 0 0 9 10z"/><circle cx="18" cy="24" r="1.6" fill="currentColor"/><circle cx="25" cy="32" r="1.6" fill="currentColor"/><g class="si-a si-blink" style="color:#c4ff49"><circle cx="40" cy="12" r="2" fill="currentColor" stroke="none"/></g>',
 "health":  '<g class="si-a si-beat"><path d="M24 40s-14-9-14-20a8 8 0 0 1 14-5 8 8 0 0 1 14 5c0 11-14 20-14 20z"/></g><path d="M14 24h6l3-5 4 9 3-4h4" stroke="#c4ff49"/>',
 "retain":  '<circle cx="24" cy="24" r="15"/><path d="M24 24v-8"/><g class="si-a si-spin si-slow" style="color:#c4ff49"><path d="M24 24l7 4"/></g><circle cx="24" cy="24" r="1.8" fill="currentColor"/>',
 "rights":  '<circle cx="24" cy="24" r="15"/><g class="si-a si-pop" style="color:#c4ff49"><path d="M17 24.5l5 5 9-10"/></g>',
 "secure":  '<rect x="12" y="21" width="24" height="18" rx="3"/><path d="M17 21v-5a7 7 0 0 1 14 0v5"/><g class="si-a si-beat" style="color:#c4ff49"><circle cx="24" cy="29" r="2.6" fill="currentColor" stroke="none"/><path d="M24 31v4"/></g>',
 "links":   '<g class="si-a si-bob"><path d="M21 27a6 6 0 0 0 8.5 0l5-5a6 6 0 0 0-8.5-8.5l-1.5 1.5"/></g><path d="M27 21a6 6 0 0 0-8.5 0l-5 5a6 6 0 0 0 8.5 8.5l1.5-1.5" stroke="#c4ff49"/>',
 "children":'<path d="M24 7l14 5v10c0 9-6 15-14 18-8-3-14-9-14-18V12z"/><g class="si-a si-pop" style="color:#c4ff49"><path d="M18 24h12"/></g>',
 "changes": '<g class="si-a si-spin si-slow"><path d="M37 20a13 13 0 0 0-24-4"/><path d="M13 9v7h7"/><path d="M11 28a13 13 0 0 0 24 4"/><path d="M35 39v-7h-7"/></g>',
 "contact": '<rect x="8" y="13" width="32" height="22" rx="3"/><g class="si-a si-flap" style="color:#c4ff49"><path d="M8 15l16 11 16-11"/></g>',
}
def si(name):
    return '<svg class="si" viewBox="0 0 48 48" %s aria-hidden="true" focusable="false">%s</svg>' % (SW, SI[name])

ENV = ('<rect x="14" y="30" width="92" height="58" rx="8" fill="#142e14" stroke="#c4ff49" stroke-width="3"/>'
       '<path d="M16 34l44 30 44-30" stroke="#c4ff49" stroke-width="3" stroke-linejoin="round"/>'
       '<g class="ev-dot"><circle cx="60" cy="18" r="5" fill="#ffffff"/></g>'
       '<g class="ev-ck"><circle cx="98" cy="30" r="12" fill="#c4ff49"/><path d="M92 30l4 4 8-8" stroke="#0f240f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>')

# ---------- JSON-LD (WebPage + Organization + WebSite + BreadcrumbList; no FAQPage) ----------
def jsonld():
    url = SITE + "/" + SLUG
    g = [
     {"@type": "Organization", "@id": SITE + "/#organization", "name": "Odin Health Labs", "alternateName": "Odin Labs", "url": SITE + "/", "logo": LOGO,
      "address": {"@type": "PostalAddress", "addressLocality": "Calgary", "addressRegion": "AB", "addressCountry": "CA"},
      "contactPoint": {"@type": "ContactPoint", "contactType": "customer support", "email": EMAIL, "telephone": PHONE, "areaServed": ["CA", "US"]},
      "areaServed": [{"@type": "Country", "name": "Canada"}, {"@type": "Country", "name": "United States"}]},
     {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Odin Health Labs", "inLanguage": "en", "publisher": {"@id": SITE + "/#organization"}},
     {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": TITLE, "description": DESC, "inLanguage": "en",
      "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#organization"}, "about": {"@id": SITE + "/#organization"},
      "breadcrumb": {"@id": url + "#breadcrumb"}, "datePublished": EFFECTIVE, "dateModified": UPDATED, "primaryImageOfPage": OG_IMG},
     {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Privacy Policy", "item": url}]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, indent=2).replace("</", "<\\/")

def build():
    rd = lambda *p: open(os.path.join(*p), encoding="utf-8").read()
    slots = {"{{HERO}}": hero(), "{{SHARE}}": share(), "{{ENV}}": ENV}
    slots.update({"{{SI:%s}}" % k: si(k) for k in SI})
    body = rd(HERE, "page.body.html")
    body = re.sub(r"\{\{CI:(\w+):(\d+)\}\}", lambda m: ci(m.group(1), int(m.group(2))), body)
    st, mo = G.css()
    css = (rd(HERE, "..", "_shared", "answer.css") + "\n" + rd(HERE, "page.css")).replace("/*@GEN_STATIC*/", st).replace("/*@GEN_MOTION*/", mo)
    out = (rd(SHARED, "base_head.html") + rd(SHARED, "base_motion.html") + css
           + "\n</style>\n\n<script type=\"application/ld+json\">\n{{JSONLD}}\n</script>\n</head>\n\n"
           + rd(SHARED, "base_loader.html") + body + "\n" + rd(SHARED, "base_tail.html"))
    subs = {"{{TITLE}}": html.escape(TITLE, quote=False), "{{DESC}}": html.escape(DESC), "{{SITE}}": SITE, "{{PAGE_URL}}": SITE + "/" + SLUG,
            "{{OG_IMG}}": OG_IMG, "{{OG_ALT}}": html.escape(OG_ALT), "{{SLUG}}": SLUG, "{{JSONLD}}": jsonld(), "{{ICONS}}": icons_svg()}
    subs.update(slots)
    for k, v in subs.items():
        out = out.replace(k, v)
    assert "{{" not in out, re.findall(r"\{\{[\w:]+\}\}", out)
    # Calgary is allowed ONLY as the organization's location (policy header, Sections 1 and 14) and the JSON-LD address
    rest = re.sub(r"Odin-Health-Calgary|odinlabcalgary|Calgary, Alberta, Canada|\"addressLocality\": \"Calgary\"", "", out)
    assert "calgary" not in rest.lower(), "unexpected Calgary wording"
    for bad in ("owen-lowt", "/pemf", "hydrogen-inhalation", "marma-therapy", 'class="disclaimer"'):
        assert bad not in out, bad
    text = re.sub(r"<[^>]+>", " ", re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", "", out))
    for bad in ("pemf", "hydrogen", "marma", "therapy", "physician", "illustration only", "clinic"):
        assert bad not in text.lower(), bad
    open(os.path.join(HERE, "page.html"), "w", encoding="utf-8").write(out)
    print(SLUG, len(out.encode()), "bytes,", out.count("\n") + 1, "lines; title", len(TITLE), "desc", len(DESC))

build()
