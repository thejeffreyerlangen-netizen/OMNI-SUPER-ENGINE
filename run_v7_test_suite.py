import subprocess
import sys

if __name__ == "__main__":
    result = subprocess.run([sys.executable, "-m", "pytest", "-q"], check=False)
    raise SystemExit(result.returncode)
