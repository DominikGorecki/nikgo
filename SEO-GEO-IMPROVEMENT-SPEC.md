# nikGo SEO and Generative Engine Optimization Improvement Spec

**Site:** [https://nikgo.com/](https://nikgo.com/)  
**Repository:** `DominikGorecki/nikgo`  
**Audit date:** 2026-08-13  
**Platform:** GitHub Pages, Jekyll, Cayman theme, Cloudflare edge  
**Purpose:** Establish a technically sound, search-visible, entity-rich publishing system that makes Dominik Gorecki's original work easy to discover, understand, cite, and revisit through conventional search and generative AI experiences.

---

## 1. Executive summary

nikGo has the hard part that many SEO projects lack: roughly 60,000 words of substantive, original writing across engineering leadership, agentic software development, RAG research, AI economics, and cognition. Several articles include primary analysis, explicit methodology, charts, references, and memorable original frameworks. That is strong raw material for both traditional search and generative answer systems.

The publishing layer is currently preventing that material from reaching its potential. The live audit found the following critical problems:

- `robots.txt` and `sitemap.xml` both return **404**.
- All 26 article Markdown sources are publicly available as raw `.md` files in addition to rendered `.html` pages, creating duplicate crawlable representations without canonical consolidation.
- **13 of 26 rendered article pages use the generic title `nikgo`** rather than the article title. This happens when GitHub Pages cannot infer the title from the first heading because an image precedes it.
- **None of the 26 audited articles has a meta description.**
- Every audited article is represented in JSON-LD as a generic `WebPage`, not `Article`, `BlogPosting`, or `ScholarlyArticle`.
- Article metadata does not provide a published date, modified date, author entity, topic entities, or a stable author URL.
- Generated canonical links use `https://`, while `og:url`, Open Graph image URLs, and JSON-LD URLs use `http://`. The missing `url` setting in `_config.yml` is the likely source of this inconsistency.
- The global template creates two H1 elements on most content pages: the global `nikGo` hero and the page/article H1.
- At least eight article files are drafts, alternate versions, or near-duplicates that are live but absent from the article index. Three are explicitly named `__no_ref`; three are versions of “AI in the Veins”; both versions of “What Freedom Is For” are live; and `ai_public_opinion_cliff.md` is live but unlisted.
- A default Jekyll test page is live at `/b/test.html`.
- Seven source/design/operating-system artifact files are deployed publicly. Confirmed examples include a 2.0 MB Affinity file at `/assets/images/profile_pic.af`, a 5.0 MB Affinity file under the article image directory, lock files, and Windows `Zone.Identifier` files.
- Important article artwork is usually 800×450. That is below Google's recommended 1,200-pixel width for large Discover previews.
- The global background image is 1.6 MB and the 150-pixel profile avatar downloads an 880 KB, 1024×1024 PNG. No authored images declare `width`, `height`, `loading`, or `decoding` attributes.
- A full jQuery 3.6.0 dependency is loaded on every page even though the site JavaScript is written entirely with browser APIs and does not use jQuery.
- There is no repository-visible analytics, Search Console verification, or search performance instrumentation. DNS-based verification may exist, so this is not proof that the accounts are absent.

The highest-leverage move is not producing more articles. It is consolidating the existing work into one canonical URL per article, giving every page explicit editorial metadata, adding article and author structured data, publishing discovery files, and building topic hubs and internal links around the strongest areas of demonstrated expertise.

### Recommended order

1. **Fix crawl/index control and duplicate URLs.**
2. **Add explicit page metadata, canonical URL consistency, article schema, dates, and authorship.**
3. **Create author and topic entities, then connect articles into deliberate clusters.**
4. **Refactor articles for answerability and citation without flattening their voice.**
5. **Improve images, page weight, accessibility, and measurement.**
6. **Use measured search and AI citation data to decide what to expand next.**

### Expected outcome

After implementation, every indexable idea should have one stable HTTPS URL, a unique title and description, an explicit author and publication history, a representative large image, valid machine-readable semantics, and multiple contextual internal links. Search engines should receive a canonical sitemap. AI search crawlers should receive an explicit access policy. Readers and answer engines should be able to identify the thesis, evidence, definitions, and source provenance without guessing.

---

## 2. Scope, method, and limitations

### 2.1 What was examined

This audit covered:

- All tracked repository files and primary Jekyll configuration/templates.
- The home page, article index, project index, all 26 article Markdown files, article images, figures, and the PDF white paper.
- Live HTTP status, response headers, metadata, headings, canonical tags, JSON-LD, Open Graph tags, and content types on representative and bulk article URLs.
- Live availability of discovery files, raw source files, draft/version pages, test content, and non-web design artifacts.
- Domain variant redirect behavior for HTTP, HTTPS, apex, and `www`.
- Representative requests using Googlebot, Bingbot, OAI-SearchBot, GPTBot, ChatGPT-User, ClaudeBot, and PerplexityBot user agents.
- Current primary-source guidance from Google Search Central, Bing Webmaster, OpenAI, GitHub Pages, and web.dev.

### 2.2 What was not available

This repository does not contain private performance data. The following cannot be determined conclusively without owner access:

- Google Search Console impressions, clicks, indexed URL count, canonical selections, crawl errors, and AI feature visibility.
- Bing Webmaster Tools indexed URLs, backlink data, grounding queries, and AI citation counts.
- Actual ChatGPT, Perplexity, Gemini, Claude, or Copilot citation frequency.
- Organic conversions and engaged reading behavior.
- Real-user Core Web Vitals.
- Backlink quality and referring-domain history.
- Whether Search Console/Bing verification exists through DNS.

The public `site:` spot checks performed during the audit returned the homepage but did not surface an article result. Search operators are incomplete and must not be treated as an authoritative index count. Use Search Console and Bing Webmaster Tools to establish the real baseline.

Google PageSpeed Insights could not return a lab report because the public API quota was exhausted. Performance findings below are therefore based on direct asset inspection and code review, not an invented Lighthouse score.

---

## 3. Current-state inventory

| Item | Observed state |
|---|---:|
| Tracked repository files | 134 |
| Article Markdown files | 26 |
| Approximate article word count | 60,642 |
| Article image/figure files | 62 |
| Articles/white papers linked from “All Articles” | 18 Markdown articles + 1 PDF |
| Unlisted draft/version/article candidates | 8 |
| Audited article HTML URLs returning 200 | 26/26 |
| Audited raw article `.md` URLs returning 200 | Confirmed; publishing pattern applies to all source pages |
| Article pages with generic `nikgo` title | 13/26 |
| Article pages with a meta description | 0/26 |
| Article pages with `Article`/`BlogPosting` schema | 0/26 |
| Root `robots.txt` | 404 |
| Root `sitemap.xml` | 404 |
| Live default Jekyll test page | `/b/test.html` returns 200 |
| Public non-web artifact candidates | 7 tracked; representative URLs confirmed 200 |

### 3.1 Content strengths

- The content is not thin. Individual articles range from roughly 800 to 5,600 words.
- The RAG papers provide abstracts, methods, statistical results, charts, limitations, and references. They are the strongest natural candidates for citations and durable search traffic.
- The opinion essays have specific theses and original terminology, including “portable minds,” “OODA velocity,” the “90 percent problem,” “leisure literacy,” “Context Bank,” and “agentic engineering.” Distinct concepts are useful for entity association and earned mentions.
- References are generally descriptive and point to credible external sources.
- Content is server-rendered HTML; core text does not depend on client-side JavaScript to exist in the DOM.
- HTTPS works, the apex domain is stable, and tested major search/AI user agents received HTTP 200 for an article page.
- The site is readable on mobile and already has a consistent visual identity.

### 3.2 Content liabilities

- The same subject is sometimes published as multiple live versions without a canonical editorial decision.
- The article index hard-codes metadata rather than generating it from article front matter, so titles, dates, descriptions, and URLs can drift.
- Published dates appear only in the article index, often as month/year or year only. They are absent from the article pages and structured data.
- The “All Articles” entry for the RAG dose-response article spells the author as `Domink Gorecki`.
- Article pages do not show a consistent byline, author biography, revision date, category, tags, or related reading.
- The homepage describes expertise but provides limited verifiable experience detail, speaking/writing history, project outcomes, or a dedicated author profile.
- The single articles page mixes general essays and research papers but does not create crawlable subject hubs.

---

## 4. Severity model and scorecard

| Priority | Meaning |
|---|---|
| **P0 — Critical** | Prevents reliable discovery, causes duplicate/incorrect indexing, or materially misrepresents pages. Resolve before publishing more content. |
| **P1 — High** | Strongly affects relevance, entity confidence, click-through, citations, or user experience. Resolve in the first implementation cycle. |
| **P2 — Medium** | Improves reach, performance, maintenance, and measurement after foundations are correct. |
| **P3 — Experimental** | Test only after measurable baselines exist; do not mistake for a ranking requirement. |

| Area | Current assessment | Primary reason |
|---|---|---|
| Crawl discovery | **Critical** | No sitemap or robots file; raw source and unwanted files are public. |
| Canonicalization | **Critical** | HTML and Markdown variants plus live drafts; inconsistent HTTP/HTTPS metadata. |
| Page metadata | **Critical** | Half of article titles are generic; all article descriptions are absent. |
| Structured data | **Critical** | Articles are declared only as generic `WebPage` objects. |
| Authorship/entity signals | **Weak** | No author page, article author entity, dates, or consistent sameAs graph. |
| Content substance | **Strong** | Original, long-form, referenced, often evidence-rich material. |
| Information architecture | **Weak** | Flat article list; no topic hubs or systematic related-content links. |
| GEO answerability | **Moderate** | Strong source material, but key claims and provenance are not consistently surfaced. |
| Image/search presentation | **Weak** | Small social images, HTTP OG URLs, no large-preview directive, missing dimensions. |
| Performance | **Needs work** | 1.6 MB global hero, oversized avatar, unused jQuery, and no field measurements. |
| Measurement | **Unknown** | No accessible webmaster/analytics data; no defensible baseline. |

---

## 5. Detailed findings and requirements

## 5.1 Crawlability, indexing, and URL control

### P0-1: Publish an explicit robots policy

**Finding:** `https://nikgo.com/robots.txt` returns 404. A missing file generally means crawlers are not disallowed, and the user-agent tests returned 200, but absence is not a strategy. It also prevents sitemap discovery through the standard `Sitemap:` directive.

**Requirement:** Add `/robots.txt` as a plain root file:

```text
User-agent: *
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

Sitemap: https://nikgo.com/sitemap.xml
```

Do not add crawler names merely to create SEO theater. The explicit OpenAI entries document the desired policy, while `User-agent: *` already allows other crawlers. Decide separately whether model-training crawlers such as GPTBot should be allowed. OpenAI distinguishes search discovery from model training; blocking GPTBot should not require blocking OAI-SearchBot. Record that policy decision in the repository.

**Acceptance criteria:**

- `/robots.txt` returns 200 and `text/plain`.
- It references exactly the canonical HTTPS sitemap.
- It does not disallow `/assets/`, article content, CSS, JavaScript, or images.
- OAI-SearchBot and major search crawlers receive content without Cloudflare challenges.

### P0-2: Generate and submit a canonical XML sitemap

**Finding:** `/sitemap.xml` returns 404.

**Requirement:** Enable the GitHub Pages-supported `jekyll-sitemap` plugin and include only canonical, indexable HTML pages and the canonical PDF if it is intended to rank independently. Do not include raw `.md` URLs, alternate drafts, `__no_ref` files, test pages, asset files, or redirect stubs.

Recommended `_config.yml` addition:

```yaml
plugins:
  - jekyll-seo-tag
  - jekyll-sitemap
  - jekyll-redirect-from
```

`jekyll-seo-tag` already runs through the theme stack, but listing it makes the dependency explicit. Confirm all plugin versions against [GitHub Pages dependency versions](https://pages.github.com/versions/).

**Acceptance criteria:**

- `/sitemap.xml` returns 200 and valid XML.
- Every URL is absolute, HTTPS, canonical, and returns 200.
- No sitemap URL is redirected, noindexed, duplicated, or a raw source file.
- The sitemap is submitted and processed without errors in Google Search Console and Bing Webmaster Tools.
- `lastmod` is emitted only when it reflects a real, significant content update.

### P0-3: Eliminate raw Markdown duplicates

**Finding:** An article is accessible both as rendered HTML and raw Markdown, for example:

- `/pages/articles/your_ai_career_plan.html`
- `/pages/articles/your_ai_career_plan.md`

Both return 200. The Markdown response has no HTML canonical element. Google explicitly states that the existence of machine-readable or Markdown files provides no special generative-search benefit. Raw Markdown is therefore a duplicate representation and not an `llms.txt` substitute.

**Preferred implementation:** Move publishable article source into a Jekyll collection whose source directory begins with an underscore, for example `_articles/`. Configure `output: true` and a clean permalink. Jekyll source files under the collection directory will not be copied as public static Markdown.

```yaml
collections:
  articles:
    output: true
    permalink: /articles/:slug/

defaults:
  - scope:
      path: ""
      type: articles
    values:
      layout: article
      author: dominik-gorecki
      sitemap: true
```

If a collection migration is deferred, the deployment pipeline must explicitly exclude source Markdown while still generating HTML. Do not use `robots.txt` as a canonicalization mechanism.

### P0-4: Resolve every alternate, draft, and orphan URL

**Finding:** Eight article candidates are absent from the article index, and several substantially overlap listed articles:

- `Rokos_Symbiotic_Carrot__no_ref.md`
- `Why_Office_Agents_Shouldnt_Live_in_a_Shell__no_ref.md`
- `wrong_kind_of_smart__no_ref.md`
- `ai_in_the_veins_v1.md`
- `ai_in_the_veins_v2.md`
- `ai_in_the_veins_v3.md`
- `what_freedom_for.md` while `what_freedom_for__v2.md` is the linked version
- `ai_public_opinion_cliff.md`

**Requirement:** Create an editorial disposition sheet before migration:

| Status | Action |
|---|---|
| Canonical published article | Keep one URL, merge any unique useful material, add full metadata. |
| Superseded version with external history | 301/308 redirect to the canonical article. |
| Unpublished draft with no public value | Exclude from build; allow old URL to return 404/410. |
| Distinct article accidentally omitted | Publish intentionally with metadata and add it to the appropriate hub/index. |
| “No references” derivative | Remove from production; never make citation-stripped copies indexable. |

Do not canonicalize meaningfully different articles to one another merely because their topic is similar. Canonicals are for duplicate or near-duplicate representations. When consolidating, preserve the strongest copy and redirect old URLs.

### P0-5: Remove non-content from the deployment

**Finding:** `/b/test.html` is a live default Jekyll test page. Seven tracked source or operating-system artifacts are also deployment candidates, and representative URLs return 200.

**Requirement:**

- Remove the test post from production.
- Remove or exclude `.af`, lock, `Zone.Identifier`, and other source artifacts.
- Add repository ignore rules for `*.af`, `*.af~lock~*`, `*:Zone.Identifier`, and editor/OS temp files as appropriate.
- Keep editable originals outside the public Jekyll source tree if they must remain versioned.
- Add a branded `404.html` with navigation and search/topic links, while preserving the real 404 status.

**Acceptance criteria:** known artifact and test URLs return 404/410, not 200 and not a blanket redirect to the homepage.

### P1-6: Standardize the domain and redirects

**Finding:** `http://nikgo.com/` redirects to `https://nikgo.com/`. `https://www.nikgo.com/` currently redirects first to `http://nikgo.com/`, which then redirects to HTTPS. This creates an unnecessary two-hop chain.

**Requirement:** Configure Cloudflare so every noncanonical variant redirects in one permanent hop to the equivalent path on `https://nikgo.com/`.

Examples:

- `http://nikgo.com/a` → `https://nikgo.com/a`
- `http://www.nikgo.com/a` → `https://nikgo.com/a`
- `https://www.nikgo.com/a` → `https://nikgo.com/a`

Preserve paths and query strings. Do not redirect every missing URL to the homepage.

---

## 5.2 Site configuration and canonical metadata

### P0-7: Define the site identity explicitly

**Finding:** `_config.yml` contains only `theme: jekyll-theme-cayman`. Jekyll SEO output therefore relies on inferred GitHub metadata. This produces the observed HTTPS canonical but HTTP Open Graph/JSON-LD inconsistency and a generic lowercase site identity.

**Requirement:** Define canonical site metadata directly:

```yaml
title: "nikGo"
tagline: "Engineering, AI, and Cognition"
description: "Original research and essays by engineering leader Dominik Gorecki on agentic software delivery, RAG systems, AI strategy, and cognition."
url: "https://nikgo.com"
baseurl: ""
lang: "en-US" # Confirm the author's intended language/locale before finalizing.

author:
  name: "Dominik Gorecki"
  url: "https://nikgo.com/about/"

logo: "/assets/images/profile_pic.png"

social:
  name: "Dominik Gorecki"
  links:
    - "https://www.linkedin.com/in/nikgo"
    - "https://github.com/DominikGorecki"
```

The actual description should be editorially approved, not copied blindly. Use one consistent capitalization for `nikGo`. Update the README's `nikgo.me` heading to the actual `nikgo.com` domain to remove operational ambiguity.

### P0-8: Give every indexable page explicit front matter

**Finding:** GitHub Pages' `jekyll-optional-front-matter` and `jekyll-titles-from-headings` plugins render the current Markdown without explicit front matter. Inferred titles fail whenever an image appears before the H1. That explains why half the live articles have the title `nikgo` while others inherit their first heading.

**Requirement:** Every published article must have an explicit metadata contract:

```yaml
---
layout: article
title: "Your Company’s AI Rollout Is Not Your Career Plan"
description: "Why access to a corporate AI assistant is not a substitute for deliberate practice, portable judgment, and a personal AI workflow."
slug: "company-ai-rollout-career-plan"
date: 2026-04-15
last_modified_at: 2026-08-11
author: dominik-gorecki
category: agentic-engineering
tags:
  - AI-assisted software development
  - engineering careers
  - agentic engineering
image:
  path: /assets/articles/company-ai-rollout-career-plan/cover-16x9.webp
  alt: "An engineer developing a portable AI practice beyond a company-provided assistant"
  width: 1280
  height: 720
canonical_url: https://nikgo.com/articles/company-ai-rollout-career-plan/
status: published
---
```

Rules:

- `title`, `description`, `date`, `author`, `image`, `category`, and `status` are required.
- `last_modified_at` changes only after a material editorial update, not on every build.
- Dates on the visible page and in JSON-LD must match.
- Do not infer publication dates solely from Git commits if the original publication history differs. Reconstruct and document the authoritative dates.
- Use a single editorial title. A shorter `seo_title` may be permitted when the display title is unusually long, but it must remain accurate.
- `canonical_url` can be generated from `site.url` and `page.url`; storing it manually is optional and risks drift. Prefer generation unless cross-domain canonicalization is intentional.
- Drafts must use `published: false` or live outside the publishable collection.

### P0-9: Make titles and descriptions unique

**Requirement:**

- Home title: communicate both person and subject, for example `Dominik Gorecki — Engineering, AI, and Cognition`.
- Articles index: `Articles on Agentic Engineering, RAG, and AI | Dominik Gorecki`.
- Projects: `Engineering and AI Projects | Dominik Gorecki`.
- Article pattern: `[Article title] | Dominik Gorecki` unless the title becomes unreasonably long; do not append redundant terms mechanically.
- Meta descriptions should summarize the specific thesis and likely reader value. They are snippet suggestions, not keyword containers.
- Do not use the same description on multiple pages.

No fixed character limit guarantees display, but titles should front-load the identifying subject and descriptions should usually fit a concise one- or two-sentence summary. Validate real rendering rather than optimizing to an arbitrary counter.

### P0-10: Fix URL schemes across all metadata

**Finding:** Representative live pages emit:

- HTTPS in `<link rel="canonical">`
- HTTP in `og:url`
- HTTP in `og:image`
- HTTP in JSON-LD `url`

**Requirement:** All canonical, Open Graph, Twitter, JSON-LD, sitemap, feed, and internal absolute URLs must use `https://nikgo.com`. Add a build assertion that fails on `http://nikgo.com` in generated HTML/XML.

---

## 5.3 Semantic HTML and page templates

### P0-11: Create a dedicated article layout

**Finding:** Every page uses the same generic layout. Articles receive no semantic header, byline, publication details, breadcrumbs, or related content.

**Requirement:** Add `_layouts/article.html`, inheriting from the default shell if useful. It should render:

1. Breadcrumbs: Home → Articles → Topic → Article.
2. One visible article H1.
3. A concise deck/description.
4. Author link, published date, and material update date.
5. Representative image with dimensions and descriptive alternative text.
6. Optional table of contents for long papers.
7. Article body in `<article>`.
8. A short, visible author bio linked to `/about/`.
9. “Related reading” selected by topic and intent, not random recency.
10. Citation/share metadata where relevant.

### P0-12: Use exactly one primary H1

**Finding:** The site-wide hero uses `<h1 class="hero-title">nikGo</h1>` and page content normally adds another H1.

**Requirement:** Replace the global brand H1 with an appropriate non-heading element or make the brand an accessible linked logo. The page title must be the only H1. Use H2/H3 hierarchy for article sections without skipping levels for styling.

### P1-13: Make navigation and controls semantic

**Finding:** Homepage feature cards are clickable `<div>` elements with inline `onclick`. They are not real links, are not keyboard-native, and offer little to browser agents or crawlers as navigation.

**Requirement:** Use `<a>` for navigation and `<button>` only for actions. Add a labeled primary `<nav>`, a skip link, visible focus styles, and meaningful ARIA only where native semantics are insufficient. This improves accessibility and also makes browser-agent intent easier to interpret. OpenAI explicitly notes that accessible labels, roles, and states help agent understanding.

### P1-14: Improve the article index semantics

Replace the manually duplicated card/list content with collection-driven templates. One metadata record should generate:

- Article page metadata.
- Article card.
- “All Articles” list entry.
- Sitemap record.
- Feed record if enabled.
- Related-content and topic hub associations.

Use `<ol>` or `<ul>` of `<article>` summaries, visible dates in `<time datetime="…">`, and real canonical links. Add filtering only if it works without hiding the base crawlable list.

---

## 5.4 Structured data and entity design

Structured data does not create authority by itself and does not guarantee rich results. Its purpose here is to make the site's real entities and editorial facts unambiguous.

### P0-15: Define one reusable entity graph

Use stable `@id` values across pages:

```text
https://nikgo.com/#website
https://nikgo.com/about/#person
https://nikgo.com/articles/example/#article
https://nikgo.com/articles/example/#breadcrumb
```

### Homepage graph

Include:

- `WebSite` with name, alternateName if appropriate, URL, description, and publisher/creator.
- `ProfilePage` whose `mainEntity` is `Person`.
- `Person` for Dominik Gorecki with name, URL, image, jobTitle, short description, `knowsAbout`, and verified `sameAs` profiles.

Do not add unverifiable affiliations, awards, credentials, or knowledge claims merely for SEO.

### Article graph

Use `BlogPosting` or `Article` as appropriate:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "@id": "https://nikgo.com/articles/example/#article",
      "mainEntityOfPage": "https://nikgo.com/articles/example/",
      "headline": "Example title",
      "description": "Example description",
      "datePublished": "2026-04-15",
      "dateModified": "2026-08-11",
      "image": {
        "@type": "ImageObject",
        "url": "https://nikgo.com/assets/articles/example/cover-16x9.webp",
        "width": 1280,
        "height": 720
      },
      "author": { "@id": "https://nikgo.com/about/#person" },
      "isPartOf": { "@id": "https://nikgo.com/#website" },
      "keywords": ["agentic engineering", "software delivery"],
      "inLanguage": "en-US"
    }
  ]
}
```

Add a `BreadcrumbList` matching visible breadcrumbs. For research papers, use `ScholarlyArticle` where the page genuinely has scholarly structure, while retaining the properties expected for an article. Add `abstract`, `citation`, `isBasedOn`, `encoding` for a PDF, and dataset links only when they truthfully exist.

### Project and collection pages

- `/articles/`: `CollectionPage` plus an `ItemList` of canonical articles.
- Topic hubs: `CollectionPage` with `about` pointing to the relevant concept entity.
- `/projects/`: `CollectionPage`/`ItemList`; only use `SoftwareApplication` for projects that meet the type and have accurate properties.

### Validation

- Validate Article and Breadcrumb markup in Google's Rich Results Test.
- Validate the complete graph in Schema.org's validator.
- Confirm structured facts are visible and consistent with the page.
- Add a generated-build test that parses every JSON-LD block.

### Do not implement

- Fake reviews, ratings, citations, or organization data.
- FAQ markup on prose that is not a visible FAQ.
- `Speakable` or other schema merely because it exists.
- Multiple conflicting author or canonical objects.
- `llms.txt` as a substitute for crawlability, content quality, sitemap, or structured data. Google's current guidance explicitly says it does not use `llms.txt` or special AI markup for Search.

---

## 5.5 Content architecture and internal linking

### P1-16: Build three primary topic hubs

The existing corpus naturally supports three authority clusters. Create stable hub pages with an original introduction, key definitions, a recommended reading path, and annotated links.

#### Hub A: Agentic engineering and AI-enabled organizations

Candidate path: `/topics/agentic-engineering/`

Include:

- The 90 Percent Problem of Agentic Software Delivery
- The Vibe Trap
- The Companies That OODA Faster
- Why Office Agents Shouldn't Live in a Shell
- Bring Your Own AI, Bring Your Own Leverage
- Your Company's AI Rollout Is Not Your Career Plan
- The Market for Portable Minds
- The Wrong Kind of Smart
- AI Tokenomics for Software Engineering

#### Hub B: Retrieval-augmented generation research

Candidate path: `/topics/rag-research/`

Include:

- RAG as a Capability Multiplier
- Small RAG Beats Large Search
- The Dose-Response Curve of RAG
- AI Tokenomics where model routing/evaluation overlaps
- Relevant project links to VulcLab, with clear disclosure of the relationship

This is the strongest near-term topical authority opportunity because the corpus includes experiments, quantitative results, figures, limitations, and reproducible claims.

#### Hub C: AI, cognition, and society

Candidate path: `/topics/ai-cognition-society/`

Include:

- Attention Is Fundamental
- AI After the Outrage Machine
- What Freedom Is For
- Medicine's Dead Time
- Roko's Symbiotic Carrot
- The 2028 Intelligence Explosion
- The Great AI Pink-Slip Panic
- AI's Public-Opinion Cliff, if intentionally published

### P1-17: Add deliberate internal-link rules

Every article should have:

- One link to its topic hub.
- Two to four contextual links from body text to closely related articles.
- Two to four related-reading links after the article.
- One author link.
- Breadcrumb links.

Every new article should receive links from at least two older relevant pages during publication. Use descriptive anchor text that states the concept, not repeated “read more.” Do not force links where the relationship is weak.

### P1-18: Create a real author/about page

The homepage currently provides a short biography but not a durable author entity. Create `/about/` with:

- Full name and consistent headshot.
- Current role stated at an appropriate level of specificity.
- Areas of demonstrated expertise.
- Selected projects/publications.
- Links to GitHub, LinkedIn, and any other verified profiles.
- Editorial approach, research methods, and correction/update policy.
- Contact or professional inquiry path if desired.

Link the byline on every article to this page. Use `ProfilePage` and `Person` structured data. The goal is not keyword repetition; it is a coherent, verifiable identity.

---

## 5.6 GEO: making content easy to retrieve and cite

Generative engine optimization should be treated as **retrieval eligibility + source quality + answer extraction + entity confidence + measurement**. It is not a separate trick layer over SEO. Google states that its generative search experiences use core Search ranking and retrieval systems, and specifically advises against special “GEO hacks,” forced chunking, unnecessary AI text files, and writing only for machines.

### P1-19: Add an answerable opening to each article

Preserve the narrative voice, but give readers and retrieval systems a clear orientation near the top. After the title/deck, add one of:

- A two- to four-sentence thesis.
- “In brief” with three concrete takeaways.
- An abstract for research work.
- A definition block when introducing original terminology.

The opening should answer:

1. What question does this page address?
2. What is the author's answer?
3. What evidence or reasoning supports it?
4. For whom is the conclusion useful?

Do not turn every paragraph into disconnected “chunks.” Cohesive argument and originality remain more important.

### P1-20: Make original claims explicit and attributable

For each article, identify three to seven claims worth citing. Express them in clear prose, then immediately provide the evidence, boundary, or reasoning. Examples from the existing corpus might include model-routing economics, RAG experiment outcomes, the distinction between code generation and delivery, or the ownership layers of portable context.

Use a visible pattern such as:

```markdown
## Key finding

