from langchain_ollama import ChatOllama
from langchain_community.tools import tool 
from langchain_core.messages import HumanMessage
import requests

# tool create 

@tool
def mulitply(a: int, b:int)-> int: 
    """Given 2 numbers a and b this tool returns their product"""
    return a * b


#tool binding
llm = ChatOllama(
    model='llama3.2'
)

llm_with_tools =llm.bind_tools([mulitply])
