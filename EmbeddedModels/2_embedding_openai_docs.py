from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
document = [
    "Nepal lies in the sout asia.", 
    "Mount everest also lies in Nepal", 
    "Paris is the capital city of France."
]

result = embedding.embed_documents(document)

print(str(result))