"""Compatibility shim for the legacy omni_engine import path.

This project exposes the main implementation in ``super_engine_omni_v460.py``.
Older code and tests import it as ``omni_engine``; this module re-exports the
public API under that name so callers do not need to change imports.
"""

from super_engine_omni_v460 import (
    PHYSICAL_COLLAPSE_THRESHOLD,
    SuperEngineOmniCleanKernelV45,
    SuperEngineOmniCleanKernelV46,
    evaluate_gate_status,
)

__all__ = [
    "PHYSICAL_COLLAPSE_THRESHOLD",
    "SuperEngineOmniCleanKernelV45",
    "SuperEngineOmniCleanKernelV46",
    "evaluate_gate_status",
]
