import weaviate
import json
from api_keys import WEAVIATE_URL, WEAVIATE_API_KEY

auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

client = weaviate.Client(
        url = WEAVIATE_URL,
        auth_client_secret= auth_config
        )

meta_info = client.get_meta()
print(json.dumps(meta_info, indent=2))
