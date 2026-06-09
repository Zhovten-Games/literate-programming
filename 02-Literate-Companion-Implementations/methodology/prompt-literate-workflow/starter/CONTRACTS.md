# CONTRACTS

## Chunk: `<<define public contract>>`

- **Role:** Define stable public expectations.
- **Status:** author-defined
- **Inputs:** Human-authored plan.
- **Outputs:** Public contract description.
- **Allowed changes:** None during generation.
- **Forbidden changes:** Redefining scope without plan revision.
- **Acceptance criteria:** Preserved during candidate generation.

## Chunk: `<<implement core behavior>>`

- **Role:** Implement the bounded core behavior.
- **Status:** LLM-fillable
- **Inputs:** Plan and public contract.
- **Outputs:** Candidate implementation text or artifact.
- **Allowed changes:** Only this chunk.
- **Forbidden changes:** Changing author-defined chunks.
- **Acceptance criteria:** Satisfies the plan, contract, and scenarios.

## Chunk: `<<validate expected result>>`

- **Role:** Implement bounded validation behavior.
- **Status:** LLM-fillable
- **Inputs:** Plan, contract, and scenarios.
- **Outputs:** Candidate validation text or artifact.
- **Allowed changes:** Only this chunk.
- **Forbidden changes:** Treating generated output as source of truth.
- **Acceptance criteria:** Produces deterministic evidence or a documented review result.
