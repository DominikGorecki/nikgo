# SEO-004 — Configure site identity, canonical discovery, sitemap, and robots

- **Priority:** P0
- **Effort:** M
- **Status:** Ready after SEO-003
- **Dependencies:** SEO-001, SEO-003
- **Blocks:** SEO-005, SEO-006, SEO-016, SEO-018, SEO-019
- **Spec coverage:** P0-1, P0-2, P0-7, P0-10

## Outcome

Jekyll generates one consistent HTTPS identity for nikgo.com, a valid canonical sitemap containing only indexable pages, and an explicit robots policy that permits search/AI discovery according to owner policy.

## Current-state evidence

- `_config.yml` contains only `theme: jekyll-theme-cayman`.
- `robots.txt` and `sitemap.xml` both return 404 in production.
- Current generated canonicals are HTTPS while `og:url`, JSON-LD URL, and social image URLs use HTTP.
- `jekyll-sitemap` 1.4.0 and `jekyll-redirect-from` 0.16.0 are already in the `github-pages` 232 lockfile but are not enabled in `_config.yml`.
- `jekyll-seo-tag` 2.8.0 is already invoked as `{% seo %}` by the overridden default layout.

## GitHub Pages compatibility constraints

- Enable supported plugins through `_config.yml`; the GitHub Pages gem ignores plugin declarations made only in `Gemfile`.
- Do not set `safe: true` locally; GitHub Pages supplies its own safe build and `jekyll-sitemap` must be allowed to run.
- Do not add a hand-authored sitemap that competes with `jekyll-sitemap`.
- `robots.txt` can be a static root file; no server configuration is needed.

## Implementation scope

### 1. Expand `_config.yml`

Use approved copy and profiles:

```yaml
theme: jekyll-theme-cayman

title: "nikGo"
tagline: "Engineering, AI, and Cognition"
description: "Approved site description"
url: "https://nikgo.com"
baseurl: ""
lang: "en-US"
locale: "en_US"

author:
  name: "Dominik Gorecki"
  url: "https://nikgo.com/about/"

logo: "/assets/images/profile_pic.png"

social:
  name: "Dominik Gorecki"
  links:
    - "https://www.linkedin.com/in/nikgo"
    - "https://github.com/DominikGorecki"

plugins:
  - jekyll-redirect-from
  - jekyll-sitemap
```

Use `/about/` as the new canonical author URL unless an implementation-time conflict is documented. Do not invent a Twitter handle.

Keep `jekyll-redirect-from` before `jekyll-sitemap` so redirect pages can be handled consistently, then verify the sitemap excludes redirect stubs.

### 2. Add root `robots.txt`

Use the owner-approved policy from SEO-002. Minimum discovery-friendly file:

```text
User-agent: *
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

Sitemap: https://nikgo.com/sitemap.xml
```

An explicit OAI search entry documents intent but does not replace `User-agent: *`. Decide GPTBot/model-training access separately. Do not add `Disallow` directives for CSS, JS, images, or canonical content. Do not use robots rules to canonicalize duplicate URLs.

### 3. Configure sitemap inclusion

- Set `sitemap: false` on `404.html`, any redirect/utility page that the plugin includes, and any non-indexable landing page.
- Ensure only canonical HTML pages and intentionally indexable static documents appear.
- Decide whether the PDF is independently indexable. If the PDF should not be in the sitemap, use a Jekyll front-matter default for that exact asset path; do not assume static assets inherit page defaults without testing generated XML.
- Use explicit `last_modified_at` from article front matter.
- Do not emit `changefreq` or `priority` manually.

### 4. Remove scheme drift

- Generated canonical, `og:url`, JSON-LD URL, sitemap locations, and absolute social image URLs must use `https://nikgo.com`.
- Search generated output for `http://nikgo.com` and treat any occurrence as a build failure.
- Keep internal links root-relative or use `relative_url`; do not hard-code the GitHub repository Pages hostname.

## Acceptance criteria

- [ ] `_config.yml` contains explicit title, description, URL, baseurl, language/locale, author, logo, social profiles, and supported plugins.
- [ ] The site builds with `github-pages` 232 in safe-compatible mode.
- [ ] `_site/sitemap.xml` exists and is valid XML.
- [ ] Every sitemap URL is absolute HTTPS, canonical, indexable, and generated as 200 content.
- [ ] No raw Markdown, redirect stub, 404, draft, test page, or source artifact appears in the sitemap.
- [ ] `_site/robots.txt` exists as plain text and references the HTTPS sitemap.
- [ ] No generated file contains `http://nikgo.com`.
- [ ] Production `/robots.txt` and `/sitemap.xml` return 200 after deployment.
- [ ] `CNAME` remains `nikgo.com`.

## Verification

```bash
bundle exec jekyll build --trace
test -f _site/sitemap.xml
test -f _site/robots.txt
rg -n 'http://nikgo\.com' _site
rg -n '\.md|__no_ref|/b/test|404\.html|Zone\.Identifier|\.af<' _site/sitemap.xml
```

Parse the sitemap as XML and request every `<loc>` against the local server. After deployment:

```bash
curl -fsS https://nikgo.com/robots.txt
curl -fsS https://nikgo.com/sitemap.xml
```

## Out of scope

- Article layout and visible bylines.
- Custom article schema beyond what existing metadata produces.
- Search Console/Bing submission; SEO-018.
- IndexNow; SEO-019.
- Cloudflare domain redirects; SEO-016.
- `llms.txt` or special AI markup. It is not a substitute for crawlability, source quality, sitemap, or structured data.

## Rollback

Revert `_config.yml` and `robots.txt` together if build output becomes inconsistent. Do not remove the explicit `url` while leaving canonical metadata changes that depend on it.
