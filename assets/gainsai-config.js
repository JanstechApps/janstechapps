/*
 * Central public configuration for GainsAI website references.
 *
 * The public Google Play listing URL is published, so the store links are plain
 * anchors in the pages, exactly like the other apps. Set regional prices only
 * after they have been verified from the live Play offer; the app page hides an
 * unavailable price summary automatically.
 */
window.GainsAIConfig = Object.freeze({
  proPricing: Object.freeze({
    monthly: null,
    yearly: null
  })
});
