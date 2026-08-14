# SEO-009 — Build intentional internal links and related-reading paths

- **Priority:** P0
- **Effort:** L
- **Status:** Ready after SEO-008
- **Dependencies:** SEO-005, SEO-008
- **Blocks:** SEO-010, SEO-011, SEO-012, SEO-017, SEO-021
- **Spec coverage:** P1-17

## Outcome

Every article participates in a coherent knowledge graph with descriptive contextual links, a canonical hub path, and useful related reading that helps both human readers and retrieval systems understand topic relationships.

## Current-state evidence

- Existing articles contain only sparse cross-links and most are isolated from adjacent site content.
- Related-content modules are absent.
- Manual index cards are the primary discovery path.
- Some reference sections contain inconsistent numbering; the Roko article has a duplicate `[5]` key.

## GitHub Pages compatibility constraints

- Resolve related content at build time with collection data and standard Liquid; no runtime API or JavaScript graph is required.
- Give each canonical article a stable `content_id` independent of filename and display title.
- Store relationships as front-matter IDs, not generated paths, so explicit legacy permalinks remain changeable without breaking the model.
- CI, rather than a custom Jekyll plugin, must validate missing IDs and broken relationships.

## Implementation scope

### 1. Define relationship metadata

Add unique, immutable IDs and ordered relationships:

```yaml
content_id: ooda-loop-for-agentic-software-development
related:
  - 90-percent-problem-agentic-engineering
  - vibe-coding-trap
```

The `related` field is editorial and directional: the target need not point back. Limit the rendered module to two to four strong relationships. Never infer relationships solely because two pages share a generic `AI` tag.

### 2. Implement the related-content include

- Resolve each ID against `site.articles` using Liquid-supported operations.
- Render title, concise description, category, and canonical link in the declared order.
- Skip no target silently in production: fail CI when an ID is unknown, unpublished, duplicate, or self-referential.
- Render no section when the list is intentionally empty.
- Keep the module server-rendered and semantic.

### 3. Edit contextual links in article prose

For every article:

- Add a link to its primary topic hub.
- Add two to four relevant links from sentences where the destination genuinely expands a concept.
- Use descriptive anchor text that states the destination concept; avoid repeated `click here`, raw URLs, and keyword-stuffed exact-match anchors.
- Add links bidirectionally only when each direction is editorially useful.
- Preserve cited external sources; internal links do not replace evidence.
- Avoid linking every occurrence of a repeated term.

### 4. Repair reference integrity

- Fix duplicate or skipped citation labels, beginning with the duplicate `[5]` in the Roko article.
- Ensure in-text markers point to the intended unique reference.
- Do not change quotations or source claims while renumbering.
- Flag orphan reference entries and uncited factual claims for the content-cluster tickets.

### 5. Produce an audit artifact

Generate a machine-readable internal-link report during CI or as a maintained script output with:

- Canonical URL.
- Inbound article links.
- Outbound internal links.
- Primary hub link.
- Related IDs.
- Broken/redirecting links.

The report should identify orphan pages and pages with no contextual inbound links. It need not be committed if CI presents it as an artifact.

## Acceptance criteria

- [ ] Every article has a unique `content_id` and a primary topic-hub link.
- [ ] Every article has at least two useful contextual inbound links from other canonical pages, unless an approved exception is documented.
- [ ] Related modules contain no self-links, missing targets, duplicates, redirects, or non-canonical URLs.
- [ ] All anchors are server-rendered, crawlable, descriptive, and keyboard accessible.
- [ ] Citation/reference identifiers are unique within each article and all in-text identifiers resolve.
- [ ] The link report shows no orphan canonical article and no broken internal URL.
- [ ] No implementation creates circular redirect paths or links to raw `.md` alternatives.

## Verification

- Build and crawl all internal anchors, images, and fragments.
- Run a graph check over canonical HTML pages and report weakly connected/orphan nodes.
- Compare each `related` front-matter ID to the generated module.
- Manually review anchor context; HTTP validity alone does not establish editorial relevance.

## Out of scope

- New content created only to receive links; SEO-021.
- Third-party backlinks; SEO-020.
- Rewriting unsupported claims; SEO-010 through SEO-012.

## Rollback

Relationship metadata and the related include can be reverted independently from contextual prose links. If a target is withdrawn, remove all incoming relationships and prose links in the same change.
