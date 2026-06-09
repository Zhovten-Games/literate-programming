# Prompt-literate plan: first 1000 primes

Purpose:
Generate and print the first 1000 prime numbers in the same page/row/column layout used by the noweb-like remaster.

## Methodological status

- This file is the canonical plan for the prime-number example.
- The general method is defined in `../../../methodology/prompt-literate-workflow/`.
- `CONTRACTS.md` defines chunk contracts.
- `SCENARIOS.md` defines acceptance scenarios and criteria.
- Only chunks marked `LLM-TODO` may be filled by the LLM.
- All other chunks are author-defined constraints.
- Accepted generated code must preserve this plan or be reflected back into it.

Canonical constraints:
- C++17 or later.
- Do not use external dependencies.
- Keep output format:
  `The First 1000 Prime Numbers --- Page 1`
  `The First 1000 Prime Numbers --- Page 5`
- Final output must contain `7919`.
- Do not edit generated code manually without reflecting the change in this plan.

Named chunks:
`<<program>>`
`<<constants>>`
`<<types>>`
`<<declarations>>`
`<<prime-generation>>`
`<<table-output>>`

Human-authored frame:
`<<program>>`, `<<constants>>`, `<<types>>`, and `<<declarations>>` are specified by the author.
`<<prime-generation>>` and `<<table-output>>` are intentionally left as LLM-fillable chunks.

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

Note: prompt files in `prompts/` are intentionally kept in English.
