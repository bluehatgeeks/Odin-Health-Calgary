import json, html, re

SITE = "https://odinhealthlab.ca"
ASSESS = SITE + "/owen-lowt"
OG_IMG = "https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/og-home.png"
LOGO = "https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/zJaxLUStVkljpkn9qddd/media/69feb24f-b3d0-45e6-b747-20dc1d2eb84d.svg+xml"
FOUNDER_IMG = "https://assets.cdn.filesafe.space/Q6uTvwNHOg3F0JyLXiUV/media/69a742d5f183822a40a28166.png"

# 2026-10-27 brand1027: lead with the GBP brand "Odin Health Lab" (brand query 'odin' pos 3.9, 0 clicks)
TITLE = "Odin Health Lab: Low Testosterone & Men's Health Telehealth"
DESC = ("Odin Health Lab: telehealth for men in Canada and the USA with low testosterone (andropause) "
        "symptoms: fatigue, low drive, poor sleep. Free assessment.")
assert len(TITLE) <= 60 and len(DESC) <= 155, (len(TITLE), len(DESC))

FAQ = [
 ("What is andropause, and is it the same as low testosterone?",
  "Andropause is the everyday word for the drop in energy, drive and mood that some men notice as testosterone declines with age. The clinical name is late-onset hypogonadism, or low testosterone. It is not the same for every man, and not every man who feels this way has low testosterone."),
 ("How do I know if my symptoms are low testosterone?",
  "Fatigue, low drive, poor sleep and low mood overlap with stress, sleep problems, thyroid issues and more, so the clearest answer comes from blood tests together with a full history. Our free assessment shows which pattern your symptoms resemble and where to look first, and your first call covers which tests are worth asking for."),
 ("My labs came back \u201cnormal.\u201d Can low testosterone still be the problem?",
  "It can be worth a second look. Many standard panels report total testosterone only, while free testosterone, the portion your body can actually use, is a separate measurement. A number inside the reference range doesn't always settle the question. It helps to ask which test was run, and we can walk you through it on a call."),
 ("Who will I speak with, and how do you work with my doctor?",
  "You'll speak privately, by video or phone, with a clinician from the Odin Health Lab team. We work alongside your family doctor: we can share your plan with them, help you prepare questions for appointments and bring your results to the conversation."),
 ("What do you actually do about low testosterone?",
  "We look for the reasons testosterone may be low, then build a plan around your pattern: sleep, stress load, training, nutrition and targeted support, adjusted as we learn what is working, with regular check-ins."),
 ("Where do you work with men, and is it fully online?",
  "Odin Health Lab is telehealth only and serves men across Canada and the USA. Everything happens by secure video or phone, so there is no clinic visit."),
 ("How quickly will I notice a change?",
  "It depends on what is driving your symptoms, so we won't promise a timeline. Part of your first call is agreeing on what to track so you can see for yourself whether the plan is working."),
 ("What if I'm not a good fit?",
  "We work that out on your first call. You leave the call knowing the best next step for you."),
 ("Is my information private?",
  'Your assessment answers and calls are kept confidential. You can read exactly how we collect and protect your information in our <a href="%s/privacy">Privacy Policy</a>.' % SITE),
]

# ---------------- JSON-LD ----------------
ld = {
 "@context": "https://schema.org",
 "@graph": [
  {
   "@type": "Organization",
   "@id": SITE + "/#organization",
   "name": "Odin Health Lab",
   "alternateName": "Odin Labs",
   "url": SITE + "/",
   "sameAs": ["https://x.com/odinhealthlab", "https://www.linkedin.com/company/odin-health-lab/"],
   "logo": LOGO,
   "description": "Telehealth for men in Canada and the USA with andropause and low testosterone symptoms.",
   "areaServed": [{"@type": "Country", "name": "Canada"}, {"@type": "Country", "name": "United States"}],
   "contactPoint": [{
     "@type": "ContactPoint", "contactType": "customer support",
     "telephone": "+1-587-324-8710", "email": "office@odinhealthcoaching.com",
     "areaServed": ["CA", "US"], "availableLanguage": "English"}],
   "founder": {"@type": "Person", "name": "Alexander Tretjakov"}
  },
  {
   "@type": "WebSite",
   "@id": SITE + "/#website",
   "url": SITE + "/",
   "name": "Odin Health Lab",
   "description": DESC,
   "inLanguage": "en",
   "publisher": {"@id": SITE + "/#organization"}
  },
  {
   "@type": "WebPage",
   "@id": SITE + "/#webpage",
   "url": SITE + "/",
   "name": TITLE,
   "description": DESC,
   "isPartOf": {"@id": SITE + "/#website"},
   "about": {"@id": SITE + "/#organization"},
   "inLanguage": "en"
  },
  {
   "@type": "FAQPage",
   "@id": SITE + "/#faq",
   "mainEntity": [
     {"@type": "Question", "name": q,
      "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]
  }
 ]
}
ld_json = json.dumps(ld, ensure_ascii=False, indent=2).replace("</", "<\\/")

faq_html = "\n".join(
 '<details class="faq-item">\n<summary><span class="faq-question">%s</span></summary>\n<p class="faq-answer">%s</p>\n</details>' % (html.escape(q, quote=False), a)
 for q, a in FAQ)

tpl = open('/workspace/homepage/home.template.html', encoding='utf-8').read()
out = (tpl.replace('{{TITLE}}', html.escape(TITLE, quote=False))
          .replace('{{DESC}}', html.escape(DESC))
          .replace('{{SITE}}', SITE).replace('{{ASSESS}}', ASSESS)
          .replace('{{OG_IMG}}', OG_IMG).replace('{{FOUNDER_IMG}}', FOUNDER_IMG)
          .replace('{{JSONLD}}', ld_json).replace('{{FAQ}}', faq_html))
assert '{{' not in out
open('/workspace/homepage/home.html', 'w', encoding='utf-8').write(out)
print(len(out), 'bytes')
