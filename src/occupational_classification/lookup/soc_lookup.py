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

import pandas as pd

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
        data_path: str | None = None,
    ):
        """Initialises the SOCLookup class by loading SOC data from a CSV file.

        Args:
            data_path (str | None): The path to the SOC lookup data.
                When None, uses the example dataset by default, mirroring
                SICLookup startup behaviour.
        """
        # Default startup mirrors SICLookup.
        if data_path is None:
            data_path = (
                "src/occupational_classification/data/example_soc_lookup_data.csv"
            )

        if not data_path.lower().endswith(".csv"):
            raise ValueError("SOCLookup data_path must point to a CSV file")

        # CSV-backed lookup data (example or full index export).
        self.data = pd.read_csv(data_path, dtype=str)
        self.data["description"] = self.data["description"].str.lower()

        # CSV-backed metadata, mirroring SIC's in-library startup pattern.
        self.meta: SocMeta | None = SocMeta()
        self.lookup_dict: dict[str, str] = self.data.set_index("description").to_dict()[
            "label"
        ]

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
            matching_code_major_group = matching_code[:1]
            if self.meta is not None:
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
            potential_codes = matches["label"].unique().tolist()
            potential_descriptions = matches["description"].unique().tolist()

            major_group_codes = list({str(code)[:1] for code in potential_codes})

            major_groups: list[dict[str, Any]] = []
            if self.meta is not None:
                # Get metadata associated with each major group code.
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
        matching_code_major_group: Optional[str] = code[:1] if code else None
        major_group_meta: Optional[dict[str, Any]] = None
        if self.meta is not None and matching_code_major_group is not None:
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
        data (pd.DataFrame): The SOC rephrase data loaded from a CSV file.
        lookup_dict (dict[str, str]): A dictionary mapping SOC codes to rephrased descriptions.
    """

    def __init__(
        self,
        data_path: str = "src/occupational_classification/data/example_rephrased_soc_data.csv",
    ):
        """Initialise the SOCRephraseLookup with a rephrased SOC dataset.

        Args:
            data_path: Path to the CSV file containing rephrased SOC descriptions.
        """
        # Load SOC rephrased descriptions and treat soc_code column as string
        self.data: pd.DataFrame = pd.read_csv(data_path, dtype={"soc_code": str})

        # Create a lookup dictionary for quick access
        self.lookup_dict: dict[str, str] = self.data.set_index("soc_code")[
            "rephrased_description"
        ].to_dict()

    def lookup(self, soc_code: Union[str, int]) -> dict[str, Union[str, Any]]:
        """Retrieve rephrased description for the given SOC code."""
        soc_code = str(soc_code)

        if soc_code in self.lookup_dict:
            return {
                "soc_code": soc_code,
                "rephrased_description": self.lookup_dict[soc_code],
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
                "rephrased_description"
            ]
        else:
            input_json["soc_description"] = None

        # Update SOC candidates
        for candidate in input_json["soc_candidates"]:
            rephrased_descriptive = self.lookup(candidate["soc_code"])
            if rephrased_descriptive:
                candidate["soc_descriptive"] = rephrased_descriptive[
                    "rephrased_description"
                ]

        return input_json
