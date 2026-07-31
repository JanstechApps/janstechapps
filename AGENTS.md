# 🤖 AGENTS.md — JanstechApps repository rules for Codex / AI agents

This repository is the public JanstechApps static website.

Production domain:

- https://janstechapps.com/

The repository hosts:

- JanstechApps landing page
- shared public assets
- app-specific legal/support pages
- GitHub Pages custom domain configuration

---

# 🔴 CRITICAL RULE

No change is complete unless:

- the site still works
- public URLs are not broken
- documentation is updated when structure or behavior changes
- changes are committed

---

# 🌐 PRODUCTION URL POLICY

The production domain is:

- https://janstechapps.com/

Agents MUST NOT replace production links with:

- janstech.github.io
- localhost
- temporary preview URLs
- old standalone privacy-policy repository URLs

All public links should use the janstechapps.com domain unless there is a clear external target such as Google Play.

---

# 📁 REPOSITORY STRUCTURE

Expected structure:

~~~text
.
├── CNAME
├── README.md
├── index.html
├── home.css
├── style.css
├── sitemap.xml
├── robots.txt
├── .nojekyll
├── AGENTS.md
├── .github/
│   └── workflows/
├── tools/
├── assets/
├── apps/
│   ├── gainsai/
│   ├── kauppalista/
│   └── waveiq/
├── docs/
│   └── apps/
└── legal/
    ├── kauppalista/
    ├── waveiq/
    └── gainsai/
~~~

Root should stay clean.

Root is reserved for:

- index.html
- home.css
- style.css
- CNAME
- sitemap.xml
- robots.txt
- .nojekyll
- README.md
- AGENTS.md
- high-level config files only

Maintenance scripts belong under:

- tools/

Shared images, icons and favicons belong under:

- assets/

Public app landing pages belong under:

- apps/gainsai/
- apps/kauppalista/
- apps/waveiq/

Public app-page source profiles belong under:

- docs/apps/

Legal and support pages belong under:

- legal/kauppalista/
- legal/waveiq/
- legal/gainsai/

Do NOT recreate imported folders such as:

- *-privacy-policy-main
- kauppalista-privacy-policy-main
- waveiq-radio-privacy-policy-main
- gains-ai-privacy-policy-main

---

# 🔗 PUBLIC URLS THAT MUST KEEP WORKING

Agents MUST preserve or intentionally update these public URLs.

## Landing page

- https://janstechapps.com/

## Shopping List & Notes / Kauppalista

- https://janstechapps.com/apps/kauppalista/
- https://janstechapps.com/legal/kauppalista/
- https://janstechapps.com/legal/kauppalista/support.html
- https://janstechapps.com/legal/kauppalista/terms.html
- https://janstechapps.com/legal/kauppalista/delete-data.html

## WaveIQ Radio

- https://janstechapps.com/apps/waveiq/
- https://janstechapps.com/legal/waveiq/
- https://janstechapps.com/legal/waveiq/support.html
- https://janstechapps.com/legal/waveiq/terms.html
- https://janstechapps.com/legal/waveiq/delete-data.html

## GainsAI

- https://janstechapps.com/apps/gainsai/
- https://janstechapps.com/legal/gainsai/
- https://janstechapps.com/legal/gainsai/support.html
- https://janstechapps.com/legal/gainsai/terms.html
- https://janstechapps.com/legal/gainsai/delete-data.html

Before completing work, agents MUST check that internal links still point to valid paths.

---

# 🧾 LEGAL CONTENT RULE

Legal content must be preserved carefully.

Agents MUST NOT casually rewrite:

- privacy policy text
- terms text
- support instructions
- delete-data instructions
- data handling descriptions

Legal text may only be changed when explicitly requested or when fixing:

- broken links
- outdated URLs
- formatting
- navigation
- contact details

If legal content changes, the final response must clearly mention what was changed.

---

# 🖼️ ASSET POLICY

Shared static files belong in:

- assets/

Use root-relative paths where appropriate:

~~~text
/assets/AI.png
/assets/GainsAI.png
/assets/iq_kuv1.png
/assets/favicon.ico
~~~

Do NOT leave random images or favicons in the repository root.

When moving assets, update all references in:

- index.html
- legal pages
- Open Graph metadata
- favicon links
- README.md if relevant

---

# 🧭 LINKING RULE

Use stable root-relative links for internal site navigation:

~~~text
/legal/waveiq/
/legal/waveiq/support.html
/assets/AI.png
~~~

