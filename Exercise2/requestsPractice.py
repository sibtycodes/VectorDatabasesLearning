import requests
import json

# Define the URL for the JSON data
# Note: The image shows a truncated URL. I'm using the full URL you provided earlier.
data_url = 'https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json'

# --- Download the data ---
print("--- Downloading data ---")
try:
    resp = requests.get(data_url)
    resp.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    data = json.loads(resp.text) # Load data from the response text
    print("Data downloaded successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error downloading data: {e}")
    # Exit or handle the error appropriately if data download fails
    data = None

if data is not None:
    # --- Parse the JSON and preview it ---
    print("\n--- Data Preview ---")
    print(f"Type of data: {type(data)}")
    print(f"Number of items in data: {len(data)}")

    if len(data) > 0:
        print("\n--- First Item (data[0]) Preview ---")
        # Use json.dumps with indent=2 for pretty printing JSON
        print(json.dumps(data[0], indent=2))
    else:
        print("Data is empty, no first item to display.")

    # --- Helper function for pretty printing JSON ---
    def json_print(data_to_print):
        """
        Prints the given data (assumed to be JSON-serializable) in a human-readable
        format with an indent of 2 spaces.
        """
        print(json.dumps(data_to_print, indent=2))

    # --- Print out the rest of the data (entire dataset) ---
    print("\n--- Full Data (using json_print function) ---")
    json_print(data)

else:
    print("\nCould not proceed with data parsing and printing as data download failed.")


 