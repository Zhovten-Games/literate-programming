# TRACE Policy

TRACE records one entry per prompt/tool run. It links inputs, allowed scope, review, validation, and decisions.

## Placeholder status

A `not-run` TRACE placeholder may be used only when the scaffold or example has not recorded an actual prompt/tool run.

A not-run TRACE placeholder is not execution evidence. Replace it with a real TRACE entry when the first run occurs.

Do not use `accepted` or `accepted-with-notes` for a run that did not occur.

## Phase 0: planning/documentation runs

Use `schemas/TRACE.phase-0.schema.md` for planning, documentation, review, or scaffold-maintenance runs that do not create accepted generated implementation artifacts.

Phase 0 TRACE may be reduced, but it must not fabricate generated artifacts, tests, smoke-check results, accepted chunks, rejected chunks, or manual edits if they do not exist.

Real Phase 0 results are `accepted`, `accepted-with-notes`, or `rejected`.

## Phase 1: candidate generation / implementation runs

Use `schemas/TRACE.phase-1.schema.md` when a run asks an LLM or tool to generate or modify candidate implementation artifacts.

Phase 1 TRACE requires method version, input plan version, contract version, generated file, accepted/rejected chunks, manual edits, reviewer, method validation result, smoke-check/test evidence, acceptance decision, and notes.

## Evidence rule

A test, script-backed check, or scenario is evidence only when it is executed and reported, or when it is explicitly marked as documentation-only. Unexecuted checks must not be presented as passed evidence.
