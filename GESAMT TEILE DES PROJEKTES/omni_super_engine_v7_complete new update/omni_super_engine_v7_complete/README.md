# Super Engine Omni v7.0 (Core 7)

Mathematical simulation and computation framework for continuum mechanics, Navier-Stokes with hyperviscosity (H² Sobolev smoothing), and Ziolkowski rocket dynamics.

## Quickstart (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_v7_test_suite.py
```

## Quickstart (bash / Linux / macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_v7_test_suite.py
```

## Validation

```bash
python -m pytest -q
```
