"""Tests for SOC data access utilities."""

# pylint: disable=missing-function-docstring,redefined-outer-name,unused-argument

from unittest.mock import ANY, patch

import pandas as pd
import pytest

from src.occupational_classification.data_access import soc_data_access


def test_load_soc_index_lookup_csv(tmp_path):
    csv_path = tmp_path / "lookup.csv"
    csv_path.write_text(
        "documents,label\nprimary teacher,2314\n",
        encoding="utf-8",
    )
    df = soc_data_access.load_soc_index(str(csv_path))
    pd.testing.assert_frame_equal(
        df,
        pd.DataFrame({"code": ["2314"], "title": ["Primary teacher"]}),
    )


def test_load_soc_index_rejects_legacy_columns(tmp_path):
    csv_path = tmp_path / "lookup.csv"
    csv_path.write_text(
        "description,label\nprimary teacher,2314\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Expected columns"):
        soc_data_access.load_soc_index(str(csv_path))


def test_load_soc_index_rejects_non_csv(tmp_path):
    p = tmp_path / "index.xlsx"
    p.write_bytes(b"")
    with pytest.raises(ValueError, match="lookup CSV only"):
        soc_data_access.load_soc_index(str(p))


def test_load_soc_index_drops_non_numeric_labels(tmp_path):
    csv_path = tmp_path / "lookup.csv"
    csv_path.write_text(
        "documents,label\na,2314\nb,abc\n",
        encoding="utf-8",
    )
    df = soc_data_access.load_soc_index(str(csv_path))
    pd.testing.assert_frame_equal(
        df,
        pd.DataFrame({"code": ["2314"], "title": ["A"]}),
    )


def test_load_soc_index_dropna(tmp_path):
    csv_path = tmp_path / "lookup.csv"
    csv_path.write_text(
        "documents,label\nx,2314\n,2324\ny,\n",
        encoding="utf-8",
    )
    df = soc_data_access.load_soc_index(str(csv_path))
    pd.testing.assert_frame_equal(
        df,
        pd.DataFrame({"code": ["2314"], "title": ["X"]}),
    )


def test_load_soc_structure_from_lookup_csv(tmp_path):
    csv_path = tmp_path / "lookup.csv"
    csv_path.write_text(
        "documents,label\nx,2314\n",
        encoding="utf-8",
    )
    df = soc_data_access.load_soc_structure(str(csv_path))
    assert list(df["code"]) == ["2", "23", "231", "2314"]


def test_load_soc_structure_rejects_non_label_code_column(tmp_path):
    csv_path = tmp_path / "lookup.csv"
    csv_path.write_text(
        "ids,documents,soc_code\n0,x,2314\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Expected columns"):
        soc_data_access.load_soc_structure(str(csv_path))


@pytest.fixture
def soc_index_workbook_ref():
    return ("test.pkg", "soc2020volume2thecodingindexexcel16102024.xlsx")


@patch("src.occupational_classification.data_access.soc_data_access.files")
@patch("src.occupational_classification.data_access.soc_data_access.pd.read_excel")
def test_load_soc_index_from_workbook(mock_read_excel, mock_files, soc_index_workbook_ref):
    mock_files.return_value.joinpath.return_value = "dummy/soc_index.xlsx"
    mock_read_excel.return_value = pd.DataFrame(
        {
            "SOC_2020": ["2314", "4111"],
            "INDEXOCC_-_natural_word_order": [
                "Teacher, primary",
                "Investigator, benefits fraud",
            ],
            "ADD": [None, "Senior"],
            "IND": [None, "Fraud team"],
        }
    )
    result = soc_data_access.load_soc_index(soc_index_workbook_ref)

    mock_read_excel.assert_called_once_with(
        ANY,
        sheet_name="SOC2020 coding index",
        usecols=["SOC_2020", "INDEXOCC_-_natural_word_order", "ADD", "IND"],
        dtype=str,
    )
    called_args, _ = mock_read_excel.call_args
    assert str(called_args[0]).endswith("soc_index.xlsx")
    mock_files.assert_called_once_with("test.pkg")
    assert list(result.columns) == ["code", "title"]
    assert set(result["code"]) == {"2314", "4111"}
    assert "Teacher, primary" in result["title"].tolist()


@patch("src.occupational_classification.data_access.soc_data_access.files")
@patch("src.occupational_classification.data_access.soc_data_access.pd.read_excel")
def test_load_soc_structure_from_workbook(mock_read_excel, mock_files):
    soc_structure_workbook_ref = ("test.pkg", "soc2020volume1structureanddescriptionofunitgroupsexcel16102024.xlsx")
    mock_files.return_value.joinpath.return_value = "dummy/soc_structure.xlsx"
    mock_read_excel.return_value = pd.DataFrame(
        {
            "SOC\n2020 Major Group": ["2", "4"],
            "SOC\n2020 Sub-Major Group": ["23", "41"],
            "SOC\n2020 Minor Group": ["231", "411"],
            "SOC 2020 Unit Group": ["2314", "4111"],
        }
    )
    result = soc_data_access.load_soc_structure(soc_structure_workbook_ref)

    mock_read_excel.assert_called_once_with(
        ANY,
        sheet_name="SOC2020 descriptions",
        usecols=[
            "SOC\n2020 Major Group",
            "SOC\n2020 Sub-Major Group",
            "SOC\n2020 Minor Group",
            "SOC 2020 Unit Group",
        ],
        dtype=str,
    )
    called_args, _ = mock_read_excel.call_args
    assert str(called_args[0]).endswith("soc_structure.xlsx")
    mock_files.assert_called_once_with("test.pkg")
    assert list(result.columns) == ["code"]
    assert {"2", "23", "231", "2314", "4", "41", "411", "4111"} <= set(result["code"])


@patch("src.occupational_classification.data_access.soc_data_access.files")
@patch("src.occupational_classification.data_access.soc_data_access.pd.read_excel")
def test_load_soc_hierarchy_workbook_resources(mock_read_excel, mock_files, soc_index_workbook_ref):
    soc_structure_workbook_ref = ("test.pkg", "soc2020volume1structureanddescriptionofunitgroupsexcel16102024.xlsx")
    mock_files.return_value.joinpath.side_effect = [
        "dummy/soc_index.xlsx",
        "dummy/soc_structure.xlsx",
    ]
    mock_read_excel.side_effect = [
        pd.DataFrame(
            {
                "SOC_2020": ["2314", "4111"],
                "INDEXOCC_-_natural_word_order": [
                    "Teacher, primary",
                    "Investigator, benefits fraud",
                ],
                "ADD": [None, None],
                "IND": [None, None],
            }
        ),
        pd.DataFrame(
            {
                "SOC\n2020 Major Group": ["2", "4"],
                "SOC\n2020 Sub-Major Group": ["23", "41"],
                "SOC\n2020 Minor Group": ["231", "411"],
                "SOC 2020 Unit Group": ["2314", "4111"],
            }
        ),
    ]
    soc = soc_data_access.load_soc_hierarchy(soc_index_workbook_ref, soc_structure_workbook_ref)
    assert mock_files.call_count == 2
    assert "2314" in soc.lookup
    assert soc["2314"].job_titles
