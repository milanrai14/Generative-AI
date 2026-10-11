
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

# 1. Create an embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# 2. Create documents
documents = [
    Document(
        page_content="Python is used for machine learning.",
        metadata={"topic": "Python"}
    ),
    Document(
        page_content="CNNs are used for image classification.",
        metadata={"topic": "Deep Learning"}
    ),
    Document(
        page_content="RAG retrieves relevant information for LLMs.",
        metadata={"topic": "Generative AI"}
    )
]

# 3. Create the Chroma vector store
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="ai_notes",
    persist_directory="./chroma_db"
)

# 4. Search for relevant documents
results = vector_store.similarity_search(
    query="How does AI recognize images?",
    k=2
)

# 5. Print the results
for doc in results:
    print("Content:", doc.page_content)
    print("Metadata:", doc.metadata)
    print("-" * 40)
