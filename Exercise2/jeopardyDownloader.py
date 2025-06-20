import requests
import json

# URL of the JSON data
url = "https://raw.githubusercontent.com/weaviate-tutorials/intro-workshop/main/data/jeopardy_1k.json"

# Send HTTP GET request
response = requests.get(url)

# Raise error if request failed
response.raise_for_status()

# Parse JSON content
jeopardy_data = response.json()

# Save to local file
with open("jeopardy_1k.json", "w", encoding="utf-8") as f:
    json.dump(jeopardy_data, f, ensure_ascii=False, indent=2)

print("✅ Data downloaded and saved to 'jeopardy_1k.json'")
