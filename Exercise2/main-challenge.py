import weaviate

import weaviate.classes.config as wc

import json

client = weaviate.connect_to_local()

try:
    print("✅ Connected to Weaviate")

    # Load the JSON dataset
    # with open("jeopardy_1k.json", "r", encoding="utf-8") as f:
    #     jeopardy_data = json.load(f)
    #
    # print(f"✅ Loaded {len(jeopardy_data)} items from 'jeopardy_1k.json'")
    # print(f"Sample keys: {list(jeopardy_data[0].keys())}")

    # Remove old collection if it exists
    # if client.collections.exists("Jeopardy"):
    #     client.collections.delete("Jeopardy")
    #
    # client.collections.create(
    #     name="Jeopardy",
    #     properties=[
    #         wc.Property(name="question", data_type=wc.DataType.TEXT),
    #         wc.Property(name="answer", data_type=wc.DataType.TEXT),
    #         wc.Property(name="round", data_type=wc.DataType.TEXT),  # ✅ stored but not vectorized
    #     ],
    #     vectorizer_config=wc.Configure.Vectorizer.multi2vec_clip(
    #         text_fields=[
    #             wc.Multi2VecField(name="question", weight=1.0),
    #             wc.Multi2VecField(name="answer", weight=0.5)
    #         ]
    #     )
    # )
    #
    # print("✅ Collection 'Jeopardy' created successfully!")
    #
    # # Insert objects
    # collection = client.collections.get("Jeopardy")
    # added = 0
    #
    # for item in jeopardy_data:
    #     question = item.get("Question")
    #     answer = item.get("Answer")
    #     round_ = item.get("Round")
    #
    #     if question and answer and round_:
    #         collection.data.insert({
    #             "question": question.strip(),
    #             "answer": answer.strip(),
    #             "round": round_.strip()
    #         })
    #         added += 1
    #
    # print(f"✅ Added {added} valid items to the 'Jeopardy' collection")

    # --------------ABOVE CODE IS FOR SETUP ONLY----------------WE HAVE A COLLECTION NOW AND VECTORIZED DATA----------------

    # response = client.collections.get("Jeopardy").aggregate.over_all(total_count=True)
    # print("🔢 Total objects in 'Jeopardy':", response.total_count)

    response = client.collections.get("Jeopardy").query.near_text(
        query="spicy food recipes",
        limit=4,
        return_properties=["question", "answer"],
        return_metadata=["distance"]
    )

    results = []
    for obj in response.objects:
        results.append({
            "question": obj.properties.get("question"),
            "answer": obj.properties.get("answer"),
            "distance": obj.metadata.distance
        })

    print(json.dumps(results, indent=2))


finally:
    client.close()
    print("🔒 Weaviate connection closed.")
