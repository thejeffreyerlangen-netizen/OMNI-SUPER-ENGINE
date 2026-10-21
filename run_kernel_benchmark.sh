#!/usr/bin/env bash
# ==============================================================================
#  SUPER ENGINE OMNI (M-DSL IR KERNEL v4.6.0) — AUTOMATED LAUNCHER
# ==============================================================================
#  Runs the full M-DSL IR Kernel benchmark suite across all operator tokens.
# ============================================================================== 

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_EXEC="python3"

echo "================================================================================"
echo "  LAUNCHING SUPER ENGINE OMNI M-DSL IR BENCHMARK SUITE (v4.6.0)"
echo "================================================================================"

if ! command -v $PYTHON_EXEC &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH."
    exit 1
fi

$PYTHON_EXEC "$SCRIPT_DIR/test_super_engine_omni_v460_clean.py" "$@"

echo "================================================================================"
echo "✓ Execution complete. Check generated JSON proof certificates."
echo "================================================================================"
