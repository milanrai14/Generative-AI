from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

message_model = ChatOllama(
    model='llama3.2'
)
