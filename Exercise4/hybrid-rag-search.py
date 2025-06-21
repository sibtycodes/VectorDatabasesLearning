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
    #first download data in json
    resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
    data = json.loads(resp.text)
    #save it to file in beautiful json format
    with open('jeopardy_tiny.json', 'w') as f:
        json.dump(data, f, indent=4)

finally:
    client.close()
    print("Connection closed. 🌸")


