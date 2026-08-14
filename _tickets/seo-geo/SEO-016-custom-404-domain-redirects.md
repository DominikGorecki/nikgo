# SEO-016 — Add a useful 404 and normalize domain redirects

- **Priority:** P1
- **Effort:** M
- **Status:** Ready after SEO-004
- **Dependencies:** SEO-004
- **Blocks:** SEO-017, SEO-018
- **Spec coverage:** P0-5, P1-6

## Outcome

Invalid URLs end at a useful, non-indexable 404, while all supported scheme/host variants reach the HTTPS apex canonical in one permanent hop without losing path or query.

## Current-state evidence

- `CNAME` correctly declares `nikgo.com`.
- Metadata currently shows evidence of HTTP/HTTPS identity drift.
- There is no project-specific 404 experience.
- GitHub Pages can enforce HTTPS for the configured custom domain but offers limited control over host redirects and response headers.
- `jekyll-redirect-from` creates static redirect documents, generally using client/meta refresh rather than true server-side 301 responses.

## GitHub Pages compatibility constraints

- Use a root `404.html` with front matter; GitHub Pages serves it for missing paths while retaining an HTTP 404 status.
- Do not use `.htaccess`, Netlify/Vercel rules, custom middleware, or a Ruby plugin.
- Configure domain-level HTTP redirects in the DNS/proxy provider only if it currently fronts the domain; document the external operation.
- Never describe `jekyll-redirect-from` stubs as HTTP 301/308 redirects.

## Implementation scope

### 1. Add `404.html`

Create a dedicated 404 layout/page with:

- Clear `Page not found` title and explanation.
- Links to Home, Articles, and primary topic hubs.
- Optional concise search guidance.
- No misleading fake search box.
- `sitemap: false` and `robots: noindex, follow` metadata.
- No Article/BlogPosting schema.

Verify GitHub Pages returns the custom body with a real 404 status for an unknown path.

### 2. Inventory legacy paths

Use the SEO-002 disposition table, external-link reports, and Search Console to identify URLs that previously returned meaningful content. For each:

- Map to the closest topical canonical URL.
- Use a static `redirect_from` stub only when preserving a known legacy path is more valuable than the lack of a true HTTP redirect.
- Set redirect stubs `sitemap: false` and ensure they never become canonical/internal-link destinations.
- Return 404 for random, unrelated, spam, and malformed paths; do not blanket-redirect them to Home.

### 3. Normalize scheme and host

Preferred identity: `https://nikgo.com/<path>?<query>`.

Verify/configure:

- GitHub Pages `Enforce HTTPS` enabled.
- `http://nikgo.com` → `https://nikgo.com`.
- `http://www.nikgo.com` → `https://nikgo.com`.
- `https://www.nikgo.com` → `https://nikgo.com`.
- Path and query preserved.
- At most one permanent redirect hop for externally controlled variants.

If `www` is not configured, decide whether to add the necessary DNS/proxy route. Do not point both apex and `www` at separate independently rendered sites.

### 4. Document operational ownership

Record the DNS provider, GitHub Pages domain settings, HTTPS enforcement state, proxy status, redirect-rule owner, and safe rollback. Store no account credentials/API tokens in the repository.

## Acceptance criteria

- [ ] A random missing URL returns the project 404 body with HTTP 404, `noindex, follow`, and no sitemap entry.
- [ ] Known legacy paths have explicit reviewed dispositions and no blanket homepage redirects.
- [ ] Every supported HTTP/`www` variant reaches the HTTPS apex in one permanent hop while preserving path/query.
- [ ] Canonical URLs, internal links, sitemap entries, and structured data never use a redirecting host/scheme.
- [ ] Static redirect stubs are identified as such, excluded from sitemap/internal navigation, and are not claimed to be HTTP 301s.
- [ ] `CNAME` remains exactly `nikgo.com`.

## Verification

```bash
curl -sSIL http://nikgo.com/pages/articles.md?test=1
curl -sSIL http://www.nikgo.com/pages/articles.md?test=1
curl -sSIL https://www.nikgo.com/pages/articles.md?test=1
curl -sS -o /dev/null -w '%{http_code}\n' https://nikgo.com/definitely-missing-seo-test
```

Run redirect-chain tests before and after DNS/proxy changes. Inspect generated 404 and redirect files locally, then confirm production status codes separately.

## Out of scope

- Migrating hosting providers solely for redirect headers.
- Redirecting every raw Markdown URL before SEO-002/SEO-003 has mapped it.
- IndexNow submission; SEO-019.

## Rollback

Revert external host rules at the provider if they loop or drop paths. Keep GitHub Pages HTTPS enforcement and the custom 404 unless either is proven to be the cause.
