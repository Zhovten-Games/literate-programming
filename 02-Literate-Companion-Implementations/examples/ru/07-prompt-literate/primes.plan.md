# Prompt-literate plan: first 1000 primes

Назначение:
Сгенерировать и вывести первые 1000 простых чисел в той же раскладке страниц/строк/колонок, что и в noweb-like ремастере.

## Методологический статус

- Этот файл — канонический plan для примера с простыми числами.
- Общая методология определена в `../../../methodology/prompt-literate-workflow/`.
- `CONTRACTS.md` задаёт контракты чанков.
- `SCENARIOS.md` задаёт сценарии и критерии приёмки.
- Только чанки с меткой `LLM-TODO` могут заполняться LLM.
- Все остальные чанки являются author-defined ограничениями.
- Принятый generated-code должен сохранять этот план или изменения должны быть отражены обратно в нём.

Канонические ограничения:
- C++17 или новее.
- Не использовать внешние зависимости.
- Сохранить формат вывода:
  `The First 1000 Prime Numbers --- Page 1`
  `The First 1000 Prime Numbers --- Page 5`
- В итоговом выводе обязательно должно присутствовать `7919`.
- Не вносить ручные правки в generated-код без отражения изменений в этом плане.

Именованные чанки:
`<<program>>`
`<<constants>>`
`<<types>>`
`<<declarations>>`
`<<prime-generation>>`
`<<table-output>>`

Человеко-авторская рамка:
`<<program>>`, `<<constants>>`, `<<types>>` и `<<declarations>>` заданы автором.
`<<prime-generation>>` и `<<table-output>>` намеренно оставлены для LLM-заполнения.

```text
<<program>>=
#include <cstddef>
#include <iomanip>
#include <iostream>
#include <vector>

<<constants>>
<<types>>
<<declarations>>

int main() {
    const auto primes = generate_primes(PRIME_COUNT);
    print_table(primes);
    return 0;
}

<<prime-generation>>
<<table-output>>
@

<<constants>>=
constexpr std::size_t PRIME_COUNT = 1000;
constexpr std::size_t ROWS_PER_PAGE = 50;
constexpr std::size_t COLUMNS_PER_PAGE = 4;
constexpr int COLUMN_WIDTH = 10;
@

<<types>>=
using PrimeTable = std::vector<int>;
@

<<declarations>>=
PrimeTable generate_primes(std::size_t count);
bool is_prime_candidate(int candidate, const PrimeTable& primes);
void print_table(const PrimeTable& primes);
@

<<prime-generation>>=
[[LLM-TODO:
Fill this chunk with C++ code that:
- starts with prime 2;
- tests only odd candidates;
- uses already found primes for divisibility checks;
- stops divisibility testing when p > candidate / p;
- returns exactly `PrimeTable`.
Do not change chunk names or public declarations.
]]
@

<<table-output>>=
[[LLM-TODO:
Fill this chunk with C++ code that:
- prints pages in the required Knuth-like format;
- keeps rows/columns layout via ROWS_PER_PAGE/COLUMNS_PER_PAGE;
- preserves output header format exactly;
- does not change function signature.
]]
@
```


Примечание: prompt-файлы в каталоге `prompts/` намеренно оставлены на английском языке.
