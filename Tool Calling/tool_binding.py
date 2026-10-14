from langchain_ollama import ChatOllama
from langchain_core.tools import tool 
from langchain_core.messages import HumanMessage

import requests

# tool create 

@tool
def mulitply(a: int, b:int)-> int: 
    """Given 2 numbers a and b this tool returns their product"""
    return a * b


#tool binding
llm = ChatOllama(
    model='qwen2.5:3b', 
    temperature=0
)

llm_with_tools =llm.bind_tools([mulitply])


# result = llm_with_tools.invoke("Hi how are you")
result = llm_with_tools.invoke("Can you multiply 3 with 10")
print("content: ", result.content)
print("Tool calls: ", result.tool_calls)