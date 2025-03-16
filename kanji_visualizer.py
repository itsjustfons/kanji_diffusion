import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

# Load the XML data
xml_file = "kanjidic2.xml"  # Replace with your XML file path
tree = ET.parse(xml_file)
root = tree.getroot()

# Font setup
font_path = "./fonts/Noto_Sans_JP/static/NotoSansJP-Thin.ttf"  # Replace with the actual font path
font_size = 200
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print("Font not found or not supported. Using default font.")
    font = ImageFont.load_default()

# Function to create an image for each kanji
def create_kanji_image(character):
    try:
        # Extract Kanji character
        literal = character.find("literal").text

        # Debug print
        print("Processing Kanji: {}".format(literal))

        # Image setup
        img_width, img_height = 500, 500
        background_color = (255, 255, 255)  # White
        text_color = (0, 0, 0)  # Black

        image = Image.new("RGB", (img_width, img_height), background_color)
        draw = ImageDraw.Draw(image)

        # Measure text size to center it
        text_width, text_height = draw.textsize(literal, font=font)
        x_position = (img_width - text_width) // 2
        y_position = (img_height - text_height) // 2

        # Draw the Kanji in the center
        draw.text((x_position, y_position), literal, fill=text_color, font=font)

        # Save the image
        output_file = "./kanji_images/kanji_{}.png".format(literal)
        image.save(output_file)
        print("Image saved as {}".format(output_file))

    except Exception as e:
        print("Error processing Kanji {}: {}".format(character.find("literal").text, e))

# Process each kanji in the XML
for character in root.findall("character"):
    create_kanji_image(character)
