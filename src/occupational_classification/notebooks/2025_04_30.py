# %%
from google.cloud import storage


# %%
def download_from_gcs(project_id, bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(
        f"Downloaded storage object {source_blob_name} from bucket {bucket_name} to {destination_file_name}"
    )


project_id = "classifai-sandbox"
bucket_name = "classifai-app-data"

# %%
source_blob_name = "soc2020volume1structureanddescriptionofunitgroupsexcel16102024.xlsx"
destination_file_name = (
    "data/soc2020volume1structureanddescriptionofunitgroupsexcel16102024.xlsx"
)
download_from_gcs(project_id, bucket_name, source_blob_name, destination_file_name)

# %%
source_blob_name = "soc2020volume2thecodingindexexcel16102024.xlsx"
destination_file_name = "data/soc2020volume2thecodingindexexcel16102024.xlsx"
download_from_gcs(project_id, bucket_name, source_blob_name, destination_file_name)

# %%
from occupational_classification import get_config
from occupational_classification.data_access import soc_data_access

soc_df_input = soc_data_access.load_soc_structure(
    get_config()["lookups"]["soc_structure"]
)

# %%
soc_df_input.head()
