# Literate Programming: Donald Knuth, WEB, and Contemporary Workflows

This repository accompanies a methodological review of Donald Knuth’s 1984 article *Literate Programming*.

Knuth proposed that programs should be written primarily for human readers and only secondarily transformed into machine-executable form. The review reconstructs this argument through the WEB system and examines how its central principle persists across contemporary engineering practices.

The repository distinguishes:

* direct or historically proximate continuations, such as CWEB and noweb;
* instrumentally related workflows, such as Org Babel;
* broader conceptual associations involving executable documents, reproducible environments, IDE navigation, context maps, and LLM-assisted development.

The companion suite remasters Knuth’s prime-number example through several deterministic workflows and introduces Prompt-Literate Workflow as a controlled boundary case for probabilistic generation.

## Read the Article

* [English article source](01-Literate Programming - Knuth WEB and Contemporary Workflows/01-Literate Programming - Knuth WEB and Contemporary Workflows.md)
* [Russian article source](01-Literate Programming Дональд Кнут, WEB и современные рабочие процессы/Literate Programming - Дональд Кнут, WEB и современные рабочие процессы.md)

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
├── 01-Literate Programming - Knuth WEB and Contemporary Workflows/
│   ├── 01-Literate Programming - Knuth WEB and Contemporary Workflows.md
│   ├── authors.yml
│   └── Bibliography/
├── 01-Literate Programming Дональд Кнут, WEB и современные рабочие процессы/
│   ├── Literate Programming - Дональд Кнут, WEB и современные рабочие процессы.md
│   ├── authors.yml
│   └── Bibliography/
├── 02-Literate-Companion-Implementations/
│   ├── README.md
│   ├── Makefile
│   ├── examples/
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

* [Английская версия](01-Literate Programming - Knuth WEB and Contemporary Workflows/01-Literate Programming - Knuth WEB and Contemporary Workflows.md)
* [Русская версия](01-Literate Programming Дональд Кнут, WEB и современные рабочие процессы/Literate Programming - Дональд Кнут, WEB и современные рабочие процессы.md)

## Карта статьи

### Основная статья

* **Вступление** — историческая постановка проблемы, рамка сравнения и обоснование современного remaster-подхода.
* **A. Introduction** — смена адресата программирования: от инструктажа машины к объяснению человеку.
* **B. The WEB System** — WEB как система, порождающая человеческую и машинную проекции из одного источника.
* **C–F. Example / source / tangle / weave** — пример Кнута с простыми числами, исходный WEB-файл, TANGLE, WEAVE и облегчённый C++-ремастер.
* **G. Additional Bells and Whistles** — переход от учебного примера к производственной сложности.
* **H. Occam’s Razor** — ограничение инструмента и необходимость методологической сдержанности.
* **I. Portability** — переносимость за пределы исходной пары TeX / Pascal и современная роль воспроизводимых окружений.
* **J. Programs as Webs** — программы как сети именованных фрагментов, зависимостей и объяснительных связей.
* **K. Stylistic Issues** — именование секций, читаемая структура и инженерная роль стиля.
* **L. Economic Issues** — цена и выгоды literate-дисциплины.
* **M. Related Work** — structured programming, документационные системы, executable documents и смежные линии.
* **N. Retrospect and Prospects** — ретроспективная оценка метода и его перспективы.

### Выводы

* **1. Что именно предложил Дональд Кнут**
* **2. Что сохранилось, а что сменило форму**
* **3. Цена метода и границы применимости**
* **4. LLM: продолжение идеи или новая форма разрыва**
* **5. Где идея может работать дальше**

## Companion-набор

[Companion-набор](02-Literate-Companion-Implementations/README.md) включает воспроизводимые примеры:

* `01-cweb` — канонический CWEB-маршрут с ветками `tangle / weave`;
* `02-noweb-like` — основной облегчённый C++-ремастер с `tangle-first workflow`;
* `03-org-babel` — plain-text workflow в Org-mode / Emacs;
* `04-quarto` — executable-document маршрут для computational publishing;
* `05-jupyter` — notebook-маршрут с вниманием к hidden state и воспроизводимому выполнению;
* `06-rmarkdown` — reproducible-report workflow на R Markdown / knitr / Pandoc;
* `07-prompt-literate` — граничный пример применения Prompt-Literate Workflow к задаче Кнута о простых числах.

Детерминированные примеры и LLM-граничный пример намеренно разделены. Вывод LLM рассматривается как кандидатный артефакт, требующий review, tests, smoke-check и TRACE, а не как детерминированный build artifact.
</details>