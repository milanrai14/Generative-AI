from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_ollama import ChatOllama

#create model 
model = ChatOllama(
    model='llama3.2'
)

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

vector_store = Chroma.from_documents(
    documents=documents, 
    embedding=embeddings, 
    collection_name='multiquery'
)

#create a object of multi query retriver 
retriver = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(), 
    llm =model
)
query = "What is machine learning?"
results = retriver.invoke(query)

for i, doc in enumerate(results, start=1):
    print(f"\nDocument {i}:")
    print(doc.page_content)