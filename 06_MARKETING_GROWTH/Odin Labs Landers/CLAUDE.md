# Odin Lab Landers — Claude Instructions

## Design Requirements

**Before creating any new design element, component, section, or style — read `design.md`.**

`design.md` is the single source of truth for:
- Color palette and CSS variable tokens
- Typography scale and font families
- Spacing and container conventions
- All component patterns (buttons, cards, nav, modals, surveys, grids, etc.)
- Accessibility requirements
- External CDN and service URLs
- File structure conventions

### Enforcement Rules

- Do not hardcode color hex values. Use `var(--lime-green)`, `var(--dark-green)`, `var(--white)`, etc.
- Do not introduce new brand colors or font families not already defined in `design.md`.
- Do not duplicate nav or footer inline. Always use the shared component loader pattern.
- All booking CTAs must carry class `.booking-trigger`.
- New multi-column layouts must collapse at `≤768px`.
- Increment CSS version query strings (`?v=N`) when updating CDN-hosted stylesheets.
- After adding or modifying any design element, update `design.md` if it introduces a new pattern.

## Project Context

- Calgary-based functional health coaching practice
- Two main page types: main lander (`odinlabcalgary.html`) and therapy-specific landers (`odintherapiestemplate.html`)
- Shared styles in `odin-shared.css`; page-specific styles in separate CSS files
- Nav and footer loaded dynamically from GitHub raw content with `cache: 'no-store'`
