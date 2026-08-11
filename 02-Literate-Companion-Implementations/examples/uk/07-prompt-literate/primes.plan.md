# Prompt-literate plan: first 1000 primes

Призначення:
Згенерувати і вивести перші 1000 простих чисел у тому самому компонуванні сторінок, рядків і стовпців, що й у noweb-like ремастері.

## Методологічний статус

- Цей файл є канонічним plan для прикладу з простими числами.
- Загальну методологію визначено в `../../../methodology/prompt-literate-workflow/`.
- `CONTRACTS.md` задає контракти чанків.
- `SCENARIOS.md` задає сценарії і критерії прийняття.
- LLM може заповнювати лише чанки з позначкою `LLM-TODO`.
- Усі інші чанки є author-defined обмеженнями.
- Прийнятий generated-code має зберігати цей план; будь-які зміни потрібно відобразити назад у плані.

Канонічні обмеження:
- C++17 або новіша версія.
- Зовнішні залежності заборонені.
- Формат виводу потрібно зберегти:
  `The First 1000 Prime Numbers --- Page 1`
  `The First 1000 Prime Numbers --- Page 5`
- Підсумковий вивід має містити `7919`.
- Ручні правки у generated-коді потребують відображення змін у цьому плані.

Іменовані чанки:
`<<program>>`
`<<constants>>`
`<<types>>`
`<<declarations>>`
`<<prime-generation>>`
`<<table-output>>`

Задана людиною авторська рамка:
`<<program>>`, `<<constants>>`, `<<types>>` і `<<declarations>>` задано автором.
`<<prime-generation>>` і `<<table-output>>` навмисно залишено для LLM-заповнення.

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


Примітка: prompt-файли у каталозі `prompts/` навмисно залишено англійською мовою.
