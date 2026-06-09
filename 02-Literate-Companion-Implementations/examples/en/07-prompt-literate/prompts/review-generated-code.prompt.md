Review the generated code against the prompt-literate plan.

Review targets:
- Plan conformance (`primes.plan.md`).
- CONTRACTS.md and SCENARIOS.md conformance.
- Chunk boundaries and names.
- Output requirements and expected markers.
- Edge cases (`count == 0`, odd-candidate progression, divisibility stop condition).
- Unwanted architecture changes.
- Manual edits not reflected in the plan/TRACE.

Questions to answer:
- Did output modify forbidden chunks?
- Did output change architecture?
- Did output preserve public declarations?
- Did output satisfy CONTRACTS.md?
- Did output satisfy SCENARIOS.md?
- Can output be inserted back into the plan?
- Is it ready for smoke-check?

Rules:
- Do not rewrite architecture by default.
- Report deviations first.
- Suggest minimal corrective edits only when needed.

Output format:
1. Conformance summary
2. Violations (if any)
3. Minimal patch recommendations
4. Smoke-check readiness
