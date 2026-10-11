from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

docs = retriever.invoke("Neural networks")

for doc in docs: 
    print(doc.page_content)
    print("\n")