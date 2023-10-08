import weaviate
import json

auth_config = weaviate.AuthApiKey(api_key="readonly-demo")

client = weaviate.Client(
        url= "https://edu-demo.weaviate.network",
        auth_client_secret= auth_config
        )
meta = client.get_meta()
print(json.dumps(meta, indent=2))
