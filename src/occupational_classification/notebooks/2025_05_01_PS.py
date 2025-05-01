# %%
from occupational_classification.data_access import soc_data_access

# %%
soc_df_input = soc_data_access.load_soc_structure(
    "../data/soc2020volume1structureanddescriptionofunitgroupsexcel16042025.xlsx"
)

# %%
soc_df_input.head()

# %%
soc_index = soc_data_access.load_soc_index(
    "../data/soc2020volume2thecodingindexexcel16042025.xlsx"
)

# %%
soc_index.head()
