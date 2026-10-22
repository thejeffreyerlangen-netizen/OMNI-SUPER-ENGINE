import numpy as np
import pytest
from omni_super_engine_master_v7 import OmniPhysicsBridge, SuperEngineOmniCore7Master

def test_symplectic_invariant_enforcement():
    bridge = OmniPhysicsBridge(base_frequency=98.112)
    j_matrix = np.eye(4) * 1.5
    enforced = bridge.enforce_symplectic_invariant(j_matrix)
    det_val = np.linalg.det(enforced)
    assert np.abs(det_val - 1.0) < 1e-10

def test_ziolkowski_stage_calculation():
    bridge = OmniPhysicsBridge(base_frequency=98.112)
    result = bridge.translate_ziolkowski(
        m_payload=5000, isp=450, delta_v=4500, structural_ratio=0.10
    )
    assert result["mass_ratio"] > 2.5
    assert result["total_start_mass_m0"] > 17000.0

def test_navier_stokes_hyperviscous_smoothing():
    bridge = OmniPhysicsBridge(base_frequency=98.112)
    dummy_field = np.sin(np.linspace(0, 2 * np.pi, 50))
    smoothed = bridge.translate_navier_stokes(dummy_field, nu=1e-3, hyper_coeff=1e-4)
    assert smoothed.shape == dummy_field.shape
    assert not np.any(np.isnan(smoothed))

def test_master_engine_evolution_cycle():
    engine = SuperEngineOmniCore7Master()
    engine.initialize_state(np.linspace(1.0, 2.0, 20))
    res_ziolkowski = engine.execute_evolution_cycle(
        physics_mode="ziolkowski",
        m_payload=5000,
        isp=450,
        delta_v=4500,
        structural_ratio=0.10,
    )
    assert res_ziolkowski["status"] == "VERIFIED_STABLE"

    res_fluid = engine.execute_evolution_cycle(
        physics_mode="navier_stokes",
        nu=1e-3,
        hyper_coeff=1e-4,
    )
    assert res_fluid["status"] == "VERIFIED_STABLE"
