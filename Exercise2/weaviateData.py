import weaviate
from weaviate import EmbeddedOptions
import os
import json

client = weaviate.WeaviateClient(
    embedded_options=EmbeddedOptions(),
    additional_headers={
        "X-OpenAI-Api-Key": "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"
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