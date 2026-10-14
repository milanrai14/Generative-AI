from langchain_core.tools import tool

#Custome tools
@tool
def add(a:int, b:int)->int:
    """Add two numbers"""
    return a + b
    