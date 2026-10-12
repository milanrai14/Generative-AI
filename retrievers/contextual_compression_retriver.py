from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor

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

#Create a vector store
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="compression_demo"
)

#create a base retriever
base_retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

#Create a LLM
llm = ChatOllama(model="llama3.2", temperature=0)

#Create the compressor
compressor = LLMChainExtractor.from_llm(llm)


#Create the compression retriever
retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

#Retrieve compressed documents
query = "What are the applications of machine learning?"
results = retriever.invoke(query)

#Display the result
for i, doc in enumerate(results, start=1):
    print(f"\nDocument {i}:")
    print(doc.page_content)