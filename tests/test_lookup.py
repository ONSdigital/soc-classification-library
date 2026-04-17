"""Tests for SOCLookup and SOCRephraseLookup.

Mirrors sic-classification-library/tests/test_sic_lookup.py: uses fixture-based
mock CSV data so tests do not require external Excel or config.
"""

# pylint: disable=C0301,missing-function-docstring,redefined-outer-name

import pandas as pd
import pytest

from occupational_classification.lookup.soc_lookup import SOCLookup, SOCRephraseLookup


@pytest.fixture
def mock_data(tmp_path):
    """Creates a temporary CSV file with mock SOC data.

    Args:
        tmp_path (Path): Temporary directory provided by pytest.

    Returns:
        Path: Path to the temporary CSV file.
    """
    data = pd.DataFrame(
        {
            "label": ["4111", "8139", "1131", "2112"],
            "documents": [
                "benefits fraud investigator (government)",
                "saw doctor",
                "vice president (banking)",
                "zoologist",
            ],
        }
    )
    file_path = tmp_path / "mock_soc_data.csv"
    data.to_csv(file_path, index=False)
    return file_path


@pytest.fixture
def soc_lookup_fixture(mock_data):
    """Creates an instance of SOCLookup using the mock data.

    Args:
        mock_data (Path): Path to the mock SOC data CSV file.

    Returns:
        SOCLookup: Instance of the SOCLookup class.
    """
    return SOCLookup(data_path=str(mock_data))


@pytest.mark.parametrize(
    "description, expected_label",
    [
        ("benefits fraud investigator (government)", "4111"),
        ("saw doctor", "8139"),
        ("vice president (banking)", "1131"),
        ("zoologist", "2112"),
    ],
)
def test_soc_lookup_find_code_for_title(
    soc_lookup_fixture, description, expected_label
):
    """Tests lookup_dict returns expected label for description (mirrors SIC exact match)."""
    lookup = soc_lookup_fixture.lookup_dict[description]
    assert lookup == expected_label


@pytest.mark.parametrize(
    "description, expected_code, expected_major_group",
    [
        ("benefits fraud investigator (government)", "4111", "4"),
        ("zoologist", "2112", "2"),
    ],
)
def test_lookup(soc_lookup_fixture, description, expected_code, expected_major_group):
    """Tests lookup() returns code, major group and metadata (mirrors SIC)."""
    result = soc_lookup_fixture.lookup(description)
    assert result["description"] == description
    assert result["code"] == expected_code
    assert result["code_major_group"] == expected_major_group
    # With always-on SocMeta, code_meta and major-group meta should be populated
    assert result["code_meta"] is not None
    assert result["code_major_group_meta"] is not None


@pytest.mark.parametrize(
    "code, expected_major_group",
    [
        ("4111", "4"),
        ("2112", "2"),
    ],
)
def test_lookup_code_major_group(soc_lookup_fixture, code, expected_major_group):
    """Tests lookup_code_major_group returns major group from code with metadata (mirrors SIC)."""
    result = soc_lookup_fixture.lookup_code_major_group(code)
    assert result["code_major_group"] == expected_major_group
    assert result["code_major_group_meta"] is not None


@pytest.mark.parametrize(
    "candidates, expected_major_groups",
    [
        ([{"soc_code": "2111"}, {"soc_code": "2431"}], ["2"]),
        ([{"soc_code": "2111"}, {"soc_code": "4111"}], ["2", "4"]),
    ],
)
def test_unique_code_major_group(soc_lookup_fixture, candidates, expected_major_groups):
    """Tests unique_code_major_group returns unique major groups with metadata (mirrors SIC)."""
    result = soc_lookup_fixture.unique_code_major_group(candidates)
    assert len(result) == len(expected_major_groups)
    got = sorted(r["code_major_group"] for r in result)
    assert got == sorted(expected_major_groups)
    for item in result:
        assert item["code_major_group_meta"] is not None


def test_lookup_no_match(soc_lookup_fixture):
    """Tests lookup when no match is found (mirrors SIC test_lookup_no_match)."""
    result = soc_lookup_fixture.lookup("nonexistent description")
    assert result["code"] is None
    # When there is no matching code, meta should also be None.
    assert result["code_meta"] is None
    assert result["code_major_group_meta"] is None


def test_lookup_similarity(soc_lookup_fixture):
    """Tests lookup with similarity enabled (mirrors SIC test_lookup_similarity)."""
    result = soc_lookup_fixture.lookup("fraud", similarity=True)
    assert "potential_matches" in result
    assert result["potential_matches"]["descriptions_count"] > 0


def test_unique_code_major_group_empty_list(soc_lookup_fixture):
    """Tests unique_code_major_group with empty list (mirrors SIC test_unique_code_divisions_empty_list)."""
    result = soc_lookup_fixture.unique_code_major_group([])
    assert result == []


