# CONTRACTS (example-specific): Prompt-Literate Workflow for primes

## Chunk: `<<program>>`
- **Role:** Program assembly frame and execution order.
- **Status:** author-defined.
- **Inputs:** Includes, constants/types/declarations chunks, function definitions.
- **Outputs:** Complete compilable translation unit structure.
- **Allowed changes:** None unless the plan is explicitly revised first.
- **Forbidden changes:** Architecture reordering, `main()` changes, external dependencies.
- **Acceptance criteria:** Preserved exactly as in the plan.

## Chunk: `<<constants>>`
- **Role:** Canonical constants for output layout and prime count.
- **Status:** author-defined.
- **Inputs:** Human-authored plan constraints.
- **Outputs:** `PRIME_COUNT`, `ROWS_PER_PAGE`, `COLUMNS_PER_PAGE`, `COLUMN_WIDTH`.
- **Allowed changes:** None by LLM.
- **Forbidden changes:** Any constant value/name change.
- **Acceptance criteria:** Values unchanged; output markers remain reachable.

## Chunk: `<<types>>`
- **Role:** Public local type alias.
- **Status:** author-defined.
- **Inputs:** Standard library vector type.
- **Outputs:** `using PrimeTable = std::vector<int>;`.
- **Allowed changes:** None by LLM.
- **Forbidden changes:** Alias rename or type replacement.
- **Acceptance criteria:** Declaration preserved exactly.

## Chunk: `<<declarations>>`
- **Role:** Public function declarations for generation and output.
- **Status:** author-defined.
- **Inputs:** Plan-defined interfaces.
- **Outputs:** Stable signatures for `generate_primes`, `is_prime_candidate`, `print_table`.
- **Allowed changes:** None by LLM.
- **Forbidden changes:** Signature changes, removed/added public declarations.
- **Acceptance criteria:** Signatures preserved exactly.

## Chunk: `<<prime-generation>>`
- **Role:** Generate exactly the first 1000 primes according to declared interfaces.
- **Status:** LLM-fillable.
- **Inputs:** `PRIME_COUNT`, `PrimeTable`, `is_prime_candidate` declaration.
- **Outputs:** Definitions for `generate_primes` and `is_prime_candidate` returning correct primes.
- **Allowed changes:** Only implementation logic inside this chunk.
- **Forbidden changes:** Changing declarations, constants, chunk names, architecture, or dependencies.
- **Acceptance criteria:**
  - Starts from prime `2`.
  - Tests only odd candidates after initial prime.
  - Uses already found primes for divisibility checks.
  - Stops divisibility checks when `p > candidate / p`.
  - Returns exactly `PrimeTable` with `count` primes.

## Chunk: `<<table-output>>`
- **Role:** Print prime table in Knuth-like paginated layout.
- **Status:** LLM-fillable.
- **Inputs:** `PrimeTable`, `ROWS_PER_PAGE`, `COLUMNS_PER_PAGE`, `COLUMN_WIDTH`.
- **Outputs:** `print_table` implementation with exact headers and page traversal.
- **Allowed changes:** Only printing logic inside this chunk.
- **Forbidden changes:** Header format changes, layout reinterpretation, signature changes.
- **Acceptance criteria:**
  - Prints headers as `The First 1000 Prime Numbers --- Page N`.
  - Preserves row/column pagination based on constants.
  - Output contains Page 1 and Page 5 markers.
  - Output includes prime `7919`.
