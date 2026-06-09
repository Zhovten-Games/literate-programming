#!/usr/bin/env python3
"""Validate structural equivalence between localized prime examples."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path

REQUIRED_RELATIVE_FILES = {
    "COMPANION.md",
    "CONTRACTS.md",
    "SCENARIOS.md",
    "TRACE.md",
    "generated/.gitkeep",
    "output.expected.txt",
    "primes.plan.md",
    "prompts/fill-chunks.prompt.md",
    "prompts/review-generated-code.prompt.md",
    "tests/smoke-check.sh",
}
NOWEB_CHUNK_DEFINITION_RE = re.compile(r"^<<([^<>\n]+)>>=\s*$", re.MULTILINE)
MARKDOWN_CHUNK_HEADING_RE = re.compile(r"^##\s+Chunk:\s+`<<([^<>`]+)>>`\s*$", re.MULTILINE)
CONTRACT_HEADING_RE = re.compile(r"^##\s+Chunk:\s+`<<([^<>`]+)>>`", re.MULTILINE)
SCENARIO_HEADING_RE = re.compile(r"^##\s+Scenario:\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class LocaleExample:
    """Structured view of one localized example directory."""

    root: Path

    def relative_files(self) -> set[str]:
        return {path.relative_to(self.root).as_posix() for path in self.root.rglob("*") if path.is_file()}

    def text(self, relative_path: str) -> str:
        return (self.root / relative_path).read_text(encoding="utf-8", errors="replace")

    def plan_chunks(self) -> tuple[set[str], list[str]]:
        chunks: set[str] = set()
        duplicates: list[str] = []
        for plan_file in sorted(self.root.glob("*.plan.md")):
            text = plan_file.read_text(encoding="utf-8", errors="replace")
            definitions = [match.group(1).strip() for match in MARKDOWN_CHUNK_HEADING_RE.finditer(text)]
            definitions.extend(match.group(1).strip() for match in NOWEB_CHUNK_DEFINITION_RE.finditer(text))
            for chunk_name in definitions:
                if chunk_name in chunks:
                    duplicates.append(f"Duplicate plan chunk definition <<{chunk_name}>> in {plan_file.relative_to(self.root).as_posix()}")
                    continue
                chunks.add(chunk_name)
        return chunks, duplicates

    def contract_chunks(self) -> set[str]:
        return set(CONTRACT_HEADING_RE.findall(self.text("CONTRACTS.md")))

    def scenarios(self) -> set[str]:
        return set(SCENARIO_HEADING_RE.findall(self.text("SCENARIOS.md")))


@dataclass
class LocaleEquivalenceValidator:
    """Compare RU and EN prime examples without requiring prose equivalence."""

    ru: LocaleExample
    en: LocaleExample
    errors: list[str] = field(default_factory=list)

    def compare_sets(self, label: str, left: set[str], right: set[str]) -> None:
        only_left = sorted(left - right)
        only_right = sorted(right - left)
        if only_left:
            self.errors.append(f"{label} only in RU: {only_left}")
        if only_right:
            self.errors.append(f"{label} only in EN: {only_right}")

    def validate_required_files(self) -> None:
        for locale_name, example in (("RU", self.ru), ("EN", self.en)):
            files = example.relative_files()
            missing = sorted(REQUIRED_RELATIVE_FILES - files)
            if missing:
                self.errors.append(f"{locale_name} example missing required files: {missing}")
        self.compare_sets("Relative files", self.ru.relative_files(), self.en.relative_files())

    def validate(self) -> list[str]:
        for locale_name, example in (("RU", self.ru), ("EN", self.en)):
            if not example.root.is_dir():
                self.errors.append(f"{locale_name} example is not a directory: {example.root}")
        if self.errors:
            return self.errors
        self.validate_required_files()
        ru_plan_chunks, ru_plan_duplicates = self.ru.plan_chunks()
        en_plan_chunks, en_plan_duplicates = self.en.plan_chunks()
        for duplicate in ru_plan_duplicates:
            self.errors.append(f"RU {duplicate}")
        for duplicate in en_plan_duplicates:
            self.errors.append(f"EN {duplicate}")
        self.compare_sets("Plan chunks", ru_plan_chunks, en_plan_chunks)
        self.compare_sets("Contract chunks", self.ru.contract_chunks(), self.en.contract_chunks())
        self.compare_sets("Scenario names", self.ru.scenarios(), self.en.scenarios())
        return self.errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ru_example", type=Path)
    parser.add_argument("en_example", type=Path)
    args = parser.parse_args()

    validator = LocaleEquivalenceValidator(LocaleExample(args.ru_example.resolve()), LocaleExample(args.en_example.resolve()))
    errors = validator.validate()
    if errors:
        print("primes locale-equivalence validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("primes locale-equivalence validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