def test_soc_lookup_default_path_uses_example_csv():
    """Tests SOCLookup() with no args uses default example CSV (covers default-path branch for coverage)."""
    # Default path is relative; run from repo root so src/.../data/example_soc_lookup_data.csv exists
    lookup = SOCLookup()
    result = lookup.lookup("chief executives and senior officials")
    assert result["code"] == "1111"
    assert result["code_major_group"] == "1"


def test_soc_lookup_rejects_non_csv_path(tmp_path):
    """SOCLookup rejects legacy non-CSV lookup paths."""
    fake_path = tmp_path / "legacy_lookup.xlsx"
    fake_path.write_text("placeholder", encoding="utf-8")

    with pytest.raises(ValueError, match="must point to a CSV file"):
        SOCLookup(data_path=str(fake_path))


def test_soc_lookup_rejects_legacy_description_column(tmp_path):
    data = pd.DataFrame(
        {
            "description": ["primary teacher", "zoologist"],
            "label": ["2314", "2112"],
        }
    )
    file_path = tmp_path / "soc_lookup_legacy.csv"
    data.to_csv(file_path, index=False)

    with pytest.raises(ValueError, match="Expected columns"):
        SOCLookup(data_path=str(file_path))


# --- SOCRephraseLookup tests (mirrors SIC rephrase coverage) ---


@pytest.fixture
def mock_rephrase_data(tmp_path):
    """Creates a temporary CSV file with mock SOC rephrase data."""
    data = pd.DataFrame(
        {
            "soc_code": ["1111", "2112", "4111"],
            "rephrased_description": [
                "Senior officials and managers",
                "Biological scientists",
                "National government administrative occupations",
            ],
        }
    )
    file_path = tmp_path / "mock_rephrase_soc_data.csv"
    data.to_csv(file_path, index=False)
    return file_path


@pytest.fixture
def soc_rephrase_lookup_fixture(mock_rephrase_data):
    """Creates an instance of SOCRephraseLookup using the mock rephrase data."""
    return SOCRephraseLookup(data_path=str(mock_rephrase_data))


def test_soc_rephrase_lookup_found(soc_rephrase_lookup_fixture):
    """Tests SOCRephraseLookup.lookup when soc_code is found."""
    result = soc_rephrase_lookup_fixture.lookup("1111")
    assert result["soc_code"] == "1111"
    assert result["rephrased_description"] == "Senior officials and managers"


def test_soc_rephrase_lookup_not_found(soc_rephrase_lookup_fixture):
    """Tests SOCRephraseLookup.lookup when soc_code is not found."""
    result = soc_rephrase_lookup_fixture.lookup("9999")
    assert result["soc_code"] == "9999"
    assert "error" in result


def test_soc_rephrase_lookup_int_code(soc_rephrase_lookup_fixture):
    """Tests SOCRephraseLookup.lookup accepts int soc_code (converted to str)."""
    result = soc_rephrase_lookup_fixture.lookup(2112)
    assert result["soc_code"] == "2112"
    assert result["rephrased_description"] == "Biological scientists"


def test_soc_rephrase_process_json(soc_rephrase_lookup_fixture):
    """Tests SOCRephraseLookup.process_json updates main and candidate descriptions."""
    input_json = {
        "soc_code": "1111",
        "soc_description": None,
        "soc_candidates": [
            {"soc_code": "2112"},
            {"soc_code": "4111"},
        ],
    }
    result = soc_rephrase_lookup_fixture.process_json(input_json)
    assert result["soc_description"] == "Senior officials and managers"
    assert result["soc_candidates"][0]["soc_descriptive"] == "Biological scientists"
    assert (
        result["soc_candidates"][1]["soc_descriptive"]
        == "National government administrative occupations"
    )


def test_soc_rephrase_process_json_null_soc_code(soc_rephrase_lookup_fixture):
    """Tests SOCRephraseLookup.process_json when soc_code is None."""
    input_json = {
        "soc_code": None,
        "soc_description": None,
        "soc_candidates": [],
    }
    result = soc_rephrase_lookup_fixture.process_json(input_json)
    assert result["soc_description"] is None


def test_soc_rephrase_lookup_supports_alias_columns(tmp_path):
    """SOC rephrase lookup accepts common alias column names."""
    data = pd.DataFrame(
        {
            "code": ["1139"],
            "description_rephrased": ["Functional managers and directors other roles"],
        }
    )
    file_path = tmp_path / "mock_rephrase_soc_alias_data.csv"
    data.to_csv(file_path, index=False)

    lookup = SOCRephraseLookup(data_path=str(file_path))
    result = lookup.lookup("1139")

    assert result["soc_code"] == "1139"
    assert (
        result["rephrased_description"]
        == "Functional managers and directors other roles"
    )
