"""Core tests for OMNI SUPER ENGINE v8.2"""

import numpy as np
import pytest

from omni_engine import (
    SuperEngineOmniCore8Master,
    OmniPhysicsBridge,
    PathIntegralMonitor,
    HolographicTopologyAnalyzer,
)


@pytest.fixture
def engine():
    eng = SuperEngineOmniCore8Master(dimension=20, n_paths=8, seed=0)
    eng.initialize_state(np.linspace(1.0, 2.0, 20))
    return eng


@pytest.fixture
def bridge():
    return OmniPhysicsBridge(98.112)


class TestSymplectic:
    def test_identity(self, bridge):
        J = np.eye(4)
        d = np.linalg.det(bridge.enforce_symplectic_invariant(J))
        assert abs(d - 1.0) < 1e-10

    def test_negative_orientation(self, bridge):
        J = np.diag([1.0, 1.0, -1.0, 1.0])
        d = np.linalg.det(bridge.enforce_symplectic_invariant(J))
        assert abs(d - 1.0) < 1e-10

    def test_random_batch(self, bridge):
        rng = np.random.default_rng(1)
        for _ in range(20):
            n = int(rng.integers(2, 12))
            J = rng.normal(size=(n, n))
            d = np.linalg.det(bridge.enforce_symplectic_invariant(J))
            assert abs(d - 1.0) < 1e-6


class TestZiolkowski:
    def test_leo_locked(self, bridge):
        z = bridge.translate_ziolkowski(5000, 450, 4500, 0.10)
        assert z["status"].startswith("LOCKED")
        assert z["total_start_mass_m0"] > 0

    def test_invalid_payload(self, bridge):
        z = bridge.translate_ziolkowski(-1, 450, 1000, 0.1)
        assert z["status"] == "INVALID_INPUT"

    def test_v_equals_c(self, bridge):
        z = bridge.translate_ziolkowski(1000, 4000, bridge.C_LIGHT, 0.02)
        assert z["status"] == "UNPHYSICAL_TRAJECTORY"

    def test_classical_vs_rel_low_dv(self, bridge):
        z_r = bridge.translate_ziolkowski(5000, 450, 4500, 0.1, relativistic=True)
        z_c = bridge.translate_ziolkowski(5000, 450, 4500, 0.1, relativistic=False)
        assert abs(z_r["total_start_mass_m0"] - z_c["total_start_mass_m0"]) < 1e-4


class TestOmegaAndNS:
    def test_omega_key(self, engine):
        r = engine.execute_evolution_cycle("omega_key")
        assert r["status"] == "VERIFIED_STABLE_OMEGA_KEY"
        assert abs(r["symplectic_determinant"] - 1.0) < 1e-8
        assert r["bridge_data"]["h2_sobolev_stability_verified"] is True

    def test_navier_stokes_nu(self, bridge):
        v = np.random.default_rng(0).normal(size=64)
        a = bridge.translate_navier_stokes(v, nu=0.0, hyper_coeff=1e-4)
        b = bridge.translate_navier_stokes(v, nu=1.0, hyper_coeff=1e-4)
        assert not np.allclose(a, b)


class TestV8Layers:
    def test_path_integral(self, engine):
        r = engine.execute_evolution_cycle("path_integral", n_steps=4)
        assert r["path_integral"] is not None
        assert np.isfinite(r["path_integral"]["mean_action"])
        assert r["path_integral"]["weighted_mean_state"].shape == (20,)

    def test_adaptive(self, engine):
        r = engine.execute_evolution_cycle("adaptive")
        assert r["adaptive"] is not None
        assert 0 < r["adaptive"]["alpha"] <= 0.24
        assert 0.5 <= r["adaptive"]["freq_scale"] <= 2.0

    def test_topology(self, engine):
        r = engine.execute_evolution_cycle("topology")
        assert r["topology"] is not None
        assert r["topology"]["betti"]["beta0"] >= 0

    def test_full_v8(self, engine):
        r = engine.execute_evolution_cycle("full_v8", include_omega=True)
        assert r["bridge_data"] is not None
        assert abs(r["symplectic_determinant"] - 1.0) < 1e-8

    def test_unknown_mode(self, engine):
        r = engine.execute_evolution_cycle("not_a_real_mode")
        assert r["status"] == "UNKNOWN_MODE_FALLBACK_STANDARD"


class TestGuards:
    def test_wrong_dimension(self, engine):
        with pytest.raises(ValueError):
            engine.initialize_state(np.ones(7))

    def test_set_dimension_sync(self):
        eng = SuperEngineOmniCore8Master(dimension=20, n_paths=4, seed=1)
        eng.set_dimension(12)
        assert eng.path_integral.dimension == 12
        assert eng.adaptive.dimension == 12
        assert eng.accel.dimension == 12
        eng.initialize_state(np.ones(12))
        r = eng.execute_evolution_cycle("standard")
        assert abs(r["symplectic_determinant"] - 1.0) < 1e-8

    def test_singularity_finite(self, engine):
        pol = np.linspace(1, 2, 20)
        pol[10] = 1e8
        engine.initialize_state(pol)
        for _ in range(5):
            engine.execute_evolution_cycle("full_v8")
        assert np.all(np.isfinite(engine.state_psi))
