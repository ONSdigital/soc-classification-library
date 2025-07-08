# %% [markdown]
# # Provide a simple example on the usage of files.

# %%
from occupational_classification._config.main import get_config
from occupational_classification.data_access.soc_data_access import (
    load_soc_index,
    load_soc_structure,
)
from occupational_classification.hierarchy import soc_hierarchy
from occupational_classification.lookup.soc_lookup import SOCLookup, SOCRephraseLookup
from occupational_classification.meta.soc_meta import SocDB, SocMeta

# %% [markdown]
# ### Read the data from files using get_config()

# %%
soc_df_input = load_soc_structure(get_config()["data_source"]["soc_structure"])

# %%
soc_df_input.sample(5)

# %%
soc_index = load_soc_index(get_config()["data_source"]["soc_index"])

# %%
soc_index.sample(5)

# %% [markdown]
# ### Perform data operations on columns for soc structure file.

# %%
soc_df = SocDB.create_soc_dataframe(soc_df_input)

# %%
soc_df.sample(5)

# %% [markdown]
# ### Accessing information from soc_hierarchy

# %%
# Load hierarchy from the SOC structure and index
hierarchy = soc_hierarchy.load_hierarchy(soc_df, soc_index)

# %%
# Main usage - returns a DF with codes and their corresponding information.
hierarchy.all_leaf_text()

# %% [markdown]
# Access specific attributes of hierarchy (from soc_code, group_title, group_description, group_level, tasks, parent, children, qualifications, job_titles)

# %%
hierarchy["1111"].job_titles

# %% [markdown]
# ## Create a lookup, for identical matches

# %%
soc_lookup = SOCLookup()

# %%
soc_lookup.data.sample(10)

# %% [markdown]
# Find the code for a specific job title

# %%
# soc_lookup.lookup_dict["seed analyst"]
soc_lookup.lookup_dict["vice president (banking)"]

# %% [markdown]
# Access information about the specific job title such as description, code, and meta.

# %%
# soc_lookup.lookup("Machine tester")
# soc_lookup.lookup("benefits fraud investigator (government)")
soc_lookup.lookup("zoologist")

# %% [markdown]
# Find the major group for the specific code.

# %%
soc_lookup.lookup_code_major_group("2112")

# %% [markdown]
# Access meta for the major group of the specified code

# %%
soc_lookup.unique_code_major_group(
    [{"soc_code": "1111"}, {"soc_code": "2111"}, {"soc_code": "9265"}, {"soc_code": "41"}]
)

# %% [markdown]
# ### SOCRephraseLookup

# %%
rephrased_soc = SOCRephraseLookup()

# %% [markdown]
# Access group title for code

# %%
rephrased_soc.lookup_dict["1"]

# %%
rephrased_soc.lookup("1111")

# %%
input_json = {
    "soc_code": "1111",
    "soc_candidates": [{"soc_code": "1112"}, {"soc_code": "1121"}],
}
processed_json = rephrased_soc.process_json(input_json)

# %%
processed_json

# %% [markdown]
# ## Other methods to access meta

# %%
soc_meta = SocMeta(get_config()["data_source"]["soc_structure"])

# %%
soc_meta.soc_meta[3]

# %% [markdown]
# Possible to go through code, soc2020_group_title, group_description, qualifications, and tasks.

# %%
soc_meta.soc_meta[3].get("group_description")

# %%
soc_lookup.meta.soc_meta[3]

# %%
soc_lookup.meta.get_meta_by_code("2431")

# %% [markdown]
# # Misc


