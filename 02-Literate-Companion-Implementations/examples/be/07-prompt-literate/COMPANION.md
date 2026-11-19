# Суправаджальны прыклад

`07-prompt-literate` дэманструе граничнае прымяненне **Prompt-Literate Workflow** да задачы простых лікаў Кнута.

Базавая методыка даступная тут:

```text
../../../methodology/prompt-literate-workflow/
```

Яна сінхранізаваная з публічным рэпазіторыем і каранёвым submodule/scaffold праекта `literate-programming`:

```text
https://github.com/IRONCREED/prompt-literate-workflow
```

Спецыялізацыя задачы простых лікаў:

```text
../../../methodology/extensions/primes-example/
```

Прыклад дэманструе лакальнае дапаўняльнае пашырэнне паўторна выкарыстоўванай методыкі. `CONTRACTS.md` і `SCENARIOS.md` задаюць патрабаванні гэтай задачы. Промпты захоўваюцца па-англійску для пераноснасці паміж інструментамі і мадэлямі.

Гэты праход мае статус планавання. Стварэнне і прыняцце згенераванай рэалізацыі, запаўненне `LLM-TODO` і даданне згенераванага кода тут забаронены.

## Праверка

З каталога прыкладу:

```bash
python ../../../methodology/prompt-literate-workflow/scripts/validate-project.py --project . --state generation-ready
python ../../../methodology/extensions/primes-example/tests/validate-primes-example.py .
```

Базавы валідатар правярае дысцыпліну працэсу, лакальны — маркеры простых лікаў `7919`, `Page 1`, `Page 5`.
