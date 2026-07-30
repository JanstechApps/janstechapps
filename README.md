# Janstech Apps Website

This repository contains the static Janstech Apps website served from the repository root by GitHub Pages. The custom domain is configured with `CNAME`, so production pages are available under `https://janstechapps.com`.

## Structure

- `index.html` - Janstech Apps landing page.
- `home.css` - Landing page stylesheet and design tokens (used only by `index.html`).
- `style.css` - Stylesheet for the app pages under `apps/` (legal pages use their own local `style.css`).
- `assets/` - Shared app images and favicon files.
- `apps/kauppalista/` - Shopping List & Notes public app landing page.
- `apps/waveiq/` - WaveIQ Radio public app landing page.
- `apps/gainsai/` - GainsAI public app landing page.
- `assets/gainsai-config.js` - Central verified regional GainsAI Pro-price configuration.
- `docs/apps/gainsai_app_profile.md` - GainsAI public product profile, source audit, and website release notes.
- `legal/kauppalista/` - Shopping List & Notes privacy, support, terms, and delete-data pages.
- `legal/waveiq/` - WaveIQ Radio privacy, support, terms, and delete-data pages.
- `legal/gainsai/` - GainsAI privacy, support, terms, and delete-data pages.
- `legal/surekeep/` - SureKeep privacy, support, terms, and delete-data pages.
- `CNAME` - GitHub Pages custom domain configuration for `janstechapps.com`.
- `sitemap.xml` - Generated sitemap of every indexable page, submitted to Google Search Console.
- `robots.txt` - Crawler rules and the `Sitemap:` reference.
- `.nojekyll` - Publishes the repository verbatim instead of running it through Jekyll.
- `tools/validate_site.py` - Sitemap, robots.txt and internal-link validator/generator.
- `.github/workflows/validate-site.yml` - Runs the validator on push and pull request.

## Production URLs

- https://janstechapps.com/
- https://janstechapps.com/apps/kauppalista/
- https://janstechapps.com/apps/waveiq/
- https://janstechapps.com/apps/gainsai/

### Shopping List & Notes

- https://janstechapps.com/legal/kauppalista/
- https://janstechapps.com/legal/kauppalista/support.html
- https://janstechapps.com/legal/kauppalista/terms.html
- https://janstechapps.com/legal/kauppalista/delete-data.html

### WaveIQ Radio

- https://janstechapps.com/legal/waveiq/
- https://janstechapps.com/legal/waveiq/support.html
- https://janstechapps.com/legal/waveiq/terms.html
- https://janstechapps.com/legal/waveiq/delete-data.html

### GainsAI

- https://janstechapps.com/apps/gainsai/
- https://janstechapps.com/legal/gainsai/
- https://janstechapps.com/legal/gainsai/support.html
- https://janstechapps.com/legal/gainsai/terms.html
- https://janstechapps.com/legal/gainsai/delete-data.html

### SureKeep

- https://janstechapps.com/legal/surekeep/
- https://janstechapps.com/legal/surekeep/support.html
- https://janstechapps.com/legal/surekeep/terms.html
- https://janstechapps.com/legal/surekeep/delete-data.html

## Deployment

GitHub Pages serves this static site directly from the repository root ("Deploy from a branch", `main` / `/ (root)`). There is no build step: the repository root *is* the publish root, so every committed file is published at the matching path. `.nojekyll` keeps GitHub Pages from running the content through Jekyll, which guarantees files such as `sitemap.xml` and `robots.txt` are published exactly as committed.

Keep public page links root-relative or absolute to `https://janstechapps.com` so pages work from their final production URLs.

## Landing page

`index.html` loads `home.css` only. The app pages under `apps/` load the root
`style.css`, and each legal folder has its own local `style.css`, so landing page
styling can change without touching any other page.

### Structure

`header` (brand, Apps link, EN/FI switch) → `main` with the hero, the `#apps`
card grid and the `#why` benefit grid plus the Janstech Apps intro → `footer`
with four link groups and a second EN/FI switch. There is exactly one `h1`
(the hero title).

### Responsive behaviour

The page is mobile first: the base rules are the small-screen layout and every
media query is `min-width`. A single `.shell` wrapper centres content at
`--shell-max` (1200px) with a `--gutter` that steps 18px → 28px (600px) → 40px
(1024px), so content stays centred on very wide screens without stretching.

