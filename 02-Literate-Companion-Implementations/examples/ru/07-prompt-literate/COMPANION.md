# Companion

`07-prompt-literate` — локальный для статьи граничный пример **Prompt-Literate Workflow** применительно к задаче Кнута о простых числах.

Базовая методология доступна здесь:

```text
../../../methodology/prompt-literate-workflow/
```

Она синхронизирована с публичным репозиторием Prompt-Literate Workflow и корневым submodule/scaffold в `literate-programming`:

```text
https://github.com/IRONCREED/prompt-literate-workflow
```

Специализация для задачи о простых числах определена здесь:

```text
../../../methodology/extensions/primes-example/
```

Этот пример не определяет Prompt-Literate Workflow заново. Он показывает локальное добавочное расширение поверх переиспользуемой базовой методологии.

`CONTRACTS.md` и `SCENARIOS.md` относятся именно к задаче о простых числах. Prompt files в `prompts/` намеренно оставлены на английском языке для переносимости между tools and models.

Generated output в этом проходе не создаётся и не принимается. Не заполняйте `LLM-TODO` chunks и не создавайте generated implementation code здесь.

## Validation commands

Из этого каталога примера выполните:

```bash
python ../../../methodology/prompt-literate-workflow/scripts/validate-project.py --project . --state generation-ready
python ../../../methodology/extensions/primes-example/tests/validate-primes-example.py .
```

Базовый validator проверяет workflow discipline. Локальный validator проверяет prime-specific markers: `7919`, `Page 1`, and `Page 5`.
