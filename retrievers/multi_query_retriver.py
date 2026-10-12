from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_classic.retrievers import MultiQueryRetriever

#Createing a embeddings model 
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Create a sample documents 
documents = [
    Document(page_content="Machine learning learns patterns from data."),
    Document(page_content="ML algorithms identify patterns in datasets"), 
    Document(page_content="Deep learning use neural networks with multiple layers"), 
    Document(page_content="Machine learning is a subset of artificial intelligence."),
    Document(page_content="Python is widely used for programming.")
]
