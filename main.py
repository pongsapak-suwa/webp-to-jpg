import os
from PIL import Image

# Define the folder containing .webp files
input_folder = "path/to/your/folder"
output_folder = "path/to/output/folder"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Convert each .webp file to .jpg
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith('.webp'):
        webp_path = os.path.join(input_folder, file_name)
        jpg_path = os.path.join(output_folder, file_name.rsplit('.', 1)[0] + '.jpg')
        try:
            # Open and convert to RGB (WebP might have transparency)
            with Image.open(webp_path) as img:
                rgb_image = img.convert('RGB')
                rgb_image.save(jpg_path, 'JPEG')
            print(f"Converted: {file_name} -> {jpg_path}")
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")
