from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

#Createing a embeddings model 
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Create a sample documents 
documents = [
    Document(page_content="Machine learning learns patterns from data."),
    Document(page_content="ML algorithms identify patterns in datasets"), 
    Document(page_content="Deep learning use neural networks with multiple layers"), 
    Document(page_content="Python is widely used for programming.")
]

#Sore documents in chroma 
vector_store = Chroma.from_documents(
    embedding=embeddings, 
    documents=documents, 
    collection_name="mmr_example"
)

# create an MMR retriever
retriver = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs = {
        "k":3, 
        "fetch_k":5, 
        "lambda_mult":0.5
    }
)
