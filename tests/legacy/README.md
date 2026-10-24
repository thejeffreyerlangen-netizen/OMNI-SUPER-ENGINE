# Legacy validation catalog

This directory stores historical test artifacts that were uploaded outside the active suite.

The files are grouped by intent so the main test suite stays discoverable and reproducible.

## integrity
- `integrity/test_super_engine_omni_v460_clean.py`

## validation
- `validation/rigorous_master_test_suite_v460.py`

## exploratory
- `exploratory/mutation_stresstest_hardened.py`

The active Pytest suite remains under `tests/` and is the default target for CI and local validation.