In this experiment, the domain-specific RAG condition outperformed the comparison condition on four of five judged dimensions. The coherence difference was not statistically significant.

**Method:** …  
**Sample:** …  
**Limitations:** …  
**Data/figures:** …
```

This is both human-friendly and citation-friendly because the claim is adjacent to provenance and qualification.

### P1-21: Strengthen research-paper provenance

For the three RAG research articles and AI tokenomics paper:

- Add named author, publication date, revision date, and version.
- Add an abstract and plain-language executive summary.
- Publish downloadable methodology, prompt/evaluation protocol, anonymized data, and code when legally and ethically possible.
- Add a “How to cite” section with a stable canonical URL; optionally provide BibTeX.
- State conflicts or product relationships, especially where VulcLab is discussed.
- State sample size, model version, evaluation date, statistical test, uncertainty, and limitations near the result.
- Use stable figure filenames, captions, and surrounding explanatory text.
- If the PDF duplicates a full HTML paper, choose which should be canonical and send an HTTP `Link: <…>; rel="canonical"` header for the PDF if the hosting stack supports it. Otherwise provide clear cross-links and avoid duplicating the entire work unnecessarily.

Original datasets and transparent methods are more defensible GEO assets than generic summaries because answer systems have a reason to cite the originator.

### P1-22: Clarify terms and entities

Create concise, consistent definitions for recurring concepts:

- Agentic engineering
- OODA velocity
- Company Context Bank
- Portable minds / portable context
- Total expected cost of completion
- RAG dose-response curve
- Leisure literacy

Define a term once on the most authoritative page, link back to that definition from related articles, and avoid changing the meaning between pages. A glossary may be useful after at least ten recurring terms exist, but it should not become a collection of thin definition pages.

### P1-23: Use evidence-rich formats where they improve comprehension

Appropriate formats include:

- Comparison tables with explicit dimensions.
- Decision trees and checklists for engineering leaders.
- Result tables with units, sample sizes, and uncertainty.
- Short timelines where chronology matters.
- Diagrams that have equivalent text explanations and useful alt text.
- Visible source notes and descriptive reference titles.

Bing's current AI visibility guidance specifically recommends clear headings, tables, evidence, freshness, and consistent representation across formats. Use these because they improve comprehension, not because a table is a magic citation trigger.

### P2-24: Create genuinely useful query-targeted companion pages

The long essays often address several questions at once. After Search Console/Bing data reveals demand, create focused companion resources that solve a distinct intent and link to the long-form argument. Examples:

- “How to measure the total cost of an AI coding task”
- “RAG evaluation checklist for small teams”
- “Agentic software delivery maturity model”
- “Context Bank architecture: components and governance”
- “When should a smaller model with RAG beat a larger model?”

Each page must add a tool, model, example, calculation, or decision framework. Do not mass-produce paraphrased keyword variations.

### P2-25: Earn corroboration outside the site

Entity and citation confidence also depends on the wider web. Prioritize legitimate distribution:

- Publish experiment code/data in a linked GitHub repository.
- Create canonical project documentation that references the research appropriately.
- Submit technical talks, podcasts, or guest essays where the work fits.
- Encourage references to the canonical article, not alternate copies.
- If content is syndicated, require an explicit canonical link to nikgo.com when the publisher supports it.
- Maintain consistent name, bio, and profile URLs across GitHub, LinkedIn, project sites, and speaker profiles.

Do not purchase links, manufacture mentions, or create fake profiles.

---

## 5.7 Images, social presentation, and Discover

### P1-26: Standardize article cover assets

**Finding:** Most key article images are 800×450. Google's Discover guidance recommends compelling images at least 1,200 pixels wide and enabling large previews.

**Requirement:** For each canonical article, create at minimum:

- 1280×720 or larger 16:9 WebP/AVIF cover.
- 4:3 and 1:1 crops for Article structured data where practical.
- Descriptive filename and alt text.
- Explicit width and height.
- `og:image`, `twitter:image`, and schema `image` using HTTPS absolute URLs.
- `twitter:card` set to `summary_large_image` for articles with qualifying artwork.
- `<meta name="robots" content="max-image-preview:large">` unless there is a rights reason not to allow it.

Do not use decorative phrases such as “banner” as the only alt text. Describe the meaningful visual content or use empty alt text for purely decorative duplicates.

### P1-27: Add image loading rules

- Do not lazy-load the likely LCP image.
- Add `fetchpriority="high"` only to the true above-the-fold LCP image after measurement.
- Use `loading="lazy"` and `decoding="async"` for below-the-fold figures.
- Add `width` and `height` to prevent layout shift.
- Use `<figure>` and `<figcaption>` for research figures.
- Ensure every figure is explained in nearby text; answer engines cannot rely on chart pixels alone.

### P2-28: Add image provenance

If images are AI-generated or materially edited, add a concise disclosure policy and preserve appropriate metadata where useful. For original charts, state the data source and creator. Add image licensing metadata only when an actual license and rights page exist.

---

## 5.8 Performance and experience

### P1-29: Reduce global page weight

Confirmed opportunities:

- Convert and resize the 1.6 MB `rainbow-nebula.jpg`; provide responsive variants and target a much smaller transfer size.
- Resize the 880 KB profile PNG to the maximum rendered dimensions, with a high-density variant if needed.
- Remove jQuery 3.6.0 because `assets/js/main.js` uses no jQuery API.
- Remove the duplicate Google Fonts declaration from either the layout or CSS import. Prefer a single non-`@import` stylesheet request, or self-host a deliberately limited font subset.
- Convert multi-hundred-kilobyte and multi-megabyte PNG article images to optimized WebP/AVIF while preserving readable chart text.
- Keep editable Affinity files entirely out of the public build.
- Set long-lived immutable caching for content-hashed/static assets where Cloudflare and GitHub Pages configuration permits it.

### P1-30: Make animation resilient

`main.js` sets every direct content child to `opacity: 0` after DOM ready and reveals it through `IntersectionObserver`. This is unnecessary for primary reading content and creates a failure mode where content remains visually hidden if observation or animation fails.

Requirements:

- Primary article text should be visible by default.
- Apply animation only when a progressive-enhancement class is active.
- Respect `prefers-reduced-motion`.
- Avoid animating every paragraph in long articles.
- Use passive scroll listeners or consolidate the two current scroll handlers after profiling.

### Performance targets

Measure representative home, index, short article, and long research-paper templates. At the 75th percentile of real visits, target the current “good” Core Web Vitals thresholds:

- LCP ≤ 2.5 seconds.
- INP ≤ 200 ms.
- CLS ≤ 0.1.

Also set project budgets:

- No uncompressed source/design artifacts in production.
- No article cover larger than necessary for its display and social purpose.
- Zero unused global JavaScript libraries.
- No layout shift caused by authored images.

These are acceptance goals, not claims about the current field performance.

---

## 5.9 Trust, transparency, and editorial operations

### P1-31: Publish editorial signals

Add concise pages or sections for:

- About/author.
- Contact.
- Editorial and AI-assistance policy.
- Corrections and material-update policy.
- Privacy policy if analytics or data collection is introduced.

The AI policy should reflect reality. It can describe research, drafting, editing, image generation, or verification workflows without making performative claims. For technical papers, distinguish author analysis from model-generated experimental outputs.

### P1-32: Add publication QA

Before any article becomes indexable, require:

- Editorial title and description.
- Unique canonical slug.
- Author and dates.
- Category/tags.
- Cover image with dimensions and alt text.
- One H1 and valid heading order.
- At least two internal links in and two links from existing content.
- Checked external references.
- Visible thesis/abstract.
- Relevant limitations/disclosures.
- Valid JSON-LD.
- Sitemap inclusion.
- Social preview validation.

---

## 6. Recommended repository design

This is the preferred end state, not a requirement to rename everything in one risky commit.

```text
/
├── _articles/
│   ├── company-ai-rollout-career-plan.md
│   ├── rag-capability-multiplier.md
│   └── ...
├── _data/
│   ├── authors.yml
│   └── redirects.yml
├── _includes/
│   ├── head-meta.html
│   ├── jsonld.html
│   ├── article-card.html
│   ├── breadcrumbs.html
│   └── related-articles.html
├── _layouts/
│   ├── default.html
│   ├── article.html
│   ├── topic.html
│   └── profile.html
├── assets/
│   ├── articles/<slug>/...
│   ├── css/
│   └── js/
├── pages/
│   ├── about.md
│   ├── articles.md
│   ├── projects.md
│   └── topics/
├── 404.html
├── robots.txt
├── _config.yml
└── Gemfile
```

### 6.1 Build and deployment

GitHub now recommends GitHub Actions for deploying and automating GitHub Pages, although the `github-pages` gem remains supported. A custom Actions build is preferable if it is needed to:

- Enforce metadata schema.
- Generate redirects reliably.
- Run HTML/link/schema tests.
- Prevent source artifacts from publishing.
- Run Lighthouse or asset budgets.
- Generate canonical headers for non-HTML resources through a more capable hosting layer.

If branch-based GitHub Pages is retained, use only supported plugins and keep the first implementation conservative.

### 6.2 URL strategy

Preferred new article URLs:

```text
https://nikgo.com/articles/company-ai-rollout-career-plan/
https://nikgo.com/articles/rag-capability-multiplier/
```

Benefits are human readability, lower case, no `.html`, no underscores, and a stable information hierarchy. URL keywords alone are not a reason to disrupt working URLs, so migration must be controlled.

For every changed URL:

1. Map exactly one old URL to one canonical new URL.
2. Use a permanent server-side redirect where possible.
3. Update all internal links, sitemap entries, canonicals, Open Graph URLs, and structured data.
4. Preserve query strings.
5. Keep redirects indefinitely.
6. Test for chains and loops.
7. Request recrawl for priority URLs in Search Console/Bing.

If reliable redirects cannot be implemented on the current stack, keep existing HTML paths for published articles during phase one and clean the URL structure only after the deployment mechanism supports it.

---

## 7. Implementation plan

### Phase 0: Baseline and editorial decisions — 0.5–1 day

| Task | Owner | Output |
|---|---|---|
| Export Google Search Console and Bing Webmaster baselines | Site owner | Indexed pages, queries, impressions, clicks, canonicals, crawl errors, AI citations |
| Decide canonical version/status for all 26 article files | Author/editor | Content disposition sheet |
| Confirm actual publication and modification dates | Author/editor | Authoritative date inventory |
| Decide search-vs-training crawler policy | Site owner | Documented robots policy |
| Choose whether current URLs stay or migrate | Engineering + owner | URL map and redirect feasibility decision |

### Phase 1: Critical technical repair — 2–4 days

1. Expand `_config.yml` with URL, site identity, author, language, and plugins.
2. Add explicit front matter to every published page.
3. Add article layout and unique metadata.
4. Remove the global duplicate H1.
5. Add HTTPS-consistent canonical, Open Graph, Twitter, and JSON-LD output.
6. Add robots and sitemap.
7. Exclude/remove raw Markdown, drafts, alternates, test post, and artifact files.
8. Add redirects or preserve existing HTML URLs until redirects are reliable.
9. Add a custom 404.

### Phase 2: Entity and content architecture — 3–5 days

1. Create author/about page and Person/ProfilePage graph.
2. Create three topic hubs.
3. Generate article index and related links from front matter.
4. Add breadcrumbs and BreadcrumbList.
5. Correct author spelling and normalize dates/categories.
6. Add bylines, visible dates, author bios, and editorial disclosures.

### Phase 3: GEO and research upgrades — ongoing, start with 3–5 highest-value pages

Priority page order:

1. RAG as a Capability Multiplier.
2. Small RAG Beats Large Search.
3. The Dose-Response Curve of RAG.
4. The 90 Percent Problem of Agentic Software Delivery.
5. The Companies That OODA Faster or The Market for Portable Minds.

For each, add answer-first orientation, explicit findings, provenance, limitations, citation instructions, related links, and large imagery. Use the measured response before rolling the format across every essay.

### Phase 4: Performance and automation — 2–4 days

1. Optimize global hero and profile assets.
2. Remove jQuery and duplicate font declarations.
3. Add image dimensions/lazy-loading policy.
4. Make animations progressive and reduced-motion-safe.
5. Add CI checks and asset budgets.
6. Validate mobile templates and Core Web Vitals.

### Phase 5: Distribution and iteration — monthly

1. Review Google generative AI/Search performance and Bing AI citations.
2. Update decaying or superseded technical claims.
3. Publish query-informed companion resources only when they add original value.
4. Earn relevant external references through data, tools, talks, and collaborations.
5. Audit duplicates, broken links, schema, and crawl logs quarterly.

---

## 8. Measurement plan

### 8.1 Establish the baseline before deployment

Record a 90-day and 16-month view where available:

- Google indexed pages and excluded reasons.
- Google impressions, clicks, CTR, and average position by query/page/country/device.
- Google generative AI performance report metrics, if available in the property.
- Bing indexed pages, search clicks, keywords, and crawl health.
- Bing AI Performance: total citations, average cited pages, cited URLs, grounding-query samples, and trends.
- Organic referrals from `google`, `bing`, `chatgpt.com`, `perplexity`, `copilot`, `gemini`, and other observable sources.
- Referring domains and backlinks to each canonical article.
- Engaged reading: scroll depth or completion proxy, related-article clicks, and project/contact conversions.
- Core Web Vitals by template and device.

ChatGPT adds `utm_source=chatgpt.com` to search referral URLs according to OpenAI's publisher guidance. Preserve UTM parameters through redirects and group them in analytics.

### 8.2 KPI hierarchy

#### Leading technical indicators

- 100% of indexable pages have unique titles/descriptions and HTTPS self-canonicals.
- 100% of articles have valid Article/BlogPosting schema, author, and dates.
- 0 raw Markdown, drafts, test pages, or design artifacts in the indexable build.
- 0 redirect chains and 0 sitemap errors.
- 100% of priority URLs indexed as the declared canonical.
- All major templates pass field Core Web Vitals at p75 when enough data exists.

#### Search outcomes

- Growth in non-brand impressions and clicks to articles.
- More distinct queries per topic hub.
- Improved CTR on pages whose positions remain comparable.
- Increased indexed/crawled ratio for canonical URLs.
- Increased backlinks to research pages and original frameworks.

#### GEO outcomes

- Growth in Bing AI citations and unique cited pages.
- Growth in generative grounding queries associated with the three topic clusters.
- Growth in AI referral sessions and assisted conversions.
- A repeatable manual benchmark: test 20–30 stable questions monthly across major answer engines and log whether nikgo.com is cited, which URL is cited, and whether the claim is represented accurately.

Do not interpret one manually prompted answer as a ranking report. Keep prompts, location, account state, date, model, and methodology consistent enough to observe direction rather than anecdotes.

### 8.3 Suggested 90-day targets

Targets should be finalized after the baseline. Reasonable implementation targets are:

- Week 2: all P0 technical acceptance tests pass.
- Week 4: priority canonical URLs are submitted and major crawlers have revisited them.
- Day 45: all three hubs and the author entity are live.
- Day 60: five priority pages receive full GEO/editorial upgrades.
- Day 90: compare indexed URLs, non-brand impressions, cited pages, AI referrals, and CTR against the pre-change baseline.

Avoid promising a fixed traffic percentage before baseline demand, competition, and index state are known.

---

## 9. Automated acceptance tests

Add CI that fails the build when any of these conditions occurs:

### Metadata

- Missing or duplicate `<title>` among indexable pages.
- Title equal to generic `nikgo` on any article.
- Missing/empty meta description.
- More or fewer than one H1 on primary pages.
- Missing HTTPS self-canonical.
- Any generated `http://nikgo.com` URL.
- Missing `og:title`, `og:description`, `og:url`, and article image.

