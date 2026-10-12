from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_core.retrievers.document_compressors import LLMChainExtractor

#Create embeddings
embeddings = OllamaEmbeddings(
    model="llama3.2"
)

#Create a document
documents = [
    Document(
        page_content=(
            "Machine learning learns patterns from data. "
            "It is used to predict diseases and detect fraud. "
            "Python is a popular programming language."
        )
    ),
    Document(
        page_content=(
            "Deep learning uses neural networks with multiple layers. "
            "It is useful for image recognition and speech processing."
        )
    ),
    Document(
        page_content=(
            "Football is played by two teams. "
            "Each team tries to score goals."
        )
    ),
]
