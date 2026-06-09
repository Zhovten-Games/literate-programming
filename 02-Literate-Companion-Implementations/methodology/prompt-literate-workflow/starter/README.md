# Prompt-Literate Workflow starter

This starter is a neutral project scaffold for applying Prompt-Literate Workflow.

## Human-authored plan

`project.plan.md` is the canonical source of truth. It explains intent, names chunks, and marks only explicitly fillable areas with `LLM-TODO`.

## Contracts

`CONTRACTS.md` defines the contract for each fillable chunk: role, inputs, outputs, allowed changes, forbidden changes, and acceptance criteria.

## Scenarios

`SCENARIOS.md` defines validation scenarios and declares test-backing status for each scenario.

## TRACE

`TRACE.md` records prompt/tool runs. Planning runs may use phase 0. Candidate generation and implementation runs require phase 1.

## Bounded prompts

Prompts operate over the plan and contracts. They must name allowed chunks or files and must not ask for a full redesign.

## Generated output

Generated output remains a candidate until review, deterministic validation, and TRACE acceptance.
