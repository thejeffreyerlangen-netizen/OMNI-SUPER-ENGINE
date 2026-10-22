"""OMNI Core 7 prototype: generator-driven symplectic evolution.

This is an exploratory numerical core, not a claim that a particular field
model from Mensah Theory has been derived. The Hamiltonian generator is an
explicit model input until a theory-specific generator is supplied.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any
import numpy as np
from numpy.typing import NDArray

Array = NDArray[np.float64]


@dataclass(frozen=True)
class StepReport:
    generator_residual: float
    symplectic_residual_before: float
    symplectic_residual_after: float
    step_matrix_condition: float
    displacement: float

    def to_dict(self) -> dict[str, float]:
        return asdict(self)


def canonical_J(n: int) -> Array:
    """Return J=[[0,I],[-I,0]] of dimension 2n."""
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    I = np.eye(n, dtype=float)
    Z = np.zeros((n, n), dtype=float)
    return np.block([[Z, I], [-I, Z]])


def _square_even(M: Array, name: str) -> Array:
    A = np.asarray(M, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1] or A.shape[0] % 2:
        raise ValueError(f"{name} must be a square even-dimensional matrix")
    if not np.all(np.isfinite(A)):
        raise ValueError(f"{name} contains non-finite values")
    return A


def symplectic_residual(S: Array, J: Array) -> float:
    S = _square_even(S, "S")
    J = _square_even(J, "J")
    if S.shape != J.shape:
        raise ValueError("S and J must have the same shape")
    denom = np.linalg.norm(J, ord="fro")
    if denom == 0:
        raise ValueError("J must be nonzero")
    return float(np.linalg.norm(S.T @ J @ S - J, ord="fro") / denom)


def hamiltonian_residual(A: Array, J: Array) -> float:
    """Relative residual for A.T J + J A = 0."""
    A = _square_even(A, "A")
    J = _square_even(J, "J")
    if A.shape != J.shape:
        raise ValueError("A and J must have the same shape")
    denom = max(np.linalg.norm(A, ord="fro") * np.linalg.norm(J, ord="fro"), 1.0)
    return float(np.linalg.norm(A.T @ J + J @ A, ord="fro") / denom)


def generator_from_symmetric_hessian(K: Array, J: Array) -> Array:
    """Construct A=J K. Symmetric K gives a Hamiltonian A for canonical J."""
    K = _square_even(K, "K")
    J = _square_even(J, "J")
    if K.shape != J.shape:
        raise ValueError("K and J must have the same shape")
    symmetry_error = np.linalg.norm(K - K.T, ord="fro")
    if symmetry_error > 1e-12 * max(np.linalg.norm(K, ord="fro"), 1.0):
        raise ValueError("K must be symmetric to construct a Hamiltonian generator")
    if not np.allclose(J.T, -J, atol=1e-12) or not np.allclose(J @ J, -np.eye(J.shape[0]), atol=1e-12):
        raise ValueError("This helper requires canonical J")
    return J @ K


def cayley_operator(A: Array, h: float, *, max_condition: float = 1e12) -> tuple[Array, float]:
    """Compute (I-hA/2)^-1 (I+hA/2), rejecting ill-conditioned solves."""
    A = _square_even(A, "A")
    if not np.isfinite(h) or h == 0:
        raise ValueError("h must be finite and nonzero")
    I = np.eye(A.shape[0])
    left = I - 0.5 * h * A
    right = I + 0.5 * h * A
    condition = float(np.linalg.cond(left))
    if not np.isfinite(condition) or condition > max_condition:
        raise np.linalg.LinAlgError(f"Cayley solve is ill-conditioned (cond={condition:.3e})")
    return np.linalg.solve(left, right), condition


def omni_geometric_step(
    S: Array, A: Array, J: Array, h: float, *, generator_tol: float = 1e-10,
    max_condition: float = 1e12,
) -> tuple[Array, StepReport]:
    """Advance a linear transformation by one generator-driven Cayley step."""
    S = _square_even(S, "S")
    A = _square_even(A, "A")
    J = _square_even(J, "J")
    if S.shape != A.shape or A.shape != J.shape:
        raise ValueError("S, A and J must have identical dimensions")
    ares = hamiltonian_residual(A, J)
    if ares > generator_tol:
        raise ValueError(f"generator is not Hamiltonian within tolerance: {ares:.3e}")
    before = symplectic_residual(S, J)
    C, cond = cayley_operator(A, h, max_condition=max_condition)
    out = C @ S
    after = symplectic_residual(out, J)
    report = StepReport(
        generator_residual=ares,
        symplectic_residual_before=before,
        symplectic_residual_after=after,
        step_matrix_condition=cond,
        displacement=float(np.linalg.norm(out - S, ord="fro")),
    )
    return out, report


def legacy_elementwise_update(M: Array, alpha: float = 0.1, beta: float = 0.001) -> Array:
    """Reproduce the v6.3-style elementwise update for comparison only."""
    M = _square_even(M, "M")
    if not np.isfinite(alpha) or not np.isfinite(beta):
        raise ValueError("alpha and beta must be finite")
    D = M - np.eye(M.shape[0])
    return M - alpha * D - beta * np.sin(D)  # NumPy sine is elementwise.


def demo(seed: int = 2026, n_half: int = 3, h: float = 0.05, steps: int = 20) -> dict[str, Any]:
    """Run a reproducible structural comparison; not a physics benchmark."""
    rng = np.random.default_rng(seed)
    J = canonical_J(n_half)
    raw = rng.normal(size=J.shape)
    K = 0.5 * (raw + raw.T)
    A = generator_from_symmetric_hessian(K, J)
    # Start from the same non-identity symplectic state for both updates.
    S0, _ = cayley_operator(A, 0.1)
    S_cayley = S0.copy()
    S_legacy = S0.copy()
    trajectory = []
    for k in range(steps):
        S_cayley, report = omni_geometric_step(S_cayley, A, J, h)
        S_legacy = legacy_elementwise_update(S_legacy)
        trajectory.append({
            "step": k + 1,
            "cayley_symplectic_residual": symplectic_residual(S_cayley, J),
            "legacy_symplectic_residual": symplectic_residual(S_legacy, J),
            "cayley_displacement_this_step": report.displacement,
        })
    return {
        "seed": seed, "dimension": int(J.shape[0]), "h": h, "steps": steps,
        "generator_residual": hamiltonian_residual(A, J),
        "cayley_final_symplectic_residual": symplectic_residual(S_cayley, J),
        "legacy_final_symplectic_residual": symplectic_residual(S_legacy, J),
        "trajectory": trajectory,
        "interpretation": (
            "Structural comparison only: the two updates encode different dynamics. "
            "This does not establish which one represents the intended Mensah/OMNI field model."
        ),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(demo(), indent=2))
