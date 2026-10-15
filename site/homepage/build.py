import json, html, re

SITE = "https://odinhealthlab.ca"
ASSESS = SITE + "/owen-lowt"
OG_IMG = "https://cdn.jsdelivr.net/gh/bluehatgeeks/Odin-Health-Calgary@master/img/og-home.png"
LOGO = "https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/zJaxLUStVkljpkn9qddd/media/69feb24f-b3d0-45e6-b747-20dc1d2eb84d.svg+xml"
FOUNDER_IMG = "https://assets.cdn.filesafe.space/Q6uTvwNHOg3F0JyLXiUV/media/69a742d5f183822a40a28166.png"

TITLE = "Low Testosterone & Andropause Support for Men | Odin Health Labs"
DESC = ("Telehealth for men in Canada and the USA with low testosterone (andropause) symptoms: "
        "fatigue, low drive, belly fat, poor sleep. Start with a free assessment.")

FAQ = [
 ("What is andropause, and is it the same as low testosterone?",
  "Andropause is the everyday word for the drop in energy, drive and mood that some men notice as testosterone declines with age. Doctors usually call it late-onset hypogonadism or low testosterone. It is not the same for every man, and not every man who feels this way has low testosterone."),
 ("How do I know if my symptoms are low testosterone?",
  "You can't tell from symptoms alone. Fatigue, low drive, poor sleep and low mood overlap with stress, sleep problems, thyroid issues and more. Blood tests, a full history and a clinician's interpretation are what separate these. Our free assessment shows which pattern your symptoms resemble. It is a starting point, not a diagnosis."),
 ("My labs came back \u201cnormal.\u201d Can low testosterone still be the problem?",
  "It can be worth a second look. Many standard panels report total testosterone only, while free testosterone, the portion your body can actually use, is a separate measurement. A number inside the reference range doesn't always settle the question. It helps to ask which test was run, and we can walk you through it on a call."),
 ("Who will I speak with, and do you replace my doctor?",
  "You'll speak privately, by video or phone, with a clinician from the Odin Health Labs team. We work alongside your family doctor, not instead of them. If something needs medical testing or treatment, we'll tell you plainly."),
 ("What do you actually do about low testosterone?",
  "We look for the reasons testosterone may be low, then build a plan around your pattern: sleep, stress load, training, nutrition and targeted support, adjusted as we learn what is working. If your situation needs medical treatment, including hormone therapy, we'll say so and work alongside the physician who provides it."),
 ("Where do you work with men, and is it fully online?",
  "Odin Health Labs is telehealth only and serves men across Canada and the USA. Everything happens by secure video or phone, so there is no clinic visit."),
 ("How quickly will I notice a change?",
  "It depends on what is driving your symptoms, so we won't promise a timeline. Part of your first call is agreeing on what to track so you can see for yourself whether the plan is working."),
 ("What if I'm not a good fit?",
  "We work that out on your first call. If we can't help, we'll say so directly and point you to the right next step, which is sometimes seeing a physician."),
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
   "name": "Odin Health Labs",
   "alternateName": "Odin Labs",
   "url": SITE + "/",
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
   "name": "Odin Health Labs",
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
