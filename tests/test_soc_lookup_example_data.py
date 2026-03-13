"""Tests for SOCLookup using the packaged example SOC lookup dataset."""

from importlib import resources

import pandas as pd

from occupational_classification.lookup.soc_lookup import SOCLookup


def _get_example_csv_path() -> str:
    # Mirror the survey-assist-api SOCLookupClient default, which resolves the
    # lookup CSV from the "data" package directory, aligned with SIC.
    data_dir = resources.files("occupational_classification.data")
    return str(data_dir / "example_soc_lookup_data.csv")


def test_soc_lookup_example_exact_match():
    """SOCLookup returns expected code for an exact description from the example CSV."""
    csv_path = _get_example_csv_path()
    # Sanity check that the CSV is readable and has expected columns
    df = pd.read_csv(csv_path, dtype=str)
    assert "description" in df.columns
    assert "label" in df.columns

    lookup = SOCLookup(data_path=csv_path)
    result = lookup.lookup("chief executives and senior officials")

    assert result["code"] == "1111"
    assert result["description"] == "chief executives and senior officials"


def test_soc_lookup_example_similarity():
    """SOCLookup similarity search returns multiple potential matches."""
    csv_path = _get_example_csv_path()
    lookup = SOCLookup(data_path=csv_path)

    result = lookup.lookup("managers", similarity=True)

    assert "potential_matches" in result
    potential = result["potential_matches"]
    assert potential["descriptions_count"] >= 1
    assert any("managers" in desc for desc in potential["descriptions"])
