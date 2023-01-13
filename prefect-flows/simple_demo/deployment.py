from prefect.deployments import Deployment
from prefect.filesystems import Azure
import os
import uuid
from prefect_azure.container_instance import AzureContainerInstanceJob

azure_container_instance_job_block = AzureContainerInstanceJob.load("aci")
# Import flow function from flow.py
from flow import simple_demo

az_block = Azure.load("az-storage")
# kubernetes_job_block = KubernetesJob.load("orion-mini")

daily_deployment = Deployment.build_from_flow(
    flow=simple_demo,
    name="Simple Deployment",
    version="1",
    storage=az_block,
    infrastructure=azure_container_instance_job_block,
    work_queue_name="armaci",
    path=str(uuid.uuid4()),
)


daily_deployment.apply(upload=True)