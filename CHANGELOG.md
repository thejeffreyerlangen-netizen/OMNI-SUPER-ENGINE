# Changelog

All notable changes to this project will be documented in this file.

## [8.2.0] - 2026-10-24

### Added
- release alignment for the v8.2 engineering baseline
- updated repository metadata and version tracking
- documentation cleanup for the stable core release

### Changed
- updated README to reflect the v8.2 release version
- normalized release messaging around the deterministic simulation stack
- clarified the project documentation around active code and legacy archives

### Notes
- Legacy packaged artifacts remain in the repository root but are not part of the active runtime path.
- The active code path remains the stable deterministic engine and test suite under the project root and `tests/`.

## [7.0.0] - 2026-10-22

### Added
- professional project metadata via `pyproject.toml`
- clean repository documentation and installation guidance
- validation-focused pytest configuration
- project-local test runner for standardized local execution
- repository status documentation for release readiness
- CI workflow for automated validation on push and pull request
- MIT license metadata

### Changed
- updated README to reflect the active v7.0 core architecture
- normalized dependency configuration
- improved setup and validation workflow clarity
- aligned release documentation with the active engineering codebase

### Notes
- Legacy packaged artifacts remain in the repository root but are not part of the active runtime path.
- The active code path is the v7.0 physics bridge and test suite under `omni_super_engine_master_v7.py` and `tests/`.
