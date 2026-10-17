"""Build /workspace/pages/testosterone-and-hair-loss/page.html (self-contained; paste into a GHL custom-code element when approved).
Edit page.body.html (markup), page.css (graphics CSS), this file (copy, FAQ, sources, SVG generators) or ../_shared/*; then: python3 build.py
FAQ HTML and FAQPage JSON-LD come from ONE list (FAQ), so they always match. Output is minified at the end (HighLevel save limit).
Template: /how-to-raise-testosterone-naturally (same pipeline). Every number is from /workspace/research-hairloss/SOURCES.md (fetched Oct 17 2026)."""
import sys, os, math, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_shared"))
from gfx import *
import common

SLUG = "testosterone-and-hair-loss"
TITLE = "Testosterone and Hair Loss: DHT and TRT | Odin Health Labs"
DESC = "Does low T or TRT cause hair loss? How DHT and genes drive balding, finasteride and dutasteride on TRT, other causes, and labs for men in Canada and USA."
OG_ALT = "Odin Health Labs: testosterone, DHT and hair loss in men, TRT, finasteride and dutasteride, other causes and labs"
assert len(TITLE) <= 60 and 140 <= len(DESC) <= 155, (len(TITLE), len(DESC))

common.ICONS.update({
 "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
 "hair": '<path d="M6 13a6 6 0 0 1 12 0v1.5a6 6 0 0 1-12 0z"/><path d="M6.5 10.5C8 6.5 10 5.5 12 5.5s4 1 5.5 5"/><path d="M9 6.5l1 2M15 6.5l-1 2"/>',
 "dna": '<path d="M7 3c0 5 10 7 10 12s-4 6-10 6"/><path d="M17 3c0 5-10 7-10 12"/><path d="M8.5 7h7M8 17h8M10 12h4"/>',
})

FAQ = [
 ("Does testosterone cause hair loss?",
  "Not on its own. Pattern hair loss is driven by DHT, a stronger hormone your body makes from testosterone, acting on scalp follicles that are genetically sensitive to it. In a study of 373 men in Germany, blood testosterone and other sex hormones were not linked with hair loss, and the authors pointed to follicle sensitivity instead. Variation in the androgen receptor gene, which sits on the X chromosome you inherit from your mother, is the strongest single genetic factor."),
 ("Does low testosterone cause hair loss?",
  "Low testosterone can thin body hair: the Endocrine Society lists loss of armpit and pubic hair as a specific sign of testosterone deficiency. Thinning at the temples and crown is a different process that follows your genes and DHT sensitivity. If your scalp hair is shedding all over, thyroid problems, low iron, a recent illness, stress or fast weight loss are more common causes, and simple labs can check most of them."),
 ("Will TRT make me go bald?",
  "Most men on TRT do not lose hair because of it. The Endocrine Society lists male pattern balding in men with a family tendency as an uncommon side effect, with weak evidence. If you are already thinning, TRT can add to what your genes are doing, so it helps to plan for it: keep your levels in the normal range, know that gels give moderately high DHT levels, and track your hairline with photos. We go through all of this with you before and during treatment."),
 ("Can I take finasteride while on TRT?",
  "Trials suggest the two can be combined. When DHT was blocked with dutasteride in 139 men, or with finasteride in 60 older men with low testosterone, testosterone still built muscle, strength and bone, and in the older men finasteride prevented testosterone-driven prostate growth. A 2014 review called the combination safe and effective so far but asked for longer studies. Finasteride lowers PSA, so your PSA baseline and its trend need to be read with that in mind."),
 ("Does finasteride affect fertility or libido?",
  "At the 1 mg hair-loss dose, a study of 181 young men found no significant change in sperm counts over almost a year. The higher 5 mg finasteride dose and dutasteride lowered total sperm counts by 29 to 34 percent at six months in healthy men, changes the authors called mild and likely to recover after stopping. In the main 1 mg trials, sexual side effects were reported by 3.8 percent of men on finasteride and 2.1 percent on placebo; the FDA label also lists sexual side effects that continued after stopping in some men, and both the FDA and Health Canada list mood changes, including suicidal thoughts. TRT itself lowers sperm production, so if children are in your plans, talk this through early."),
 ("How does Odin Health Labs work with my doctor?",
  'Odin Health Labs is an andropause and low testosterone telehealth service for men in Canada and the USA. We work alongside your own doctor: we go through your symptoms, hair history, family history, medications and lab results with you, help you decide which tests to ask your doctor for (such as morning testosterone, thyroid, iron studies and PSA), and build your plan for hormones, sleep, weight and nutrition. Finasteride, dutasteride and TRT are prescription medicines, so we help you prepare clear questions for the doctor who prescribes them, and we can share your plan and results with your doctor if you choose. See our <a href="%s/">low testosterone overview</a> and our <a href="%s/privacy">Privacy Policy</a>.' % (SITE, SITE)),
]

