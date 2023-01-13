from prefect_azure.credentials import AzureContainerInstanceCredentials
import os

tenant_id = os.getenv("TENANT_ID")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

aci_credentials = AzureContainerInstanceCredentials(
    name="aci-sp",
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret,
)

aci_credentials.save('aci-sp', overwrite=True)