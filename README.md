# OMNI SUPER ENGINE v7.0 (CORE 7)

Super Engine Omni (v7.0): M-DSL IR-Kernel for Navier-Stokes and field PDEs. High-performance vectorized simulation framework with H² Sobolev damping for deterministic plasma stability, reactor safety, and safety-critical continuum dynamics.

## Overview

OMNI SUPER ENGINE v7.0 is a lightweight engineering and research-oriented implementation centered on three core ideas:

- symplectic invariant enforcement via determinant scaling
- Ziolkowski upper-stage mass and trajectory translation
- H² Sobolev-inspired smoothing for stable flow-field evolution

The active project code lives under `src/omni_engine/`. Validation suites are in `tests/`.

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
│   └── omni_engine/          # Active source (master_v7, core7, …)
├── tests/                    # Unit / validation tests
├── docs/                     # Project status, notes, chapter drafts
├── data/
│   └── qe6d/                 # CSV export data
├── reports/
│   ├── figures/              # PNG visualizations
│   └── pdfs/                 # Reports and documentation PDFs
├── scripts/                  # Install, test runners, utilities
├── config/                   # (reserved)
├── archive/                  # Historical zip packages
└── legacy/                   # Full older version trees
```

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

## Notes on layout

- **Active code**: `src/omni_engine/`
- **Historical / duplicate bundles** (v4.x, v6.x, earlier v7 packages, mensah packages, matlab exports) are kept under `legacy/` and as zips under `archive/` for reference. They are not required for the active engine workflow.
