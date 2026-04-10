# SOC Classification Libraries

This code is used to implement a Standard Occupational Classification (SOC) library used by Survey Assist API.

## Data sources
This library loads packaged CSV example data by default for lookup and hierarchy; the Excel workbooks below are the official ONS SOC 2020 publications (authoritative scheme reference, or for preparing your own CSV extracts).
- [SOC 2020 Volume 1: structure and descriptions of unit groups](https://www.ons.gov.uk/methodology/classificationsandstandards/standardoccupationalclassificationsoc/soc2020/soc2020volume1structureanddescriptionsofunitgroups). Download [link](https://www.ons.gov.uk/file?uri=/methodology/classificationsandstandards/standardoccupationalclassificationsoc/soc2020/soc2020volume1structureanddescriptionsofunitgroups/soc2020volume1structureanddescriptionofunitgroupsexcel16042025.xlsx)
- [SOC 2020 Volume 2: the coding index](https://www.ons.gov.uk/methodology/classificationsandstandards/standardoccupationalclassificationsoc/soc2020/soc2020volume2codingrulesandconventions). Download [link](https://www.ons.gov.uk/file?uri=/methodology/classificationsandstandards/standardoccupationalclassificationsoc/soc2020/soc2020volume2codingrulesandconventions/soc2020volume2thecodingindexexcel16042025v2.xlsx)

## Available Utilities

- [SOC Lookup](guide.md): Lookup SOC from a well known list of occupations.
- SOC rephrase support: packaged example data and `SOCRephraseLookup` for mapping `soc_code` values to respondent-friendly rephrased descriptions.
- Example datasets: the package ships with small SOC lookup and SOC rephrase CSVs for testing/demonstration (see `docs/example_data.md`).
