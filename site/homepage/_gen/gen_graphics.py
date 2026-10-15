# Generates the per-section motion graphics (HTML fragments) and patches home.template.html.
# Run once from the v2 template: python3 _gen/gen_graphics.py  (reads home.template.v2.html, writes home.template.html)
import math, re

L = '#c4ff49'; G = '#9db39d'; C = '#142e14'; D = '#0f240f'

def pl(d):  # draw-on path helper (pathLength=1)
    return d

# ---------- shared icon symbols (causes nodes + cards) ----------
ICONS = {
 1: '<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-5"/><path d="M3 20h18"/>',                 # metabolic strain: gauge
 2: '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',                                                      # stress/illness: bolt
 3: '<rect x="3" y="8" width="18" height="8" rx="4" transform="rotate(-45 12 12)"/><path d="M8.5 8.5l7 7"/>',  # meds: capsule
 4: '<path d="M2 12c2.5-6 4.5-6 7 0s4.5 6 7 0 3-3 6-3"/>',                                          # other hormones: wave
 5: '<circle cx="9" cy="12" r="5"/><circle cx="15" cy="12" r="5"/>',                                # testicular: overlapping circles
 6: '<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/>',  # pituitary: signal
 7: '<path d="M8 3c0 4 8 6 8 9s-8 5-8 9"/><path d="M16 3c0 4-8 6-8 9s8 5 8 9"/><path d="M9.2 7.5h5.6M9.2 16.5h5.6"/>',  # structural/genetic: helix
}
SYMBOLS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>'
  + ''.join('<symbol id="ci-%d" viewBox="0 0 24 24">%s</symbol>' % (k, v) for k, v in ICONS.items())
  + '</defs></svg>')

def ci(k):
    return ('<svg class="ci" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true" focusable="false"><use href="#ci-%d"/></svg>' % k)

def pt(p): return '%.1f' % p

# ---------- SYMPTOMS: a day of energy (curve sags, sun fades to moon, battery cells drop) ----------
SY_PATH = 'M20 52 C90 40 150 34 210 44 C280 58 320 100 380 112 C450 124 520 120 620 118'
def sym():
    cells = ''.join('<rect class="sy-c sy-c%d" x="%d" y="26" width="14" height="18" rx="3" fill="%s"/>' % (i, 449 + i * 18, L) for i in range(4))
    rays = ''.join('<path d="M%s %s L%s %s"/>' % (pt(50 + 13 * math.cos(a)), pt(34 + 13 * math.sin(a)), pt(50 + 19 * math.cos(a)), pt(34 + 19 * math.sin(a)))
                   for a in [i * math.pi / 4 for i in range(8)])
    return ('''<figure class="mg mg--sym reveal" aria-hidden="true" data-live style="--ar:640/150">
<svg class="mg-svg" viewBox="0 0 640 150" focusable="false">
<defs>
<linearGradient id="sy-g" gradientUnits="userSpaceOnUse" x1="20" y1="0" x2="620" y2="0"><stop offset="0" stop-color="%(L)s"/><stop offset="0.45" stop-color="%(L)s"/><stop offset="0.75" stop-color="%(G)s"/><stop offset="1" stop-color="%(G)s"/></linearGradient>
<linearGradient id="sy-a" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%(L)s" stop-opacity="0.18"/><stop offset="1" stop-color="%(L)s" stop-opacity="0"/></linearGradient>
<radialGradient id="sy-glow"><stop offset="0" stop-color="%(L)s" stop-opacity="0.5"/><stop offset="1" stop-color="%(L)s" stop-opacity="0"/></radialGradient>
</defs>
<g stroke="rgba(255,255,255,0.07)" stroke-width="1"><path d="M20 62H620M20 92H620M20 122H620"/></g>
<g stroke="rgba(255,255,255,0.18)" stroke-width="1.5" stroke-linecap="round"><path d="M20 134H620"/><path d="M20 130v8M170 130v8M320 130v8M470 130v8M620 130v8"/></g>
<path d="%(P)s" fill="none" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="3 7" stroke-linecap="round"/>
<g class="sy-stage">
<path class="sy-area" d="%(P)s V134 H20 Z" fill="url(#sy-a)"/>
<path class="sy-draw" pathLength="1" d="%(P)s" fill="none" stroke="url(#sy-g)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<g class="sy-sun"><g class="sy-rays" fill="none" stroke="%(L)s" stroke-width="2" stroke-linecap="round">%(R)s</g><circle cx="50" cy="34" r="8" fill="%(L)s"/></g>
<path class="sy-moon" d="M590 24a11 11 0 1 0 12 15a9 9 0 0 1 -12 -15z" fill="%(G)s"/>
<g><rect x="441" y="20" width="84" height="30" rx="7" fill="none" stroke="%(G)s" stroke-width="2"/><rect x="527" y="29" width="5" height="12" rx="2" fill="%(G)s"/>%(cells)s</g>
<g class="sy-ringg"><circle class="sy-ring" cx="380" cy="112" r="10" fill="none" stroke="%(G)s" stroke-width="2"/></g>
<circle class="sy-dot" cx="0" cy="0" r="5" fill="#fff"/>
</g>
</svg>
<div class="mg-leg mg-leg--spread"><span>Morning</span><span>Afternoon</span><span>Night</span></div>
<figcaption class="mg-cap">Illustration only. Not real data.</figcaption>
</figure>''' % dict(L=L, G=G, P=SY_PATH, R=rays, cells=cells))

