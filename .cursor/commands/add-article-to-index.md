---
description: Add a markdown article to pages/articles.md
---

The input to this command is a single markdown article reference in this repo:

`$ARGUMENTS`

Update `pages/articles.md` to add that article in the same pattern used by the existing entries.

Requirements:

1. Treat `$ARGUMENTS` as the article file to index.
2. Read the target article and `pages/articles.md`.
3. Add the article as the top card in the `## General` card section on `pages/articles.md`.
4. Add the article as the next entry in the `## All Articles` section on `pages/articles.md`.
5. Reuse the structure, wording style, and HTML/Markdown patterns already present in `pages/articles.md`.
6. Write a concise summary in the voice of the article, not a generic abstract.
7. Infer the article title from the markdown heading and prefer the first article image for the card when one exists.
8. Do not reorder or rewrite unrelated entries.
9. After editing, check for lint or formatting issues only if the touched files participate in such checks.

Return a short summary of what you changed.
