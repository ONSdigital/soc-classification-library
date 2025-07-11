"""Module for the 'SocDB' class and 'SocMeta' class.

This module defines the 'SocDB' class, which makes necessary changes to the
structure of the data being passed (soc_structure).
This module defines the 'SocMeta' class, which retrieves titles and details
for given SOC codes.
"""

import pandas as pd

from occupational_classification.data_access.soc_data_access import load_soc_structure
from occupational_classification.meta.classification_meta import ClassificationMeta


class SocDB:
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
            if "tasks" in soc_dict:
                soc_dict["tasks"] = soc_dict["tasks"].replace("\n", "").split("~")[1:]
            soc_dict["group_description"] = soc_dict["group_description"].replace(
                "\n", " "
            )
            soc_dict["soc2020_group_title"] = soc_dict["soc2020_group_title"].replace(
                "\n", " "
            )
            soc_validated = ClassificationMeta.model_validate(soc_dict)
            soc_list.append(soc_validated.dict())
        return soc_list

    def create_soc_dataframe(self) -> pd.DataFrame:
        """Takes a list of dictionaries and converts to a dataframe."""
        return pd.DataFrame(SocDB(self).create_soc_dictionary())


class SocMeta:
    """SOC Meta data model class for SOC codes and their desriptions.
    Load and manage data related to SOC codes.

    Args:
        structure_data_path (str): a path to the file containing soc structure
        data.

    Attributes:
        df (pd.DataFrame): DataFrame containing data for SOC structure.
        soc_meta (List[ClassificationMeta]): List of ClassificationMeta objects
    """

    def __init__(self, structure_data_path: str):
        self.df = load_soc_structure(structure_data_path)
        self.soc_meta = SocDB(self.df).create_soc_dictionary()

    def get_meta_by_code(self, code: str) -> dict:
        """Retrieve title and details for a given SOC code.

        Args:
            code (str): A SOC code to lookup.

        Returns:
            dict: Dictionary with title and detail if found, else an error message.
        """
        for element in self.soc_meta:
            if element["code"] == code:
                return {
                    "code": element.get("code", None),
                    "group_title": element.get("soc2020_group_title", None),
                    "group_description": element.get("group_description", None),
                    "entry_routes_and_quals": element.get("qualifications", []),
                    "tasks": element.get("tasks"),
                }

        # No match found
        return {"error": f"No metadata found for SOC code {code}"}
