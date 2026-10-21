"""Helpers for the answer-style pages (trt-or-fix-causes-first, low-testosterone-labs-to-ask-for).
Same shared system as health-coaching/supplements (base_head/base_motion/base_loader/base_tail + common.py). Adds:
 - extra icons (merged into common.ICONS at import, common.py itself is untouched)
 - path()/Gen.travel(): coordinates -> SVG path + CSS keyframes for a dot riding the path
 - shared graphics used by both pages (hub, sources, step icons) and answer.css (answer box, sources list, hub/sources motion)
 - build(): expands {{CI:..}}, injects generated CSS, adds Article JSON-LD, calls common.assemble()"""
import math, os, re, json, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common
from common import *

SHARED = os.path.dirname(os.path.abspath(__file__))
common.ICONS.update({
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "tube": '<path d="M9 3h6"/><path d="M10 3v14a2 2 0 0 0 4 0V3"/><path d="M10 12h4"/>',
 "scale": '<path d="M12 3v17"/><path d="M6 21h12"/><path d="M4 7h16"/><path d="M4 7l-2.5 6a2.5 2.5 0 0 0 5 0z"/><path d="M20 7l-2.5 6a2.5 2.5 0 0 0 5 0z"/>',
 "question": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1 1-1 1.7"/><path d="M12 17v.01"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 "gauge": '<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-5"/>',
 "pulse": '<path d="M3 12h4l2-5 4 10 2-5h6"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "wine": '<path d="M8 3h8l-1 7a3 3 0 0 1-6 0z"/><path d="M12 13v8M8 21h8"/>',
 "wind": '<path d="M3 8h11a3 3 0 1 0-3-3"/><path d="M3 12h16a3 3 0 1 1-3 3"/><path d="M3 16h7"/>',
 "brain": '<path d="M12 4a3 3 0 0 0-5.5 1.5A3 3 0 0 0 4 9.5a3 3 0 0 0 1.5 5A3 3 0 0 0 9 19a3 3 0 0 0 3 1z"/><path d="M12 4a3 3 0 0 1 5.5 1.5A3 3 0 0 1 20 9.5a3 3 0 0 1-1.5 5A3 3 0 0 1 15 19a3 3 0 0 1-3 1z"/>',
 "gland": '<circle cx="9" cy="14" r="5"/><circle cx="16.5" cy="8.5" r="3.5"/>',
 "pills": '<path d="M10.5 20.5a4.95 4.95 0 0 1-7-7l10-10a4.95 4.95 0 0 1 7 7z"/><path d="M8.5 8.5l7 7"/>',
 "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 "list": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6h.01M4 12h.01M4 18h.01"/>',
})

def f(x):
    s = ('%.1f' % x).rstrip('0').rstrip('.')
    return s if s != '-0' else '0'

# ---------- paths and travelling dots ----------
def _cubic(p0, c1, c2, p1, n=14):
    out = []
    for i in range(1, n + 1):
        t = i / n; u = 1 - t
        out.append((u**3*p0[0] + 3*u*u*t*c1[0] + 3*u*t*t*c2[0] + t**3*p1[0], u**3*p0[1] + 3*u*u*t*c1[1] + 3*u*t*t*c2[1] + t**3*p1[1]))
    return out

def path(*segs, n=14):
    """segs: ('M',x,y) ('L',x,y) ('C',x1,y1,x2,y2,x,y) -> (d, sampled points)"""
    d, pts, cur = [], [], None
    for s in segs:
        if s[0] == 'M':
            cur = (s[1], s[2]); pts.append(cur); d.append('M%s %s' % (f(s[1]), f(s[2])))
        elif s[0] == 'L':
            cur = (s[1], s[2]); pts.append(cur); d.append('L%s %s' % (f(s[1]), f(s[2])))
        else:
            e = (s[5], s[6]); pts += _cubic(cur, (s[1], s[2]), (s[3], s[4]), e, n); cur = e
            d.append('C%s %s %s %s %s %s' % tuple(f(v) for v in s[1:]))
    return ' '.join(d), pts

