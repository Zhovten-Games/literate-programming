PRIME_COUNT = 1000
ROWS_PER_PAGE = 50
COLUMNS_PER_PAGE = 4
COLUMN_WIDTH = 10


def generate_primes(count: int) -> list[int]:
    primes = []
    if count == 0:
        return primes
    primes.append(2)
    candidate = 3
    while len(primes) < count:
        is_prime = True
        for p in primes:
            if p > candidate // p:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    return primes


def print_table(primes: list[int]) -> None:
    page_number = 1
    page_offset = 0
    while page_offset < len(primes):
        print(f"The First {len(primes)} Prime Numbers --- Page {page_number}\n")
        for row in range(ROWS_PER_PAGE):
            line = []
            for column in range(COLUMNS_PER_PAGE):
                index = page_offset + row + column * ROWS_PER_PAGE
                if index < len(primes):
                    line.append(f"{primes[index]:>{COLUMN_WIDTH}}")
            print("".join(line))
        print()
        page_number += 1
        page_offset += ROWS_PER_PAGE * COLUMNS_PER_PAGE


if __name__ == "__main__":
    print_table(generate_primes(PRIME_COUNT))
