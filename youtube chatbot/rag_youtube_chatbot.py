from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate

#indexing
video_id = "LPZh9BOjkQs"

try:
    transcript_list = YouTubeTranscriptApi.fetch(video_id, langauages=['en'])

    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print(transcript)
except TranscriptsDisabled: 
    print("No captione avainlabe for this video")