class Gen:
    """Collects generated CSS. static = FINAL-state rules; motion = rules + keyframes placed inside the no-preference media block."""
    def __init__(s): s.static, s.motion = [], []
    def travel(s, cls, pts, a, b, dur, delay='0s', rest=None, fade=2.0, ease='linear', rest_opacity=1):
        """A dot (element with class cls, drawn at 0,0) rides pts between a% and b% of dur, invisible outside."""
        L = [0.0]
        for i in range(1, len(pts)):
            L.append(L[-1] + math.hypot(pts[i][0] - pts[i-1][0], pts[i][1] - pts[i-1][1]))
        tot = L[-1] or 1
        tr = lambda p: 'translate(%spx,%spx)' % (f(p[0]), f(p[1]))
        fr = ['0%% { opacity: 0; transform: %s; }' % tr(pts[0])]
        if a - fade > 0: fr.append('%s%% { opacity: 0; transform: %s; }' % (f(a - fade), tr(pts[0])))
        fr.append('%s%% { opacity: 1; transform: %s; }' % (f(a), tr(pts[0])))
        last = a
        for i in range(1, len(pts)):
            p = a + (b - a) * L[i] / tot
            if p <= last: p = last + 0.01
            fr.append('%s%% { transform: %s; }' % (('%.2f' % p).rstrip('0').rstrip('.'), tr(pts[i]))); last = p
        fr.append('%s%% { opacity: 1; transform: %s; }' % (f(b), tr(pts[-1])))
        fr.append('%s%% { opacity: 0; transform: %s; }' % (f(min(b + fade, 99.5)), tr(pts[-1])))
        fr.append('100%% { opacity: 0; transform: %s; }' % tr(pts[-1]))
        rp = rest if rest is not None else pts[-1]
        s.static.append('.pg .%s { transform: %s; opacity: %s; }' % (cls, tr(rp), rest_opacity))
        s.motion.append('.js-reveal .pg .%s { animation: kf-%s %ss %s infinite; animation-delay: %s; }\n@keyframes kf-%s {\n  %s\n}' % (cls, cls, f(dur), ease, delay, cls, '\n  '.join(fr)))
    def css(s):
        return '\n'.join(s.static), '\n'.join(s.motion)

# ---------- svg snippets ----------
LIME, WHITE, DARK = '#c4ff49', '#ffffff', '#0f240f'
def dr(d, delay=0, dur=None, stroke=LIME, sw=3, extra=''):
    return '<path class="dr" pathLength="1" style="--d:%s%s" d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"%s/>' % (delay, (';--dur:%ss' % dur) if dur else '', d, stroke, sw, extra)

def node(cx, cy, r, icon, delay=0, color=LIME, dashed=False, fill=DARK, isz=None, extra_cls=''):
    isz = isz or int(r * 1.15)
    return ('<g class="pop t %s" style="--d:%s"><circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="2.6"%s/>%s</g>'
            % (extra_cls, delay, f(cx), f(cy), f(r), fill, color if color != WHITE else 'rgba(255,255,255,0.75)', ' stroke-dasharray="4 5"' if dashed else '', ico(icon, cx, cy, isz, color, 1.7)))

def dot(cls, r=6, fill=LIME, ring=False):
    g = '<g class="%s"><circle r="%s" fill="%s"/>' % (cls, r, fill)
    if ring: g += '<circle r="%s" fill="none" stroke="%s" stroke-opacity="0.35" stroke-width="2"/>' % (r + 5, fill)
    return g + '</g>'

