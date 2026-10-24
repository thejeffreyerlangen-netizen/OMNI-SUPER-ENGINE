#!/usr/bin/env python3
"""Inject a pole and damp it with full_v8."""

import numpy as np
from omni_engine import SuperEngineOmniCore8Master

def main():
    engine = SuperEngineOmniCore8Master(dimension=20, n_paths=16, seed=1)
    state = np.linspace(1.0, 2.0, 20)
    state[10] = 1e6
    engine.initialize_state(state)

    print(f"{'cycle':>6}  {'pole':>12}  {'residual':>12}")
    print(f"{0:6d}  {engine.state_psi[10]:12.4e}  {engine.compute_residual():12.4e}")
    for i in range(1, 11):
        r = engine.execute_evolution_cycle("full_v8")
        print(f"{i:6d}  {engine.state_psi[10]:12.4e}  {r['current_residual']:12.4e}")

if __name__ == "__main__":
    main()