SRC = [
 ("source_endocrine_2018", "Bhasin S, Brito JP, Cunningham GR, et al. Testosterone Therapy in Men With Hypogonadism: An Endocrine Society Clinical Practice Guideline. <em>J Clin Endocrinol Metab</em> 2018;103(5):1715&ndash;1744.", "https://doi.org/10.1210/jc.2018-00229", "doi.org/10.1210/jc.2018-00229"),
 ("source_s3_2018", "Kanti V, Messenger A, Dobos G, et al. Evidence-based (S3) guideline for the treatment of androgenetic alopecia in women and in men, short version. <em>J Eur Acad Dermatol Venereol</em> 2018;32(1):11&ndash;22.", "https://doi.org/10.1111/jdv.14624", "doi.org/10.1111/jdv.14624"),
 ("source_hc_2026", "Health Canada. Summary Safety Review: Finasteride and Dutasteride, Assessing the Potential Risk of Suicidal Ideation (2026).", "https://dhpp.hpfb-dgpsa.ca/review-documents/resource/SSR1781100269999", "dhpp.hpfb-dgpsa.ca safety review"),
 ("source_fda_label", "US Food and Drug Administration. PROPECIA (finasteride) tablets, US label (2022).", "https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/020788s030lbl.pdf", "accessdata.fda.gov Propecia label"),
 ("source_fda_2012", "US Food and Drug Administration. Questions and Answers: Finasteride Label Changes (April 11, 2012; archived copy).", "https://web.archive.org/web/20140818144525/www.fda.gov/Drugs/DrugSafety/InformationbyDrugClass/ucm299754.htm", "fda.gov finasteride Q&amp;A (archived)"),
 ("source_medlineplus", "MedlinePlus Genetics, US National Library of Medicine. Androgenetic alopecia.", "https://medlineplus.gov/genetics/condition/androgenetic-alopecia/", "medlineplus.gov androgenetic alopecia"),
 ("source_kische_2017", "Kische H, Arnold A, Gross S, et al. Sex Hormones and Hair Loss in Men From the General Population of Northeastern Germany. <em>JAMA Dermatol</em> 2017;153(9):935&ndash;937.", "https://doi.org/10.1001/jamadermatol.2017.0297", "doi.org/10.1001/jamadermatol.2017.0297"),
 ("source_hillmer_2005", "Hillmer AM, Hanneken S, Ritzmann S, et al. Genetic variation in the human androgen receptor gene is the major determinant of common early-onset androgenetic alopecia. <em>Am J Hum Genet</em> 2005;77(1):140&ndash;148.", "https://doi.org/10.1086/431425", "doi.org/10.1086/431425"),
 ("source_heilmann_2017", "Heilmann-Heimbach S, Herold C, Hochfeld LM, et al. Meta-analysis identifies novel risk loci and yields systematic insights into the biology of male-pattern baldness. <em>Nat Commun</em> 2017;8:14694.", "https://doi.org/10.1038/ncomms14694", "doi.org/10.1038/ncomms14694"),
 ("source_kaufman_1998", "Kaufman KD, Olsen EA, Whiting D, et al. Finasteride in the treatment of men with androgenetic alopecia. <em>J Am Acad Dermatol</em> 1998;39(4):578&ndash;589.", "https://doi.org/10.1016/s0190-9622(98)70007-6", "doi.org/10.1016/s0190-9622(98)70007-6"),
 ("source_gupta_2022", "Gupta AK, Talukder M, Williams G. Comparison of oral minoxidil, finasteride, and dutasteride for treating androgenetic alopecia. <em>J Dermatolog Treat</em> 2022;33(7):2946&ndash;2962.", "https://doi.org/10.1080/09546634.2022.2109567", "doi.org/10.1080/09546634.2022.2109567"),
 ("source_gupta_nma_2022", "Gupta AK, Venkataraman M, Talukder M, Bamimore MA. Relative Efficacy of Minoxidil and the 5-&alpha; Reductase Inhibitors in Androgenetic Alopecia Treatment of Male Patients: A Network Meta-analysis. <em>JAMA Dermatol</em> 2022;158(3):266&ndash;274.", "https://doi.org/10.1001/jamadermatol.2021.5743", "doi.org/10.1001/jamadermatol.2021.5743"),
 ("source_amory_2007", "Amory JK, Wang C, Swerdloff RS, et al. The effect of 5&alpha;-reductase inhibition with dutasteride and finasteride on semen parameters and serum hormones in healthy men. <em>J Clin Endocrinol Metab</em> 2007;92(5):1659&ndash;1665.", "https://doi.org/10.1210/jc.2006-2203", "doi.org/10.1210/jc.2006-2203"),
 ("source_overstreet_1999", "Overstreet JW, Fuh VL, Gould J, et al. Chronic treatment with finasteride daily does not affect spermatogenesis or semen production in young men. <em>J Urol</em> 1999;162(4):1295&ndash;1300.", "https://pubmed.ncbi.nlm.nih.gov/10492183/", "pubmed.ncbi.nlm.nih.gov/10492183"),
 ("source_bhasin_2012", "Bhasin S, Travison TG, Storer TW, et al. Effect of testosterone supplementation with and without a dual 5&alpha;-reductase inhibitor on fat-free mass in men with suppressed testosterone production: a randomized controlled trial. <em>JAMA</em> 2012;307(9):931&ndash;939.", "https://doi.org/10.1001/jama.2012.227", "doi.org/10.1001/jama.2012.227"),
 ("source_borst_2014", "Borst SE, Yarrow JF, Conover CF, et al. Musculoskeletal and prostate effects of combined testosterone and finasteride administration in older hypogonadal men: a randomized, controlled trial. <em>Am J Physiol Endocrinol Metab</em> 2014;306(4):E433&ndash;E442.", "https://doi.org/10.1152/ajpendo.00592.2013", "doi.org/10.1152/ajpendo.00592.2013"),
 ("source_nickel_2014", "Nickel JC, Carson CC. Testosterone Supplementation in Hypogonadal Men on 5-ARI Therapy. <em>Sex Med Rev</em> 2014;2(2):75&ndash;78.", "https://doi.org/10.1002/smrj.27", "doi.org/10.1002/smrj.27"),
 ("source_bergfeld_2026", "Bergfeld WF, Mendez D. Shedding: An updated guide to a common cause of hair loss. <em>Cleve Clin J Med</em> 2026;93(10):616&ndash;622.", "https://doi.org/10.3949/ccjm.93a.26008", "doi.org/10.3949/ccjm.93a.26008"),
 ("source_malkud_2015", "Malkud S. Telogen Effluvium: A Review. <em>J Clin Diagn Res</em> 2015;9(9):WE01&ndash;WE03.", "https://doi.org/10.7860/JCDR/2015/15219.6492", "doi.org/10.7860/JCDR/2015/15219.6492"),
 ("source_walker_2026", "Walker CW, Champigny D, Hartman T, et al. Hair loss: a systematic approach to evaluation and management. <em>JAAPA</em> 2026;39(9):27&ndash;34.", "https://doi.org/10.1097/01.JAA.0000000000000405", "doi.org/10.1097/01.JAA.0000000000000405"),
 ("source_trost_2006", "Trost LB, Bergfeld WF, Calogeras E. Iron deficiency, its treatment and its potential relationship to hair loss (review). <em>J Am Acad Dermatol</em> 2006;54(5):824&ndash;844.", "https://doi.org/10.1016/j.jaad.2005.11.1104", "doi.org/10.1016/j.jaad.2005.11.1104"),
 ("source_viquez_2026", "Viquez Burboa GU, Flores Guill&eacute;n M&Aacute;R, Duardo Gonz&aacute;lez VS. GLP-1 Receptor Agonists and Alopecia: A Systematic Review and Meta-Analysis of Incidence, Risk, Subtypes, and Mechanisms. <em>Skin Appendage Disord</em> 2026.", "https://doi.org/10.1159/000553070", "doi.org/10.1159/000553070"),
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

def follicle(x, top, w, k, cls='hr-h'):
    """skin line at y=232; bulb at 250; a strand from the bulb up to `top` with stroke width w"""
    return ('<ellipse cx="%s" cy="252" rx="13" ry="10" fill="#142e14" stroke="rgba(255,255,255,0.6)" stroke-width="2"/>'
            '<g class="%s" style="--k:%d"><path d="M%s 244C%s %s %s %s %s %s" stroke="#c4ff49" stroke-width="%s" stroke-linecap="round" fill="none"/></g>'
            % (f(x), cls, k, f(x), f(x - 6), f((244 + top) / 2 + 20), f(x + 6), f((244 + top) / 2 - 10), f(x), f(top), w))

# ---------- hero: T rides through the 5-alpha reductase gate, becomes DHT, and follicles shrink ----------
def hero():
    s = ['<defs><radialGradient id="hl-g" cx="0.5" cy="0.5" r="0.55"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.14"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><ellipse cx="240" cy="168" rx="225" ry="140" fill="url(#hl-g)"/>']
    s.append(txt(240, 26, 'Testosterone, DHT and your follicles', 13, '#c4ff49', 0.9))
    s.append('<path d="M86 84H374" stroke="rgba(255,255,255,0.22)" stroke-width="3" stroke-dasharray="3 7"/>')
    d, pts = path(('M', 86, 84), ('L', 374, 84))
    s.append(dot('hr-d fx', 6, LIME, ring=True)); G.travel('hr-d', pts, 5, 60, 6, rest=pts[-1], rest_opacity=0, fade=4)
    s.append(node(60, 84, 26, 'gauge', 0.1, WHITE, isz=26))
    s.append('<g class="hr-gate">%s%s</g>' % (solid(176, 62, 128, 44, True, 12), txt(240, 89, '5-alpha reductase', 12, '#fff', 0.95)))
    s.append(node(408, 84, 28, 'flame', 0.3, LIME, fill='#142e14', isz=28))
    s.append(txt(60, 132, 'Testosterone', 12, '#fff', 0.85) + txt(240, 126, 'Enzyme in the scalp', 11.5, '#fff', 0.75) + txt(408, 132, 'DHT, stronger', 12, '#c4ff49', 0.95))
    line = 'M408 140C408 170 300 160 240 188'
    s.append('<path d="%s" stroke="rgba(196,255,73,0.25)" stroke-width="2.4" fill="none" stroke-dasharray="2 6"/>' % line)
    d, pts = path(('M', 408, 140), ('C', 408, 170, 300, 160, 240, 188), n=10)
    s.append(dot('hr-e fx', 5, LIME)); G.travel('hr-e', pts, 45, 80, 6, rest=pts[0], rest_opacity=0, fade=3)
    s.append('<path d="M40 232H440" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>')
    for k, (x, top, w, lab) in enumerate(((120, 150, 7, 'Thick'), (240, 182, 4, 'Finer'), (360, 212, 2, 'Miniaturized'))):
        s.append(follicle(x, top, w, k))
        s.append(txt(x, 286, lab, 12, '#c4ff49' if k == 0 else '#fff', 0.9))
    s.append(txt(240, 310, 'Inherited sensitivity decides how fast', 11.5, '#fff', 0.7))
    return '\n'.join(s)

# ---------- DHT: growth phase bars shorten on a sensitive follicle ----------
def dht_fig():
    s = [txt(16, 26, 'Hair growth cycle, one follicle', 13, '#c4ff49', 0.95, 'start')]
    rows = (('Typical follicle', 'Grows for 2 to 6 years, rests, then sheds', 330, False), ('DHT-sensitive follicle', 'Shorter growth, finer hair, slower regrowth', 150, True))
    for k, (a, b, gw, hot) in enumerate(rows):
        y = 52 + k * 82
        s.append(txt(16, y + 4, a, 13, '#c4ff49' if hot else '#fff', 0.95, 'start'))
        s.append('<rect x="16" y="%d" width="528" height="18" rx="9" fill="rgba(255,255,255,0.07)"/>' % (y + 14))
        s.append('<g class="dh-b" style="--k:%d"><rect x="16" y="%d" width="%d" height="18" rx="9" fill="#c4ff49" fill-opacity="%s"/></g>' % (k, y + 14, gw, 0.85 if not hot else 0.55))
        s.append('<g class="dh-r" style="--k:%d"><rect x="%d" y="%d" width="70" height="18" rx="9" fill="#fff" fill-opacity="0.45"/></g>' % (k, 24 + gw, y + 14))
        if hot:
            s.append('<path d="M%d %dH%d" stroke="rgba(255,255,255,0.45)" stroke-width="2" stroke-dasharray="3 5"/>' % (102 + gw, y + 23, 230 + gw))
            s.append(txt(166 + gw, y + 10, 'gap before regrowth', 11, '#fff', 0.7))
        s.append(txt(16, y + 52, b, 12, '#fff', 0.85, 'start'))
    s.append(txt(16, 214, 'Growth', 11, '#c4ff49', 0.85, 'start') + '<rect x="64" y="205" width="22" height="10" rx="5" fill="#fff" fill-opacity="0.45"/>' + txt(92, 214, 'Rest and shed', 11, '#fff', 0.8, 'start'))
    s.append(txt(544, 214, 'Balding scalp holds more DHT than hairy scalp', 11, '#fff', 0.7, 'end'))
    return '\n'.join(s)

# ---------- low T: three groups of men, same share thinning at every testosterone level ----------
def lowt_fig():
    s = [txt(280, 24, '373 men: hair loss compared with blood hormone levels', 12.5, '#c4ff49', 0.9)]
    lit = ((0, 5, 6), (2, 3, 7), (1, 4, 6))
    k = 0
    for c, lab in enumerate(('Lower T', 'Middle', 'Higher T')):
        cx = 100 + c * 180
        s.append(box(cx - 82, 40, 164, 132, c == 1, 14))
        for i in range(8):
            x = cx - 54 + (i % 4) * 36
            y = 74 + (i // 4) * 54
            hot = i in lit[c]
            s.append('<circle cx="%s" cy="%s" r="11" fill="#142e14" stroke="rgba(255,255,255,0.55)" stroke-width="1.8"/><path d="M%s %sq12 10 24 0" stroke="rgba(255,255,255,0.4)" stroke-width="2" fill="none"/>' % (f(x), f(y), f(x - 12), f(y + 22)))
            if hot:
                s.append('<g class="lt-h" style="--k:%d"><path d="M%s %sa11 11 0 0 1 22 0" stroke="#c4ff49" stroke-width="3" fill="none" stroke-linecap="round"/></g>' % (k % 3, f(x - 11), f(y - 1))); k += 1
        s.append(txt(cx, 192, lab, 12.5, '#fff', 0.9))
    s.append(txt(280, 220, 'Same share thinning at every level: no link with blood testosterone', 11.5, '#fff', 0.75))
    return '\n'.join(s)

# ---------- genes: X chromosome with the AR band glowing; 63 gene-region dots light row by row ----------
def genes_fig():
    s = ['<g transform="rotate(-24 100 110)"><rect x="88" y="34" width="24" height="152" rx="12" fill="#142e14" stroke="rgba(255,255,255,0.6)" stroke-width="2"/></g>',
         '<g transform="rotate(24 100 110)"><rect x="88" y="34" width="24" height="152" rx="12" fill="#142e14" stroke="rgba(255,255,255,0.6)" stroke-width="2"/></g>',
         '<g class="gn-ar"><rect x="84" y="62" width="32" height="12" rx="4" fill="#c4ff49" transform="rotate(24 100 110)"/></g>']
    s.append(txt(100, 206, 'AR gene, X chromosome', 12, '#c4ff49', 0.95) + txt(100, 224, 'from your mother', 11.5, '#fff', 0.8))
    s.append(txt(256, 26, '63 gene regions linked to male pattern baldness', 12.5, '#c4ff49', 0.95, 'start'))
    for r in range(7):
        d = ''.join('M%d %dh0' % (262 + c * 32, 52 + r * 22) for c in range(9))
        s.append('<path d="%s" stroke="rgba(255,255,255,0.3)" stroke-width="10" stroke-linecap="round"/>' % d)
        s.append('<g class="gn-r" style="--k:%d"><path d="%s" stroke="#c4ff49" stroke-width="10" stroke-linecap="round"/></g>' % (r, d))
    s.append(txt(256, 220, 'Together about 39 percent of the variation', 12, '#fff', 0.88, 'start'))
    return '\n'.join(s)

# ---------- TRT: a level dot rises into the normal band; three evidence rows light in turn ----------
def trt_fig():
    s = ['<rect x="40" y="20" width="46" height="180" rx="12" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.35)" stroke-width="1.8"/>',
         '<rect x="40" y="56" width="46" height="74" fill="rgba(196,255,73,0.14)"/>']
    s.append(txt(63, 218, 'Your T level', 11.5, '#fff', 0.8))
    s.append(txt(98, 96, 'Normal', 11, '#c4ff49', 0.9, 'start') + txt(98, 110, 'range', 11, '#c4ff49', 0.9, 'start'))
    s.append('<g class="tt-l"><circle cx="63" cy="96" r="9" fill="#c4ff49"/></g>')
    rows = (('Clear link with TRT', 'Acne, oily skin, higher red cell count', False),
            ('Uncommon, weak evidence', 'Pattern balding in men with a family tendency', True),
            ('Gels and underarm solution', 'Moderately high DHT, significance unknown', False))
    for k, (a, b, hot) in enumerate(rows):
        y = 16 + k * 66
        s.append('<g class="tt-r" style="--k:%d">%s%s%s%s</g>' % (k, box(160, y, 384, 56, hot, 12), ico('hair' if hot else ('drop' if k == 2 else 'mood'), 188, y + 28, 22, LIME, 2),
                 txt(212, y + 24, a, 13, '#c4ff49' if hot else '#fff', 0.95, 'start'), txt(212, y + 43, b, 12, '#fff', 0.85, 'start')))
    return '\n'.join(s)

# ---------- finasteride / dutasteride: DHT suppression bars + extra hairs vs placebo ----------
def fin_fig():
    s = [txt(16, 24, 'Serum DHT lowered by', 13, '#c4ff49', 0.95, 'start')]
    rows = (('Finasteride 1 mg, first day', 65), ('Finasteride 5 mg, one year', 73), ('Dutasteride 0.5 mg, one year', 94))
    for k, (lab, v) in enumerate(rows):
        y = 56 + k * 58
        s.append(txt(16, y, lab, 12, '#fff', 0.9, 'start'))
        s.append('<path d="M16 %dH186" stroke="rgba(255,255,255,0.1)" stroke-width="14" stroke-linecap="round"/>' % (y + 16))
        s.append('<g class="fn-b" style="--k:%d"><rect x="16" y="%d" width="%s" height="14" rx="7" fill="#c4ff49" fill-opacity="%s"/></g>' % (k, y + 9, f(v * 1.7), 0.85 if k == 2 else 0.6))
        s.append(txt(196, y + 21, '%d percent' % v, 12, '#c4ff49', 0.95, 'start'))
    s.append('<path d="M290 12V214" stroke="rgba(255,255,255,0.12)" stroke-width="2"/>')
    s.append(txt(312, 24, 'Extra hairs vs placebo, finasteride 1 mg', 12.5, '#c4ff49', 0.95, 'start'))
    for k, (lab, v) in enumerate((('Year 1', 107), ('Year 2', 138))):
        x = 352 + k * 110
        h = v * 1.05
        s.append('<rect x="%d" y="%s" width="50" height="%s" rx="6" fill="rgba(255,255,255,0.06)"/>' % (x, f(190 - 145), f(145)))
        s.append('<g class="fn-h" style="--k:%d"><rect x="%d" y="%s" width="50" height="%s" rx="6" fill="#c4ff49" fill-opacity="%s"/></g>' % (k, x, f(190 - h), f(h), 0.6 if k == 0 else 0.85))
        s.append(txt(x + 25, 184 - h, '+%d' % v, 13, '#fff', 0.95) + txt(x + 25, 208, lab, 12, '#fff', 0.85))
    s.append(txt(420, 228, 'One-inch circle at the crown, 1,553 men', 11, '#fff', 0.7))
    return '\n'.join(s)

# ---------- with TRT: testosterone still reaches muscle, strength and bone; the DHT gate blocks prostate growth ----------
def combo_fig():
    s = [node(62, 110, 30, 'gauge', 0.1, LIME, fill='#142e14', isz=28), txt(62, 160, 'Testosterone', 12, '#fff', 0.9), txt(62, 176, 'on TRT', 11.5, '#fff', 0.7)]
    outs = (('train', 'Muscle and strength', True), ('body', 'Bone density', True), ('scale', 'Fat loss', True), ('gland', 'Prostate growth', False))
    for k, (ic, lab, ok) in enumerate(outs):
        y = 30 + k * 54
        d, pts = path(('M', 94, 110), ('C', 180, 110, 200, y + 20, 300, y + 20), n=8)
        s.append('<path d="%s" stroke="rgba(255,255,255,0.16)" stroke-width="2.2" fill="none" stroke-dasharray="2 6"/>' % d)
        if ok:
            s.append(dot('cb-d%d fx' % k, 5, LIME)); G.travel('cb-d%d' % k, pts, 5 + k * 12, 40 + k * 12, 8, rest=pts[0], rest_opacity=0, fade=3)
        else:
            s.append('<g class="cb-x"><circle cx="246" cy="%d" r="12" fill="#0f240f" stroke="#c4ff49" stroke-width="2.4"/><path d="M241 %dl10 10M251 %dl-10 10" stroke="#c4ff49" stroke-width="2.6" stroke-linecap="round"/></g>' % (y + 17, y + 12, y + 12))
            s.append(txt(246, y + 46, 'DHT blocked', 10.5, '#c4ff49', 0.9))
        s.append('<g class="cb-r" style="--k:%d">%s%s%s%s</g>' % (k, box(304, y, 240, 40, ok and k == 0, 12), ico(ic, 326, y + 20, 18, LIME, 2), txt(344, y + 25, lab, 12.5, '#fff', 0.95, 'start'),
                 txt(532, y + 25, 'kept' if ok else 'prevented', 11.5, '#c4ff49', 0.95, 'end')))
    s.append(txt(424, 244, 'Trials of TRT with dutasteride or finasteride', 11, '#fff', 0.7))
    return '\n'.join(s)

# ---------- side effects: paired bars, finasteride 1 mg vs placebo, year one ----------
def sfx_fig():
    s = [txt(16, 24, 'Year one of the main finasteride 1 mg trials', 13, '#c4ff49', 0.95, 'start')]
    rows = (('Lower sex drive', 1.8, 1.3), ('Erection problems', 1.3, 0.7), ('Ejaculation changes', 1.2, 0.7), ('Any of these', 3.8, 2.1))
    sc = 280 / 3.8
    for k, (lab, a, b) in enumerate(rows):
        y = 46 + k * 42
        s.append(txt(16, y + 18, lab, 12.5, '#c4ff49' if k == 3 else '#fff', 0.92, 'start'))
        s.append('<g class="sx-b" style="--k:%d"><rect x="176" y="%d" width="%s" height="11" rx="5" fill="#c4ff49" fill-opacity="0.85"/><rect x="176" y="%d" width="%s" height="11" rx="5" fill="#fff" fill-opacity="0.45"/></g>' % (k, y + 4, f(a * sc), y + 18, f(b * sc)))
        s.append(txt(184 + a * sc, y + 13, '%s' % a, 11.5, '#c4ff49', 0.95, 'start') + txt(184 + b * sc, y + 27, '%s' % b, 11.5, '#fff', 0.85, 'start'))
    s.append('<rect x="176" y="222" width="14" height="10" rx="4" fill="#c4ff49" fill-opacity="0.85"/>' + txt(196, 231, 'Finasteride (945 men)', 11, '#fff', 0.85, 'start'))
    s.append('<rect x="352" y="222" width="14" height="10" rx="4" fill="#fff" fill-opacity="0.45"/>' + txt(372, 231, 'Placebo (934 men), percent', 11, '#fff', 0.85, 'start'))
    return '\n'.join(s)

# ---------- causes: three scalps seen from above, patterned / diffuse / patches ----------
def causes_fig():
    s = []
    def scalp(cx, cy):
        d = ''.join('M%s %sh0' % (f(cx + dx), f(cy + dy)) for dx in range(-44, 45, 11) for dy in range(-44, 45, 11) if dx * dx + dy * dy <= 44 * 44)
        return '<circle cx="%s" cy="%s" r="54" fill="#142e14" stroke="rgba(255,255,255,0.55)" stroke-width="2"/><path d="%s" stroke="#c4ff49" stroke-opacity="0.75" stroke-width="5" stroke-linecap="round"/>' % (f(cx), f(cy), d)
    cols = ((100, 'Patterned', 'Temples and crown', 'Genes and DHT'), (280, 'Diffuse', 'Thinning all over', 'Shedding, thyroid, iron'), (460, 'Patches', 'Round bare spots', 'Alopecia areata'))
    for k, (cx, a, b, c) in enumerate(cols):
        cy = 82
        s.append(scalp(cx, cy))
        if k == 0:
            g = '<circle cx="%d" cy="%d" r="20" fill="#0f240f"/><ellipse cx="%d" cy="%d" rx="13" ry="18" fill="#0f240f"/><ellipse cx="%d" cy="%d" rx="13" ry="18" fill="#0f240f"/>' % (cx, cy + 14, cx - 28, cy - 34, cx + 28, cy - 34)
        elif k == 1:
            g = '<circle cx="%d" cy="%d" r="50" fill="#0f240f" fill-opacity="0.55"/>' % (cx, cy)
        else:
            g = '<circle cx="%d" cy="%d" r="13" fill="#0f240f"/><circle cx="%d" cy="%d" r="9" fill="#0f240f"/>' % (cx - 16, cy - 10, cx + 20, cy + 18)
        s.append('<g class="cs-a" style="--k:%d">%s</g>' % (k, g))
        s.append(txt(cx, 162, a, 13, '#c4ff49', 0.95) + txt(cx, 182, b, 12, '#fff', 0.88) + txt(cx, 200, c, 11.5, '#fff', 0.7))
    return '\n'.join(s)

# ---------- labs: checklist ticks row by row while a magnifier scans down ----------
def labs_fig():
    s = [solid(40, 10, 480, 234, False, 14)]
    s.append(ico('tube', 66, 36, 18, LIME, 2) + txt(84, 41, 'Labs worth asking about', 13, '#c4ff49', 0.95, 'start'))
    rows = ('Two morning testosterone tests', 'TSH for your thyroid', 'Complete blood count and ferritin', 'PSA baseline before finasteride or TRT', 'Hematocrit and PSA once on TRT', 'Free T and SHBG if borderline')
    for k, lab in enumerate(rows):
        y = 72 + k * 29
        s.append('<rect x="64" y="%d" width="18" height="18" rx="4" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="1.8"/>' % (y - 13))
        s.append('<g class="lb-c" style="--k:%d"><path d="M67 %dl4 4 8-9" fill="none" stroke="#c4ff49" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></g>' % (k, y - 4))
        s.append(txt(94, y + 1, lab, 12.5, '#fff', 0.92, 'start'))
    s.append('<g class="lb-m"><circle cx="472" cy="64" r="15" fill="rgba(196,255,73,0.08)" stroke="#c4ff49" stroke-width="3"/><path d="M483 75l12 12" stroke="#c4ff49" stroke-width="4" stroke-linecap="round"/></g>')
    return '\n'.join(s)

# ---------- help: history + labs + goals -> telehealth assessment -> plan ----------
def help_fig():
    s = []
    for i, (y, ic, lab) in enumerate(((44, 'chat', 'Your history'), (115, 'tube', 'Your labs'), (186, 'hair', 'Your goals'))):
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
    for k, (ic, lab) in enumerate((('gauge', 'Hormones'), ('hair', 'Hair'), ('tube', 'Labs'), ('sleep', 'Habits'))):
        y = 76 + k * 34
        s.append('<g class="hp-r" style="--k:%d">%s%s</g>' % (k, ico(ic, 402, y, 18, LIME, 2), txt(420, y + 4, lab, 12.5, '#fff', 0.92, 'start')))
    return '\n'.join(s)

def final():
    s = ['<defs><radialGradient id="fn-g"><stop offset="0" stop-color="#c4ff49" stop-opacity="0.3"/><stop offset="1" stop-color="#c4ff49" stop-opacity="0"/></radialGradient></defs><circle cx="180" cy="105" r="92" fill="url(#fn-g)"/>']
    s.append('<circle class="fn-ring fx" cx="180" cy="104" r="56" fill="none" stroke="#c4ff49" stroke-width="2"/>')
    s.append('<g class="fn-sh"><path d="M180 48l46 17v34c0 30-20 48-46 56-26-8-46-26-46-56V65z" fill="#142e14" stroke="#c4ff49" stroke-width="4" stroke-linejoin="round"/></g>')
    s.append(dr('M160 104l14 14 28-30', 0.4, 0.9, '#fff', 5))
    s.append(node(56, 70, 20, 'hair', 0.3, WHITE, isz=22)); s.append(node(304, 70, 20, 'tube', 0.4, LIME, fill='#142e14', isz=22))
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
    icons = ['pills', 'drop', 'tube', 'scale', 'gauge', 'list']
    out = []
    for i, ic in enumerate(icons):
        a = -math.pi / 2 + (i + 0.5) * 2 * math.pi / len(icons)
        out.append((round(280 + 220 * math.cos(a)), round(100 + 66 * math.sin(a)), ic))
    return out

HUB = hub(G, hub_nodes())
slots = {"{{HERO}}": hero(), "{{DHT}}": dht_fig(), "{{LOWT}}": lowt_fig(), "{{GENES}}": genes_fig(), "{{TRT}}": trt_fig(), "{{FIN}}": fin_fig(),
         "{{COMBO}}": combo_fig(), "{{SFX}}": sfx_fig(), "{{CAUSES}}": causes_fig(), "{{LABS}}": labs_fig(),
         "{{HELP}}": help_fig(), "{{SOURCES}}": sources_fig(), "{{SRC}}": src_html(), "{{HUB}}": HUB,
         "{{FAQMOTIF}}": FAQMOTIF, "{{FINAL}}": final()}
slots.update(step_icons())
build(HERE, SLUG, TITLE, DESC, OG_ALT, FAQ, "Testosterone, DHT and hair loss in men: androgenetic alopecia, genetics, TRT, finasteride, dutasteride, other causes and labs",
      "Testosterone and hair loss", "Testosterone and hair loss: what DHT, genes and TRT really do", slots, G, published="2026-10-17")

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
