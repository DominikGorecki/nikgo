# SEO-020 — Align external entity signals and distribute canonical work

- **Priority:** P1
- **Effort:** L
- **Status:** Ready after SEO-007 and first refreshed content batch
- **Dependencies:** SEO-007, SEO-010, SEO-011, SEO-012
- **Blocks:** None
- **Spec coverage:** P1-18, P2-25

## Outcome

Owned profiles, repositories, research artifacts, and selective distribution consistently identify the author and point to nikgo.com canonical pages without creating duplicate-content ambiguity or manufactured links.

## Current-state evidence

- The site references GitHub and LinkedIn identities, but the consistency of names, biographies, profile images, current site URLs, and topical descriptions has not been audited.
- Research articles and the PDF do not yet have a coordinated first-party repository/citation distribution path.
- There is no documented syndication/canonical policy or outreach register.

## GitHub Pages compatibility constraints

- Repository work is limited to accurate outbound profile links, author metadata, citation resources, and tracking documents that are safe to commit.
- Updating LinkedIn, GitHub profile settings, third-party publications, and community posts is an external owner action.
- GitHub Pages cannot enforce a canonical tag on content copied to another platform; only syndicate where the destination supports a canonical/original-source link or use a materially adapted excerpt.
- Do not add client-side badge widgets that harm privacy/performance just to display social proof.

## Implementation scope

### 1. Audit the entity footprint

Inventory owner-approved profiles and properties, including as applicable:

- GitHub user/profile and relevant repositories.
- LinkedIn.
- VulcLab, MyCue, and other real authored/product profiles.
- Research repositories, dataset pages, presentation pages, or scholarly identifiers.
- Existing guest posts, interviews, conference/community profiles, and bios.

For each, record current name, headshot, short bio, role/credential claims, primary URL, topic terms, ownership/access, and last update. Do not claim or include an unverified profile.

### 2. Normalize durable facts

- Use the same preferred author name and current canonical site URL.
- Keep short bios semantically consistent while adapting them naturally to each platform.
- Link to the canonical About page or most relevant canonical article/research landing page.
- Keep role, company, credential, and location facts current and consistent with SEO-007.
- Use approved profile URLs as `sameAs`; do not use every mention or directory listing.

### 3. Publish first-party research support

Where materials exist and release is approved:

- Create or improve a GitHub repository/README for data, code, notebooks, methods, or reproducibility instructions.
- Link repository → canonical research landing page and landing page → repository.
- Add version/date/license/citation instructions.
- Preserve archived releases for results tied to a specific revision.
- If no public artifact exists, retain the explicit availability statement from SEO-010 rather than creating an empty repository.

### 4. Distribute selectively

- Share new/updated work through relevant owned profiles and communities after canonical publication.
- Use excerpts or platform-native summaries that add context and link to the original.
- Seek legitimate links from cited projects, collaborators, event/resource pages, or topical roundups only when the page is genuinely useful to their readers.
- If republishing full content, set a supported canonical to nikgo.com; if the platform cannot, publish a shortened adapted version with a conspicuous original-source link.
- Track outreach, result, destination URL, link target, `rel` behavior, and follow-up date.

### 5. Protect trust

Do not buy links, exchange reciprocal sitewide links, mass-submit directories, automate generic outreach, create false personas, or represent AI-generated testimonials/endorsements as real. Disclose affiliations and conflicts.

## Acceptance criteria

- [ ] Every structured `sameAs` profile is owned/verified, current, and consistent with the About page.
- [ ] Major owned profiles use the preferred name, accurate bio facts, and canonical site URL.
- [ ] Released research artifacts have bidirectional links, version/date, license, and citation guidance.
- [ ] Syndicated copies either use an actual canonical or are materially adapted excerpts with a clear original link.
- [ ] Outreach targets are selected for topical relevance, not domain metrics alone.
- [ ] No paid/manipulative link tactic or unverifiable identity claim is used.
- [ ] A private or repository-safe distribution log records actions and outcomes without personal/contact data leakage.

## Verification

Open each owned profile while authenticated and publicly, check the current URL and bio, and verify bidirectional links. Inspect published syndicated HTML for its actual canonical link. Crawl outbound links from About and research pages. Review new backlinks/referrals in webmaster tools at the SEO-018 cadence without assuming causation.

## Out of scope

- Purchasing backlinks or guaranteed placements.
- Creating unsupported academic identifiers or affiliations.
- Mass syndication of the entire corpus.

## Rollback

Remove or correct stale external facts at their source and update `sameAs` in the same cycle. If a syndication destination cannot honor the agreed attribution/canonical policy, shorten or remove the duplicate where the owner has control.
