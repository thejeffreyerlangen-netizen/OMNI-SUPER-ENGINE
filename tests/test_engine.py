import numpy as np

from omni_engine.core import SuperEngineOmniCore7Master


def test_engine_cycle_ziolkowski():
    engine = SuperEngineOmniCore7Master()
    engine.initialize_state(np.linspace(1.0, 2.0, 20))
    result = engine.execute_evolution_cycle("ziolkowski")
    assert result["status"] == "VERIFIED_STABLE"
    assert result["symplectic_determinant"] > 0.0
    assert "mass_ratio" in result["bridge_data"]


def test_engine_cycle_navier_stokes():
    engine = SuperEngineOmniCore7Master()
    engine.initialize_state(np.linspace(0.0, 1.0, 16))
    result = engine.execute_evolution_cycle("navier_stokes")
    assert result["status"] == "VERIFIED_STABLE"
    assert result["current_residual"] >= 0.0
