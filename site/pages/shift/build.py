"""Build /workspace/pages/shift/page.html (self-contained, paste into the GHL custom-code block).
Edit page.body.html (markup), page.css (graphics CSS), the lists below, or ../_shared/*; then run: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ) so they always match.
Generated CSS (per-element delays computed from coordinates) is injected into page.css at /*@GEN_STATIC*/ and /*@GEN_MOTION*/."""
import sys, os, math, re, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
import common
import gfx  # adds sun / tube / scale / calendar ... icons to common.ICONS
from common import *
from gfx import f, dr, LIME, WHITE, DARK

SLUG = "shift"
# Verbatim from /workspace/homepage/seo-meta.md (title 62 chars: see NOTES.md, SEO flag 1)
TITLE = "Shift Work, Low Energy and Low Testosterone | Odin Health Lab"
DESC = "Night and rotating shifts disrupt sleep, stress and hormones and can pull testosterone down. How men on shift work rebuild energy and recovery, online."
OG_ALT = "Odin Health Lab: online support for men on night and rotating shifts with low energy and low-T symptoms, Canada and USA"
assert len(DESC) <= 160

BC_URL = "https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/bc-guidelines/testosterone-testing"
CMAJ_URL = "https://pmc.ncbi.nlm.nih.gov/articles/PMC4674408/"

common.ICONS.update({
 "cup": '<path d="M5 9h11v5a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5z"/><path d="M16 11h1.5a2.5 2.5 0 0 1 0 5H16"/><path d="M8.5 3.5c-.8 1 .8 2-.1 3M12 3.5c-.8 1 .8 2-.1 3"/>',
 "work": '<path d="M4 8h16a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><path d="M9 8V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5V8"/><path d="M3 13h18"/>',
})

FAQ = [
  ("Can shift work lower testosterone?",
   "It can. Shift work doesn\u2019t lower testosterone in every man, but it often cuts sleep short and moves it around, and short or broken sleep can pull testosterone down. Long blocks, stress, late meals, extra caffeine or alcohol and missed training add to it. Many of the same symptoms also come from plain sleep debt, so we look at the whole picture first."),
  ("What can you do for me if I work nights or rotating shifts?",
   "We build a plan around the rotation you actually work: an anchor sleep window, light and caffeine timing, meals on shift, training that fits your days off, and a routine for switching between nights and days. We review it with you at regular check-ins and change it when your schedule changes."),
  ("When should a shift worker get testosterone tested?",
   'Canadian guidelines recommend a sample in the morning, or within about three hours of waking for men who work shifts, at a time when your sleep pattern is stable, not right after a switch between nights and days. Repeat tests are best done at the same lab. See <a href="%s/low-testosterone-labs-to-ask-for">which labs to ask for</a>.' % SITE),
  ("How do you work with my medical doctor?",
   "Your doctor stays your doctor. With your permission we share your plan and symptom notes, help you prepare questions for your appointment and walk you through your results. Decisions about testing, prescriptions and testosterone therapy stay with your doctor, and we fit your plan around them."),
  ("Will this fit around my schedule?",
   "Yes. Calls and messages are booked around your rotation, including before or after nights, and your plan is written for the schedule you work. When your rotation changes, your plan changes with it."),
  ("Is it fully online, and where do you work with men?",
   'Yes. Odin Health Lab is telehealth only and serves men across Canada and the USA. Everything happens by secure video, phone and message, so there are no clinic visits. See our <a href="%s/">low testosterone and andropause overview</a> for how the service works, or read our <a href="%s/privacy">Privacy Policy</a> for how we protect your information.' % (SITE, SITE)),
]

ST, MO = [], []   # generated static (final-state) and motion CSS

def pt(cx, cy, r, a):
    """point on a circle, angle a in degrees clockwise from 12 o'clock"""
    return cx + r * math.sin(math.radians(a)), cy - r * math.cos(math.radians(a))

