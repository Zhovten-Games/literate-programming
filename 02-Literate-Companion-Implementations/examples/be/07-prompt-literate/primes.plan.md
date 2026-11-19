# Prompt-literate план: першыя 1000 простых лікаў

Прызначэнне: згенераваць і надрукаваць першую тысячу простых лікаў у тым жа парадку старонак, радкоў і слупкоў, што і ў noweb-падобнай рэалізацыі.

## Метадалагічны статус

- Гэта кананічны план прыкладу простых лікаў.
- Агульны метад знаходзіцца ў `../../../methodology/prompt-literate-workflow/`.
- `CONTRACTS.md` задае кантракты фрагментаў, `SCENARIOS.md` — сцэнарыі і крытэрыі прыняцця.
- LLM запаўняе толькі фрагменты з `LLM-TODO`.
- Астатнія фрагменты вызначаны аўтарам і задаюць абмежаванні.
- Прыняты згенераваны код захоўвае план; змены адлюстроўваюцца назад у плане.

Кананічныя абмежаванні: C++17 або навейшы; знешнія залежнасці забаронены; загалоўкі `The First 1000 Prime Numbers --- Page 1` і `The First 1000 Prime Numbers --- Page 5` захоўваюцца; вынік утрымлівае `7919`; ручныя праўкі згенераванага кода патрабуюць адлюстравання ў плане.

Іменаваныя фрагменты: `<<program>>`, `<<constants>>`, `<<types>>`, `<<declarations>>`, `<<prime-generation>>`, `<<table-output>>`.

Аўтар вызначае рамку `<<program>>`, канстанты, тыпы і дэкларацыі. `<<prime-generation>>` і `<<table-output>>` пакідаюцца для LLM.

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

Промпты і машыначытальныя кантрактныя палі захоўваюць англійскую форму.
