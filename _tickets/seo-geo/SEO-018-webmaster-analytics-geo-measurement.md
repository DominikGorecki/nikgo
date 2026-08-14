# SEO-018 — Establish webmaster verification, analytics, and GEO measurement

- **Priority:** P0
- **Effort:** L
- **Status:** Ready after deployment and SEO-017
- **Dependencies:** SEO-002, SEO-004, SEO-007, SEO-014, SEO-016, SEO-017
- **Blocks:** SEO-019, SEO-021, SEO-022
- **Spec coverage:** Baseline, KPI hierarchy, 30/60/90-day measurement plan

## Outcome

The owner can measure crawl/index health, search demand, page performance, referral traffic, and generative-answer visibility against the pre-change baseline without collecting unnecessary personal data.

## Current-state evidence

- No Search Console, Bing Webmaster Tools, analytics, or repeatable GEO benchmark is documented in the repository.
- Production has no sitemap/robots discovery endpoints until SEO-004 deploys.
- Success criteria in the source spec require a baseline plus 30/60/90-day comparisons.
- GitHub Pages has no private server-side analytics layer; any page analytics is a client-side third-party decision.

## GitHub Pages compatibility constraints

- Use DNS verification where possible; if an HTML/meta verification token is required, store only the provider-designated public verification value.
- Never commit API credentials, service account files, private analytics keys, or exported user-level data.
- Any client analytics tag must be a static include controlled through `_config.yml` and must respect the approved privacy/cookie policy.
- Search Console/Bing ownership, analytics properties, and prompt-monitoring accounts are external operational steps.

## Implementation scope

### 1. Verify webmaster properties

- Verify the `nikgo.com` domain property in Google Search Console, preferably by DNS.
- Verify/import the site in Bing Webmaster Tools.
- Submit `https://nikgo.com/sitemap.xml` to both.
- Confirm the live robots file is fetched successfully.
- Record owner/admin access and recovery responsibility outside the public repository.
- Inspect representative homepage, article, research landing, hub, redirect/old URL, and 404 paths after deployment.

### 2. Define a privacy-conscious analytics choice

Choose one:

- Search Console/Bing only initially, with no client analytics.
- A privacy-oriented first-party/cookieless product.
- GA4 with an approved privacy/cookie implementation appropriate to actual jurisdictions and features.

Document the business question each event answers. At minimum measure page views/landing pages, outbound source/resource clicks, PDF downloads, and navigation to companion resources. Avoid scroll-depth or invasive fingerprinting unless a real decision depends on it.

### 3. Create reporting views

Track weekly/monthly:

- Indexed vs submitted canonical pages and exclusion reasons.
- Crawl errors, sitemap health, manual/security issues.
- Search clicks, impressions, CTR, average position by page/query/country/device.
- Brand vs non-brand and cluster/hub performance.
- Core Web Vitals/HTTPS/mobile signals.
- Bing search and any available AI answer/citation metrics.
- Referral traffic from ChatGPT, Perplexity, Gemini, Copilot, Claude, and other identifiable sources, with the caveat that attribution is incomplete.
- PDF downloads and companion-resource engagement.

Use the SEO-002 exports as the immutable pre-change comparison.

### 4. Run a repeatable GEO benchmark

Create a 20–30 prompt set covering:

- Exact branded/entity questions.
- Core definitions coined by the site.
- Research questions and finding summaries.
- Non-branded problem/decision prompts from each topic hub.
- Adversarial prompts that could misstate a nuanced claim.

For each supported engine and run date, record whether nikgo.com is cited/linked, which URL, answer position/prominence, quotation/paraphrase accuracy, competing sources, and whether the answer preserves important uncertainty. Use a clean, documented method and accept that outputs are stochastic and personalized.

### 5. Define launch evaluation windows

- Day 0: verify deployment, sitemap fetch, representative inspection, analytics collection.
- Day 7–14: diagnose crawl/index errors; do not treat ranking volatility as a content failure.
- Day 30: compare coverage, impressions, referrals, and GEO citations.
- Day 60: prioritize technical/content corrections.
- Day 90: decide companion-resource investments in SEO-021.

Do not promise rankings, traffic, or AI citations. Define success as directional improvement plus healthy canonical indexation and accurate citations.

## Acceptance criteria

- [ ] Google and Bing properties are verified under durable owner control.
- [ ] The HTTPS sitemap is accepted and representative canonical URLs are inspectable/indexable.
- [ ] The selected analytics posture and privacy implications are explicitly approved before code is deployed.
- [ ] No secret or user-level analytics export is committed.
- [ ] Dashboards/report templates compare against the dated SEO-002 baseline at 30/60/90 days.
- [ ] The GEO benchmark has fixed prompts, recorded engine/date/method, and accuracy—not citation count alone—as an outcome.
- [ ] Tracking distinguishes canonical HTML from PDF and excludes preview/test/self traffic where practical.
- [ ] An owner and cadence exist for alerts, reports, and remediation.

## Verification

Use provider live tests to confirm ownership, sitemap status, robots fetch, and representative URL inspection. Test analytics in browser developer tools and verify that denied consent/no-JavaScript behavior matches the policy. Run the full prompt benchmark twice before drawing a conclusion about stochastic changes.

## Out of scope

- Buying an analytics platform without owner approval.
- Scraping generative engines in violation of their terms.
- Treating referral source labels as complete AI usage data.

## Rollback

If analytics violates the approved privacy posture or materially harms performance, remove the client include/config immediately while retaining Search Console/Bing verification. Preserve aggregate baseline reports without retaining unnecessary personal data.
