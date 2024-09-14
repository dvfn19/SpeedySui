import os
import requests
from paddleocr import PaddleOCR
from PIL import Image
from io import BytesIO

# Initialize the PaddleOCR model
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # You can change 'lang' based on your needs

def download_images(image_urls, download_folder):
    """
    Download images from the provided URLs and perform OCR on them.

    Args:
        image_urls (list): List of image URLs.
        download_folder (str): Folder to save downloaded images.

    Returns:
        dict: A dictionary with image filenames as keys and extracted text as values.
    """
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    extracted_text = {}

    for url in image_urls:
        try:
            # Download the image
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses

            # Open the image
            img = Image.open(BytesIO(response.content))

            # Save the image
            filename = os.path.join(download_folder, url.split('/')[-1])
            img.save(filename)

            # Perform OCR
            result = ocr.ocr(filename, cls=True)

            # Process the results
            text = ''
            for line in result:
                for word_info in line:
                    text += word_info[1][0] + ' '  # Extract the text

            extracted_text[filename] = text.strip()  # Store the extracted text

        except Exception as e:
            print(f"Error downloading or processing {url}: {e}")

    return extracted_text


