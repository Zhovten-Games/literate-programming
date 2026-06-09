# Prompt-Literate Workflow

Prompt-Literate Workflow is a reusable methodology for constrained LLM-assisted work inside a literate process.
It is not a `prompt -> code` shortcut and it is not tied to any concrete toolchain, runtime, publication pipeline, domain, or project.

The public repository is:

```text
https://github.com/IRONCREED/prompt-literate-workflow
```

This repository can be consumed as a GitHub template repository or pinned into another project as a Git submodule. In `literate-programming`, the reusable methodology is integrated as a root submodule/scaffold at `prompt-literate-workflow/`.

The release line starts from `v0.1.0`; this scaffold remains versioned as `0.1.0-dev` until that release is cut.

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

## Repository layout

- `methodology/` contains the reusable method and policies.
- `schemas/` contains neutral documentation schemas for project-local use.
- `starter/` is the neutral starting structure copied into new Prompt-Literate Workflow projects.
- `scripts/validate-project.py` validates the discipline of a project-local application.

## Template repository vs submodule use

A GitHub template repository creates a new repository from the complete scaffold tree. It does not automatically extract only `starter/`.

`starter/` provides a neutral project-local starting structure that may be copied or promoted into a consuming project.

A pinned submodule pins reusable methodology rules to a specific external revision and lets a project keep the reusable method separate from local extensions.

## Extension boundary

The reusable method is intentionally compact. Project-local extensions may add stricter checks, local terminology, or explanatory policy, but they must not silently contradict base invariants. Promotion of a local rule into the base methodology requires an explicit promotion pass.
