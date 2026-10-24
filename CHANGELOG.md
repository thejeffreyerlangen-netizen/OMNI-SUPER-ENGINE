# Changelog

## [8.2.0] – 2026-10-24

### Added
- Configurable topology thresholds (`defect_warn`, `beta0_frac_warn`)
- Configurable path-integral `instability_factor`
- Optional `include_omega=True` in `full_v8` pipeline

### Fixed (from v8.0 analysis)
- Dimension desync across submodules → `set_dimension()`
- Neural operator dtype float32 → float64
- Dead `freq_scale` → adaptive and applied to Laplace
- Unused `nu` in Navier–Stokes → k² term
- Removed unused `find_peaks` import
- Unknown `physics_mode` → explicit status
- RNG seed configurable
- State mixing L2-norm preserving

## [8.1.0] – 2026-10-24
Hardening release (see above fixes).

## [8.0.0] – 2026-10-24
Quantum-topological extension: PIMC, FNO, TDA-lite, Torch backend.

## [7.3.0] – 2026-10-24
Overflow-safe relativity, Omega_key restored, stable Laplace, residual API.

## [7.2.0] – 2026-10-24
Relativistic Ackeret + Laplace-flow stabilization.

## [7.1.0] – 2026-10-24
Symplectic det=+1, Ziolkowski mass guards.

## [7.0.0] – 2026-10-24
Initial unified master architecture.

## [6.2.0] – 2026-10-24
Historical master-unified bundle release retained as a legacy packaged archive.

## [4.6.0] – 2026-10-24
Historical production baseline bundle retained as a legacy packaged archive.

> Historical note: v4.6.0 and v6.2.0 are archived package bundles and are not part of the active engineering runtime path. The active lineage documented by the project is v7.0 → v8.2.
