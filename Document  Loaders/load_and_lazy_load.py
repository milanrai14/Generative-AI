from langchain_community.document_loaders import TextLoader


loader = TextLoader('football.txt', encoding='utf-8')

documents1 = loader.load()
documents2 = loader.lazy_load()

for doc in documents1: 
    print(doc.metadata)


for doc in documents2: 
    print(doc.metadata)