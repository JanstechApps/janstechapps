# JanstechApps Website

This repository contains the static JanstechApps website served from the repository root by GitHub Pages. The custom domain is configured with `CNAME`, so production pages are available under `https://janstechapps.com`.

## Structure

- `index.html` - JanstechApps landing page.
- `home.css` - Landing page stylesheet and design tokens (used only by `index.html`).
- `style.css` - Stylesheet for the app pages under `apps/` (legal pages use their own local `style.css`).
- `assets/` - Shared app images and favicon files.
- `apps/kauppalista/` - Shopping List & Notes public app landing page.
- `apps/waveiq/` - WaveIQ Radio public app landing page.
- `apps/gainsai/` - GainsAI public app landing page.
- `apps/tyotori/` - Työtori public app landing page.
- `assets/gainsai-config.js` - Central verified regional GainsAI Pro-price configuration.
- `assets/tyotori/` - Työtori app screenshots used by the Työtori app page.
- `docs/janstechapps-redesign.md` - "JanstechApps Product Editorial" design direction: audit findings, colour, typography, spacing, breakpoints, per-app accents, and when a card is allowed.
- `docs/apps/gainsai_app_profile.md` - GainsAI public product profile, source audit, and website release notes.
- `docs/apps/tyotori_app_profile.md` - Työtori public product profile, verified feature and privacy facts, and the "do not claim" list.
- `legal/kauppalista/` - Shopping List & Notes privacy, support, terms, and delete-data pages.
- `legal/waveiq/` - WaveIQ Radio privacy, support, terms, and delete-data pages.
- `legal/gainsai/` - GainsAI privacy, support, terms, and delete-data pages.
- `legal/tyotori/` - Työtori privacy, support, terms, and delete-data pages.
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
- https://janstechapps.com/apps/tyotori/

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

### Työtori

- https://janstechapps.com/apps/tyotori/
- https://janstechapps.com/legal/tyotori/
- https://janstechapps.com/legal/tyotori/support.html
- https://janstechapps.com/legal/tyotori/terms.html
- https://janstechapps.com/legal/tyotori/delete-data.html

### SureKeep

- https://janstechapps.com/legal/surekeep/
- https://janstechapps.com/legal/surekeep/support.html
- https://janstechapps.com/legal/surekeep/terms.html
- https://janstechapps.com/legal/surekeep/delete-data.html

## Deployment

GitHub Pages serves this static site directly from the repository root ("Deploy from a branch", `main` / `/ (root)`). There is no build step: the repository root *is* the publish root, so every committed file is published at the matching path. `.nojekyll` keeps GitHub Pages from running the content through Jekyll, which guarantees files such as `sitemap.xml` and `robots.txt` are published exactly as committed.

Keep public page links root-relative or absolute to `https://janstechapps.com` so pages work from their final production URLs.

## Design direction

The whole site follows one documented direction, "JanstechApps Product
Editorial": a flat warm-charcoal page, hairlines and whitespace instead of
rounded cards, one copper brand accent with quiet per-app identifiers, and a
serif/sans/mono type system. Colour values, the type scale, spacing, breakpoints
and the rule for when a card is allowed all live in
[`docs/janstechapps-redesign.md`](docs/janstechapps-redesign.md). Read that
before changing any styling.

## Landing page

`index.html` loads `home.css` only. The app pages under `apps/` load the root
`style.css`, and each legal folder has its own local `style.css`, so landing page
styling can change without touching any other page.

### Structure

`header.masthead` (brand, three nav links, EN/FI switch) → `main` with the hero
(message plus a typographic app index), the `#apps` product index, the
`#principles` list and the `#developer` note → `footer` with four link groups
and a second EN/FI switch. There is exactly one `h1` (the hero title).

### Responsive behaviour

The page is mobile first: the base rules are the small-screen layout and every
media query is `min-width`. A single `.shell` wrapper centres content at
`--shell` (1240px) with a `--gutter` that steps 20px → 32px (640px) → 48px
(1100px), so content stays centred on very wide screens without stretching.

| Breakpoint | What changes |
| --- | --- |
| base | one column everywhere; masthead nav on its own row; app rows stack |
| 560px | app feature lists to 2 columns, footer to 2 columns |
| 720px | masthead on one row, principles to 3 columns, developer note to 2 |
| 900px | split section heads: title left, intro right |
| 1024px | hero to 2 columns with a hairline, app rows to number/icon + body + availability, footer to 4 columns |

### Design tokens

