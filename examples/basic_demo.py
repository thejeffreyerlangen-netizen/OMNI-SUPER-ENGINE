#!/usr/bin/env python3
"""Minimal demo of all physics modes."""

import numpy as np
from omni_engine import SuperEngineOmniCore8Master

def main():
    engine = SuperEngineOmniCore8Master(dimension=20, n_paths=24, seed=42)
    engine.initialize_state(np.linspace(1.0, 2.0, 20))

    for mode in ("omega_key", "standard", "navier_stokes", "path_integral",
                 "adaptive", "topology", "full_v8"):
        r = engine.execute_evolution_cycle(mode)
        print(f"{mode:16s}  status={r['status']:40s}  res={r['current_residual']}")

    z = engine.bridge.translate_ziolkowski(5000, 450, 4500, 0.10)
    print(f"\nZiolkowski LEO: {z['status']}, m0={z['total_start_mass_m0']:.1f} kg")

if __name__ == "__main__":
    main()
