from prefect_azure.container_instance import AzureContainerInstanceJob
from prefect_azure.container_instance import AzureContainerInstanceCredentials
import os

acisp = AzureContainerInstanceCredentials.load("aci-sp")
subscription_id = os.getenv("SUBSCRIPTION_ID")

azi = AzureContainerInstanceJob(
    name="aci",
    image="radbrt/orion_aci_base:latest",
    cpu=1,
    memory=1,
    aci_credentials=acisp,
    subscription_id=subscription_id,
    resource_group_name="aci-rg",
    task_start_timeout_seconds=480,
    identities=[f"/subscriptions/{ subscription_id }/resourcegroups/aci-rg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/orionid"]
)

azi.save('aci', overwrite=True)