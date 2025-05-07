# %% [markdown]
# Provides a simple example on the usage of files.

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
from occupational_classification.meta.socDB import soc_meta

# %%
soc_df = soc_meta.create_soc_dataframe(soc_df_input)

# %%
soc_df.sample(5)

# %%
from occupational_classification.hierarchy import soc_hierarchy

# %%
soc = soc_hierarchy.load_hierarchy(soc_df, soc_index)

# %%
# Main usage - returns a DF with codes and their corresponding information.
soc.all_leaf_text()

# %%
# example codes used: 1, 2, and 4 digit long for accessing information regarding specific code.
soc["1"].print_all()

# %%
soc["11"].print_all()

# %%
soc["1111"].print_all()

# %%



