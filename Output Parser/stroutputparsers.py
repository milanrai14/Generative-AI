from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(
    model='llama3.2'
)

#1st prompt -> detailed report

#2nd prompt -> summary
