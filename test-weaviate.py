import os

import weaviate
import os




client = weaviate.connect_to_local()

if client.is_ready():
    print("✅ Connected to Weaviate!")
else:
    print("❌ Failed to connect.")

#close connection
client.close()