def arc(cx, cy, r, a0, a1):
    x0, y0 = pt(cx, cy, r, a0); x1, y1 = pt(cx, cy, r, a1)
    return "M%s %sA%s %s 0 %d 1 %s %s" % (f(x0), f(y0), r, r, 1 if (a1 - a0) % 360 > 180 else 0, f(x1), f(y1))

# ---------- 1 · HERO: a 24-hour dial. Sun and moon circle the rim; a sleep block jumps with each rotation, then settles and locks; the battery refills ----------
HERO_SETTLE = 200   # final (static) angle of the sleep block
def hero_dial():
    cx, cy = 240, 160
    s = ['<defs><radialGradient id="sh-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.22"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs>',
         '<circle cx="240" cy="160" r="150" fill="url(#sh-g)"/>',
         '<path d="%s" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="10" stroke-linecap="round"/>' % arc(cx, cy, 136, 272, 448),
         '<path d="%s" fill="none" stroke="rgba(196,255,73,0.14)" stroke-width="10" stroke-linecap="round"/>' % arc(cx, cy, 136, 92, 268)]
    ticks = ""
    for h in range(24):
        a = h * 15; r0 = 112 if h % 6 else 106
        x0, y0 = pt(cx, cy, r0, a); x1, y1 = pt(cx, cy, 118, a)
        ticks += "M%s %sL%s %s" % (f(x0), f(y0), f(x1), f(y1))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.35)" stroke-width="2" stroke-linecap="round"/>' % ticks)
    s.append(dr("M240 42A118 118 0 1 1 239.9 42", 0.1, 1.6, LIME, 2.6))
    # sleep block (rotates as a group around the centre)
    s.append('<g class="sh-wedge">'
             '<path class="sh-lock fx" d="%s" fill="none" stroke="#fff" stroke-width="30" stroke-linecap="round" stroke-opacity="0.35"/>'
             '<path d="%s" fill="none" stroke="#c4ff49" stroke-width="18" stroke-linecap="round"/>'
             '%s</g>' % (arc(cx, cy, 92, -50, 50), arc(cx, cy, 92, -50, 50), ico("sleep", *pt(cx, cy, 92, 0), 16, DARK, 2.4)))
    # battery in the middle
    s.append('<g class="pop t" style="--d:0.3"><rect x="204" y="138" width="66" height="44" rx="9" fill="#0f240f" stroke="#fff" stroke-width="3"/><rect x="272" y="151" width="7" height="18" rx="2.5" fill="#fff"/></g>')
    for k in range(4):
        s.append('<rect class="sh-bar" style="--k:%d" x="%d" y="145" width="11" height="30" rx="3" fill="#c4ff49"/>' % (k, 211 + k * 14))
    # sun and moon orbit (stay upright)
    s.append('<g class="sh-orbit">')
    for nm, a, col in (("sun", 0, "#fff"), ("sleep", 180, LIME)):
        x, y = pt(cx, cy, 136, a)
        s.append('<g class="sh-sat" style="transform-origin:%spx %spx"><circle cx="%s" cy="%s" r="19" fill="#0f240f" stroke="%s" stroke-width="2.4"/>%s</g>' % (f(x), f(y), f(x), f(y), col, ico(nm, x, y, 22, col, 1.9)))
    s.append('</g>')
    ST.append('.pg .sh-wedge { transform: rotate(%ddeg); }' % HERO_SETTLE)
    return "\n".join(s)

