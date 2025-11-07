#!/usr/bin/env python3
import json
import pathlib
from typing import Dict, List, Tuple


def load_example(file_path: pathlib.Path) -> Tuple[str, str, str]:
    """Return (title, comment, data_json) from an example JSON file.
    Falls back sensibly if keys are missing.
    """
    text = file_path.read_text(encoding="utf-8")
    title = file_path.stem
    comment = ""
    data_str = text
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            title = obj.get("title", title)
            comment = obj.get("comment", "")
            data = obj.get("data", obj)
            data_str = json.dumps(data, indent=2, ensure_ascii=False)
    except Exception:
        # Keep raw content
        pass
    return title, comment, data_str


def collect_examples(examples_dir: pathlib.Path) -> Dict[str, List[pathlib.Path]]:
    """Group example files by relative subdirectory.
    Returns mapping: section_name -> list of file paths
    The root directory is grouped under 'General'.
    """
    groups: Dict[str, List[pathlib.Path]] = {}
    for path in sorted(examples_dir.rglob("*.json")):
        # Ignore README.json or other non-example files if any naming convention exists; none specified, so include all
        if path.name.lower() == "package.json":
            continue
        rel = path.relative_to(examples_dir)
        section = rel.parent.as_posix() if rel.parent != pathlib.Path(".") else "General"
        groups.setdefault(section, []).append(path)
    return dict(sorted(groups.items(), key=lambda kv: kv[0].lower()))


def build_readme_content(examples_dir: pathlib.Path) -> str:
    header = (
        "---\n"
        "layout: readme\n"
        "title: FIRE data examples\n"
        "---\n\n"
        "This README is generated from files in the `examples/` directory.\n\n"
    )

    groups = collect_examples(examples_dir)
    lines: List[str] = [header]

    # Build contents section
    lines.append("## Contents\n")
    contents_lines: List[str] = []
    for section, files in groups.items():
        section_anchor = section.lower().replace(" ", "-")
        contents_lines.append(f"- [{section.title()}](#{section_anchor})")
        for fp in sorted(files, key=lambda p: p.name.lower()):
            title, _, _ = load_example(fp)
            entry_anchor = title.lower().replace("_", "-").replace(" ", "-")
            contents_lines.append(f"  - [{title.replace('_', ' ').title()}](#{entry_anchor})")
    lines.extend(contents_lines)
    lines.append("")

    for section, files in groups.items():
        # Section heading
        lines.append(f"## {section.title()}\n")
        for fp in sorted(files, key=lambda p: p.name.lower()):
            title, comment, data_str = load_example(fp)
            # Block heading
            lines.append(f"#### {title.replace('_', ' ').title()}\n")
            if comment:
                lines.append(f"{comment}\n")
            # Inline JSON data block
            lines.append("```json")
            lines.append(data_str)
            lines.append("```")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    examples_dir = repo_root / "examples"
    out_file = examples_dir / "README.md"

    content = build_readme_content(examples_dir)
    if not out_file.exists() or out_file.read_text(encoding="utf-8") != content:
        out_file.write_text(content, encoding="utf-8")
        print(f"Wrote {out_file}")
        return 1
    print("No changes needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


