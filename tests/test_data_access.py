"""Tests for SOC data access utilities."""

# pylint: disable=missing-function-docstring,redefined-outer-name,unused-argument

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
