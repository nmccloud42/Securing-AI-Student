
#!/usr/bin/env python3

"""
Securing AI - Notebook Preparation

Collapses demonstration code cells while preserving
student exercises and visible notebook outputs.

Run from the repository root:

    python3 scripts/prepare_notebooks.py
"""

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Student activity markers
EDIT_MARKERS = [
    "TODO",
    "YOUR CODE HERE",
    "STUDENT CODE",
    "FILL IN",
    "COMPLETE THIS",
]

def is_student_activity(cell):
    """Determine whether a code cell should stay expanded."""

    metadata = cell.get("metadata", {})
    tags = metadata.get("tags", [])

    if "student-edit" in tags:
        return True

    source = cell.get("source", "")

    if isinstance(source, list):
        source = "".join(source)

    source_upper = source.upper()

    return any(
        marker in source_upper
        for marker in EDIT_MARKERS
    )


def prepare_notebook(path):
    """Update notebook cell visibility metadata."""

    with path.open("r", encoding="utf-8") as file:
        notebook = json.load(file)

    changed = False
    collapsed = 0
    expanded = 0

    for cell in notebook.get("cells", []):

        if cell.get("cell_type") != "code":
            continue

        metadata = cell.setdefault("metadata", {})

        # Preserve explicitly editable cells
        if is_student_activity(cell):
            desired = False
            expanded += 1
        else:
            desired = True
            collapsed += 1

        if metadata.get("inputCollapsed") != desired:
            metadata["inputCollapsed"] = desired
            changed = True

        if metadata.get("outputCollapsed") is not False:
            metadata["outputCollapsed"] = False
            changed = True

    if changed:
        backup = path.with_suffix(".ipynb.bak")

        if not backup.exists():
            shutil.copy2(path, backup)

        with path.open("w", encoding="utf-8") as file:
            json.dump(
                notebook,
                file,
                indent=1,
                ensure_ascii=False
            )

            file.write("\n")

    return changed, collapsed, expanded


def main():

    notebooks = sorted(ROOT.rglob("*.ipynb"))

    # Exclude local environments and instructor notebooks
    notebooks = [
        path for path in notebooks
        if ".venv" not in path.parts
        and ".git" not in path.parts
        and "Instructor" not in path.name
    ]

    print("=" * 50)
    print("Securing AI - Preparing VS Code Notebooks")
    print("=" * 50)

    for path in notebooks:

        changed, collapsed, expanded = prepare_notebook(path)

        print(f"\nNotebook: {path.relative_to(ROOT)}")
        print(f"  Collapsed code cells: {collapsed}")
        print(f"  Editable code cells: {expanded}")
        print(f"  Updated: {changed}")

    print("\nNotebook preparation complete.")


if __name__ == "__main__":
    main()
