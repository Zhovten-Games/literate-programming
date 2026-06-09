# Метод Prompt-Literate Workflow

## 1. Назначение

Prompt-Literate Workflow — это метод использования LLM внутри literate-процесса. Это не короткая схема `prompt -> code`. LLM здесь работает как исполнитель или редактор внутри структуры, заданной человеком, а не как архитектор системы по умолчанию.

## 2. Центральный workflow

```text
human-authored plan
  -> chunk contracts
  -> bounded prompt
  -> candidate output
  -> review
  -> tests / smoke-check
  -> TRACE
```

## 3. Базовые инварианты

1. Источник истины — human-authored literate plan.
2. Contract layer обязателен между планом и генерацией.
3. Prompt — это операция над plan/contracts, а не источник.
4. Chat log является trace material, а не источником.
5. LLM output — candidate artifact, а не автоматически принятая implementation.
6. LLM может изменять только явно разрешённые chunks.
7. Каждый generated chunk должен иметь contract до generation.
8. Каждый LLM-fillable chunk должен иметь acceptance criteria.
9. Один prompt run соответствует одной записи TRACE.
10. Generated code нельзя принять без review.
11. Generated code нельзя принять без smoke-check/tests.
12. Manual edits to generated code должны быть отражены в plan/contracts/TRACE.
13. Contract changes должны быть внесены до regeneration или acceptance.
14. LLM generation недетерминированна; validation детерминированна.
15. Non-reproducible output может быть принят только как traced and reviewed artifact.
16. Base methodology и локальные для проекта extensions являются отдельными слоями.
17. Project-local extension не должен молча противоречить base invariants.
18. Local extension становится частью base methodology только через явный promotion pass.
19. Planning/documentation runs могут использовать reduced TRACE.
20. Implementation/generation runs требуют full TRACE.
21. During planning-only runs нельзя фабриковать generated artifacts, test results, accepted chunks или rejected chunks.
22. Generated artifacts являются outputs, но никогда source of truth.
23. External authoring/review surfaces являются candidate inputs, пока они не normalized, validated, reviewed и committed в canonical source.
24. Every scenario must declare validation/test-backing status.
25. Test, который не executed или не reported, не является evidence.
26. Project-specific semantics должны оставаться вне reusable base methodology.
27. Extensions могут быть additive, restrictive или explanatory, но должны объявлять связь с base invariants.

## 4. Роли файлов

- `*.plan.md` — canonical human-authored plan с named chunks, constraints и intent.
- `CONTRACTS.md` — обязательный contract layer между plan и generation.
- `SCENARIOS.md` — acceptance and validation scenarios, включая test-backing status.
- `prompts/*.prompt.md` — bounded LLM operations over plan/contracts.
- `generated/` — candidate generated artifacts до acceptance.
- `tests/smoke-check.*` — deterministic checks для accepted или candidate artifacts.
- `TRACE.md` — runs, decisions, acceptance, rejection и validation evidence.

## 5. Этапы процесса

1. Написать или зафиксировать human-authored plan.
2. Определить named chunks.
3. Добавить contracts для каждого LLM-fillable chunk.
4. Добавить acceptance criteria и scenarios.
5. Пометить fillable chunks с помощью `LLM-TODO`.
6. Запустить planning или generation-readiness validation.
7. Запустить LLM через bounded prompt.
8. Принимать только allowed chunk replacements, а не полный redesign.
9. Выполнить manual review и/или review prompt.
10. Создавать или обновлять candidate artifacts только после ясного определения review boundaries.
11. Запустить smoke-check/tests.
12. Записать model/tool, prompt, edits, rejected/accepted chunks и test results в `TRACE.md`.

## 6. Критерии принятия

Generated result может быть принят только если он:

- изменяет только allowed chunks;
- сохраняет chunk names;
- сохраняет public declarations, если обратное не разрешено явно;
- satisfies chunk contracts;
- satisfies scenarios;
- проходит relevant deterministic checks;
- содержит required evidence;
- документирует manual edits, если они были;
- имеет updated TRACE.

## 7. Граничный статус

Детерминированная часть метода — это plan, contracts, validation, tests и TRACE. LLM output остаётся зависимым от model, version и context, поэтому он должен оставаться candidate до review и validation.
