# /testosterone-calculator: sources (checked 2026-10-18; local copies in this folder)
Every number on the page maps to one of these. Nothing is estimated or invented.

## Conversion factors
- PubChem CID 6013, testosterone C19H28O2, molecular weight 288.4 g/mol (https://pubchem.ncbi.nlm.nih.gov/compound/6013; saved /workspace/research-freet/pubchem.json).
  Derived: 1 nmol/L = 288.4 ng/L = 28.84 ng/dL; 1 pg/mL = 1000/288.4 pmol/L = 3.467 pmol/L.
  Cross-check against Endocrine Society 2018 pairs: 264 ng/dL = 9.2 nmol/L, 916 = 31.8, 320 = 11, 64 pg/mL = 220 pmol/L (ES rounds 221.9).

## Vermeulen equation and validation
- Vermeulen A, Verdonck L, Kaufman JM. J Clin Endocrinol Metab 1999;84(10):3666-72. doi 10.1210/jcem.84.10.6079. PMID 10523012 (abstract: vermeulen_abstract.txt). Calculated free T agrees with equilibrium dialysis under all conditions studied except pregnancy. The OUP full text is blocked, so the constants are taken from the next two sources.
- ISSAM free testosterone calculator, worked example (https://issam.ch/freetesuit.html; issam_freetesuit.html). The same text is in the LASA appendix A (lasa_appendixA.pdf/.txt).
  Constants: Ka (albumin) 3.6e4 L/mol; albumin MW 69,000; K (SHBG) 1e9 L/mol; default albumin 4.3 g/dL (43 g/L).
  Example: total T 10 nmol/L (288.4 ng/dL), SHBG 40 nmol/L, albumin 4.3 g/dL. Result: N = 23.43; [S] = 1.7388e-10 mol/L; 1.74 percent free; FT 5.02 ng/dL; Bio T 118 ng/dL.
  Note: ISSAM prints "48.86e9" in the denominator, a typo for 2a = 2 x 23.43e9 = 46.86e9. Their final result only works with 46.86e9.
- de Ronde W et al. Clin Chem 2006;52(9):1777-84. doi 10.1373/clinchem.2005.063354. Compares 5 published algorithms. Vermeulen constants: SHBG association constant 1e9 L/mol (printed as 10e8), albumin 3.6e4 L/mol, albumin MW 69,000. Source: abstract and search excerpt only.
- calcengines.com free T worked example (calcengines.html): total T 15 nmol/L, SHBG 30 nmol/L, albumin 4.3 g/dL gives N 23.43, b 38.43 and FT 3.256e-10 mol/L = 325.6 pmol/L. This is also the page's default example.
- alphahealthfinder.com / aresmensclinic.com example, used only to check the quadratic. Their albumin MW is about 66,430: 500 ng/dL, SHBG 30, albumin 4.3 g/dL gives N 24.30, FT 10.8 ng/dL (108 pg/mL), 2.17 percent, BAT 264 ng/dL.
- Not used: dialedin calculator (dialedin.html). Its example (600 ng/dL, SHBG 45, albumin 4.3 g/dL gives 104.7 pg/mL, 1.75 percent, BAT 254.3, 363.1 pmol/L) does not reproduce with the published ISSAM/Vermeulen constants (we get 106.6 pg/mL, 369.6 pmol/L). They likely use different constants, so it was left out.

## Reference points shown on the page
- Endocrine Society 2018: Bhasin S et al. JCEM 2018;103(5):1715-44, doi 10.1210/jc.2018-00229. Harmonized total T range 264-916 ng/dL (9.2-31.8 nmol/L), from healthy non-obese men aged 19-39 (2.5th-97.5th percentile, CDC-standardized). A harmonized free T range has not been established.
- AUA 2018: Mulhall JP et al. Testosterone deficiency guideline (auanet.org). Low T cut-off: total T under 300 ng/dL (page: about 10.4 nmol/L = 300/28.84).
- CUA 2021: Grober ED et al. Can Urol Assoc J 2021;15(5):E234-43, doi 10.5489/cuaj.7252. Total T under 10 nmol/L is a reasonable threshold. Calculated free or bioavailable T can resolve equivocal results. Units are nmol/L.
- EMAS: Wu FC et al. NEJM 2010;363(2):123-35, doi 10.1056/NEJMoa0911101. Late-onset hypogonadism = 3 sexual symptoms plus total T under 11 nmol/L (320 ng/dL) and free T under 220 pmol/L (64 pg/mL). Free T by the Vermeulen formula.
- Alberta Precision Laboratories test directory, Testosterone Total (apl_testosterone.html): men 18 and over 8.0-35.0 nmol/L. Provincially standardized per the APL bulletin 2021 (apl_bulletin_2021.pdf).
- LifeLabs Burnaby Reference Laboratory reference intervals, Mar 15 2024 (lifelabs_brl_ranges.pdf, https://lifelabs.azureedge.net/lifelabs-wp-cdn/2018/10/brl_ranges.pdf):
  - testosterone, males over 18: 8.4-28.8 nmol/L
  - calculated free testosterone, males: 115-577 pmol/L
  - bioavailable T, males: 2.7-13.5 nmol/L (kept in research, not shown on the page)
- Not used: the LifeLabs Ontario guidebook 2026 free T figure "179-475" (lifelabs_guidebook_2026.txt). Its units are not printed in the text.

## Why Canada uses nmol/L and the USA ng/dL
- McQueen MJ. Conversion to SI units. The Canadian experience. JAMA 1986;256(21):3001-2. PMID 3773219, doi 10.1001/jama.256.21.3001.
  The quote "IN 1983, seven Canadian provinces (Nova Scotia, New Brunswick, Prince Edward Island, Ontario, Manitoba, Saskatchewan, and Alberta) converted to the use of SI units in health care" comes from the search-result excerpt of the article's first lines. Full text is blocked; the PubMed record confirms the citation.
- Huth EJ. The American shift to medical SI units. Ann Intern Med 1987;106(1):149-50. PMID 3789560, doi 10.7326/0003-4819-106-1-149. Quote: "most of the medical community in the United States has stood by while the rest of the medical world, including our close neighbor Canada, moved ... to SI".
- US FDA (CDER/CBER), position on SI units for lab tests, Oct 25 2013 (fda_si_units.pdf, https://www.fda.gov/media/161520/download): "majority of U.S. healthcare providers are trained using U.S. conventional units ... In the absence of a holistic transition within the U.S. healthcare community to SI units". The page paraphrases this as "conventional units as the ones most US care teams are trained in".
- IFCC protocol note "Canada converted in 1982" was seen in search results. It is not cited, because the page says "early 1980s".