### Structured data

- Invalid JSON-LD.
- Article without `headline`, `description`, `author`, `datePublished`, `dateModified` where applicable, `image`, or `mainEntityOfPage`.
- Structured author not linked to the stable Person `@id`.
- Schema values that disagree with visible content.

### Crawl and links

- Broken internal link or image.
- Redirect URL in sitemap.
- Non-200 canonical URL.
- Raw `.md`, `__no_ref`, version draft, test, `.af`, lock, or `Zone.Identifier` file in output.
- Orphan published article with no index/hub link.
- Sitemap URL not represented by a canonical page.

### Performance and accessibility

- Image without width/height or meaningful alt handling.
- Global JavaScript dependency not used by the codebase.
- Lighthouse regression beyond the agreed budget on representative templates.
- Keyboard-inaccessible navigation controls.
- Motion that ignores `prefers-reduced-motion`.

Suggested tools include Jekyll build validation, HTMLProofer or equivalent, a JSON-LD parser, a link checker, Lighthouse CI, and targeted template assertions. Pin versions and run the same checks on pull requests and production URLs after deployment.

---

## 10. Definition of done

The foundational SEO/GEO project is complete when:

1. Each published idea has one canonical HTML URL.
2. Raw Markdown, drafts, superseded copies, test pages, and source artifacts are not publicly indexable.
3. Robots and sitemap files return 200 and express the intended policy.
4. Every indexable page has an explicit unique title, description, HTTPS canonical, social metadata, and one H1.
5. Every article shows accurate author and date information and emits valid Article-family structured data.
6. The homepage and about page define one consistent Person/WebSite entity graph.
7. All articles belong to a topic hub and have contextual internal links.
8. Priority articles expose their thesis, evidence, limitations, and provenance clearly enough to cite accurately.
9. Representative images qualify for large previews and do not cause layout shift.
10. Domain variants resolve to the canonical HTTPS URL in one hop.
11. Search Console and Bing Webmaster Tools process the sitemap without critical errors.
12. Technical, search, and AI citation baselines are recorded and reviewed on a schedule.
13. CI prevents recurrence of the defects found in this audit.

