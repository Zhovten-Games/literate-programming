# Extension Governance

## Purpose

This document defines how project-local methodology extensions specialize Prompt-Literate Workflow without redefining the reusable base methodology.

## Base methodology vs project-local extension layer

The base methodology defines universal workflow invariants, file roles, TRACE expectations, and validation discipline. A project-local extension lives outside the base layer and documents local constraints for a concrete project.

Neutral example locations:

```text
<project-root>/external/prompt-literate-workflow/
<project-root>/methodology/extensions/
```

## Extension registration

Each extension should have a named file or folder under `<project-root>/methodology/extensions/` and should follow `schemas/EXTENSION.schema.md`.

Registration must declare:

- purpose and scope;
- extension type;
- base invariants preserved;
- allowed and forbidden adjustments;
- validation expectations;
- conflict-handling rule;
- review owner;
- promotion candidate status.

## Allowed extension types

- **Additive:** adds local checks, terminology, scenarios, or evidence requirements while preserving all base invariants.
- **Restrictive:** narrows allowed behavior or adds stricter gates than the base method.
- **Explanatory:** clarifies how the base method is applied locally without adding new gates.

## Conflict resolution

Priority order:

1. Active task-level instructions.
2. Base Prompt-Literate Workflow invariants.
3. Registered project-local extensions.
4. Run-local operational notes.

If an extension conflicts with a base invariant, the base invariant remains authoritative. The extension must be revised or explicitly escalated into a promotion discussion.

## Promotion rule

A project-local rule becomes part of the base methodology only through an explicit promotion pass. Local use, repetition, or convenience does not silently modify the base method.

## Traceability

Extension changes should be recorded in version control and referenced in project TRACE when they affect a run, validation gate, or acceptance decision.

## Source-of-truth hierarchy

The canonical project plan remains the source of truth for project intent. The base methodology defines workflow discipline. Extensions define local specialization. Generated artifacts remain outputs and cannot override the plan, contracts, or accepted TRACE.

## Review ownership

Each extension must identify a review owner or owning role. The owner is responsible for checking that local rules preserve base invariants and remain appropriate for the project.

## Extension validation expectations

Extensions should define how their local rules are validated. Validation may be documentation-only, script-backed, manually reviewed, or tied to project tests, but the backing status must be explicit.
