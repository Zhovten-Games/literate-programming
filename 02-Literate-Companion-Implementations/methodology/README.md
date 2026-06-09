# Methodology layers

This directory separates reusable Prompt-Literate Workflow methodology from article-local extensions.

## `prompt-literate-workflow/`

`prompt-literate-workflow/` is the companion-local methodology path synchronized with the reusable Prompt-Literate Workflow scaffold located at the repository root:

```text
../../prompt-literate-workflow/
```

The public methodology repository is:

```text
https://github.com/IRONCREED/prompt-literate-workflow
```

The methodology is integrated into `literate-programming` as a root submodule/scaffold at `prompt-literate-workflow/`; this directory provides the path consumed by the companion examples.

The reusable mirror must not be edited independently from the source scaffold. Update the source scaffold first, then synchronize this path.

## `extensions/`

Article-specific local extensions live under:

```text
methodology/extensions/
```

These extensions demonstrate how a concrete companion example specializes the reusable method without redefining it.
