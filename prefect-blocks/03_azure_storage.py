from prefect.filesystems import Azure

account_name = "<my-account-name>"
account_key = "<my-account-key>"

az_block = Azure(
    container="flows",
    bucket_path="flows",
    azure_storage_account_name=account_name,
    azure_storage_account_key=account_key
)


az_block.save("az-storage", overwrite=True)