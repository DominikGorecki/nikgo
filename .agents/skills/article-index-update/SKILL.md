---
name: article-index-update
description: Update pages/articles.md for a newly published article or white paper, adding the correct category card and latest All Articles entry.
---

# Article Index Update

## Use When

Use this skill when the user gives a new article markdown or PDF path, such as `pages/articles/medicines_dead_time.md`, and wants it added to `pages/articles.md`.

## Inputs

- Article file path. Usually `pages/articles/<slug>.md`; occasionally a PDF under `pages/articles/`.
- Index file. Default: `pages/articles.md`.
- Update date. Default: today's date in the user's/project timezone.

## Workflow

1. Inspect the article and index.
   - Read the target article title, opening sections, and any top image markdown.
   - Read `pages/articles.md`, especially the first few cards in `## General`, `## White Papers`, and the first few entries in `## All Articles`.
   - Preserve the existing style and HTML/markdown formatting exactly.

2. Decide the category.
   - Use `## General` for essays, arguments, explainers, commentary, and narrative articles.
   - Use `## White Papers` for formal papers, empirical studies, benchmark reports, PDFs, or article-like pages explicitly framed as white papers.
   - If the article could fit either, classify by presentation and reader expectation: editorial/narrative goes in General; research/report framing goes in White Papers.

3. Draft the short summary.
   - Write one concise paragraph in the same voice and length as nearby cards.
   - Summarize the article's argument, not just its topic.
   - Avoid generic filler like "This article explores" unless that matches nearby entries.
   - Use the same summary, or a slightly fuller version, for the All Articles entry if it fits the local pattern.

4. Add the category card at the top of the chosen card grid.
   - Insert the new `<a class="card-item">` as the first item after the opening `<div class="card-grid">` in the chosen section.
   - For markdown articles, the card `href` should use the generated HTML path:

     ```html
     <a href="pages/articles/<slug>.html" class="card-item">
     ```

   - For PDFs, keep the `.pdf` path.
   - If the article has a top image such as:

     ```markdown
     ![Alt text](./images/01__example.webp)
     ```

     convert it to the index-relative card image path:

     ```html
     <img src="pages/articles/images/01__example.webp" class="card-image" alt="<Title> banner" />
     ```

   - If the article has no clear image, follow the current local pattern and omit the `<img>` line.
   - Use `Read Article` for General cards and `Read Paper` for White Paper cards.

5. Add the All Articles entry at the top.
   - Insert it immediately after `## All Articles`, before the previous first entry.
   - Use the exact local markdown pattern:

     ```markdown
     ### [Article Title](articles/<slug>.md) (Month YYYY)
     *By Dominik Gorecki*

     One-paragraph summary.
     ```

   - Use `articles/<slug>.md` for markdown articles and `articles/<filename>.pdf` for PDFs.
   - Date the entry with the current update month and year, for example `April 2026`.
   - Always place the new entry at the top because `All Articles` is ordered latest to oldest.

6. Verify.
   - Confirm the article appears once in the chosen category card grid.
   - Confirm the article appears once at the top of `All Articles`.
   - Confirm title, links, image path, category footer text, author line, and date formatting match nearby entries.
   - Do not modify article content unless the user also requested it.

## Example

For `pages/articles/medicines_dead_time.md` on April 30, 2026:

- It belongs in `## General` because it is an editorial argument, not a white paper.
- The card link should be `pages/articles/medicines_dead_time.html`.
- The All Articles link should be `articles/medicines_dead_time.md`.
- The All Articles date should be `(April 2026)`.
