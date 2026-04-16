"""SOC data access for lookup CSVs and packaged ONS SOC2020 workbooks.

Lookup flows (``SOCLookup``) use CSV paths with ``documents`` and ``label`` columns.

Hierarchy and embedding flows (``soc-classification-utils``) use packaged Excel
workbooks via ``(package_name, filename)`` tuples, matching the previous utils
module behaviour.
"""

from __future__ import annotations

import logging
from importlib.resources import files

import pandas as pd

from occupational_classification.hierarchy.soc_hierarchy import SOC, load_hierarchy
from occupational_classification.meta.soc_meta import SocMeta

logger = logging.getLogger(__name__)

SocIndexSource = str | tuple[str, str]
SocStructureSource = str | tuple[str, str]


def _require_lookup_csv(path: str) -> None:
    if not str(path).lower().endswith(".csv"):
        raise ValueError(
            "SOC lookup loads from lookup CSV only (.csv); use workbook tuples for Excel."
        )


def _resolve_lookup_columns(df: pd.DataFrame) -> tuple[str, str]:
    text_col = "documents"
    code_col = "label"
    if text_col not in df.columns or code_col not in df.columns:
        raise ValueError(
            "Lookup CSV missing required columns. "
            "Expected columns ['documents', 'label']."
        )
    return text_col, code_col


def _combine_soc_index_job_title(row: pd.Series) -> str:
    job_title = ""
    if pd.notna(row["add"]):
        job_title += f"{row['add']} "
    if pd.notna(row["indexocc"]):
        job_title += str(row["indexocc"])
    if pd.notna(row["ind"]):
        job_title += f" ({row['ind']})"
    return job_title.strip()


def _load_soc_index_workbook(resource_ref: tuple[str, str]) -> pd.DataFrame:
    pkg, filename = resource_ref
    file_path = files(pkg).joinpath(filename)
    logger.debug("Loading SOC index from %s", file_path)

    soc_index_df = pd.read_excel(
        file_path,
        sheet_name="SOC2020 coding index",
        usecols=["SOC_2020", "INDEXOCC_-_natural_word_order", "ADD", "IND"],
        dtype=str,
    )
    soc_index_df.columns = [col.lower() for col in soc_index_df.columns]
    soc_index_df = soc_index_df.rename(
        columns={"soc_2020": "code", "indexocc_-_natural_word_order": "indexocc"}
    )
    soc_index_df["title"] = soc_index_df.apply(_combine_soc_index_job_title, axis=1)
    soc_index_df = soc_index_df.dropna(subset=["code", "title"])
    soc_index_df = soc_index_df[["code", "title"]]
    soc_index_df["code"] = soc_index_df["code"].astype(str).str.strip()
    soc_index_df["title"] = soc_index_df["title"].astype(str).str.strip()
    soc_index_df = soc_index_df[soc_index_df["code"].str.fullmatch(r"\d+")]
    return soc_index_df


def _load_soc_structure_workbook(resource_ref: tuple[str, str]) -> pd.DataFrame:
    pkg, filename = resource_ref
    file_path = files(pkg).joinpath(filename)
    logger.debug("Loading SOC structure from %s", file_path)

    soc_df = pd.read_excel(
        file_path,
        sheet_name="SOC2020 descriptions",
        usecols=[
            "SOC\n2020 Major Group",
            "SOC\n2020 Sub-Major Group",
            "SOC\n2020 Minor Group",
            "SOC 2020 Unit Group",
        ],
        dtype=str,
    )

    codes: set[str] = set()
    for col in soc_df.columns:
        for raw in soc_df[col].dropna():
            code = str(raw).strip()
            if code.isdigit():
                codes.add(code)
    return pd.DataFrame({"code": sorted(codes, key=lambda c: (len(c), c))})


def load_soc_index(source: SocIndexSource) -> pd.DataFrame:
    """Load SOC index rows as ``code`` and ``title``.

    Args:
        source: Either a path to a lookup CSV (``documents``, ``label``), or a
            ``(package_name, xlsx_filename)`` tuple for the ONS coding index workbook.

    Returns:
        DataFrame with ``code`` and ``title`` columns.
    """
    if isinstance(source, tuple):
        return _load_soc_index_workbook(source)
    if isinstance(source, str):
        _require_lookup_csv(source)
        df = pd.read_csv(source, dtype=str)
        text_col, code_col = _resolve_lookup_columns(df)

        out = df[[code_col, text_col]].copy()
        out = out.rename(columns={code_col: "code", text_col: "title"})
        out = out.dropna(subset=["code", "title"])
        out["code"] = out["code"].astype(str).str.strip()
        out["title"] = out["title"].astype(str).str.strip().str.capitalize()
        out = out[out["code"].str.fullmatch(r"\d+")]
        return out.reset_index(drop=True)
    raise TypeError(
        "load_soc_index expects a CSV path (str) or workbook resource tuple (str, str)."
    )


def load_soc_structure(source: SocStructureSource) -> pd.DataFrame:
    """Load SOC structure codes for ``load_hierarchy``.

    Args:
        source: Either a path to the same lookup CSV used for index loading, or a
            ``(package_name, xlsx_filename)`` tuple for the ONS structure workbook.

    Returns:
        DataFrame with a single ``code`` column.
    """
    if isinstance(source, tuple):
        return _load_soc_structure_workbook(source)
    if isinstance(source, str):
        _require_lookup_csv(source)
        df = pd.read_csv(source, dtype=str)
        _, code_col = _resolve_lookup_columns(df)

        codes: set[str] = set()
        for raw in df[code_col].dropna():
            label = str(raw).strip()
            if not label.isdigit():
                continue
            for i in range(1, len(label) + 1):
                codes.add(label[:i])

        sorted_codes = sorted(codes, key=lambda c: (len(c), c))
        return pd.DataFrame({"code": sorted_codes})
    raise TypeError(
        "load_soc_structure expects a CSV path (str) or workbook resource tuple (str, str)."
    )


def load_soc_hierarchy(
    index_ref: tuple[str, str], structure_ref: tuple[str, str]
) -> SOC:
    """Load SOC hierarchy from packaged index and structure workbooks."""
    soc_index_df = load_soc_index(index_ref)
    soc_df = load_soc_structure(structure_ref)
    return load_hierarchy(soc_df, soc_index_df)


def get_soc_meta(structure_ref: tuple[str, str]):
    """Return in-library SOC metadata (``SocMeta.soc_meta``).

    ``structure_ref`` is unused; retained for config shape parity with SIC callers.

    Args:
        structure_ref: Tuple ``(package_name, path)`` (unused).

    Returns:
        The ``soc_meta`` mapping from ``SocMeta()``.
    """
    _ = structure_ref
    return SocMeta().soc_meta


def load_text_from_config(config_section: tuple[str, str]) -> str:
    """Load UTF-8 text from a packaged resource tuple ``(package_name, filename)``."""
    pkg, filename = config_section
    file_path = files(pkg).joinpath(filename)

    logger.debug("Loading text from %s", file_path)

    with file_path.open(encoding="utf-8") as f:
        return f.read()
