# OMNI SUPER ENGINE Architecture

## Purpose

This project is organized around a small active runtime and a clean separation between the source package, tests, examples, docs, and historical bundles.

## Active code path

The active Python package lives under `src/omni_engine/` and should remain the canonical runtime entry point for the project.

## Structure

- `src/omni_engine/` contains the package code
- `tests/` contains pytest coverage for the active package
- `examples/` contains runnable usage examples
- `docs/` contains design and release notes
- `archive/` and `legacy/` preserve historical material

## Notes

Historical packages and exported datasets should not be mixed into the active runtime path. They are kept for traceability and reference, but not used as the primary import path.
