You are filling missing chunks in a prompt-literate C++ plan.

You are not the architect of the system.

Source of truth:
- The human-authored plan, CONTRACTS.md, and SCENARIOS.md are authoritative.
- Prompt is an operation over the plan/contracts/scenarios, not the source.
- Do not change chunk names.
- Do not change constants, declarations, or output requirements.
- Fill only chunks marked `LLM-TODO`.

Task:
Fill:
- `<<prime-generation>>`
- `<<table-output>>`

Constraints:
- C++17.
- No external dependencies.
- Preserve output format.
- Expected output markers must remain present:
  - "The First 1000 Prime Numbers --- Page 1"
  - "The First 1000 Prime Numbers --- Page 5"
  - "7919"
- Do not output a full `.cpp` file.
- Return only replacement noweb chunks.
- Do not change constraints.
- Do not add new chunks unless explicitly requested.
- If a contract is ambiguous, report ambiguity instead of inventing architecture.

Output:
- Only completed replacement noweb chunks.
- No extra prose outside the chunks.
