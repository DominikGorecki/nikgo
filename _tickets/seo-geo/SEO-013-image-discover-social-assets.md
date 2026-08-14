# SEO-013 — Standardize image assets for search, Discover, and social previews

- **Priority:** P1
- **Effort:** L
- **Status:** Ready after SEO-006 and SEO-005
- **Dependencies:** SEO-005, SEO-006
- **Blocks:** SEO-014, SEO-017
- **Spec coverage:** P1-26, P1-27, P2-28

## Outcome

Every indexable article has an explicit, high-quality, rights-cleared image set that renders efficiently in the article, search previews, large-image surfaces, and social cards.

## Current-state evidence

- Most current article covers are approximately 800×450, below the preferred 1200-pixel width for large preview eligibility.
- Social-image selection is inferred from source conventions rather than a normalized front-matter image object.
- Asset directories contain metadata/artifact files such as `.af` and `Zone.Identifier` companions.
- Alt text, captions, credits, provenance, intrinsic dimensions, and loading behavior are inconsistent.

## GitHub Pages compatibility constraints

- Commit pre-generated raster variants; GitHub Pages will not run an image-processing plugin.
- Use standard `<picture>`, `srcset`, `width`, `height`, `loading`, and `decoding` attributes.
- Keep paths case-correct for Linux/GitHub Pages.
- Do not add build dependencies that fall outside `github-pages` 232 merely to resize images.

## Implementation scope

### 1. Define the asset contract

Store normalized article images under a stable convention such as:

```text
assets/articles/<content_id>/cover-16x9.webp   # 1280×720 minimum
assets/articles/<content_id>/cover-4x3.webp    # optional editorial crop
assets/articles/<content_id>/cover-1x1.webp    # optional social/profile crop
```

Retain PNG/JPEG only where transparency, diagrams, or compatibility make WebP inappropriate. Filenames must be lowercase, portable, and descriptive. Strip OS metadata and embedded EXIF not needed for attribution.

### 2. Create or upgrade every cover

- Produce a minimum 1280×720 16:9 cover for every canonical article.
- Preserve important visual content inside social/Discover safe areas.
- Avoid tiny text, misleading charts, copyrighted logos, and visual claims absent from the article.
- Confirm ownership/license for existing assets.
- Record whether an image is original, licensed, generated, or materially AI-edited and retain generation/source notes outside public metadata when appropriate.
- Disclose AI-generated imagery according to SEO-007's approved policy.

### 3. Populate explicit image metadata

For every article, set `image.path`, `image.width`, `image.height`, and `image.alt`. Add caption and credit/source fields where required. Alt text must explain the image's purpose in context; decorative texture should use empty alt rather than keyword stuffing.

### 4. Render responsive images

- Render the above-the-fold article cover with intrinsic dimensions and high priority; do not lazy-load the LCP cover.
- Lazy-load and asynchronously decode non-critical body images.
- Use `srcset`/`sizes` only when real variants exist.
- Give diagrams readable high-resolution sources, accessible captions, and a prose explanation of their key information.
- Keep Open Graph/Twitter metadata pointed to an absolute version of the 1280×720 asset.

### 5. Enforce budgets

- Target ≤200 KB for ordinary photographic/illustrative covers where quality permits.
- Set a documented exception process for dense diagrams/screenshots.
- Reject missing dimensions, broken assets, images under 1200 pixels wide when used as a large preview, and committed metadata artifacts.

## Acceptance criteria

- [ ] Every canonical article has an explicit ≥1200-pixel-wide cover with valid dimensions and contextual alt text.
- [ ] Every declared image resolves locally and in production with the correct case and MIME type.
- [ ] Article, Open Graph, Twitter, and JSON-LD image references point to the intended canonical asset.
- [ ] Above-the-fold covers are not lazy-loaded; below-the-fold images are lazy-loaded unless an exception is documented.
- [ ] Images reserve layout space and do not introduce material cumulative layout shift.
- [ ] No `.af`, `Zone.Identifier`, EXIF location data, or other source artifact is published.
- [ ] Licensing/provenance and any required AI-image disclosure are recorded.
- [ ] Meaningful charts/diagrams have captions and equivalent prose context.

## Verification

Build an image inventory from article front matter and inspect dimensions, file size, MIME type, duplicate hash, path case, alt, caption, and credit. Test representative previews after deployment and run Lighthouse on a cover-heavy article. Confirm `max-image-preview:large` is present from SEO-006.

## Out of scope

- Broad visual redesign unrelated to discovery or performance.
- Runtime image CDN/transformation service.
- Replacing diagrams that are already accessible and suitably sized.

## Rollback

Keep original source assets until normalized variants pass visual review. If a new asset has rights or factual issues, restore the prior approved asset and update front matter/social metadata together.
