"""Release smoke test for the active package."""

from omni_engine.core import SuperEngineOmniCore7Master


def test_release_package_import():
    engine = SuperEngineOmniCore7Master()
    assert engine.base_frequency > 0
