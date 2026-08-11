#!/usr/bin/env python3
"""Validate structural equivalence across localized prime examples."""

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

    name: str
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
    """Compare localized prime examples without requiring prose equivalence."""

    examples: list[LocaleExample]
    errors: list[str] = field(default_factory=list)

    def compare_sets(
        self,
        label: str,
        baseline: LocaleExample,
        baseline_values: set[str],
        candidate: LocaleExample,
        candidate_values: set[str],
    ) -> None:
        only_baseline = sorted(baseline_values - candidate_values)
        only_candidate = sorted(candidate_values - baseline_values)
        if only_baseline:
            self.errors.append(f"{label} only in {baseline.name}: {only_baseline}")
        if only_candidate:
            self.errors.append(f"{label} only in {candidate.name}: {only_candidate}")

    def validate_required_files(self) -> None:
        baseline = self.examples[0]
        baseline_files = baseline.relative_files()
        for example in self.examples:
            files = example.relative_files()
            missing = sorted(REQUIRED_RELATIVE_FILES - files)
            if missing:
                self.errors.append(f"{example.name} example missing required files: {missing}")
            if example is not baseline:
                self.compare_sets("Relative files", baseline, baseline_files, example, files)

    def validate(self) -> list[str]:
        if len(self.examples) < 2:
            return ["At least two localized examples are required"]
        for example in self.examples:
            if not example.root.is_dir():
                self.errors.append(f"{example.name} example is not a directory: {example.root}")
        if self.errors:
            return self.errors
        self.validate_required_files()
        baseline = self.examples[0]
        baseline_plan_chunks, baseline_plan_duplicates = baseline.plan_chunks()
        for duplicate in baseline_plan_duplicates:
            self.errors.append(f"{baseline.name} {duplicate}")
        baseline_contract_chunks = baseline.contract_chunks()
        baseline_scenarios = baseline.scenarios()
        for example in self.examples[1:]:
            plan_chunks, plan_duplicates = example.plan_chunks()
            for duplicate in plan_duplicates:
                self.errors.append(f"{example.name} {duplicate}")
            self.compare_sets("Plan chunks", baseline, baseline_plan_chunks, example, plan_chunks)
            self.compare_sets(
                "Contract chunks",
                baseline,
                baseline_contract_chunks,
                example,
                example.contract_chunks(),
            )
            self.compare_sets("Scenario names", baseline, baseline_scenarios, example, example.scenarios())
        return self.errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("locale_examples", nargs="+", type=Path)
    args = parser.parse_args()

    examples = [
        LocaleExample(path.parent.name.upper(), path.resolve())
        for path in args.locale_examples
    ]
    validator = LocaleEquivalenceValidator(examples)
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
