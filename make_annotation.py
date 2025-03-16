import os
import xml.etree.ElementTree as ET
import pandas as pd

def parse_kanji_xml(xml_path, output_csv, image_dir):
    """
    Parse the XML file and create a CSV file for kanji annotations.

    Args:
        xml_path (str): Path to the XML file.
        output_csv (str): Output CSV file path.
        image_dir (str): Directory containing kanji images.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Prepare lists to store extracted data
    image_paths = []
    kanji_list = []
    meanings_list = []

    for character in root.findall('character'):
        # Extract kanji literal
        kanji = character.find('literal').text

        # Generate image file path
        image_filename = f"kanji_{kanji}.png"
        image_path = os.path.join(image_dir, image_filename)

        # Check if the image exists
        if not os.path.isfile(image_path):
            print(f"Warning: Image {image_filename} not found.")
            continue

        # Extract English meanings
        rmgroup = character.find("reading_meaning/rmgroup")
        if rmgroup is not None:
            meanings = [meaning.text for meaning in rmgroup.findall('meaning') if 'm_lang' not in meaning.attrib]
            if meanings:
                meaning_text = ', '.join(meanings)
            else:
                meaning_text = ""  # Fallback in case no meanings are found
        else:
            meaning_text = ""

        # Append data to lists
        image_paths.append(image_path)
        kanji_list.append(kanji)
        meanings_list.append(meaning_text)

    # Create a DataFrame
    data = {
        "filepath": image_paths,
        "kanji": kanji_list,
        "meaning": meanings_list
    }
    df = pd.DataFrame(data)

    # Remove rows with empty meanings
    df = df[df['meaning'].str.strip().astype(bool)]

    # Save to a CSV file
    df.to_csv(output_csv, index=False)
    print(f"CSV file saved to {output_csv}")



# Example usage
xml_file = "../kanjidic2.xml"  # Replace with the path to your XML file
output_file = "./output_annotations.csv"  # Replace with your desired output path
kanji_image_dir = "../kanji_images"  # Replace with the path to your image directory

parse_kanji_xml(xml_file, output_file, kanji_image_dir)
