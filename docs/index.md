# SOC Classification Libraries

This code is used to implement a Standard Occupational Classification (SOC) library used by Survey Assist API.

## Startup model

This library follows the same startup style as the SIC library:

- `SOCLookup` defaults to packaged example CSV data.
- Lookup and hierarchy loading are CSV-only.
- Metadata is provided in-library via `SocMeta` (code-embedded metadata).

Legacy Excel/config-driven lookup startup paths were removed in SA-649 and are not supported.

## Data sources

Packaged example datasets are the default for local testing and downstream integration:

- `src/occupational_classification/data/example_soc_lookup_data.csv`
- `src/occupational_classification/data/example_rephrased_soc_data.csv`

Official ONS SOC publications can still be used as reference material when preparing your own CSV extracts, but they are not required at constructor/startup time.

## Available Utilities

- [SOC Lookup](guide.md): Lookup SOC from a well known list of occupations.
- SOC rephrase support: packaged example data and `SOCRephraseLookup` for mapping `soc_code` values to respondent-friendly rephrased descriptions.
- Example datasets: the package ships with small SOC lookup and SOC rephrase CSVs for testing/demonstration (see `docs/example_data.md`).
