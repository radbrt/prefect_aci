from prefect.deployments import Deployment
from prefect.filesystems import Azure
import uuid
from prefect_azure.container_instance import AzureContainerInstanceJob

azure_container_instance_job_block = AzureContainerInstanceJob.load("aci")
# Import flow function from flow.py
from flow import key_vault_demo

az_block = Azure.load("az-storage")

daily_deployment = Deployment.build_from_flow(
    flow=key_vault_demo,
    name="Manual Deployment",
    version="1",
    storage=az_block,
    infrastructure=azure_container_instance_job_block,
    work_queue_name="armaci",
    path=str(uuid.uuid4()),
)


daily_deployment.apply(upload=True)