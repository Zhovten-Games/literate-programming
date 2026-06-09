# Prompt-Literate Workflow Method

## Purpose

Prompt-Literate Workflow is a method for using an LLM inside a literate workflow. It is not a direct `prompt -> code` shortcut. The LLM acts as an executor or editor inside a human-defined structure, not as the default system architect.

## Central workflow

```text
human-authored plan
  -> chunk contracts
  -> bounded prompt
  -> candidate output
  -> review
  -> tests / smoke-check
  -> TRACE
```

## Core invariants

1. Source of truth is the human-authored literate plan.
2. The contract layer is mandatory between plan and generation.
3. A prompt is an operation over plan/contracts, not a source.
4. Chat log is trace material, not a source.
5. LLM output is a candidate artifact, not an accepted implementation.
6. The LLM may modify only explicitly allowed chunks.
7. Every generated chunk must have a contract before generation.
8. Every LLM-fillable chunk must have acceptance criteria.
9. One prompt run equals one TRACE entry.
10. Generated code cannot be accepted without review.
11. Generated code cannot be accepted without smoke-check/tests.
12. Manual edits to generated code must be reflected in plan/contracts/TRACE.
13. Contract changes must be made before regeneration or acceptance.
14. LLM generation is non-deterministic; validation is deterministic.
15. Non-reproducible output may be accepted only as a traced and reviewed artifact.
16. Base methodology and project-local extensions are separate layers.
17. A project-local extension must not silently contradict base invariants.
18. A local extension becomes part of the base methodology only through an explicit promotion pass.
19. Planning/documentation runs may use reduced TRACE.
20. Implementation/generation runs require full TRACE.
21. Do not fabricate generated artifacts, test results, accepted chunks, or rejected chunks during planning-only runs.
22. Generated artifacts are outputs, never source of truth.
23. External authoring/review surfaces are candidate inputs until normalized, validated, reviewed, and committed into the canonical source.
24. Every scenario must declare validation/test-backing status.
25. A test that is not executed or reported is not evidence.
26. Project-specific semantics must stay outside the reusable base methodology.
27. Extensions may be additive, restrictive, or explanatory, but must declare their relationship to base invariants.

## File roles

- `*.plan.md` is the canonical human-authored plan with named chunks, constraints, and intent.
- `CONTRACTS.md` is the mandatory contract layer between plan and generation.
- `SCENARIOS.md` records acceptance and validation scenarios, including test-backing status.
- `prompts/*.prompt.md` are bounded LLM operations over plan/contracts.
- `generated/` contains candidate generated artifacts before acceptance.
- `tests/smoke-check.*` contains deterministic checks for accepted or candidate artifacts.
- `TRACE.md` records runs, decisions, acceptance, rejection, and validation evidence.

## Workflow stages

1. Write or freeze the human-authored plan.
2. Define named chunks.
3. Add contracts for each LLM-fillable chunk.
4. Add acceptance criteria and scenarios.
5. Mark fillable chunks with `LLM-TODO`.
6. Run planning or generation-readiness validation.
7. Run the LLM with a bounded prompt.
8. Accept only allowed chunk replacements, not a full redesign.
9. Review manually and/or with a review prompt.
10. Produce or update candidate artifacts only after review boundaries are clear.
11. Run smoke-check/tests.
12. Record model/tool, prompt, edits, rejected/accepted chunks, and test results in `TRACE.md`.

## Acceptance criteria

A generated result is accepted only if it:

- changes only allowed chunks;
- preserves chunk names;
- preserves public declarations unless explicitly allowed otherwise;
- satisfies chunk contracts;
- satisfies scenarios;
- passes relevant deterministic checks;
- includes required evidence;
- has documented manual edits, if any;
- has updated TRACE.

## Boundary status

The deterministic part is plan, contracts, validation, tests, and TRACE. LLM output remains model-, version-, and context-dependent, so it must remain a candidate until reviewed and validated.