Do NOT use fragile paths unless there is a specific reason:

~~~text
../
../../
~~~

Before completing work, search for old/broken patterns:

- janstech.github.io
- *-privacy-policy-main
- ../
- localhost
- 127.0.0.1

Exceptions are allowed only if deliberately documented.

---

# 🏷️ APP BRANDING RULE

This repository is for JanstechApps, not the personal portfolio.

Agents MUST NOT add personal portfolio content unless explicitly requested.

Avoid:

- personal CV content
- portfolio project pages
- generic GitHub profile promotion
- unrelated developer biography

Keep the site focused on:

- JanstechApps
- Android apps
- Google Play links
- privacy/support/terms/delete-data pages
- brand contact information

---

# 🔐 SECURITY AND PRIVACY RULE

Never commit:

- API keys
- Firebase service account files
- Google credentials
- OpenAI keys
- .env secrets
- private tokens
- local config containing credentials

If such files are found, do not move or expose them. Report them immediately.

---

# 🌍 LANGUAGE RULE

The public landing page may contain both English and Finnish UI text.

When editing bilingual content:

- keep English and Finnish versions consistent
- do not remove either language accidentally
- update translation dictionaries when visible text changes
- avoid mixed-language UI unless it already exists intentionally

Legal pages may be app-specific and language-specific. Preserve their existing language and structure unless explicitly requested.

---

# 🧪 VALIDATION RULE

Before completing changes, agents SHOULD run a local static server when practical:

~~~bash
python -m http.server 8000
~~~

Then test key pages locally:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/apps/kauppalista/
- http://127.0.0.1:8000/apps/waveiq/
- http://127.0.0.1:8000/legal/kauppalista/
- http://127.0.0.1:8000/legal/waveiq/
- http://127.0.0.1:8000/legal/gainsai/

At minimum, validate:

- landing page loads
- CSS loads
- app logos load
- favicons do not use broken paths
- privacy/support/terms/delete-data links work
- no 404s for expected public pages

Agents MUST also run the automated check, which validates `sitemap.xml`,
`robots.txt` and every internal link and asset reference:

~~~bash
python tools/validate_site.py
~~~

It exits non-zero on failure and also runs in CI on every push and pull
request via `.github/workflows/validate-site.yml`.

---

# 🔎 REQUIRED SEARCHES BEFORE COMPLETION

Before finalizing a task that changes paths, links or structure, search for:

- janstech.github.io
- privacy-policy-main
- waveiq-radio-privacy-policy
- kauppalista-privacy-policy
- gains-ai-privacy-policy
- localhost
- 127.0.0.1

Also search for broken relative path patterns when relevant:

~~~text
../
../../
~~~

If any remain, explain whether they are intentional.

---

# 📘 DOCUMENTATION RULE

Update README.md whenever changes affect:

- folder structure
- production URLs
- deployment assumptions
- GitHub Pages configuration
- legal page paths
- asset paths
- testing instructions

README should remain concise and useful.

---

# 🌍 PUBLIC PAGE LOCALIZATION RULE

All public user-facing pages in this repository MUST support both:

- English (EN)
- Finnish (FI)

This applies to:

- the main landing page
- app landing pages under `/apps/`
- legal/support pages when they already use the bilingual page template
- shared navigation
- CTA buttons
- footer links
- metadata where practical

When adding or editing public pages, agents MUST:

- preserve the existing EN/FI language toggle pattern
- provide all visible user-facing text in both languages
- avoid mixed-language UI
- keep terminology consistent across pages
- ensure language switching updates all relevant text on the page

For app landing pages, language switching MUST cover at minimum:

- hero title and subtitle
- feature cards
- benefit sections
- privacy/local-first/AI summaries
- Google Play CTA text
- support/legal link labels
- footer/contact text

Agents MUST NOT create English-only public landing pages unless explicitly requested.

A public page task is not complete until bilingual behavior has been considered and implemented.

---


# 🚀 GITHUB PAGES RULE

This repository is served by GitHub Pages from the repository root.

The custom domain is controlled by:

~~~text
CNAME
~~~

Expected CNAME content:

~~~text
janstechapps.com
~~~

Do NOT delete or rename CNAME.

Do NOT replace it with the old GitHub Pages domain.

The publishing source is "Deploy from a branch": `main` / `/ (root)`.

There is no build step, so the repository root is the publish root. Do NOT
move the site into `docs/` or switch the publishing source to a GitHub Actions
workflow without explicit instruction; both would change every production URL
or silently stop publishing.

