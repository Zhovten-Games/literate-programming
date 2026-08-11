# Метод Prompt-Literate Workflow

## 1. Призначення

Prompt-Literate Workflow — це метод використання LLM усередині literate-процесу. Він розширює коротку схему `prompt -> code` керованою структурою, у якій LLM працює як виконавець або редактор, а роль архітектора системи за замовчуванням залишається за людиною.

## 2. Центральний workflow

```text
human-authored plan
  -> chunk contracts
  -> bounded prompt
  -> candidate output
  -> review
  -> tests / smoke-check
  -> TRACE
```

## 3. Базові інваріанти

1. Джерело істини — human-authored literate plan.
2. Contract layer є обов’язковим між планом і генерацією.
3. Prompt є операцією над plan/contracts, а не джерелом.
4. Chat log є trace material, а не джерелом.
5. LLM output має статус candidate artifact до явного прийняття implementation.
6. LLM може змінювати лише виразно дозволені chunks.
7. Кожен generated chunk повинен мати contract до generation.
8. Кожен LLM-fillable chunk повинен мати acceptance criteria.
9. Один prompt run відповідає одному запису TRACE.
10. Generated code потребує review перед прийняттям.
11. Generated code потребує smoke-check/tests перед прийняттям.
12. Manual edits to generated code мають бути відображені у plan/contracts/TRACE.
13. Contract changes мають бути внесені до regeneration або acceptance.
14. LLM generation є недетермінованою; validation є детермінованою.
15. Non-reproducible output можна прийняти лише як traced and reviewed artifact.
16. Base methodology і локальні для проєкту extensions є окремими шарами.
17. Project-local extension має зберігати base invariants і виразно оголошувати обмеження.
18. Local extension стає частиною base methodology лише через явний promotion pass.
19. Planning/documentation runs можуть використовувати reduced TRACE.
20. Implementation/generation runs потребують full TRACE.
21. During planning-only runs заборонено фабрикувати generated artifacts, test results, accepted chunks або rejected chunks.
22. Generated artifacts є outputs і ніколи не є source of truth.
23. External authoring/review surfaces є candidate inputs, доки їх не буде normalized, validated, reviewed і committed до canonical source.
24. Every scenario must declare validation/test-backing status.
25. Test без executed або reported статусу не є evidence.
26. Project-specific semantics мають залишатися поза reusable base methodology.
27. Extensions можуть бути additive, restrictive або explanatory і мають оголошувати зв’язок із base invariants.

## 4. Ролі файлів

- `*.plan.md` — canonical human-authored plan із named chunks, constraints та intent.
- `CONTRACTS.md` — обов’язковий contract layer між plan і generation.
- `SCENARIOS.md` — acceptance and validation scenarios, включно з test-backing status.
- `prompts/*.prompt.md` — bounded LLM operations over plan/contracts.
- `generated/` — candidate generated artifacts до acceptance.
- `tests/smoke-check.*` — deterministic checks для accepted або candidate artifacts.
- `TRACE.md` — runs, decisions, acceptance, rejection і validation evidence.

## 5. Етапи процесу

1. Написати або зафіксувати human-authored plan.
2. Визначити named chunks.
3. Додати contracts для кожного LLM-fillable chunk.
4. Додати acceptance criteria і scenarios.
5. Позначити fillable chunks за допомогою `LLM-TODO`.
6. Запустити planning або generation-readiness validation.
7. Запустити LLM через bounded prompt.
8. Приймати лише allowed chunk replacements у межах заданої архітектури.
9. Виконати manual review та/або review prompt.
10. Створювати або оновлювати candidate artifacts лише після чіткого визначення review boundaries.
11. Запустити smoke-check/tests.
12. Записати model/tool, prompt, edits, rejected/accepted chunks і test results до `TRACE.md`.

## 6. Критерії прийняття

Generated result можна прийняти лише за таких умов:

- змінює лише allowed chunks;
- зберігає chunk names;
- зберігає public declarations, якщо інше виразно не дозволено;
- satisfies chunk contracts;
- satisfies scenarios;
- проходить relevant deterministic checks;
- містить required evidence;
- документує manual edits, якщо вони були;
- має updated TRACE.

## 7. Граничний статус

Детермінована частина методу охоплює plan, contracts, validation, tests і TRACE. LLM output залишається залежним від model, version і context, тому зберігає статус candidate до review і validation.
