# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).
---
## [0.1.3] - 2025-07-08

## Added
- type hints

## Changed
- `src.occupational_classification.meta.soc_meta` SocMeta instantiation method: now requires to specify a path to the file containing data for soc structure.
- `src.occupational_classification.hierarchy.soc_hierarchy` load_hierarchy: takes additinoal argument _structure_data_path_ to allow specifying path to the file containing data for SOC structure.

---
## [0.1.2] - 2025-06-10

## Added
- config for easier access to the data;
- documentation - `README.md` containing overview, features, prerequisites, setup and testing instructions. Example usage is shown in `notebooks/soc_2025_05_01.py`;
- tests for `occupational_classification.data_access.soc_data_access` and `occupational_classification.lookup.soc_lookup`.

## Changed
- use SocMeta for populating objects in SOC;
- `all_leaf_text` in `occupational_classification.hieararchy.soc_hierarchy` to return disaggregated job titles and group titles.

## Removed
- duplicated functionalities in `occupational_classification.hieararchy.soc_hierarchy`.

---

## [0.1.1] - 2025-05-14

## Added
- `combine_job_title` function under `occupational_classification.data_access.soc_data_access`

### Changed

- Renamed `occupational_classification.meta.soc_meta` and `occupational_classification.meta.classification_meta`
- Updated `SocMeta` class in `occupational_classification.meta.soc_meta`
- Updated `load_soc_index` in `occupational_classification.data_access.soc_data_access` to process job titles from SOC index
---

## [0.1.0] - 2025-05-07

### Added

- occupational_classsification.hierarchy.soc_hierarchy and dependencies
- tests/test_soc_data_structure.py

