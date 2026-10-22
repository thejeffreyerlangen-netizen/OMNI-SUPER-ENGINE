# OMNI SUPER ENGINE v7.0 (CORE 7)

A compact physics-focused simulation and validation project centered on a symplectic invariant layer, a Ziolkowski stage model, and a hyper-viscous Navier–Stokes smoothing bridge.

## Overview

OMNI SUPER ENGINE v7.0 is a lightweight engineering and research-oriented Python project that combines three core ideas:

- Symplectic invariant enforcement via determinant scaling
- Ziolkowski stage mass/propellant translation for lossless trajectory assumptions
- H² Sobolev-style smoothing for stable fluid-field evolution

The repository is structured around a master engine implementation and a validation suite that exercises the physics bridge and runtime behavior.

## Features

- Symplectic invariant enforcement with `det(J) == 1.0`
- Ziolkowski upper-stage mass model
- H² smoothing layer for flow-field stabilization
- Master engine evolution cycle
- Automated tests in `tests/test_omni_physics_bridge.py`
- Clean local setup via `install.sh`

## Repository structure

```text
OMNI-SUPER-ENGINE/
├── README.md
├── install.sh
├── requirements.txt
├── pytest.ini
├── pyproject.toml
├── omni_super_engine_master_v7.py
├── run_v7_test_suite.py
├── tests/
│   └── test_omni_physics_bridge.py
├── .gitignore
└── additional legacy/packaged artifacts
```

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
```

For the bundled test runner:

```bash
python run_v7_test_suite.py
```

## Core usage example

```python
import numpy as np
from omni_super_engine_master_v7 import SuperEngineOmniCore7Master

engine = SuperEngineOmniCore7Master()
engine.initialize_state(np.linspace(1.0, 2.0, 20))

result = engine.execute_evolution_cycle(
    physics_mode="ziolkowski",
    m_payload=5000,
    isp=450,
    delta_v=4500,
    structural_ratio=0.10,
)

print(result)
```

## Validation

The project includes a focused validation suite for:

- symplectic invariant enforcement
- Ziolkowski stage translation
- hyperviscous smoothing
- complete master-engine execution cycle

Run:

```bash
python -m pytest -q
```

## Notes

This repository contains both active v7.0 files and legacy packaging artifacts. The active code path is centered on `omni_super_engine_master_v7.py` and the tests in `tests/`.

## License

No explicit license file is currently present in the repository; use this project with care and respect the repository owner’s terms in the GitHub project context.
