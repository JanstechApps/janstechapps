# GainsAI Legal & Support Pages

This repository contains the public legal and support pages for **GainsAI**.

These pages are intended for:

- Google Play Console privacy policy URL
- support page URL
- terms page URL
- delete-data page URL

The site is designed to be hosted with **GitHub Pages**.

## Pages included

- `index.html` -> Privacy Policy
- `support.html` -> Support and AI-generated content report contact
- `terms.html` -> Terms of Use
- `delete-data.html` -> Account and data deletion request information
- `style.css` -> shared styling
- `/assets/GainsAI.png` -> app/site logo
- `/assets/gainsai-favicon.ico` -> favicon

Last legal content update: 2026-07-26.

The pages intentionally do not invent missing legal-entity details, postal
addresses, D-U-N-S numbers, or Play Console values. If those are required for
release, they must be confirmed by the app owner before publication.

## Languages

The pages currently support:

- English
- Finnish

Language selection is handled client-side with a simple toggle and saved to `localStorage`.

## Hosting with GitHub Pages

To publish this site with GitHub Pages:

1. Open the repository on GitHub
2. Go to **Settings**
3. Open **Pages**
4. Under **Build and deployment**
   - set **Source** = `Deploy from a branch`
   - set **Branch** = `main`
   - set folder = `/(root)`
5. Save

After deployment, the site will be available at a URL similar to:

```text
https://janstechapps.com/legal/gainsai/
```
