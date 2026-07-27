# Janstech Apps Website

This repository contains the static Janstech Apps website served from the repository root by GitHub Pages. The custom domain is configured with `CNAME`, so production pages are available under `https://janstechapps.com`.

## Structure

- `index.html` - Janstech Apps landing page.
- `style.css` - Landing page stylesheet.
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
