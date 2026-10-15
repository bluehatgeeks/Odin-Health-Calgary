"""Shared builder for the rewritten Odin pages (health-coaching, supplements).
Same architecture as /workspace/pages/functional-health: self-contained page.html for the GHL custom-code element,
inline CDN CSS, nav/footer loaders, booking modal, guarded Mixpanel CTA tracking (function trackCta), motion system.
Each page folder has build.py (content, FAQ list, graphics), page.body.html (markup with {{SLOTS}}) and page.css (page graphics)."""
import json, html, re, os

SITE = "https://odinhealthlab.ca"
ASSESS = SITE + "/owen-lowt"
OG_IMG = "https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/og-home.png"
LOGO = "https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/zJaxLUStVkljpkn9qddd/media/69feb24f-b3d0-45e6-b747-20dc1d2eb84d.svg+xml"
SHARED = os.path.dirname(os.path.abspath(__file__))

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
 "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.8 2.8L16 9.5"/>',
 "chat": '<path d="M4 5h16a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1h-9l-5 4v-4H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/><path d="M8 10h8M8 13h5"/>',
 "leaf": '<path d="M5 19C5 10 10 5 20 4c0 10-5 15-13 15"/><path d="M5 19c3-5 6-8 10-10"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "pen": '<path d="M4 20l1-4L16 5a2 2 0 0 1 3 3L8 19z"/><path d="M14 7l3 3"/>',
 "bottle": '<path d="M9 3h6v3H9z"/><path d="M8 6h8a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1z"/><path d="M7 12h10M7 16h10"/>',
}

def icons_svg():
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>'
            + "".join('<symbol id="pi-%s" viewBox="0 0 24 24">%s</symbol>' % (k, v) for k, v in ICONS.items())
            + '</defs></svg>')

def ico(name, cx, cy, size, color, sw=1.8):
    return ('<g fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">'
            '<use href="#pi-%s" x="%.1f" y="%.1f" width="%d" height="%d"/></g>') % (color, sw, name, cx - size / 2, cy - size / 2, size, size)

def ci(name, k=0):
    """Card icon chip (animated by .ci pulse in page.css)."""
    return ('<svg class="ci" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true" focusable="false" style="--k:%d"><use href="#pi-%s"/></svg>' % (k, name))

def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))

def faq_html(faq):
    return "\n".join('<details class="faq-item">\n<summary><span class="faq-question">%s</span></summary>\n<p class="faq-answer">%s</p>\n</details>'
                     % (html.escape(q, quote=False), a) for q, a in faq)

def jsonld(slug, title, desc, about, crumb, faq):
    url = SITE + "/" + slug
    g = [
     {"@type": "Organization", "@id": SITE + "/#organization", "name": "Odin Health Labs", "alternateName": "Odin Labs",
      "url": SITE + "/", "logo": LOGO, "areaServed": [{"@type": "Country", "name": "Canada"}, {"@type": "Country", "name": "United States"}]},
     {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Odin Health Labs", "inLanguage": "en",
      "publisher": {"@id": SITE + "/#organization"}},
     {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "inLanguage": "en",
      "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#organization"},
      "about": {"@type": "Thing", "name": about}, "breadcrumb": {"@id": url + "#breadcrumb"}, "mainEntity": {"@id": url + "#faq"}},
     {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]},
     {"@type": "FAQPage", "@id": url + "#faq", "url": url, "inLanguage": "en",
      "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faq]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, indent=2).replace("</", "<\\/")

def assemble(page_dir, slug, title, desc, og_alt, ld, slots, extra_checks=()):
    rd = lambda *p: open(os.path.join(*p), encoding="utf-8").read()
    out = (rd(SHARED, "base_head.html") + rd(SHARED, "base_motion.html") + rd(page_dir, "page.css")
           + "\n</style>\n\n<script type=\"application/ld+json\">\n{{JSONLD}}\n</script>\n</head>\n\n"
           + rd(SHARED, "base_loader.html") + rd(page_dir, "page.body.html") + "\n" + rd(SHARED, "base_tail.html"))
    subs = {"{{TITLE}}": html.escape(title, quote=False), "{{DESC}}": html.escape(desc), "{{SITE}}": SITE,
            "{{PAGE_URL}}": SITE + "/" + slug, "{{ASSESS}}": ASSESS, "{{OG_IMG}}": OG_IMG, "{{OG_ALT}}": html.escape(og_alt),
            "{{SLUG}}": slug, "{{JSONLD}}": ld, "{{ICONS}}": icons_svg()}
    subs.update(slots)
    for k, v in subs.items():
        out = out.replace(k, v)
    assert "{{" not in out, re.findall(r"\{\{\w+\}\}", out)
    assert "calgary" not in re.sub(r"Odin-Health-Calgary|odinlabcalgary", "", out, flags=re.I).lower(), "Calgary wording left"
    # attribute-quote safety: title/desc used in attributes
    open(os.path.join(page_dir, "page.html"), "w", encoding="utf-8").write(out)
    print(slug, len(out.encode()), "bytes,", out.count("\n") + 1, "lines; title", len(title), "desc", len(desc))
