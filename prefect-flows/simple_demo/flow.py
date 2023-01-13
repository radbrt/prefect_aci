from prefect import task, flow
from prefect import get_run_logger


@task
def log_secret_value():
    logger = get_run_logger()
    testsecret = "DEFAUT VALUE"
    logger.info(f"Connected to Azure Key Vault and retrieved secret 'testsecret' with value '{testsecret}'")


@flow(name="Simple Demo")
def simple_demo():
    log_secret_value()

if __name__ == '__main__':
    simple_demo()


