import pytest
from src.omni_engine import SuperEngineOmniCore7Master

def test_engine_init():
    engine = SuperEngineOmniCore7Master()
    assert engine.version == "7.0.0"
