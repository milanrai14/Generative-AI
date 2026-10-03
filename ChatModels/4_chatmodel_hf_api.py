import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print("Token loaded:", token is not None)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke(
    "What is the capital city of Nepal?"
)

print(result.content)