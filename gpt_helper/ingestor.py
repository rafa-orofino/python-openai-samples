"""ChromaDB ingestion utilities: manage collections and documents."""
import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

embedding_fn_ = OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-small"
)

client = chromadb.Client()
COLLECTION_NAME = "my_docs"

def create_collection() -> chromadb.Collection:
    """Create a new collection in the ChromaDB client."""
    if COLLECTION_NAME in [collection.name for collection in client.list_collections()]:
        client.delete_collection(COLLECTION_NAME)
    return client.create_collection(COLLECTION_NAME, embedding_function=embedding_fn_)

def load_document(name: str, content: str):
    """Load a text document into the ChromaDB collection, splitting into fixed-size chunks."""
    collection = create_collection()
    # Simple chunking by 500 characters
    chunks = [content[i:i+500] for i in range(0, len(content), 500)]

    collection.add(
        documents=chunks,
        ids=[f"{name}_{i}" for i in range(len(chunks))]
    )

    print(f"✅ Document '{name}' indexed into {len(chunks)} chunks.")

def query_by_similarity(query: str, n_results: int = 3):
    """Query the collection by similarity."""
    collection = client.get_or_create_collection(COLLECTION_NAME, embedding_function=embedding_fn_)
    results = collection.query(query_texts=[query], n_results=n_results)
    return results["documents"][0] if results["documents"] else []