# Contributing

1. Fork and create a feature branch.
2. Keep the deterministic core (symplectic, Ziolkowski guards, overflow-safe relativity) intact unless the change is intentional and tested.
3. Add or update tests under `tests/`.
4. Run `pytest -q` before opening a PR.
5. Document new `physics_mode` values in the README table.
