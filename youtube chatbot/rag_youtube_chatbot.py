from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate

##indexing
#Document downloading
video_id = "LPZh9BOjkQs"

try:
    transcript_list = YouTubeTranscriptApi().fetch(video_id, languages=['en'])
    # print(transcript_list)
    print("*" *100)
    transcript = " ".join(chunk.text for chunk in transcript_list)
    # print(transcript)
    # print(type(transcript))
except TranscriptsDisabled: 
    print("No captione avainlabe for this video")

#text spliting
spliter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap =200
)
chunks = spliter.create_documents([transcript])

#embeddings 
embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

#vector store
vector_store = Chroma.from_documents(chunks, embedding)
# data = vector_store.get(include=["documents", "embeddings", "metadatas"])

# print("Documents:")
# print(data["documents"])

# print("\nEmbeddings:")
# print(data["embeddings"])

# print("\nMetadata:")
# print(data["metadatas"])

#Retriver
retriver = vector_store.as_retriever(search_type="similarity",search_kwargs={"k":4})
print(retriver)

query = "Explain transformer architecture."
result = retriver.invoke(query)
# print(len(result))
# print(result[0].page_content)


#agumentation
# merging retriver and query

lmm = ChatOllama(
    model="llama3.2",
    temperature=0.2
)