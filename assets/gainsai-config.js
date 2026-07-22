/*
 * Central public configuration for GainsAI website references.
 *
 * Set playStoreUrl only after the exact public Google Play listing URL has been
 * confirmed. Set regional prices only after they have been verified from the
 * live Play offer. Pages hide unavailable values automatically.
 */
window.GainsAIConfig = Object.freeze({
  playStoreUrl: null,
  proPricing: Object.freeze({
    monthly: null,
    yearly: null
  })
});
