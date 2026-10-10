from langchain_community.document_loaders import WebBaseLoader

url = "https://forestaction.org/iconic-latahar-tree/"

loader = WebBaseLoader(url)

docs = loader.load()


print(len(docs))

for doc in docs: 
    print(doc.page_content)