# ---------- 2 · WHY: body-clock wave and shift-pattern wave drift in and out of step ----------
def waves():
    s = ['<defs><clipPath id="wy-c"><rect x="24" y="16" width="512" height="188" rx="14"/></clipPath></defs>',
         '<path d="M24 110H536" stroke="rgba(255,255,255,0.12)" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/>']
    P, A = 160, 44
    pts = ["%s %s" % (f(x), f(110 - A * math.sin(2 * math.pi * x / P))) for x in range(-P, 720 + 1, 8)]
    sine = "M" + "L".join(pts)
    sq, x, hi = "M%d 70" % -200, -200, True
    while x < 760:
        x2 = x + (120 if hi else 80)
        sq += "H%d V%d" % (x2, 150 if hi else 70); hi = not hi; x = x2
    s.append('<g clip-path="url(#wy-c)">')
    s.append('<path class="wy-b" d="%s" fill="none" stroke="#9db39d" stroke-width="3.2" stroke-dasharray="7 7" stroke-linejoin="round"/>' % sq)
    s.append('<path class="wy-a" d="%s" fill="none" stroke="#c4ff49" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>' % sine)
    s.append('</g>')
    s.append('<path d="M280 24V196" stroke="#fff" stroke-opacity="0.5" stroke-width="2" stroke-linecap="round"/>')
    s.append('<circle class="wy-ring fx" cx="280" cy="110" r="14" fill="none" stroke="#fff" stroke-width="2.4"/>')
    s.append('<g class="pop t" style="--d:0.2"><circle cx="280" cy="110" r="7" fill="#fff"/></g>')
    s.append('<g class="pop t" style="--d:0.1"><circle cx="54" cy="44" r="16" fill="#0f240f" stroke="#fff" stroke-width="2"/>%s</g>' % ico("sun", 54, 44, 20, "#fff", 1.8))
    s.append('<g class="pop t" style="--d:0.2"><circle cx="54" cy="176" r="16" fill="#0f240f" stroke="#c4ff49" stroke-width="2"/>%s</g>' % ico("sleep", 54, 176, 18, LIME, 1.9))
    return "\n".join(s)

# ---------- 3 · WHAT SHOWS UP: four dashboard lights flick on in turn while a scan sweeps across ----------
def dash():
    s = []
    for k, (nm, x) in enumerate((("batt", 88), ("sleep", 216), ("flame", 344), ("body", 472))):
        s.append('<g class="pop t" style="--d:%.2f"><rect x="%d" y="52" width="104" height="104" rx="22" fill="#0f240f" stroke="rgba(196,255,73,0.3)" stroke-width="2.4"/>'
                 '<rect class="sd-lit fx" style="--k:%d" x="%d" y="52" width="104" height="104" rx="22" fill="rgba(196,255,73,0.16)" stroke="#c4ff49" stroke-width="3"/>'
                 '<g class="sd-ico t" style="--k:%d">%s</g>'
                 '<circle class="sd-led" style="--k:%d" cx="%d" cy="34" r="6" fill="#c4ff49"/></g>'
                 % (0.1 + k * 0.12, x - 52, k, x - 52, k, ico(nm, x, 104, 46, "#fff" if k % 2 else LIME, 1.6), k, x))
    s.append('<g class="sd-sweep fx"><rect x="0" y="44" width="5" height="120" rx="2.5" fill="#fff" fill-opacity="0.65"/></g>')
    s.append('<path d="M36 184H524" stroke="rgba(255,255,255,0.14)" stroke-width="2" stroke-linecap="round"/>')
    return "\n".join(s)

