# Odin Lab Site Files

This directory contains the homepage files and documentation for the Odin Lab website deployed via GHL (GoHighLevel).

## Directory Structure

```
site/
├── homepage/
│   ├── home.html               # Current live homepage (per-section motion graphics)
│   ├── home.template.html      # Build template for current version
│   ├── home.v2.html            # Previous version backup (animated-motion)
│   ├── home.template.v2.html   # Build template for v2 backup
│   ├── build.py                # Python builder for generating HTML from templates
│   ├── NOTES.md                # Implementation notes and TODO items
│   ├── motion-checklist.md     # Motion design checklist
│   ├── graphics-per-section.md # Graphics implementation guide
│   └── _gen/                   # Generator utilities
│       ├── gen_graphics.py     # Graphics generation script
│       └── motion2.css         # Additional motion styles
└── docs/
    └── odin-site-log.md        # Site change log and deployment history
```

## Homepage Versions

### Current: Per-Section Motion Graphics (home.html)
- Published: 2026-10-15 12:13 MDT
- Features: Per-section scroll-reveal motion graphics
- Lines: 1190
- Template: home.template.html

### v2 Backup: Animated Motion (home.v2.html)
- Published: 2026-10-15 11:31 MDT (replaced by current)
- Features: Animated-motion homepage
- Lines: 893
- Template: home.template.v2.html

## Build System

The `build.py` script generates final HTML files from templates:
- Injects shared navigation and footer components
- Manages version increments for CSS/JS cache-busting
- Handles template variable substitution

The `_gen/` directory contains utilities for generating graphics and additional styles.

## Deployment

Homepage files are deployed to GHL and served at:
- `/` (root)
- `/yyc` (Calgary-specific URL)

Shared assets (CSS, nav, footer) are hosted via jsDelivr CDN from the master branch and remain unchanged by homepage updates.

## Notes

- Mixpanel tracking is added at the page level for CTA clicks only; site-level Mixpanel init and Page View events are managed in GHL and not included in these files.
- Facebook Pixel is injected site-wide and not duplicated in homepage files.
- The OG image `og-home.png` should be committed to the repo as `img/og-home.png` and served via jsDelivr.

See `homepage/NOTES.md` and `docs/odin-site-log.md` for detailed implementation notes and change history.
