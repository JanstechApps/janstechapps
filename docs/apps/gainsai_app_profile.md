# GainsAI App Profile and Website Release Notes

## Public identity

- App: GainsAI
- Package name: com.janstech.gainsai
- Public app page: https://janstechapps.com/apps/gainsai/
- Privacy: https://janstechapps.com/legal/gainsai/
- Support: https://janstechapps.com/legal/gainsai/support.html
- Terms: https://janstechapps.com/legal/gainsai/terms.html
- Delete data: https://janstechapps.com/legal/gainsai/delete-data.html
- Support email: janstech.apps@gmail.com

## Verified release information

The Android project configures productionRelease with version name 1.0.7.5,
version code 77, package com.janstech.gainsai, and the production backend
variant. The project contains Google Play Billing for the gainsai_pro product
with monthly and yearly base plans, backend purchase verification, and
backend-owned entitlement presentation.

The public Google Play listing is live at
https://play.google.com/store/apps/details?id=com.janstech.gainsai (owner
confirmed on 2026-07-30). The website links to it directly from the landing page
card, the app page hero, the closing CTA and the app page footer.

The public Terms page states the owner-provided intended Finland prices as of
2026-07-26: EUR 12.99/month and EUR 119.99/year, with no free trial. The app
still receives final formatted prices, taxes, renewal terms, and regional offer
details from Google Play at runtime. The central website config keeps the
marketing price summary empty until the owner confirms that the Play listing
and public offer presentation should be enabled.

## Public feature scope

- AI-assisted first training plan and saved program library.
- Workout logging, training history, estimated 1RM trends, progress analysis,
  body metrics, and weekly check-ins.
- Adaptive training recommendations that help highlight a next training focus.
- GainsAI Coach, using the app backend and deterministic coaching logic to
  explain program, progress, and priority signals.
- In-app reporting for problematic AI-generated Coach responses, backed by an
  authenticated server-side report queue once the matching backend migration
  and deployment have been completed.
- Multi-day meal plans, Google Drive backup and restore, and a dedicated
  account-deletion flow.
- Google sign-in / Firebase Authentication for account-linked functionality.
- Pro purchase restoration, Google Play subscription management, and
  backend-verified Pro entitlement state.

GainsAI is a fitness and wellness tool. Public copy must not describe it as a
medical service or as a replacement for a doctor, physiotherapist, dietitian,
personal trainer, or other qualified professional.

## Free and Pro presentation

The public page presents the code-confirmed entitlement boundary:

- Free: first AI-assisted plan, workout logging/history, and five free Coach
  questions.
- Pro: additional AI programs, manual programs, progress/analytics, Google
  Drive backup and restore, multi-day meal plans, and Coach after the free
  questions.

Subscriptions are purchased and managed in Google Play. The app can restore
eligible purchases, while backend verification determines the account-linked
entitlement. Account deletion does not cancel a Google Play subscription.

## Website implementation

- Added the bilingual /apps/gainsai/ app page with canonical, Open Graph, and
  SoftwareApplication structured data.
- Updated the homepage GainsAI card with the app page and all published legal
  routes. The Google Play action is configuration-driven and hidden while the
  listing URL is unavailable.
- Updated GainsAI privacy, support, terms, and deletion information for
  verified billing, account-deletion, subscription behaviour, Health Connect,
  Firebase, OpenAI API processing, Crashlytics, Google Play disclosure
  coverage, and AI-generated Coach content reporting.
- Used /assets/GainsAI.png as the branded app visual. It was checked against
  the Android launcher artwork.
- Used /assets/gainsai/ominaisuuskuva/promo.png as a wide visual brand
  presentation below the hero section.
- Added current localized in-app screenshots from
  /assets/gainsai/en_screenshots/ and /assets/gainsai/fi_screenshots/. The
  gallery selects the images that match the active EN/FI language.
- EN/FI content is maintained with each page's existing client-side language
  dictionary and language preference key.
- Rebuilt the page on the shared app-page design system in `style.css`
  (see README.md "App pages"): the app name is the single `h1`, sections use
  eyebrow + `h2`, and the violet/blue accent comes from
  `body.app--gainsai`. Content, links, and metadata were preserved. The Google
  Play actions (hero, closing CTA, footer, and the landing page card) link
  straight to the published listing, in the same pattern as the other apps.

## Sources checked

Primary GainsAI sources:

- android/app/build.gradle.kts
- android/app/src/main/AndroidManifest.xml
- android/app/build.gradle.kts
- android/app/src/main/java/com/janstech/gainsai/data/billing/BillingRepository.kt
- android/app/src/main/java/com/janstech/gainsai/data/health/HealthConnectRepository.kt
- android/app/src/main/java/com/janstech/gainsai/data/backup/BackupSnapshot.kt
- android/app/src/main/java/com/janstech/gainsai/data/analytics/GainsAnalytics.kt
- android/app/src/main/java/com/janstech/gainsai/platform/SafeCrashReporter.kt
- android/app/src/main/java/com/janstech/gainsai/ui/billing/ProPaywall.kt
- android/app/src/main/java/com/janstech/gainsai/ui/coach/CoachScreen.kt
- backend/app/services/billing_constants.py
- backend/app/services/account_deletion_service.py
- backend/app/services/coach_prompt_service.py
- backend/app/services/coach_safety_service.py
- backend/app/services/coach_content_report_service.py
- backend/app/api/v1/routers/coach.py
- android/app/src/main/res/values/strings.xml
- android/app/src/main/java/com/janstech/gainsai/ui/settings/AccountDeletionViewModel.kt
- docs/architecture/changes/2026-07-22-google-play-billing-prod-valmius.md
- docs/architecture/changes/2026-07-22-play-test-billing-backend-ja-kayttooikeuden-palautuminen.md

Reference implementation sources:

- JanstechApps pages for Shopping List & Notes and WaveIQ Radio, used for the
  shared hero, card, CTA, legal-link, responsive, and EN/FI patterns.
- RadioPlayer/README.md and Shoppinglist/README.md, used to compare
  production-status and public-product documentation conventions.

## Remaining publication inputs

- Owner confirmation before exposing public marketing price summary in
  `assets/gainsai-config.js`.
- Play Console Data safety, Health apps, AI-generated content, account deletion,
  content rating, and subscription configuration confirmation.
- Migration/deploy/physical-test proof that the in-app report path for
  AI-generated Coach content is available and that reports reach the
  operational review queue.

When the public price presentation is confirmed, edit
`assets/gainsai-config.js`; the app page will reveal the price summary
automatically.
