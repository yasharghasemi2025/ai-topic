---
name: rtl-ravi
description: Apply Persian right-to-left layout, Ravi font, and right-aligned text when creating or formatting Persian documents, spreadsheets, slides, PDFs, or HTML/CSS files. Use for requests mentioning RTL, راست‌به‌چپ, راست‌چین, or Ravi typography; do not apply to unrelated source code or English-only content.
---

# Persian RTL with Ravi

When this skill applies, use three separate defaults: right-to-left reading direction, the Ravi font family, and right text alignment. Direction alone does not guarantee alignment. Preserve explicit user overrides and the content and structure of existing files.

## Shared requirements

- Apply the defaults consistently to Persian headings, paragraphs, lists, tables, captions, headers, footers, text boxes, and editable form text where the format supports them.
- Keep text in Unicode logical order. Never reverse strings or use spaces to simulate alignment.
- Isolate English phrases, URLs, email addresses, formulas, and code as left-to-right when necessary while retaining the surrounding RTL layout. Preserve numeric values and identifiers.
- Locate Ravi in supplied assets or installed fonts. Use its actual family name and available weights. Do not silently substitute a different font or claim Ravi rendered without checking. If Ravi is unavailable, retain the requested family in editable output, explain the limitation, and request the font file when actual rendering or embedding requires it. Use supplied or otherwise authorized font assets; do not download an arbitrary font or assume embedding rights.
- Apply this typography alongside the relevant artifact skill's creation and verification workflow. This skill does not replace the document, spreadsheet, presentation, or PDF workflow.

## Format-specific application

### HTML and CSS

Set the Persian content root to `lang="fa"` and `dir="rtl"`, with `direction: rtl; text-align: right; font-family: 'Ravi', sans-serif;`. Ensure inputs, buttons, tables, and nested components inherit the intended typography. Use a real, available font asset for `@font-face` when needed; never invent a working font URL. Use logical spacing properties when helpful. Give LTR fragments appropriate isolation, such as `<bdi dir="ltr">`. Inspect the rendered page and actual loaded font.

### Word documents

Set paragraph bidirectional direction and right alignment independently. Apply Ravi to styles and relevant run font slots, including complex-script text. Apply RTL table direction where appropriate and check list numbering and indentation. Include headers, footers, and text boxes in the review. Do not mark purely Latin runs RTL if it disrupts their reading order.

### Spreadsheets

Use RTL worksheet view for Persian sheets and right alignment plus Ravi for the intended cells and text objects. Preserve numeric cell types, formulas, and date values. Check mixed-language labels and charts separately; worksheet direction alone does not format their text.

### Presentations

Apply RTL paragraph direction, right alignment, and Ravi to Persian text boxes, tables, and relevant master/layout styles where supported. Check bullet placement, indentation, wrapping, and mixed-language labels. Preserve an explicitly requested visual composition.

### PDF

Prefer an editable source or a renderer that supports Persian shaping and bidirectional layout. Use Ravi and embed/subset it when permitted and supported. Verify joined letter forms, punctuation, mixed-language order, and right alignment in rendered pages. Do not implement RTL by reversing character order. For existing PDFs, explain when faithful editing requires the source file or reconstruction.

### Plain text and Markdown

Plain text cannot guarantee font, direction, or alignment; Markdown support depends on its renderer. Preserve readable Unicode text and use supported HTML/CSS only when suitable for the target renderer. If reliable styling is essential, provide an appropriate styled format within the user's requested scope and explain any remaining limitation.

## Final verification

Inspect representative rendered content: a heading, multi-line paragraph, list or table when present, and mixed Persian/English text with numbers and punctuation. Confirm RTL reading direction, right alignment, actual Ravi rendering, and absence of clipping or disconnected Persian letters. Report font substitution or unsupported formatting honestly rather than treating a font-family declaration as proof of correct output.

