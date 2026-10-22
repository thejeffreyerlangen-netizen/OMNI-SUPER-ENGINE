# ============================================================================
# OMNI SUPER ENGINE v7.0 (CORE 7) - UNIT TEST SUITE (tests/test_omni_physics_bridge.py)
# Automatisierte Validierung der physikalischen Brücke und des Master-Kerns
# ============================================================================

import os
import sys

import numpy as np
import pytest

# Füge das Hauptverzeichnis zum Pfad hinzu, um die Engine-Module zu importieren
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from omni_super_engine_master_v7 import OmniPhysicsBridge, SuperEngineOmniCore7Master


def test_symplectic_invariant_enforcement():
    """Prüft, ob die symplektische Volumeninvarianz det(J) == 1.0 exakt erzwungen wird."""
    bridge = OmniPhysicsBridge(base_frequency=98.112)
    # Erzeuge eine Matrix mit von 1.0 abweichender Determinante
    j_matrix = np.eye(4) * 1.5
    enforced = bridge.enforce_symplectic_invariant(j_matrix)
    det_val = np.linalg.det(enforced)

    assert np.abs(det_val - 1.0) < 1e-10, f"Symplektische Determinante weicht ab: {det_val}"


def test_ziolkowski_stage_calculation():
    """Validiert die Ziolkowski-Berechnung der Hydrolox-Oberstufe (5t Nutzlast, 4500 m/s Delta-V)."""
    bridge = OmniPhysicsBridge(base_frequency=98.112)
    result = bridge.translate_ziolkowski(m_payload=5000, isp=450, delta_v=4500, structural_ratio=0.10)

    assert result["mass_ratio"] > 2.5
    assert result["total_start_mass_m0"] > 17000.0
    assert result["propellant_mass_mp"] > 11000.0
    assert result["structural_mass_ms"] > 1200.0
    assert result["status"] == "LOCKED_LOSSLESS_TRAJECTORY"


def test_navier_stokes_hyperviscous_smoothing():
    """Überprüft die biharmonische H2-Sobolev-Glättung des Geschwindigkeitsfeldes."""
    bridge = OmniPhysicsBridge(base_frequency=98.112)
    dummy_field = np.sin(np.linspace(0, 2 * np.pi, 50))
    smoothed = bridge.translate_navier_stokes(dummy_field, nu=1e-3, hyper_coeff=1e-4)

    assert smoothed.shape == dummy_field.shape
    assert not np.any(np.isnan(smoothed)), "Glättung erzeugt NaN-Werte."


def test_master_engine_evolution_cycle():
    """Testet einen vollständigen Evolutions-Zyklus der Super Engine Omni Core 7."""
    engine = SuperEngineOmniCore7Master()
    initial_state = np.linspace(1.0, 2.0, 20)
    engine.initialize_state(initial_state)

    # Test mit Ziolkowski-Brücke
    res_rocket = engine.execute_evolution_cycle(
        physics_mode="ziolkowski",
        m_payload=5000,
        isp=450,
        delta_v=4500,
        structural_ratio=0.10,
    )

    assert res_rocket["cycle_frequency_hz"] == 98.112
    assert res_rocket["symplectic_determinant"] == pytest.approx(1.0, rel=1e-7)
    assert res_rocket["bridge_data"] is not None

    # Test mit Navier-Stokes-Modus
    res_fluid = engine.execute_evolution_cycle(physics_mode="navier_stokes", nu=1e-3, hyper_coeff=1e-3)
    assert res_fluid["current_residual"] >= 0.0
    assert res_fluid["status"] in ["VERIFIED_STABLE", "TRIGGER_PRFE_FORENSIC_CORRECTION"]
