import weaviate

import os
import json
from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("OPENAI_API_KEY")

client = weaviate.connect_to_local()


try:

    metadata = client.get_meta()


    print(json.dumps(metadata, indent=2))

finally:

    client.close()

