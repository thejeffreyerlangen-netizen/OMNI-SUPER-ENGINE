# Architecture

## Core stack

```
SuperEngineOmniCore8Master
├── EnvironmentCarrier          # global frequencies / metric signature
├── OmniPhysicsBridge           # symplectic, Omega_key, NS, Ziolkowski
├── PathIntegralMonitor         # PIMC ensemble
├── AdaptiveHyperController     # FNO-lite + α / freq_scale
├── HolographicTopologyAnalyzer # Betti β0 / β1-proxy / defect
└── TensorAccelerationLayer     # NumPy | Torch float64
```

## Evolution cycle

1. Mode-specific operator (physics / quantum / topology / adaptive)
2. Optional proactive correction (PIMC mean state on early warning)
3. Stable Laplacian flow (CFL-limited, `freq_scale`-modulated)
4. Symplectic projection \(\det(J)=+1\)
5. Residual + structured status dict

## Design constraints

- No silent negative rocket masses
- No `det = -1` after projection
- Relativistic mass ratio computed in log-space (no `exp` overflow)
- Submodule dimensions stay in sync via `set_dimension`