# ---------- 4 · WHAT WE WORK ON: a 24-hour planner; blocks slide into place, a cursor moves through the day, each habit chip pings as it passes ----------
PL_X0, PL_X1, PL_DUR = 40, 520, 10.0
def planner():
    s = ['<rect x="40" y="104" width="480" height="44" rx="12" fill="#0f240f" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>']
    for k in range(1, 6):
        x = 40 + k * 80
        s.append('<path d="M%d 110V142" stroke="rgba(255,255,255,0.1)" stroke-width="2"/>' % x)
    s.append('<g class="pl-in" style="--d:0.2;--fx:-24px"><rect x="62" y="108" width="168" height="36" rx="10" fill="#c4ff49"/>%s<path d="M126 126H210" stroke="#0f240f" stroke-opacity="0.35" stroke-width="4" stroke-linecap="round"/></g>' % ico("sleep", 92, 126, 20, DARK, 2.2))
    s.append('<g class="pl-in" style="--d:0.45;--fx:24px"><rect x="296" y="108" width="208" height="36" rx="10" fill="rgba(255,255,255,0.12)" stroke="#fff" stroke-width="2.4"/>%s<path d="M352 126H486" stroke="#fff" stroke-opacity="0.35" stroke-width="4" stroke-linecap="round"/></g>' % ico("work", 324, 126, 20, "#fff", 1.9))
    chips = [("sun", 300, 56, LIME), ("cup", 344, 56, "#fff"), ("food", 420, 56, LIME), ("train", 256, 196, "#fff")]
    for k, (nm, x, y, col) in enumerate(chips):
        stem = 'M%d %dV%d' % (x, y + 18, 104) if y < 100 else 'M%d %dV%d' % (x, 148, y - 18)
        s.append('<path d="%s" stroke="rgba(255,255,255,0.28)" stroke-width="2" stroke-dasharray="2 5" stroke-linecap="round"/>' % stem)
        s.append('<g class="pop t" style="--d:%.2f"><circle class="pl-ring pl-r%d fx" cx="%d" cy="%d" r="18" fill="none" stroke="%s" stroke-width="2"/>'
                 '<g class="pl-chip pl-c%d t"><circle cx="%d" cy="%d" r="18" fill="#142e14" stroke="%s" stroke-width="2.4"/>%s</g></g>'
                 % (0.6 + k * 0.1, k, x, y, col, k, x, y, col, ico(nm, x, y, 20, col, 1.8)))
        t = (x - PL_X0) / (PL_X1 - PL_X0) * 80   # cursor runs 0-80% of the cycle
        MO.append('  @keyframes pl-c%d { 0%%, %s%% { transform: scale(1); } %s%% { transform: scale(1.18); } %s%%, 100%% { transform: scale(1); } }\n'
                  '  .js-reveal .pg .pl-c%d { animation: pl-c%d %ss var(--ease-out) infinite; }\n'
                  '  @keyframes pl-r%d { 0%%, %s%% { opacity: 0; transform: scale(1); } %s%% { opacity: 0.7; transform: scale(1); } %s%%, 100%% { opacity: 0; transform: scale(1.9); } }\n'
                  '  .js-reveal .pg .pl-r%d { animation: pl-r%d %ss ease-out infinite; }'
                  % (k, f(max(t - 0.5, 0)), f(t + 2), f(t + 8), k, k, f(PL_DUR), k, f(max(t - 0.2, 0)), f(t), f(t + 12), k, k, f(PL_DUR)))
    s.append('<g class="pl-cur fx"><path d="M0 90V162" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/><circle cx="0" cy="90" r="5" fill="#fff"/></g>')
    return "\n".join(s)

