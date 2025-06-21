import weaviate
import weaviate.classes.config as wc
from weaviate.classes.query import MetadataQuery
from weaviate.classes.generate import GenerativeConfig
from weaviate.classes.query import Filter
from weaviate.util import image_encoder_b64
import os, json, base64, io
from pathlib import Path
import requests

from dotenv import load_dotenv

load_dotenv()

GOOGLE_GENERATIVEAI_APIKEY = os.getenv("GOOGLE_GENERATIVEAI_APIKEY")

client = weaviate.connect_to_local(headers={
    "X-Goog-Api-Key": GOOGLE_GENERATIVEAI_APIKEY
})

print("Weaviate is ready!") if client.is_ready() else None

try:
    # #first download data in json
    # resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
    # data = json.loads(resp.text)
    # #save it to file in beautiful json format
    # with open('jeopardy_tiny.json', 'w') as f:
    #     json.dump(data, f, indent=4)

    # get the json from file
    with open('jeopardy_tiny.json', 'r') as f:
        data = json.load(f)
    print("Data loaded from jeopardy_tiny.json")

    # Create collection "JeopardyRAGSearch"
    if client.collections.exists("JeopardyRAGSearch"):
        print("Collection 'JeopardyRAGSearch' already exists. Deleting it...")
        client.collections.delete("JeopardyRAGSearch")

    client.collections.create(
        name="JeopardyRAGSearch",
        properties=[
            wc.Property(name="question", data_type=wc.DataType.TEXT),
            wc.Property(name="answer", data_type=wc.DataType.TEXT),
            wc.Property(name="category", data_type=wc.DataType.TEXT)
        ],
        vectorizer_config=wc.Configure.Vectorizer.multi2vec_clip(
            text_fields=[
                wc.Multi2VecField(name="question", weight=1.0),
                wc.Multi2VecField(name="answer", weight=1.0),
                wc.Multi2VecField(name="category", weight=1.0)
            ]
        ),
        generative_config=wc.Configure.Generative.google(
            model_id="gemini-2.0-flash",
            project_id="gen-lang-client-0499851562"
        )
    )
    print("✅ Collection 'JeopardyRAGSearch' already created successfully!")

    # add the json data to the collection
    jeopardyCollection = client.collections.get("JeopardyRAGSearch")
    for item in data:
        jeopardyCollection.data.insert({
            "question": item["Question"],
            "answer": item["Answer"],
            "category": item["Category"]
        })
        print(f"Inserted item: {item['Question']}")

    print("JeopardyRAGSearch collection inserted ")

    # #get the collection with vectors and direction
    #
    # results = jeopardyCollection.query.near_text(
    #     query="organ",
    #     limit=3,
    #     return_properties=["question", "answer", "category"],
    #     return_metadata=MetadataQuery(distance=True),
    #     include_vector=True,
    #
    # )
    #
    #
    # for o in results.objects:
    #     merged = {**o.properties, "vector": o.vector["default"]}
    #     print(json.dumps(merged, indent=4))
    #

    # # ! Search  and give questions only for organ
    # results = jeopardyCollection.query.near_text(
    #     query="organ",
    #     limit=3,
    #     return_properties=["question"],
    #     return_metadata=MetadataQuery(distance=True)
    # )
    # for o in results.objects:
    #     print(f"Question: {o.properties['question']}")
    #
    # ! RAG search with generative model

    # responseRAG = jeopardyCollection.generate.near_text(
    #     query="animals",
    #     limit=3,
    #     return_properties=["question"],
    #     single_prompt="Answer the Jeopardy question: {question}. If you don't know the answer say I don't know.",
    #     grouped_task="Summarize the following questions and their likely answers.",
    #     generative_provider=GenerativeConfig.google()
    # )
    #
    # #print out response properly
    # for o in responseRAG.objects:
    #     print(f"Properties: {o.properties}")
    #     print(f"Single prompt result: {o.generative.text}")








finally:
    client.close()
    print("Connection closed. 🌸")
