# OMNI SUPER ENGINE v8.2

**Quantum-Topological Simulation Framework**

Deterministic core (symplectic invariants, H² hyperviscosity, relativistic rocketry) plus evolutionary layers: Path-Integral Monte Carlo, adaptive Fourier neural operator, holographic topology (Betti-like defect scoring), and deterministic PDE stabilization.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Features

| Layer | Description |
|-------|-------------|
| **Symplectic guard** | Enforces det(J) = +1 (orientation-preserving) |
| **Omega_key** | Multi-domain resonance tensor (HI-line, Schumann, torsion, …) |
| **Navier–Stokes H²** | Biharmonic hyperviscosity + viscous k² term in Fourier space |
| **Ziolkowski / Ackeret** | Classical and relativistic rocket equation, overflow-safe |
| **Path-Integral (PIMC)** | Stochastic trajectory ensemble, action weights, early-warning |
| **Neural Operator** | Lightweight FNO + residual-driven alpha / freq_scale adaptation |
| **Topology (TDA-lite)** | beta0, beta1-proxy, defect score |
| **Tensor backend** | NumPy or PyTorch (CPU/CUDA), float64 |

---

## Install

```bash
# Minimal (NumPy only)
pip install -e .

# Full stack (Torch + SciPy)
pip install -e ".[full]"

# Or from requirements
pip install -r requirements-full.txt
```

---

## Quick start

```python
import numpy as np
from omni_engine import SuperEngineOmniCore8Master

engine = SuperEngineOmniCore8Master(dimension=20, n_paths=32, seed=42)
engine.initialize_state(np.linspace(1.0, 2.0, 20))

# Deterministic modes (v7.3 compatible)
r = engine.execute_evolution_cycle("omega_key")
print(r["status"], r["symplectic_determinant"])

r = engine.execute_evolution_cycle("navier_stokes", nu=1e-3, hyper_coeff=1e-4)
r = engine.execute_evolution_cycle(
    "ziolkowski",
    m_payload=5000, isp=450, delta_v=4500, structural_ratio=0.10,
    relativistic=True,
)

# Evolutionary modes (v8.x)
r = engine.execute_evolution_cycle("path_integral", n_steps=6)
r = engine.execute_evolution_cycle("adaptive")
r = engine.execute_evolution_cycle("topology")
r = engine.execute_evolution_cycle("full_v8", include_omega=True)

print(r["status"], r["current_residual"])
```

### Physics modes

| Mode | Role |
|------|------|
| `standard` | Laplace flow + symplectic projection |
| `omega_key` | Resonance tensor evaluation |
| `navier_stokes` | H² + viscous smoothing |
| `ziolkowski` | Rocket mass ratios (classical / relativistic) |
| `path_integral` | PIMC future ensemble |
| `adaptive` | Neural operator + hyperparameter adaptation |
| `topology` | Betti / defect analysis |
| `full_v8` | Topology → PIMC → Adaptive → Laplace → Symplectik |

---

## Project layout

```
omni-super-engine/
├── omni_engine/
│   ├── __init__.py
│   └── core.py          # full engine (v8.2)
├── tests/
│   └── test_engine.py
├── examples/
│   ├── basic_demo.py
│   └── singularity_damping.py
├── docs/
│   └── ARCHITECTURE.md
├── pyproject.toml
├── requirements.txt
├── requirements-full.txt
├── LICENSE
└── README.md
```

---

## Tests

```bash
pip install -e ".[dev]"
pytest -q
```

---

## Version lineage

This repository contains both archived release bundles and the active engineering lineage.

### Historical packaged bundles

| Version | Status |
|---------|--------|
| v4.6.0 | Historical production bundle |
| v6.2.0 | Historical master-unified bundle |

### Active project lineage

| Version | Focus |
|---------|--------|
| v7.0 | Initial unified architecture |
| v7.1 | Symplectic det=+1, mass guards |
| v7.2 | Relativistic Ackeret, Laplace flow |
| v7.3 | Overflow-safe relativity, Omega_key restored |
| v8.0 | Path-integral, FNO, topology, Torch backend |
| v8.1 | Hardening (dim-sync, float64, nu, guards) |
| **v8.2** | Release: configurable thresholds, optional Omega in full_v8 |

> Note: the root-level v4.6 and v6.2 artifacts are legacy archive bundles. The active code path and documentation lineage are v7.x → v8.x.

---

## License

MIT – see [LICENSE](LICENSE).

## Citation

If you use this framework in research, please cite the repository and version tag (`v8.2.0`).
