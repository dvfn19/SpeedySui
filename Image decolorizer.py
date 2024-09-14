from PIL import Image
import os

from z import download_folder


def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))  # Resize to a standard size
    img = img.convert('RGB')  # Ensure it's in RGB format
    return img

# Preprocess all images
processed_images = []
for filename in os.listdir(download_folder):
    image_path = os.path.join(download_folder, filename)
    processed_images.append(preprocess_image(image_path))
