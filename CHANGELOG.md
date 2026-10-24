# Changelog

All notable changes to this project will be documented in this file.

## [8.2.0] - 2026-10-24

### Added
- organized package structure under `src/omni_engine/`
- clean release layout for active code, tests, docs, and examples
- explicit archive and legacy staging areas for historical artifacts
- structured release notes for the v8.2 baseline

### Changed
- aligned project metadata and documentation to v8.2.0
- clarified the active runtime path versus historical bundles
- kept legacy data and export artifacts outside the active package layout

### Notes
- Historical ZIP files, reports, and research data remain in `archive/` and `legacy/` for reference.
- Active runtime code is expected to live under `src/omni_engine/`.

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
