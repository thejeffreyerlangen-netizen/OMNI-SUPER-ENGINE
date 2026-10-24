"""Example demonstrating the damping flow path."""

import numpy as np

from omni_engine.core import SuperEngineOmniCore7Master


engine = SuperEngineOmniCore7Master()
engine.initialize_state(np.linspace(0.0, 1.0, 32))
result = engine.execute_evolution_cycle("navier_stokes", nu=1e-3, hyper_coeff=1e-4)
print(result["status"], result["current_residual"])
