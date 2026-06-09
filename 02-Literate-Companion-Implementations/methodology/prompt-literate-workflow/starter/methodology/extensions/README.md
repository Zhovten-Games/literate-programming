# Project-local extensions starter

Project-local extensions are optional. Create an extension only when a consuming project has domain-specific constraints that must be documented outside the reusable Prompt-Literate Workflow core.

The base methodology remains authoritative. Extensions may be:

- **additive** — add local checks, scenarios, or evidence requirements;
- **restrictive** — narrow allowed behavior or add stricter gates;
- **explanatory** — clarify local use without adding new gates.

Extensions must not silently contradict base invariants. Each extension must declare validation expectations and review ownership.

Promotion into the base methodology requires a separate explicit promotion pass. Local adoption alone does not modify the Prompt-Literate Workflow core.