# ---------- EXPLAIN: three-way comparison ----------
CM = {
 'age': 'M40 90 C160 96 300 120 530 150',
 'andro': 'M40 88 C90 80 130 100 180 96 S250 120 290 126 S380 150 430 152 S500 170 530 174',
 'low': 'M40 92 C130 92 210 100 270 140 S420 196 530 200',
}
def cmp_():
    ticks = ''.join('<path d="M%d 226v8"/>' % x for x in range(40, 531, 70))
    return ('''<figure class="mg mg--cmp reveal" aria-hidden="true" data-live style="--ar:560/260">
<svg class="mg-svg" viewBox="0 0 560 260" focusable="false">
<defs><radialGradient id="cm-ov"><stop offset="0" stop-color="%(L)s" stop-opacity="0.32"/><stop offset="1" stop-color="%(L)s" stop-opacity="0"/></radialGradient></defs>
<g stroke="rgba(255,255,255,0.07)" stroke-width="1"><path d="M40 60H530M40 110H530M40 160H530M40 210H530"/></g>
<g class="cm-axisg" stroke="rgba(255,255,255,0.28)" stroke-width="2" stroke-linecap="round" fill="none"><path class="cm-axis" pathLength="1" d="M40 30V226H532"/><path d="M526 220l8 6-8 6"/><g stroke-width="1.5">%(ticks)s</g></g>
<ellipse class="cm-ov" cx="120" cy="92" rx="104" ry="36" fill="url(#cm-ov)"/>
<g class="cm-stage" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path class="cm-line cm-age" pathLength="1" d="%(age)s" stroke="%(G)s" stroke-width="3.5"/>
<path class="cm-line cm-andro" pathLength="1" d="%(andro)s" stroke="#fff" stroke-width="3"/>
<path class="cm-line cm-low" pathLength="1" d="%(low)s" stroke="%(L)s" stroke-width="4.5"/>
<g class="cm-sym" fill="#fff"><circle cx="180" cy="96" r="3.5"/><circle cx="290" cy="126" r="3.5"/><circle cx="430" cy="152" r="3.5"/></g>
<circle class="cm-dot cm-dot-age" cx="0" cy="0" r="5" fill="%(G)s"/>
<circle class="cm-dot cm-dot-andro" cx="0" cy="0" r="5" fill="#fff"/>
<circle class="cm-dot cm-dot-low" cx="0" cy="0" r="5.5" fill="%(L)s"/>
</g>
</svg>
<div class="mg-leg" style="justify-content:center"><span><i class="sw sw--low"></i>Low testosterone</span><span><i class="sw sw--andro"></i>Andropause</span><span><i class="sw sw--age"></i>Getting older</span></div>
<figcaption class="mg-cap">Illustration only. Not real data.</figcaption>
</figure>''' % dict(L=L, G=G, ticks=ticks, **CM))

