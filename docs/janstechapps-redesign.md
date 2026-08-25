# JanstechApps Product Editorial — design direction

The visual direction of the JanstechApps website, the audit it came out of, and
the rules for keeping it consistent when pages are added or edited.

Applies to:

| Page type | Stylesheet |
| --- | --- |
| `index.html` | `/home.css` |
| `apps/*/index.html` | `/style.css` |
| `legal/*/*.html` | `legal/<app>/style.css` (palette only, see §9) |

---

## 1. Brand name

The brand is written **JanstechApps** — one word, exactly this casing.

Never `Janstech Apps`. This covers visible UI text, headings, navigation,
footers, `<title>` and meta tags, Open Graph, JSON-LD, documentation,
`README.md`, `AGENTS.md`, this file, CSS comments, HTML comments and commit
messages.

Not affected, because changing them would break something: the domain
`janstechapps.com`, file paths, technical identifiers (`janstech_apps_lang`,
`com.janstech.*`, `janstech.apps@gmail.com`), existing URLs, and historical or
external strings.

---

## 2. What the audit found

The site before this redesign was technically sound — responsive, accessible,
mobile first, valid metadata — but its visual identity read as a generated
AI/SaaS landing page. The specific causes:

| Problem | Where |
| --- | --- |
| Navy background with cyan / mint / violet ambient washes | `home.css` body background, `style.css` body glow |
| Fixed dot-grid overlay across the viewport | `home.css` `body::before` |
| Translucent surfaces over a veil (glassmorphism) | `--surface-veil`, `.icon-stack`, `.panel`, `.cta-band` |
| Everything in a rounded card: 22–28px radii, gradients, drop shadows | `.app-card`, `.why-card`, `.card`, `.step`, `.plan-card`, `.about` |
| Symmetrical 2/3/4-column feature-card grids repeated on every page | `.app-grid`, `.why-grid`, `.card-grid`, `.steps` |
| Same section formula everywhere: eyebrow → heading → intro → card grid | all app pages |
| Per-app colour used as a glow and a gradient button, not as an identifier | `--app-glow`, `.btn--primary` gradients |
| Floating icon collage in the hero | `.icon-stack` |
| Pill buttons for navigation, language, legal links | `.site-nav__link`, `.lang-switch`, `.link-row > .btn` |
| Generic marketing copy ("Smart Android apps for real everyday needs") | landing hero, `why-*` cards |
| Four identical benefit cards standing in for real principles | `.why-grid` |
| Legal pages on a completely different violet/teal design | `legal/*/style.css` |

Worth keeping, and kept: the EN/FI dictionary pattern and `localStorage` key,
the language-filtered screenshot gallery, `[hidden]{display:none !important}`,
the `SoftwareApplication` / `Organization` JSON-LD, image `width`/`height`
attributes, the skip link and landmark structure, `tools/validate_site.py`, and
the stylesheet ownership split.

---

## 3. The direction

**Practical, not futuristic.** The work does concrete jobs: a shopping list, a
radio station you want to find again, a training session to log, a treatment
price a customer has to find on a phone. The visual language argues for
usefulness, not for the future.

**One portfolio, two kinds of entry.** Since August 2026 the brand covers
websites, Android applications, backend systems and AI features rather than
Android alone. Customer projects and the brand's own apps are presented with the
same `.app-row` component, so the widening changed the copy and added two
sections — it did not add a second visual identity.

**Editorial, not brochure.** Structure comes from typographic hierarchy,
hairline rules, whitespace, index numbers, categories and product metadata.
Controlled asymmetry, wide but readable measures, a different shape for each
kind of content.

**One brand, quiet app colours.** One copper accent for the whole site. An
app's own colour is an identifier — a number, a short rule, a nav underline —
never a surface, a glow or a card.

**Cards are the exception.** A bounded surface has to earn its place. On the
whole site there are exactly two: the GainsAI Free/Pro comparison and the
legal-page content columns, which were already built that way.

### How this differs from the personal portfolio

