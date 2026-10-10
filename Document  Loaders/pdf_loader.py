from langchain_community.document_loaders import PyPDFLoader



loader = PyPDFLoader('milan.pdf')

docs = loader.load()
print(len(docs))