# ---------- WHO: network ----------
HUB = (320, 110)
LEFT = [(62, 52), (112, 152), (194, 68), (232, 166)]
RIGHT = [(578, 58), (528, 150), (448, 72), (408, 170)]
def person(x, y):
    return ('<circle cx="%d" cy="%d" r="5.5"/><path d="M%d %dC%d %d %d %d %d %d"/>' % (x, y - 5, x - 9, y + 11, x - 9, y + 2, x + 9, y + 2, x + 9, y + 11))
def who():
    out = []; k = 0
    nodes = [(p, 'l') for p in LEFT] + [(p, 'r') for p in RIGHT]
    links = ''; pk = ''; nd = ''
    for i, ((x, y), side) in enumerate(nodes):
        mx, my = (HUB[0] + x) / 2, (HUB[1] + y) / 2
        cy = my + (-26 if y < HUB[1] else 26)
        d = 'M%d %d Q%s %s %d %d' % (HUB[0], HUB[1], pt(mx), pt(cy), x, y)
        links += '<path class="wh-link" style="--k:%d" d="%s" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round"/>' % (i, d, L)
        pk += '<circle class="wh-pk" style="--k:%d;offset-path:path(\'%s\')" r="3.5" fill="#fff"/>' % (i, d)
        nd += ('<g class="wh-n" style="--k:%d"><circle class="wh-ring t" cx="%d" cy="%d" r="19" fill="none" stroke="%s" stroke-width="1.5"/>'
               '<circle cx="%d" cy="%d" r="19" fill="%s" stroke="rgba(196,255,73,0.5)" stroke-width="1.5"/>'
               '<g fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round">%s</g></g>') % (i, x, y, L, x, y, D, L, person(x, y))
    fl = ''.join('<circle class="mg-fl" style="--d:%d" cx="%d" cy="%d" r="2.2" fill="%s"/>' % (i, x, y, L)
                 for i, (x, y) in enumerate([(30, 120), (150, 24), (270, 196), (370, 28), (610, 130), (480, 200)]))
    return ('''<figure class="mg mg--who reveal" aria-hidden="true" data-live style="--ar:640/220">
<svg class="mg-svg" viewBox="0 0 640 220" focusable="false">
<g fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="1"><ellipse cx="320" cy="110" rx="300" ry="100"/><ellipse cx="320" cy="110" rx="190" ry="64"/></g>
<g class="wh-fl">%(fl)s</g>
<g class="wh-base" opacity="0.2">%(links)s</g>
<g class="wh-flow">%(links2)s</g>
<g class="wh-pks">%(pk)s</g>
%(nd)s
<g class="wh-hub"><circle class="wh-hring t" cx="320" cy="110" r="40" fill="none" stroke="%(L)s" stroke-width="2"/>
<rect x="284" y="84" width="72" height="52" rx="11" fill="%(D)s" stroke="%(L)s" stroke-width="2.5"/>
<g fill="none" stroke="%(L)s" stroke-width="2.2" stroke-linecap="round"><circle cx="320" cy="105" r="7"/><path d="M306 126C306 115 334 115 334 126"/></g>
<circle class="wh-live" cx="345" cy="94" r="2.5" fill="%(L)s"/></g>
</svg>
<div class="mg-leg mg-leg--spread"><span>Canada</span><span>USA</span></div>
</figure>''' % dict(L=L, D=D, fl=fl, links=links, links2=links.replace('wh-link', 'wh-link2'), pk=pk, nd=nd))

