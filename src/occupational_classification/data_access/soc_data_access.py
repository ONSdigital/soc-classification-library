"""Provide CSV data access for SOC lookup and hierarchy.

Aligned with ``sic-classification-library``: no Excel loaders in this package.
Index and structure are derived from a lookup CSV (``description``, ``label``)
such as ``example_soc_lookup_data.csv``.
"""

import pandas as pd


def _require_lookup_csv(path: str) -> None:
    if not str(path).lower().endswith(".csv"):
        raise ValueError(
            "SOC data loads from lookup CSV only (.csv); Excel workbooks are not supported."
        )


def load_soc_index(filepath: str) -> pd.DataFrame:
    """Load SOC index columns ``code`` and ``title`` from a lookup CSV.

    The file must contain ``description`` and ``label`` columns. ``label`` is
    the SOC unit code.

    Args:
        filepath: Path to the CSV file.

    Returns:
        DataFrame with ``code`` and ``title`` (title capitalised per prior convention).
    """
    _require_lookup_csv(filepath)
    df = pd.read_csv(filepath, dtype=str)
    required = {"description", "label"}
    if not required.issubset(df.columns):
        missing = required - set(df.columns)
        raise ValueError(f"Lookup CSV missing columns: {sorted(missing)}")

    out = df[["label", "description"]].copy()
    out = out.rename(columns={"label": "code", "description": "title"})
    out = out.dropna(subset=["code", "title"])
    out["code"] = out["code"].astype(str).str.strip()
    out["title"] = out["title"].astype(str).str.strip().str.capitalize()
    out = out[out["code"].str.fullmatch(r"\d+")]
    return out.reset_index(drop=True)


def load_soc_structure(filepath: str) -> pd.DataFrame:
    """Build minimal SOC structure (``code`` column) from the same lookup CSV.

    Expands every unit code in ``label`` into itself and all numeric prefixes
    (e.g. ``2314`` → ``2``, ``23``, ``231``, ``2314``) for ``load_hierarchy``.

    Args:
        filepath: Path to a CSV that includes a ``label`` column of SOC codes.

    Returns:
        DataFrame with a single ``code`` column, sorted by length then value.
    """
    _require_lookup_csv(filepath)
    df = pd.read_csv(filepath, dtype=str)
    if "label" not in df.columns:
        raise ValueError("Lookup CSV must contain a 'label' column")

    codes: set[str] = set()
    for raw in df["label"].dropna():
        label = str(raw).strip()
        if not label.isdigit():
            continue
        for i in range(1, len(label) + 1):
            codes.add(label[:i])

    sorted_codes = sorted(codes, key=lambda c: (len(c), c))
    return pd.DataFrame({"code": sorted_codes})