`home.css` starts with a `:root` block holding page surfaces, text colours,
hairlines, the copper brand accent, per-app accents, the three font stacks, a
`clamp()` type scale, a spacing scale (`--space-1` … `--space-9`), layout values
(`--shell`, `--gutter`, `--section-gap`, `--measure`, `--prose`) and small radii.
Change the look from these tokens rather than from individual rules.

The page background is a single flat colour: no gradients, no images, no dot
grid, no ambient washes and no animation. Depth comes from typography, hairlines
and whitespace.

Per-app accents are applied with the `.a-kauppalista`, `.a-waveiq`,
`.a-gainsai` and `.a-tyotori` utility classes, which set `--app-accent` for that
row only. The
accent drives the index number and the short rule in front of each feature — not
a background, a glow or a card.

`home.css` also contains `[hidden]{display:none !important}`. Keep it: `.btn` is
`display:inline-flex`, which would otherwise override the browser's `[hidden]`
rule and reveal elements a page keeps hidden until it has verified data.

### Adding an app to the landing page

1. Add an `li.app-row.a-<app>` to the `.app-index` list with the index number,
   the app icon (`alt=""`, the name is next to it), the category, an `h3` name
   linking to the app page, a one-line promise, 3–4 feature lines, the `.spec`
   list, the primary button, the Google Play link and the four legal links.
2. Add the app to `.hero__index-list` with the same `.a-<app>` class.
3. Add an `--accent-<app>` token and an `.a-<app>` rule to `home.css`.
4. Add the app to the footer link groups.
5. Add every new visible string to both `dict.en` and `dict.fi` (see below).

### FI/EN texts

Every visible string carries a `data-i18n="key"` attribute and must exist in both
`dict.en` and `dict.fi` in the inline script at the bottom of `index.html`.
`setLang()` writes `textContent`, sets `<html lang>`, and syncs `aria-pressed` on
both EN/FI switches. The stored choice lives in `localStorage` under
`janstech_apps_lang`, and the default is English.

### Screenshots

No screenshots are used on the landing page. When real ones exist, the natural
place is a strip directly under the hero. Do not add empty placeholders in the
meantime.

## App pages

The four app pages under `apps/` (`gainsai/`, `kauppalista/`, `tyotori/`,
`waveiq/`) share one structure and one stylesheet, `style.css`. Each page is a
single HTML file with its own inline EN/FI dictionary. There is no build step and
no framework.

### Shared structure

`header.masthead` (brand link, app nav with `aria-current="page"`, EN/FI switch)
→ `main#main` → `footer.site-footer` (app blurb, support/privacy links, apps,
second EN/FI switch, copyright). There is exactly one `h1`: the app name in the
hero. Section titles are `h2`, row and column titles are `h3`.

| Block | Markup | Used by |
| --- | --- | --- |
| App hero | `section.app-hero > .shell.app-hero__inner` with `.app-hero__copy` (context line, `.app-hero__mark` icon + `h1`, promise, lead, actions, quiet links) and `.app-hero__facts` (`dl.spec` + `.summary`) | all |
| Promo image | `figure.media-band > .shell > .media-band__frame` | GainsAI |
| Section head | `section.section > .shell > .section__head` (`p.label` + `h2.section__title` [+ `p.section__intro` with `--split`]) | all |
| Feature rows | `ol.feature-rows > li.feature` (`.feature__num`, `h3.feature__title`, `p.feature__text`) | all |
| Open two-column prose | `.duo > .duo__col` (`h3.duo__title`, `p.duo__text`, optional `ul.duo__list`) | all |
| Steps | `ol.steps > li.step` (`.step__num`, `h3.step__title`, `p.step__text`) | GainsAI, Työtori, WaveIQ (`--3`) |
| Screenshot gallery | `.gallery[tabindex="0"][role="group"] > figure.gallery__item` | GainsAI, Työtori |
| Plans | `.plans > article.plan` | GainsAI, Työtori |
| FAQ | `.faq > details > summary + p` | GainsAI |
| Quiet link row | `ul.quiet > li > a` | all |
| Closing CTA | `section.closing > .shell.closing__inner` | all |

### Widths and breakpoints

The pages are mobile first: base rules are the small-screen layout and every
media query is `min-width`. `.shell` centres content at `--shell` (1240px) with
a `--gutter` that steps 20px → 32px (640px) → 48px (1100px), so content stays
centred on very wide screens without stretching. Body copy is additionally
capped: `--measure` (64ch) for section intros, `--prose` (68ch) for fine print
and FAQ answers, 52–60ch inside rows, so text lines never run the full width.

