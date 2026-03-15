---
name: remove-article-reference
description: Strip all references and links from markdown articles, generating a sanitized copy with the "__no_ref.md" suffix in the same folder. Use when a user asks to "Remove reference to [file.md]" or "Create no reference version of [file.md]".
---

# Remove Article Reference

## Overview

This skill enables the automatic sanitization of markdown files by removing all links and reference definitions. It creates a new file in the same directory as the source, appending `__no_ref.md` to the filename.

## Core Behavior

- **Trigger**: Prompt contains "Remove reference to [file]" or "Create no reference version of [file]".
- **Action**: Runs a Python script to strip markdown links and references.
- **Output**: Generates a new file `<original_name>__no_ref.md` in the same directory.

## Workflow

1.  Identify the source markdown file from the user's request.
2.  Execute the sanitization script using the project-local path:
    ```bash
    python3 .cursor/skills/remove-article-reference/scripts/remove_references.py <path_to_markdown_file>
    ```
3.  Confirm to the user that the sanitized file has been created.

## Implementation Details

The sanitization logic is handled by `scripts/remove_references.py`, which removes:
- Inline links: `[text](url)` -> `text`
- Reference-style links: `[text][ref]` -> `text`
- Reference definitions: `[ref]: url`
- Image links: `![alt](url)` -> `IMAGE: [alt] - url`
- Autolinks: `<url>`
- Bare URLs: `https://example.com`

## Example

**User**: "Create no reference version of pages/articles.md"

**Assistant**:
- Runs `python3 .cursor/skills/remove-article-reference/scripts/remove_references.py pages/articles.md`
- Confirms: "I've created a sanitized version of the article at `pages/articles__no_ref.md`."

## Resources

### scripts/

- `remove_references.py`: The primary script for stripping references and links from markdown.
