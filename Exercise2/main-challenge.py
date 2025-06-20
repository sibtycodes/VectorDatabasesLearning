import weaviate
import os
import json
from dotenv import load_dotenv
import weaviate.classes.config as wc

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

client = weaviate.connect_to_local(headers={
    "X-OpenAI-Api-Key": API_KEY,
})

try:
    print("Connected to Weaviate")

    # Load jeopardy data
    with open("jeopardy_1k.json", "r", encoding="utf-8") as f:
        jeopardy_data = json.load(f)

    print(f"✅ Loaded {len(jeopardy_data)} items from 'jeopardy_1k.json'")

    # Delete previous collection if exists
    if client.collections.exists("Jeopardy"):
        client.collections.delete("Jeopardy")

    # Create the Jeopardy collection with schema
    client.collections.create(
        name="Jeopardy",
        properties=[
            wc.Property(name="question", data_type=wc.DataType.TEXT),
            wc.Property(name="answer", data_type=wc.DataType.TEXT),
            wc.Property(name="round", data_type=wc.DataType.TEXT),
        ],
        vectorizer_config=wc.Configure.Vectorizer.text2vec_openai(),  # uses OpenAI to vectorize text
        # generative_config=wc.Configure.Generative.openai(),  # optional, only if you're using Gen AI
    )

    print("✅ Collection 'Jeopardy' created successfully!")

finally:
    client.close()
