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
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="ai_notes",
    persist_directory="./chroma_db"
)

#Convert vectorstoe into a retriver
retriver = vector_store.as_retriever(search_kwargs={"k":2})

query = "What is Chroma used for"

result = retriver.invoke(query)
# for res in result:
#     print(res)
result = vector_store.similarity_search(query, k=2)

for res in result:
    print(res)