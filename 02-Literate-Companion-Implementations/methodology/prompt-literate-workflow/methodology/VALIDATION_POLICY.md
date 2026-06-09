# Validation Policy

Validation is the deterministic part of Prompt-Literate Workflow.

## General expectations

- Validate that required project files exist.
- Validate that every `LLM-TODO` has an `LLM-fillable` contract.
- Validate that fillable contracts include acceptance criteria.
- Validate that scenarios declare test-backing status.
- Validate that TRACE declares the phase and records run evidence.
- Validate that generated outputs are not treated as source of truth.

## Phase expectations

- `planning`: validates structure for planning or documentation work.
- `generation-ready`: validates that the project can ask for bounded generation.
- `candidate`: validates the presence and traceability of candidate generated artifacts.
- `accepted`: validates review, deterministic checks, evidence, and acceptance decision.

## Validator state vs TRACE phase

`validate-project.py --state` describes project readiness. TRACE `Phase` describes the kind of prompt/tool run being recorded. The backward-compatible `--phase` CLI alias maps to validator state only and must not be confused with TRACE phase.
