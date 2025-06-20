import weaviate
# import os
import json
# from dotenv import load_dotenv
import weaviate.classes.config as wc

# # Load environment variables from .env (not required here but left in for future use)
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")
#
# # Connect to local Weaviate (no API key needed for local + transformers)
client = weaviate.connect_to_local()

try:
    print("✅ Connected to Weaviate")

    # Load the JSON dataset
    with open("jeopardy_1k.json", "r", encoding="utf-8") as f:
        jeopardy_data = json.load(f)

    print(f"✅ Loaded {len(jeopardy_data)} items from 'jeopardy_1k.json'")
    print(f"Sample keys: {list(jeopardy_data[0].keys())}")

    # Remove old collection if it exists
    if client.collections.exists("Jeopardy"):
        client.collections.delete("Jeopardy")

    # Create new collection schema
    client.collections.create(
        name="Jeopardy",
        properties=[
            wc.Property(name="question", data_type=wc.DataType.TEXT),
            wc.Property(name="answer", data_type=wc.DataType.TEXT),
            wc.Property(name="round", data_type=wc.DataType.TEXT),
        ],
        vectorizer_config=wc.Configure.Vectorizer.text2vec_transformers()
    )

    print("✅ Collection 'Jeopardy' created successfully!")

    # Insert objects
    collection = client.collections.get("Jeopardy")
    added = 0

    for item in jeopardy_data:
        question = item.get("Question")
        answer = item.get("Answer")
        round_ = item.get("Round")

        if question and answer and round_:
            collection.data.insert({
                "question": question.strip(),
                "answer": answer.strip(),
                "round": round_.strip()
            })
            added += 1

    print(f"✅ Added {added} valid items to the 'Jeopardy' collection")

finally:
    client.close()
    print("🔒 Weaviate connection closed.")
