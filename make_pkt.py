import pandas as pd
from PIL import Image
import io

# Read the CSV file
csv_file = "./output_annotations.csv"
df = pd.read_csv(csv_file)

# Function to load an image
def load_image(filepath):
    try:
        with open(filepath, "rb") as f:
            img = f.read()
        return img  # Store the image as binary data
    except Exception as e:
        print(f"Error loading image {filepath}: {e}")
        return None

# Create a new DataFrame
data = {
    "image": [load_image(filepath) for filepath in df["filepath"]],
    "text": df["meaning"]
}

new_df = pd.DataFrame(data)

# Save as Parquet
parquet_file = "annotations.parquet"
new_df.to_parquet(parquet_file, engine="pyarrow", index=False)
