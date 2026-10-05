from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


model = ChatOllama(
    model='llama3.2'
)

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}', 
    input_variables=['topic']
)