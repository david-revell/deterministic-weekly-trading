# Tooling Notes and Practical Tips

This file captures small but useful tooling notes discovered during development.
It is not part of the trading logic.

## Markdown Table Conversion

Markdown tables can be converted cleanly into structured formats if needed later.

Common options:
- Markdown → CSV
- Markdown → Excel
- Markdown → Pandas DataFrame

Typical tools:
- pandoc (markdown → csv / xlsx)
- simple scripts (regex or Python parsing)
- manual copy-paste into Excel (works reliably for simple tables)

Key point:
Even though raw Markdown tables look ugly, they are structurally lossless and
can be transformed later without rewriting the content.

## Documentation Principle

- Markdown is the canonical documentation format in this repo.
- Human readability is prioritised over machine optimisation.
- If data-like structure is needed later, it is regenerated from specs,
  not scraped from documentation.

Additional tooling notes can be added here as they arise.
