# Example Data

Snippets of example data, useful for testing and understanding format, are detailed below. For full source data, see the SOC 2020 releases linked from `docs/index.md`.

## Example SOC Lookup Data

The SOC lookup examples are derived from the ONS SOC 2020 coding index and structure
files (see `docs/index.md`). The library ships with a small, self-contained slice of
that data to exercise the lookup and hierarchy APIs.

### SOC Lookup - Example Rows

Typical lookup rows contain:

- **code**: SOC 2020 unit group code (for example `1111`)
- **title**: example job title (for example `Chief executives and senior officials`)

This data is exposed via `load_soc_index(...)` and used by `SOCLookup` to build an
exact-match dictionary from lowercased job titles to SOC codes.

## Example Rephrased SOC Data

The library also includes an example SOC rephrase dataset in:

- `src/occupational_classification/data/example_rephrased_soc_data.csv`

This CSV is intentionally small and is designed for testing and demonstrations rather
than full SOC 2020 coverage.

### Rephrased SOC - Example Rows

Each row in the rephrase CSV contains:

- **soc_code**: SOC 2020 code as a string (for example `1111`)
- **rephrased_description**: a shorter, respondent-friendly description for that code
  (for example “Senior officials and executives”).

`SOCRephraseLookup` loads this file and exposes a simple `lookup(soc_code)` method and
`process_json(...)` helper, which are consumed by `survey-assist-api` to attach
rephrased SOC descriptions to classification responses.