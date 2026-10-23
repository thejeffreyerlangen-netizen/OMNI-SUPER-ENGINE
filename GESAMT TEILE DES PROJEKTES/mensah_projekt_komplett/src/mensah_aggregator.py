# Mensah-Abhandlungs-Automator v3
import hashlib
from pathlib import Path
from typing import Iterable, tuple

def sha256_of(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

print("Mensah Aggregator Core Loaded.")
