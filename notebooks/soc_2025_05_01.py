# %% [markdown]
# Provides a simple example on the usage of files.

# %% [markdown]
# Reading the data from /src/occupational_classification/data

# %%
from occupational_classification.data_access.soc_data_access import load_soc_index, load_soc_structure

# %%
soc_df_input = load_soc_structure("../src/occupational_classification/data/soc2020volume1structureanddescriptionofunitgroupsexcel16042025.xlsx")

# %%
soc_df_input.sample(5)

# %%
soc_index = load_soc_index("../src/occupational_classification/data/soc2020volume2thecodingindexexcel16042025.xlsx")

# %%
soc_index.sample(5)

# %%
from occupational_classification.meta.soc_meta import SocMeta, SocDB

# %%
soc_df = SocDB.create_soc_dataframe(soc_df_input)

# %%
soc_df.sample(5)

# %% [markdown]
# Accessing information from soc_hierarchy

# %%
from occupational_classification.hierarchy import soc_hierarchy

# %%
hierarchy = soc_hierarchy.load_hierarchy(soc_df, soc_index)

# %%
# Main usage - returns a DF with codes and their corresponding information.
hierarchy.all_leaf_text()

# %%
soc["1"].print_all()

# %% [markdown]
# Creating a lookup, for identical matches

# %%
from occupational_classification.lookup import soc_lookup

# %%
soc = soc_lookup.SOCLookup()

# %%
soc.data.sample(5)

# %%
soc.lookup(description = "bar staff", similarity = True)

# %%
code = "92"

# %%
soc.meta.get_meta_by_code(code)

# %%
SocMeta(soc_df_input).soc_meta[0].keys()

# %%
soc.lookup_code_major_group("9265")

# %%
soc.unique_code_major_group([{"soc_code": "1111"}, {"soc_code": "2111"}, {"soc_code": "9265"}])

# %%
soc_lookup.SOCLookup().data.sample(5)

# %%
rephrased_soc = soc_lookup.SOCRephraseLookup()

# %%
rephrased_soc.data.sample()

# %%
rephrased_soc.lookup_dict.keys()

# %%
rephrased_soc.lookup("1110")

# %%
input_json = {
    "soc_code": "1111",
    "soc_candidates": [{"soc_code": "1112"}, {"soc_code": "1121"}],
}
processed_json = rephrased_soc.process_json(input_json)


# %%
processed_json

# %%



