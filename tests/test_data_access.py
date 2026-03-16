"""Tests for SOC data access utilities."""

# pylint: disable=missing-function-docstring,redefined-outer-name,unused-argument

from unittest.mock import patch

import pandas as pd

from src.occupational_classification.data_access import soc_data_access


# combine_job_title()
def test_combine_job_title_all():
    """Test case, where all job title components are present."""
    data = {"natural_word": "Teacher", "add": "mathematics", "ind": "secondary school"}
    row = pd.Series(data)
    expected_job_title = "mathematics Teacher (secondary school)"
    assert soc_data_access.combine_job_title(row) == expected_job_title


def test_combine_job_title_missing_add():
    """Test case, where the "add" component is missing (is NaN)."""
    data = {"natural_word": "Teacher", "add": float("nan"), "ind": "secondary school"}
    row = pd.Series(data)
    expected_job_title = "Teacher (secondary school)"
    assert soc_data_access.combine_job_title(row) == expected_job_title


def test_combine_job_title_missing_ind():
    """Test case, where the "ind" component is missing (is NaN)."""
    data = {"natural_word": "Teacher", "add": "mathematics", "ind": float("nan")}
    row = pd.Series(data)
    expected_job_title = "mathematics Teacher"
    assert soc_data_access.combine_job_title(row) == expected_job_title


def test_combine_job_title_missing_add_ind():
    """Test case, where "add" and "ind" components are missing (are NaN)."""
    data = {"natural_word": "Teacher", "add": float("nan"), "ind": float("nan")}
    row = pd.Series(data)
    expected_job_title = "Teacher"
    assert soc_data_access.combine_job_title(row) == expected_job_title


def test_combine_job_title_non_string():
    """Test case, where "add" and "ind" components are numerical."""
    data = {"natural_word": "Teacher", "add": 1, "ind": 2}
    row = pd.Series(data)
    expected_job_title = "1 Teacher (2)"
    assert soc_data_access.combine_job_title(row) == expected_job_title


# load_soc_index()


def test_load_soc_index_load(tmp_path):
    """Test basic functionality with a mock CSV file."""
    mock_data = {
        "SOC_2020": ["1111", "2222", "3333"],
        "INDEXOCC_-_natural_word_order": ["Teacher", "Engineer", "Manager"],
        "ADD": ["mathematics", "nos", "sales"],
        "IND": ["secondary school", "broadcasting", "garage"],
    }
    mock_df = pd.DataFrame(mock_data)
    csv_path = tmp_path / "soc_index.csv"
    mock_df.to_csv(csv_path, index=False)
    with patch("pandas.read_csv", return_value=mock_df):
        df = soc_data_access.load_soc_index(str(csv_path))
    expected_data = {
        "code": ["1111", "2222", "3333"],
        "title": [
            "Mathematics teacher (secondary school)",
            "Nos engineer (broadcasting)",
            "Sales manager (garage)",
        ],
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(df, expected_df)


def test_load_soc_index_code_filter(tmp_path):
    """Test the code filter for '}}}}'."""
    mock_data = {
        "SOC_2020": ["1111", "}}}}"],
        "INDEXOCC_-_natural_word_order": ["Teacher", "Engineer"],
        "ADD": ["mathematics", "nos"],
        "IND": ["secondary school", "broadcasting"],
    }
    mock_df = pd.DataFrame(mock_data)
    csv_path = tmp_path / "soc_index.csv"
    mock_df.to_csv(csv_path, index=False)
    with patch("pandas.read_csv", return_value=mock_df):
        df = soc_data_access.load_soc_index(str(csv_path))
    expected_data = {
        "code": ["1111"],
        "title": [
            "Mathematics teacher (secondary school)",
        ],
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(df, expected_df)


def test_load_soc_index_dropna(tmp_path):
    """Test the rows with missing values for 'code' or
    'INDEXOCC_-_natural_word_order' are dropped.
    """
    mock_data = {
        "SOC_2020": ["1111", None, "3333"],
        "INDEXOCC_-_natural_word_order": ["Teacher", "Engineer", None],
        "ADD": ["mathematics", "nos", "sales"],
        "IND": ["secondary school", "broadcasting", "garage"],
    }
    mock_df = pd.DataFrame(mock_data)
    csv_path = tmp_path / "soc_index.csv"
    mock_df.to_csv(csv_path, index=False)
    with patch("pandas.read_csv", return_value=mock_df):
        df = soc_data_access.load_soc_index(str(csv_path))
    expected_data = {
        "code": ["1111"],
        "title": [
            "Mathematics teacher (secondary school)",
        ],
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(df, expected_df)
