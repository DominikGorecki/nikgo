# SEO-015 — Make navigation and content accessible to people and browser agents

- **Priority:** P1
- **Effort:** L
- **Status:** Ready after SEO-005
- **Dependencies:** SEO-005
- **Blocks:** SEO-017
- **Spec coverage:** P1-13, P1-30, P1-32

## Outcome

All important content and actions are expressed through resilient semantic HTML with predictable keyboard, focus, motion, image, and navigation behavior.

## Current-state evidence

- Some cards use clickable `div`/JavaScript behavior rather than native anchors.
- The global heading and content wrappers create a weak/duplicated document outline.
- Scroll/fade styles can hide content until script runs.
- The current image overlay is not a complete keyboard/focus-managed dialog.
- Navigation, theme controls, and motion behavior need explicit accessible-name and reduced-motion review.

## GitHub Pages compatibility constraints

- Implement with semantic HTML, CSS, and small native JavaScript; no runtime accessibility service or custom Jekyll plugin.
- Render all primary content, links, labels, and relationships in the initial HTML.
- Use ARIA only where native HTML cannot express the interaction.
- Ensure the site remains fully readable when JavaScript is unavailable.

## Implementation scope

### 1. Correct landmarks and headings

- Add a `Skip to main content` link that becomes visible on focus.
- Use one banner/header, one primary navigation, one `main`, and an appropriate footer.
- Keep exactly one `h1` per content page and a logical heading hierarchy.
- Use `article` only for self-contained articles; use `section` only when it has a meaningful label.
- Add accessible breadcrumb navigation with `aria-label="Breadcrumb"` and `aria-current="page"`.

### 2. Replace simulated controls

- Render article cards and navigation destinations as real anchors with visible focus.
- Render theme and menu actions as `button` elements with stable accessible names and state (`aria-expanded`/`aria-pressed` only when appropriate).
- Remove inline `onclick` navigation from non-interactive containers.
- Ensure every control works with Enter/Space according to its native role.

### 3. Repair motion and progressive enhancement

- Primary content must be visible before scripts execute.
- Honor `prefers-reduced-motion: reduce` for fades, scroll effects, transitions, and animated overlays.
- Do not move focus on ordinary navigation enhancements.
- Theme initialization may prevent a flash but must not block content or fail when storage access is denied.
- Ensure light/dark states meet WCAG AA contrast for text, links, focus indicators, code, and metadata.

### 4. Make media interactions accessible

- All informative images require meaningful alt; decorative images use `alt=""`.
- Charts and diagrams need captions plus equivalent explanatory prose or data table.
- If the lightbox remains, implement it as an accessible dialog: named close button, initial focus, focus containment, Escape close, focus restoration, backdrop behavior, alt/caption, and scroll management.
- Do not make the image itself the only route to important text.

### 5. Improve machine legibility

- Use explicit link text, lists, tables with headers/captions, `<time>`, `<figure>`, `<blockquote>`/`cite`, and `code` as appropriate.
- Keep key facts and definitions as text rather than CSS pseudo-content or image text.
- Avoid DOM duplication of the same article summary for visual breakpoints.
- Make hidden navigation truly unavailable when collapsed and exposed when expanded.

## Acceptance criteria

- [ ] Primary navigation, article index, theme control, image viewer, and all article links are fully keyboard operable.
- [ ] Visible focus is never removed or obscured.
- [ ] Page landmarks/headings pass automated checks and manual screen-reader navigation.
- [ ] No important content is hidden when JavaScript fails or reduced motion is enabled.
- [ ] Text, controls, links, code blocks, and focus indicators meet WCAG 2.2 AA contrast and target-size expectations where applicable.
- [ ] Images, figures, tables, inputs, and controls have appropriate accessible names/alternatives.
- [ ] Automated tooling reports no serious/critical issues on each representative template.
- [ ] Browser-agent extraction can identify title, author, dates, body, headings, figures, citations, and related links from server-rendered HTML.

## Verification

- Run axe or an equivalent automated audit on homepage, index, hub, article, research article, About, and 404.
- Complete keyboard-only testing at mobile and desktop widths.
- Test with JavaScript disabled, reduced motion enabled, zoom at 200%/400%, and Windows high-contrast/forced-colors where available.
- Perform a screen-reader smoke test with landmark, heading, link, table, figure, and dialog navigation.
- Review rendered HTML with a text/browser-agent extractor.

## Out of scope

- Accessibility overlays.
- ARIA that duplicates native semantics.
- Full translation/localization.

## Rollback

Do not roll back a verified accessibility correction solely to restore a visual effect. If a replacement interaction regresses, fall back to the simpler native link/button behavior.