`.nojekyll` keeps GitHub Pages from processing the site with Jekyll. Do NOT
delete it — it is what guarantees files such as `sitemap.xml` and `robots.txt`
are published exactly as committed.

---

# 🎨 STYLESHEET OWNERSHIP RULE

Stylesheets are split by page type. Agents MUST respect this split.

~~~text
index.html            -> /home.css
apps/*/index.html     -> /style.css
legal/*/*.html        -> legal/<app>/style.css   (local, relative)
~~~

`home.css` is the landing page design system: tokens, shell, header, hero,
app cards, benefit grid and footer. It is mobile first, so base rules are the
small-screen layout and every media query is `min-width`.

Consequences:

- landing page work belongs in `home.css` and MUST NOT edit `style.css`
- app page work belongs in `style.css` and MUST NOT edit `home.css`
- do NOT re-point `index.html` at `style.css`, and do NOT merge the two files
- when adding a landing page rule, use the `:root` tokens in `home.css` instead
  of new hard-coded colours, radii or spacing values

`style.css` is the app page design system and follows the same rules: mobile
first, `min-width` media queries only, and a `:root` token block that
intentionally MIRRORS the tokens in `home.css` so both files share one visual
system while staying independent. `home.css` is the reference for shared values:
change it there first, then mirror into `style.css`. Do NOT introduce a third
shared stylesheet or re-point pages at another file without explicit
instruction.

Each app page sets `<body class="app-page app--<app>">`. The `.app--<app>` block
in `style.css` overrides `--accent`, `--accent-2` and `--glow` only; those
values match the app's card on the landing page. Do NOT give an app page a
separate design — the accent is the only per-app visual difference.

BOTH `home.css` and `style.css` contain `[hidden]{display:none !important}`.
Do NOT remove it. `.btn` is `display:inline-flex`, which otherwise overrides the
user-agent `[hidden]` rule and reveals elements a page keeps hidden until it has
verified data, such as the GainsAI Pro price summary.

Every app has a published Google Play listing, so all three apps link to their
store page with plain anchors from the landing page card, the hero, the closing
CTA and the app page footer. Agents MUST NOT add a guessed URL, a disabled
button, a "coming soon" label, or any placeholder that renders as a broken
action for an app whose listing is not public. `assets/gainsai-config.js` still
holds the GainsAI Pro price summary, which stays hidden until the prices are
verified from the live Play offer.

Every visible landing page and app page string needs a `data-i18n` key present
in BOTH `dict.en` and `dict.fi`; translated `aria-label`s use `data-i18n-label`.
A page change is not complete until both languages are updated.

---

# 🗺️ SITEMAP AND ROBOTS RULE

`sitemap.xml` and `robots.txt` live in the publish root and are submitted to
Google Search Console.

`sitemap.xml` is generated, not hand-edited. Whenever a public page is added,
removed, renamed or edited, regenerate and commit it:

~~~bash
python tools/validate_site.py --write
~~~

The sitemap must contain only canonical, indexable pages. Agents MUST NOT add:

- 404 pages
- redirect URLs
- URLs with fragments or query strings
- duplicate URLs
- noindex pages
- development or test files
- assets such as images, CSS or JavaScript

Keep sitemap URLs consistent with the linking rule: absolute
`https://janstechapps.com` URLs, lowercase paths, and a trailing slash for
directory URLs (`/legal/waveiq/`, not `/legal/waveiq/index.html`).

`robots.txt` MUST NOT block public pages and MUST keep its final line:

~~~text
Sitemap: https://janstechapps.com/sitemap.xml
~~~

---

# ✅ DEFINITION OF DONE

A task is complete only when:

- implementation works
- relevant links are updated
- no expected public page returns 404 locally
- root folder remains clean
- legal content is preserved unless explicitly changed
- `python tools/validate_site.py` passes
- sitemap.xml is regenerated if public pages changed
- README is updated if structure or URLs changed
- changes are committed

---

# 🧾 FINAL RESPONSE REQUIREMENTS

After completing work, report:

- commit hash
- changed files
- final folder/tree summary if structure changed
- public URLs to test
- any assumptions
- any remaining issues

If no commit was made, clearly say why.

---

# 🏁 FINAL RULE

This repository represents the public JanstechApps brand.

Keep it:

- clean
- stable
- professional
- easy to maintain
- safe for Google Play public links
