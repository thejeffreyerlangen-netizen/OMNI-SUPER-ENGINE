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
- Unused `nu` in Navier–Stokes → \(k^2\) term
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

## [7.1.0] – 2026-10-24
Symplectic \(\det=+1\), Ziolkowski mass guards.

## [7.0.0] – 2026-10-24
Initial unified master architecture.
