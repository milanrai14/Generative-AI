from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    path='documents', 
    glob= '*.txt', 
    loader_cls=TextLoader
)

docs = loader.load()
print(len(docs))