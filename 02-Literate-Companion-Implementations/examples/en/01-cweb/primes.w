@* Printing the first thousand primes (CWEB style).

@c
@<Includes@>
@<Constants@>
@<Global state@>
@<Function declarations@>

int main(void) {
  @<Prime generation@>
  @<Table output@>
  return 0;
}

@<Function definitions@>

@ @<Includes@>=
#include <stdio.h>

@ @<Constants@>=
#define PRIME_COUNT 1000
#define ROWS_PER_PAGE 50
#define COLUMNS_PER_PAGE 4
#define COLUMN_WIDTH 10

@ @<Global state@>=
int primes[PRIME_COUNT];

@ @<Function declarations@>=
int is_prime_candidate(int candidate, int current_count);
void generate_primes(void);
void print_table(void);

@ @<Prime generation@>=
generate_primes();

@ @<Table output@>=
print_table();

@ @<Function definitions@>=
int is_prime_candidate(int candidate, int current_count) {
  for (int i = 0; i < current_count; ++i) {
    int p = primes[i];
    if (p > candidate / p) return 1;
    if (candidate % p == 0) return 0;
  }
  return 1;
}

void generate_primes(void) {
  int count = 0;
  primes[count++] = 2;
  for (int candidate = 3; count < PRIME_COUNT; candidate += 2) {
    if (is_prime_candidate(candidate, count)) {
      primes[count++] = candidate;
    }
  }
}

void print_table(void) {
  int page_number = 1;
  int page_offset = 0;
  while (page_offset < PRIME_COUNT) {
    printf("The First %d Prime Numbers --- Page %d\n\n", PRIME_COUNT, page_number);
    for (int row = 0; row < ROWS_PER_PAGE; ++row) {
      for (int column = 0; column < COLUMNS_PER_PAGE; ++column) {
        int index = page_offset + row + column * ROWS_PER_PAGE;
        if (index < PRIME_COUNT) printf("%*d", COLUMN_WIDTH, primes[index]);
      }
      printf("\n");
    }
    printf("\n");
    ++page_number;
    page_offset += ROWS_PER_PAGE * COLUMNS_PER_PAGE;
  }
}
