# IndexNow post-publish procedure

The repository script `scripts/indexnow_submit.py` only prepares or submits an explicit set of canonical URLs. It is not connected to GitHub Pages automatically because a submission must not race an unconfirmed deployment.

1. Wait for GitHub Pages to report a successful production deployment of the exact commit.
2. Produce the changed canonical URL list since the last recorded successful submission. Include only added, substantively updated, or deleted canonical HTML content.
3. For added/updated pages, confirm the live canonical HTTPS URL returns 200 and represents the deployed revision. For deleted pages, confirm the final 404/redirect disposition.
4. Run `python3 scripts/indexnow_submit.py --dry-run urls.txt` and review the filtered list.
5. Set `INDEXNOW_KEY` in the shell only, then submit with `python3 scripts/indexnow_submit.py urls.txt`.
6. Record the deployment commit, timestamp, count, response summary, and any retry decision in the owner-held operational log.

The public verification key file is intentionally public and is not an account password. Sitemap submission remains primary discovery coverage; IndexNow is only a freshness notification.
