# Site Files

This directory contains homepage source files, documentation, and prepared SEO assets for the Odin Lab Calgary website.

## Homepage Files (`site/homepage/`)

- **`home.html`** — The currently published homepage (pasted into the HighLevel Home page 'Main Content' custom code element)
- **`home.template.html`** — Editable template for the homepage; edit this file, then run `build.py` to regenerate `home.html`
- **`build.py`** — Build script that processes `home.template.html` into `home.html`
- **`home.v1.html`** and **`home.template.v1.html`** — Previous versions of the homepage (archived for reference)

## SEO Files (`site/homepage/`)

- **`robots.txt`** — Robots exclusion file (currently live in HighLevel)
- **`sitemap.xml`** — XML sitemap (prepared, not yet published)
- **`llms.txt`** — LLM-friendly site description (prepared, not yet published)

## Documentation (`site/docs/`)

- Audit reports and site change logs

## Snapshots (`site/homepage/`)

- **`owen-lowt.live-snapshot.html`** — Read-only snapshot of a page that lives only in HighLevel (not editable from this repo)

## Notes

Additional implementation notes and checklists are in `site/homepage/NOTES.md` and `site/homepage/motion-checklist.md`.
