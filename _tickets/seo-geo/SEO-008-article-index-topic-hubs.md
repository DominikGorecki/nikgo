# SEO-008 — Generate the article index and topic hubs from canonical content

- **Priority:** P0
- **Effort:** L
- **Status:** Ready after SEO-003 and SEO-005
- **Dependencies:** SEO-003, SEO-005
- **Blocks:** SEO-009, SEO-011, SEO-012, SEO-017, SEO-021
- **Spec coverage:** P0-15, P1-14, P1-16

## Outcome

The site exposes complete, crawlable, semantically grouped entry points generated from the canonical article collection rather than a manually maintained and incomplete card list.

## Current-state evidence

- `pages/articles.md` hard-codes article cards, ordering, image paths, and excerpts.
- The manual list can drift from source files and already carries naming/label inconsistencies.
- There are no canonical topic hubs for RAG research, agentic engineering/AI-enabled organizations, or AI/cognition/society.
- `pages/projects.md` is manually authored and has no explicit collection/ItemList metadata contract.
- Articles do not have a consistent category/topic vocabulary.

## GitHub Pages compatibility constraints

- Generate lists with Jekyll collections and Liquid 4.0 filters such as `sort`, `reverse`, and `where`; avoid custom filters.
- Keep all links generated through `relative_url` or canonical page URLs.
- Put topic hubs in `pages/topics/` with explicit permalinks so source directory names do not leak into URL decisions.
- Do not use client-side rendering or JavaScript filtering as the only way to expose articles to crawlers.

## Implementation scope

### 1. Define a controlled taxonomy

Add approved front-matter fields to every article:

```yaml
category: agentic-engineering
topics:
  - software-development
  - ai-agents
featured: false
feature_order: 0
```

Use a small controlled vocabulary documented in `_data/taxonomy.yml`. Publish these three primary hubs:

- `/topics/agentic-engineering/` — agentic engineering, AI-enabled organizations, and future of work.
- `/topics/rag-research/` — RAG research, evaluation, and AI tokenomics where relevant.
- `/topics/ai-cognition-society/` — cognition, attention, health, labor disruption, and society.

An article may belong to one primary category and several topics. Add a fourth primary hub only after the same editorial/demand review required by SEO-021.

### 2. Rebuild `pages/articles.md`

- Generate all published `site.articles` in reverse chronological order.
- Render featured items in a deliberate editorial order, then a complete all-articles list.
- Use each article's canonical URL, explicit cover image, title, description, publication date, and category.
- Prevent featured items from appearing twice unless the design explicitly labels the second occurrence as the complete archive.
- Render cards as semantic links/list items; the entire card must not depend on an `onclick` handler.
- Add an introductory paragraph that explains the scope and links to topic hubs.

### 3. Add substantive topic hubs

Each hub must include:

- A unique title and description matching a real search/research intent.
- A concise definition and scope boundary.
- A curated reading path, not merely an auto-generated tag dump.
- A complete server-rendered list of relevant canonical articles.
- Short descriptions explaining why each article belongs.
- Links to adjacent hubs and the full index.

Add visible breadcrumbs and, after SEO-006, valid `CollectionPage`/`ItemList` metadata whose entries exactly match visible items.

### 4. Add taxonomy validation

- Reject undeclared categories/topics in CI.
- Reject collection articles missing a primary category.
- Detect duplicate featured order values.
- Ensure unpublished, archived, and non-canonical alternatives never appear.

### 5. Normalize the projects index

- Preserve the current `projects.html` public URL unless an explicit redirect plan is approved.
- Move project title, description, image/logo, canonical external URL, relationship/disclosure, and status into structured front matter or `_data/projects.yml`.
- Render the visible list server-side as real links with meaningful descriptions.
- Emit `CollectionPage`/`ItemList` whose entries match the visible projects.
- Use `SoftwareApplication` only for a real project whose visible page supplies accurate application properties; otherwise keep a plain list item/Thing reference.
- Link VulcLab to RAG research with a clear author/product relationship disclosure where relevant.

## Acceptance criteria

- [ ] Every published canonical article appears in the generated complete index exactly once.
- [ ] No raw Markdown, archived alternate, test page, redirect stub, or PDF-only asset appears as an article card.
- [ ] Featured and chronological ordering are deterministic across local and GitHub Pages builds.
- [ ] Topic/category values come from the documented controlled taxonomy.
- [ ] Each published topic hub has unique explanatory copy and at least three relevant canonical items.
- [ ] Every index and hub item is discoverable without JavaScript and links to a canonical HTTPS URL.
- [ ] Visible lists and ItemList schema contain the same items and order.
- [ ] The projects index has accurate structured entries, semantic links, and no unsupported SoftwareApplication claims.
- [ ] Adding a valid collection article updates its index/hub automatically without editing card HTML.

## Verification

Build twice and diff the generated index/hubs to confirm deterministic output. Compare the count and URLs of `site.articles` to rendered card URLs, then crawl all links and images. Test keyboard navigation and a no-JavaScript browser view.

## Out of scope

- Contextual links inside article prose; SEO-009.
- Writing new companion content to fill thin hubs; SEO-021.
- Client-side search.

## Rollback

Retain the previous manual index in version control until generated output is verified. If generation fails, restore the manual page without reverting the canonical article collection or taxonomy metadata.
