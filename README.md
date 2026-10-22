# Super Engine Omni (v4.6.0)

Canonical hardened release of the Super Engine Omni kernel with the Physically Validated Gate Evaluator, UAFF forensic integrity checks, and DAIECS invariant monitoring.

## Overview

This repository includes:
- the primary runtime implementation: `super_engine_omni_v460.py`
- the public compatibility wrapper: `omni_engine.py`
- the canonical validation suite: `test_super_engine_omni_v460_clean.py`
- the rigorous scientific validation workflow: `rigorous_master_test_suite_v460.py`
- the mutation stress test: `mutation_stresstest_hardened.py`
- the benchmark runner: `run_kernel_benchmark.sh`

## Repository

- GitHub: https://github.com/thejeffreyerlangen-netizen/OMNI-SUPER-ENGINE

## Requirements

- Python 3.10+
- numpy
- pytest

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Quick start

Run the core kernel:

```bash
python3 super_engine_omni_v460.py
```

Run the canonical test suite:

```bash
python3 -m pytest -q
```

Run the rigorous validation suite:

```bash
python3 rigorous_master_test_suite_v460.py
```

Run the benchmark script:

```bash
bash run_kernel_benchmark.sh
```

Run the hardened mutation stress test:

```bash
python3 mutation_stresstest_hardened.py --count 100000 --source super_engine_omni_v460.py
```

## Validation datasheet

See `TEST_INFO_DATASHEET.md` for a compact description of the validation assets and execution order.

## Installation helper

The repo includes an installation script:

```bash
bash install.sh
```

## Licensing and provenance

This project is distributed as a research and engineering kernel under the repository's current project documentation and provenance notes. The code includes built-in integrity and audit checks for safety monitoring and forensic verification.
