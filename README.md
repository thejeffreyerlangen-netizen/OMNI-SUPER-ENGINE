# OMNI SUPER ENGINE v7.0 (CORE 7)

Super Engine Omni (v7.0): M-DSL IR-Kernel for Navier-Stokes and field PDEs. High-performance vectorized simulation framework with H² Sobolev damping for deterministic plasma stability, reactor safety, and safety-critical continuum dynamics.

## Overview

OMNI SUPER ENGINE is a research-oriented computational framework for continuum mechanics, Navier-Stokes equations, and field PDEs. The project combines an M-DSL-based intermediate representation with high-performance numerical kernels and H² Sobolev-inspired smoothing to preserve stability in strongly coupled fluid and field systems.

This repository is designed for deterministic simulation workflows, plasma stability analysis, and safety-critical reactor and continuum dynamics tasks. The active implementation is primarily Python-based, with supporting shell tooling for automation and execution workflows.

## Key capabilities

- M-DSL IR kernel and symbolic / numerical bridge
- symplectic invariant enforcement via determinant scaling
- Ziolkowski upper-stage mass and trajectory translation
- H² Sobolev-inspired hyperviscous smoothing
- validation and regression testing for engineering workflows
- support for numerical stability analysis and simulation research

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
│   └── omni_engine/          # Active source (master_v7, core7, ...)
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

The repository is predominantly Python-based, with a small Shell component for automation and execution support.

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

## Features

- symplectic invariant enforcement with `det(J) == 1.0`
- Ziolkowski upper-stage mass model
- hyperviscous smoothing layer for fluid evolution
- master engine evolution cycle
- automated validation in `tests/`
- compatibility with engineering and research simulation pipelines

## Notes on layout

- **Active code**: `src/omni_engine/`
- **Historical / duplicate bundles** (v4.x, v6.x, earlier v7 packages, mensah packages, Matlab exports) are kept under `legacy/` and as zip archives under `archive/` for reference.
- These historical bundles are not required for the active engine workflow.

## Validation

```bash
python -m pytest -q
```