---

## 11. Risks and trade-offs

### URL migration risk

Clean URLs are desirable but not worth losing existing links or citations. If redirects cannot be guaranteed, preserve current HTML URLs in phase one. Never change article URLs casually after publication.

### Over-optimization risk

The site's strongest advantage is an identifiable authorial voice. Answer summaries, tables, and definitions should orient the reader, not convert every essay into templated SEO prose. Apply more structure to research and how-to content than to reflective essays.

### Freshness risk

Many pages make time-sensitive claims about current models, companies, markets, and regulation. Add update dates only after factual review. A recent date attached to stale content reduces trust.

### Medical and high-stakes content risk

“Medicine's Dead Time” discusses regulatory and health-related policy. It should retain strong primary sourcing, distinguish argument from medical advice, disclose author qualifications accurately, and receive more frequent factual review than an opinion essay about leisure.

### Schema drift risk

Hand-authored JSON-LD across dozens of pages will drift. Generate it from the same front matter used for visible bylines, cards, and sitemap data.

### Crawler-control risk

Search inclusion and model training are separate policy decisions. Do not block a search crawler unintentionally while trying to opt out of training. Re-check vendor documentation periodically because bot names and behavior can change.

### Measurement risk

AI referrals are undercounted when users do not click citations, and manual answer tests are variable. Use multiple indicators—citations, cited pages, grounding queries, referrals, backlinks, and conventional search performance—rather than one vanity metric.

