# Literate Companion Implementations / Каталог literate-реализаций

- `examples/en/` contains the English companion set.
- `examples/ru/` contains the Russian companion set.
- `methodology/` contains reusable workflow methodology definitions and article-local extensions.
- Variants `01`–`06` solve the same task deterministically: print the first 1000 prime numbers in a 4-column paginated table.
- `07-prompt-literate` is an article-local boundary example of Prompt-Literate Workflow; it constrains LLM-assisted generation via human-authored plan, chunk contracts, bounded prompts, review, tests, and TRACE.
- Examples are not equivalent in strictness:
  - **CWEB** and **noweb-like** are the closest to classical literate programming.
  - **org-babel** is a practical plain-text workflow with tangling.
  - **Quarto**, **Jupyter**, and **R Markdown** are executable-document descendants, not strict WEB equivalents.

## Full comparison table / Полная сравнительная таблица

| Variant / Вариант | Main role / Роль                             | Strong side / Сильная сторона             | Main cost / Цена                                |
| --------------- | ---------------------------------------------- | ------------------------------------------ | ------------------------------------------------ |
| `01-cweb`       | Historical canon                               | Full tangle/weave                          | CWEB/TeX ritual                                  |
| `02-noweb-like` | Main practical C++ reboot                      | Minimal syntax and ritual                  | Weaker separate document-generation branch       |
| `03-org-babel`  | Modern literate environment                    | Org-mode, tangling, export, execution      | Emacs ecosystem                                  |
| `04-quarto`     | Executable document / computational publishing | Rendered publication with live computation | Not strict WEB/source generation                 |
| `05-jupyter`    | Notebook / literate computing                  | Interactivity                              | Hidden state / execution-order risk              |
| `06-rmarkdown`  | Reproducible report                            | Reports and computational documents        | Closer to report workflow than source generation |
| `07-prompt-literate` | Experimental boundary workflow              | Example of Prompt-Literate Workflow         | Prompt output is not deterministic; validation is controlled       |

## Interpretation / Краткая интерпретация

- Use `01-cweb` to understand the historical full WEB/CWEB mechanism.
- Use `02-noweb-like` as the main lightweight C++ literate-programming reboot example.
- Use `03-org-babel` if Emacs/Org-mode is acceptable as an environment.
- Use `04-quarto`, `05-jupyter`, or `06-rmarkdown` when the target is executable documents / computational publishing rather than strict WEB-style source generation.
- Use `07-prompt-literate` to inspect the Prompt-Literate Workflow boundary case where generation is candidate-only until review, evidence, and TRACE.

- `01-cweb` — для исторического полного WEB/CWEB-механизма.
- `02-noweb-like` — основной лёгкий C++ literate-programming reboot-пример.
- `03-org-babel` — если Emacs/Org-mode подходит как рабочая среда.
- `04-quarto`, `05-jupyter`, `06-rmarkdown` — когда цель executable documents / computational publishing, а не строгая WEB-style генерация исходника.
- `07-prompt-literate` — для граничного случая Prompt-Literate Workflow, где generated output остаётся кандидатом до review, evidence и TRACE.

## Methodology layers

### `methodology/prompt-literate-workflow/`

Companion-local methodology path synchronized with the public Prompt-Literate Workflow repository:

```text
https://github.com/IRONCREED/prompt-literate-workflow
```

The reusable methodology is integrated into the `literate-programming` repository as a root submodule/scaffold at `prompt-literate-workflow/`; this companion path exposes the same method for the article-local examples.

### `methodology/extensions/primes-example/`

Local additive extension for Knuth's prime-number task. It contains prime-specific acceptance markers and validation rules for the article-local `07-prompt-literate` examples.
