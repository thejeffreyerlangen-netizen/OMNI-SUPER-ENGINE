#!/usr/bin/env python3
import unittest
from super_engine_omni_v460 import SuperEngineOmniCleanKernelV46, evaluate_gate_status, PHYSICAL_COLLAPSE_THRESHOLD

class TestSuperEngineOmniV46(unittest.TestCase):
    def setUp(self):
        self.kernel = SuperEngineOmniCleanKernelV46()

    def test_tri_state_gate_evaluator(self):
        msg, status = evaluate_gate_status(1e-11, 1e-10)
        self.assertIn("PASSED", msg)
        self.assertEqual(status, "VERIFIED_STABLE")

        msg, status = evaluate_gate_status(0.01, 1e-10)
        self.assertIn("FAILED (Numerical Tolerance", msg)
        self.assertEqual(status, "PHYSICALLY_FEASIBLE_NO_COLLAPSE")

        msg, status = evaluate_gate_status(0.25, 1e-10)
        self.assertIn("CRITICAL WARNING (PHYSICAL COLLAPSE RISK", msg)
        self.assertEqual(status, "UNFEASIBLE_REAL_WORLD_COLLAPSE")

    def test_ns_sobolev_h2_gate_pass(self):
        res = self.kernel.execute_ns_sobolev_h2()
        self.assertIn("PASSED", res["gate_1_lege_invariant"])
        self.assertEqual(res["physical_reality_status"], "VERIFIED_STABLE")
        self.assertEqual(res["real_world_feasibility"], "SAFE FOR PRODUCTION / TOKAMAK RUN")
        self.assertLessEqual(res["final_residual"], 1.0e-07)
        self.assertEqual(res["symplektic_det_J"], 1.0)

    def test_mhd_3d_asym(self):
        res = self.kernel.execute_mhd_3d_asym()
        self.assertIn("PASSED", res["gate_1_lege_invariant"])
        self.assertEqual(res["physical_reality_status"], "VERIFIED_STABLE")
        self.assertEqual(res["real_world_feasibility"], "SAFE FOR PRODUCTION / TOKAMAK RUN")

    def test_custom_tensor(self):
        res = self.kernel.execute_custom_tensor()
        self.assertIn("PASSED", res["gate_1_lege_invariant"])
        self.assertEqual(res["physical_reality_status"], "VERIFIED_STABLE")

if __name__ == "__main__":
    unittest.main()
