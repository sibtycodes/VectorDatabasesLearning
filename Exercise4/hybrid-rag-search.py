import weaviate
import weaviate.classes.config as wc
from weaviate.classes.query import MetadataQuery
from weaviate.classes.query import Filter
from weaviate.util import image_encoder_b64
import os, json, base64, io
from pathlib import Path
import requests

client = weaviate.connect_to_local()


print("Weaviate is ready!") if client.is_ready() else None

try:
    # #first download data in json
    # resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
    # data = json.loads(resp.text)
    # #save it to file in beautiful json format
    # with open('jeopardy_tiny.json', 'w') as f:
    #     json.dump(data, f, indent=4)

    #get the json from file
    with open('jeopardy_tiny.json', 'r') as f:
        data = json.load(f)
    print("Data loaded from jeopardy_tiny.json")

    # #Create collection "JeopardyRAGSearch"
    # if client.collections.exists("JeopardyRAGSearch"):
    #     print("Collection 'JeopardyRAGSearch' already exists. Deleting it...")
    #     client.collections.delete("JeopardyRAGSearch")
    #
    # client.collections.create(
    #     name="JeopardyRAGSearch",
    #     properties=[
    #         wc.Property(name="question", data_type=wc.DataType.TEXT),
    #         wc.Property(name="answer", data_type=wc.DataType.TEXT),
    #         wc.Property(name="category", data_type=wc.DataType.TEXT)
    #     ],
    #     vectorizer_config=wc.Configure.Vectorizer.multi2vec_clip(
    #         text_fields=[
    #             wc.Multi2VecField(name="question", weight=1.0),
    #             wc.Multi2VecField(name="answer", weight=1.0),
    #             wc.Multi2VecField(name="category", weight=1.0)
    #         ]
    #     )
    # )
    print("✅ Collection 'JeopardyRAGSearch' created successfully!")

    # add the json data to the collection
    jeopardyCollection = client.collections.get("JeopardyRAGSearch")
    # for item in data:
    #     jeopardyCollection.data.insert({
    #         "question": item["Question"],
    #         "answer": item["Answer"],
    #         "category": item["Category"]
    #     })
    #     print(f"Inserted item: {item['Question']}")
    #
    # print("JeopardyRAGSearch collection inserted ")

    #get the collection with vectors and direction

    results = jeopardyCollection.query.near_text(
        query="organ",
        limit=3,
        return_properties=["question", "answer", "category"],
        return_metadata=MetadataQuery(distance=True),
        include_vector=True,

    )


    for o in results.objects:
        merged = {**o.properties, "vector": o.vector["default"]}
        print(json.dumps(merged, indent=4))













finally:
    client.close()
    print("Connection closed. 🌸")


