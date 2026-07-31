# Shopping List & Notes / Kauppalista App Profile

Source of truth: `docs/architecture/kauppalista_v7_master.md`  
Audience: public landing pages, app listings, and AI-assisted marketing copy  
Scope: safe public information only

## App Identity

- App name: Shopping List & Notes
- Finnish name: Kauppalista & Muistiinpanot
- Short app name: Shopping List / Kauppalista
- Package name: `com.janstech.kauppalista`
- Google Play: https://play.google.com/store/apps/details?id=com.janstech.kauppalista

## One-Line Pitch

A local-first Android app for shopping lists, notes, tasks, recipes, birthdays, reminders, optional AI meal help, and shared lists when you choose to sign in.

## Current Production Status

The app is an Android 8+ productivity app with a production local/offline core. Account-free use is supported for the main local features. AI tools and shared lists are optional online features that require network access, and shared lists require Google Sign-In.

## Key User-Facing Features

- Shopping lists with item editing, reordering, purchased state, deletion, and favorites
- Tasks with local one-time reminders
- Notes and folders
- Recipe notes and weekly meal plans
- Birthdays with local birthday reminders
- Onboarding, settings, theme options, and optional biometric protection for selected views
- Local backup, export, and import for local app data
- Google Play review prompt and Play Store fallback
- Flexible Google Play in-app updates

## AI Features

AI features are optional and network-based. User-facing AI capabilities include:

- Recipe generation
- Weekly meal plan generation
- Ingredient scanning
- Recipe suggestions from scanned ingredients
- Saving AI-generated recipes to notes

AI is not required for normal local list, note, task, reminder, or backup use.

## Local-First / Offline-First Summary

The core app works locally without an account. Shopping lists, favorites, tasks, notes, folders, recipes saved as notes, birthdays, local reminders, settings, and local backup/export/import are stored on the device.

Online-only areas are AI features and cloud-backed shared lists. Shared-list cloud sync is separate from the local list data and does not automatically move local notes, recipes, birthdays, reminders, or ordinary lists to the cloud.

## Shared Lists / Sync Summary

Shared lists are an optional collaboration feature for shopping and task lists. Users sign in with Google to create or join shared lists, invite others with a link, and see updates in real time.

Shared lists support member roles, item add/edit/toggle, open-item reordering, owner-only cleanup of completed items, list rename/delete for owners, leaving a list for editors/viewers, member display names/avatars, and optional push notifications.

Local "share as copy" remains separate from cloud shared lists and does not require an account.

## Privacy Summary

- Core use does not require an account.
- Local app data stays on the device unless the user exports/imports it or chooses an online feature.
- Shared lists are cloud data and require Google Sign-In.
- Signing in does not automatically upload local lists, notes, recipes, birthdays, or reminders.
- Shared lists may store list metadata, items, memberships, roles, invite metadata, notification settings, and push notification metadata.
- Other members of the same shared list may see a member display name and Google/Firebase profile photo URL when available.
- The app does not upload custom avatar files to its own storage.
- Backup v4 stores shared-list cloud references only, not full shared-list content, invite tokens, FCM tokens, device IDs, or member photo URLs.

## Supported Languages

Documented supported locales:

`fi`, `en`, `de`, `es`, `fr`, `it`, `ja`, `sv`, `no`, `da`, `hu`, `et`, `uk`, `zh`

## Legal And Support URLs

- Privacy policy: https://janstechapps.com/legal/kauppalista/
- JanstechApps: https://janstechapps.com/
- Support email: `janstech.apps@gmail.com`

## Do Not Claim

Do not claim these features unless later documentation marks them production-ready:

- Mandatory account sign-in for normal app use
- Full cloud sync for all local app data
- Offline editing queue for shared lists
- Shared-list content restore from local backup
- Custom avatar upload or app-hosted avatar storage
- Presence, online status, or live typing indicators
- Owner role transfer, owner leaving their own list, owner-side member removal, or full role management UI
- Shared-list archive browsing UI
- Premium plans, quota gates, or paid shared-list tiers
- Automatic upload of local notes, recipes, birthdays, reminders, or ordinary local lists to Firebase
- Internal backend, database, security-token, or rate-limit implementation details in public marketing copy
