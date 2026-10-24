"""Basic demo for the OMNI SUPER ENGINE package."""

import numpy as np

from omni_engine.core import SuperEngineOmniCore7Master


engine = SuperEngineOmniCore7Master()
engine.initialize_state(np.linspace(1.0, 2.0, 20))
result = engine.execute_evolution_cycle("ziolkowski")
print(result["status"], result["current_residual"])