# ---------- shared graphics ----------
def hub(gen, nodes, center_icon='home'):
    """Hub and spokes: nodes = [(x, y, icon), ...] around (280,100) in a 560x200 box. Pulses flow in from every satellite."""
    s = ['<defs><radialGradient id="xh-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.2"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><circle cx="280" cy="100" r="92" fill="url(#xh-g)"/>']
    for i, (x, y, ic) in enumerate(nodes):
        d, pts = path(('M', x, y), ('L', 280, 100))
        s.append('<path d="%s" stroke="rgba(196,255,73,0.18)" stroke-width="3" fill="none" stroke-linecap="round"/>' % d)
        s.append(dr(d, 0.4 + i * 0.12, 1.0, LIME, 2.4))
        s.append(dot('xh-p%d fx' % i, 5, WHITE))
        gen.travel('xh-p%d' % i, pts, 6, 40, 8, delay='%ss' % f(-i * 2), rest=pts[0], rest_opacity=0)
    s.append('<circle class="xh-ring fx" cx="280" cy="100" r="40" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(node(280, 100, 32, center_icon, 0.1, LIME, fill='#142e14', isz=34))
    for i, (x, y, ic) in enumerate(nodes):
        s.append(node(x, y, 26, ic, 0.3 + i * 0.12, WHITE if i % 2 else LIME, isz=28))
    return '\n'.join(s)

def sources_fig():
    """Three papers fan out and tuck back; a tick draws on the top one."""
    s = []
    for k, (rot, dx) in enumerate(((-9, -46), (0, 0), (9, 46))):
        s.append('<g class="so-card" style="--k:%d;--rot:%sdeg;--dx:%spx"><g class="pop t" style="--d:%s"><rect x="150" y="22" width="68" height="92" rx="9" fill="%s" stroke="%s" stroke-width="2.4"/><path d="M164 44h40M164 56h40M164 68h26" stroke="rgba(255,255,255,0.55)" stroke-width="2.4" stroke-linecap="round"/></g></g>'
                 % (k, rot, dx, 0.1 + k * 0.12, '#142e14' if k != 1 else '#173617', LIME if k == 1 else 'rgba(255,255,255,0.6)'))
    s.append(dr('M168 92l7 7 14-15', 0.7, 0.8, LIME, 3.4))
    return '\n'.join(s)

def step_icons(defs):
    """defs: dict slot -> svg inner string (48x48 viewBox)."""
    return defs

# ---------- build ----------
def build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, about, crumb, headline, slots, gen, published="2026-10-15", modified=None):
    rd = lambda *p: open(os.path.join(*p), encoding="utf-8").read()
    body = rd(HERE, "page.body.html")
    body = re.sub(r"\{\{CI:(\w+):(\d+)\}\}", lambda m: ci(m.group(1), int(m.group(2))), body)
    st, mo = gen.css()
    css = rd(SHARED, "answer.css") + "\n" + rd(HERE, "page.css")
    css = css.replace("/*@GEN_STATIC*/", st).replace("/*@GEN_MOTION*/", mo)
    tmp = os.path.join(HERE, ".tmp"); os.makedirs(tmp, exist_ok=True)
    open(os.path.join(tmp, "page.body.html"), "w", encoding="utf-8").write(body)
    open(os.path.join(tmp, "page.css"), "w", encoding="utf-8").write(css)
    ld = json.loads(jsonld(SLUG, TITLE, DESC, about, crumb, FAQ))
    url = SITE + "/" + SLUG
    ld["@graph"].insert(3, {"@type": "Article", "@id": url + "#article", "headline": headline, "description": DESC, "inLanguage": "en",
        "mainEntityOfPage": {"@id": url + "#webpage"}, "author": {"@id": SITE + "/#organization"}, "publisher": {"@id": SITE + "/#organization"},
        "datePublished": published, "dateModified": modified or published, "image": OG_IMG})
    ldj = json.dumps(ld, ensure_ascii=False, indent=2).replace("</", "<\\/")
    all_slots = dict(slots); all_slots["{{FAQ}}"] = faq_html(FAQ)
    assemble(tmp, SLUG, TITLE, DESC, OG_ALT, ldj, all_slots)
    shutil.copy(os.path.join(tmp, "page.html"), os.path.join(HERE, "page.html"))
    shutil.rmtree(tmp)
