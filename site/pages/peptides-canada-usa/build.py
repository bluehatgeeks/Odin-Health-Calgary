"""Build /workspace/pages/peptides-canada-usa/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *

SLUG = "peptides-canada-usa"
TITLE = "Peptides for Men in Canada and the USA | Odin Health Lab"
DESC = "Peptide status for men in Canada and the USA: Health Canada advisory, FDA compounding rules, quality risks, and how Odin helps with labs and plans."
OG_ALT = "Odin Health Lab: are peptides legal and available for men in Canada and the USA? Regulatory status and what to ask"
assert len(TITLE) <= 60 and len(DESC) <= 160, (len(TITLE), len(DESC))

FAQ = [
 ("Are peptides legal for men in Canada?",
  "In Canada, peptides are generally regulated as prescription drugs. Authorized peptide medicines should only be used under the care of a licensed healthcare professional and bought from a licensed pharmacy. On April 9, 2026, Health Canada issued a public advisory warning that unauthorized injectable peptide products sold online for anti-aging, bodybuilding or wellness are illegal, have not been assessed for safety, efficacy or quality, and can seriously harm you. Products labelled &ldquo;For Research Use Only &ndash; Not for Human Consumption&rdquo; are not legal or exempt. Authorized prescription drugs in Canada carry an eight-digit Drug Identification Number (DIN) on the label."),
 ("Are peptides legal or available for men in the USA?",
  "In the USA, some peptides are FDA-approved drugs (for example insulin or semaglutide) and are dispensed by licensed pharmacies with a prescription. Many wellness and recovery peptides that men hear about online are not approved drugs. Compounding under sections 503A and 503B of the FD&amp;C Act is tightly constrained: bulk substances must generally be components of FDA-approved drugs, have an applicable USP or NF monograph, appear on FDA&rsquo;s bulks list, or fall within FDA&rsquo;s interim Category 1 policy. FDA has also identified certain peptide bulk substances as presenting significant safety risks for compounding. Status can change as FDA evaluates nominations, so we treat each question carefully and never claim a gray-market product is cleared."),
 ("What did Health Canada warn about in April 2026?",
  "Health Canada&rsquo;s April 9, 2026 public advisory (identification number RA-81874) warned consumers not to buy or use unauthorized injectable peptide drugs marketed online for anti-aging, weight loss, bodybuilding, recovery, sleep, focus or wellness. Examples of unauthorized products Health Canada reported seizing include BPC-157, CJC-1295, Ipamorelin, Melanotan I and II, TB-500, MOTS-C, Epitalon and others. Risks named in the advisory include hormonal imbalance, blood sugar imbalance, liver or kidney damage, blood clots, infections, contaminants and unknown or unlisted ingredients. Health Canada is working with the Canada Border Services Agency to stop unauthorized shipments."),
 ("What about FDA compounding rules for peptides?",
  "FDA&rsquo;s January 2025 interim guidances describe when state-licensed pharmacies (503A) and outsourcing facilities (503B) may compound using bulk drug substances while FDA develops its bulks lists. Substances that present significant safety risks appear in Category 2 and are outside the compounding policy. FDA&rsquo;s public list includes several growth-hormone&ndash;related peptides among those concerns. In July 2026, FDA&rsquo;s Pharmacy Compounding Advisory Committee discussed several peptide bulk substances nominated for the 503A bulks list. A committee recommendation is advisory only; it does not by itself place a substance on the list or change the rules. FDA decides through formal rulemaking, and compounding status can drift as evaluations continue."),
 ("Does Odin Health Lab prescribe or sell peptides?",
  "No. Odin Health Lab does not prescribe peptides or any drug, and we do not sell injectable research chemicals. We help men in Canada and the USA who have low testosterone (andropause) symptoms clarify what they are asking about, review their labs, and build a sleep, stress, training and nutrition plan online. If a man is considering an authorized prescription medicine with his own doctor or pharmacist, we can help him prepare questions and track labs around that decision."),
 ("How does Odin Health Lab work with my doctor?",
  'Odin Health Lab is a telehealth service for men in Canada and the USA with low testosterone (andropause) symptoms. We work alongside your own doctor: we review your labs with you, build your sleep, stress, training and nutrition plan, and track your progress. We can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]
G = Gen()

# ---------- 1 · HERO: CA and US nodes flank a central question; pulses ride into the hub ----------
def hero_conv():
    s = ['<defs><radialGradient id="pep-g" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.16"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="150" rx="220" ry="130" fill="url(#pep-g)"/>']
    left, right, mid = (90, 150), (390, 150), (240, 150)
    for i, (a, b) in enumerate([(left, mid), (right, mid)]):
        d, pts = path(('M', a[0], a[1]), ('L', b[0], b[1]))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.14)" stroke-width="2.4" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>' % d)
        s.append(dr(d, 0.4 + i * 0.15, 1.1, LIME if i else 'rgba(255,255,255,0.7)', 2.6))
        s.append(dot('ph-p%d fx' % i, 5, LIME if i else WHITE))
        G.travel('ph-p%d' % i, pts, 8, 55, 7, delay='%ss' % f(-i * 2.1), rest=pts[0], rest_opacity=0, fade=3)
    s.append('<circle class="ph-ring fx" cx="240" cy="150" r="44" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(node(240, 150, 34, 'question', 0.15, LIME, fill='#142e14', isz=36))
    s.append(node(90, 150, 28, 'shield', 0.3, WHITE, isz=30))
    s.append(node(390, 150, 28, 'doc', 0.45, LIME, fill='#142e14', isz=30))
    s.append('<text x="90" y="210" font-size="14" fill="#fff" fill-opacity="0.85" text-anchor="middle">Canada</text>')
    s.append('<text x="390" y="210" font-size="14" fill="#c4ff49" fill-opacity="0.95" text-anchor="middle">USA</text>')
    s.append('<text x="240" y="86" font-size="14" fill="#fff" fill-opacity="0.8" text-anchor="middle">What is allowed?</text>')
    # small bottom icons: labs / chat / coach
    for i, (x, ic, col) in enumerate([(140, 'labs', WHITE), (240, 'chat', LIME), (340, 'coach', WHITE)]):
        s.append(node(x, 268, 18, ic, 0.55 + i * 0.1, col, fill='#142e14' if col == LIME else DARK, isz=20))
    return '\n'.join(s)

# ---------- 2 · TYPES: three columns — approved drug, compounding path, research gray ----------
def types():
    cols = [(95, 'bottle', 'Approved drug', LIME), (280, 'caps', 'Compounded', WHITE), (465, 'tube', 'Research label', WHITE)]
    s = []
    for i, (x, ic, lab, col) in enumerate(cols):
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="40" width="130" height="160" rx="14" fill="rgba(255,255,255,0.05)" stroke="%s" stroke-width="2"/></g>' % (0.1 + i * 0.12, x - 65, LIME if i == 0 else 'rgba(255,255,255,0.28)'))
        s.append(node(x, 90, 26, ic, 0.25 + i * 0.12, col, fill='#142e14' if col == LIME else DARK, isz=28))
        s.append('<text x="%d" y="150" font-size="14" fill="#fff" text-anchor="middle">%s</text>' % (x, lab))
    # connectors with a travelling pulse from left to right
    for i, (x1, x2) in enumerate([(160, 215), (345, 400)]):
        d, pts = path(('M', x1, 90), ('L', x2, 90))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.18)" stroke-width="2" stroke-dasharray="3 7" fill="none"/>' % d)
        s.append(dr(d, 0.5 + i * 0.2, 0.8, 'rgba(196,255,73,0.55)', 2.2))
        s.append(dot('ty-p%d fx' % i, 4.5, LIME))
        G.travel('ty-p%d' % i, pts, 10, 50, 6, delay='%ss' % f(-i * 1.8), rest=pts[0], rest_opacity=0, fade=2.5)
    s.append('<g class="ty-x"><path d="M450 178l30 30M480 178l-30 30" stroke="#c4ff49" stroke-width="3" stroke-linecap="round"/></g>')
    s.append('<text x="280" y="230" font-size="13" fill="#fff" fill-opacity="0.7" text-anchor="middle">Same word, three very different buckets</text>')
    return '\n'.join(s)

# ---------- 3 · CANADA: DIN check vs unauthorized vial, shield pulses ----------
def canada():
    s = ['<defs><linearGradient id="ca-g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.12"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></linearGradient></defs>']
    s.append('<rect x="40" y="30" width="220" height="180" rx="16" fill="url(#ca-g)" stroke="rgba(196,255,73,0.45)" stroke-width="2"/>')
    s.append('<rect x="300" y="30" width="220" height="180" rx="16" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.22)" stroke-width="2"/>')
    s.append(node(150, 90, 28, 'shield', 0.2, LIME, fill='#142e14', isz=30))
    s.append(node(410, 90, 28, 'bottle', 0.35, WHITE, isz=30))
    s.append('<text x="150" y="150" font-size="15" fill="#c4ff49" text-anchor="middle">Authorized + DIN</text>')
    s.append('<text x="410" y="150" font-size="15" fill="#fff" fill-opacity="0.85" text-anchor="middle">Unauthorized online</text>')
    s.append('<g class="ca-ck"><path d="M128 188l10 10 22-24" stroke="#c4ff49" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>')
    s.append('<g class="ca-x"><path d="M392 178l36 36M428 178l-36 36" stroke="#fff" stroke-opacity="0.7" stroke-width="3" stroke-linecap="round"/></g>')
    # pulse from left panel toward advisory badge
    d, pts = path(('M', 260, 120), ('C', 300, 80, 360, 60, 410, 50))
    s.append(dr(d, 0.6, 1.0, 'rgba(196,255,73,0.5)', 2))
    s.append(dot('ca-p fx', 5, LIME)); G.travel('ca-p', pts, 12, 55, 7, rest=pts[0], rest_opacity=0, fade=2.5)
    s.append('<text x="410" y="44" font-size="12" fill="#c4ff49" text-anchor="middle">Apr 2026 advisory</text>')
    return '\n'.join(s)

# ---------- 4 · USA: 503A and 503B gates into a bulks-list funnel ----------
def usa():
    s = []
    # two entry gates
    for i, (x, lab, ic) in enumerate([(110, '503A pharmacy', 'home'), (110, '503B facility', 'doc')]):
        y = 60 + i * 100
        s.append('<g class="pop t" style="--d:%s"><rect x="40" y="%d" width="140" height="56" rx="12" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.3)" stroke-width="1.8"/></g>' % (0.1 + i * 0.12, y))
        s.append(node(70, y + 28, 18, ic, 0.2 + i * 0.1, WHITE if i else LIME, fill='#142e14' if not i else DARK, isz=20))
        s.append('<text x="130" y="%d" font-size="13" fill="#fff" text-anchor="middle">%s</text>' % (y + 32, lab.split()[0]))
        s.append('<text x="130" y="%d" font-size="12" fill="#fff" fill-opacity="0.65" text-anchor="middle">%s</text>' % (y + 46, ' '.join(lab.split()[1:])))
        d, pts = path(('M', 180, y + 28), ('C', 240, y + 28, 280, 118, 320, 118))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-dasharray="2 7" fill="none"/>' % d)
        s.append(dr(d, 0.4 + i * 0.15, 1.2, LIME if not i else 'rgba(255,255,255,0.65)', 2.4))
        s.append(dot('us-p%d fx' % i, 5, LIME if not i else WHITE))
        G.travel('us-p%d' % i, pts, 8, 50, 8, delay='%ss' % f(-i * 2.2), rest=pts[0], rest_opacity=0, fade=2.5)
    # funnel / gate
    s.append('<g class="pop t" style="--d:0.5"><path d="M320 70 L480 95 L480 141 L320 166 Z" fill="rgba(196,255,73,0.08)" stroke="#c4ff49" stroke-width="2.2"/></g>')
    s.append(node(400, 118, 26, 'list', 0.6, LIME, fill='#142e14', isz=28))
    s.append('<text x="400" y="178" font-size="13" fill="#fff" fill-opacity="0.8" text-anchor="middle">Bulks list / Category rules</text>')
    s.append('<g class="us-gate"><path d="M470 108v20M470 118h18" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/></g>')
    return '\n'.join(s)

# ---------- 5 · RISKS: unlabeled vial with drifting contaminant dots ----------
def risks():
    s = ['<g class="pop t" style="--d:0.1"><rect x="180" y="40" width="90" height="140" rx="10" fill="#142e14" stroke="rgba(255,255,255,0.45)" stroke-width="2.4"/><rect x="198" y="28" width="54" height="22" rx="4" fill="#173617" stroke="#c4ff49" stroke-width="1.8"/></g>']
    s.append('<path d="M205 70h40M205 90h40M205 110h28" stroke="rgba(255,255,255,0.35)" stroke-width="2.4" stroke-linecap="round"/>')
    s.append('<text x="225" y="155" font-size="12" fill="#fff" fill-opacity="0.6" text-anchor="middle">???</text>')
    # contaminant dots orbit / drift
    for i, (ox, oy) in enumerate([(120, 80), (340, 70), (100, 140), (360, 150), (140, 170), (320, 110)]):
        s.append('<circle class="rk-d" style="--k:%d" cx="%d" cy="%d" r="%s" fill="%s" fill-opacity="0.75"/>' % (i, ox, oy, 4 + (i % 3), LIME if i % 2 else '#fff'))
    s.append(node(60, 100, 22, 'shield', 0.4, WHITE, isz=24))
    s.append(node(500, 100, 22, 'pulse', 0.55, LIME, fill='#142e14', isz=24))
    s.append('<text x="60" y="150" font-size="13" fill="#fff" fill-opacity="0.8" text-anchor="middle">Quality</text>')
    s.append('<text x="500" y="150" font-size="13" fill="#c4ff49" text-anchor="middle">Unknown dose</text>')
    s.append('<text x="280" y="220" font-size="13" fill="#fff" fill-opacity="0.7" text-anchor="middle">Unlabeled, research-only and gray-market injectables</text>')
    return '\n'.join(s)

# ---------- 6 · HELP: labs + plan + doctor link converging on you ----------
def help_fig():
    nodes_pos = [(90, 70, 'labs', 'Labs'), (90, 170, 'coach', 'Plan'), (470, 120, 'doc', 'Your doctor')]
    s = []
    for i, (x, y, ic, lab) in enumerate(nodes_pos):
        d, pts = path(('M', x, y), ('L', 280, 120))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.14)" stroke-width="2.4" stroke-dasharray="2 8" fill="none"/>' % d)
        s.append(dr(d, 0.35 + i * 0.12, 1.1, LIME if i == 1 else 'rgba(255,255,255,0.7)', 2.6))
        s.append(dot('hp-p%d fx' % i, 5, LIME if i == 1 else WHITE))
        G.travel('hp-p%d' % i, pts, 8, 52, 7.5, delay='%ss' % f(-i * 2), rest=pts[0], rest_opacity=0, fade=2.5)
        s.append(node(x, y, 24, ic, 0.2 + i * 0.1, LIME if i == 1 else WHITE, fill='#142e14' if i == 1 else DARK, isz=26))
        s.append('<text x="%d" y="%d" font-size="13" fill="#fff" fill-opacity="0.85" text-anchor="middle">%s</text>' % (x, y + 48, lab))
    s.append('<circle class="hp-ring fx" cx="280" cy="120" r="38" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append(node(280, 120, 30, 'you', 0.15, LIME, fill='#142e14', isz=32))
    s.append('<text x="280" y="190" font-size="13" fill="#fff" fill-opacity="0.75" text-anchor="middle">You</text>')
    return '\n'.join(s)

# ---------- final: four rising steps ----------
def final():
    s = ['<path d="M24 170H336" stroke="rgba(255,255,255,0.55)" stroke-width="3.4" stroke-linecap="round"/>']
    for k in range(4):
        x = 40 + k * 70; h = (k + 1) * 28
        s.append('<g class="pop t" style="--d:%s"><rect x="%d" y="%d" width="64" height="%d" rx="8" fill="%s" stroke="%s" stroke-width="2.4"/></g>' % (0.1 + k * 0.12, x, 170 - h, h, '#142e14' if k % 2 == 0 else '#173617', LIME if k == 3 else 'rgba(255,255,255,0.5)'))
    tops = [(72, 170 - 28 - 10), (142, 170 - 56 - 10), (212, 170 - 84 - 10), (282, 170 - 112 - 10)]
    sg = [('M', tops[0][0], tops[0][1])]
    for i in range(1, 4):
        px, py = tops[i - 1]; qx, qy = tops[i]
        sg.append(('C', px + 24, py - 30, qx - 24, qy - 30, qx, qy))
    d, p = path(*sg, n=10)
    s.append(dot('fn-p', 8, LIME, ring=True)); G.travel('fn-p', p, 8, 82, 8, rest=p[-1], fade=3)
    s.append('<path d="M282 58V20" stroke="#fff" stroke-width="3" stroke-linecap="round"/><g class="fn-fl"><path d="M282 20h26l-6 8 6 8h-26z" fill="#c4ff49" fill-opacity="0.9"/></g>')
    s.append(node(48, 110, 22, 'labs', 0.4, WHITE, isz=24))
    s.append(node(140, 62, 20, 'shield', 0.5, LIME, fill='#142e14', isz=22))
    return '\n'.join(s)

FAQMOTIF = '''<g class="fq-dr"><path d="M30 20c9 12 15 20 15 28a15 15 0 0 1-30 0c0-8 6-16 15-28z" fill="#c4ff49" fill-opacity="0.85"/></g>
<path class="dr" pathLength="1" style="--d:0.2;--dur:1.1s" d="M70 38c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82" cy="66" r="3" fill="#fff"/>
<path class="fq-st" style="--k:0" d="M104 20v10M99 25h10" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/>'''

def step_icons():
    return {
     "{{STEP1}}": '<path d="M9 3h6"/><path d="M10 3v6l-5 9a2 2 0 0 0 1.8 3h10.4a2 2 0 0 0 1.8-3l-5-9V3"/><g class="hi-bl" style="--k:0"><circle cx="38" cy="14" r="2.6" fill="#fff" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="10" cy="36" r="2.6" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><g class="hi-ck" style="--k:0"><path d="M8.5 14l3 3 6-7" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<path d="M14 24h20"/><g class="hi-pu" style="--k:0"><path d="M10 14v20M5 19v10" stroke="#c4ff49"/></g><g class="hi-pu" style="--k:1"><path d="M38 14v20M43 19v10" stroke="#c4ff49"/></g>',
     "{{STEP4}}": '<path d="M5 28h9l4-10 8 20 4-10h13"/><g class="hi-ck" style="--k:0"><path d="M30 12l5 5 9-11" stroke="#fff"/></g>',
    }

HUB = hub(G, [(110, 52, 'tube'), (110, 148, 'scale'), (450, 52, 'drop'), (450, 148, 'coach'), (230, 28, 'caps'), (330, 172, 'labs'), (330, 28, 'flame'), (230, 172, 'pulse')])
slots = {"{{HERO}}": hero_conv(), "{{TYPES}}": types(), "{{CANADA}}": canada(), "{{USA}}": usa(), "{{RISKS}}": risks(),
         "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(), "{{HUB}}": HUB, "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Peptide therapies for men in Canada and the USA: regulatory status",
      "Peptides Canada and USA", "Are peptides legal or available for men in Canada and the USA?", slots, G)