# ---------- 5 · TESTING: a 24-hour clock with a short window after waking; the hand sweeps it and a sample tube fills while it is inside ----------
def testing():
    cx, cy = 130, 124
    s = ['<circle cx="130" cy="124" r="86" fill="#0f240f" stroke="rgba(255,255,255,0.3)" stroke-width="2.4"/>']
    ticks = ""
    for h in range(24):
        x0, y0 = pt(cx, cy, 72 if h % 6 else 66, h * 15); x1, y1 = pt(cx, cy, 78, h * 15)
        ticks += "M%s %sL%s %s" % (f(x0), f(y0), f(x1), f(y1))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.32)" stroke-width="2" stroke-linecap="round"/>' % ticks)
    s.append('<path d="%s" fill="none" stroke="rgba(196,255,73,0.25)" stroke-width="14" stroke-linecap="round"/>' % arc(cx, cy, 56, 0, 45))
    s.append(dr(arc(cx, cy, 56, 0, 45), 0.3, 0.9, LIME, 14))
    sx, sy = pt(cx, cy, 104, 0)
    s.append('<g class="pop t" style="--d:0.1"><circle cx="%s" cy="%s" r="15" fill="#142e14" stroke="#c4ff49" stroke-width="2.4"/>%s</g>' % (f(sx), f(sy), ico("sun", sx, sy, 18, LIME, 1.9)))
    s.append('<g class="tt-hand"><path d="M130 124V58" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/></g><circle cx="130" cy="124" r="7" fill="#fff"/>')
    s.append('<path d="M226 124H280" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-dasharray="2 6" stroke-linecap="round"/>')
    # sample tube
    s.append('<defs><clipPath id="tt-c"><path d="M314 40V182a20 20 0 0 0 40 0V40z"/></clipPath></defs>')
    s.append('<g clip-path="url(#tt-c)"><rect class="tt-liq" x="314" y="70" width="40" height="134" fill="#c4ff49" fill-opacity="0.8"/>'
             '<circle class="tt-bub" style="--k:0" cx="326" cy="182" r="3" fill="#0f240f" fill-opacity="0.5"/><circle class="tt-bub" style="--k:1" cx="342" cy="190" r="2.4" fill="#0f240f" fill-opacity="0.5"/></g>')
    s.append('<path d="M314 40V182a20 20 0 0 0 40 0V40" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/><rect x="306" y="28" width="56" height="14" rx="5" fill="#142e14" stroke="#fff" stroke-width="2.6"/>')
    s.append('<g class="tt-ok t"><circle cx="384" cy="70" r="15" fill="#c4ff49"/><path d="M377 70l4.5 4.5L391 65" fill="none" stroke="#0f240f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>')
    return "\n".join(s)

# ---------- 6 · RELATED: a transit line; a dot rides through six stations and each lights as it passes ----------
TM_DUR = 9.0
def transit():
    xs = [60 + i * 88 for i in range(6)]; Y = 64
    s = ['<path d="M40 %dH520" stroke="rgba(196,255,73,0.18)" stroke-width="8" stroke-linecap="round"/>' % Y, dr("M40 %dH520" % Y, 0.1, 1.4, LIME, 4),
         '<g class="tm-dot fx"><circle cx="0" cy="%d" r="8" fill="#fff"/><circle cx="0" cy="%d" r="13" fill="none" stroke="#fff" stroke-opacity="0.4" stroke-width="2"/></g>' % (Y, Y)]
    for k, (x, nm) in enumerate(zip(xs, ("home", "labs", "coach", "caps", "scale", "tube"))):
        s.append('<circle class="tm-ring tm-r%d fx" cx="%d" cy="%d" r="26" fill="none" stroke="#c4ff49" stroke-width="2"/>' % (k, x, Y))
        s.append('<g class="pop t" style="--d:%.2f"><circle cx="%d" cy="%d" r="25" fill="#0f240f" stroke="%s" stroke-width="2.6"/>%s</g>' % (0.3 + k * 0.1, x, Y, LIME if k % 2 == 0 else "rgba(255,255,255,0.75)", ico(nm, x, Y, 26, LIME if k % 2 == 0 else "#fff", 1.7)))
        t = (x - 40) / 480 * 80
        MO.append('  @keyframes tm-r%d { 0%%, %s%% { opacity: 0; transform: scale(1); } %s%% { opacity: 0.75; transform: scale(1); } %s%%, 100%% { opacity: 0; transform: scale(1.7); } }\n'
                  '  .js-reveal .pg .tm-r%d { animation: tm-r%d %ss ease-out infinite; }' % (k, f(max(t - 0.2, 0)), f(t), f(t + 14), k, k, f(TM_DUR)))
    return "\n".join(s)

