from langchain_core.tools import tool

#step 1 - Create a function 
def multiply(a,b): 
    """Multiply two number"""
    return a*b


#step 2- add type hints
def multiply(a: int, b: int) -> int: 
    """Multiply two numbers"""
    return a*b 

#step 3 - add tool decorators 
@tool
def multiply(a: int, b: int) -> int: 
    """Multiply two numbers"""
    return a*b

