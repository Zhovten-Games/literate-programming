# Project-local extension schema

## Extension: `primes-example`

- **Purpose:** Demonstrate Prompt-Literate Workflow on Knuth's prime-number task in the article companion set.
- **Scope:** Applies only to `examples/en/07-prompt-literate/`, `examples/uk/07-prompt-literate/`, and `examples/ru/07-prompt-literate/`.
- **Type:** additive
- **Base invariants preserved:** All base Prompt-Literate Workflow invariants remain authoritative; this extension adds local evidence markers only.
- **Allowed adjustments:** Add prime-specific acceptance markers, locale-equivalence checks, and a local validator for the article example.
- **Forbidden adjustments:** Redefining source-of-truth rules, filling `LLM-TODO` chunks during planning-only work, accepting generated artifacts without review and smoke-check, or changing the prime-number algorithm.
- **Validation expectations:** The local validator checks required example files and prime-specific markers while the base validator checks workflow discipline.
- **Conflict-handling rule:** If this extension conflicts with the base methodology, the base methodology wins and the extension must be revised.
- **Review owner:** Article companion maintainer.
- **Promotion candidate:** no
- **Notes:** Prime-specific expectations:
  - expected final prime marker: 7919;
  - expected pagination marker: Page 1;
  - expected pagination marker: Page 5;
  - generated artifact is not accepted without review and smoke-check;
  - generated artifact must not be committed as accepted implementation while LLM-TODO remains unresolved;
  - en, uk, and ru examples must preserve equivalent structure.