# ---------- CAUSES: radial diagram ----------
def causes():
    cx, cy, rx, ry = 280, 170, 212, 120
    spokes = nodes = ''
    for i in range(7):
        a = math.radians(-90 + i * 360 / 7)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        dx, dy = x - cx, y - cy; n = math.hypot(dx, dy)
        sx, sy = cx + dx / n * 40, cy + dy / n * 40       # start at hub edge
        ex, ey = x - dx / n * 32, y - dy / n * 32          # end at node edge
        d = 'M%s %s L%s %s' % (pt(sx), pt(sy), pt(ex), pt(ey))
        spokes += ('<path d="%s" fill="none" stroke="rgba(196,255,73,0.2)" stroke-width="2" stroke-linecap="round"%s/>' % (d, ' stroke-dasharray="4 5"' if i >= 4 else '')
                   + '<path class="cau-spoke" style="--k:%d" pathLength="1" d="%s" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (i, d, L))
        phys = i >= 4
        nodes += ('<g class="cau-n" style="--k:%(i)d"><circle class="cau-glow t" cx="%(x)s" cy="%(y)s" r="44" fill="url(#cau-glow)"/>'
                  '<g class="cau-body t"><circle cx="%(x)s" cy="%(y)s" r="30" fill="%(D)s" stroke="%(st)s" stroke-width="2.2"%(da)s/>'
                  '<circle class="cau-hi" cx="%(x)s" cy="%(y)s" r="30" fill="none" stroke="%(L)s" stroke-width="3.5"/>'
                  '<g fill="none" stroke="%(ic)s" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><use href="#ci-%(n)d" x="%(ux)s" y="%(uy)s" width="34" height="34"/></g></g></g>') % dict(
                  i=i, x=pt(x), y=pt(y), D=D, L=L, n=i + 1, ux=pt(x - 17), uy=pt(y - 17),
                  st=('rgba(255,255,255,0.45)' if phys else 'rgba(196,255,73,0.6)'), da=(' stroke-dasharray="5 4"' if phys else ''), ic=('#e8efe8' if phys else L))
    return ('''<figure class="mg mg--cau reveal" aria-hidden="true" style="--ar:560/340">
<svg class="mg-svg" viewBox="0 0 560 340" focusable="false">
<defs><radialGradient id="cau-glow"><stop offset="0" stop-color="%(L)s" stop-opacity="0.45"/><stop offset="1" stop-color="%(L)s" stop-opacity="0"/></radialGradient></defs>
<ellipse class="cau-orbit" cx="280" cy="170" rx="212" ry="120" fill="none" stroke="rgba(196,255,73,0.22)" stroke-width="1.5" stroke-dasharray="3 9" stroke-linecap="round"/>
%(spokes)s
%(nodes)s
<g class="cau-hub"><circle class="cau-hring t" cx="280" cy="170" r="36" fill="none" stroke="%(L)s" stroke-width="2"/>
<circle cx="280" cy="170" r="36" fill="%(D)s" stroke="%(L)s" stroke-width="2.5"/>
<path d="M280 150c9 11 14 18 14 25a14 14 0 0 1-28 0c0-7 5-14 14-25z" fill="none" stroke="%(L)s" stroke-width="2.5" stroke-linejoin="round"/></g>
</svg>
<div class="mg-leg" style="justify-content:center"><span><i class="sw sw--low"></i>Four we build a plan around</span><span><i class="sw sw--phys"></i>Three that need a physician</span></div>
</figure>''' % dict(L=L, D=D, spokes=spokes, nodes=nodes))

# ---------- HOW IT WORKS: step icons ----------
STEP_ICONS = {
 1: '''<svg class="hi" viewBox="0 0 48 48" fill="none" stroke="%(L)s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="10" y="8" width="28" height="34" rx="5"/><path d="M18 8V6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v2"/><path d="M17 20h14M17 27h8"/><path class="hi-check" pathLength="1" d="M17 35l4 4 9-9" stroke="#fff"/></svg>''',
 2: '''<svg class="hi" viewBox="0 0 48 48" fill="none" stroke="%(L)s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="4" y="12" width="29" height="24" rx="5"/><path d="M33 21l11-6v18l-11-6"/><circle cx="18.5" cy="22" r="3.5"/><path d="M12 31c0-7 13-7 13 0"/><path class="hi-w hi-w1" d="M38 8a9 9 0 0 1 6 5" stroke-width="2"/><path class="hi-w hi-w2" d="M36 4a14 14 0 0 1 10 8" stroke-width="2"/></svg>''',
 3: '''<svg class="hi" viewBox="0 0 48 48" fill="none" stroke="%(L)s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect class="hi-bar hi-b1" x="6" y="30" width="9" height="12" rx="2.5"/><rect class="hi-bar hi-b2" x="19.5" y="21" width="9" height="21" rx="2.5"/><rect class="hi-bar hi-b3" x="33" y="10" width="9" height="32" rx="2.5"/><path class="hi-flag" d="M37.5 6V2" stroke="#fff"/></svg>''',
 4: '''<svg class="hi" viewBox="0 0 48 48" fill="none" stroke="%(L)s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><g class="hi-rot"><path d="M40 24a16 16 0 0 1-27.5 11"/><path d="M8 24a16 16 0 0 1 27.5-11"/><path d="M39 6v8h-8"/><path d="M9 42v-8h8"/></g><circle cx="24" cy="24" r="4" fill="#fff" stroke="none"/></svg>''',
}
def step_icon(n): return STEP_ICONS[n] % dict(L=L)

# ---------- ABOUT: telehealth motif ----------
def about():
    def bars(x0, cls):
        hs = [0.5, 1, 0.65, 0.9, 0.45]
        return ''.join('<rect class="ab-bar %s" style="--k:%d;--h:%s" x="%d" y="150" width="6" height="22" rx="3"/>' % (cls, i, hs[i], x0 + i * 11) for i in range(5))
    return ('''<figure class="mg mg--abt reveal" aria-hidden="true" data-live style="--ar:560/270">
<svg class="mg-svg" viewBox="0 0 560 270" focusable="false">
<defs><radialGradient id="ab-glow"><stop offset="0" stop-color="%(L)s" stop-opacity="0.28"/><stop offset="1" stop-color="%(L)s" stop-opacity="0"/></radialGradient></defs>
<ellipse class="ab-glow" cx="280" cy="125" rx="250" ry="120" fill="url(#ab-glow)"/>
<path d="M120 212H440l-22 18H142z" fill="%(D)s" stroke="rgba(196,255,73,0.5)" stroke-width="2.2" stroke-linejoin="round"/>
<rect x="150" y="34" width="260" height="168" rx="16" fill="%(D)s" stroke="%(L)s" stroke-width="3"/>
<path d="M280 46V190" stroke="rgba(196,255,73,0.25)" stroke-width="2" stroke-dasharray="3 6"/>
<rect class="ab-pane ab-pane-l" x="158" y="42" width="116" height="152" rx="10" fill="rgba(196,255,73,0.1)"/>
<rect class="ab-pane ab-pane-r" x="286" y="42" width="116" height="152" rx="10" fill="rgba(196,255,73,0.1)"/>
<g fill="none" stroke="%(L)s" stroke-width="3" stroke-linecap="round"><circle cx="216" cy="95" r="15"/><path d="M190 140C190 112 242 112 242 140"/><circle cx="344" cy="95" r="15"/><path d="M318 140C318 112 370 112 370 140"/></g>
<g fill="%(L)s">%(bl)s%(br)s</g>
<circle class="ab-ring t" cx="172" cy="56" r="4" fill="none" stroke="%(L)s" stroke-width="2"/><circle cx="172" cy="56" r="4" fill="%(L)s"/>
<g class="ab-b" style="--k:0"><path d="M30 64h84a12 12 0 0 1 12 12v22a12 12 0 0 1-12 12H62l-14 12v-12H30a12 12 0 0 1-12-12V76a12 12 0 0 1 12-12z" fill="%(D)s" stroke="%(L)s" stroke-width="2.2" stroke-linejoin="round"/><g fill="%(L)s"><circle class="ab-td" style="--k:0" cx="52" cy="88" r="4"/><circle class="ab-td" style="--k:1" cx="72" cy="88" r="4"/><circle class="ab-td" style="--k:2" cx="92" cy="88" r="4"/></g></g>
<g class="ab-b" style="--k:1"><path d="M446 104h84a12 12 0 0 1 12 12v22a12 12 0 0 1-12 12h-18v12l-14-12h-52a12 12 0 0 1-12-12v-22a12 12 0 0 1 12-12z" fill="%(D)s" stroke="%(L)s" stroke-width="2.2" stroke-linejoin="round" transform="translate(-14 0)"/><g stroke="%(L)s" stroke-width="3" stroke-linecap="round" transform="translate(-14 0)"><path d="M446 124h60M446 138h36"/></g></g>
<g class="ab-b" style="--k:2"><path d="M44 164h70a12 12 0 0 1 12 12v14a12 12 0 0 1-12 12H72l-14 12v-12H44a12 12 0 0 1-12-12v-14a12 12 0 0 1 12-12z" fill="%(D)s" stroke="rgba(196,255,73,0.6)" stroke-width="2.2" stroke-linejoin="round"/><g stroke="rgba(196,255,73,0.8)" stroke-width="3" stroke-linecap="round"><path d="M50 183h50"/></g></g>
</svg>
</figure>''' % dict(L=L, D=D, bl=bars(194, 'ab-bar-l'), br=bars(322, 'ab-bar-r')))

# ---------- FAQ motif ----------
def faq():
    return ('''<svg class="fq-motif" viewBox="0 0 120 100" fill="none" aria-hidden="true" focusable="false">
<circle cx="60" cy="50" r="44" stroke="rgba(196,255,73,0.2)" stroke-width="1.5" stroke-dasharray="2 7" stroke-linecap="round"/>
<g class="fq-orb"><circle cx="60" cy="6" r="4.5" fill="%(L)s"/><circle cx="98" cy="72" r="3.5" fill="#fff"/><circle cx="22" cy="72" r="3" fill="%(G)s"/></g>
<g class="fq-stage"><path class="fq-q" pathLength="1" d="M45 36c0-9 7-15 15-15s15 6 15 14c0 7-6 10-10 13-4 3-5 5-5 11" stroke="%(L)s" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle class="fq-qd t" cx="60" cy="76" r="3.4" fill="%(L)s"/></g>
<g transform="translate(14 62) scale(.3)"><g class="fq-fl" style="--k:0"><path d="M45 36c0-9 7-15 15-15s15 6 15 14c0 7-6 10-10 13-4 3-5 5-5 11M60 76v.1" stroke="%(L)s" stroke-width="9" stroke-linecap="round"/></g></g>
<g transform="translate(92 30) scale(.26)"><g class="fq-fl" style="--k:1"><path d="M45 36c0-9 7-15 15-15s15 6 15 14c0 7-6 10-10 13-4 3-5 5-5 11M60 76v.1" stroke="#fff" stroke-width="9" stroke-linecap="round"/></g></g>
</svg>''' % dict(L=L, G=G))

# ---------- FINAL CTA: rising curve echo ----------
FI = 'M20 142 H150 C230 142 262 130 322 100 C392 66 462 36 576 28'
def final():
    rays = ''.join('<path d="M%s %s L%s %s"/>' % (pt(576 + 17 * math.cos(a)), pt(28 + 17 * math.sin(a)), pt(576 + 25 * math.cos(a)), pt(28 + 25 * math.sin(a)))
                   for a in [i * math.pi / 4 for i in range(8)])
    return ('''<figure class="mg mg--fin reveal" aria-hidden="true" style="--ar:600/170">
<svg class="mg-svg" viewBox="0 0 600 170" focusable="false">
<defs>
<linearGradient id="fi-g" gradientUnits="userSpaceOnUse" x1="20" y1="0" x2="576" y2="0"><stop offset="0" stop-color="%(G)s"/><stop offset="0.3" stop-color="%(G)s"/><stop offset="0.55" stop-color="%(L)s"/><stop offset="1" stop-color="%(L)s"/></linearGradient>
<linearGradient id="fi-a" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%(L)s" stop-opacity="0.2"/><stop offset="1" stop-color="%(L)s" stop-opacity="0"/></linearGradient>
<radialGradient id="fi-glow"><stop offset="0" stop-color="%(L)s" stop-opacity="0.55"/><stop offset="1" stop-color="%(L)s" stop-opacity="0"/></radialGradient>
</defs>
<path d="M20 150H580" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" stroke-linecap="round"/>
<path d="M20 90H580M20 40H580" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>
<path d="%(P)s" fill="none" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="3 7" stroke-linecap="round"/>
<g class="fi-stage">
<path class="fi-area" d="%(P)s L600 28 V150 H20 Z" fill="url(#fi-a)"/>
<path class="fi-draw" pathLength="1" d="%(P)s" fill="none" stroke="url(#fi-g)" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
<circle class="fi-m fi-m1 t" cx="150" cy="142" r="5.5" fill="%(C)s" stroke="%(G)s" stroke-width="2.5"/>
<circle class="fi-m fi-m2 t" cx="322" cy="100" r="5.5" fill="%(C)s" stroke="%(L)s" stroke-width="2.5"/>
<g class="fi-end t"><circle cx="576" cy="28" r="30" fill="url(#fi-glow)"/><circle class="fi-ring t" cx="576" cy="28" r="10" fill="none" stroke="%(L)s" stroke-width="2"/><g class="fi-rays" fill="none" stroke="%(L)s" stroke-width="2.4" stroke-linecap="round">%(R)s</g><circle cx="576" cy="28" r="8" fill="%(L)s"/></g>
<circle class="fi-dot" cx="0" cy="0" r="5" fill="#fff"/>
</g>
</svg>
</figure>''' % dict(L=L, G=G, C=C, P=FI, R=rays))

def patch(t):
    def rep(old, new, count=1):
        nonlocal t
        assert t.count(old) >= 1, old[:60]
        t = t.replace(old, new, count)
    # symbols once after <main ...>
    rep('<main id="main" class="home-v2" style="padding-top: 80px;">\n', '<main id="main" class="home-v2" style="padding-top: 80px;">\n' + SYMBOLS + '\n')
    # symptoms graphic
    rep('<h2 id="symptoms-title" class="medium-heading reveal">Does any of this sound like you?</h2>\n', '<h2 id="symptoms-title" class="medium-heading reveal">Does any of this sound like you?</h2>\n' + sym() + '\n')
    # explain
    rep('<div class="metabolism-cards">', cmp_() + '\n<div class="metabolism-cards">')
    # who
    rep('<h2 id="who-title" class="medium-heading reveal">Who we work with</h2>\n', '<h2 id="who-title" class="medium-heading reveal">Who we work with</h2>\n' + who() + '\n')
    # causes: section data-live (card icon sync), diagram, card icons
    rep('<section class="section" aria-labelledby="causes-title">', '<section class="section causes-section" aria-labelledby="causes-title" data-live>')
    rep('<h3 class="group-label reveal">Four we build a plan around</h3>', causes() + '\n<h3 class="group-label reveal">Four we build a plan around</h3>')
    names = ['Metabolic strain', 'Stress, illness and under-recovery', 'Medications and substances', 'Other hormones getting in the way',
             'Testicular problems', 'Pituitary or hypothalamic problems', 'Structural or genetic conditions']
    # (card icons added with regex below to preserve existing style attr)
    for i, nme in enumerate(names):
        pat = re.compile(r'(<li class="therapy-card[^"]*reveal" )style="--i:(\d)"><h4>' + re.escape(nme) + '</h4>')
        t, n = pat.subn(lambda m: m.group(1) + 'style="--i:%s;--k:%d">%s<h4>%s</h4>' % (m.group(2), i, ci(i + 1), nme), t)
        assert n == 1, nme
    # how it works: icons next to Step label
    for n in range(1, 5):
        rep('<span class="step-num">Step %d</span>' % n, '<span class="step-head"><span class="step-num">Step %d</span>%s</span>' % (n, step_icon(n)))
    rep('<div class="timeline" data-timeline>', '<div class="timeline" data-timeline data-live>')
    # about: after the first paragraph
    rep('We think it shouldn&rsquo;t be a solo job.</p>\n', 'We think it shouldn&rsquo;t be a solo job.</p>\n' + about() + '\n')
    # faq heading row
    rep('<h2 id="faq-title" class="medium-heading reveal">Frequently asked questions</h2>', '<div class="faq-head reveal" data-live>' + faq() + '<h2 id="faq-title" class="medium-heading">Frequently asked questions</h2></div>')
    # final
    rep('<p class="cta-note reveal">Prefer to talk first?', '<p class="cta-note reveal">Prefer to talk first?')
    rep('</p>\n</div>\n</section>\n\n<p class="disclaimer">', '</p>\n' + final() + '\n</div>\n</section>\n\n<p class="disclaimer">')
    return t

if __name__ == '__main__':
    base = open('/workspace/homepage/home.template.v2.html', encoding='utf-8').read()
    css = open('/workspace/homepage/_gen/motion2.css', encoding='utf-8').read()
    t = patch(base)
    marker = '</style>\n\n<script type="application/ld+json">'
    assert marker in t
    t = t.replace(marker, css + '\n' + marker, 1)
    open('/workspace/homepage/home.template.html', 'w', encoding='utf-8').write(t)
    print('template', len(t))
