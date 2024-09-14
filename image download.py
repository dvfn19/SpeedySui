import pandas as pd
from src.utils import download_images

# Load the test dataset
test_df = pd.read_csv('dataset/test.csv')

# Extract the image links
image_links = test_df['image_link'].tolist()

# Set the folder where images will be saved
download_folder = 'downloaded_images'

# Download images
download_images(image_links, download_folder)
