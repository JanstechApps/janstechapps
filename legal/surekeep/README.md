# SureKeep legal pages

Static legal/support pages for SureKeep.

Suggested deploy path:
`/legal/surekeep/`

Files:
- `index.html` – Privacy Policy, bilingual EN/FI switch like the Kauppalista example
- `support.html` – Support, EN/FI language switch
- `terms.html` – Terms, EN/FI language switch
- `delete-data.html` – Data deletion instructions, EN/FI language switch
- `style.css` – Shared styling

Notes:
- All SureKeep legal pages use the same EN/FI language switching model with `surekeep_legal_lang` localStorage persistence. They do not show mixed bilingual body text at the same time.
- Replace `/assets/surekeep-logo.png` and `/assets/surekeep-favicon.ico` with real website assets.
- Review legal content before production publishing.
