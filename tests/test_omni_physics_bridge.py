import numpy as np

from omni_engine.core import OmniPhysicsBridge


def test_symplectic_invariant_enforced():
    bridge = OmniPhysicsBridge()
    J = np.array([[2.0, 0.0], [0.0, 0.5]])
    enforced = bridge.enforce_symplectic_invariant(J)
    assert np.isclose(np.linalg.det(enforced), 1.0)


def test_ziolkowski_translation_basic():
    bridge = OmniPhysicsBridge()
    result = bridge.translate_ziolkowski(5000, 450, 4500, 0.10)
    assert result["status"] == "LOCKED_LOSSLESS_TRAJECTORY"
    assert result["mass_ratio"] > 1.0
