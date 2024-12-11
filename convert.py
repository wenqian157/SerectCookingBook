from PIL import Image
import pillow_heif
import os

pillow_heif.register_heif_opener()

# Folder containing .heic files
input_folder = "C:\D\GitHub\Cooking\heic"
output_folder = "C:\D\GitHub\Cooking\jpg"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(".heic"):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".jpg")
        try:
            with Image.open(input_path) as img:
                img.convert("RGB").save(output_path, "JPEG")
                print(f"Converted: {file_name} -> {output_path}")
        except Exception as e:
            print(f"Failed to convert {file_name}: {e}")
