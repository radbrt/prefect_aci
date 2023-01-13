from prefect.blocks.system import String
import os

kv_name = os.getenv("KV_NAME")

kv_url = f"https://{ kv_name }.vault.azure.net"
kv_url_block = String(value=kv_url)
kv_url_block.save("kv-url", overwrite=True)