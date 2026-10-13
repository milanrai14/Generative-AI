from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


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
# print(retriver)

question = "Explain the transformer architecture."
question = "Explain neuclear bomb."
result = retriver.invoke(question)
# print(len(result))
# print(result[0].page_content)


#agumentation
# merging retriver and query

llm = ChatOllama(
    model="llama3.2",
    temperature=0.2
)

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer Only from the provied transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}

    """,
    input_variables=['context', 'question']
)

# question = "What is LLM?"
retrived_docs = retriver.invoke(question)

# print(retrived_docs)

#Connatination
context_text= "\n\n".join(doc.page_content for doc in retrived_docs)
# print(context_text)
final_prompt = prompt.invoke({"context": context_text, "question": question})

# print(final_prompt)
#Generation

answer = llm.invoke(final_prompt)
print(answer.content)

# Building a chain
def format_docs(retrieved_docs): 
    context_text= "\n\n".join(doc.page_content for doc in retrived_docs)
    return context_text

parallel_chain = RunnableParallel({
    'context': retriver | RunnableLambda(format_docs),
    'question': RunnablePassthrough()

})

parallel_chain.invoke("Who is Milan")

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

result = main_chain.invoke("Can you summarize the video?")
print(result)