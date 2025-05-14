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
