import os
import time
from PIL import Image
from doctr.io import DocumentFile
from doctr.models import ocr_predictor
from transformers import AutoModel
from save_chromadb import add_text_image_data

# Initialize Models
ocr_model = ocr_predictor(pretrained=True)
embedding_model = AutoModel.from_pretrained('jinaai/jina-clip-v1', trust_remote_code=True)

# Directories and Files
SCREENSHOT_DIR = 'screenshots'
DATA_FILE = 'data.txt'
PROCESSED_FILE_LIST = 'processed_files.txt'  # File to keep track of processed screenshots
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def get_processed_files():
    """Reads the processed filenames from a file and returns a set of these filenames."""
    if not os.path.exists(PROCESSED_FILE_LIST):
        return set()
    with open(PROCESSED_FILE_LIST, 'r') as f:
        processed_files = set(line.strip() for line in f)
    return processed_files

def save_processed_file(filename):
    """Saves a new processed filename to the processed file list."""
    with open(PROCESSED_FILE_LIST, 'a') as f:
        f.write(f"{filename}\n")

def process_screenshot(image_path):
    """Processes a single screenshot: performs OCR, generates embeddings, and saves results."""
    # OCR
    doc = DocumentFile.from_images(image_path)
    result = ocr_model(doc)
    extracted_text = " ".join([word.value for page in result.pages for block in page.blocks for line in block.lines for word in line.words])
    print(f"Extracted text: {extracted_text}")

    # Embeddings (Assuming encode_text and encode_image are methods available for embedding_model)
    image = Image.open(image_path)
    text_embeddings = embedding_model.encode_text([extracted_text])
    image_embeddings = embedding_model.encode_image([image])

    # Save to Chroma
    add_text_image_data(image_path, text_embeddings, image_embeddings, extracted_text)

    # Save text (Optional)
    with open(DATA_FILE, 'a') as f:
        f.write(f"{image_path}\t{extracted_text.strip()}\n")

    # Mark the file as processed
    save_processed_file(image_path)

def capture_analyze_and_embed():
    """Captures a screenshot, performs OCR, generates embeddings, and saves results."""
    processed_files = get_processed_files()
    for filename in os.listdir(SCREENSHOT_DIR):
        image_path = os.path.join(SCREENSHOT_DIR, filename)
        if filename.endswith(".png") and os.path.isfile(image_path) and image_path not in processed_files:
            process_screenshot(image_path)

if __name__ == "__main__":
    while True:
        capture_analyze_and_embed()
        time.sleep(10)  # Sleep a bit before re-checking the directory
