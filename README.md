# nikGo

Personal website and blog published at [https://nikgo.com](https://nikgo.com).

## Production

- GitHub Pages deploys the Jekyll source from the repository root of `master`.
- `master` is the only production environment; there is no staging branch or preview deployment.
- `CNAME` maps the Pages site to `nikgo.com`.
- Cloudflare handles public HTTPS and edge redirects for `nikgo.com`. The local development container does not reproduce Cloudflare behavior.
- Production deployment remains GitHub Pages' branch-based build. The local Docker setup does not publish the site.

## Local development

### Prerequisites

- Docker Engine with Docker Compose v2, or Docker Desktop with WSL integration enabled.
- GNU Make. It is included by default in the intended Linux/WSL development environment.

The repository-owned image pins the official `ruby:3.3.7-alpine3.21` image by digest and runs it as `linux/amd64`. It installs Bundler 2.3.25 and the exact gems in `Gemfile.lock`, including `github-pages` 232 and Jekyll 3.10.0. The base image uses musl libc, matching the `x86_64-linux-musl` platform recorded in the lockfile.

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
