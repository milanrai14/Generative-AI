from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document


#Creating a own source documents 
documents = [
    Document(page_content="LangChain helps developers build LLM application easily."), 
    Document(page_content="Chroma is a vector database optimized for LLM-based search"), 
    Document(page_content='OpenAI provides prowerfull embedding models.')
]

#initilize the embeddings model 
embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

