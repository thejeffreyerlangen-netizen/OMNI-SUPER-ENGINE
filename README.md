# OMNI SUPER ENGINE v8.2

Deterministic simulation framework for continuum mechanics, Navier–Stokes flow, and relativistic trajectory dynamics.

## Overview

OMNI SUPER ENGINE is a research-oriented Python framework for deterministic field dynamics, symplectic invariants, hyperviscous smoothing, and mission-ready trajectory analysis. The current repository structure keeps the active code and tests in a clean package layout while preserving historical releases in archive and legacy folders.

This release aligns the project with the v8.2 baseline and keeps the active runtime path structured and reproducible.

## Project layout

```text
OMNI-SUPER-ENGINE/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── requirements-full.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── omni_engine/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_engine.py
│   ├── test_omni_physics_bridge.py
│   └── test_release.py
├── examples/
│   ├── basic_demo.py
│   └── singularity_damping.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── RELEASE_NOTES.md
│   └── PROJECT_STATUS.md
├── scripts/
│   ├── install.sh
│   ├── run_v7_test_suite.py
│   └── run_kernel_benchmark.sh
├── assets/
│   ├── figures/
│   ├── graphs/
│   └── reports/
├── archive/
│   └── README.md
├── legacy/
│   └── README.md
└── .venv/   # local environment, not committed
```

## Active runtime

The active Python package lives under `src/omni_engine/` and is the path used by the tests and examples.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
```

## Features

- symplectic invariant enforcement
- Ziolkowski mass / trajectory translation
- hyperviscous smoothing for Navier–Stokes flow
- deterministic evolution-cycle interface
- test-backed engineering workflow

## Notes on legacy artifacts

Historical ZIP files, older package bundles, and research export folders are intentionally kept out of the active runtime path and stored under `archive/` and `legacy/` for reference only.

## Validation

```bash
python -m pytest -q
```

## Version

Current release: v8.2.0
