# OMNI SUPER ENGINE v8.2

Super Engine Omni (v8.2): deterministic simulation framework for Navier–Stokes, field PDEs, and relativistic trajectory dynamics. The project combines a stable core with configurable evolution layers, hyperviscous smoothing, symplectic guards, and release-ready engineering documentation.

## Overview

OMNI SUPER ENGINE is a research-oriented computational framework for continuum mechanics, Navier–Stokes equations, and field PDEs. The active implementation is focused on deterministic simulation workflows, plasma stability analysis, and safety-critical reactor and continuum dynamics tasks.

This release aligns the repository metadata and documentation with the current v8.2 engineering baseline.

## Key capabilities

- symplectic invariant enforcement via determinant scaling
- Ziolkowski upper-stage mass and trajectory translation
- H² Sobolev-inspired hyperviscous smoothing
- deterministic evolution and stability checks
- validation and regression testing for engineering workflows
- compatibility with research and simulation pipelines

## Repository structure

```text
omni-super-engine/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── pyproject.toml
├── requirements.txt
├── pytest.ini
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── omni_engine/          # Active source
├── tests/                    # Unit / validation tests
├── docs/                     # Project status, notes, chapter drafts
├── data/
│   └── qe6d/                 # CSV export data
├── reports/
│   ├── figures/              # PNG visualizations
│   └── pdfs/                 # Reports and documentation PDFs
├── scripts/                  # Install, test runners, utilities
├── config/                   # Reserved configuration area
├── archive/                  # Historical zip packages
├── legacy/                   # Full older version trees
└── ...
```

## Language profile

The repository is predominantly Python-based, with a small Shell component for execution support and automation.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/run_v7_test_suite.py
# or
python -m pytest -q
```

## Validation

```bash
python -m pytest -q
```

## Version

Current release: v8.2.0

This release keeps the deterministic core stable while aligning the package metadata and documentation with the v8.2 baseline.
