"""Provide data access for key files.

Filepaths are provided in config: "src/occupational_classification/_config".
"""

import pandas as pd


def load_soc_index(filepath: str) -> pd.DataFrame:
    """Load SOC index.

    Provides a list of over 32,000 titles associated with employment.
    """
    soc_index_df = pd.read_excel(
        filepath,
        sheet_name="SOC2020 coding index",
        usecols=["SOC_2020", "INDEXOCC_-_natural_word_order", "ADD", "IND"],
        dtype=str,
    )

    soc_index_df.columns = [col.lower() for col in soc_index_df.columns]

    soc_index_df = soc_index_df.rename(
        columns={"indexocc_-_natural_word_order": "natural_word"}
    )

    return soc_index_df


def load_soc_structure(filepath: str) -> pd.DataFrame:
    """Load SOC structure.

    Provides structure with all levels and names of the SOC 2020.

    Returns:
        DataFrame with group code, group title, group description and list of tasks.
    """
    soc_df = pd.read_excel(
        filepath,
        sheet_name="SOC2020 descriptions",
        usecols=[
            "SOC\n2020 Major Group",
            "SOC\n2020 Sub-Major Group",
            "SOC\n2020 Minor Group",
            "SOC 2020 Unit Group",
            "SOC\n2020 \nGroup Title",
            "Typical Entry Routes And Associated Qualifications",
            "Group  Description",
            "Tasks",
        ],
        dtype=str,
    )
    soc_df.columns = [
        col.lower().replace(" ", "_").replace("__", "_").replace("\n", "")
        for col in soc_df.columns
    ]
    soc_df = soc_df.rename(
        columns={"typical_entry_routes_and_associated_qualifications": "qualifications"}
    )

    for col in soc_df.columns:
        soc_df[col] = soc_df[col].str.strip()

    return soc_df
