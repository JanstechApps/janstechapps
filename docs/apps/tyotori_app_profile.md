# Työtori App Profile

Source of truth for the public Työtori pages on this website. Every claim below was
read from the Työtori project (`C:\Dev\Tyotori`): its `CLAUDE.md`/`AGENTS.md` product
contract, `docs/architecture/tyotori-plus-v1-contract.md`,
`docs/architecture/discovery-source-matrix.md`,
`docs/release/tyotori-data-flow-and-data-safety-evidence.md`,
`app/build.gradle.kts`, and the Android string resources.

## App Name

Työtori

There is no separate English product name. Use `Työtori` in both languages.

## One-Line Pitch

An Android job search assistant for Finland: search several job boards, follow
application deadlines, prepare an application draft and its attachments, and track
the applications of a review period. The user always sends the application.

## Current Production Status

Production-ready and published on Google Play as `com.janstech.tyotori`. Google Play
Billing is live with the `tyotori_plus` subscription (monthly and yearly base plans),
and entitlement is verified by the Työtori backend, never by the app alone.

## Key User-Facing Features

- Automatic job search built from the profile, across five job sources.
- Manual job entry from a pasted posting link, or from pasted posting text when a page
  cannot be read.
- Search narrowing: keywords from the profile, one or more locations, nationwide,
  remote work, chosen job sources, sorting by best match or newest, hiding a candidate,
  paged loading.
- Result cards with job title, employer, location, source and application deadline.
- Deterministic suitability score with a level and a short reason. AI explanation on
  Työtori+.
- Saved jobs, application drafts, sent applications, archive, restore and permanent
  delete.
- AI application draft: application text and cover message, generated from the profile,
  the CV and the posting. Editable, with a separately chosen document language.
- Application letter PDF, and a generated PDF CV built from a hand-written CV that the
  user previews and accepts.
- Application materials and attachment preparation, email sending path, and saving the
  attachments to the phone.
- Työtori browser: opens the employer's own application form, checks the form, form help
  (Lomakeapu), user-confirmed basic-details fill, inserting an application text into one
  field, rule-based "Analyze application instructions", external-browser fallback.
- Sending assistant that lists the method and the readiness of each material.
- Job search obligation tracking: review period start and end date, required application
  count, progress from applications marked as sent, and starting the next period.
- Settings: language, usage analytics toggle, privacy policy link, account deletion,
  open-source licences, feedback email.

## AI Features

The backend makes exactly four model calls, all through the same service:

1. Application draft and cover message generation.
2. Suitability analysis of one saved job.
3. Explanation of the best candidates of a search.
4. Form help answers from the sanitized visible questions of an employer form.

`Analyze application instructions` is rule-based and uses no model. Deterministic
suitability scoring runs without the model, so a search still returns results if the
provider is unavailable.

## Free vs Työtori+

| | Työtori Free | Työtori+ |
| --- | --- | --- |
| Työmarkkinatori | 10 successful searches / 30 days | no search limit |
| Duunitori, Jobly, Kuntarekry, Valtiolle.fi | — | included |
| Saved jobs without a draft | 10 active | high configured fair-use limit |
| AI application draft | 1 successful per account | continuing, within quota |
| AI rewrite, AI suitability, AI search explanations | — | included |
| Form help AI, sending assistant | — | included |
| Profile, CV, PDF export, email paths, archive, review period, deletion | included | included |

The numeric limits are backend configuration, not permanent commercial promises. A
subscription never gates privacy settings, data deletion, sign-out, password reset or
reading your own data.

## Privacy Summary

Työtori requires an account (Firebase Authentication: email and password, or Google
Sign-In). Profile, CV, searches, saved jobs, applications and subscription state live on
the Työtori backend, which runs on CodentraTec-operated hosting. Profile, CV, posting and
draft text are transmitted to a text-generation service acting as a processor, so the
public copy must not claim data is never passed on. Firebase Analytics is coarse and
user-controllable; Firebase Crashlytics stays on in release builds and is **not** covered
by the analytics toggle. The App Set ID is stored only as a keyed hash for free-search
abuse control. No Advertising ID, no location permission, no profile photo.

The internal browser reads only the visible structure of an employer form — never typed
values, passwords, hidden fields, cookies, storage, HTML, DOM or full page text. It never
submits. It can fill only name, first name, last name, email, phone, city, LinkedIn and
portfolio, into text, email and phone fields, after the user starts and confirms the
action. The employer's own service can hold filled values and a chosen file before the
user presses send, and the public copy must say so.

## Supported Languages

- Finnish
- Swedish
- English

Plus a "device language" option. The language of a generated application document is
chosen separately from the app language.

## Google Play Link

`https://play.google.com/store/apps/details?id=com.janstech.tyotori`

## Legal And Support

- App page: `https://janstechapps.com/apps/tyotori/`
- Privacy policy: `https://janstechapps.com/legal/tyotori/`
- Support: `https://janstechapps.com/legal/tyotori/support.html`
- Terms: `https://janstechapps.com/legal/tyotori/terms.html`
- Delete data: `https://janstechapps.com/legal/tyotori/delete-data.html`
- Support email: `janstech.apps@gmail.com`

Open follow-up owned by the Työtori project, not by this repository: the app constant
`TyotoriLegalLinks.PrivacyPolicyUrl` and the Play Console privacy policy URL still point
at `https://codentratec.com/tyotori/tietosuoja`, and the current draft policy in that
project names CodentraTec as the controller. If the pages published here are meant to be
canonical, the app constant, its unit test and the Play Console URLs have to be updated,
and the controller wording on these pages confirmed.

## Do Not Claim

- Do not claim Työtori applies for the user, sends an application, or submits a form.
- Do not claim Työtori guarantees a job, an interview, or that an obligation is fulfilled.
- Do not claim a posting, its employer or its deadline is guaranteed current or correct.
- Do not claim data is never shared with third parties: draft generation, suitability
  analysis, search explanations and form help transmit user text to a processor.
- Do not claim local-first or offline operation. Työtori needs an account and a backend.
- Do not claim the analytics toggle covers crash reporting.
- Do not publish a subscription price. Google Play shows it in the user's own currency.
- Do not publish DEV or PROD backend URLs, API details, database tables, quota internals,
  the model provider's name or security internals.
- Do not describe roadmap items (job alerts, advanced history, advanced analytics,
  advanced PDF) as available features.
