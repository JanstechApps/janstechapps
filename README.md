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
- `assets/gainsai-config.js` - Central GainsAI Google Play URL and verified regional Pro-price configuration.
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

`home.css` also contains `[hidden]{display:none !important}`. Keep it: `.btn` is
`display:inline-flex`, which would otherwise override the browser's `[hidden]`
rule and reveal the GainsAI Google Play link before a verified store URL exists
in `assets/gainsai-config.js`.

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

## GainsAI Google Play and Pro configuration

The GainsAI app page and homepage card read `assets/gainsai-config.js`. Keep
`playStoreUrl` empty until the exact public Google Play listing URL is confirmed.
Regional Pro prices are also intentionally empty until verified from the live
Google Play offer; this keeps the CTA hidden and avoids publishing an
unverified price.
