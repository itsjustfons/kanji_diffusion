import pandas as pd
import json

# Load the CSV file
input_csv = "transformed.csv"  # Replace with your actual CSV filename
metadata_json = "metadata.json"  # Desired output JSON file

# Read the CSV into a DataFrame
df = pd.read_csv(input_csv)

# Create a list of dictionaries for metadata entries
metadata = []
for _, row in df.iterrows():
    entry = {
        "file_name": row["filename"],
        "text": row["text"]
    }
    metadata.append(entry)

# Write the metadata to a JSON file
with open(metadata_json, "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=4)

print(f"Metadata JSON saved to {metadata_json}")
