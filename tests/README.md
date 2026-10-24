# Test organization

This repository keeps the active automated suite under `tests/`.

- `tests/` : active pytest suite for the current package (`test_engine.py`, `test_omni_physics_bridge.py`, `test_release.py`)
- `tests/legacy/` : historical validation, integrity, and exploratory test scripts that were uploaded separately

This separation keeps the valid current suite discoverable by `pytest` while preserving archived validation artifacts for reference.