# ---------- 7 · FAQ: crescent moon, a question mark bobs beside it, stars twinkle ----------
FAQMOTIF = '''<circle cx="60" cy="52" r="46" stroke="rgba(196,255,73,0.18)" stroke-width="1.5" stroke-dasharray="2 7" stroke-linecap="round"/>
<g class="fq-moon"><path d="M48 26a28 28 0 1 0 30 38 22 22 0 1 1-30-38z" fill="rgba(196,255,73,0.16)" stroke="#c4ff49" stroke-width="3" stroke-linejoin="round"/></g>
<g class="fq-q"><path class="dr" pathLength="1" style="--d:0.3;--dur:1.1s" d="M74 26c0-5 3.5-8 8-8s8 3 8 7c0 3.5-2.7 5-4.8 6.6-1.7 1.4-2.7 2.6-2.7 5.2" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82.6" cy="44" r="2.4" fill="#fff"/></g>
<circle class="fq-st" style="--k:0" cx="100" cy="62" r="3" fill="#c4ff49"/><circle class="fq-st" style="--k:1" cx="18" cy="40" r="2.4" fill="#fff"/><circle class="fq-st" style="--k:2" cx="96" cy="88" r="2" fill="#fff"/>'''

# ---------- 8 · FINAL: sunrise over a horizon; the moon sets as the sun climbs, rays turn slowly ----------
def sunrise():
    s = ['<defs><clipPath id="fs-c"><rect x="0" y="0" width="360" height="150"/></clipPath><radialGradient id="fs-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.35"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs>',
         '<g clip-path="url(#fs-c)">',
         '<g class="fs-moon"><path d="M76 40a22 22 0 1 0 24 30 17 17 0 1 1-24-30z" fill="rgba(255,255,255,0.12)" stroke="#fff" stroke-width="2.4" stroke-linejoin="round"/></g>',
         '<g class="fs-sun"><circle cx="180" cy="104" r="78" fill="url(#fs-g)"/><g class="fs-rays t">']
    rays = ""
    for k in range(12):
        x0, y0 = pt(180, 104, 44, k * 30); x1, y1 = pt(180, 104, 58, k * 30)
        rays += "M%s %sL%s %s" % (f(x0), f(y0), f(x1), f(y1))
    s.append('<path d="%s" stroke="#c4ff49" stroke-width="3.4" stroke-linecap="round"/></g>' % rays)
    s.append('<circle cx="180" cy="104" r="32" fill="#c4ff49"/></g></g>')
    s.append(dr("M24 150H336", 0.1, 1.2, "#fff", 3))
    for k, (x, w) in enumerate(((70, 50), (150, 80), (250, 60))):
        s.append('<path class="fs-ln" style="--k:%d" d="M%d %dH%d" stroke="rgba(255,255,255,0.3)" stroke-width="3" stroke-linecap="round"/>' % (k, x, 168 + (k % 2) * 12, x + w))
    return "\n".join(s)

