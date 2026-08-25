# Webmaster, measurement, and GEO operating runbook

This site currently uses the privacy-preserving **webmaster-tools-only** posture: no client analytics script is shipped. Search Console and Bing Webmaster Tools are sufficient to establish crawl, index, query, and Core Web Vitals baselines before a separately approved analytics decision.

## Owner-held setup (do not commit credentials)

1. Verify the `nikgo.com` Domain property in Google Search Console with a DNS record held by the domain owner. Record the owner, recovery contact, and verification date in the owner's private records.
2. Verify or import `https://nikgo.com/` in Bing Webmaster Tools under the same durable owner control.
3. After a successful Pages deployment, submit `https://nikgo.com/sitemap.xml` to both tools and confirm that `https://nikgo.com/robots.txt` is fetchable.
4. Inspect Home, `/about/`, `/articles.html`, each topic hub, one standard article, one research article, one legacy redirect, and `/404.html`. Record any exclusion or canonical disagreement in the private operational log.

Never commit API credentials, verification-recovery material, raw query exports, user-level analytics, cookies, or account screenshots. A provider-required public verification token may be committed only after the owner approves it.

## Analytics decision gate

Do not add a browser analytics tag until the owner approves both the provider and the applicable privacy/cookie posture. The proposal must state the decision each event serves, data retention, jurisdictions, consent behavior, and how no-JavaScript/denied-consent behavior works. The minimum useful events are landing-page views, outbound resource clicks, PDF downloads, and companion-resource navigation; do not collect scroll depth or fingerprinting data by default.

## Reporting cadence

Use `_tickets/seo-geo/SEO-002-*` exports as the immutable pre-change baseline. Maintain a private copy of `templates/seo/monthly-measurement-report.md` for Day 0, Day 7–14, Day 30, Day 60, and Day 90 reviews. Day 90 is the earliest decision point for SEO-021 companion-resource proposals.

## GEO benchmark

Use `templates/seo/geo-benchmark.csv` as a repeatable 24-prompt benchmark. For each engine, record the date, signed-out/clean-session method, cited URL, answer position, citation/quotation accuracy, qualification preservation, and competing sources. Generative answers are stochastic and personalized: compare repeated runs and do not treat an uncited answer as proof of a site defect.

## Escalation

Escalate immediately to the site owner for a manual action, security issue, robots/sitemap outage, widespread canonical exclusion, or material analytics/privacy concern. Diagnose normal ranking movement at the next scheduled review rather than changing content reactively.