---

## 12. Primary references

These sources support the implementation approach and should be rechecked during implementation because search and crawler guidance changes.

- [Google: Optimizing a website for generative AI features on Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google: Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google: Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google: Canonical URL methods and duplicate consolidation](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google: Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article)
- [Google: Publication and modification dates](https://developers.google.com/search/docs/appearance/publication-dates)
- [Google: Discover and large-image guidance](https://developers.google.com/search/docs/appearance/google-discover)
- [Google: Image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)
- [Google: Generative AI content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- [OpenAI: Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)
- [OpenAI: ChatGPT search](https://help.openai.com/en/articles/9237897-chatgpt-search)
- [Bing: AI Performance in Webmaster Tools](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- [Bing: Duplicate content and AI search visibility](https://blogs.bing.com/webmaster/December-2025/Does-Duplicate-Content-Hurt-SEO-and-AI-Search-Visibility)
- [Bing: IndexNow](https://www.bing.com/webmasters/help/indexnow-0z209wby)
- [GitHub: GitHub Pages and Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)
- [GitHub Pages: Dependency versions](https://pages.github.com/versions/)
- [web.dev: Core Web Vitals and current thresholds](https://web.dev/articles/vitals)

---

## 13. Final recommendation

Treat this as a publishing-system repair followed by an authority-building program. The immediate bottleneck is not a lack of keywords or content volume. It is that the site does not consistently tell crawlers which pages are authoritative, what each article is called, who wrote it, when it was published, or how it relates to the rest of the corpus.

Fix those fundamentals first. Then concentrate the existing research and essays into three explicit domains of expertise, strengthen the provenance of the RAG work, and use measured query/citation data to decide which companion resources deserve creation. That approach improves classic SEO and generative visibility for the same underlying reason: it makes nikgo.com a clearer, more trustworthy, more retrievable source.
