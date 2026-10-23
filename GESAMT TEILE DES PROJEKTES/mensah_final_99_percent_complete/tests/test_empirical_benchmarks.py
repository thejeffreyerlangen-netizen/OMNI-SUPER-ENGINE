import pytest
import pandas as pd
import numpy as np

def test_eq1_quantum_string():
    df = pd.read_csv("eq1_quantum_string.csv")
    assert "q1" in df.columns
    assert np.all(np.isfinite(df["q1"]))

def test_eq2_hypersonic_shockwave():
    df = pd.read_csv("eq2_hypersonic_shockwave.csv")
    assert "T_mach" in df.columns
    assert df["T_mach"].max() <= 25.0

def test_eq3_kuramoto_oscillator():
    df = pd.read_csv("eq3_kuramoto_oscillator.csv")
    assert df["coherence_r"].median() > 0.90

def test_eq4_submarine_hydrodynamics():
    df = pd.read_csv("eq4_submarine_hydrodynamics.csv")
    assert abs(df["WSS"].mean() - 24.50) < 0.1

def test_eq5_tokamak_reactor():
    df = pd.read_csv("eq5_tokamak_reactor.csv")
    assert abs(df["mag_pressure"].mean() - 4.00) < 0.05
