import weaviate
from api_keys import WEAVIATE_API_KEY, WEAVIATE_URL, OPENAI_API_KEY

auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)

# Instantiate the client
client = weaviate.Client(
        url = WEAVIATE_URL,
        auth_client_secret=auth_config,
        additional_headers={
            'X-OpenAI-Api-Key': OPENAI_API_KEY 
            }
        )
