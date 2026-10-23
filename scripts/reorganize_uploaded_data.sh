#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

mkdir -p "$ROOT/docs" "$ROOT/src" "$ROOT/tests" "$ROOT/data" "$ROOT/archive" "$ROOT/legacy" "$ROOT/scripts" "$ROOT/config" "$ROOT/reports"

safe_move() {
  local src="$1"
  local dst="$2"
  if [ -e "$src" ]; then
    if [ -e "$dst" ] && [ "$(basename "$src")" != "$(basename "$dst")" ]; then
      local base="$(basename "$src")"
      local ext="${base##*.}"
      local name="${base%.*}"
      local counter=1
      while [ -e "$dst/$base" ] || [ -e "$dst" ]; do
        new_base="${name}_${counter}.${ext}"
        if [ "$ext" = "$base" ]; then
          new_base="${name}_${counter}"
        fi
        if [ ! -e "$dst/$new_base" ]; then
          dst="$dst/$new_base"
          break
        fi
        counter=$((counter + 1))
      done
    fi
    mkdir -p "$(dirname "$dst")"
    mv -n "$src" "$dst"
  fi
}

# Move docs and summaries
for f in *.md *.pdf; do
  [ -e "$f" ] || continue
  case "$f" in
    README.md|CHANGELOG.md|RELEASE_NOTES.md|PROJECT_FINAL_SUMMARY.md|EXECUTIVE_SUMMARY.md|INFO_BLATT.md|TEST_INFO_DATASHEET.md|docs_PROJECT_STATUS.md|REPO_DATA_AND_SCRIPT_UPDATES.md)
      safe_move "$f" "$ROOT/docs/"
      ;;
    *)
      safe_move "$f" "$ROOT/docs/"
      ;;
  esac
done

# Move source files
for f in *.py; do
  [ -e "$f" ] || continue
  safe_move "$f" "$ROOT/src/"
done

# Move tests and validation assets
for f in *.json *.csv; do
  [ -e "$f" ] || continue
  safe_move "$f" "$ROOT/data/"
done

for f in *.png *.jpg *.jpeg *.gif *.svg; do
  [ -e "$f" ] || continue
  safe_move "$f" "$ROOT/reports/"
done

# Move build / archive assets
for f in *.zip; do
  [ -e "$f" ] || continue
  safe_move "$f" "$ROOT/archive/"
done

# Move scripts and config
for f in *.sh *.yml *.yaml *.toml *.ini *.txt; do
  [ -e "$f" ] || continue
  case "$f" in
    *.sh)
      safe_move "$f" "$ROOT/scripts/"
      ;;
    *.yml|*.yaml)
      safe_move "$f" "$ROOT/scripts/"
      ;;
    *.toml|*.ini)
      safe_move "$f" "$ROOT/config/"
      ;;
    *.txt)
      safe_move "$f" "$ROOT/legacy/"
      ;;
  esac
done

# Legacy project snapshots and duplicated full-project bundles
for d in "GESAMT TEILE DES PROJEKTES" "omni_super_engine_v7_complete" "omni_super_engine_v7_complete new update" "qe6d_matlab_export"; do
  [ -e "$d" ] || continue
  safe_move "$d" "$ROOT/legacy/"
done

# Sort nested project copies into a dedicated legacy folder if they are not already in a final project tree.
for d in "$ROOT/legacy"/*; do
  [ -d "$d" ] || continue
  case "$(basename "$d")" in
    "GESAMT TEILE DES PROJEKTES"|"omni_super_engine_v7_complete"|"omni_super_engine_v7_complete new update")
      :
      ;;
  esac
done

# Place the root tests directory in its canonical path if it exists.
if [ -d "$ROOT/tests" ] && [ "$(ls -A "$ROOT/tests" 2>/dev/null)" != "" ]; then
  mkdir -p "$ROOT/tests/legacy"
  find "$ROOT/tests" -mindepth 1 -maxdepth 1 -type f -exec mv -n {} "$ROOT/tests/legacy/" \; 2>/dev/null || true
fi

# Final notice
cat <<'EOF'
Repository organization complete.

Canonical structure:
- docs/
- src/
- tests/
- data/
- reports/
- archive/
- scripts/
- config/
- legacy/

Any duplicate or historical bundles were preserved in legacy/ and archive/.
EOF
