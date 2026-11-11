
#!/usr/bin/env bash

# ==========================================================
# Securing AI Certification
# Automated Environment Installation
# ==========================================================

set -euo pipefail

echo "=========================================="
echo " Securing AI - Environment Setup"
echo "=========================================="

# Move to repository root
cd "$(dirname "$0")"

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed."
    exit 1
fi

echo "Python detected:"
python3 --version

# Verify requirements file
if [ ! -f requirements.txt ]; then
    echo "ERROR: requirements.txt not found."
    exit 1
fi

# Create virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment..."

    python3 -m venv .venv || {
        echo "Failed to create virtual environment."
        echo "On Ubuntu/Debian, install python3-venv:"
        echo "sudo apt install python3-venv"
        exit 1
    }
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
echo "Updating pip..."
python -m pip install --upgrade pip

# Install dependencies
echo "Installing Securing AI dependencies..."
python -m pip install -r requirements.txt

# Register Jupyter kernel
echo "Registering Jupyter kernel..."

python -m ipykernel install \
    --user \
    --name securing-ai \
    --display-name "Python (Securing AI)"

# Verify installation
echo "Verifying environment..."

python - <<'PY'
import importlib

modules = [
    "ipykernel",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "sklearn",
    "tensorflow",
    "torch",
    "shap",
    "requests",
]

failed = []

for module in modules:
    try:
        importlib.import_module(module)
        print(f"[OK] {module}")
    except Exception as error:
        print(f"[FAILED] {module}: {error}")
        failed.append(module)

if failed:
    raise SystemExit(
        "Installation verification failed: "
        + ", ".join(failed)
    )

print("All checked dependencies are available.")
PY

echo ""
echo "=========================================="
echo " Securing AI Setup Complete!"
echo "=========================================="
echo ""
echo "Open a notebook in VS Code."
echo "Select Kernel -> Python (Securing AI)"
echo "Run your notebook cells."
