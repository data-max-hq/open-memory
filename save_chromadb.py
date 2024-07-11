import chromadb

# --- ChromaDB Persistent Setup ---
CHROMA_PATH = "chroma"
client = chromadb.PersistentClient(
    path=CHROMA_PATH
)
text_collection = client.get_or_create_collection("texts")
image_collection = client.get_or_create_collection("images")

def add_text_image_data(screenshot_name, text_embedding, image_embedding, extracted_text):
    """Adds text and image embeddings to their respective collections 
       with a common ID (screenshot_name).
    """
    
    text_collection.add(embeddings=text_embedding, ids=[screenshot_name], documents=extracted_text)
    image_collection.add(embeddings=image_embedding, ids=[screenshot_name])
    print(f"Processed and saved: {screenshot_name}")
    