# WaveIQ Radio App Profile

## App Name

WaveIQ Radio

## One-Line Pitch

An AI-assisted internet radio app that helps listeners find, save, understand, and rediscover stations that match their taste.

## Current Production Status

WaveIQ Radio is production-ready as an Android app, with playback, discovery, recommendations, similar stations, backup/restore, localization, privacy/support links, and Google Play readiness work documented. Google Drive OAuth is configured for production use; Google Drive backup is documented as working in closed testing and ready for production release.

## Key User-Facing Features

- Internet radio playback with saved stations and favorites.
- Browse and search stations by name, genre, country, or language.
- Preview stations before saving them.
- Personalized recommendations based on listening taste and station signals.
- Similar stations for discovering alternatives to a station the user already likes.
- Similar station tuning options: less talk, more energy, and calmer.
- Station cards with logos or consistent placeholders.
- Undo support for adding/removing stations where available.
- Sleep timer with fade-out.
- Stream reliability checks and user-facing playback feedback.
- Settings, app sharing, rating entry point, privacy link, support contact, and version information.

## AI Features

- AI-assisted station search from natural prompts.
- Locale-aware AI search explanations.
- AI-powered recommendation explanations where enough station data is available.
- "Why this station?" explanations in Recommendations and Similar Stations.
- AI-supported station summaries/labels surfaced only as user-facing insights.

## Privacy And Local-First Summary

WaveIQ Radio keeps the core listening experience local-first: saved stations, favorites, settings, and station logos are stored on the device. Online features such as AI search, recommendations, similar stations, stream health, and backup require network services. Public copy should point users to the privacy policy for details about analytics, listening signals, AI usage, and backend-assisted discovery.

## Backup And Sync Summary

WaveIQ Radio supports backup and restore for saved stations, settings, and logos. Google Drive backup is available through user-authorized Google sign-in, with manual backup/restore and automatic backup controls including Wi-Fi-only behavior. Do not describe this as live real-time cross-device sync.

## Supported Languages

- English
- Finnish
- Dutch
- Polish
- Portuguese
- Turkish

## Google Play Link

Placeholder: `https://play.google.com/store/apps/details?id=com.janstech.radioplayer`

## Legal And Support

- Website: `https://janstechapps.com/`
- Privacy policy: `https://janstechapps.com/legal/waveiq/`
- Support email: `info@janstechapps.com`
- Terms / data deletion: use the published legal page or support contact unless separate public URLs are added.

## Do Not Claim

- Do not claim real-time cross-device sync beyond backup and restore.
- Do not claim subscriptions, premium plans, or server-side premium gating are available.
- Do not claim complete recommendation coverage for every possible station.
- Do not claim every recommendation or similar station has an AI explanation.
- Do not expose internal backend endpoints, database tables, scoring fields, provider names, security internals, quotas, or implementation architecture in public marketing copy.
- Do not market unfinished experiments or roadmap items as available features.
