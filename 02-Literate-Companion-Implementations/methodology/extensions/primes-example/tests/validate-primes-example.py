#!/usr/bin/env python3
"""Validate article-local prime-number extension markers in expected files."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path

REQUIRED_FILES = (
    "primes.plan.md",
    "CONTRACTS.md",
    "SCENARIOS.md",
    "TRACE.md",
    "output.expected.txt",
    "tests/smoke-check.sh",
)
FILE_MARKERS = {
    "primes.plan.md": ("LLM-TODO",),
    "CONTRACTS.md": ("LLM-fillable",),
    "SCENARIOS.md": ("7919", "Page 1", "Page 5"),
    "output.expected.txt": ("7919", "Page 1", "Page 5"),
    "tests/smoke-check.sh": ("7919", "Page 1", "Page 5"),
}


@dataclass
class PrimeExampleValidator:
    """Validator for the article-local prime-number extension only."""

    example_dir: Path
    errors: list[str] = field(default_factory=list)

    def read(self, relative_path: str) -> str:
        return (self.example_dir / relative_path).read_text(encoding="utf-8", errors="replace")

    def validate_required_files(self) -> None:
        for relative_path in REQUIRED_FILES:
            path = self.example_dir / relative_path
            if not path.is_file():
                self.errors.append(f"Missing required file: {path}")

    def validate_file_markers(self) -> None:
        for relative_path, markers in FILE_MARKERS.items():
            path = self.example_dir / relative_path
            if not path.is_file():
                continue
            text = self.read(relative_path)
            for marker in markers:
                if marker not in text:
                    self.errors.append(f"{relative_path} must contain marker: {marker}")

    def validate(self) -> list[str]:
        if not self.example_dir.is_dir():
            return [f"Example directory is not a directory: {self.example_dir}"]
        self.validate_required_files()
        self.validate_file_markers()
        return self.errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("example_dir", type=Path)
    args = parser.parse_args()

    validator = PrimeExampleValidator(args.example_dir.resolve())
    errors = validator.validate()
    if errors:
        print("primes-example validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("primes-example validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
