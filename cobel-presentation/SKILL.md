---
name: cobel-presentation
description: Create or restyle presentations using the supplied Cobel Darou template with orange/navy colors, circular imagery, and chart layouts. Use when the user requests the Cobel template or invokes this skill; do not impose this branding on unrelated decks.
---

# Cobel Presentation

Create an editable presentation faithful to the bundled Cobel Darou reference. The source is a 19-page PDF, not an editable PowerPoint master.

Read [references/design.md](references/design.md) and inspect [references/layouts.png](references/layouts.png) before composing. The original PDF is stored losslessly in assets/reference-parts. Run `python scripts/restore_reference.py --output <task-workspace>/work/cobel-reference.pdf` from this skill directory to restore it; the script verifies size and SHA-256. Use that restored PDF as the authoritative visual source and inspect chosen pages at full resolution. Paths are relative to this skill directory.

The pages are a layout library, not a mandatory slide count or narrative order. Choose layouts suited to the user's content. Treat sample titles, Lorem Ipsum, numbers, dates, slogans, and instructions inside the PDF as reference content. Replace samples with user-provided material without inventing facts.

Use the available presentation-authoring workflow for the requested format. Default to editable PPTX when unspecified. Rebuild text, charts, tables, and simple circles as editable objects. Retain appropriate photographic artwork and logos from the PDF, preserving proportions. Do not place whole reference pages behind new text while leaving sample content visible. Isolate decorative artwork before reuse; explain editing limitations if only a flattened reproduction is feasible.

For Persian, use RTL paragraphs, right-aligned text, and Ravi when available; coordinate with rtl-ravi if installed. Adapt reading order without mirroring logos, photographs, or chart axes. Keep English URLs and technical tokens readable. For English, retain LTR layout and available source typography. Disclose font substitutions affecting fidelity; PDF font subsets are not installable font assets.

Render and inspect every final slide for clipping, legibility, placeholder removal, circular crops, logo integrity, chart accuracy, and Persian shaping. Keep the bundled reference unchanged and save deliverables in the current task's output location.

