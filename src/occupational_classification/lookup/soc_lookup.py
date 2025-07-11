"""This module provides the `SOCLookup` and `SOCRephraseLookup` classes, which facilitate
the lookup of Standard Occupational Classification (SOC) codes based on descriptions and
rephrased descriptions. It also handles preprocessing of SOC data and provides metadata
for the classifications.

The data is provided from ONS, as in docs/index.md.
To access data:
    ```
    from occupational_classification._config.main import get_config
    get_config().CONFIG_NAME
    ```

Classes:
    SOCLookup: A class for loading SOC data, performing lookups, and managing metadata.
    SOCRephraseLookup: A class for performing rephrased lookups of SOC codes.
"""

from typing import Any, Optional, Union

from occupational_classification._config.main import get_config
from occupational_classification.data_access.soc_data_access import (
    load_soc_index,
)
from occupational_classification.meta.soc_meta import SocMeta

UNIT_CODE_LEN = 4


class SOCLookup:
    """A class for performing lookups of SOC codes based on descriptions.

    Attributes:
        data (pd.DataFrame): The SOC data loaded from a CSV file.
        lookup_dict (dict[str, str]): A dictionary mapping descriptions to SOC codes.
        meta (SocDB): Metadata for SOC classifications.

    Methods:
        lookup(description: str, similarity: bool = False) -> dict[str, Any]:
            Looks up an SOC code based on the given description.
    """

    def __init__(
        self,
        data_path: str = get_config()["data_source"]["soc_index"],
    ):
        """Initialises the SOCLookup class by loading SOC data from a CSV file.

        Args:
            data_path (str): The path to the CSV file containing SOC data.
        """
        self.data = self.data_preparation(data_path)
        self.lookup_dict: dict[str, str] = self.data.set_index("description").to_dict()[
            "label"
        ]
        self.meta: SocMeta = SocMeta(get_config()["data_source"]["soc_structure"])

    def data_preparation(self, data_path):
        """Converts the data for useful format for lookup method.

        Returns:
            pd.DataFrame: A DataFrame containing data useful for lookups.
        """
        data = load_soc_index(data_path)
        data["label"] = data["code"]
        data["description"] = data["title"].str.lower()
        data = data.drop(["title", "code"], axis=1)
        return data

    def lookup(self, description: str, similarity: bool = False) -> dict[str, Any]:
        """Looks up an SOC code based on the given description.

        Args:
            description (str): The description to look up.
            similarity (bool, optional): Whether to perform a similarity-based lookup.
                                         Defaults to False.

        Returns:
            dict[str, Any]: A dictionary containing the matching SOC code and metadata.
        """
        description = description.lower()

        matching_code: Optional[str] = self.lookup_dict.get(description)
        matching_code_meta: Optional[dict[str, Any]] = None
        major_group_meta: Optional[dict[str, Any]] = None

        # Extract the first digit of the code as code_major_group
        matching_code_major_group: Optional[str] = None
        if matching_code:
            # Lookup the most aggregated (Major) group
            matching_code_major_group = matching_code[:1]
            # Lookup the meta data for the code
            matching_code_meta = self.meta.get_meta_by_code(matching_code)
            major_group_meta = self.meta.get_meta_by_code(matching_code_major_group)

        if not matching_code:
            matching_code = None

        potential_matches: dict[str, Any] = {}

        if similarity:
            # Check if the description is mentioned elsewhere in the dataset
            matches = self.data[
                self.data["description"].str.contains(description, na=False)
            ]
            potential_codes = matches["label"].unique()

            potential_codes = potential_codes.tolist()
            potential_descriptions = matches["description"].unique().tolist()

            major_group_codes = list({str(code)[:1] for code in potential_codes})

            # Get meta data associated with each major group code
            major_groups = [
                {
                    "code": major_group_code,
                    "meta": self.meta.get_meta_by_code(major_group_code),
                }
                for major_group_code in major_group_codes
            ]

            # Return the potential labels
            potential_matches = {
                "descriptions_count": len(matches),
                "descriptions": potential_descriptions,
                "codes_count": len(potential_codes),
                "codes": potential_codes,
                "major_groups_count": len(major_group_codes),
                "major_groups": major_groups,
            }

        response: dict[str, Any] = {
            "description": description,
            "code": matching_code,
            "code_meta": matching_code_meta,
            "code_major_group": matching_code_major_group,
            "code_major_group_meta": major_group_meta,
        }
        if similarity:
            response["potential_matches"] = potential_matches

        return response

    def lookup_code_major_group(
        self, code: str
    ) -> dict[str, Optional[Union[str, dict[str, Any]]]]:
        """Retrieve code major group from SOC code.

        Returns:
            dict[str, dict[str, Any]]: A dictionary containing
            the matching Major Group SOC code and Major Group metadata.
        """
        matching_code_meta: Optional[dict[str, Any]] = self.meta.get_meta_by_code(code)
        major_group_meta: Optional[dict[str, Any]] = None
        matching_code_major_group: Optional[str] = None
        if matching_code_meta:
            matching_code_major_group = code[:1]
            major_group_meta = self.meta.get_meta_by_code(matching_code_major_group)
        return {
            "code_major_group": matching_code_major_group,
            "code_major_group_meta": major_group_meta,
        }

    def unique_code_major_group(
        self, soc_candidates: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """Retrieve unique code divisions from SOC candidates.

        Returns:
            list[dict[str, Union[str, dict[str, str]]]]: Major group metadata.
        """
        unique_major_group: dict[str, dict[str, Any]] = {}

        for candidate in soc_candidates:
            major_group_info = self.lookup_code_major_group(candidate["soc_code"])
            code_major_group = major_group_info["code_major_group"]

            # Only add unique divisions
            if (
                isinstance(code_major_group, str)
                and code_major_group not in unique_major_group
            ):
                unique_major_group[code_major_group] = major_group_info

        return list(unique_major_group.values())


class SOCRephraseLookup:
    """A class for performing rephrased lookups of SOC codes based on descriptions.

    This class extends the functionality of SOC lookups by allowing for
    rephrased or alternative descriptions to be matched to SOC codes.

    Attributes:
        rephrase_dict (dict[str, str]): A dictionary mapping rephrased descriptions
            to their corresponding SOC codes.
        meta (SocMeta): Metadata for SOC classifications.

    Methods:
        rephrase_lookup(description: str) -> dict[str, Any]:
            Looks up an SOC code based on a rephrased description.
        add_rephrase_mapping(original: str, rephrased: str) -> None:
            Adds a new rephrase mapping to the lookup dictionary.
    """

    def __init__(self):
        self.meta: SocMeta = SocMeta(structure_data_path = get_config()["data_source"]["soc_structure"])

        self.lookup_dict: dict[str, str] = {
            item["code"]: item["soc2020_group_title"] for item in self.meta.soc_meta
        }

    def lookup(self, soc_code: str) -> dict[str, Union[str, Any]]:
        """Retrieve reviewed description for the given SOC code."""
        if soc_code in self.lookup_dict:
            return {
                "soc_code": soc_code,
                "input_description": self.lookup_dict[soc_code],
            }

        return {"soc_code": soc_code, "error": "SOC code not found"}

    def process_json(self, input_json: dict[str, Any]) -> dict[str, Any]:
        """Process a JSON response to rephrase SOC descriptions."""
        # Update main SOC description
        rephrased_soc_description: Optional[dict[str, Union[str, Any]]] = None

        rephrased_soc_description = (
            self.lookup(input_json["soc_code"])
            if input_json["soc_code"] is not None
            else None
        )

        if rephrased_soc_description:
            input_json["soc_description"] = rephrased_soc_description[
                "input_description"
            ]
        else:
            input_json["soc_description"] = None

        # Update SOC candidates
        for candidate in input_json["soc_candidates"]:
            rephrased_descriptive = self.lookup(candidate["soc_code"])
            if rephrased_descriptive:
                candidate["soc_descriptive"] = rephrased_descriptive[
                    "input_description"
                ]

        return input_json
