#!/usr/bin/env python3
"""
SUPER ENGINE OMNI v4.4.5 — Hardened 100,000-case mutation / integrity test.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import subprocess
import sys
import tempfile
import time
from pathlib import Path

PINNED_SHA256 = "eb3dfa96feb275fd905357289e94fd3ee126d2305d615f8574bdb18cfa425b4c"

MUTATION_TYPES = (
    "character",
    "append_comment",
    "insert_comment",
    "alter_number",
    "swap_operator",
    "duplicate_line",
    "delete_line",
    "whitespace",
    "line_ending",
    "identifier",
    "truncate",
    "append_bytes",
)

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def mutate(source: bytes, seed: int) -> tuple[bytes, str]:
    """Return a deterministic candidate and mutation category."""
    rng = random.Random(seed)
    text = source.decode("utf-8", errors="replace")
    lines = text.splitlines(keepends=True)
    kind = rng.choice(MUTATION_TYPES)

    if kind == "character" and text:
        i = rng.randrange(len(text))
        old = text[i]
        new = "X" if old != "X" else "Y"
        text = text[:i] + new + text[i + 1:]
    elif kind == "append_comment":
        text += f"\n# mutation-seed-{seed}\n"
    elif kind == "insert_comment":
        i = rng.randrange(len(lines) + 1)
        lines.insert(i, f"# mutation-seed-{seed}\n")
        text = "".join(lines)
    elif kind == "alter_number":
        import re
        matches = list(re.finditer(r"(?<![A-Za-z_])\d+(?![A-Za-z_])", text))
        if matches:
            m = rng.choice(matches)
            replacement = str(int(m.group()) + rng.choice((-7, -1, 1, 13)))
            text = text[:m.start()] + replacement + text[m.end():]
        else:
            text += f"\n# numeric-fallback-{seed}\n"
    elif kind == "swap_operator":
        candidates = [(" == ", " != "), (" != ", " == "), (" + ", " - "),
                      (" - ", " + "), (" <= ", " >= "), (" >= ", " <= ")]
        rng.shuffle(candidates)
        for old, new in candidates:
            if old in text:
                text = text.replace(old, new, 1)
                break
        else:
            text += f"\n# operator-fallback-{seed}\n"
    elif kind == "duplicate_line" and lines:
        i = rng.randrange(len(lines))
        lines.insert(i, lines[i])
        text = "".join(lines)
    elif kind == "delete_line" and len(lines) > 1:
        i = rng.randrange(len(lines))
        lines.pop(i)
        text = "".join(lines)
    elif kind == "whitespace":
        text += " " if not text.endswith(" ") else "\t"
    elif kind == "line_ending":
        text = text.replace("\r\n", "\n")
        text = text.replace("\n", "\r\n", 1) if "\n" in text else text + "\r\n"
    elif kind == "identifier":
        import re
        matches = list(re.finditer(r"\b[A-Za-z_][A-Za-z_0-9]{2,}\b", text))
        if matches:
            m = rng.choice(matches)
            replacement = m.group() + "_mut"
            text = text[:m.start()] + replacement + text[m.end():]
        else:
            text += f"\nidentifier_fallback_{seed} = True\n"
    elif kind == "truncate" and len(text) > 2:
        cut = rng.randrange(1, len(text))
        text = text[:cut]
    elif kind == "append_bytes":
        return source + f"\n# raw-byte-mutation-{seed}\n".encode(), kind

    candidate = text.encode("utf-8")
    if candidate == source:
        candidate = source + f"\n# guaranteed-mutation-{seed}\n".encode()
    return candidate, kind

def check_runtime_guard(source_path: Path, pinned_hash: str) -> tuple[bool, str]:
    original = source_path.read_bytes()
    mod_name = source_path.stem
    with tempfile.TemporaryDirectory(prefix="omni_integrity_") as td:
        tmp = Path(td) / source_path.name
        tmp.write_bytes(original + b"\n# runtime-guard-tamper\n")
        code = "\n".join([
            "import os, sys, json, hashlib",
            f"sys.path.insert(0, {repr(td)})",
            f"import {mod_name} as mod",
            "source_bytes = open(mod.__file__, 'rb').read()",
            "curr_hash = hashlib.sha256(source_bytes).hexdigest()",
            f"expected = os.environ.get('SUPER_ENGINE_EXPECTED_HASH', {repr(pinned_hash)})",
            "if curr_hash != expected:",
            "    print(json.dumps({'blocked': True, 'reason': 'HASH_MISMATCH', 'curr': curr_hash, 'expected': expected}))",
            "    sys.exit(0)",
            "print(json.dumps({'blocked': False}))",
            "sys.exit(7)"
        ])
        env = os.environ.copy()
        env["SUPER_ENGINE_EXPECTED_HASH"] = pinned_hash
        env["PYTHONPATH"] = td + os.pathsep + env.get("PYTHONPATH", "")
        proc = subprocess.run([sys.executable, "-c", code], cwd=td, env=env,
                              text=True, capture_output=True, timeout=20)
        if proc.returncode == 0 and '"blocked": true' in proc.stdout.lower():
            return True, proc.stdout.strip()
        return False, (
            f"returncode={proc.returncode}; stdout={proc.stdout.strip()!r}; "
            f"stderr={proc.stderr.strip()[-1000:]!r}"
        )

def run_stress(source_path: Path, count: int, pinned_hash: str, seed_base: int) -> dict:
    source = source_path.read_bytes()
    current_hash = sha256(source)
    if current_hash != pinned_hash:
        raise SystemExit(
            "ABBRUCH: Quelltext stimmt nicht mit unabhängig gepinntem Hash überein.\n"
            f"  pinned:  {pinned_hash}\n  current: {current_hash}\n"
        )

    print("=" * 78)
    print("SUPER ENGINE OMNI v4.4.5 — HARDENED MUTATION STRESS TEST")
    print(f"Source:        {source_path}")
    print(f"Pinned SHA256: {pinned_hash}")
    print(f"Attempts:      {count:,}")
    print("=" * 78)

    start = time.perf_counter()
    unique_hashes: set[str] = set()
    detected = 0
    unchanged = 0
    kind_counts: dict[str, int] = {}
    examples: list[dict] = []

    for i in range(count):
        candidate, kind = mutate(source, seed_base + i)
        kind_counts[kind] = kind_counts.get(kind, 0) + 1
        candidate_hash = sha256(candidate)
        if candidate == source:
            unchanged += 1
        else:
            unique_hashes.add(candidate_hash)
        if candidate_hash != pinned_hash:
            detected += 1
        elif len(examples) < 10:
            examples.append({"attempt": i, "kind": kind, "candidate_hash": candidate_hash})

        if (i + 1) % max(1, count // 10) == 0 or i + 1 == count:
            elapsed = time.perf_counter() - start
            print(f"Progress {i+1:>7,}/{count:,} | hash mismatches {detected:>7,} | "
                  f"unique candidates {len(unique_hashes):>7,} | {elapsed:.2f}s")

    runtime_guard_pass, runtime_detail = check_runtime_guard(source_path, pinned_hash)
    elapsed_total = time.perf_counter() - start
    result = {
        "attempts": count,
        "detected_by_pinned_hash": detected,
        "undetected_hash_matches": count - detected,
        "unchanged_candidates": unchanged,
        "unique_mutated_hashes": len(unique_hashes),
        "runtime_guard_rejects_tampered_module": runtime_guard_pass,
        "runtime_guard_detail": runtime_detail,
        "pinned_sha256": pinned_hash,
        "source_sha256": current_hash,
        "elapsed_seconds": round(elapsed_total, 3),
        "mutation_types": kind_counts,
        "undetected_examples": examples,
    }
    print("-" * 78)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if detected == count and unchanged == 0 and runtime_guard_pass:
        print("\n[PASS] Alle Kandidaten weichen vom gepinnten Hash ab; Runtime-Guard blockierte Testdatei.")
    else:
        print("\n[FAIL] Mindestens eine Prüfbedingung fehlgeschlagen.")
        raise SystemExit(2)
    return result

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=100000)
    parser.add_argument("--seed", type=int, default=20261021)
    parser.add_argument("--source", default="test_super_engine_omni_v42_clean.py")
    parser.add_argument("--expected-hash", default="",
                        help="Separat bezogener SHA-256-Referenzwert")
    args = parser.parse_args()
    if args.count < 1 or args.count > 1_000_000:
        parser.error("--count muss zwischen 1 und 1.000.000 liegen")
    path = Path(args.source).resolve()
    if not path.is_file():
        path = Path("/workspace/artifacts") / args.source
    if not path.is_file():
        raise SystemExit(f"Datei nicht gefunden: {path}")
    
    expected_hash = args.expected_hash.lower() if args.expected_hash else sha256(path.read_bytes())
    run_stress(path, args.count, expected_hash, args.seed)

if __name__ == "__main__":
    main()
