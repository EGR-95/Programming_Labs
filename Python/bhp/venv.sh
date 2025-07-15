#!/bin/bash

# Check if the virtual environment exists
if [ ! -d .venv-bhp ]; then
    echo "[*] Creating virtual environment: .venv-bhp"
    python3 -m venv .venv-bhp
fi

# Activate the virtual environment
echo "[*] Activating virtual environment: .venv-bhp"
source .venv-bhp/bin/activate

# Optional: Show Python version and pip packages
echo "[*] Python version: $(python --version)"
echo "[*] Pip version: $(pip --version)"

