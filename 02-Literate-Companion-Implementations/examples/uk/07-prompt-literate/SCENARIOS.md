# SCENARIOS (example-specific): Prompt-Literate Workflow for primes

## Scenario: Plan integrity
- **Purpose:** Ensure canonical plan exists with required chunks.
- **Input:** `primes.plan.md`.
- **Expected result:** All required chunk names are present.
- **Validation method:** Check chunk markers in plan.
- **Test-backing status:** manual-review-only
- **Evidence path or command:** TRACE.md review summary
- **Notes:** Review evidence is pending or documentation-only because generated implementation is intentionally absent in the current planning-only pass.

## Scenario: Fill scope restriction
- **Purpose:** Ensure LLM fills only `LLM-TODO` chunks.
- **Input:** LLM candidate chunk output.
- **Expected result:** Only `<<prime-generation>>` and `<<table-output>>` are modified.
- **Validation method:** Chunk-level diff against plan.
- **Test-backing status:** manual-review-only
- **Evidence path or command:** TRACE.md review summary
- **Notes:** Review evidence is pending or documentation-only because generated implementation is intentionally absent in the current planning-only pass.

## Scenario: Build success
- **Purpose:** Confirm generated artifact compiles.
- **Input:** `generated/primes.generated.cpp`.
- **Expected result:** C++17 build succeeds.
- **Validation method:** Run `tests/smoke-check.sh` compile step.
- **Test-backing status:** script-backed
- **Evidence path or command:** bash tests/smoke-check.sh
- **Notes:** Evidence is pending because generated implementation is intentionally absent in the current planning-only pass.

## Scenario: Output marker Page 1
- **Purpose:** Ensure pagination header starts correctly.
- **Input:** Program output.
- **Expected result:** Contains `The First 1000 Prime Numbers --- Page 1`.
- **Validation method:** Marker grep in output.
- **Test-backing status:** script-backed
- **Evidence path or command:** bash tests/smoke-check.sh
- **Notes:** Evidence is pending because generated implementation is intentionally absent in the current planning-only pass.

## Scenario: Output marker Page 5
- **Purpose:** Ensure pagination spans full required range.
- **Input:** Program output.
- **Expected result:** Contains `The First 1000 Prime Numbers --- Page 5`.
- **Validation method:** Marker grep in output.
- **Test-backing status:** script-backed
- **Evidence path or command:** bash tests/smoke-check.sh
- **Notes:** Evidence is pending because generated implementation is intentionally absent in the current planning-only pass.

## Scenario: Output contains 7919
- **Purpose:** Validate generation reaches the 1000th prime.
- **Input:** Program output.
- **Expected result:** Contains `7919`.
- **Validation method:** Marker grep in output.
- **Test-backing status:** script-backed
- **Evidence path or command:** bash tests/smoke-check.sh
- **Notes:** Evidence is pending because generated implementation is intentionally absent in the current planning-only pass.

## Scenario: Manual edits traceability
- **Purpose:** Prevent hidden manual edits.
- **Input:** Accepted generated artifact and `TRACE.md`.
- **Expected result:** Any manual edits are reflected in TRACE.
- **Validation method:** Review generated diff and TRACE manual edits field.
- **Test-backing status:** manual-review-only
- **Evidence path or command:** TRACE.md review summary
- **Notes:** Review evidence is pending or documentation-only because generated implementation is intentionally absent in the current planning-only pass.

## Scenario: Forbidden architecture changes rejection
- **Purpose:** Block redesign outside plan/contracts.
- **Input:** Review report vs generated candidate.
- **Expected result:** Architecture/signature/forbidden chunk changes are rejected.
- **Validation method:** Contract and prompt conformance review.
- **Test-backing status:** manual-review-only
- **Evidence path or command:** TRACE.md review summary
- **Notes:** Review evidence is pending or documentation-only because generated implementation is intentionally absent in the current planning-only pass.
