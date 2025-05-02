# %% [markdown]
# Provides a simple example on the usage of files.

# %%
from occupational_classification.data_access.soc_data_access import (
    load_soc_index,
    load_soc_structure,
)

# %%
soc_df_input = load_soc_structure(
    "../data/soc2020volume1structureanddescriptionofunitgroupsexcel16042025.xlsx"
)

# %%
soc_df_input.sample(5)

# %%
soc_index = load_soc_index("../data/soc2020volume2thecodingindexexcel16042025.xlsx")

# %%
soc_index.sample(5)

# %%
from occupational_classification.meta.socDB import soc_meta

# %%
soc_structure = soc_meta.create_soc_dataframe(soc_df_input)

# %%
soc_structure.sample(5)

# %%
