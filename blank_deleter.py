import os
import csv

# Path to the folder containing images and CSV file
folder_path = './'  # Update this with the correct folder path
csv_file = 'metadata.csv'  # Update this with the name of the CSV file

# Get all the image filenames from the CSV file
image_files_from_csv = set()
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        image_filename = row[0]  # Assuming the first column contains the image filenames
        image_files_from_csv.add(image_filename.strip())

# List all files in the folder
files_in_folder = os.listdir(folder_path)

# Loop through the files and delete the ones not in the CSV
for file in files_in_folder:
    if file.endswith(('.png', '.jpg', '.jpeg')) and file not in image_files_from_csv:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
        print(f"Deleted: {file}")