`https://janstech.github.io/` (the developer's personal portfolio) uses a
related but separate direction: a neutral graphite page with an amber accent
and an all-sans "workbench" voice, organised as a CV.

JanstechApps shares the general principles — restrained palette, strong type
hierarchy, open layout, no neon — and deliberately differs in:

- a **warm charcoal** page (`#121110`), not neutral graphite
- a **copper** accent (`#e07a4f`), not amber
- a **serif editorial voice** for the site's own headings, with sans reserved
  for product names and UI
- a **product-catalogue structure**: numbered app rows with icon, category and
  availability columns, rather than a CV timeline

Same hand, different product.

---

## 4. Colour

Tokens live in the `:root` block of `home.css`; `style.css` mirrors them (see
§8). Change `home.css` first, then mirror.

| Token | Value | Use |
| --- | --- | --- |
| `--page-bg` | `#121110` | the page; flat, no gradient, no image |
| `--page-bg-raised` | `#171614` | reserved for a raised band |
| `--surface` | `#1b1917` | the rare bounded surface |
| `--surface-subtle` | `#151412` | footer, icon frames, screenshot backing |
| `--text` | `#ece9e6` | body and headings — 15.4:1 on the page |
| `--text-muted` | `#b5aea6` | secondary prose — 8.5:1 |
| `--text-dim` | `#8f8880` | metadata and tertiary links — 5.3:1 |
| `--rule` | `#2b2825` | the standard hairline |
| `--rule-strong` | `#443e38` | button borders, section-closing rules |
| `--brand` | `#e07a4f` | one accent: primary buttons, links on hover, focus — 6.7:1 |
| `--brand-hover` | `#f0906a` | primary button hover |
| `--brand-soft` | `rgba(224,122,79,.14)` | active language button |
| `--on-brand` | `#1a0d06` | text on the copper fill — 6.8:1 |
| `--focus` | `#e07a4f` | focus ring, same on every page |

Per-app accents, used only as identifiers:

| App | Token | Value |
| --- | --- | --- |
| Shopping List & Notes | `--accent-kauppalista` | `#8fb894` sage |
| WaveIQ Radio | `--accent-waveiq` | `#8aa6c6` dusty blue |
| GainsAI | `--accent-gainsai` | `#c78d6a` terracotta |
| Työtori | `--accent-tyotori` | `#a79ac6` heather |

Customer projects take an accent from the same family, used in exactly the same
places:

| Project | Token | Value |
| --- | --- | --- |
| Tmi Piikula | `--accent-piikula` | `#c98ba0` dusty rose — 6.9:1, the customer's own crimson brought onto the charcoal page |

All of them clear 6.5:1 on the page background — Työtori's is 7.3:1. They are
picked to stay separable at the size they are actually used, which is why the
fourth app accent is a cool violet rather than another green, blue or warm tone. An app
page selects one with `body class="app-page app--<app>"`, which sets
`--app-accent`. On the landing page the same job is done by the `.a-<app>` and
`.a-<project>` utility classes. `--accent-piikula` is used only on the landing
page; it is mirrored into `style.css` to keep the two token blocks identical.

**Banned:** ambient washes, radial glows, multi-layer gradients, dot or line
grids, background images, translucent veils, coloured shadows, `backdrop-filter`.

---

## 5. Typography

Three voices, three jobs. No downloaded fonts.

| Token | Stack | Used for |
| --- | --- | --- |
| `--font-display` | `"Iowan Old Style", "Hoefler Text", Georgia, "Noto Serif", serif` | the site's own voice: the landing `h1` and every section `h2`, plus the app-page promise line |
| `--font-sans` | `system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif` | the product voice: app names, the app-page `h1`, all `h3`, body copy, buttons |
| `--font-mono` | `ui-monospace, "Cascadia Mono", "Segoe UI Mono", Menlo, Consolas, monospace` | metadata only: index numbers, `.label`, spec terms |

The rule to remember: **serif is the site talking, sans is the product.**

Scale (all `clamp()`, all in the token block):

| Token | Range | Used for |
| --- | --- | --- |
| `--fs-display` | 2.15 → 3.25rem | landing `h1`, app-page `h1` |
| `--fs-h2` | 1.5 → 2.05rem | section titles, closing title |
| `--fs-h3` | 1.14 → 1.32rem | feature, tenet, duo and plan titles |
| `--fs-lede` | 1.06 → 1.2rem | leads and section intros |
| `--fs-body` | 1.0625rem | body copy |
| `--fs-small` | .9375rem | list items, feature text, buttons |
| `--fs-meta` | .8125rem | spec values, quiet links, footer bottom |
| `--fs-label` | .75rem | mono uppercase labels |

Line lengths: `--measure` 64ch for section intros, `--prose` 68ch for fine
print and FAQ answers, 52–60ch inside rows. Body line-height 1.65, headings 1.2,
display 1.08.

Restraint rules: at most one uppercase mono label per section; one `h1` per
page; never the same heading pattern in two consecutive sections; no giant
one-word feature headings.

---

## 6. Spacing, layout and radii

- Spacing scale `--space-1` … `--space-9` (0.25rem → 6rem, 4px base).
- `--shell` 1240px, `--gutter` 20px → 32px (640px) → 48px (1100px).
- `--section-gap` `clamp(3rem, 2rem + 4.5vw, 5.25rem)`.
- Radii stay small: `--radius-sm` 4px (buttons, focus ring), `--radius-md` 8px
  (the two remaining bounded surfaces), `--radius-icon` 11px (app icon frames).

Breakpoints, all `min-width`:

| Width | What changes |
| --- | --- |
| base | one column; masthead nav on its own row; app rows stack |
| 560 / 620px | landing services and feature lists to two columns; footer to two columns; larger app icons and screenshots |
| 720px | masthead on one row; feature rows, principles, duo columns, steps and plans go two-column |
| 900px | split section heads (title left, intro right); closing CTA text and actions side by side |
| 1024px | hero and app hero to two columns with a hairline between; landing services to four columns; app rows to number/icon + body + availability; steps to four columns; footer to four columns; screenshots grow to 620px |

---

## 7. When a card is allowed

Use an open row, a list or a column — separated by a hairline and whitespace —
by default.

A bounded surface (border + background + radius) is allowed only when the
content is genuinely a discrete object that is compared against a sibling. In
practice that is the GainsAI Free/Pro pair and the Työtori Free/Työtori+ pair
(`.plan`), and nothing else on the landing or app pages.

Everything that used to be a card is now:

| Was | Is |
| --- | --- |
| `.app-card` grid | `.app-index` → `.app-row` open rows |
| `.why-card` × 4 | `.tenets` → numbered `.tenet` rows |
| `.card-grid--2` feature cards | `.feature-rows` → numbered `.feature` rows |
| `.card--wide` explainer pairs | `.duo` → two open columns with a top rule |
| `.step` cards | `.steps` → columns with an accent rule on top |
| `.panel` with a glow | plain section head + `.plans` |
| `.faq details` cards | hairline-separated `<details>` |
| `.cta-band` gradient panel | `.closing` with a single top rule |
| `.icon-stack` hero collage | `.hero__index` typographic list |
| a service-card grid (never built) | `.services` → `.service` columns with a rule on top |
| a project-card grid (never built) | `.app-row` reused in `#work` |
| `.media-band__frame` with shadow | 1px border, no shadow |

---

## 8. Stylesheet architecture

The ownership split from `AGENTS.md` is unchanged: `home.css` for the landing
page, `style.css` for the app pages, one local stylesheet per legal folder. No
new shared stylesheet was introduced — that would have meant re-pointing every
page for no functional gain.

`style.css` mirrors the `home.css` token block on purpose. `home.css` is the
reference: change a shared value there first, then mirror it.

Both files keep `[hidden]{display:none !important}` — `.btn` is `inline-flex`,
which would otherwise beat the user-agent `[hidden]` rule and reveal the GainsAI
Pro price summary before its prices are verified.

The per-app focus ring was dropped: `--focus` is the brand copper on every page,
so the focus indicator is the same everywhere. `.app--<app>` now overrides
`--app-accent` only.

---

## 9. Legal pages

The legal HTML, its content, its structure and its URLs are untouched. Only the
four local stylesheets were harmonised, and only their palette, radii and
surfaces:

- flat `#121110` page instead of violet/teal radial gradients
- `#171614` panels instead of translucent white over a blur
- copper links and active states instead of violet/teal
- `backdrop-filter: blur()` removed
- radii reduced to 6–8px, drop shadows removed
- nav and language buttons raised to 44px touch targets

No legal sentence, link, heading or date was changed.

---

## 10. Working on the site

### Adding an app

1. Add an `<li class="app-row a-<app>">` to `.app-index` in `index.html` with
   the index number, icon (`alt=""`, the name is adjacent), category, name
   linking to the app page, promise, 3–4 features, the `.spec` list, the
   "see what it does" button, the Play link and the four legal links.
2. Add the app to `.hero__index-list` with the same `.a-<app>` class.
3. Add `--accent-<app>` to the token block of `home.css`, mirror it into
   `style.css`, and add an `.app--<app>` rule there.
4. Add the footer links.
5. Copy `apps/waveiq/index.html` (the smallest page) to `apps/<app>/index.html`
   and update the head block: description, canonical, Open Graph, Twitter Card,
   `SoftwareApplication` JSON-LD, title.
6. Add every new visible string to both `dict.en` and `dict.fi`.
7. Update `README.md`, regenerate the sitemap, run the validator.

Työtori was added this way in August 2026 and is the worked example: index
number `04`, accent `#a79ac6`, `apps/tyotori/`, `legal/tyotori/`, and
`docs/apps/tyotori_app_profile.md` as the source of every factual claim on its
pages.

Copy that names a count has to move with the list. Adding Työtori changed
`hero_lede`, `hero_index_note` ("All four…"), `apps_h` ("Four published Android
apps") and the third principle, which now says out loud that Työtori needs an
account and a server. Check those four before shipping a fifth app.

### Adding a customer project

1. Add an `<li class="app-row a-<project>">` to the `.app-index` in `#work`:
   index number, `.app-row__glyph` monogram (or an icon the customer publishes),
   category, an `h3` name linking to the customer's own site with
   `target="_blank" rel="noopener noreferrer"`, a one-line promise, 3–4 lines of
   real implementation detail, the `.spec` list and one
   `.btn--primary.btn--out` link.
2. Add `--accent-<project>` to `home.css`, mirror it into `style.css`, and add
   the `.a-<project>` rule.
3. Add every new visible string to both `dict.en` and `dict.fi`.

Tmi Piikula (`piikula.fi`) was added this way in August 2026 and is the worked
example. Describe a project by what was actually built — for Piikula that is
WordPress on a custom Kadence child theme, custom treatment and pricing
templates, per-treatment detail pages, a Soluni partner shop integration,
privacy pages and the production setup. No invented client counts, no
exaggerated scope, and no internal infrastructure detail, credentials or hosting
specifics.

Copy that names a count still has to move with the list: `hero_index_note`
("Four apps on Google Play, and the first customer website below.") and
`apps_h` ("Four published Android apps") both name one.

### FI/EN content

Every visible string carries `data-i18n="key"` and must exist in **both**
`dict.en` and `dict.fi`. Translated `aria-label`s use `data-i18n-label`.
`setLang()` writes `textContent`, sets `<html lang>`, updates `document.title`
and the meta description, applies the aria-labels, and syncs `aria-pressed` on
both EN/FI switches. The choice is stored in `localStorage` under
`janstech_apps_lang`; the default is English. A small script in `<head>` applies
the stored language to `<html lang>` before first paint.

Write both languages as if a person wrote them. No word-for-word translation.
The brand name stays `JanstechApps` in both.

### Screenshot gallery

`.gallery` is a horizontal scroll-snap strip: `tabindex="0"`, `role="group"`,
translated `aria-label`. Each `figure.gallery__item` carries
`data-screenshot-lang="en|fi"` and CSS shows only the items matching
`html[lang]`. When an app has screenshots in only one interface language, as
Työtori does, the same files appear in both sets with `alt` text written in the
page language, and a `.fineprint` note under the strip states which interface
language is on screen. Do not pass a Finnish-only screenshot off as an English
one. Images keep their real `width`/`height` and are sized by height
(`--shot-h`: 400 → 520 → 620px), so each keeps its own aspect ratio, nothing is
cropped and nothing is scaled past its natural size. No per-image frame, no
shadow. Gallery images are `loading="lazy"`; hero icons and the GainsAI promo
image use `fetchpriority="high"` instead, because they are in the first
viewport.

Do not add empty screenshot placeholders for apps that have none.

### Google Play CTA logic

All three apps have published listings, so the store URL is a plain anchor in
the markup and the `downloadUrl` in each page's JSON-LD. Never add a guessed
URL, a disabled button, a "coming soon" label or anything that renders as a
broken action for an app whose listing is not public.

### GainsAI configuration

`assets/gainsai-config.js` holds the Pro price summary. While `monthly` or
`yearly` is `null`, `updatePriceSummary()` sets `hidden` on
`#gainsaiPriceSummary` and nothing is shown. Filling in verified prices reveals
the summary with no HTML change. This is what `[hidden]{display:none !important}`
protects.

### Sitemap

Generated, never hand-edited. `<lastmod>` comes from each file's git commit
date, so regenerate **after** committing a page change and amend, or commit the
sitemap separately:

~~~bash
python tools/validate_site.py --write
~~~

### Validation

~~~bash
python tools/validate_site.py           # sitemap, robots.txt, every internal link
python -m http.server 8000              # then check pages in a browser
~~~

Check both languages of the landing page and all three app pages at 320, 360,
390, 412, 600, 768, 1024, 1366 and 1920px. What to look for: no horizontal
scrolling, exactly one `h1`, the primary action visible without a long scroll,
touch targets at least 44px tall, visible focus rings when tabbing, readable
screenshots, no visible `href="#"`, and identical key sets in `dict.en` and
`dict.fi`.

### Publishing

GitHub Pages, "Deploy from a branch", `main` / `/ (root)`. No build step: the
repository root is the publish root, and `.nojekyll` keeps the files published
exactly as committed.
