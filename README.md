# nikGo

Personal website and blog published at [https://nikgo.com](https://nikgo.com).

## Production

- GitHub Pages deploys the Jekyll source from the repository root of `master`.
- `master` is the only production environment; there is no staging branch or preview deployment.
- `CNAME` maps the Pages site to `nikgo.com`.
- Cloudflare handles public HTTPS and edge redirects for `nikgo.com`. The local development container does not reproduce Cloudflare behavior.
- Production deployment remains GitHub Pages' branch-based build. The local Docker setup does not publish the site.

### Canonical domain and redirect operations

The public identity is `https://nikgo.com`. The repository can provide the custom `404.html` body and static legacy redirect documents, but it cannot configure HTTP status codes or host redirects. Cloudflare and GitHub Pages settings are therefore an external release step, owned by the domain/DNS administrator; do not store provider credentials or API tokens in this repository.

Current operational record (checked 2026-08-25): the production response identifies Cloudflare as the active edge/proxy in front of GitHub Pages; the checked-in `CNAME` is exactly `nikgo.com`. The repository cannot inspect the GitHub Pages custom-domain or **Enforce HTTPS** dashboard setting, so the domain/DNS administrator must record and verify both there before release. That administrator also owns the Cloudflare redirect rule and any safe rollback. At this check, `https://www.nikgo.com` redirected to `http://nikgo.com` before HTTPS, while `http://www.nikgo.com` added an extra hop through `https://www.nikgo.com`; neither met the one-hop requirement, so the edge rule below remains a required deployment action.

Before changing edge rules, record the current DNS zone/proxy state and confirm that GitHub Pages still has `nikgo.com` as its custom domain with **Enforce HTTPS** enabled. Configure Cloudflare to issue one permanent redirect, preserving the complete path and query string, for each noncanonical entry point:

- `http://nikgo.com/*` to `https://nikgo.com/$1`
- `http://www.nikgo.com/*` to `https://nikgo.com/$1`
- `https://www.nikgo.com/*` to `https://nikgo.com/$1`

Use the provider's equivalent of a single-hop, permanent redirect rule; do not point `www` at a separately rendered Pages site, and do not redirect unknown paths to the home page. If a Cloudflare proxy/rule is not active for a hostname, do not claim that the repository or GitHub Pages supplies this normalization.

After the change, check each variant with a path and query string (for example, `/articles.html?test=1`) and confirm exactly one permanent hop reaches the HTTPS apex. Confirm a random missing canonical URL serves the custom body with HTTP 404. For rollback, disable or restore only the affected Cloudflare redirect rule, then re-run those checks; retain GitHub Pages HTTPS enforcement and the custom 404 unless either is demonstrated to cause the problem.

## Local development

### Prerequisites

- Docker Engine with Docker Compose v2, or Docker Desktop with WSL integration enabled.
- GNU Make. It is included by default in the intended Linux/WSL development environment.

The repository-owned image pins the official `ruby:3.3.7-alpine3.21` image by digest and runs it as `linux/amd64`. It installs Bundler 2.3.25 and the exact gems in `Gemfile.lock`, including `github-pages` 232 and Jekyll 3.10.0. The lockfile records both the Alpine container's `x86_64-linux-musl` platform and GitHub Actions' `x86_64-linux` platform.

`bundle exec` is required so local commands use the Jekyll and plugin versions selected by `github-pages`, rather than a global Jekyll installation. `Gemfile.lock` is committed intentionally to make local and CI builds repeatable.

The container sets the non-secret `PAGES_REPO_NWO=DominikGorecki/nikgo` value that GitHub injects into production Pages builds. This lets `jekyll-github-metadata` resolve the repository identity during an unauthenticated local build.

### Build the site

```bash
make site-build
```

This runs the equivalent of:

```bash
bundle _2.3.25_ exec jekyll build --trace
```

with `JEKYLL_ENV=production`. Generated output is written to `_site`. That directory is disposable, ignored by Git, and must not be committed.

### Run the SEO quality gate

```bash
make site-check
```

This runs the locked production build and then `scripts/validate_site.rb` against both `_articles/` and `_site/`. The gate checks front-matter/taxonomy/date/image/related contracts, sitemap and canonical metadata, JSON-LD, landmarks, internal links/fragments/resources, and image alt/size constraints. It writes a disposable diagnostic report to `_site/seo-quality-report.json` when it fails. Run only the second phase after an existing production build with:

```bash
make site-validate
```

The read-only `.github/workflows/seo-quality.yml` workflow runs the same Ruby validator after the locked Jekyll build on pull requests and `master` pushes. Make it a required branch check only after an observation period without unexplained flakes.

### Preview the site

```bash
make site-serve
```

Open [http://localhost:4000](http://localhost:4000). Local HTTPS is neither required nor configured; Cloudflare provides HTTPS only for production.

The preview uses Jekyll's watch mode and `--force_polling`, which is more reliable for bind-mounted files on WSL and Docker Desktop. Stop it with `Ctrl+C`.

Jekyll does not reload `_config.yml` while serving. Restart `make site-serve` after changing site configuration.

### Confirm the locked versions

```bash
make site-versions
```

The output must include:

```text
Bundler version 2.3.25
jekyll 3.10.0
github-pages 232
```

### Rebuild the development image

The Make targets pass `--build`, so Docker checks the image definition every time and reuses valid layers. After changing `Gemfile`, `Gemfile.lock`, `Dockerfile`, or the build arguments in `compose.yml`, the next command rebuilds the affected layers automatically.

### Compare local and production output

Compare the same path in two browser tabs, for example:

- Local: `http://localhost:4000/pages/articles/your_ai_career_plan.html`
- Production: `https://nikgo.com/pages/articles/your_ai_career_plan.html`

For a text diff:

```bash
curl -fsS http://localhost:4000/pages/articles/your_ai_career_plan.html -o /tmp/nikgo-local.html
curl -fsS https://nikgo.com/pages/articles/your_ai_career_plan.html -o /tmp/nikgo-production.html
diff -u /tmp/nikgo-production.html /tmp/nikgo-local.html
```

Differences are expected when the working tree contains unpublished changes. Scheme and edge-header differences are also expected because local development is HTTP and does not pass through Cloudflare.

### Docker Desktop troubleshooting on WSL

If `docker` reports that it cannot be found in the WSL distribution or cannot connect to `dockerDesktopLinuxEngine`, start Docker Desktop and enable integration for the current WSL distribution. Then confirm both commands work:

```bash
docker version
docker compose version
```
