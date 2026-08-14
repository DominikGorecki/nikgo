# SEO-007 — Publish an author, editorial, and trust entity layer

- **Priority:** P0
- **Effort:** M
- **Status:** Ready after SEO-005 and SEO-006
- **Dependencies:** SEO-005, SEO-006
- **Blocks:** SEO-010, SEO-011, SEO-012, SEO-018, SEO-020
- **Spec coverage:** P0-15, P1-18, P1-31

## Outcome

Readers, search engines, and generative systems can connect every article to a stable, verifiable author identity, editorial policy, correction path, and disclosed content-production process.

## Current-state evidence

- There is no canonical About/author page linked from article bylines.
- The site does not expose a consistent biography, expertise statement, editorial policy, correction process, or contact method.
- Article metadata names an author inconsistently or relies only on site defaults.
- External profiles exist in site copy/configuration but are not currently expressed as one stable entity graph.

## GitHub Pages compatibility constraints

- Build trust pages as ordinary Markdown pages with supported layouts and explicit permalinks.
- Generate Person/ProfilePage JSON-LD through a tested include; no custom plugin is needed.
- Do not put private email addresses, credentials, or unpublished personal details into source control.
- Keep `site.author.url`, visible bylines, and structured identity pointed to the same canonical About URL.

## Implementation scope

### 1. Add a canonical About/author page

Create `pages/about.md` with `permalink: /about/`. It must contain:

- Full author name and current photograph.
- A concise biography focused on demonstrated engineering, AI, research, and writing experience.
- Clear areas of expertise and explicit boundaries where the author is commenting outside professional credentials.
- Links to verifiable first-party profiles and selected work.
- A contact route that does not expose sensitive information.
- A short explanation of the site's purpose and topic scope.

Do not invent employers, titles, awards, degrees, affiliations, clients, publications, or credentials. Every factual claim must be approved or externally verifiable.

### 2. Add editorial and correction policies

Create an editorial policy page covering:

- Research and primary-source preference.
- Fact checking and date-sensitive verification.
- Citation and link practices.
- Corrections, updates, and visible modified dates.
- Conflicts of interest and affiliate/sponsorship disclosure.
- Use of generative AI in drafting, research, code, and image production.
- Medical/high-stakes content review boundaries.

Provide a visible correction/contact path. If analytics is introduced in SEO-018, create or extend a privacy page before collection begins.

### 3. Connect the entity across the site

- Link every article byline to the About page.
- Add a compact author bio after article content without repeating the full About page.
- Link About and editorial policy from persistent site navigation or footer.
- Configure `author.name`, `author.url`, `social.name`, and approved `social.links` consistently.
- Add `_data/authors.yml` keyed by `dominik-gorecki`; use it as the single source for the visible byline/bio and the structured Person.
- Emit a single `ProfilePage` with a nested `Person` on the About page, using `https://nikgo.com/about/#person` and only verified `sameAs` profiles.
- Reference that identity from article schema where the supported generator allows it; do not create competing Person objects with different identifiers.

## Acceptance criteria

- [ ] The canonical About page is indexable, linked globally, and returns 200.
- [ ] Every canonical article displays the same author name linked to that page.
- [ ] A visible editorial/corrections policy is reachable within two clicks from every article.
- [ ] ProfilePage/Person JSON-LD is valid and contains only approved factual fields and profiles.
- [ ] The author name, URL, image, and external profiles agree across config, visible content, and structured data.
- [ ] AI-assisted writing or image practices are disclosed accurately without blanket claims that cannot be audited.
- [ ] A privacy policy is present before any behavior-level analytics or cookies are enabled.

## Verification

- Build locally and crawl all article bylines, author links, policy links, and images.
- Validate the About JSON-LD and confirm there is one stable Person `@id`.
- Compare every `sameAs` URL against the live owned profile.
- Have the author approve the biography, credential boundaries, contact route, AI-use disclosure, and correction policy before merge.

## Out of scope

- Editing third-party profiles; SEO-020.
- Choosing or deploying analytics; SEO-018.
- Inventing an organization entity where no real organization publishes the site.

## Rollback

If personal or credential information is disputed, remove the disputed field from visible and structured representations together. Retain a minimal name and contact route rather than leaving inconsistent identity data.
