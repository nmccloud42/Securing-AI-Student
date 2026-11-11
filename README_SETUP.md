
# Securing AI Certification — VS Code Setup

## Overview

The Securing AI Certification uses Jupyter Notebooks
within Visual Studio Code.

Each module includes instructional material,
hands-on Python demonstrations, knowledge checks,
and practical assessments.

## Requirements

- Linux cyber range machine
- Python 3.12
- Visual Studio Code
- Python extension
- Jupyter extension
- Internet access for initial dependency installation

## Initial Installation

Open the Securing-AI-Student repository in VS Code.

Open Terminal > New Terminal.

Run:

    bash install_securing_ai.sh

Wait for installation to finish.

## Select the Notebook Kernel

1. Open a module's .ipynb notebook.
2. Click Select Kernel in the top-right corner.
3. Select Python (Securing AI).
4. Run the notebook cells.

## Working Through Modules

1. Read each instructional section.
2. Run the provided demonstration cells.
3. Review the generated outputs and visualizations.
4. Complete the student activities.
5. Answer the written-response questions.
6. Complete the end-of-module capstone.

## Notebook Display

Demonstration code may be collapsed by default.

Students can run collapsed code cells and inspect
their outputs without expanding the code.

Student coding activities should remain expanded.

Code is hidden for presentation purposes only.
It is not access-restricted.

## Troubleshooting

### Missing ipykernel

Run:

    bash install_securing_ai.sh

Then select Python (Securing AI).

### Missing Python package

Activate the environment:

    source .venv/bin/activate

Install dependencies:

    python -m pip install -r requirements.txt

### Notebook visualization does not appear

Confirm the cell ran successfully.

For Matplotlib, use:

    plt.show()

For DataFrames, use:

    display(df)

### Incorrect Python kernel

Select the Python (Securing AI) kernel in VS Code.

## Instructor Setup

Before distributing the notebooks, instructors can
prepare their code-cell visibility by running:

    python3 scripts/prepare_notebooks.py

Review the resulting notebooks before committing
the changes to GitHub.
