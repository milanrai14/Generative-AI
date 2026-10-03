from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document = [
    "Nepal lies in the sout asia.", 
    "Mount everest also lies in Nepal", 
    "Paris is the capital city of France."
]

vector = embedding.embed_documents(document)

print(str(vector))