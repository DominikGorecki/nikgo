# SEO-017 — Add GitHub Actions SEO, GEO, link, and build quality gates

- **Priority:** P0
- **Effort:** XL
- **Status:** Ready after implementation tickets SEO-003 through SEO-016
- **Dependencies:** SEO-001, SEO-003, SEO-004, SEO-005, SEO-006, SEO-008, SEO-009, SEO-013, SEO-014, SEO-015, SEO-016
- **Blocks:** SEO-018, SEO-019, SEO-022
- **Spec coverage:** Automated acceptance tests; P1-32; regression coverage for P0-1 through P0-15

## Outcome

Every pull request proves that the locked GitHub Pages build succeeds and that canonical pages satisfy enforceable technical SEO/GEO, accessibility-structure, asset, schema, and link invariants before merge.

## Current-state evidence

- There is no `.github/workflows` directory or automated validation.
- Local documentation uses an unpinned `jekyll/jekyll:latest` command and no CI parity check.
- Raw Markdown and source artifacts are currently published alongside HTML.
- Metadata, sitemap, link, heading, image, and schema regressions can reach production without a gate.

## GitHub Pages compatibility constraints

- Keep GitHub Pages branch publishing unchanged; this workflow validates source and generated output but does not replace deployment.
- Run `bundle exec jekyll build` using the committed `Gemfile.lock` and compatible Ruby.
- Add a lockfile platform only if needed and commit the deterministic result; do not update the entire dependency graph accidentally.
- Build validation scripts in repository-supported Ruby/shell or a narrowly pinned tool. Do not add an unsupported Jekyll plugin to production config.

## Implementation scope

### 1. Add a validation workflow

Create a pull-request and `master` push workflow with:

1. Checkout.
2. Supported Ruby setup with Bundler cache.
3. Locked dependency install.
4. `bundle exec jekyll build --trace` with production environment.
5. Repository validators.
6. Optional pinned Lighthouse step for representative output.
7. Upload diagnostic reports on failure.

Pin action major versions and grant read-only contents permission unless an individual job needs more.

### 2. Validate source/front matter

Fail on:

- Canonical article missing required fields from SEO-003/SEO-006/SEO-008/SEO-009.
- Duplicate `content_id`, duplicate permalink, or undeclared taxonomy.
- `date_modified` unequal to `last_modified_at`.
- Invalid date, image object, related target, or schema type.
- Indexable file missing a disposition/category.
- Committed `.af`, `Zone.Identifier`, test, raw alternate, or archive leakage.
- Unapproved `http://nikgo.com`, repository-host canonical, or production secret.

### 3. Validate generated HTML and discovery files

For every canonical page, assert:

- Unique non-empty title and description.
- Exactly one canonical with the expected HTTPS URL.
- Exactly one `h1`, valid `main`, logical article landmarks, and non-empty visible content.
- Parseable JSON-LD with page-appropriate type and internally consistent URLs/dates/images.
- One robots policy and correct `noindex`/sitemap relationship.
- Open Graph/Twitter URL/image/title agreement.
- No raw `.md`, source artifact, 404, redirect stub, or unapproved static asset in sitemap.
- No duplicate canonical HTML pages for the same content ID.

### 4. Crawl internal resources

- Resolve internal links, fragments, images, stylesheets, scripts, PDF, and canonical URLs against `_site`.
- Fail on broken resources, case mismatches, links to redirects, raw source, or unpublished collection items.
- Validate image dimensions, size budgets, MIME/extensions, and alt presence from the DOM/front matter.
- Produce inbound/outbound graph data required by SEO-009.

### 5. Add regression fixtures and documentation

- Add small unit/fixture tests proving each validator fails for a known bad canonical, duplicate ID, malformed JSON-LD, broken fragment, missing image, mismatched dates, and sitemap leak.
- Document local commands in README.
- Set the workflow as a required branch check after it is stable.
- Keep messages actionable with the source path and failed invariant.

## Acceptance criteria

- [ ] A clean checkout builds with the lockfile and the same command documented for local development.
- [ ] Pull requests run build, source, output, schema, sitemap, link, artifact, and asset checks.
- [ ] Negative fixtures demonstrate that every critical validator can actually fail.
- [ ] Reports identify the exact source/page rather than only returning a generic exit code.
- [ ] The workflow has least-privilege permissions and does not deploy or mutate Pages.
- [ ] Validation covers every canonical generated page, not only a hand-selected sample.
- [ ] A required check blocks merge after an observation period with no unexplained flakes.
- [ ] CI passes on the same `github-pages` 232/Jekyll 3.10.0 stack unless SEO-001 intentionally updates it.

## Verification

Run the workflow locally where practical, open a test branch/PR, and introduce one controlled failure from each validation family. Confirm Pages publishing remains configured exactly as before. Record total duration and keep normal PR validation within an agreed budget, targeting under ten minutes.

## Out of scope

- Replacing branch-based GitHub Pages deployment.
- Live Search Console/indexation tests on every pull request.
- Using CI to auto-rewrite editorial content.

## Rollback

If a validator is demonstrably false-positive, make that specific check advisory while fixing it; keep the deterministic Jekyll build gate active. Never disable the entire workflow to bypass one content exception.