# ---------- How-it-works step icons (48x48) ----------
STEPS = {
 "{{STEP1}}": '<rect x="10" y="7" width="28" height="35" rx="5"/><rect x="17" y="4" width="14" height="6" rx="2"/>'
              + "".join('<rect x="15" y="%d" width="6" height="6" rx="1.5" opacity="0.6"/><path d="M25 %dh8" opacity="0.45"/><path class="hs-tick t" style="--k:%d" d="M15.5 %dl2 2 3.5-4" stroke="#fff"/>' % (y, y + 3, k, y + 3) for k, y in enumerate((15, 24, 33))),
 "{{STEP2}}": '<rect x="6" y="9" width="36" height="31" rx="5"/><path d="M6 18h36M15 5v7M33 5v7" opacity="0.7"/>'
              '<g class="hs-sun t"><circle cx="24" cy="29" r="5" fill="#c4ff49" stroke="none"/></g>'
              '<g class="hs-moon t"><path d="M22 23.5a6 6 0 1 0 7.5 7.5 4.6 4.6 0 1 1-7.5-7.5z" fill="#142e14" stroke="#fff"/></g>',
 "{{STEP3}}": '<path d="M8 36c8 0 6-12 16-12s8-12 16-12" stroke-dasharray="3 4" opacity="0.6"/><path d="M38 6v12M38 6l6 3-6 3"/><circle class="hs-go" cx="8" cy="36" r="4" fill="#fff" stroke="none"/>',
 "{{STEP4}}": '<g class="hs-spin"><path d="M36 17a14 14 0 0 0-24 2"/><path d="M12 12v7h7"/><path d="M12 31a14 14 0 0 0 24-2"/><path d="M36 36v-7h-7"/></g><circle cx="24" cy="24" r="3" fill="#c4ff49" stroke="none"/>',
}
# STEP3 dot follows the dashed S-curve: sample it into keyframes
d3, p3 = gfx.path(("M", 8, 36), ("C", 16, 36, 14, 24, 24, 24), ("C", 34, 24, 32, 12, 40, 12))
MO.append('  .js-reveal .pg .timeline-list > li.is-on .hs-go { animation: hs-go 3s cubic-bezier(0.77, 0, 0.175, 1) infinite; }\n  @keyframes hs-go { 0%% { opacity: 0; transform: translate(0,0); } 10%% { opacity: 1; transform: translate(0,0); } %s 80%% { opacity: 1; } 92%%, 100%% { opacity: 0; transform: translate(%spx,%spx); } }'
          % (" ".join("%s%% { transform: translate(%spx,%spx); }" % (f(10 + 70 * i / (len(p3) - 1)), f(x - 8), f(y - 36)) for i, (x, y) in enumerate(p3) if 0 < i < len(p3) - 1), f(p3[-1][0] - 8), f(p3[-1][1] - 36)))
ST.append('.pg .hs-go { transform: translate(%spx,%spx); }' % (f(p3[-1][0] - 8), f(p3[-1][1] - 36)))

slots = {"{{HERO}}": hero_dial(), "{{WAVES}}": waves(), "{{DASH}}": dash(), "{{PLANNER}}": planner(), "{{TESTING}}": testing(),
         "{{TRANSIT}}": transit(), "{{FAQMOTIF}}": FAQMOTIF, "{{SUNRISE}}": sunrise(), "{{FAQ}}": faq_html(FAQ),
         "{{BC_URL}}": BC_URL, "{{CMAJ_URL}}": CMAJ_URL}
slots.update(STEPS)

body = open(os.path.join(HERE, "page.body.html"), encoding="utf-8").read()
body = re.sub(r"\{\{CI:(\w+):(\d+)\}\}", lambda m: ci(m.group(1), int(m.group(2))), body)
# body-copy guards (Alex): no disclaimers / captions / physician-aware wording; doctor mentions only in the FAQ
low = re.sub(r"<[^>]+>", " ", body).lower()
for bad in ("illustration only", "disclaimer", "911", "988", "physician-aware", "not a treatment", "metabolic", "calgary", "doctor", "physician"):
    assert bad not in low, "banned wording in body: " + bad
tmp = os.path.join(HERE, ".tmp"); os.makedirs(tmp, exist_ok=True)
open(os.path.join(tmp, "page.body.html"), "w", encoding="utf-8").write(body)
css = open(os.path.join(HERE, "page.css"), encoding="utf-8").read().replace("/*@GEN_STATIC*/", "\n".join(ST)).replace("/*@GEN_MOTION*/", "\n".join(MO))
open(os.path.join(tmp, "page.css"), "w", encoding="utf-8").write(css)
ld = jsonld(SLUG, TITLE, DESC, "Shift work, low energy and low testosterone in men", "Shift work", FAQ)
assemble(tmp, SLUG, TITLE, DESC, OG_ALT, ld, slots)
shutil.copy(os.path.join(tmp, "page.html"), os.path.join(HERE, "page.html"))
shutil.rmtree(tmp)
