from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

text = docs[0].page_content
