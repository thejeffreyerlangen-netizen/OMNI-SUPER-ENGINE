#!/bin/bash
set -e

echo "Installing virtual environment for Super Engine Omni v7.0..."
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo "Installation complete."
