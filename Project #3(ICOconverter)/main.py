import os
from PIL import Image


input_folder = "images"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# === Process Images ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        file_path = os.path.join(input_folder, filename)
        output_name = os.path.splitext(filename)[0] + ".ico"
        output_path = os.path.join(output_folder, output_name)

        try:
            image = Image.open(file_path)
            image.save(output_path, format="ICO")
            print(f"Processed and converted: {filename} → {output_name}")
        except Exception as e:
            print(f"Error with {filename}: {e}")

print("All done.")