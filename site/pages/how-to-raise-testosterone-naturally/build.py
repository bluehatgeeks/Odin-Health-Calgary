"""Build /workspace/pages/how-to-raise-testosterone-naturally/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, sources, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match. Output is minified at the end (HighLevel save limit).
Every number is from /workspace/research-natural/SOURCES.md (fetched Oct 16 2026). nmol/L -> ng/dL conversions (x 28.84) are our arithmetic, shown as "about"."""
import sys, os, math, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "how-to-raise-testosterone-naturally"
TITLE = "How to Raise Testosterone Naturally | Odin Health Labs"
DESC = "What raises testosterone without TRT for men 35+: sleep, fat loss, training, alcohol, stress, vitamin D and zinc, and what boosters really do. Sourced."
OG_ALT = "Odin Health Labs: how to raise testosterone naturally with sleep, fat loss, training, alcohol, stress, vitamin D and zinc"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 155, (len(TITLE), len(DESC))

common.ICONS.update({
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
})

FAQ = [
 ("What is the fastest way to raise testosterone naturally?",
  "There is no overnight fix, but three levers have the best evidence: losing extra body fat, sleeping enough and staying active. In a meta-analysis of 24 studies, low-calorie diets raised total testosterone by 2.87 nmol/L on average (about 83 ng/dL), and in a <em>JAMA</em> study a week of five-hour nights lowered young men&rsquo;s daytime testosterone by 10 to 15 percent. Cutting back heavy drinking and reviewing medications such as opioids also help."),
 ("Do testosterone booster supplements work?",
  "Mostly not as advertised. A 2020 analysis of 50 &ldquo;T booster&rdquo; products found that 90 percent claimed to raise testosterone, yet 67 of their 109 ingredients had no published data on testosterone at all and 11 had data showing a fall. The Canadian Urological Association says boosters cannot be recommended and warns that some have contained banned substances, including steroids."),
 ("Can vitamin D or zinc raise testosterone?",
  "Mainly if you are deficient. In men with low vitamin D on a weight-loss program, a year of vitamin D raised total testosterone from 10.7 to 13.4 nmol/L, but later randomized trials found no effect, and a 2026 meta-analysis found no clear effect overall. Zinc raised testosterone in older men who were marginally deficient, while a zinc and magnesium supplement did nothing in men already eating enough zinc. Adult men need 11 mg of zinc a day and the upper limit is 40 mg, so test first and top up only what is low."),
 ("How much can lifestyle changes raise testosterone?",
  "Usually by a few nmol/L, not tens. Averages from the research: low-calorie diets about 2.9 nmol/L (about 83 ng/dL), bariatric surgery about 8.7 nmol/L (about 250 ng/dL), and the more weight lost, the bigger the rise. Sleep and alcohol work mostly by removing a drag: one week of five-hour nights cost about 10 to 15 percent of daytime testosterone. We test before and after so you can see your own change."),
 ("When is it time to think about TRT instead?",
  "When testosterone stays low on repeat morning tests after a fair try at the fixable causes and your symptoms persist, or when labs point to a problem in the pituitary or testes. The American Urological Association uses a total testosterone below 300 ng/dL on two early-morning tests, together with symptoms, as its definition of low testosterone."),
 ("How does Odin Health Labs work with my doctor?",
  'Odin Health Labs is an andropause and low testosterone telehealth service for men in Canada and the USA. We work alongside your own doctor: we go through your symptoms, history, medications and lab results with you, help you decide which tests to ask your doctor for, flag medications worth reviewing with whoever prescribes them, and build your sleep, weight, training, stress and nutrition plan. If TRT comes up, we help you prepare clear questions for your doctor. We can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]

SRC = [
 ("source_endocrine_2018", "Bhasin S, Brito JP, Cunningham GR, et al. Testosterone Therapy in Men With Hypogonadism: An Endocrine Society Clinical Practice Guideline. <em>J Clin Endocrinol Metab</em> 2018;103(5):1715&ndash;1744.", "https://doi.org/10.1210/jc.2018-00229", "doi.org/10.1210/jc.2018-00229"),
 ("source_aua_2018", "Mulhall JP, Trost LW, Brannigan RE, et al. Evaluation and Management of Testosterone Deficiency: AUA Guideline. <em>J Urol</em> 2018;200(2):423&ndash;432 (statement 21, lifestyle).", "https://doi.org/10.1016/j.juro.2018.03.115", "doi.org/10.1016/j.juro.2018.03.115"),
 ("source_cua_2021", "Grober ED, Krakowsky Y, Khera M, et al. Canadian Urological Association guideline on testosterone deficiency in men: Evidence-based Q&amp;A. <em>Can Urol Assoc J</em> 2021;15(5):E234&ndash;E243.", "https://doi.org/10.5489/cuaj.7252", "doi.org/10.5489/cuaj.7252"),
 ("source_corona_2013", "Corona G, Rastrelli G, Monami M, et al. Body weight loss reverts obesity-associated hypogonadotropic hypogonadism: a systematic review and meta-analysis. <em>Eur J Endocrinol</em> 2013;168(6):829&ndash;843.", "https://doi.org/10.1530/EJE-12-0955", "doi.org/10.1530/EJE-12-0955"),
 ("source_emas_2013", "Camacho EM, Huhtaniemi IT, O&rsquo;Neill TW, et al. Age-associated changes in hypothalamic-pituitary-testicular function in middle-aged and older men are modified by weight change and lifestyle factors: longitudinal results from the European Male Ageing Study. <em>Eur J Endocrinol</em> 2013;168(3):445&ndash;455.", "https://doi.org/10.1530/EJE-12-0890", "doi.org/10.1530/EJE-12-0890"),
 ("source_leproult_2011", "Leproult R, Van Cauter E. Research letter on a week of sleep restriction and testosterone levels in young healthy men. <em>JAMA</em> 2011;305(21):2173&ndash;2174.", "https://doi.org/10.1001/jama.2011.710", "doi.org/10.1001/jama.2011.710"),
 ("source_cignarelli_2019", "Cignarelli A, Castellana M, Castellana G, et al. Effects of CPAP on Testosterone Levels in Patients With Obstructive Sleep Apnea: A Meta-Analysis Study. <em>Front Endocrinol</em> 2019;10:551.", "https://doi.org/10.3389/fendo.2019.00551", "doi.org/10.3389/fendo.2019.00551"),
 ("source_hayes_2019", "Hayes LD, Elliott BT. Short-Term Exercise Training Inconsistently Influences Basal Testosterone in Older Men: A Systematic Review and Meta-Analysis. <em>Front Physiol</em> 2019;9:1878.", "https://doi.org/10.3389/fphys.2018.01878", "doi.org/10.3389/fphys.2018.01878"),
 ("source_kumagai_2016", "Kumagai H, Zempo-Miyaki A, Yoshikawa T, et al. Increased physical activity has a greater effect than reduced energy intake on lifestyle modification-induced increases in testosterone. <em>J Clin Biochem Nutr</em> 2016;58(1):84&ndash;89.", "https://doi.org/10.3164/jcbn.15-48", "doi.org/10.3164/jcbn.15-48"),
 ("source_friedl_2026", "Friedl KE, Nindl BC, Potter AW. Stress-associated testosterone suppression: central adaptation or hypogonadism? <em>J Clin Endocrinol Metab</em> 2026;111(8):e1951&ndash;e1960.", "https://doi.org/10.1210/clinem/dgag181", "doi.org/10.1210/clinem/dgag181"),
 ("source_sierksma_2004", "Sierksma A, Sarkola T, Eriksson CJ, et al. Effect of moderate alcohol consumption on plasma dehydroepiandrosterone sulfate, testosterone, and estradiol levels in middle-aged men and postmenopausal women: a diet-controlled intervention study. <em>Alcohol Clin Exp Res</em> 2004;28(5):780&ndash;785.", "https://doi.org/10.1097/01.alc.0000125356.70824.81", "doi.org/10.1097/01.alc.0000125356.70824.81"),
 ("source_smith_2023", "Smith SJ, Lopresti AL, Fairchild TJ. The effects of alcohol on testosterone synthesis in men: a review. <em>Expert Rev Endocrinol Metab</em> 2023;18(2):155&ndash;166.", "https://doi.org/10.1080/17446651.2023.2184797", "doi.org/10.1080/17446651.2023.2184797"),
 ("source_bawor_2015", "Bawor M, Bami H, Dennis BB, et al. Testosterone suppression in opioid users: a systematic review and meta-analysis. <em>Drug Alcohol Depend</em> 2015;149:1&ndash;9.", "https://doi.org/10.1016/j.drugalcdep.2015.01.038", "doi.org/10.1016/j.drugalcdep.2015.01.038"),
 ("source_pilz_2011", "Pilz S, Frisch S, Koertke H, et al. Effect of vitamin D supplementation on testosterone levels in men. <em>Horm Metab Res</em> 2011;43(3):223&ndash;225.", "https://doi.org/10.1055/s-0030-1269854", "doi.org/10.1055/s-0030-1269854"),
 ("source_lerchbaum_2017", "Lerchbaum E, Pilz S, Trummer C, et al. Vitamin D and Testosterone in Healthy Men: A Randomized Controlled Trial. <em>J Clin Endocrinol Metab</em> 2017;102(11):4292&ndash;4302.", "https://doi.org/10.1210/jc.2017-01428", "doi.org/10.1210/jc.2017-01428"),
 ("source_lerchbaum_2019", "Lerchbaum E, Trummer C, Theiler-Schwetz V, et al. Effects of vitamin D supplementation on androgens in men with low testosterone levels: a randomized controlled trial. <em>Eur J Nutr</em> 2019;58(8):3135&ndash;3146.", "https://doi.org/10.1007/s00394-018-1858-z", "doi.org/10.1007/s00394-018-1858-z"),
 ("source_paez_2026", "Paez-Allendes L, Valenzuela-Fuenzalida JJ, Moya MP, et al. Vitamin D Supplementation, Total Testosterone, and Androgen Bioavailability Markers in Adult Men: A Systematic Review and Meta-Analysis of Randomized Controlled Trials. <em>Nutrients</em> 2026;18(13):2090.", "https://doi.org/10.3390/nu18132090", "doi.org/10.3390/nu18132090"),
 ("source_prasad_1996", "Prasad AS, Mantzoros CS, Beck FW, et al. Zinc status and serum testosterone levels of healthy adults. <em>Nutrition</em> 1996;12(5):344&ndash;348.", "https://doi.org/10.1016/s0899-9007(96)80058-x", "doi.org/10.1016/s0899-9007(96)80058-x"),
 ("source_koehler_2009", "Koehler K, Parr MK, Geyer H, et al. Serum testosterone and urinary excretion of steroid hormone metabolites after administration of a high-dose zinc supplement. <em>Eur J Clin Nutr</em> 2009;63(1):65&ndash;70.", "https://doi.org/10.1038/sj.ejcn.1602899", "doi.org/10.1038/sj.ejcn.1602899"),
 ("source_nih_zinc", "NIH Office of Dietary Supplements. Zinc: Fact Sheet for Consumers (updated October 4, 2022).", "https://ods.od.nih.gov/factsheets/Zinc-Consumer/", "ods.od.nih.gov zinc fact sheet"),
 ("source_clemesha_2020", "Clemesha CG, Thaker H, Samplaski MK. &lsquo;Testosterone Boosting&rsquo; Supplements Composition and Claims Are not Supported by the Academic Literature. <em>World J Mens Health</em> 2020;38(1):115&ndash;122.", "https://doi.org/10.5534/wjmh.190043", "doi.org/10.5534/wjmh.190043"),
 ("source_balasubramanian_2019", "Balasubramanian A, Thirumavalavan N, Srivatsav A, et al. Testosterone Imposters: An Analysis of Popular Online Testosterone Boosting Supplements. <em>J Sex Med</em> 2019;16(2):203&ndash;212.", "https://doi.org/10.1016/j.jsxm.2018.12.008", "doi.org/10.1016/j.jsxm.2018.12.008"),
 ("source_fornalik_2026", "Fornalik M, Malkiewicz A, Adamczak D, et al. Hormonal Modulation with Withania somnifera: Systematic Review and Meta-Analysis of Randomized-controlled Trials. <em>Planta Med</em> 2026;92(8):790&ndash;805.", "https://doi.org/10.1055/a-2802-8363", "doi.org/10.1055/a-2802-8363"),
 ("source_fda_supplements", "US Food and Drug Administration. Information for Consumers on Using Dietary Supplements (content current as of October 21, 2022).", "https://www.fda.gov/food/dietary-supplements/information-consumers-using-dietary-supplements", "fda.gov dietary supplements"),
 ("source_hc_nhp", "Health Canada. Natural health product regulation in Canada: Overview.", "https://www.canada.ca/en/health-canada/services/drugs-health-products/natural-non-prescription/regulation.html", "canada.ca natural health products"),
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

# ---------- hero: five lever chips light in turn; the gauge needle steps up with each ----------
def hero():
    cx, cy, r = 240, 180, 112
    s = ['<defs><radialGradient id="nt-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.14"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="168" rx="225" ry="140" fill="url(#nt-g)"/>']
    tk = ''
    for i in range(11):
        a = math.pi + i * math.pi / 10
        tk += 'M%s %sL%s %s' % (f(cx + (r + 16) * math.cos(a)), f(cy + (r + 16) * math.sin(a)), f(cx + (r + 25) * math.cos(a)), f(cy + (r + 25) * math.sin(a)))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.4)" stroke-width="2" stroke-linecap="round"/>' % tk)
    arc = 'M%d %dA%d %d 0 0 1 %d %d' % (cx - r, cy, r, r, cx + r, cy)
    s.append('<path d="%s" stroke="rgba(255,255,255,0.12)" stroke-width="18" fill="none" stroke-linecap="round"/>' % arc)
    s.append('<path class="hr-arc" pathLength="100" d="%s" stroke="#c4ff49" stroke-width="18" fill="none" stroke-linecap="round" stroke-dasharray="100 100"/>' % arc)
    s.append('<g class="hr-nd"><path d="M%d %dL%d %d" stroke="#fff" stroke-width="5" stroke-linecap="round"/></g>' % (cx, cy, cx, cy - r + 22))
    s.append('<circle cx="%d" cy="%d" r="12" fill="#0f240f" stroke="#c4ff49" stroke-width="3"/>' % (cx, cy))
    s.append(txt(cx - r, cy + 26, 'Lower', 11.5, '#fff', 0.7) + txt(cx + r, cy + 26, 'Higher', 11.5, '#c4ff49', 0.9))
    s.append(txt(cx, cy + 36, 'Your testosterone', 13, '#fff', 0.9))
    s.append(txt(240, 30, 'Five levers you control', 13, '#c4ff49', 0.9))
    chips = (('sleep', 'Sleep'), ('scale', 'Fat loss'), ('train', 'Training'), ('wine', 'Alcohol'), ('stress', 'Stress'))
    for k, (ic, lab) in enumerate(chips):
        x = 8 + k * 93.5
        s.append('<g class="hr-t" style="--k:%d"><rect x="%s" y="262" width="86" height="32" rx="16" fill="rgba(255,255,255,0.05)" stroke="rgba(196,255,73,0.6)" stroke-width="1.6"/>%s%s</g>'
                 % (k, f(x), ico(ic, x + 18, 278, 16, LIME, 2), txt(x + 31, 282.5, lab, 11.5, '#fff', 0.92, 'start')))
    return '\n'.join(s)

# ---------- sleep: eleven nights of bedtimes (3 x 10 h, 8 x 5 h); the daytime T line steps down ----------
def sleep_fig():
    s = []
    for k in range(11):
        h = 10 if k < 3 else 5
        x = 50 + k * 44
        s.append('<g class="sl-b" style="--k:%d"><rect x="%d" y="%d" width="26" height="%d" rx="6" fill="%s" fill-opacity="%s"/></g>' % (k, x, 200 - h * 11, h * 11, LIME if k < 3 else WHITE, 0.75 if k < 3 else 0.45))
    s.append('<path d="M40 200H530" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>')
    s.append(txt(107, 220, '10-hour nights', 11.5, '#c4ff49', 0.9) + txt(349, 220, '5-hour nights', 11.5, '#fff', 0.85))
    line = 'M50 40H178C214 40 226 64 262 64H516'
    s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="3" fill="none"/>' % line)
    s.append(dr(line, 0.2, 1.4, LIME, 3))
    d, pts = path(('M', 50, 40), ('L', 178, 40), ('C', 214, 40, 226, 64, 262, 64), ('L', 516, 64), n=6)
    s.append(dot('sl-d fx', 6, LIME, ring=True)); G.travel('sl-d', pts, 5, 80, 9, rest=pts[-1], rest_opacity=0, fade=4)
    s.append(txt(114, 28, 'Daytime T 18.4 nmol/L', 12, '#c4ff49', 0.95) + txt(516, 52, '16.5 nmol/L', 12, '#fff', 0.92, 'end'))
    s.append('<g class="sl-n">%s%s</g>' % (box(282, 92, 236, 34, True, 12), txt(400, 114, 'Daytime T 10 to 15 percent lower', 12, '#fff', 0.95)))
    return '\n'.join(s)

# ---------- weight: a torso slims on a scale; two bars grow (diet vs surgery) ----------
def weight_fig():
    s = ['<circle cx="92" cy="50" r="16" fill="#142e14" stroke="rgba(255,255,255,0.6)" stroke-width="2.4"/>']
    s.append('<g class="wt-b"><ellipse cx="92" cy="122" rx="40" ry="52" fill="rgba(196,255,73,0.1)" stroke="#c4ff49" stroke-width="2.4"/></g>')
    s.append('<rect x="44" y="182" width="96" height="14" rx="7" fill="rgba(255,255,255,0.6)"/>')
    s.append('<g class="wt-w"><circle cx="92" cy="189" r="4" fill="#0f240f"/></g>')
    sc = 330 / 8.73
    for k, (y, lab, v, val, hot) in enumerate(((54, 'Low-calorie diet', 2.87, '+2.87 nmol/L, about 83 ng/dL', False), (128, 'Bariatric surgery', 8.73, '+8.73 nmol/L, about 250 ng/dL', True))):
        s.append(txt(196, y, lab, 13, '#c4ff49' if hot else '#fff', 0.95, 'start'))
        s.append('<path d="M196 %dH526" stroke="rgba(255,255,255,0.12)" stroke-width="16" stroke-linecap="round"/>' % (y + 18))
        s.append('<g class="wt-r" style="--k:%d"><rect x="196" y="%d" width="%s" height="16" rx="8" fill="#c4ff49" fill-opacity="%s"/></g>' % (k, y + 10, f(v * sc), 0.85 if hot else 0.55))
        s.append(txt(196, y + 48, val, 12, '#fff', 0.88, 'start'))
    s.append(txt(361, 222, '24 studies: more weight lost, bigger rise', 12, '#c4ff49', 0.9))
    return '\n'.join(s)

# ---------- training: a barbell lifts, step dots light; three result rows ----------
def train_fig():
    s = ['<path d="M24 160H180" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>']
    s.append('<g class="tr-bb"><path d="M38 92H166" stroke="#fff" stroke-width="5" stroke-linecap="round"/><rect x="44" y="70" width="14" height="44" rx="4" fill="#c4ff49"/><rect x="146" y="70" width="14" height="44" rx="4" fill="#c4ff49"/><rect x="30" y="78" width="10" height="28" rx="3" fill="rgba(196,255,73,0.6)"/><rect x="164" y="78" width="10" height="28" rx="3" fill="rgba(196,255,73,0.6)"/></g>')
    for k in range(7):
        s.append('<g class="tr-s" style="--k:%d"><ellipse cx="%d" cy="%d" rx="6" ry="9" fill="#c4ff49"/></g>' % (k, 34 + k * 22, 186 if k % 2 == 0 else 200))
    s.append(txt(102, 228, 'More daily steps, bigger rise', 11.5, '#fff', 0.8))
    rows = (('pulse', 'Endurance training', 'Small rise in resting T, men 60+', True), ('gauge', 'Interval training', 'Small rise in resting T, men 60+', True), ('train', 'Resistance training', 'No clear change in resting T, more muscle', False))
    for k, (ic, a, b, hot) in enumerate(rows):
        y = 18 + k * 68
        s.append('<g class="tr-r" style="--k:%d">%s%s%s%s</g>' % (k, box(214, y, 330, 56, hot, 12), ico(ic, 242, y + 28, 22, LIME, 2), txt(266, y + 24, a, 13, '#c4ff49' if hot else '#fff', 0.95, 'start'), txt(266, y + 43, b, 11.5, '#fff', 0.85, 'start')))
    return '\n'.join(s)

# ---------- alcohol: a glass drains while bubbles rise; two finding rows ----------
def alcohol_fig():
    glass = 'M52 36H130L120 172H62Z'
    s = ['<defs><clipPath id="al-c"><path d="%s"/></clipPath></defs>' % glass]
    s.append('<g clip-path="url(#al-c)"><g class="al-l"><rect x="40" y="62" width="104" height="112" fill="#c4ff49" fill-opacity="0.35"/></g></g>')
    for k, (x, y) in enumerate(((78, 150), (96, 160), (88, 130), (106, 146))):
        s.append('<g class="al-bu" style="--k:%d"><circle cx="%d" cy="%d" r="3.5" fill="#fff" fill-opacity="0.7"/></g>' % (k, x, y))
    s.append('<path d="%s" fill="none" stroke="#fff" stroke-opacity="0.75" stroke-width="3" stroke-linejoin="round"/>' % glass)
    s.append('<path d="M70 172V196M112 172V196" stroke="none"/><path d="M60 196H122" stroke="rgba(255,255,255,0.6)" stroke-width="4" stroke-linecap="round"/>')
    d, pts = path(('M', 146, 104), ('L', 184, 104))
    s.append('<path d="M146 104H184" stroke="rgba(255,255,255,0.25)" stroke-width="2.2" stroke-dasharray="2 6"/>')
    s.append(dot('al-d fx', 5, LIME)); G.travel('al-d', pts, 10, 40, 6, rest=pts[0], rest_opacity=0, fade=3)
    rows = (('About 40 g of alcohol a day, three weeks', 'Testosterone 6.8 percent lower (10 men)', True), ('Heavy or long-term drinking', 'Lowers testosterone production (2023 review)', False))
    for k, (a, b, hot) in enumerate(rows):
        y = 26 + k * 86
        s.append('<g class="al-r" style="--k:%d">%s%s%s</g>' % (k, box(196, y, 348, 66, hot, 12), txt(216, y + 28, a, 12.5, '#c4ff49' if hot else '#fff', 0.95, 'start'), txt(216, y + 49, b, 12, '#fff', 0.88, 'start')))
    return '\n'.join(s)

# ---------- stress: signal pulses run brain -> testes; stressor chips light in turn ----------
def stress_fig():
    s = []
    line = 'M100 82C200 40 360 124 460 82'
    s.append('<path d="%s" stroke="rgba(255,255,255,0.18)" stroke-width="3" fill="none" stroke-dasharray="3 7"/>' % line)
    d, pts = path(('M', 100, 82), ('C', 200, 40, 360, 124, 460, 82), n=10)
    for i in range(3):
        s.append(dot('st-p fx', 5.5, LIME).replace('<g class="st-p fx">', '<g class="st-p fx" style="animation-delay:%ss">' % f(-i * 2)))
    G.travel('st-p', pts, 5, 55, 6, rest=pts[0], rest_opacity=0, fade=3)
    s.append(node(70, 82, 28, 'brain', 0.1, LIME, fill='#142e14', isz=30) + node(490, 82, 28, 'gland', 0.3, WHITE, isz=28))
    s.append(txt(70, 134, 'Brain signal (LH)', 11.5, '#fff', 0.85) + txt(490, 134, 'Testes', 11.5, '#fff', 0.85))
    s.append(txt(280, 26, 'Sustained stress turns the signal down', 12.5, '#c4ff49', 0.9))
    for k, (ic, lab) in enumerate((('food', 'Big energy deficit'), ('sleep', 'Broken sleep'), ('stress', 'Uncontrolled stress'))):
        x = 16 + k * 180
        s.append('<g class="st-c" style="--k:%d">%s%s%s</g>' % (k, box(x, 156, 168, 38, k == 0, 19), ico(ic, x + 24, 175, 17, LIME, 2), txt(x + 40, 180, lab, 12, '#fff', 0.92, 'start')))
    return '\n'.join(s)

# ---------- medications: a checklist ticks row by row while a magnifier scans down ----------
def meds_fig():
    s = [solid(40, 12, 480, 206, False, 14)]
    s.append(ico('pills', 66, 38, 18, LIME, 2) + txt(84, 43, 'Medication and health review', 13, '#c4ff49', 0.95, 'start'))
    rows = ('Opioids, including methadone', 'Glucocorticoids such as prednisone', 'Anabolic steroids, using or stopping', 'Heavy alcohol or marijuana use', 'Snoring or untreated sleep apnea')
    for k, lab in enumerate(rows):
        y = 74 + k * 30
        s.append('<rect x="64" y="%d" width="18" height="18" rx="4" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="1.8"/>' % (y - 13))
        s.append('<g class="md-c" style="--k:%d"><path d="M67 %dl4 4 8-9" fill="none" stroke="#c4ff49" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></g>' % (k, y - 4))
        s.append(txt(94, y + 1, lab, 12.5, '#fff', 0.92, 'start'))
    s.append('<g class="md-m"><circle cx="462" cy="66" r="15" fill="rgba(196,255,73,0.08)" stroke="#c4ff49" stroke-width="3"/><path d="M473 77l12 12" stroke="#c4ff49" stroke-width="4" stroke-linecap="round"/></g>')
    return '\n'.join(s)

# ---------- vitamin D and zinc: 2 x 2 panels; bars rise only where men started low ----------
def vitz_fig():
    s = []
    cols = (('Vitamin D', 'sun', ('Deficient to start', '10.7 to 13.4 nmol/L', 10.7, 13.4), ('Enough or low T only', 'No clear effect in trials', 14, 14)),
            ('Zinc', 'caps', ('Marginally deficient', '8.3 to 16.0 nmol/L', 8.3, 16.0), ('Zinc-sufficient diet', 'No change with ZMA', 14, 14)))
    k = 0
    for c, (head, ic, a, b) in enumerate(cols):
        x = 16 + c * 272
        s.append(ico(ic, x + 12, 22, 18, LIME, 2) + txt(x + 28, 27, head, 14, '#c4ff49', 0.95, 'start'))
        for r, (lab, val, v0, v1) in enumerate((a, b)):
            y = 42 + r * 92
            up = r == 0
            g = [box(x, y, 256, 80, up, 12), txt(x + 14, y + 32, lab, 12.5, '#fff' if not up else '#c4ff49', 0.95, 'start'), txt(x + 14, y + 54, val, 12, '#fff', 0.85, 'start')]
            h0, h1 = v0 * 3.4, v1 * 3.4
            g.append('<rect x="%d" y="%s" width="16" height="%s" rx="3" fill="#fff" fill-opacity="0.4"/>' % (x + 196, f(y + 70 - h0), f(h0)))
            s.append('<g>%s</g>' % ''.join(g))
            s.append('<g class="vz-b%s" style="--k:%d"><rect x="%d" y="%s" width="16" height="%s" rx="3" fill="#c4ff49" fill-opacity="%s"/></g>' % (' vz-up' if up else '', k, x + 222, f(y + 70 - h1), f(h1), 0.85 if up else 0.5))
            k += 1
    s.append(txt(280, 226, 'Bars: before and after. Test first, top up only what is low', 11, '#fff', 0.65))
    return '\n'.join(s)

# ---------- boosters: ingredient dots float out of a bottle; four evidence bars grow ----------
def boost_fig():
    s = ['<path d="M50 74h56a8 8 0 0 1 8 8v120a8 8 0 0 1-8 8H50a8 8 0 0 1-8-8V82a8 8 0 0 1 8-8z" fill="#142e14" stroke="rgba(255,255,255,0.6)" stroke-width="2.4"/>',
         '<rect x="56" y="54" width="44" height="20" rx="4" fill="rgba(255,255,255,0.55)"/>', '<rect x="42" y="118" width="72" height="44" fill="rgba(196,255,73,0.14)"/>',
         txt(78, 137, 'T BOOST', 11, '#c4ff49', 0.95), txt(78, 153, '?', 13, '#fff', 0.8)]
    for k, (dx, c) in enumerate(((-14, LIME), (6, WHITE), (20, LIME), (-4, WHITE), (12, LIME))):
        s.append('<g class="bs-d" style="--k:%d;--dx:%dpx"><circle cx="78" cy="48" r="4.5" fill="%s"/></g>' % (k, dx, c))
    s.append(txt(150, 30, '109 ingredients in 50 &ldquo;T booster&rdquo; products', 13, '#c4ff49', 0.95, 'start'))
    rows = (('No published data on T', 67), ('Data showing a rise (15 also conflicting)', 27), ('Data showing no change', 20), ('Data showing a fall', 11))
    sc = 330 / 109
    for k, (lab, n) in enumerate(rows):
        y = 62 + k * 42
        s.append(txt(150, y, lab, 12.5, '#fff', 0.9, 'start'))
        s.append('<g class="bs-b" style="--k:%d"><rect x="150" y="%d" width="%s" height="13" rx="4" fill="#c4ff49" fill-opacity="%s"/></g>' % (k, y + 7, f(n * sc), 0.8 if k == 0 else 0.5))
        s.append(txt(150 + n * sc + 10, y + 18, str(n), 13, '#c4ff49', 0.95, 'start'))
    s.append(txt(150, 234, 'An ingredient can sit in more than one row (Clemesha, 2020)', 10.5, '#fff', 0.65, 'start'))
    return '\n'.join(s)

# ---------- expect: average changes drop onto a ruler of nmol/L ----------
def expect_fig():
    X = lambda v: 60 + (v + 3) * 40
    s = ['<path d="M60 150H540" stroke="rgba(255,255,255,0.5)" stroke-width="2.4" stroke-linecap="round"/>']
    s.append('<path d="%s" stroke="rgba(255,255,255,0.35)" stroke-width="1.4"/>' % ''.join('M%s 145V155' % f(X(v)) for v in range(-3, 10) if v % 3))
    s.append('<path d="%s" stroke="rgba(255,255,255,0.7)" stroke-width="2"/>' % ''.join('M%s 142V158' % f(X(v)) for v in range(-3, 10, 3)))
    for v in range(-3, 10, 3):
        if True:
            s.append(txt(X(v), 174, ('+%d' % v) if v > 0 else ('&minus;%d' % -v if v < 0 else '0'), 11.5, '#fff', 0.75))
    s.append('<path d="M%s 134V166" stroke="#c4ff49" stroke-width="2.4"/>' % f(X(0)))
    s.append(txt(540, 194, 'nmol/L', 11, '#fff', 0.65, 'end'))
    marks = ((-1.9, 'One week of short sleep', '&minus;1.9 (18.4 to 16.5)', 'up', WHITE), (0.47, 'Vitamin D, pooled trials', '+0.47, not a clear effect', 'down', WHITE),
             (2.87, 'Low-calorie diet', '+2.87 average', 'up', LIME), (8.73, 'Bariatric surgery', '+8.73 average', 'up', LIME))
    for k, (v, a, b, side, col) in enumerate(marks):
        x = X(v)
        anchor = 'end' if v > 8 else 'middle'
        tx = x + 8 if v > 8 else x
        if side == 'up':
            g = '<path d="M%s 98V142" stroke="rgba(255,255,255,0.35)" stroke-width="1.6" stroke-dasharray="3 3"/>' % f(x) + txt(tx, 70, a, 12, '#c4ff49' if col == LIME else '#fff', 0.95, anchor) + txt(tx, 88, b, 11.5, '#fff', 0.85, anchor)
        else:
            g = '<path d="M%s 158V190" stroke="rgba(255,255,255,0.35)" stroke-width="1.6" stroke-dasharray="3 3"/>' % f(x) + txt(tx, 208, a, 12, '#fff', 0.95, anchor) + txt(tx, 226, b, 11.5, '#fff', 0.85, anchor)
        s.append('<g class="ex-m" style="--k:%d">%s<circle cx="%s" cy="150" r="7" fill="#0f240f" stroke="%s" stroke-width="3"/></g>' % (k, g, f(x), col))
    s.append(txt(60, 30, 'Average change in total testosterone', 12.5, '#c4ff49', 0.9, 'start'))
    return '\n'.join(s)

# ---------- enough: a dot walks the decision path; nodes light in turn ----------
def enough_fig():
    s = []
    line = 'M95 53H465V163H95'
    s.append('<path d="%s" stroke="rgba(255,255,255,0.22)" stroke-width="2.4" fill="none" stroke-dasharray="2 7"/>' % line)
    d, pts = path(('M', 95, 53), ('L', 465, 53), ('L', 465, 163), ('L', 95, 163))
    s.append(dot('en-d fx', 6, LIME, ring=True)); G.travel('en-d', pts, 3, 88, 10, rest=pts[-1], rest_opacity=0, fade=3)
    nodes = ((95, 53, 'tube', 'Two morning tests'), (280, 53, 'question', 'Low, with symptoms'), (465, 53, 'leaf', 'Fix the causes'),
             (465, 163, 'tube', 'Recheck your labs'), (280, 163, 'question', 'Still low?'), (95, 163, 'chat', 'Talk through TRT'))
    for k, (x, y, ic, lab) in enumerate(nodes):
        hot = k in (2, 5)
        s.append('<g class="en-n" style="--k:%d">%s%s%s</g>' % (k, solid(x - 80, y - 23, 160, 46, hot, 12), ico(ic, x - 56, y, 18, LIME, 2), txt(x - 40, y + 4.5, lab, 12, '#fff', 0.95, 'start')))
    s.append(txt(280, 222, 'Pituitary or testicular causes need their own work-up', 11.5, '#c4ff49', 0.85))
    return '\n'.join(s)

# ---------- help: symptoms + labs + habits -> telehealth assessment -> plan ----------
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
    for k, (ic, lab) in enumerate((('sleep', 'Sleep'), ('scale', 'Fat loss'), ('train', 'Training'), ('stress', 'Stress'))):
        y = 76 + k * 34
        s.append('<g class="hp-r" style="--k:%d">%s%s</g>' % (k, ico(ic, 402, y, 18, LIME, 2), txt(420, y + 4, lab, 12.5, '#fff', 0.92, 'start')))
    return '\n'.join(s)

def final():
    s = ['<defs><radialGradient id="fn-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.3"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><circle cx="180" cy="105" r="92" fill="url(#fn-g)"/>']
    s.append('<circle class="fn-ring fx" cx="180" cy="104" r="56" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append('<g class="fn-sh"><path d="M180 48l46 17v34c0 30-20 48-46 56-26-8-46-26-46-56V65z" fill="#142e14" stroke="#c4ff49" stroke-width="4" stroke-linejoin="round"/></g>')
    s.append(dr('M160 104l14 14 28-30', 0.4, 0.9, '#fff', 5))
    s.append(node(56, 70, 20, 'sleep', 0.3, WHITE, isz=22)); s.append(node(304, 70, 20, 'train', 0.4, LIME, fill='#142e14', isz=22))
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
    icons = ['scale', 'sleep', 'calendar', 'pills', 'tube', 'caps']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)
        out.append((round(280 + 220 * math.cos(a)), round(100 + 66 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{SLEEP}}": sleep_fig(), "{{WEIGHT}}": weight_fig(), "{{TRAIN}}": train_fig(), "{{ALCOHOL}}": alcohol_fig(),
         "{{STRESS}}": stress_fig(), "{{MEDS}}": meds_fig(), "{{VITZ}}": vitz_fig(), "{{BOOST}}": boost_fig(), "{{EXPECT}}": expect_fig(),
         "{{ENOUGH}}": enough_fig(), "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(), "{{SRC}}": src_html(), "{{HUB}}": HUB,
         "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Raising testosterone naturally: sleep, fat loss, exercise, alcohol, stress, medications, vitamin D, zinc and supplements",
      "How to raise testosterone naturally", "How to raise testosterone naturally: what actually works", slots, G, published="2026-10-16")

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