| Breakpoint | What changes |
| --- | --- |
| base | one column everywhere, full-width buttons, hero visual hidden |
| 520px | hero and card buttons go side by side, benefit and footer grids to 2 columns |
| 720px | app cards to 2 columns |
| 900px | footer to 4 columns |
| 1024px | hero to 2 columns and the app-icon panel appears, benefits to 4 columns |
| 1120px | app cards to 3 columns |

### Design tokens

`home.css` starts with a `:root` block holding backgrounds and surfaces, borders,
text colours, accents, radii, shadows, a spacing scale (`--s-1` … `--s-8`),
layout values (`--shell-max`, `--gutter`, `--section-gap`, `--measure`) and
transition durations. Change the look from these tokens rather than from
individual rules. Per-app accent colours are set on `.app-card--shopping`,
`.app-card--waveiq` and `.app-card--gainsai` as `--app-accent`, `--app-accent-2`
and `--app-glow`, which drive the card top border, bullets, icon glow and
primary button.

### Landing page background

The landing page background is built only from CSS gradients in `home.css`: no
images, no filters and no animation. It has three parts:

- the `body` background: a vertical ramp through `--bg-deep`, `--bg` and
  `--bg-mid`, plus the `--ambient-cyan`, `--ambient-mint` and `--ambient-violet`
  washes that keep the hero area the liveliest part of the page
- `body::before`: a viewport-fixed sheen (`--ambient-top`, `--ambient-bottom`)
  and the `--grid-line` dot grid
- `--surface-veil`, the last background layer on cards and panels, which keeps
  translucent surfaces readable wherever a wash falls behind them

Tune the background from these tokens rather than from individual rules, and
keep it static — the page must stay motion-free by default.

These background tokens are landing-page only and are deliberately **not**
mirrored into `style.css`, which keeps its own flatter `--bg` / `--bg-2` pair
for the app pages. The mirroring rule in AGENTS.md applies to the shared visual
system (accents, radii, spacing, text colours), not to this background stack.

`home.css` also contains `[hidden]{display:none !important}`. Keep it: `.btn` is
`display:inline-flex`, which would otherwise override the browser's `[hidden]`
rule and reveal elements a page keeps hidden until it has verified data.

### Adding an app to the landing page

1. Add an `article.app-card.app-card--<app>` to the `.app-grid` with the app
   icon, an `h3` title linking to the app page, a one-line promise, up to four
   short feature bullets, the `Explore the app` and Google Play buttons, and the
   `.app-card__legal` link row.
2. Add an `.app-card--<app>` accent block to `home.css`.
3. Add the app to the hero `.icon-stack` and to the footer link groups.
4. Add every new visible string to both `dict.en` and `dict.fi` (see below).

### FI/EN texts

Every visible string carries a `data-i18n="key"` attribute and must exist in both
`dict.en` and `dict.fi` in the inline script at the bottom of `index.html`.
`setLang()` writes `textContent`, sets `<html lang>`, and syncs `aria-pressed` on
both EN/FI switches. The stored choice lives in `localStorage` under
`janstech_apps_lang`, and the default is English.

### Screenshots

No screenshots are used on the landing page yet. When real ones exist, the
natural places are a strip directly under the hero (or replacing the
`.hero__visual` icon panel on wide screens), and one image per app card between
the promise line and the feature list. Do not add empty placeholders in the
meantime.

## App pages

The three app pages under `apps/` (`gainsai/`, `kauppalista/`, `waveiq/`) share
one structure and one stylesheet, `style.css`. Each page is a single HTML file
with its own inline EN/FI dictionary. There is no build step and no framework.

### Shared structure

`header.site-header` (brand link, app nav with `aria-current="page"`, EN/FI
switch) → `main#main` → `footer.site-footer` (app blurb, support/privacy links,
apps, second EN/FI switch, copyright). There is exactly one `h1`: the app name
in the hero. Section titles are `h2`, card titles are `h3`.

