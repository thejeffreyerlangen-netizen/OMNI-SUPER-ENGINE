import json
from pathlib import Path


def test_core7_audit_file_exists():
    p = Path("certs/core7_openai_audit_proof.json")
    assert p.exists(), "Core 7 audit file is missing"

    data = json.loads(p.read_text(encoding="utf-8"))
    assert data["engine"] == "Super-Engine-Omni-v7.0-Core7"
    assert data["axiomatics"]["N"] == 20
    assert data["benchmark"]["name"] == "openai/math"


def test_core7_master_engine_runtime():
    import core7_master_engine

    result = core7_master_engine.run_core7_audit()
    assert result["status"] == "SCaffold_Validation_Ready"
    assert result["stress_validation"]["cycles_total"] == 3000
