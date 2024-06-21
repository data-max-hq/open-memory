from transformers import AutoModel, AutoModelForSequenceClassification, AutoTokenizer
import torch
import chromadb
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings

# Load CLIP model and tokenizer for text embedding
model_id = "jinaai/jina-clip-v1"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
embedding_model = AutoModel.from_pretrained(model_id, trust_remote_code=True)

# Load the reranker model
reranker_model = AutoModelForSequenceClassification.from_pretrained('jinaai/jina-reranker-v1-turbo-en', num_labels=1, trust_remote_code=True)
reranker_tokenizer = AutoTokenizer.from_pretrained('jinaai/jina-reranker-v1-turbo-en', trust_remote_code=True)

class QueryRAG:
    def __init__(self):
        # Initialize ChromaDB Persistent Client
        CHROMA_PATH = "chroma"
        self.client = chromadb.PersistentClient(
            path=CHROMA_PATH,
        )
        self.text_collection = self.client.get_collection("texts")
        self.image_collection = self.client.get_collection("images")
    
    def embed_text(self, texts):
        inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            embeddings = embedding_model.get_text_features(**inputs).cpu().numpy()
        return embeddings

    def query(self, query_text: str):
        # Embed the query text
        query_embeddings = self.embed_text([query_text])

        # Perform similarity search on text_collection
        text_results = self.text_collection.query(query_embeddings=query_embeddings, n_results=10)

        if 'documents' in text_results and len(text_results['documents'][0]) > 0:
            # Extract context texts and sources
            most_relevant_documents = [str(doc) for doc in text_results['documents'][0]]
            sources = [source for source in text_results['ids'][0]]

            # Construct sentence pairs
            sentence_pairs = [[query_text, context_text] for context_text in most_relevant_documents]

            # Tokenize and encode sentence pairs for reranking
            reranker_inputs = reranker_tokenizer(sentence_pairs, padding=True, truncation=True, return_tensors='pt')
            with torch.no_grad():
                outputs = reranker_model(**reranker_inputs)
            scores = outputs.logits.squeeze(-1).cpu().numpy()

            # Rank the documents by their reranker scores
            ranked_indices = scores.argsort()[::-1][:3]  # Get indices of the top 3 scores
            top_documents = [most_relevant_documents[idx] for idx in ranked_indices]
            top_sources = [sources[idx] for idx in ranked_indices]

            formatted_responses = [(top_documents[i], top_sources[i]) for i in range(3)]
        else:
            formatted_responses = [("No relevant documents found.", "")]

        return formatted_responses
    
def get_contexts(query_text: str):
    query_rag = QueryRAG()
    results = query_rag.query(query_text)
    contexts = [result[0] for result in results if result[0] != "No relevant documents found."]
    return contexts

def main():
    query_rag = QueryRAG()
    query_text = input("Enter your question: ")
    results = query_rag.query(query_text)
    for result in results:
        print(f"Most relevant content: {result[0]}\nMost relevant source: {result[1]}\n")

if __name__ == "__main__":
    main()
