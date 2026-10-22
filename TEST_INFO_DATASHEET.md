# Super Engine Omni v4.6.0 — Test Information Datasheet

## Overview
This document describes the validation and test structure for the Super Engine Omni v4.6.0 repository. It is intended as a compact engineering reference for the verification flow, the purpose of each test script, and the local execution commands.

Repository:
- https://github.com/thejeffreyerlangen-netizen/OMNI-SUPER-ENGINE

## Included validation assets

### 1) Core kernel
- File: `super_engine_omni_v460.py`
- Purpose:
  - Primary runtime implementation of the Super Engine Omni v4.6.0 kernel.
  - Includes the ultimate master-kernel flow, integrity verification, forensic audit chain, and MHD safety evaluation.
  - Provides reversed compatibility adapters for the canonical 4.6.0 test interface.

### 2) Canonical unit validation
- File: `test_super_engine_omni_v460_clean.py`
- Purpose:
  - Validates the public interface contract for the v4.6.0 kernel.
  - Checks the 3-state gate evaluator behavior.
  - Verifies the Sobolev H² gate pass behavior.
  - Validates MHD execution path and custom tensor execution path.

### 3) Rigorous master validation suite
- File: `rigorous_master_test_suite_v460.py`
- Purpose:
  - Provides an additional scientific-style validation layer.
  - Exercises PDE convergence assumptions.
  - Tests resonance / curvature invariants.
  - Verifies hash-based integrity detection for UAFF-style tamper checks.
  - Intended for deeper validation beyond the basic unit suite.

## Test objectives

The test set is designed to verify the following project traits:

- Mathematical stability across representative PDE conditions.
- Correct three-state gate evaluation:
  - VERIFIED_STABLE
  - PHYSICALLY_FEASIBLE_NO_COLLAPSE
  - UNFEASIBLE_REAL_WORLD_COLLAPSE
- Integrity and tamper detection behavior.
- Resonance / scoring invariants and symbolic stability indicators.
- Compatibility between the advanced kernel implementation and the canonical test API.

## Execution commands

From the repository root:

```bash
python super_engine_omni_v460.py
```

Runs the main kernel and prints a summary of the MHD test execution, gate outcome, and audit-chain count.

```bash
python -m pytest test_super_engine_omni_v460_clean.py -q
```

Runs the canonical validation tests for the public v4.6.0 interface.

```bash
python rigorous_master_test_suite_v460.py
```

Runs the scientific validation suite with structured pass/fail reporting.

## Expected output behavior

The scripts are designed to produce structured console output that provides:

- pass/fail status by test case
- gate classification messages
- residual and stability references
- integrity checks and tamper detection outcomes
- audit-chain / forensic event summaries where applicable

## Interpretation guidelines

- A pass in the canonical unit tests indicates the public API contract remains consistent with the expected stable behavior.
- A pass in the rigorous suite indicates the underlying assumptions for PDE convergence and integrity checks remain aligned with the validation goals.
- A failure indicates a mismatch between the expected mathematical gate logic and the current runtime behavior. These failures should be reviewed in the relevant kernel function and the corresponding test objective.

## Recommended validation order

For a standard verification flow:

1. Run the core kernel script.
2. Run the canonical unit tests.
3. Run the rigorous master validation suite.

This layered order helps separate:
- runtime health
- API compatibility
- deeper scientific validation

## Status note
This file is intended as a technical validation datasheet for local use and repository maintenance. Actual pass/fail results depend on the environment, Python version, and installed dependencies, especially `numpy` and `pytest`.
