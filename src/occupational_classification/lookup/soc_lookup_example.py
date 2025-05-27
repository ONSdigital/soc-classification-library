"""This module provides example usage of the SOCLookup and SOCRephraseLookup classes.

Classes:
    SOCLookup: Provides methods for looking up SOC codes
    and their major groups.
    SOCRephraseLookup: Provides methods for rephrasing SOC descriptions.

Example Usage:
    - Demonstrates how to use SOCLookup to retrieve SOC code information.
    - Demonstrates how to use SOCRephraseLookup to rephrase SOC
      descriptions and process JSON responses.
"""

from typing import Any

from occupational_classification._config.main import get_config
from occupational_classification.lookup.soc_lookup import SOCLookup, SOCRephraseLookup

# Example usage of SOCLookup
print("Example usage of SOCLookup")
soc_lookup = SOCLookup(data_path=get_config()["data_source"]["soc_index"])
result = soc_lookup.lookup("Barista")
print(result)

print("\n")
print("Example usage of SOCLookup with code major group")
soc_lookup = SOCLookup(data_path=get_config()["data_source"]["soc_index"])
result = soc_lookup.lookup_code_major_group("1111")
print(result)

print("\n")
print("Example usage of SOCLookup with unique code major group")
result_list: list[dict[str, Any]] = soc_lookup.unique_code_major_group(
    [{"soc_code": "1111"}, {"soc_code": "2111"}, {"soc_code": "9265"}]
)
print(result_list)

print("\n")
print("Example usage of SOCRephraseLookup with lookup")
# Example usage of SOCRephraseLookup
soc_rephrase_lookup = SOCRephraseLookup(
    data_path_structure=get_config()["data_source"]["soc_structure"],
    data_path_index=get_config()["data_source"]["soc_index"],
)
# Retrieve reviewed description for a specific SOC code
rephrased_result = soc_rephrase_lookup.lookup("1111")
print(rephrased_result)

print("\n")
print("Example usage of SOCRephraseLookup with process_json")
# Process a JSON response to rephrase SOC descriptions
input_json = {
    "soc_code": "1111",
    "soc_candidates": [{"soc_code": "1112"}, {"soc_code": "1121"}],
}
processed_json = soc_rephrase_lookup.process_json(input_json)
print(processed_json)
