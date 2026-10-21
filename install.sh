set -e
echo 'SUPER ENGINE OMNI v4.0.0 ONE-CLICK INSTALLER'
python3 -m pip install --quiet numpy scipy
chmod +x run_kernel_benchmark.sh test_super_engine_omni_v40_clean.py
echo 'Setup complete! Running benchmark...'
bash run_kernel_benchmark.sh run_all 'GitHub-Auditor'
