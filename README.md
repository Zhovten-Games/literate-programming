# Literate Programming: Donald Knuth, WEB, and Contemporary Workflows

This repository accompanies a methodological review of Donald Knuth’s 1984 article *Literate Programming*.

Knuth proposed that programs should be written primarily for human readers and only secondarily transformed into machine-executable form. The review reconstructs this argument through the WEB system and examines how its central principle persists across contemporary engineering practices.

The repository distinguishes:

* direct or historically proximate continuations, such as CWEB and noweb;
* instrumentally related workflows, such as Org Babel;
* broader conceptual associations involving executable documents, reproducible environments, IDE navigation, context maps, and LLM-assisted development.

The companion suite remasters Knuth’s prime-number example through several deterministic workflows and introduces Prompt-Literate Workflow as a controlled boundary case for probabilistic generation.

## Read the Article

* [Literate Programming: Donald Knuth, WEB, and Contemporary Workflows](https://doi.org/10.5281/zenodo.20608558)

### Repository Sources

* [English](01-Literate-Programming-EN/01-Literate-Programming.md)
* [Українська](01-Literate-Programming-UK/01-Literate-Programming.md)
* [Русская](01-Literate-Programming-RU/01-Literate-Programming.md)

## Article Map

### Main Article

* **Opening Remarks** — historical framing, comparison criteria, and the rationale for a contemporary remaster.
* **A. Introduction** — a shift in whom programming is primarily addressed to: from instructing the machine to explaining the program to a human reader.
* **B. The WEB System** — WEB as a system that generates human-oriented and machine-oriented projections from a single source.
* **C–F. Example / source / tangle / weave** — Knuth’s prime-number example, the original WEB source, TANGLE, WEAVE, and the lightweight C++ remaster.
* **G. Additional Bells and Whistles** — the transition from an instructional example to production-level complexity.
* **H. Occam’s Razor** — the limits of the tool and the need for methodological restraint.
* **I. Portability** — portability beyond the original TeX / Pascal pairing and the contemporary role of reproducible environments.
* **J. Programs as Webs** — programs as networks of named fragments, dependencies, and explanatory relationships.
* **K. Stylistic Issues** — section naming, readable structure, and the engineering role of style.
* **L. Economic Issues** — the costs and benefits of literate discipline.
* **M. Related Work** — structured programming, documentation systems, executable documents, and adjacent lineages.
* **N. Retrospect and Prospects** — a retrospective assessment of the method and its future prospects.

### Conclusions

* **1. What Donald Knuth Actually Proposed**
* **2. What Persisted and What Changed Form**
* **3. The Cost of the Method and Its Limits of Applicability**
* **4. LLMs: A Continuation of the Idea or a New Form of Rupture**
* **5. Where the Idea May Develop Further**

## Repository Navigation

```text
.
├── 01-Literate-Programming-EN/
│   ├── 01-Literate-Programming.md
│   ├── authors.yml
│   └── Bibliography/
├── 01-Literate-Programming-UK/
│   ├── 01-Literate-Programming.md
│   ├── authors.yml
│   └── Bibliography/
├── 01-Literate-Programming-RU/
│   ├── 01-Literate-Programming.md
│   ├── authors.yml
│   └── Bibliography/
├── 02-Literate-Companion-Implementations/
│   ├── README.md
│   ├── Makefile
│   ├── examples/{en,uk,ru}/
│   └── methodology/
└── prompt-literate-workflow/
```

### Companion Suite

The [companion suite](02-Literate-Companion-Implementations/README.md) provides reproducible examples for several branches of the review:

* `01-cweb` — a canonical CWEB route with explicit `tangle / weave` branches;
* `02-noweb-like` — the primary lightweight C++ remaster, centred on a `tangle-first workflow`;
* `03-org-babel` — a plain-text Org-mode / Emacs workflow with tangling;
* `04-quarto` — an executable-document route for computational publishing;
* `05-jupyter` — a notebook route with explicit attention to hidden state and reproducible execution;
* `06-rmarkdown` — a reproducible-report workflow based on R Markdown / knitr / Pandoc;
* `07-prompt-literate` — a boundary example applying Prompt-Literate Workflow to Knuth’s prime-number task.

The deterministic examples and the LLM boundary example are intentionally separated. LLM-generated output is treated as a candidate artifact requiring review, tests, smoke-checks, and traceability rather than as a deterministic build artifact.

The localized companion branches are available in `examples/en/`, `examples/uk/`, and `examples/ru/`. Each Ukrainian localization mirrors an existing Russian localized file; methodology and control artifacts that existed only in English remain English-only.

## Prompt-Literate Workflow

The repository includes [Prompt-Literate Workflow](https://github.com/IRONCREED/prompt-literate-workflow) as a pinned Git submodule.

The method defines a controlled AI-assisted workflow:

```text
human-authored literate plan
  → chunk contracts
  → bounded prompt
  → LLM-generated candidate
  → review
  → tests / smoke-check
  → TRACE
  → accepted update to canonical source
```

<details>
<summary><strong>Українська версія</strong></summary>

# Literate Programming: Дональд Кнут, WEB і сучасні робочі процеси

Цей репозиторій супроводжує методологічний огляд статті Дональда Кнута *Literate Programming*, опублікованої 1984 року.

Кнут запропонував писати програми передусім для людського читання і лише потім перетворювати їх на форму, придатну до машинного виконання. Огляд реконструює цю аргументацію через систему WEB і розглядає, як її центральний принцип виявляється у сучасних інженерних практиках.

У репозиторії розмежовано:

* прямі або історично близькі продовження, як-от CWEB і noweb;
* інструментально споріднені практики, як-от Org Babel;
* ширші смислові асоціації, пов’язані з executable documents, відтворюваними середовищами, IDE-навігацією, context maps і LLM-assisted розробкою.

Companion-набір переносить приклад Кнута з простими числами до кількох детермінованих workflow і вводить Prompt-Literate Workflow як керований граничний приклад імовірнісної генерації.

## Читати статтю

* [Literate Programming: Дональд Кнут, WEB і сучасні робочі процеси](https://doi.org/10.5281/zenodo.20608558)
</details>

<details>
<summary><strong>Русская версия</strong></summary>

# Literate Programming: Дональд Кнут, WEB и современные рабочие процессы

Этот репозиторий сопровождает методологический обзор статьи Дональда Кнута *Literate Programming*, опубликованной в 1984 году.

Кнут предложил писать программы прежде всего для человеческого чтения и только затем преобразовывать их в машинно-исполняемую форму. Обзор реконструирует эту аргументацию через систему WEB и рассматривает, как её центральный принцип проявляется в современных инженерных практиках.

В репозитории разграничиваются:

* прямые или исторически близкие продолжения, такие как CWEB и noweb;
* инструментально родственные практики, такие как Org Babel;
* более широкие смысловые ассоциации, связанные с executable documents, воспроизводимыми окружениями, IDE-навигацией, context maps и LLM-assisted разработкой.

Companion-набор переносит пример Кнута с простыми числами в несколько детерминированных workflow и вводит Prompt-Literate Workflow как управляемый граничный пример вероятностной генерации.

## Читать статью

* [Literate Programming: Дональд Кнут, WEB и современные рабочие процессы](https://doi.org/10.5281/zenodo.20608558)
</details>
