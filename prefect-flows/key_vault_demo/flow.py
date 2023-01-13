from prefect import task, flow
from prefect import get_run_logger
from prefect.blocks.notifications import SlackWebhook
from prefect.blocks.system import String
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def az_secret(secret_name) -> str:
    kv_url = String.load("kv-url").value

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=kv_url, credential=credential)
    kv_secret = client.get_secret(secret_name).value
    return kv_secret


@task
def log_secret_value():
    logger = get_run_logger()
    testsecret = az_secret("testsecret")
    logger.info(f"Connected to Azure Key Vault and retrieved secret 'testsecret' with value '{testsecret}'")


@flow(name="Key Vault Demo")
def key_vault_demo():
    log_secret_value()

if __name__ == '__main__':
    key_vault_demo()


