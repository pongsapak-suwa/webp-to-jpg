import os
from PIL import Image

# Specify the folder containing the webp images
folder = "path/to/folder"

for file_name in os.listdir(folder):
    if file_name.lower().endswith('.webp'):
        webp_path = os.path.join(folder, file_name)
        jpg_path = os.path.join(folder, file_name.rsplit('.', 1)[0] + '.jpg')
        try:
            # Open and convert the image
            with Image.open(webp_path) as img:
                rgb_image = img.convert('RGB')
                rgb_image.save(jpg_path, 'JPEG')
            print(f"Converted: {file_name} -> {jpg_path}")
            
            # Delete the original webp file
            os.remove(webp_path)
            print(f"Deleted: {webp_path}")
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")
