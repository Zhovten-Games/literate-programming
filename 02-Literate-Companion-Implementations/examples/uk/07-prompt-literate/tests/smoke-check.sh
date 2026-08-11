#!/usr/bin/env bash
# This checks accepted generated artifacts.
# This is not the same as Prompt-Literate Workflow method validation.
# It may fail before generation, which is expected.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GEN_FILE="$ROOT_DIR/generated/primes.generated.cpp"
BIN_FILE="$ROOT_DIR/generated/primes.generated"
OUT_FILE="$ROOT_DIR/generated/output.txt"

if [[ ! -f "$GEN_FILE" ]]; then
  echo "No generated file found. Run an LLM with prompts/fill-chunks.prompt.md and place the reviewed result in generated/primes.generated.cpp."
  exit 1
fi

g++ -std=c++17 -Wall -Wextra -pedantic "$GEN_FILE" -o "$BIN_FILE"
"$BIN_FILE" > "$OUT_FILE"

grep -F "The First 1000 Prime Numbers --- Page 1" "$OUT_FILE"
grep -F "The First 1000 Prime Numbers --- Page 5" "$OUT_FILE"
grep -F "7919" "$OUT_FILE"

echo "Smoke-check passed."
