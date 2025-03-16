import pandas as pd

# Load the original CSV file
input_csv = "output_annotations.csv"  # Replace with your actual CSV filename
output_csv = "transformed.csv"  # Replace with your desired output filename

# Read the CSV into a DataFrame
df = pd.read_csv(input_csv)

# Create a new DataFrame with the required columns
transformed_df = df.rename(columns={"filepath": "image", "meaning": "text"})
transformed_df = transformed_df[["image", "text"]]

# Save the transformed DataFrame to a new CSV
transformed_df.to_csv(output_csv, index=False)

print(f"Transformed CSV saved to {output_csv}")
