from langchain_core.tools import tool

#step - Create a function 
def multiply(a,b): 
    """Multiply two number"""
    return a*b


#add type hints
def multiply(a: int, b: int) -> int: 
    """Multiply two numbers"""
    return a*b 

ass 