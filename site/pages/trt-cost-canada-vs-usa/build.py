"""Build /workspace/pages/trt-cost-canada-vs-usa/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, sources, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match. Output is minified at the end (HighLevel save limit).
Every price/number is from /workspace/research-trtcost/SOURCES.md (fetched Oct 16 2026)."""
import sys, os, math, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "trt-cost-canada-vs-usa"
TITLE = "TRT and Testosterone Cost: Canada vs USA | Odin Health Labs"
DESC = "TRT cost per month in Canada vs the USA (Oct 2026): clinic fees, testosterone cypionate, gel and pellet prices, lab tests, and what insurance covers."
OG_ALT = "Odin Health Labs: TRT cost in Canada vs the USA, lab tests, coverage, testosterone prices and monitoring"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 155, (len(TITLE), len(DESC))

common.ICONS.update({
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "coin": '<circle cx="12" cy="12" r="9"/><path d="M14.5 9.5c-.5-1-1.5-1.5-2.5-1.5-1.4 0-2.5.8-2.5 2s1 1.6 2.5 2 2.5.8 2.5 2-1.1 2-2.5 2c-1 0-2-.5-2.5-1.5M12 6.5V8M12 16v1.5"/>',
})

FAQ = [
 ("How much does TRT cost per month in Canada?",
  "For the drug itself, often less than people expect. Ontario and Alberta list generic testosterone cypionate at $34.88 CAD per 10 mL vial. At 100 mg a week one vial lasts about ten weeks, which works out to about $15 a month before the pharmacy&rsquo;s dispensing fee. Generic 1 percent gel at Ontario&rsquo;s price ($2.96 per 5 g packet) is about $89 for a month&rsquo;s supply of 30 packets. Labs and visits come on top, and public drug plans pay only in narrow cases, so the usual routes are private insurance or paying at the pharmacy. Prices as of October 2026 and they vary by province and pharmacy."),
 ("How much does TRT cost per month at a clinic?",
  "Most TRT clinics charge about $100 to $300 a month for visits and monitoring, and the medication is extra. That is the range Odin Health Labs sees across clinics; where a clinic falls depends on how often you are seen and whether extra medication or supplement support is included. Generic testosterone cypionate adds about $15 CAD a month at Ontario&rsquo;s list price, so by our arithmetic a clinic in that range comes to roughly $115 to $315 a month before labs and the pharmacy&rsquo;s dispensing fee. Ask each clinic what the monthly fee covers and whether labs are billed separately."),
 ("How much does TRT cost in the USA without insurance?",
  "Cash prices on Drugs.com in October 2026: generic testosterone cypionate from $37.99 USD per 10 mL vial, generic 1.62 percent gel $55.73 to $77.13 per 88 g pump, brand AndroGel 1 percent $318.13 to $683.83 for 30 packets, and Testopel pellets about $1,065 for ten pellets before the insertion visit. Clinics add more: in a 2022 study, a year of injections through cash-pay telehealth platforms cost $1,586 to $4,200. Consumer lab tests run $35 to $75 each at Quest with fees."),
 ("Does OHIP or my provincial plan cover testosterone testing?",
  "Provincial plans cover lab tests that are medically necessary. Ontario says OHIP covers them in community labs with a lab requisition, but PSA is covered only when prostate cancer is suspected or being followed; otherwise a LifeLabs PSA is $71. The private LifeLabs testosterone test (total, free and bioavailable T plus SHBG) is $98 and not covered by OHIP. In British Columbia the plan paid labs $15.81 for total testosterone, and the provincial protocol does not support testing men without symptoms or &ldquo;wellness&rdquo; testing."),
 ("Is TRT covered by provincial drug plans in Canada?",
  "Only in narrow cases. Ontario Drug Benefit covers people 65 and older and some other groups, and its testosterone products are Limited Use: low morning testosterone with documented hypothalamic, pituitary or testicular disease, or HIV, and older men with nonspecific symptoms and a low-normal level do not qualify. BC PharmaCare needs Special Authority for listed conditions such as hypogonadism or pituitary disease. Alberta lists generic cypionate injection as a regular benefit but not gels. Workplace and private plans vary, so check yours."),
 ("Is TRT cheaper in Canada or the USA?",
  "The generic injection lists at similar dollar figures: $34.88 CAD per vial on Ontario&rsquo;s and Alberta&rsquo;s lists versus from $37.99 USD cash. Gels are far cheaper on Canadian lists than brand gel at US cash prices, and pellets are a US option that Ontario&rsquo;s and Alberta&rsquo;s drug lists do not include. Labs are usually covered in Canada when medically necessary, while US cash tests cost $35 to $75 each and Medicare pays for one PSA a year for men over 50. The biggest US cost is often the clinic membership."),
 ("How does Odin Health Labs work with my doctor?",
  'Odin Health Labs is an andropause and low testosterone telehealth service for men in Canada and the USA. We work alongside your own doctor: we go through your symptoms, history and lab results with you, help you decide which tests to ask your doctor for and what your coverage is likely to pay for, prepare questions about TRT costs and options, and build your sleep, weight, stress and nutrition plan. We can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]

SRC = [
 ("source_bc_protocol", "British Columbia Ministry of Health, Guidelines and Protocols Advisory Committee. Testosterone Testing Protocol (revised October 27, 2022).", "https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/bc-guidelines/testosterone-testing", "gov.bc.ca testosterone testing protocol"),
 ("source_bc_hormone", "British Columbia Ministry of Health. Hormone Testing: Indications and Appropriate Use (revised October 27, 2022).", "https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/bc-guidelines/special-endocrine-testing", "gov.bc.ca hormone testing"),
 ("source_bc_pharmacare", "BC PharmaCare. Limited coverage criteria: testosterone injection (updated April 21, 2026).", "https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/pharmacare/programs/limited-coverage-drug-program/limited-coverage-drugs-testosterone-cypionate", "gov.bc.ca PharmaCare criteria"),
 ("source_ohip", "Government of Ontario. What OHIP covers (updated April 22, 2026) and Prostate cancer screening (updated February 4, 2026).", "https://www.ontario.ca/page/what-ohip-covers", "ontario.ca what OHIP covers"),
 ("source_odb", "Government of Ontario. Ontario Drug Benefit program: who qualifies and what you pay (updated August 18, 2026).", "https://www.ontario.ca/page/get-coverage-prescription-drugs", "ontario.ca Ontario Drug Benefit"),
 ("source_odb_formulary", "Ontario Ministry of Health. ODB Formulary search: testosterone (checked October 16, 2026); Limited Use code 397 as shown on rxcoverage.ca.", "https://www.formulary.health.gov.on.ca/formulary/results.xhtml?q=testosterone&amp;type=1", "formulary.health.gov.on.ca"),
 ("source_alberta_dbl", "Alberta Health Drug Benefit List, androgens (Alberta Blue Cross, checked October 16, 2026).", "https://idbl.ab.bluecross.ca/idbl/drugsList?ptc=680800", "idbl.ab.bluecross.ca androgens"),
 ("source_lifelabs", "LifeLabs. Testosterone Lab Test ($98) and PSA Lab Test ($71), Ontario store (checked October 16, 2026).", "https://store.lifelabs.com/on/wellness/product/testosterone-test-on", "store.lifelabs.com testosterone test"),
 ("source_dynacare", "Dynacare Plus. Men&rsquo;s Testosterone Home Testing Kit (checked October 16, 2026).", "https://shop.dynacareplus.com/mens-testosterone-home-test-kit.html", "shop.dynacareplus.com"),
 ("source_clhia", "Canadian Life and Health Insurance Association. Canadian Life &amp; Health Insurance Facts, 2025 Edition.", "https://www.clhia.ca/", "clhia.ca"),
 ("source_quest", "Quest consumer testing (questhealth.com): Testosterone, PSA and Complete Blood Count tests (checked October 16, 2026).", "https://www.questhealth.com/product/testosterone-test/15983M.html", "questhealth.com testosterone test"),
 ("source_labcorp", "Labcorp OnDemand. Comprehensive Testosterone Test (checked October 16, 2026).", "https://www.ondemand.labcorp.com/lab-tests/comprehensive-testosterone-test", "ondemand.labcorp.com"),
 ("source_drugs_com", "Drugs.com price guides: testosterone, Depo-Testosterone, AndroGel and Testopel (cash prices, checked October 16, 2026).", "https://www.drugs.com/price-guide/testosterone", "drugs.com price guide"),
 ("source_medicare", "Medicare.gov. Prostate cancer screenings.", "https://www.medicare.gov/coverage/prostate-cancer-screenings", "medicare.gov prostate cancer screenings"),
 ("source_jesse_2022", "Jesse E, Sellke N, Rivero MJ, et al. Practice Comparison and Cost Analysis of Direct-to-Consumer Telemedicine Platforms Offering Testosterone Therapy. <em>J Sex Med</em> 2022;19(11):1608&ndash;1615.", "https://doi.org/10.1016/j.jsxm.2022.03.609", "doi.org/10.1016/j.jsxm.2022.03.609"),
 ("source_dubin_2022", "Dubin JM, Jesse E, Fantus RJ, et al. Guideline-Discordant Care Among Direct-to-Consumer Testosterone Therapy Platforms. <em>JAMA Intern Med</em> 2022;182(12):1321&ndash;1323.", "https://doi.org/10.1001/jamainternmed.2022.4928", "doi.org/10.1001/jamainternmed.2022.4928"),
 ("source_endocrine_2018", "Bhasin S, Brito JP, Cunningham GR, et al. Testosterone Therapy in Men With Hypogonadism: An Endocrine Society Clinical Practice Guideline. <em>J Clin Endocrinol Metab</em> 2018;103(5):1715&ndash;1744.", "https://doi.org/10.1210/jc.2018-00229", "doi.org/10.1210/jc.2018-00229"),
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

# ---------- hero: a balance scale rocks between Canada (CAD) and USA (USD), coins drop in ----------
def hero():
    s = ['<defs><radialGradient id="cs-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.14"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="160" rx="225" ry="140" fill="url(#cs-g)"/>']
    s.append('<path d="M240 84V254" stroke="rgba(255,255,255,0.6)" stroke-width="5" stroke-linecap="round"/><rect x="196" y="252" width="88" height="10" rx="5" fill="rgba(255,255,255,0.6)"/>')
    s.append('<g class="hs-bm"><path d="M108 80H372" stroke="#fff" stroke-width="4.5" stroke-linecap="round"/></g>')
    for cls, x, a, b, hot in (('hs-pl', 108, 'Canada', 'CAD', True), ('hs-pr', 372, 'USA', 'USD', False)):
        col = '#c4ff49' if hot else '#fff'
        s.append('<g class="%s"><path d="M%d 80L%d 150M%d 80L%d 150" stroke="rgba(255,255,255,0.45)" stroke-width="1.8"/>' % (cls, x, x - 42, x, x + 42))
        s.append('<path d="M%d 150h96q-8 26-48 26t-48-26z" fill="%s" stroke="%s" stroke-width="2.4"/>' % (x - 48, 'rgba(196,255,73,0.14)' if hot else 'rgba(255,255,255,0.08)', col))
        for k in range(2):
            kk = k * 2 + (0 if hot else 1)
            s.append('<g class="hs-c" style="--k:%d"><circle cx="%d" cy="%d" r="11" fill="#0f240f" stroke="%s" stroke-width="2.2"/>%s</g>' % (kk, x - 12 + k * 24, 140, col, txt(x - 12 + k * 24, 144.5, '$', 13, col, 0.95)))
        s.append(txt(x, 204, a, 15, col, 0.95) + txt(x, 222, b, 12, '#fff', 0.75) + '</g>')
    s.append('<circle cx="240" cy="80" r="9" fill="#0f240f" stroke="#c4ff49" stroke-width="3"/>')
    for k, (ic, lab) in enumerate((('tube', 'Labs'), ('drop', 'The drug'), ('shield', 'Coverage'), ('chat', 'Check-ins'))):
        x = 24 + k * 110
        s.append('<g class="hs-t" style="--k:%d"><rect x="%d" y="280" width="100" height="30" rx="15" fill="rgba(255,255,255,0.05)" stroke="rgba(196,255,73,0.55)" stroke-width="1.6"/>%s%s</g>' % (k, x, ico(ic, x + 20, 295, 16, LIME, 2), txt(x + 34, 300, lab, 12, '#fff', 0.92, 'start')))
    s.append(txt(240, 36, 'Same therapy, two price tags', 13, '#c4ff49', 0.9))
    return '\n'.join(s)

# ---------- drivers: a four-part ring lights each cost driver ----------
def drivers():
    s = ['<circle cx="120" cy="115" r="72" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="22"/>']
    for k in range(4):
        s.append('<circle class="dv-a" style="--k:%d" cx="120" cy="115" r="72" fill="none" stroke="%s" stroke-width="22" pathLength="100" stroke-dasharray="23 77" stroke-dashoffset="%s" transform="rotate(-90 120 115)"/>' % (k, LIME if k % 2 == 0 else '#e8ffd0', f(-25 * k - 1)))
    s.append(txt(120, 112, 'Yearly', 14, '#fff', 0.92) + txt(120, 130, 'cost', 14, '#c4ff49', 0.92))
    rows = [('tube', 'Lab tests and how often'), ('drop', 'The form: shot, gel or pellet'), ('shield', 'Coverage: public, private or cash'), ('chat', 'Visits and clinic fees')]
    for k, (ic, lab) in enumerate(rows):
        y = 22 + k * 48
        s.append('<g class="dv-l" style="--k:%d">%s%s%s</g>' % (k, box(236, y, 308, 40, k % 2 == 0), ico(ic, 260, y + 20, 20, LIME, 2), txt(280, y + 25, lab, 13, '#fff', 0.92, 'start')))
    return '\n'.join(s)

# ---------- Canada labs: public path vs private path ----------
def calabs():
    s = [node(280, 40, 26, 'tube', 0.1, LIME, fill='#142e14', isz=28)]
    for i, (x, cls, col) in enumerate(((140, 'cl-a', LIME), (420, 'cl-b', WHITE))):
        d, pts = path(('M', 280, 68), ('C', 280, 104, x, 92, x, 124), n=10)
        s.append('<path d="%s" stroke="rgba(255,255,255,0.22)" stroke-width="2.2" stroke-dasharray="2 6" fill="none"/>' % d)
        s.append(dot('%s fx' % cls, 6, col, ring=True)); G.travel(cls, pts, 4 + i * 46, 40 + i * 46, 7, rest=pts[-1], rest_opacity=0, fade=3)
    s.append('<g class="cl-x" style="--k:0">%s%s%s%s</g>' % (box(16, 126, 248, 80, True, 14), txt(140, 150, 'Provincial plan', 14, '#c4ff49', 0.95),
             txt(140, 172, 'Medically necessary, with a requisition', 11.5, '#fff', 0.88), txt(140, 192, 'BC pays labs $15.81 for total T', 11.5, '#fff', 0.88)))
    s.append('<g class="cl-x" style="--k:1">%s%s%s%s</g>' % (box(296, 126, 248, 80, False, 14), txt(420, 150, 'Private pay', 14, '#fff', 0.95),
             txt(420, 172, 'LifeLabs T panel $98, PSA $71', 11.5, '#fff', 0.88), txt(420, 192, 'Home kit $99 to $138.99', 11.5, '#fff', 0.88)))
    s.append(txt(280, 230, 'Ontario: you pay for PSA unless cancer is suspected', 11.5, '#c4ff49', 0.9))
    return '\n'.join(s)

# ---------- provinces: three coverage panels light in turn ----------
def prov():
    s = []
    cols = [('Ontario', 'shield', ['Limited Use (code 397)', 'Drug Benefit: 65 and older', 'Needs documented disease']),
            ('British Columbia', 'doc', ['Special Authority', 'Hypogonadism, Klinefelter,', 'pituitary disease and more']),
            ('Alberta', 'check', ['Shots: regular benefit', 'Gels: not a benefit', 'Capsules: not for age decline'])]
    for k, (head, ic, lines) in enumerate(cols):
        x = 16 + k * 180
        g = [box(x, 16, 168, 152, k == 0, 14), '<rect x="%d" y="16" width="168" height="38" rx="14" fill="rgba(196,255,73,0.12)"/>' % x,
             ico(ic, x + 22, 35, 18, LIME, 2), txt(x + 38, 40, head, 12.5, '#c4ff49', 0.95, 'start')]
        for i, l in enumerate(lines):
            g.append(txt(x + 84, 84 + i * 28, l, 11.5, '#fff', 0.9))
        s.append('<g class="pv-p" style="--k:%d">%s</g>' % (k, ''.join(g)))
    s.append('<g class="pv-n">%s%s</g>' % (box(60, 182, 440, 34, True, 12), txt(280, 204, 'Age-related decline alone: excluded (ON note, AB capsules)', 12, '#fff', 0.92)))
    return '\n'.join(s)

# ---------- forms: a playhead sweeps one year; shots tick, gel flows, pellets pop ----------
def forms():
    x0, x1 = 120, 530
    s = ['<path d="M%d 196H%d" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>' % (x0, x1)]
    for x, lab in ((x0, 'Start'), ((x0 + x1) / 2, '6 mo'), (x1, '1 yr')):
        s.append('<path d="M%s 190v12" stroke="rgba(255,255,255,0.5)" stroke-width="2"/>%s' % (f(x), txt(x, 216, lab, 11, '#fff', 0.75)))
    lanes = [(48, 'drop', 'Shots', 'every week or two'), (106, 'pen', 'Gel', 'every day'), (160, 'gland', 'Pellets', 'every 3 to 6 mo')]
    for y, ic, lab, sub in lanes:
        s.append(ico(ic, 26, y, 18, LIME, 2) + txt(42, y + 2, lab, 13, '#c4ff49', 0.95, 'start') + txt(42, y + 18, sub, 10.5, '#fff', 0.72, 'start'))
    tk = ''.join('M%s 38v20' % f(x0 + i * (x1 - x0) / 26) for i in range(27))
    s.append('<path class="fm-k" d="%s" stroke="#c4ff49" stroke-width="2.4" stroke-linecap="round"/>' % tk)
    s.append('<path d="M%d 106H%d" stroke="#c4ff49" stroke-opacity="0.3" stroke-width="10" stroke-linecap="round"/>' % (x0, x1))
    s.append('<path class="fm-g" d="M%d 106H%d" stroke="#c4ff49" stroke-width="4" stroke-linecap="round" stroke-dasharray="6 6"/>' % (x0, x1))
    for k, fr in enumerate((0, 0.375, 0.75)):
        x = x0 + fr * (x1 - x0)
        s.append('<g class="fm-p" style="--k:%d"><circle cx="%s" cy="160" r="13" fill="#142e14" stroke="#fff" stroke-width="2.4"/><circle cx="%s" cy="160" r="4.5" fill="#c4ff49"/></g>' % (k, f(x), f(x)))
    s.append('<g class="fm-ph"><path d="M%d 26V188" stroke="#fff" stroke-opacity="0.7" stroke-width="2" stroke-dasharray="3 4"/><circle cx="%d" cy="26" r="5" fill="#fff"/></g>' % (x0, x0))
    return '\n'.join(s)

# ---------- prices: Canada list prices (CAD) and US cash prices (USD) ----------
def prices():
    ca = [('Cypionate, 10 mL vial', 34.88, None, '$34.88'), ('Enanthate, 5 mL vial (Ontario)', 35.59, None, '$35.59'),
          ('Gel 1%, 30 packets, generic', 88.73, None, '$88.73'), ('Gel 1%, 30 packets, brand', 135.35, None, '$135.35')]
    us = [('Cypionate 10 mL, generic', 37.99, None, 'from $37.99'), ('Depo-Testosterone 10 mL', 44.70, 93.29, '$44.70 to $93.29'),
          ('Gel 1.62%, 88 g pump', 55.73, 77.13, '$55.73 to $77.13'), ('AndroGel 1%, 30 packets', 318.13, 683.83, '$318 to $684'),
          ('Testopel, 10 pellets', 1064.63, None, 'about $1,065')]
    s = []
    k = 0
    for rows, y0, mx, head in ((ca, 26, 135.35, 'Canada, government list prices (CAD)'), (us, 218, 1064.63, 'USA, cash prices on Drugs.com (USD)')):
        s.append(txt(16, y0, head, 14, '#c4ff49', 0.95, 'start'))
        sc = 390 / mx
        for i, (lab, lo, hi, val) in enumerate(rows):
            y = y0 + 30 + i * 38
            s.append(txt(16, y, lab.replace('%', '&#37;'), 13, '#fff', 0.9, 'start'))
            w = max(lo * sc, 4)
            g = '<rect x="16" y="%d" width="%s" height="13" rx="4" fill="#c4ff49" fill-opacity="0.75"/>' % (y + 7, f(w))
            if hi:
                g += '<rect x="%s" y="%d" width="%s" height="13" rx="4" fill="#c4ff49" fill-opacity="0.3"/>' % (f(16 + w), y + 7, f(max((hi - lo) * sc, 2)))
            s.append('<g class="pr-b" style="--k:%d">%s</g>' % (k, g)); k += 1
            s.append(txt(16 + (hi or lo) * sc + 10, y + 18, val, 13, '#c4ff49' if rows is ca else '#fff', 0.95, 'start'))
    s.append(txt(544, 218, 'Each chart has its own scale', 11, '#fff', 0.6, 'end'))
    return '\n'.join(s)

# ---------- US labs: a receipt prints line by line, Medicare badge ----------
def uslabs():
    s = ['<rect x="30" y="12" width="270" height="206" rx="12" fill="#142e14" stroke="rgba(255,255,255,0.45)" stroke-width="2"/>']
    s.append(txt(165, 38, 'Quest, cash price (USD)', 12.5, '#c4ff49', 0.95))
    rows = [('Total testosterone', '$69 + $6'), ('PSA', '$69 + $6'), ('Blood count (hematocrit)', '$29 + $6')]
    for k, (a, b) in enumerate(rows):
        y = 72 + k * 32
        s.append('<g class="ul-l" style="--k:%d">%s%s</g>' % (k, txt(48, y, a, 12, '#fff', 0.9, 'start'), txt(282, y, b, 12, '#fff', 0.9, 'end')))
    s.append('<g class="ul-l" style="--k:3"><path d="M48 158H282" stroke="rgba(255,255,255,0.35)" stroke-width="1.6" stroke-dasharray="4 4"/>%s%s</g>' % (txt(48, 186, 'Total', 13, '#c4ff49', 0.95, 'start'), txt(282, 186, '$185', 15, '#c4ff49', 0.95, 'end')))
    s.append('<g class="ul-m"><circle cx="430" cy="92" r="58" fill="rgba(196,255,73,0.08)" stroke="#c4ff49" stroke-width="2.4"/></g>')
    s.append(txt(430, 80, 'Medicare', 13, '#fff', 0.9) + txt(430, 106, 'PSA $0', 18, '#c4ff49', 0.95))
    s.append(txt(430, 172, 'once a year, men over 50', 11.5, '#fff', 0.85) + txt(430, 192, 'HSA and FSA accepted at Quest', 11, '#fff', 0.65))
    return '\n'.join(s)

# ---------- telehealth: one year of injections, cash platforms vs insured ----------
def tele():
    X = lambda v: 40 + v * 480 / 4500
    s = []
    for k, (y, lab, lo, hi, a, b, hot) in enumerate(((52, 'Cash-pay telehealth platforms', 1586, 4200, '$1,586', '$4,200', True),
                                                       (124, 'Tertiary center, insurance or Medicare', 134.01, 1333.04, '$134', '$1,333', False))):
        s.append(txt(40, y - 14, lab, 12.5, '#c4ff49' if hot else '#fff', 0.95, 'start'))
        s.append('<path d="M40 %dH520" stroke="rgba(255,255,255,0.14)" stroke-width="14" stroke-linecap="round"/>' % (y + 6))
        s.append('<g class="te-b" style="--k:%d"><rect x="%s" y="%d" width="%s" height="14" rx="7" fill="%s" fill-opacity="%s"/></g>' % (k, f(X(lo)), y - 1, f(X(hi) - X(lo)), LIME if hot else WHITE, 0.8 if hot else 0.6))
        s.append(txt(X(lo), y + 32, a, 11.5, '#fff', 0.9) + txt(X(hi), y + 32, b, 11.5, '#fff', 0.9))
    s.append('<g class="te-n">%s%s</g>' % (box(40, 176, 480, 34, True, 12), txt(280, 198, 'Secret shopper: 6 of 7 platforms offered T to a man with normal levels', 11.5, '#fff', 0.92)))
    return '\n'.join(s)

# ---------- monitoring: dot walks baseline -> 3 mo -> 6 mo -> yearly, costs light ----------
def monitor():
    s = ['<path d="M70 58H490" stroke="rgba(255,255,255,0.18)" stroke-width="4" stroke-linecap="round"/>', dr('M70 58H490', 0.2, 1.4, LIME, 4)]
    for j, head in enumerate(('Baseline', '3 mo', '6 mo', 'Every year')):
        x = 70 + j * 140
        s.append(txt(x, 32, head, 13, '#c4ff49', 0.95))
        s.append('<g class="mo-n" style="--k:%d"><circle cx="%d" cy="58" r="11" fill="#0f240f" stroke="#c4ff49" stroke-width="3"/></g>' % (j, x))
        s.append('<g class="mo-c" style="--k:%d">%s%s%s</g>' % (j, box(x - 60, 82, 120, 52, False, 10), txt(x, 104, '$169 CAD', 12.5, '#c4ff49', 0.95), txt(x, 124, '$185 USD', 12.5, '#fff', 0.92)))
    d, pts = path(('M', 70, 58), ('L', 490, 58))
    s.append(dot('mo-d fx', 7, LIME, ring=True)); G.travel('mo-d', pts, 5, 85, 8.5, rest=pts[-1], rest_opacity=0, fade=4)
    s.append('<g class="mo-t">%s%s</g>' % (box(50, 156, 460, 40, True, 12), txt(280, 182, 'First six months, all private: $507 CAD or $555 USD', 13, '#fff', 0.95)))
    return '\n'.join(s)

# ---------- sample year: the injection math, step by step ----------
def year():
    s = ['<rect x="16" y="10" width="528" height="210" rx="14" fill="#142e14" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>']
    steps = [('drop', '1 vial: 10 mL at 100 mg/mL = 1,000 mg'), ('clock', 'At 100 mg a wk, one vial lasts 10 wk'), ('calendar', '52 wk / 10 = 5.2 vials a year')]
    for k, (ic, t) in enumerate(steps):
        y = 42 + k * 36
        s.append('<g class="yr-s" style="--k:%d">%s%s</g>' % (k, ico(ic, 48, y - 4, 20, LIME, 2), txt(70, y + 1, t, 13, '#fff', 0.92, 'start')))
    for k, (x, a, b, hot) in enumerate(((36, 'x $34.88 (Ontario list)', 'about $181 CAD a year', True), (288, 'x $37.99 (US cash, lowest)', 'about $198 USD a year', False))):
        s.append('<g class="yr-r" style="--k:%d">%s%s%s</g>' % (k, box(x, 146, 236, 50, hot, 12), txt(x + 118, 166, a, 11.5, '#fff', 0.85), txt(x + 118, 186, b, 14, '#c4ff49' if hot else '#fff', 0.95)))
    s.append(txt(280, 212, 'Drug only: add labs, dispensing and visit fees', 10.5, '#fff', 0.65))
    return '\n'.join(s)

# ---------- help: labs + coverage + budget -> telehealth review -> plan ----------
def help_fig():
    s = []
    for i, (y, ic, lab) in enumerate(((44, 'tube', 'Your labs'), (115, 'shield', 'Your coverage'), (186, 'coin', 'Your budget'))):
        s.append(node(40, y, 22, ic, 0.1 + i * 0.1, LIME if i != 1 else WHITE, isz=22) + txt(70, y + 4, lab, 12.5, '#fff', 0.9, 'start'))
        d, pts = path(('M', 166, y), ('C', 206, y, 214, 115, 244, 115), n=10)
        s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % d)
        s.append(dot('hp-a%d fx' % i, 5, WHITE)); G.travel('hp-a%d' % i, pts, 6 + i * 10, 40 + i * 10, 7, rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(276, 115, 30, 'video', 0.4, LIME, fill='#173617', isz=28) + txt(276, 168, 'Telehealth review', 12, '#fff', 0.88))
    d, pts = path(('M', 308, 115), ('L', 372, 115))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" stroke-dasharray="2 7" fill="none"/>' % d)
    s.append(dot('hp-b fx', 5, LIME)); G.travel('hp-b', pts, 50, 72, 7, rest=pts[0], rest_opacity=0, fade=3)
    s.append('<g class="pop t" style="--d:0.5"><rect x="376" y="22" width="168" height="186" rx="14" fill="#142e14" stroke="rgba(255,255,255,0.55)" stroke-width="2"/></g>')
    s.append(txt(460, 46, 'Your plan', 13, '#c4ff49', 0.95))
    for k, (ic, lab) in enumerate((('sleep', 'Sleep'), ('scale', 'Weight'), ('stress', 'Stress'), ('food', 'Nutrition'))):
        y = 76 + k * 34
        s.append('<g class="hp-r" style="--k:%d">%s%s</g>' % (k, ico(ic, 402, y, 18, LIME, 2), txt(420, y + 4, lab, 12.5, '#fff', 0.92, 'start')))
    return '\n'.join(s)

# ---------- clinic fees: monthly fee range, then with the drug added; what moves the fee lights in turn ----------
def clinic():
    X = lambda v: 40 + v * 480 / 350
    s = []
    for k, (y, lab, lo, hi, a, b, hot) in enumerate(((50, 'Clinic fee per month, medication not included', 100, 300, '$100', '$300', True),
                                                       (120, 'With generic cypionate added (about $15 CAD a month)', 115, 315, '$115', '$315', False))):
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
    s.append(node(56, 70, 20, 'tube', 0.3, WHITE, isz=22)); s.append(node(304, 70, 20, 'coin', 0.4, LIME, fill='#142e14', isz=22))
    return '\n'.join(s)

FAQMOTIF = '''<g class="fq-dp"><circle cx="28" cy="50" r="18" stroke="#c4ff49" stroke-width="4"/><path d="M33 43c-1-2-3-3-5-3-3 0-5 1.6-5 4s2 3.2 5 4 5 1.6 5 4-2 4-5 4c-2 0-4-1-5-3M28 36v4M28 60v4" stroke="#c4ff49" stroke-width="3" stroke-linecap="round"/></g>
<path class="dr" pathLength="1" style="--d:0.25;--dur:1.1s" d="M70 36c0-8 6-12 12-12s12 4 12 10c0 6-5 8-8 11-3 2-4 4-4 8" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="82" cy="64" r="3" fill="#fff"/>
<g class="fq-fr" style="--k:0"><circle cx="104" cy="22" r="5" fill="#c4ff49"/></g><g class="fq-fr" style="--k:1"><circle cx="50" cy="20" r="4" fill="#c4ff49"/></g>'''

def step_icons():
    return {
     "{{STEP1}}": '<path d="M8 12h32a2 2 0 0 1 2 2v18a2 2 0 0 1-2 2H22l-8 6v-6H8a2 2 0 0 1-2-2V14a2 2 0 0 1 2-2z"/><g class="hi-bl" style="--k:0"><circle cx="16" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:1"><circle cx="24" cy="23" r="2" fill="#c4ff49" stroke="none"/></g><g class="hi-bl" style="--k:2"><circle cx="32" cy="23" r="2" fill="#c4ff49" stroke="none"/></g>',
     "{{STEP2}}": '<path d="M12 6h10"/><path d="M14 6v26a3 3 0 0 0 6 0V6"/><path d="M14 20h6"/><g class="hi-gr" style="--k:0"><path d="M30 40V30M36 40V22M42 40V34" stroke="#c4ff49"/></g>',
     "{{STEP3}}": '<path d="M8 38C8 22 18 12 40 10c0 22-10 30-26 30"/><g class="hi-sw" style="--k:0"><path d="M8 38c6-9 12-15 20-19" stroke="#c4ff49"/></g>',
     "{{STEP4}}": '<path d="M6 40h36"/><path d="M8 34l9-8 7 5 14-14"/><g class="hi-ck" style="--k:0"><path d="M30 8l4 4 8-9" stroke="#c4ff49"/></g>',
    }

def hub_nodes():
    icons = ['drop', 'tube', 'scale', 'link', 'compass', 'coach']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)
        out.append((round(280 + 220 * math.cos(a)), round(100 + 66 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{DRIVERS}}": drivers(), "{{CALABS}}": calabs(), "{{PROV}}": prov(), "{{FORMS}}": forms(), "{{PRICES}}": prices(),
         "{{USLABS}}": uslabs(), "{{TELE}}": tele(), "{{MONITOR}}": monitor(), "{{YEAR}}": year(), "{{CLINIC}}": clinic(), "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(),
         "{{SRC}}": src_html(), "{{HUB}}": HUB, "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "TRT cost in Canada vs the USA: lab tests, coverage, testosterone prices and monitoring",
      "TRT cost: Canada vs USA", "How much do TRT and testosterone cost in Canada vs the USA?", slots, G, published="2026-10-16", modified="2026-10-23")

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
