import weaviate
from weaviate import EmbeddedOptions
import os
import json

API_KEY = os.getenv("OPENAI_API_KEY")

client = weaviate.WeaviateClient(
    embedded_options=EmbeddedOptions(),
    additional_headers={
        "X-OpenAI-Api-Key": API_KEY
    }
)


try:
    # Get the metadata from the Weaviate client
    metadata = client.get_meta()

    # Pretty-print the metadata as JSON
    print(json.dumps(metadata, indent=2))

finally:
    # It's good practice to close the client when you're done,
    # especially with embedded instances to free up resources.
    client.close()

# Add your client code here.
# When the client exits, the embedded instance also exits