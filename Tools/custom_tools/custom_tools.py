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

result = multiply.invoke({'a': 3, 'b': 4})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)

#LLM sees this
final_result_llm_see = multiply.args_schema.model_json_schema()
print("*" * 50)
print(final_result_llm_see)