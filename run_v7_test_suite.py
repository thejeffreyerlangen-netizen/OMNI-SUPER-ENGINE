#!/usr/bin/env python3
"""
Test Runner for OMNI SUPER ENGINE v7.0 (CORE 7) - UNIT TEST SUITE
"""

import sys
import os
import numpy as np

# Mock pytest.approx if pytest is not installed
class Approx:
    def __init__(self, expected, rel=1e-6, abs_val=None):
        self.expected = expected
        self.rel = rel
        self.abs_val = abs_val

    def __eq__(self, actual):
        if self.abs_val is not None:
            return abs(actual - self.expected) <= self.abs_val
        return abs(actual - self.expected) <= self.rel * abs(self.expected)

    def __repr__(self):
        return f"approx({self.expected} ± {self.rel})"

class PytestMock:
    @staticmethod
    def approx(expected, rel=1e-6, abs=None):
        return Approx(expected, rel=rel, abs_val=abs)

sys.modules['pytest'] = PytestMock

# Import the test suite
sys.path.insert(0, '/workspace/scratch')
from tests.test_omni_physics_bridge import (
    test_symplectic_invariant_enforcement,
    test_ziolkowski_stage_calculation,
    test_navier_stokes_hyperviscous_smoothing,
    test_master_engine_evolution_cycle
)

def run_suite():
    print("=" * 80)
    print("  OMNI SUPER ENGINE v7.0 (CORE 7) - UNIT TEST SUITE (tests/test_omni_physics_bridge.py)")
    print("=" * 80)
    
    tests = [
        ("test_symplectic_invariant_enforcement", test_symplectic_invariant_enforcement),
        ("test_ziolkowski_stage_calculation", test_ziolkowski_stage_calculation),
        ("test_navier_stokes_hyperviscous_smoothing", test_navier_stokes_hyperviscous_smoothing),
        ("test_master_engine_evolution_cycle", test_master_engine_evolution_cycle),
    ]
    
    passed = 0
    failed = 0
    
    for name, test_func in tests:
        try:
            test_func()
            print(f" [✓] {name:<45} : PASSED")
            passed += 1
        except Exception as e:
            print(f" [✗] {name:<45} : FAILED ({e})")
            failed += 1
            
    print("=" * 80)
    print(f" TEST SUITE SUMMARY: {passed}/{len(tests)} PASSED | {failed} FAILED")
    print("=" * 80)
    return failed == 0

if __name__ == "__main__":
    success = run_suite()
    sys.exit(0 if success else 1)
