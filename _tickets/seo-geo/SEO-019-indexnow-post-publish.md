# SEO-019 — Add a safe post-publish IndexNow submission workflow

- **Priority:** P1
- **Effort:** M
- **Status:** Ready after SEO-017 and SEO-018
- **Dependencies:** SEO-004, SEO-017, SEO-018
- **Blocks:** None
- **Spec coverage:** IndexNow recommendation and measurement plan

## Outcome

Owners can notify participating search engines about genuinely added, updated, or deleted canonical URLs after a successful production deployment without submitting the entire site on every commit.

## Current-state evidence

- The site has no IndexNow key or submission process.
- GitHub Pages deployment is managed externally from the repository branch; there is no current project workflow with a reliable post-deploy callback.
- IndexNow accepts a public key file hosted on the verified site and batched URL notifications.

## GitHub Pages compatibility constraints

- Host the public verification key as a static root file with front matter disabled/excluded from sitemap as needed.
- Use a repository script/manual post-publish command first; do not add a custom Jekyll plugin.
- Do not trigger submission before the changed URL is live and returns its intended production status.
- Automated credentials/secrets, if later needed, belong in GitHub Actions secrets, never source.

## Implementation scope

### 1. Generate and host the key

- Generate a strong lowercase hexadecimal key according to the current IndexNow protocol.
- Add `/<key>.txt` or an approved named key file whose body is exactly the key.
- Verify it returns 200 as plain text from the canonical HTTPS host.
- Exclude the key file from the sitemap and content indexes.
- Document that this verification key is designed to be public; it is not an account password.

### 2. Add a submission script

Create a small repository script that accepts an explicit list/file of canonical URLs and:

- Requires URLs to use `https://nikgo.com`.
- Rejects raw Markdown, preview, source artifact, image, script, stylesheet, redirect-stub, 404, and unrelated external URLs.
- Deduplicates and batches within the protocol limit.
- Sends the host, key, key location, and URL list to an official IndexNow endpoint.
- Logs timestamp, URL count, response status/body summary, and retryable errors without leaking unrelated environment data.
- Supports a dry-run mode.

Use a pinned, standard runtime already available in CI where practical.

### 3. Define the post-publish operating procedure

After GitHub Pages reports successful deployment:

1. Produce a candidate list from added/modified/deleted canonical content since the last successful submission.
2. For added/updated URLs, verify the live canonical returns 200 and matches the deployed revision.
3. For deleted URLs, verify the intended final status/redirect disposition.
4. Dry-run and review.
5. Submit one batch.
6. Record the response and submission commit/date.

Sitemap submission remains primary discovery coverage; IndexNow is a freshness notification, not a ranking or indexing guarantee.

### 4. Consider automation only after reliable manual use

Automate only if a workflow can positively identify a successful GitHub Pages production deployment and its exact revision. If that signal is unavailable, keep the documented manual command rather than using an arbitrary sleep after `push`. Automated runs must submit the diff, not every sitemap URL.

## Acceptance criteria

- [ ] The public key file returns 200 on `https://nikgo.com` and contains only the expected key.
- [ ] The script has dry-run and rejects non-canonical/non-content URLs.
- [ ] A test submission of one newly deployed canonical URL receives a protocol-success response.
- [ ] The process runs only after confirmed deployment and records the source revision.
- [ ] Repeated no-content-change runs submit zero URLs.
- [ ] Failed/retryable responses are reported without endless loops or notification spam.
- [ ] The key file is absent from sitemap, indexes, and article collection.

## Verification

Run unit tests for host filtering, deduplication, batching, dry-run, and response handling. Verify the key URL and one live changed URL with `curl`, perform a controlled submission, then check Bing/IndexNow reporting when available. Confirm the script does not submit assets or raw/redirect URLs.

## Out of scope

- Claiming IndexNow support by engines that do not participate.
- Forcing recrawl of unchanged pages.
- An unreliable action that races GitHub Pages deployment.

## Rollback

Disable the submission job/script invocation if it over-submits or targets incorrect URLs. Replace the public key file and script configuration together if key ownership must rotate.
