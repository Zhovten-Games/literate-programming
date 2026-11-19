#include <cstddef>
#include <iomanip>
#include <iostream>
#include <vector>

constexpr std::size_t PRIME_COUNT = 1000;
constexpr std::size_t ROWS_PER_PAGE = 50;
constexpr std::size_t COLUMNS_PER_PAGE = 4;
constexpr int COLUMN_WIDTH = 10;
using PrimeTable = std::vector<int>;
PrimeTable generate_primes(std::size_t count);
bool is_prime_candidate(int candidate, const PrimeTable& primes);
void print_table(const PrimeTable& primes);

int main() {
    const auto primes = generate_primes(PRIME_COUNT);
    print_table(primes);
    return 0;
}

PrimeTable generate_primes(std::size_t count) {
    PrimeTable primes;
    if (count == 0) return primes;
    primes.push_back(2);

    for (int candidate = 3; primes.size() < count; candidate += 2) {
        if (is_prime_candidate(candidate, primes)) {
            primes.push_back(candidate);
        }
    }
    return primes;
}

bool is_prime_candidate(int candidate, const PrimeTable& primes) {
    for (int p : primes) {
        if (p > candidate / p) return true;
        if (candidate % p == 0) return false;
    }
    return true;
}
void print_table(const PrimeTable& primes) {
    std::size_t page_number = 1;
    std::size_t page_offset = 0;

    while (page_offset < primes.size()) {
        std::cout << "The First " << primes.size()
                  << " Prime Numbers --- Page " << page_number << "\n\n";

        for (std::size_t row = 0; row < ROWS_PER_PAGE; ++row) {
            for (std::size_t column = 0; column < COLUMNS_PER_PAGE; ++column) {
                const std::size_t index = page_offset + row + column * ROWS_PER_PAGE;
                if (index < primes.size()) {
                    std::cout << std::setw(COLUMN_WIDTH) << primes[index];
                }
            }
            std::cout << '\n';
        }

        std::cout << '\n';
        ++page_number;
        page_offset += ROWS_PER_PAGE * COLUMNS_PER_PAGE;
    }
}
