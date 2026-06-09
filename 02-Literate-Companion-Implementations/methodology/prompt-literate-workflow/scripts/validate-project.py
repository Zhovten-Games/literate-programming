#!/usr/bin/env python3
"""Validate a project-local Prompt-Literate Workflow application.

Validator state is project readiness. TRACE phase is a run-log concept; the two
concepts are intentionally separate.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path

ALLOWED_STATES = ("planning", "generation-ready", "candidate", "accepted")
ALLOWED_SCENARIO_STATUSES = {
    "documentation-only",
    "script-backed",
    "unit-test-backed",
    "integration-test-backed",
    "adapter-stub-backed",
    "manual-review-only",
    "not-applicable-with-reason",
}
EXECUTABLE_SCENARIO_STATUSES = {
    "script-backed",
    "unit-test-backed",
    "integration-test-backed",
    "adapter-stub-backed",
}
PHASE1_FIELDS = (
    "Phase",
    "Method version",
    "Run id",
    "Model/tool",
    "Date",
    "Prompt file",
    "Input plan version",
    "Contract version",
    "Generated file",
    "Accepted chunks",
    "Rejected chunks",
    "Manual edits",
    "Reviewer",
    "Method validation result",
    "Smoke-check command",
    "Smoke-check result",
    "Test report",
    "Acceptance decision",
    "Notes",
)
PENDING_ALLOWED_IN_CANDIDATE = {
    "Accepted chunks",
    "Rejected chunks",
    "Manual edits",
    "Smoke-check command",
    "Smoke-check result",
    "Test report",
    "Acceptance decision",
}
PLACEHOLDERS = {"", "not-run", "todo", "pending"}
FAILURE_VALUES = {"failed", "fail", "error", "rejected", "not-passed", "not passed", "unsuccessful"}
NOWEB_CHUNK_DEFINITION_RE = re.compile(r"^<<([^<>\n]+)>>=\s*$", re.MULTILINE)
MARKDOWN_CHUNK_HEADING_RE = re.compile(r"^##\s+Chunk:\s+`<<([^<>`]+)>>`\s*$", re.MULTILINE)
CONTRACT_HEADING_RE = re.compile(r"^##\s+Chunk:\s+`<<([^<>`]+)>>`\s*$", re.MULTILINE)
SCENARIO_HEADING_RE = re.compile(r"^##\s+Scenario:\s+(.+?)\s*$", re.MULTILINE)
MARKDOWN_FIELD_RE_TEMPLATE = r"^[ \t]*-?[ \t]*\*\*{field}:\*\*[ \t]*(.*?)[ \t]*$"
TRACE_FIELD_RE_TEMPLATE = r"^[ \t]*-?[ \t]*{field}:[ \t]*(.*?)[ \t]*$"
ANY_MARKDOWN_FIELD_RE = re.compile(r"^[ \t]*-?[ \t]*\*\*[^*\n]+:\*\*", re.MULTILINE)


@dataclass(frozen=True)
class TextBlock:
    """Named markdown block extracted from a heading."""

    name: str
    body: str


@dataclass(frozen=True)
class ChunkDefinition:
    """One chunk definition occurrence in a plan file."""

    name: str
    start: int
    end: int
    source_type: str


@dataclass
class MarkdownExtractor:
    """Reusable markdown extraction helpers."""

    text: str

    def blocks_from_headings(self, heading_re: re.Pattern[str]) -> dict[str, TextBlock]:
        matches = list(heading_re.finditer(self.text))
        blocks: dict[str, TextBlock] = {}
        for index, match in enumerate(matches):
            start = match.end()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(self.text)
            name = match.group(1).strip().strip("`")
            blocks[name] = TextBlock(name=name, body=self.text[start:end])
        return blocks


@dataclass
class ProjectValidator:
    """Reusable validator for one project-local workflow directory."""

    project: Path
    state: str
    errors: list[str] = field(default_factory=list)

    def read_text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8", errors="replace")

    def collect_text(self, paths: list[Path]) -> str:
        return "\n".join(self.read_text(path) for path in paths if path.exists())

    def require_file(self, path: Path, label: str) -> None:
        if not path.is_file():
            self.errors.append(f"Missing required {label}: {path}")

    def candidate_files(self) -> list[Path]:
        generated = self.project / "generated"
        if not generated.is_dir():
            return []
        return [path for path in generated.rglob("*") if path.is_file() and path.name != ".gitkeep"]

    def has_source_of_truth_violation(self) -> bool:
        generated = self.project / "generated"
        if not generated.exists():
            return False
        searchable = [self.project / "CONTRACTS.md", self.project / "SCENARIOS.md", self.project / "TRACE.md"]
        searchable.extend(self.project.glob("*.plan.md"))
        lowered = self.collect_text(searchable).lower()
        suspicious_phrases = (
            "generated output is source of truth",
            "generated artifact is source of truth",
            "generated artifacts are source of truth",
            "generated files are source of truth",
            "source of truth: generated",
        )
        return any(phrase in lowered for phrase in suspicious_phrases)

    def blocks_from_headings_checked(self, text: str, heading_re: re.Pattern[str], duplicate_label: str) -> dict[str, TextBlock]:
        matches = list(heading_re.finditer(text))
        blocks: dict[str, TextBlock] = {}
        seen: set[str] = set()
        for index, match in enumerate(matches):
            start = match.end()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            name = match.group(1).strip().strip("`")
            if name in seen:
                display_name = f"<<{name}>>" if duplicate_label == "CONTRACTS.md chunk section" else name
                self.errors.append(f"Duplicate {duplicate_label}: {display_name}")
                continue
            seen.add(name)
            blocks[name] = TextBlock(name=name, body=text[start:end])
        return blocks

    def extract_contract_blocks(self, contracts_text: str) -> dict[str, TextBlock]:
        return self.blocks_from_headings_checked(contracts_text, CONTRACT_HEADING_RE, "CONTRACTS.md chunk section")

    def extract_scenario_blocks(self, scenarios_text: str) -> dict[str, TextBlock]:
        return self.blocks_from_headings_checked(scenarios_text, SCENARIO_HEADING_RE, "SCENARIOS.md scenario section")

    def collect_chunk_definitions(self, text: str) -> list[ChunkDefinition]:
        definitions: list[ChunkDefinition] = []
        for match in MARKDOWN_CHUNK_HEADING_RE.finditer(text):
            definitions.append(
                ChunkDefinition(
                    name=match.group(1).strip(),
                    start=match.start(),
                    end=match.end(),
                    source_type="Markdown-heading",
                )
            )
        for match in NOWEB_CHUNK_DEFINITION_RE.finditer(text):
            definitions.append(
                ChunkDefinition(
                    name=match.group(1).strip(),
                    start=match.start(),
                    end=match.end(),
                    source_type="noweb-style",
                )
            )
        return sorted(definitions, key=lambda definition: definition.start)

    def duplicate_message(self, definition: ChunkDefinition, previous: ChunkDefinition, plan_file: Path) -> str:
        if definition.source_type == previous.source_type:
            return f"Duplicate {definition.source_type} chunk definition <<{definition.name}>> in {plan_file}."
        return (
            f"Conflicting duplicate chunk definition <<{definition.name}>> appears in both "
            f"{previous.source_type} and {definition.source_type} forms in {plan_file}."
        )

    def extract_plan_chunk_blocks(self, plan_file: Path) -> dict[str, TextBlock]:
        text = self.read_text(plan_file)
        definitions = self.collect_chunk_definitions(text)
        blocks: dict[str, TextBlock] = {}
        first_definitions: dict[str, ChunkDefinition] = {}
        for index, definition in enumerate(definitions):
            body_start = definition.end
            body_end = definitions[index + 1].start if index + 1 < len(definitions) else len(text)
            if definition.name in first_definitions:
                message = self.duplicate_message(definition, first_definitions[definition.name], plan_file)
                if message not in self.errors:
                    self.errors.append(message)
                continue
            first_definitions[definition.name] = definition
            blocks[definition.name] = TextBlock(name=definition.name, body=text[body_start:body_end])
        return blocks

    def validate_unique_plan_chunks(self, plan_files: list[Path]) -> None:
        first_locations: dict[str, Path] = {}
        for plan_file in plan_files:
            for definition in self.collect_chunk_definitions(self.read_text(plan_file)):
                first_plan_file = first_locations.get(definition.name)
                if first_plan_file is not None and first_plan_file != plan_file:
                    self.errors.append(
                        f"Duplicate plan chunk definition <<{definition.name}>> across plan files: "
                        f"first in {first_plan_file}, again in {plan_file}."
                    )
                    continue
                first_locations[definition.name] = plan_file

    def extract_todo_chunks(self, plan_files: list[Path]) -> dict[str, str]:
        todo_chunks: dict[str, str] = {}
        for plan_file in plan_files:
            for chunk_name, block in self.extract_plan_chunk_blocks(plan_file).items():
                if "LLM-TODO" in block.body:
                    todo_chunks[chunk_name] = str(plan_file)
        return todo_chunks

    def markdown_field_content(self, body: str, field_name: str) -> str | None:
        pattern = re.compile(MARKDOWN_FIELD_RE_TEMPLATE.format(field=re.escape(field_name)), re.MULTILINE)
        match = pattern.search(body)
        if not match:
            return None
        parts = [match.group(1).strip()]
        cursor = match.end()
        next_field = ANY_MARKDOWN_FIELD_RE.search(body, cursor)
        continuation = body[cursor:next_field.start() if next_field else len(body)]
        for line in continuation.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("## "):
                break
            parts.append(stripped)
        return "\n".join(part for part in parts if part).strip()

    def trace_field_value(self, trace_text: str, field_name: str) -> str | None:
        pattern = re.compile(TRACE_FIELD_RE_TEMPLATE.format(field=re.escape(field_name)), re.MULTILINE)
        match = pattern.search(trace_text)
        if not match:
            return None
        return match.group(1).strip()

    def is_placeholder(self, value: str | None) -> bool:
        if value is None:
            return True
        return value.strip().lower() in PLACEHOLDERS

    def is_failure_value(self, value: str | None) -> bool:
        if value is None:
            return False
        return value.strip().lower() in FAILURE_VALUES

    def begins_with_passed(self, value: str | None) -> bool:
        if value is None:
            return False
        return value.strip().lower().startswith("passed")

    def is_documented_pending(self, value: str | None, body: str) -> bool:
        if value is None:
            return False
        lowered_value = value.strip().lower()
        lowered_body = body.lower()
        return lowered_value in {"pending", "not-run"} and (
            "pending" in lowered_body or "not yet" in lowered_body or "not executed" in lowered_body
        )

    def validate_scenarios(self, scenarios_text: str) -> None:
        scenario_blocks = self.extract_scenario_blocks(scenarios_text)
        if not scenario_blocks:
            self.errors.append("SCENARIOS.md must contain at least one ## Scenario: block.")
            return
        required_fields = (
            "Purpose",
            "Input",
            "Expected result",
            "Validation method",
            "Test-backing status",
            "Evidence path or command",
        )
        for scenario_name, block in scenario_blocks.items():
            for field_name in required_fields:
                value = self.markdown_field_content(block.body, field_name)
                if value is None:
                    self.errors.append(f"Scenario '{scenario_name}' missing field: {field_name}.")
                    continue
                if self.is_placeholder(value):
                    if self.state == "planning" and field_name == "Evidence path or command" and self.is_documented_pending(value, block.body):
                        continue
                    self.errors.append(f"Scenario '{scenario_name}' field '{field_name}' must not be empty or a placeholder.")
            status = self.markdown_field_content(block.body, "Test-backing status")
            if status is not None and status not in ALLOWED_SCENARIO_STATUSES:
                allowed = ", ".join(sorted(ALLOWED_SCENARIO_STATUSES))
                self.errors.append(f"Scenario '{scenario_name}' has invalid Test-backing status '{status}'. Allowed: {allowed}.")
            evidence = self.markdown_field_content(block.body, "Evidence path or command")
            if self.state == "accepted" and status in EXECUTABLE_SCENARIO_STATUSES and self.is_placeholder(evidence):
                self.errors.append(f"Accepted executable scenario '{scenario_name}' requires actual non-placeholder evidence.")

    def validate_todo_contracts(self, plan_files: list[Path], contracts_text: str) -> None:
        todo_chunks = self.extract_todo_chunks(plan_files)
        contract_blocks = self.extract_contract_blocks(contracts_text)
        for chunk_name, plan_path in todo_chunks.items():
            contract = contract_blocks.get(chunk_name)
            if contract is None:
                self.errors.append(f"LLM-TODO chunk <<{chunk_name}>> in {plan_path} has no matching contract section.")
                continue
            status = self.markdown_field_content(contract.body, "Status")
            normalized_status = status.rstrip(".") if status else status
            if normalized_status != "LLM-fillable":
                self.errors.append(f"Contract for LLM-TODO chunk <<{chunk_name}>> must contain Status: LLM-fillable.")
            acceptance = self.markdown_field_content(contract.body, "Acceptance criteria")
            if acceptance is None:
                self.errors.append(f"Contract for LLM-TODO chunk <<{chunk_name}>> must contain Acceptance criteria.")
            elif self.is_placeholder(acceptance):
                self.errors.append(f"Contract for LLM-TODO chunk <<{chunk_name}>> must have non-placeholder Acceptance criteria.")

    def validate_common(self, plan_files: list[Path], contracts_text: str, scenarios_text: str, trace_text: str) -> None:
        if not plan_files:
            self.errors.append("At least one *.plan.md file is required.")

        required = (
            (self.project / "CONTRACTS.md", "contracts file"),
            (self.project / "SCENARIOS.md", "scenarios file"),
            (self.project / "TRACE.md", "trace file"),
            (self.project / "prompts" / "fill-chunks.prompt.md", "fill prompt"),
            (self.project / "prompts" / "review-generated-code.prompt.md", "review prompt"),
        )
        for path, label in required:
            self.require_file(path, label)

        self.validate_scenarios(scenarios_text)
        self.validate_unique_plan_chunks(plan_files)
        self.validate_todo_contracts(plan_files, contracts_text)
        if "Phase:" not in trace_text and "- Phase:" not in trace_text:
            self.errors.append("TRACE.md must declare a TRACE phase. Validator state is separate from TRACE phase.")
        if self.has_source_of_truth_violation():
            self.errors.append("Generated outputs must not be treated as source of truth.")

    def validate_generation_ready(self, plan_files: list[Path], contracts_text: str) -> None:
        todo_chunks = self.extract_todo_chunks(plan_files)
        if not todo_chunks:
            self.errors.append("generation-ready state requires at least one LLM-TODO chunk in plan files.")
        if "LLM-fillable" not in contracts_text:
            self.errors.append("generation-ready state requires at least one LLM-fillable contract.")
        if "Acceptance criteria" not in contracts_text:
            self.errors.append("generation-ready state requires acceptance criteria in CONTRACTS.md.")

    def validate_generated_file_link(self, trace_text: str) -> None:
        generated_value = self.trace_field_value(trace_text, "Generated file")
        if self.is_placeholder(generated_value):
            self.errors.append("TRACE.md Generated file must point to an existing file under generated/.")
            return
        assert generated_value is not None
        raw_path = Path(generated_value)
        if raw_path.is_absolute() or ".." in raw_path.parts:
            self.errors.append("TRACE.md Generated file must be a relative path under generated/ without path traversal.")
            return
        if not raw_path.parts or raw_path.parts[0] != "generated":
            self.errors.append("TRACE.md Generated file must be under generated/.")
            return
        target = (self.project / raw_path).resolve()
        generated_root = (self.project / "generated").resolve()
        try:
            target.relative_to(generated_root)
        except ValueError:
            self.errors.append("TRACE.md Generated file resolves outside generated/.")
            return
        if not target.exists():
            self.errors.append(f"TRACE.md Generated file does not exist: {generated_value}")
        elif not target.is_file():
            self.errors.append(f"TRACE.md Generated file must point to a file, not a directory: {generated_value}")

    def validate_candidate(self, trace_text: str, allow_pending: bool) -> None:
        if not self.candidate_files():
            self.errors.append(f"{self.state} state requires at least one generated candidate artifact.")
        for field_name in PHASE1_FIELDS:
            value = self.trace_field_value(trace_text, field_name)
            if value is None:
                self.errors.append(f"TRACE.md missing Phase 1 field: {field_name}.")
                continue
            if self.is_placeholder(value) and not (allow_pending and field_name in PENDING_ALLOWED_IN_CANDIDATE):
                self.errors.append(f"TRACE.md Phase 1 field '{field_name}' must not be empty or a placeholder.")
        self.validate_generated_file_link(trace_text)

    def validate_accepted_success_field(self, trace_text: str, field_name: str) -> None:
        value = self.trace_field_value(trace_text, field_name)
        if self.is_failure_value(value):
            self.errors.append(f"accepted state requires successful {field_name}; got failure-like value: {value}")
        elif not self.begins_with_passed(value):
            self.errors.append(f"accepted state requires {field_name} to begin with 'passed'.")

    def validate_accepted_test_report(self, trace_text: str) -> None:
        value = self.trace_field_value(trace_text, "Test report")
        if self.is_placeholder(value):
            self.errors.append("accepted state requires Test report to be an inline 'passed' result or an existing local report file.")
            return
        if self.is_failure_value(value):
            self.errors.append(f"accepted state requires successful Test report; got failure-like value: {value}")
            return
        assert value is not None
        if self.begins_with_passed(value):
            return

        raw_path = Path(value.strip())
        if raw_path.is_absolute() or ".." in raw_path.parts:
            self.errors.append("accepted state Test report path must be relative and must not use path traversal.")
            return
        target = (self.project / raw_path).resolve()
        project_root = self.project.resolve()
        try:
            target.relative_to(project_root)
        except ValueError:
            self.errors.append("accepted state Test report path resolves outside the project root.")
            return
        if not target.exists():
            self.errors.append(f"accepted state Test report path does not exist: {value}")
        elif not target.is_file():
            self.errors.append(f"accepted state Test report path must point to a file, not a directory: {value}")

    def validate_accepted(self, scenarios_text: str, trace_text: str) -> None:
        acceptance_decision = self.trace_field_value(trace_text, "Acceptance decision")
        if acceptance_decision != "accepted":
            self.errors.append("accepted state requires Acceptance decision: accepted.")

        accepted_chunks = self.trace_field_value(trace_text, "Accepted chunks")
        if accepted_chunks and "LLM-TODO" in accepted_chunks:
            self.errors.append("accepted state must not list unresolved LLM-TODO in Accepted chunks.")

        self.validate_accepted_success_field(trace_text, "Method validation result")
        self.validate_accepted_success_field(trace_text, "Smoke-check result")
        self.validate_accepted_test_report(trace_text)

        evidence_values = [self.trace_field_value(trace_text, "Test report")]
        for block in self.extract_scenario_blocks(scenarios_text).values():
            evidence_values.append(self.markdown_field_content(block.body, "Evidence path or command"))
        if all(self.is_placeholder(value) for value in evidence_values):
            self.errors.append("accepted state requires a non-placeholder test report or scenario evidence path/command.")

    def validate(self) -> list[str]:
        if not self.project.is_dir():
            return [f"Project path is not a directory: {self.project}"]

        plan_files = sorted(self.project.glob("*.plan.md"))
        contracts_text = self.read_text(self.project / "CONTRACTS.md") if (self.project / "CONTRACTS.md").exists() else ""
        scenarios_text = self.read_text(self.project / "SCENARIOS.md") if (self.project / "SCENARIOS.md").exists() else ""
        trace_text = self.read_text(self.project / "TRACE.md") if (self.project / "TRACE.md").exists() else ""

        self.validate_common(plan_files, contracts_text, scenarios_text, trace_text)
        if self.state in {"generation-ready", "candidate"}:
            self.validate_generation_ready(plan_files, contracts_text)
        if self.state == "candidate":
            self.validate_candidate(trace_text, allow_pending=True)
        if self.state == "accepted":
            self.validate_candidate(trace_text, allow_pending=False)
            self.validate_accepted(scenarios_text, trace_text)
        return self.errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    state_group = parser.add_mutually_exclusive_group(required=True)
    state_group.add_argument("--state", choices=ALLOWED_STATES, help="Project readiness state to validate.")
    state_group.add_argument(
        "--phase",
        choices=ALLOWED_STATES,
        help="Backward-compatible alias for --state. TRACE phase and validator state are different concepts.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    state = args.state or args.phase
    validator = ProjectValidator(args.project.resolve(), state)
    errors = validator.validate()
    if errors:
        print("Prompt-Literate Workflow validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Prompt-Literate Workflow validation passed for state: {state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
