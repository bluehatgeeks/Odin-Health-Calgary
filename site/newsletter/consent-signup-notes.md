# Consent email signup (CASL + CAN-SPAM) — GHL notes

**Status:** Notes only. Live GHL form creation is a follow-up **browser** step. Do not create or publish a form from this file alone.

## Goal

Collect email (and optional first name) for an Odin Health Labs list about andropause / low testosterone telehealth for men in Canada and the USA, with **explicit consent** suitable for CASL (Canada) and CAN-SPAM (USA).

## Recommended GHL form fields

1. **Email** (required)
2. **First name** (optional)
3. **Consent checkbox** (required to submit) — unchecked by default

### Suggested checkbox label (plain language)

> I agree to receive emails from Odin Health Labs about men’s low testosterone and andropause telehealth (Canada and USA), including tips, article updates, and occasional offers. I can unsubscribe anytime. Message frequency varies.

Optional secondary line under the checkbox (still not a long legal disclaimer block):

> By checking this box you confirm you want these emails. We use your email only for this list unless you book care with us separately.

## Where it should live on the site (non-Paid)

- **Preferred:** Homepage section (footer of the main content, or a short “Stay in the loop” block before the site footer) on `/` (and `/yyc` if that shares the same custom HTML).
- **Also fine:** Footer strip on other **non-Paid** pages that use our shared page system (answer pages, therapy rewrites, privacy) — added via page templates / `base_tail` later, **not** via the shared Paid nav.
- **Do not** put this signup into the shared nav/loader used by **[Paid]** pages (Booking Form Only, Quiz, Quiz Emma/Owen, VSL/Owen) unless Alex explicitly asks and the change is verified safe for ad funnels.

## GHL setup checklist (browser follow-up)

1. Create a Form (or Survey) in the Odin Health Lab Main Site / marketing location Alex uses.
2. Add Email + optional First name + required consent checkbox with the copy above.
3. On submit: add contact to a dedicated list/tag e.g. `newsletter-andropause-consent` and store consent timestamp / source URL if GHL supports custom fields.
4. Embed the form on the homepage (and optionally other non-Paid pages) via GHL form embed or a lightweight custom HTML block — **separate publish** from this tracking/newsletter draft package.
5. Confirmation: thank-you message on-page or double opt-in email if Alex wants stricter CASL practice for cold signups.
6. Unsubscribe: rely on GHL’s standard unsubscribe footer on every campaign; never remove it.

## Out of scope for this package

- Creating the live form in GHL
- Publishing homepage/footer embeds
- Sending any campaign
