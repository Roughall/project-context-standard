#!/usr/bin/env python3
"""Minimal standard-library validator for required context files and project.yaml."""
from pathlib import Path
import sys

REQUIRED = [
    "AGENTS.md", "project.yaml", "PROJECT_STATUS.md", "ARCHITECTURE.md",
    "DECISIONS.md", "TEST_RESULTS.md", "CHANGELOG.md", "HANDOFF.md"
]

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    missing = [name for name in REQUIRED if not (root / name).is_file()]
    if missing:
        print("FAIL: missing required context files:")
        for name in missing:
            print(f"  - {name}")
        return 1
    manifest = root / "project.yaml"
    try:
        import yaml
    except ImportError:
        print("WARN: required files exist; PyYAML is not installed, so project.yaml syntax was not parsed.")
        print("Install PyYAML with: python -m pip install pyyaml")
        return 2
    try:
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: project.yaml could not be parsed: {exc}")
        return 1
    required_sections = ["schema_version", "project", "repository", "workflow", "paths"]
    missing_sections = [key for key in required_sections if key not in data]
    if missing_sections:
        print("FAIL: missing manifest sections: " + ", ".join(missing_sections))
        return 1
    print("PASS: required files exist and project.yaml parses with required top-level sections.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
