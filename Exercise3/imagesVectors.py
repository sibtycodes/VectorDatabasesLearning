import weaviate
import weaviate.classes.config as wc
from weaviate.classes.query import MetadataQuery
from weaviate.classes.init import AdditionalConfig, Timeout
from weaviate.classes.query import Filter
from weaviate.util import image_encoder_b64
import os, json, base64, io
from PIL import Image
from IPython.display import display
from pathlib import Path

client = weaviate.connect_to_local()

try:
    #
    # if client.collections.exists("ImagesCollection"):
    #     client.collections.delete("ImagesCollection")
    #
    # # * only use image blob vector
    # client.collections.create(
    #     name="ImagesCollection",
    #     # properties - imageblob and name
    #     properties=[
    #         wc.Property(name="imageBlob", data_type=wc.DataType.BLOB),
    #         wc.Property(name="name", data_type=wc.DataType.TEXT)
    #     ],
    #     vectorizer_config=wc.Configure.Vectorizer.multi2vec_clip(
    #         image_fields=[
    #             wc.Multi2VecField(name="imageBlob", weight=1.0)
    #         ]
    #     )
    # )
    # print("✅ Collection 'ImagesCollection' created successfully!")

    # !Images collection
    imagesCollection = client.collections.get("ImagesCollection")

    # # Insert images from the folder
    # for filename in os.listdir("../Images"):
    #     if filename.lower().endswith((".jpg", ".jpeg", ".png")):
    #         with open(os.path.join("../Images", filename), "rb") as f:
    #             image_b64 = image_encoder_b64(f)
    #
    #         imagesCollection.data.insert({
    #             "imageBlob": image_b64,
    #             "name": filename  # Store the image name
    #
    #         })
    #         print(f"Inserted image: {filename}")
    # print("✅ All images inserted into 'ImagesCollection'")

    print("ImagesCollection exists:", imagesCollection.exists())

    # ! Text-to-image vector search - NOT USING BECAUSE NAMES OF IMAGES ARE NOT PROPERLY SET SO WE SEARCH BY IMAGE ONLY
    # ! res = imagesCollection.query.near_text(
    # !     query="spicy food",
    # !     limit=3,
    # !     return_properties=["name", "imageBlob"],
    # !     return_metadata=MetadataQuery(distance=True)
    # ! )
    # !
    # ! for obj in res.objects:
    # !     print(f"Image Name: {obj.properties['name']}, Distance: {obj.metadata.distance:.2f}")
    # !     img_data = base64.b64decode(obj.properties["imageBlob"])
    # !     display(Image.open(io.BytesIO(img_data)))

    # ! Image vector search by image

    test_image_path = "../TestImages/n02102040_251.JPEG"
    with open(test_image_path, "rb") as image_file:
        test_image_b64 = image_encoder_b64(image_file)

    resultImageQuery = imagesCollection.query.near_image(
        near_image=Path(test_image_path),
        limit=3,
        return_properties=["name", "imageBlob"],
        return_metadata=["distance"]
    )

    print("🔍 Image query results:")
    for obj in resultImageQuery.objects:
        print(f"Image Name: {obj.properties['name']}, Distance: {obj.metadata.distance:.2f}")
        img_data = base64.b64decode(obj.properties["imageBlob"])
        display(Image.open(io.BytesIO(img_data)))





finally:
    # close
    client.close()
    print("Closed connection to Weaviate")
