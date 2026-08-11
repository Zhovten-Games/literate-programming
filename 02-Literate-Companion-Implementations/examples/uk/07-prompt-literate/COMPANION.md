# Companion

`07-prompt-literate` — локальний для статті граничний приклад **Prompt-Literate Workflow** у застосуванні до задачі Кнута про прості числа.

Базова методологія доступна тут:

```text
../../../methodology/prompt-literate-workflow/
```

Її синхронізовано з публічним репозиторієм Prompt-Literate Workflow і кореневим submodule/scaffold у `literate-programming`:

```text
https://github.com/IRONCREED/prompt-literate-workflow
```

Спеціалізацію для задачі про прості числа визначено тут:

```text
../../../methodology/extensions/primes-example/
```

Цей приклад показує локальне additive-розширення поверх повторно використовуваної базової методології та не перевизначає Prompt-Literate Workflow.

`CONTRACTS.md` і `SCENARIOS.md` стосуються саме задачі про прості числа. Prompt files у `prompts/` навмисно залишено англійською для переносності між tools and models.

Generated output у цьому проході не створюється і не приймається. Заповнення `LLM-TODO` chunks і створення generated implementation code на цьому етапі заборонене.

## Validation commands

Із цього каталогу прикладу виконайте:

```bash
python ../../../methodology/prompt-literate-workflow/scripts/validate-project.py --project . --state generation-ready
python ../../../methodology/extensions/primes-example/tests/validate-primes-example.py .
```

Базовий validator перевіряє workflow discipline. Локальний validator перевіряє prime-specific markers: `7919`, `Page 1` і `Page 5`.