| Block | Markup | Used by |
| --- | --- | --- |
| Hero | `section.hero > .shell.hero__inner` with `.hero__copy` (eyebrow, `h1`, optional `.hero__kicker`, lead, `.hero__actions`, `.quiet-links`) and `.hero__visual` (`.app-mark` icon + `.hero__panel` three summary rows) | all |
| Promo image | `figure.media-band > .shell > .media-band__frame` | GainsAI |
| Section head | `section.section > .shell > .section__head` (`.section__eyebrow` + `h2.section__title` + `p.section__intro`) | all |
| Feature cards | `.card-grid.card-grid--2` + `article.card` (`h3.card__title`, `p.card__text`) | all |
| Steps | `ol.steps > li.step` (`.step__num`, `h3.step__title`, `p.step__text`) | GainsAI |
| Screenshot gallery | `.gallery[tabindex="0"][role="group"] > figure.gallery__item` | GainsAI |
| Plans | `.panel > .plan-grid > article.plan-card` | GainsAI |
| FAQ | `.faq > details > summary + p` | GainsAI |
| Link row | `.link-row > a.btn` | all |
| Closing CTA | `section.cta-band > .shell.cta-band__inner` | all |

### Widths and breakpoints

The pages are mobile first: base rules are the small-screen layout and every
media query is `min-width`. `.shell` centres content at `--shell-max` (1200px)
with a `--gutter` that steps 18px → 28px (600px) → 40px (1024px), so content
stays centred on very wide screens without stretching. Body copy is additionally
capped: `--measure` (64ch) for section heads, `--prose` (68ch) for intros and
fine print, 56–66ch inside cards, so text lines never run the full 1200px.

| Breakpoint | What changes |
| --- | --- |
| base | one column everywhere, full-width hero/CTA buttons, header nav on its own row |
| 480px | hero and CTA buttons go side by side |
| 600px | cards, steps, plans and footer to 2 columns; "Language" label appears; hero icon moves beside the summary panel; gallery screenshots grow to 520px tall |
| 900px | header on one row, footer to 4 columns, CTA text and actions side by side |
| 1024px | hero to 2 columns, hero visual stacks again, steps to 4 columns, `.card-grid--3/--4` to 3/4 columns |

### Design tokens and per-app accents

