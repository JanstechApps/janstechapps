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

The Android project configures productionRelease with version name 1.0.5.9,
version code 61, package com.janstech.gainsai, and the production backend
variant. The project contains Google Play Billing for the gainsai_pro product
with monthly and yearly base plans, backend purchase verification, and
backend-owned entitlement presentation.

The source does not contain a confirmed public Google Play listing URL. The
website therefore keeps the Google Play CTA hidden until
assets/gainsai-config.js receives the exact listing URL. Do not infer the URL
from the package name.

The repository displays no fixed Pro price. The app receives formatted prices
from Google Play at runtime, and the central website config keeps regional
prices empty until a live offer has been verified. This avoids publishing the
user-provided Finnish price candidates without a source-backed confirmation.

## Public feature scope

- AI-assisted first training plan and saved program library.
- Workout logging, training history, estimated 1RM trends, progress analysis,
  body metrics, and weekly check-ins.
- Adaptive training recommendations that help highlight a next training focus.
- GainsAI Coach, using the app backend and deterministic coaching logic to
  explain program, progress, and priority signals.
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
  verified billing, account-deletion, and subscription behaviour.
- Used /assets/GainsAI.png as the branded app visual. It was checked against
  the Android launcher artwork. No screenshots were added because no
  release-ready marketing screenshots were found in the source project.
- EN/FI content is maintained with each page's existing client-side language
  dictionary and language preference key.

## Sources checked

Primary GainsAI sources:

- android/app/build.gradle.kts
- android/app/src/main/java/com/janstech/gainsai/data/billing/BillingRepository.kt
- android/app/src/main/java/com/janstech/gainsai/ui/billing/ProPaywall.kt
- backend/app/services/billing_constants.py
- android/app/src/main/res/values/strings.xml
- android/app/src/main/java/com/janstech/gainsai/ui/settings/AccountDeletionViewModel.kt
- docs/architecture/changes/2026-07-22-google-play-billing-prod-valmius.md
- docs/architecture/changes/2026-07-22-play-test-billing-backend-ja-kayttooikeuden-palautuminen.md

Reference implementation sources:

- Janstech Apps pages for Shopping List & Notes and WaveIQ Radio, used for the
  shared hero, card, CTA, legal-link, responsive, and EN/FI patterns.
- RadioPlayer/README.md and Shoppinglist/README.md, used to compare
  production-status and public-product documentation conventions.

## Remaining publication inputs

- Exact public Google Play listing URL.
- Live Google Play confirmation for regional monthly and yearly Pro prices.

When either value is confirmed, edit only assets/gainsai-config.js; page code
will reveal the store action and price summary automatically.
