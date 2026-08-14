# SEO-014 — Reduce page weight and protect Core Web Vitals

- **Priority:** P1
- **Effort:** L
- **Status:** Ready after SEO-013
- **Dependencies:** SEO-005, SEO-013
- **Blocks:** SEO-017, SEO-018
- **Spec coverage:** P1-29, P1-30

## Outcome

The static site loads quickly and remains visually stable on mobile without removing its identity, relying on lean HTML/CSS/JavaScript and pre-optimized assets suitable for GitHub Pages.

## Current-state evidence

- The homepage hero image is approximately 1.6 MB and the profile image approximately 880 KB.
- The layout loads jQuery 3.6 even though the inspected interactions can be implemented with native JavaScript.
- Font loading is duplicated between a stylesheet link and a CSS `@import`.
- Scroll, fade, theme, card-click, and image-overlay behaviors add script and accessibility cost.
- GitHub Pages provides static hosting but no repository-level control over cache headers or edge image transforms.

## GitHub Pages compatibility constraints

- Optimize committed static assets and use browser-native features; do not assume server modules, custom headers, or an image CDN.
- Keep the locked GitHub Pages/Jekyll stack unchanged unless SEO-001 explicitly updates it.
- A Cloudflare proxy/cache is optional and must not be required for acceptable baseline performance.
- Performance code must work without jQuery and degrade to readable, navigable HTML when JavaScript fails.

## Implementation scope

### 1. Capture a reproducible baseline

For homepage, article index, one long article, one image-heavy research page, and About, record mobile/desktop Lighthouse results plus transfer size, request count, LCP resource, CLS sources, and long tasks. Store the report as a CI artifact or dated audit file, not in the public site.

### 2. Optimize high-cost assets

- Resize/compress the hero and profile assets to their actual display needs with suitable responsive variants.
- Apply the image contract from SEO-013.
- Preload only the true LCP image and avoid blanket preloads.
- Give all images intrinsic dimensions.
- Remove unused duplicates and source artifacts after references are migrated.

### 3. Remove unnecessary dependencies and work

- Replace jQuery handlers with small deferred native JavaScript and remove the jQuery request.
- Consolidate scroll listeners into one passive/throttled path or CSS behavior.
- Avoid initial opacity/animation rules that hide primary content until JavaScript executes.
- Load non-critical scripts with `defer` and place scripts consistently.
- Remove card `onclick` navigation in favor of real links as required by SEO-015.
- Make the image viewer accessible and lightweight or remove it if it cannot meet those requirements.

### 4. Consolidate CSS and fonts

- Remove duplicate font imports and request only used families/weights.
- Prefer a system-font fallback immediately; use `font-display: swap` for hosted webfonts.
- Remove unused selectors after template migration.
- Keep critical above-the-fold layout stable before fonts and images arrive.
- Minification is optional; correctness and cacheable stable files matter more than opaque bundles.

### 5. Set measurable budgets

For representative mobile pages under controlled Lighthouse conditions:

- Performance score ≥90.
- LCP ≤2.5 seconds.
- CLS ≤0.1.
- INP proxy/total blocking time within Lighthouse good range; validate real INP after sufficient field data.
- Homepage initial transfer target ≤1 MB and ordinary article target ≤750 KB, with documented diagram-heavy exceptions.
- No render-blocking jQuery and no duplicate font stylesheet.

These are release gates for regressions, not claims about field Core Web Vitals until Search Console has sufficient real-user data.

## Acceptance criteria

- [ ] jQuery and any unused dependency are absent from generated pages.
- [ ] Hero/profile and article covers have responsive, compressed variants with dimensions.
- [ ] Primary text and navigation remain usable with JavaScript blocked.
- [ ] No animation causes hidden initial content, material CLS, or input blocking.
- [ ] Representative pages meet the documented Lighthouse and weight budgets or carry an approved exception with evidence.
- [ ] Font loading is not duplicated and unused weights are removed.
- [ ] Performance tests are repeatable and retained for comparison in SEO-017/SEO-018.

## Verification

Run three Lighthouse passes per template under the same throttling profile and use the median. Inspect browser network and performance traces, test slow 3G/CPU throttling, disable JavaScript, and check layout at mobile/desktop widths. After launch, compare Search Console field CWV only when enough data exists.

## Out of scope

- Migrating away from GitHub Pages solely for header control.
- A mandatory third-party CDN.
- Sacrificing readable diagrams to meet a blanket byte target.

## Rollback

Roll back individual asset/script optimizations if they break rendering or navigation. Keep the jQuery removal unless a verified essential behavior truly depends on it; restore that one behavior with a documented fallback rather than restoring all legacy scripts.
