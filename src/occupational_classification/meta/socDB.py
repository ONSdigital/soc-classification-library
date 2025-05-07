"""Module for the 'soc_meta' class.

This module defines the 'soc_meta' class, which makes necessary changes to the
structure of the data being passed (soc_structure).
"""

import pandas as pd

from occupational_classification.meta.soc_meta_model import ClassificationMeta


class soc_meta:
    """Loads data from the config file.

    Converts group level into one column, based on the length of the code.
    Returns a list of dictionaries (use create_soc_dictionary method)
    or a DataFrame (use create_soc_dataframe method).
    """

    def __init__(self, df):
        self.df = df

    def code_selection(self, soc_dict: dict) -> dict:
        """Selects the meaningful 1, 2, 3, or 4 digit long code.
            Aggregates into one column "code".

        Returns:
            Dictionary (dict) with not aggregated codes.
        """
        selected_key = next(
            (
                k
                for k in [
                    "soc2020_major_group",
                    "soc2020_sub-major_group",
                    "soc2020_minor_group",
                    "soc_2020_unit_group",
                ]
                if soc_dict[k] != "<blank>"
            ),
            None,
        )
        cleaned_data = {k: v for k, v in soc_dict.items() if v != "<blank>"}
        cleaned_data["code"] = cleaned_data.pop(selected_key)
        return cleaned_data

    def create_soc_dictionary(self) -> list:
        """Iterates through the dataframe with SOC and converts to dictionaries.

        Returns:
            List of dictionaries, such as:
                {"code": <code>,
                "soc2020_group_title": <group_title>,
                "group_description": <group_description>,
                "qualifications": <entry_level_requirements_and_qualifications>,
                "tasks": <tasks>}
        """
        soc_list = []
        df = self.df

        num_rows = len(self.code_selection(df.to_dict())["code"])

        for row in range(num_rows):
            soc_dict = self.code_selection(df.loc[row])
            soc_validated = ClassificationMeta.model_validate(soc_dict)
            soc_list.append(soc_validated.dict())
        return soc_list

    def create_soc_dataframe(self) -> pd.DataFrame:
        """Takes a list of dictionaries and converts to a dataframe."""
        return pd.DataFrame(soc_meta(self).create_soc_dictionary())
