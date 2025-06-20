import weaviate
import weaviate.classes.config as wc
from weaviate.classes.query import MetadataQuery
from weaviate.classes.init import AdditionalConfig, Timeout
from weaviate.classes.query import Filter
from weaviate.util import image_encoder_b64
import os, json, base64
from PIL import Image
from IPython.display import display

client = weaviate.connect_to_local()

try:
    if client.collections.exists("ImagesCollection"):
        client.collections.delete("ImagesCollection")

    client.collections.create(
        name="ImagesCollection",
        #properties - imageblob and name
        properties=[
            wc.Property(name="imageBlob", data_type=wc.DataType.BLOB),
            wc.Property(name="name", data_type=wc.DataType.TEXT)
        ],
        vectorizer_config=wc.Configure.Vectorizer.multi2vec_clip(
            text_fields=[
                wc.Multi2VecField(name="name", weight=1.0)
            ],
            image_fields=[
                wc.Multi2VecField(name="imageBlob", weight=1.0)
            ]
        )
    )

    print("✅ Collection 'ImagesCollection' created successfully!")

finally:
    #close
    client.close()
    print("Closed connection to Weaviate")