| Breakpoint | What changes |
| --- | --- |
| base | one column everywhere, header nav on its own row |
| 620px | larger hero icon, gallery screenshots grow to 520px tall |
| 720px | header on one row; "Language" label appears; feature rows, `.duo`, steps and plans go two-column |
| 900px | split section heads, closing CTA text and actions side by side |
| 1024px | app hero to 2 columns with a hairline, steps to 4 columns (`--3` to 3), gallery screenshots to 620px, footer to 4 columns |

### Design tokens and per-app accents

`style.css` starts with a `:root` block holding page surfaces, text colours,
hairlines, the copper brand accent, per-app accents, the three font stacks, a
`clamp()` type scale, a spacing scale (`--space-1` … `--space-9`), layout values
(`--shell`, `--gutter`, `--section-gap`, `--measure`, `--prose`) and small radii.
It intentionally mirrors the token block in `home.css`: the two stylesheets stay
independent (see AGENTS.md "Stylesheet ownership rule") while sharing one visual
system. `home.css` is the reference for shared values — change it there first,
then mirror.

Each page sets an app class on `<body>` that overrides `--app-accent` only, so
an app keeps the same quiet identifier colour from the landing page index to its
own page:

| App | `body` class | `--app-accent` |
| --- | --- | --- |
| Shopping List & Notes | `app-page app--kauppalista` | `#8fb894` |
| WaveIQ Radio | `app-page app--waveiq` | `#8aa6c6` |
| GainsAI | `app-page app--gainsai` | `#c78d6a` |
| Työtori | `app-page app--tyotori` | `#a79ac6` |

The accent drives the hero context rule, index numbers, the short rules in front
of list items, the step top rules, the summary labels and the active nav
underline. It is never a background, a glow or a card. The focus ring is the
brand copper (`--focus`) on every page, so focus looks the same site-wide.

`style.css` contains `[hidden]{display:none !important}`. Keep it: `.btn` is
`display:inline-flex`, which would otherwise override the browser's `[hidden]`
rule and reveal elements a page keeps hidden until it has verified data, such as
the GainsAI Pro price summary.

### Google Play CTA logic

Kauppalista, WaveIQ Radio, GainsAI and Työtori all link straight to their
published Play listings from the hero, the closing CTA and the footer, and from
their card on the landing page. The URL is a plain anchor `href` in the markup and is also the
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
(`--shot-h`: 400 → 520 → 620px), so each screenshot keeps its own aspect ratio,
nothing is cropped and nothing is scaled past its natural size. There is no
per-image frame and no shadow. All gallery images use `loading="lazy"`; the hero
icon and the GainsAI promo image use `fetchpriority="high"` instead, because they
are in the first viewport.

Työtori's screenshots exist only in the app's Finnish interface (one of them in
Swedish), so the same files are listed in both the `en` and the `fi` set with
`alt` text in the page's own language, and a `.fineprint` note under the strip
says which interface language is shown. Never present a Finnish-only screenshot
as an English one.

### Adding a new app page

1. Copy `apps/waveiq/index.html` to `apps/<app>/index.html` (it is the smallest
   page: hero, feature rows, use cases, privacy columns, legal links, closing
   CTA, footer).
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

## Legal pages

The pages under `legal/` keep their own HTML, structure, URLs and local
stylesheet. Their content is legal text and is not rewritten as part of design
work. Their four stylesheets were brought onto the site palette (flat warm
charcoal, copper links, small radii, no blur or glow) so they no longer look
like a different website; the markup and every legal sentence were left
untouched.

## Sitemap and robots.txt

`sitemap.xml` lists all 25 indexable pages: the landing page, the four app pages and the four legal pages of each app, plus the SureKeep legal set. It is generated from the pages on disk, so it never lists a page that does not exist and never misses one that does. Each `<lastmod>` is the file's last git commit date; no `priority` or `changefreq` values are published.

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

A quick key-parity check is worth running alongside it, because a missing
`data-i18n` key only shows up as an untranslated string in the browser.

Then check both languages of the landing page and every app page at 320, 360,
390, 412, 600, 768, 1024, 1366 and 1920px. What to look for: no horizontal
scrolling, exactly one `h1`, the primary action visible without a long scroll,
touch targets at least 44px tall, visible focus rings when tabbing, readable
screenshots, no visible `href="#"` link, and identical key sets in `dict.en` and
`dict.fi`.

## GainsAI Pro price configuration

The GainsAI app page reads the Pro price summary from
`assets/gainsai-config.js`. Regional prices stay empty until they are verified
from the live Google Play offer; the summary stays hidden until then, which
avoids publishing an unverified price. The Google Play listing URL itself is no
longer configured here — like the other apps, GainsAI links to
`https://play.google.com/store/apps/details?id=com.janstech.gainsai` directly
from the markup.
