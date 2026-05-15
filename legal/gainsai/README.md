# GainsAI – Legal & Support Pages

This repository contains the public legal and support pages for **GainsAI**.

These pages are intended for:

- Google Play Console privacy policy URL
- support page URL
- terms page URL
- delete-data page URL

The site is designed to be hosted with **GitHub Pages**.

## Pages included

- `index.html` → Privacy Policy
- `support.html` → Support
- `terms.html` → Terms of Use
- `delete-data.html` → Delete Data
- `style.css` → shared styling
- `/assets/GainsAI.png` -> app/site logo
- `/assets/gainsai-favicon.ico` -> favicon

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
