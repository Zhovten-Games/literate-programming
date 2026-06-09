# Companion

`07-prompt-literate` is an article-local boundary example of **Prompt-Literate Workflow** applied to Knuth's prime-number task.

The base methodology is available under:

```text
../../../methodology/prompt-literate-workflow/
```

It is synchronized with the public Prompt-Literate Workflow repository and the root submodule/scaffold in `literate-programming`:

```text
https://github.com/IRONCREED/prompt-literate-workflow
```

The prime-number specialization is defined under:

```text
../../../methodology/extensions/primes-example/
```

This example does not define Prompt-Literate Workflow. It demonstrates a local additive extension over the reusable base methodology.

`CONTRACTS.md` and `SCENARIOS.md` are example-specific for the prime-number task. Prompt files in `prompts/` are intentionally kept in English for portability across tools and models.

Generated output must not be created or accepted in this pass. Do not fill `LLM-TODO` chunks and do not create generated implementation code here.

## Validation commands

From this example directory, run:

```bash
python ../../../methodology/prompt-literate-workflow/scripts/validate-project.py --project . --state generation-ready
python ../../../methodology/extensions/primes-example/tests/validate-primes-example.py .
```

The base validator checks workflow discipline. The local validator checks prime-specific markers: `7919`, `Page 1`, and `Page 5`.
