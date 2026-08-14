# SEO-001 — Establish a reproducible GitHub Pages build

- **Priority:** P0
- **Effort:** M
- **Status:** Implemented and verified on 2026-08-14
- **Dependencies:** None
- **Blocks:** SEO-003, SEO-004, SEO-017
- **Spec coverage:** Build/deployment foundation for every implementation ticket

## Outcome

Developers and CI can build the same Jekyll version and plugin set used by GitHub Pages, without relying on `jekyll/jekyll:latest` or a globally installed Jekyll. The repository documents the actual `nikgo.com` deployment and provides one repeatable build and preview workflow.

## Current-state evidence

- `Gemfile` contains only `gem "github-pages", group: :jekyll_plugins`.
- `Gemfile.lock` pins `github-pages` 232, Jekyll 3.10.0, Liquid 4.0.4, and Cayman 0.2.0.
- `Gemfile.lock` currently lists only the `x86_64-linux-musl` platform.
- `README.md` calls the site `nikgo.me` even though `CNAME` and production use `nikgo.com`.
- The documented Docker command uses `jekyll/jekyll:latest` and invokes `jekyll serve` directly instead of `bundle exec jekyll serve`.
- No repository-owned build/validation script or GitHub Actions workflow exists.

## GitHub Pages compatibility constraints

- Keep `github-pages` as the dependency authority; do not add a separate `jekyll` version.
- The build must work with branch-based GitHub Pages safe mode.
- Do not add custom plugins under `_plugins`.
- Do not switch deployment to GitHub Actions in this ticket.
- Do not commit `_site`.
- Preserve `CNAME` exactly.

## Implementation scope

### 1. Confirm the production source

In GitHub repository settings, confirm and record:

- Pages source is “Deploy from a branch.”
- Branch is `master`.
- Folder is `/ (root)`.
- Custom domain is `nikgo.com`.
- Public HTTPS is handled by Cloudflare for `nikgo.com`; local HTTPS is not required.

If the settings differ, stop and update this ticket bundle before making architecture changes. Do not silently change the deployment model.

### 2. Add deterministic developer commands

Add repository scripts, a pinned container configuration, or both, so these logical commands exist:

```text
site-build  -> bundle exec jekyll build --trace
site-serve  -> bundle exec jekyll serve --watch --force_polling --host 0.0.0.0
```

Requirements:

- Install and use the Bundler version declared by `Gemfile.lock` or intentionally update the lockfile in the same change.
- Run through `bundle exec` so Jekyll 3.10.0 and the locked plugins are used.
- Pin the container image by immutable digest or explicit version; do not use `latest`.
- Mount the repository at a stable working directory.
- Keep the generated destination `_site`.
- The commands must work on Linux/WSL, the environment named in the current README.
- If the chosen environment is glibc-based, add the correct platform to `Gemfile.lock` with Bundler rather than hand-editing the lockfile.

### 3. Update README.md

Document:

- Correct site name and production URL: `nikgo.com`.
- Prerequisites.
- Exact build and preview commands.
- Why `bundle exec` is required.
- That `_config.yml` changes require restarting Jekyll.
- That `_site` is generated and must not be committed.
- How to compare a local page with its live equivalent.

### 4. Capture a pre-change build baseline

Build the current site and record at least:

- Jekyll/plugin versions shown by the environment.
- Build exit code and warnings.
- Count of generated files.
- Representative generated paths: `/index.html`, `/articles.html`, `/projects.html`, one article HTML file, its raw `.md` duplicate, and `/b/test.html`.

The raw duplicate and test page are expected at this stage; SEO-003 removes them.

## Acceptance criteria

- [x] GitHub Pages source/custom-domain settings are documented.
- [x] A fresh checkout can build without a global Jekyll installation.
- [x] The build uses `github-pages` 232 and Jekyll 3.10.0.
- [x] Local preview uses `bundle exec jekyll serve` through the documented environment.
- [x] No command uses an unpinned `latest` container tag.
- [x] `README.md` identifies `nikgo.com`, not `nikgo.me`.
- [x] `_site` remains ignored and untracked.
- [x] `CNAME` remains unchanged.
- [x] The baseline build and representative output paths are recorded in the ticket/PR notes.

## Verification

Run the repository-defined equivalents of:

```bash
bundle exec jekyll --version
bundle exec jekyll build --trace
git status --short
test -f _site/index.html
test -f _site/articles.html
test -f _site/pages/articles/your_ai_career_plan.html
```

Verify `git status` does not list `_site`.

## Out of scope

- SEO fixes.
- Content migration.
- Changing the GitHub Pages deployment source.
- Adding CI quality gates; that is SEO-017.

## Rollback

Revert only the developer tooling and README changes. The site source and public output should be unchanged by this ticket.

## Implementation record — 2026-08-14

### Confirmed deployment model

- GitHub Pages builds the repository root of `master` for the sole production environment.
- `CNAME` remains `nikgo.com`.
- Cloudflare owns public HTTPS and edge redirects.
- Local development intentionally uses `http://localhost:4000` with no HTTPS requirement.
- No deployment workflow or non-local environment was added.

### Implemented tooling

- `Dockerfile` pins `ruby:3.3.7-alpine3.21` by immutable digest and installs Bundler 2.3.25.
- `compose.yml` fixes `linux/amd64`, matching the lockfile's `x86_64-linux-musl` platform, bind-mounts the repository at `/srv/jekyll`, and supplies the non-secret Pages repository identity.
- `Makefile` provides `site-build`, `site-serve`, and `site-versions` targets. All Jekyll commands run through `bundle _2.3.25_ exec`.
- `Gemfile.lock` is no longer ignored and is part of the reproducible build input.
- `_config.yml` excludes Docker/build inputs so they are not copied into the public site.

### Locked versions verified

```text
ruby 3.3.7 (x86_64-linux-musl)
Bundler version 2.3.25
jekyll 3.10.0
github-pages 232
```

### Production-mode build baseline

Command: `make site-build`

- Exit code: `0`.
- Generated files: `139` in the current worktree.
- Build time reported by Jekyll: approximately `1.1 seconds` after the image was built.
- Expected unauthenticated-local warnings:
  - Faraday reports that optional retry middleware is not installed.
  - `jekyll-github-metadata` reports that no GitHub API authentication is configured; the repository identity is still supplied explicitly through `PAGES_REPO_NWO`.
- No build-only `Dockerfile`, `Makefile`, `compose.yml`, `Gemfile`, or `Gemfile.lock` is present in `_site`.
- `_tickets/` is not published.

Representative generated paths verified:

```text
_site/index.html
_site/articles.html
_site/projects.html
_site/pages/articles/your_ai_career_plan.html
_site/pages/articles/your_ai_career_plan.md
_site/b/test.html
```

The raw Markdown duplicate and test page are expected baseline defects and remain assigned to SEO-003. The count also reflects the current untracked SEO/GEO spec and `Amdahls_Law__The_Intelligence_Explosion_Will_Branch.md` candidate; neither was modified by this ticket.

### Local preview verification

`make site-serve` started watch mode at `http://0.0.0.0:4000`. Requests to `/` and `/pages/articles/your_ai_career_plan.html` both returned HTTP 200. Generated `_site` files are owned by the local user and remain ignored/untracked.