`style.css` starts with a `:root` block holding backgrounds and surfaces,
borders, text colours, accents, radii, shadows, a spacing scale (`--s-1` …
`--s-8`), layout values (`--shell-max`, `--gutter`, `--section-gap`, `--measure`,
`--prose`) and transition durations. It intentionally mirrors the token block in
`home.css`: the two stylesheets stay independent (see AGENTS.md "Stylesheet
ownership rule") while sharing one visual system. `home.css` is the reference
for shared values — change it there first, then mirror.

Each page sets an app class on `<body>` that overrides `--accent`, `--accent-2`
and `--glow`. The values match that app's card on the landing page, so an app
keeps the same colour identity across the site:

| App | `body` class | `--accent` / `--accent-2` |
| --- | --- | --- |
| GainsAI | `app-page app--gainsai` | `#a786ff` / `#55c6ff` |
| Shopping List & Notes | `app-page app--kauppalista` | `#5fe3bf` / `#79c8ff` |
| WaveIQ Radio | `app-page app--waveiq` | `#ff9a86` / `#f56ca6` |

The accent drives the hero kicker, the section eyebrow rule, primary buttons,
bullet dots, step numbers, the hero panel edge, the featured plan card, the CTA
band top border, the background glow and the focus ring. `--focus-ring` is
declared on `.app-page` rather than `:root`, because a `var()` inside a custom
property resolves against the element that declares it.

`style.css` contains `[hidden]{display:none !important}`. Keep it: `.btn` is
`display:inline-flex`, which would otherwise override the browser's `[hidden]`
rule and reveal elements a page keeps hidden until it has verified data, such as
the GainsAI Pro price summary.

### Google Play CTA logic

Kauppalista, WaveIQ Radio and GainsAI all link straight to their published Play
listings from the hero, the closing CTA and the footer, and from their card on
the landing page. The URL is a plain anchor `href` in the markup and is also the
`downloadUrl` of each app page's `SoftwareApplication` JSON-LD block.

The GainsAI Pro price summary stays hidden until `proPricing` is filled in in
`assets/gainsai-config.js`. Do not add a guessed store URL, a disabled button,
or a placeholder that renders as a broken action.

### Screenshot gallery

`.gallery` is a horizontal scroll-snap strip. It is `tabindex="0"` with
`role="group"` and a translated `aria-label`, so it can be scrolled with the
keyboard as well as by touch. Every `figure.gallery__item` carries
`data-screenshot-lang="en|fi"`, and CSS shows only the items matching
`html[lang]`, so the visitor sees screenshots in their own language. Images keep
their real `width`/`height` attributes and are sized by height
(`--shot-h`: 400–520px), so each screenshot keeps its own aspect ratio, nothing
is cropped and nothing is scaled past its natural size. All gallery images use
`loading="lazy"`; the hero icon and the GainsAI promo image do not, because they
are in the first viewport.

### Adding a new app page

1. Copy `apps/waveiq/index.html` to `apps/<app>/index.html` (it is the smallest
   page: hero, features, trust cards, legal links, closing CTA, footer).
2. Update the head block: description, canonical, Open Graph, Twitter Card,
   `SoftwareApplication` JSON-LD, title.
3. Set `<body class="app-page app--<app>">` and add an `.app--<app>` accent block
   to `style.css`.
4. Point the nav, legal, footer and Play links at the new app's pages.
5. Translate every visible string: each carries `data-i18n="key"` and must exist
   in both `dict.en` and `dict.fi`. Any `aria-label` that needs translating uses
   `data-i18n-label="key"`.
6. Add the app to `index.html` (landing page card, hero icon stack, footer) and
   to the README URL list.
7. Regenerate the sitemap and run the validator.

### FI/EN texts

`setLang()` writes `textContent`, sets `<html lang>`, updates `document.title`
and the meta description where the page defines `meta_title`/`meta_description`,
applies `data-i18n-label` aria-labels, and syncs `aria-pressed` on both EN/FI
switches. The stored choice lives in `localStorage` under `janstech_apps_lang`
and the default is English. A small script in `<head>` applies the stored
language to `<html lang>` before first paint, so the language-filtered
screenshots and the `lang` attribute are correct from the first frame.

## Sitemap and robots.txt

`sitemap.xml` lists all 20 indexable pages: the landing page, the three app pages and the four legal pages of each app. It is generated from the pages on disk, so it never lists a page that does not exist and never misses one that does. Each `<lastmod>` is the file's last git commit date; no `priority` or `changefreq` values are published.

Regenerate it after adding, removing, renaming or editing a public page:

~~~bash
python tools/validate_site.py --write
~~~

Then commit the updated `sitemap.xml` together with the page change.

## Validation

~~~bash
python tools/validate_site.py
~~~

The validator fails the build if any of the following is true, and the same command runs in CI via `.github/workflows/validate-site.yml`:

- `sitemap.xml` or `robots.txt` is missing from the publish root
- `sitemap.xml` is not well-formed UTF-8 XML in the sitemaps.org 0.9 namespace
- a sitemap URL is not an absolute `https://janstechapps.com` URL, or contains a fragment, query string or duplicate
- a sitemap URL does not resolve to a real page, or its path casing does not match the file on disk
- an indexable page on disk is missing from the sitemap
- a `<lastmod>` value disagrees with the file's git commit date
- `robots.txt` blocks an indexable page or is missing the `Sitemap:` line
- an internal link or asset reference in any page points at a file that does not exist

To also check the pages in a browser, serve the publish root locally:

~~~bash
python -m http.server 8000
~~~

Then check both languages of every app page at 320, 360, 390, 412, 768, 1024,
1366 and 1920px. What to look for: no horizontal scrolling, exactly one `h1`,
the primary action visible without a long scroll, touch targets at least 44px
tall, visible focus rings when tabbing, readable screenshots, and no visible
`href="#"` link.

## GainsAI Pro price configuration

The GainsAI app page reads the Pro price summary from
`assets/gainsai-config.js`. Regional prices stay empty until they are verified
from the live Google Play offer; the summary stays hidden until then, which
avoids publishing an unverified price. The Google Play listing URL itself is no
longer configured here — like the other apps, GainsAI links to
`https://play.google.com/store/apps/details?id=com.janstech.gainsai` directly
from the markup.
